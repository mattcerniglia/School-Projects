/*Matthew Cerniglia
CSC222 Tic Tac Toe Game - Complete
This program plays a two player game of Tic Tac Toe in the console, using the TicTacToe class to keep track of the board.
Initially, the program asks for the names of both players and shows the board with the squares numbered 0 to 8.
After that, the players take turns entering the number of the square they want, and the program checks each move.
The game ends when a player gets three in a row or the board is full, then the program prints the winner or a tie.
*/
import java.util.Scanner;

public class TicTacToeGame {

    //Main asks for the player names, runs the turns until someone wins or the board is full, and prints the result.
    public static void main(String[] args) {

        //Input variables
        Scanner input;                         //variable to store the Scanner object, used to read the names and the squares from the players
        String player1;                        //variable to store the name of player 1 (X), used to ask for their turn and to show the winner
        String player2;                        //variable to store the name of player 2 (O), used to ask for their turn and to show the winner
        int square;                            //variable to store the square the current player picked, used to make the move

        //Game variables
        TicTacToe game;                        //variable to store the TicTacToe object, used to make the moves and check the board
        int currentPlayer;                     //variable to store whose turn it is (1 or 2), used when making a move
        String currentName;                    //variable to store the name of the current player, used in the prompt
        String winner;                         //variable to store the name of the winner, stays null if the game is a tie
        boolean gameOver;                      //variable to store if the game has ended, used to stop the loop

        //This section creates the Scanner and the game, and it is closed at the end once the input is finished.
        //The TicTacToe class is used by creating an object with new, then calling its methods on that object (W3Schools, n.d.).
        input = new Scanner(System.in);
        game = new TicTacToe();

        //This section welcomes the players and reads both names as Strings.
        System.out.println("Welcome to Tic-Tac-Toe!");
        System.out.print("Enter the name of Player 1: ");
        player1 = input.nextLine();
        System.out.print("Enter the name of Player 2: ");
        player2 = input.nextLine();

        //This section shows the empty board so the players know which number is which square.
        System.out.println("Squares are numbered 0 (top left) to 8 (bottom right).");
        game.displayBoard();

        //Player 1 goes first, and there is no winner until someone gets three in a row.
        currentPlayer = 1;
        winner = null;
        gameOver = false;

        //This section runs the turns, one loop for each square entered, until the game is over.
        while (!gameOver) {

            //The name is picked from the current player so the right person is asked.
            if (currentPlayer == 1) {
                currentName = player1;
            } else {
                currentName = player2;
            }
            System.out.print(currentName + ", enter the number of the square you want to play (0-8): ");

            //This section checks that a number was typed, because nextInt() would throw an exception on letters, and hasNextInt() can test this first (GeeksforGeeks, n.d.).
            //The bad input is still waiting in the Scanner, so next() is used to remove it before asking again.
            if (!input.hasNextInt()) {
                System.out.println("That is not a number. Try again.");
                input.next();
                continue;
            }
            square = input.nextInt();

            //This section checks that the square is on the board and not taken yet, and the same player goes again if not.
            if (!game.isValidMove(square)) {
                System.out.println("Invalid move. Try again.");
                continue;
            }

            //The move is good, so it is made and the new board is shown.
            game.MakeMove(currentPlayer, square);
            game.displayBoard();

            //This section checks if the move won the game or filled the board, and if not it is the other player's turn.
            if (game.checkWinner(currentPlayer)) {
                winner = currentName;
                gameOver = true;
            } else if (game.isBoardFull()) {
                gameOver = true;
            } else if (currentPlayer == 1) {
                currentPlayer = 2;
            } else {
                currentPlayer = 1;
            }
        }

        //This section prints the result, winner stays null for a tie so displayWinner prints "Tie Game".
        game.displayWinner(winner);

        //This section closes the Scanner now that the input is finished.
        input.close();
    }
}

/*References
GeeksforGeeks. (n.d.). Scanner hasNextInt() method in Java with examples. Retrieved November 8, 2026, from
https://www.geeksforgeeks.org/scanner-hasnextint-method-in-java-with-examples/

W3Schools. (n.d.). Java classes and objects. Retrieved November 8, 2026, from
https://www.w3schools.com/java/java_classes.asp
*/
