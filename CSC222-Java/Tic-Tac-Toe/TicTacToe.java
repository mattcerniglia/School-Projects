/*Matthew Cerniglia
CSC222 Tic Tac Toe - Complete
This class keeps track of a Tic Tac Toe game using a 1D array with 9 spots (0 to 8), read left to right and top to bottom.
Each spot holds 0 if it is empty, 1 if player 1 (X) took it, or 2 if player 2 (O) took it.
The class checks if a move is allowed, places the move, checks the rows, columns, and diagonals for a winner, checks for a tie, and prints the board and the result.
*/
public class TicTacToe {

    //Class variable
    private int[] board;                       //variable to store the 9 spots of the board, used by every method to see who took which spot

    //The constructor creates the board, and every spot starts at 0 since all of the spots are empty.
    public TicTacToe() {
        board = new int[9];
    }

    //isValidMove checks that the position is on the board and that nobody has taken it yet.
    //It is a public boolean method so TicTacToeGame can call it, and it returns true or false (GeeksforGeeks, n.d.).
    public boolean isValidMove(int position) {

        //This section checks if the position is on the board (0 to 8), anything else is not a spot.
        if (position < 0 || position > 8) {
            return false;
        }

        //A spot is only open if it is still 0.
        return board[position] == 0;
    }

    //MakeMove places the player's number in the spot, and returns false if the move could not be made.
    public boolean MakeMove(int player, int position) {

        //This section checks that the player is 1 or 2, since those are the only two players.
        if (player != 1 && player != 2) {
            return false;
        }

        //This section checks the position using isValidMove so the same rules are not written twice.
        if (!isValidMove(position)) {
            return false;
        }

        //The move is good, so the player's number is saved in that spot.
        board[position] = player;
        return true;
    }

    //checkRows looks at the three rows (0-1-2, 3-4-5, 6-7-8) and returns true if the player has all three spots in one of them.
    //It is a private boolean method because only this class needs it, and private members cannot be used outside the class (GeeksforGeeks, n.d.).
    private boolean checkRows(int player) {

        //Loop variable
        int start;                             //variable to store the first spot of the row, used to find the other two spots in that row

        //The first spot of each row is 0, 3, and 6, so start goes up by 3 each time.
        for (start = 0; start <= 6; start += 3) {
            if (board[start] == player && board[start + 1] == player && board[start + 2] == player) {
                return true;
            }
        }
        return false;
    }

    //checkColumns looks at the three columns (0-3-6, 1-4-7, 2-5-8) and returns true if the player has all three spots in one of them.
    private boolean checkColumns(int player) {

        //Loop variable
        int start;                             //variable to store the top spot of the column, used to find the other two spots below it

        //The top spot of each column is 0, 1, and 2, and the spots below it are 3 and 6 more.
        for (start = 0; start <= 2; start++) {
            if (board[start] == player && board[start + 3] == player && board[start + 6] == player) {
                return true;
            }
        }
        return false;
    }

    //checkDiagonals looks at the two diagonals (0-4-8 and 2-4-6) and returns true if the player has all three spots in one of them.
    private boolean checkDiagonals(int player) {

        //This section checks the diagonal going from the top left to the bottom right.
        if (board[0] == player && board[4] == player && board[8] == player) {
            return true;
        }

        //This section checks the diagonal going from the top right to the bottom left.
        if (board[2] == player && board[4] == player && board[6] == player) {
            return true;
        }
        return false;
    }

    //checkWinner returns true if the player has three in a row anywhere on the board.
    public boolean checkWinner(int player) {
        return checkRows(player) || checkColumns(player) || checkDiagonals(player);
    }

    //isBoardFull returns true only for a tie, meaning every spot is taken and nobody has won.
    public boolean isBoardFull() {

        //Loop variable
        int i;                                 //variable to store the spot being checked, used to look for an empty spot

        //If someone won, the game is not a tie, so false is returned right away.
        if (checkWinner(1) || checkWinner(2)) {
            return false;
        }

        //This section goes through all 9 spots, and any empty spot means the board is not full yet.
        for (i = 0; i < board.length; i++) {
            if (board[i] == 0) {
                return false;
            }
        }
        return true;
    }

    //displayWinner prints the result of the game, a null name means nobody won.
    public void displayWinner(String winnerName) {
        if (winnerName == null) {
            System.out.println("Tie Game");
        } else {
            System.out.println("Congratulations, " + winnerName + "!");
        }
    }

    //displayBoard prints the board as a 3 by 3 grid, with X and O for the moves and the spot number for the empty spots.
    public void displayBoard() {

        //Loop variables
        int row;                               //variable to store the row number, used by the outer loop to move down the board
        int col;                               //variable to store the column number, used by the nested loop to move across the row
        int index;                             //variable to store the spot in the board array, found from the row and column
        String symbol;                         //variable to store what is printed in the spot (X, O, or the spot number)

        //This is here to leave a blank line before the board, making it easier to read.
        System.out.println();

        //This section prints each row of the board. The outer loop goes through each row and the nested loop goes through each column of that row.
        for (row = 0; row < 3; row++) {
            for (col = 0; col < 3; col++) {

                //Each row has 3 spots, so row * 3 + col gives the spot in the 1D array.
                index = row * 3 + col;

                //1 is X, 2 is O, and an empty spot shows its number so the player knows what to type.
                if (board[index] == 1) {
                    symbol = "X";
                } else if (board[index] == 2) {
                    symbol = "O";
                } else {
                    symbol = String.valueOf(index);
                }

                //The spot is printed with a | after it, except for the last spot in the row.
                System.out.print(" " + symbol + " ");
                if (col < 2) {
                    System.out.print("|");
                }
            }
            System.out.println();

            //A line is printed between the rows, but not after the last row.
            if (row < 2) {
                System.out.println("---+---+---");
            }
        }
        System.out.println();
    }
}

/*References
GeeksforGeeks. (n.d.). Access modifiers in Java. Retrieved November 8, 2026, from
https://www.geeksforgeeks.org/access-modifiers-in-java/
*/
