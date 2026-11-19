/*Matthew Cerniglia
CSC222 Throw and Catch - Complete
This application is akin to a "signup" gathering information.
It is intentionally coded wrong: the country is read as an int without telling the user a number is expected, so entering a country name creates an exception.
The exception is then caught and its error message is displayed, and the country is read again as a String.
*/
import java.util.InputMismatchException;
import java.util.Scanner;

public class ThrowAndCatch {

    //Main asks for the name, age, and country, catches the exception caused by the country being read as an int, and then reads it again as a String.
    public static void main(String[] args) {

        //Input variables
        Scanner input;                         //variable to store the Scanner object, used to read the name, age, and country from the user
        String name;                           //variable to store the name, used to thank the user once the signup is complete
        int age;                               //variable to store the age, read as an int since an age is a number
        String country;                        //variable to store the country, read as a String in the catch block after the int attempt fails

        //This section creates the Scanner used for all of the input below, and it is closed once the input is finished.
        input = new Scanner(System.in);

        //This section asks for the name before the try block, since a String can never cause the exception.
        System.out.println("Please enter your name: ");
        name = input.nextLine();

        //This section runs the rest of the signup, with the mistake in it on purpose (GeeksforGeeks, n.d.).
        //The country prompt does not mention a number, but nextInt() expects one, so a country name like "Canada" throws an InputMismatchException.
        try {
            System.out.println("Please enter your age: ");
            age = input.nextInt();
            input.nextLine();
            System.out.println("Please enter your country: ");
            country = String.valueOf(input.nextInt());
            input.nextLine();
            System.out.println("Thank you for signing up, " + name + "!");
        } catch (InputMismatchException e) {
            //This section handles the exception using the catch block (W3Schools, n.d.).
            //The bad input is still waiting in the Scanner, so nextLine() is used to remove it before reading again.
            input.nextLine();
            System.out.println("Error: " + e);

            //The country is read again, this time as a String so the input matches what the user types.
            //The name and age were already read before the exception, so only the country is asked for again.
            System.out.println("Please enter your country: ");
            country = input.nextLine();
            System.out.println("Thank you for signing up, " + name + "!");
        }

        //This section closes the Scanner now that the input is finished.
        input.close();
    }
}

/*
References
GeeksforGeeks. (n.d.). Java exception handling. https://www.geeksforgeeks.org/java/exceptions-in-java/

W3Schools. (n.d.). Java try...catch. https://www.w3schools.com/java/java_try_catch.asp
*/
