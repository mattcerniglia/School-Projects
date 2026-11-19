/*Matthew Cerniglia
CSC222 Two-D Array - Complete
This program creates a 2D array sized by user request.
Initially, the program asks for the number of rows and columns from the user, then creates the array using those dimensions.
After being created, using the Random class, the array is filled with random numbers between 1 and 10.
Finally, the program prints the array to the console.
*/
import java.util.Scanner;
import java.util.Random;

public class TwoDArray {

    //Main asks for the size of the array, checks it, fills the array with random numbers, and prints it.
    public static void main(String[] args) {

        //Input variables
        Scanner sc;                            //variable to store the Scanner object, used to read the rows and columns from the user
        int rows;                              //variable to store the number of rows, used to size the array and run the loops
        int cols;                              //variable to store the number of columns, used to size the array and run the loops

        //Array variables
        int[][] arr;                           //variable to store the 2D array, used to hold the random numbers and print them
        Random rand;                           //variable to store the Random object, used to generate the numbers that fill the array
        int i;                                 //variable to store the row index, used by the outer loops to move through each row
        int j;                                 //variable to store the column index, used by the nested loops to move through each column

        //This section asks the user for the number of rows and columns in the 2D array.
        //Both values are read as ints using the Scanner, which is closed once the input is finished.
        System.out.println("Enter the number of rows?");
        sc = new Scanner(System.in);
        rows = sc.nextInt();
        System.out.println("Enter the number of columns?");
        cols = sc.nextInt();
        sc.close();

        //This section checks if the user input for rows and columns is valid (greater than 0).
        //The program exits with a status code of 1, which indicates an error, if either value is 0 or negative.
        if (rows <= 0 || cols <= 0) {
            System.out.println("Invalid input. Please enter a positive integer.");
            System.exit(1);
        }

        //This section creates the 2D array using the number of rows and columns from the user (GeeksforGeeks, n.d.).
        //It is created after the check so a negative size is never used.
        arr = new int[rows][cols];

        //This section fills the 2D array with random numbers between 1 and 10.
        //The outer loop goes through each row and the nested loop goes through each column of that row (W3Schools, n.d.).
        //nextInt(10) gives 0 to 9, so 1 is added to bring it into the range of [1, 10].
        rand = new Random();
        for (i = 0; i < rows; i++) {
            for (j = 0; j < cols; j++) {
                arr[i][j] = rand.nextInt(10) + 1;
            }
        }

        //This is here to seperate the input from the output, making it easier to read,  showing that the array is being printed.
        System.out.println("The 2D array is:");


        //This section prints the 2D array to the console.
        //Each element is printed followed by a space, then a new line is printed after each row for clarity (W3Schools, n.d.).
        for (i = 0; i < rows; i++) {
            for (j = 0; j < cols; j++) {
                System.out.print(arr[i][j] + " ");
            }
            System.out.println();
        }
    }
}

/*
References
GeeksforGeeks. (n.d.). Multidimensional arrays in Java. https://www.geeksforgeeks.org/java/multidimensional-arrays-in-java/

W3Schools. (n.d.). Java arrays. https://www.w3schools.com/java/java_arrays.asp
*/
