/*Matthew Cerniglia
CSC222 Math Class - Complete
There are two parts to this program, the first finding circle properties: area, circumference, and diameter.
It is using Math.PI as the constant for π. The second part finds the expected value of an investment using the exponential growth model.
It uses Math.E as the constant to represent the base of the natural logarithm.*/
public class pi_and_e {
    //This is the main function. It finds the area, circumference, and diameter of a circle using the radius,
    //then finds the expected value of an investment using the exponential growth model.
    public static void main(String[] args) {

        //Part A variables
        final int radius = 14;                //variable to store the radius in feet, used in every circle calculation and kept as an int since it is a whole number
        double area;                          //variable to store the area of the circle, used to display the result
        double circumference;                 //variable to store the circumference of the circle, used to display the result
        int diameter;                         //variable to store the diameter of the circle, used to display the result

        //Part B variables
        final double initialInvestment = 1000;   //variable to store the starting money (P), used as the amount that grows over time
        final double eulersNumber = Math.E;      //variable to store the value of e from Math.E, used as the base of the growth. Source: (Oracle, n.d.)
        final double growthRate = 0.03;          //variable to store the growth rate of 3% (r), used to set how fast the investment grows
        final double years = 6.85;               //variable to store the number of years (t), used to set how long the investment grows
        double expectedValue;                    //variable to store the value of the investment after the years, used to display the result

        /*Part A - PI
        This section finds the area, circumference, and diameter of a circle with a radius of 14 feet.
        Math.PI is the ratio of a circle's circumference to its diameter, approximately 3.14159.*/

        //Displaying what will be calculated, as well as the radius being used.
        System.out.println("Determining the area, circumference, and diameter of a circle with a radius of " + radius + "ft.");

        //This section finds the area of the circle and displays it. Source: (Arora, 2021)
        //Using Math.PI in A = πr^2, saved as a double since pi has decimal values and so can the area.
        area = Math.PI * radius * radius;
        System.out.println("Area: " + area + "ft^2");

        //This section finds the circumference of the circle and displays it. Source: (Arora, 2021)
        //Using Math.PI in C = 2πr, saved as a double for the same reason as the area.
        circumference = 2 * Math.PI * radius;
        System.out.println("Circumference: " + circumference + "ft");

        //This section finds the diameter of the circle and displays it.
        //Using only the radius in D = 2r since Math.PI is not needed, saved as an int since a whole number times 2 stays whole.
        diameter = 2 * radius;
        System.out.println("Diameter: " + diameter + "ft");

        //This section separates Part A from Part B, since the two parts are unrelated to each other.
        System.out.println("--------------------------------------------------");
        System.out.println("--------------------------------------------------");

        /*Part B - Exponential Growth Model
        This section finds the expected value of an investment after a number of years using the exponential growth model.
        The model is A = Pe^(rt), where e is approximately 2.71828 and is used to express exponential growth or decay.
        */

        //Displaying what will be calculated, as well as the initial investment, number of years, and growth rate being used.
        //Each starting value is saved as a double so any decimal values carry through to the expected value.
        System.out.println("Finding the expected value of " + initialInvestment + " after " + years + " years at a rate of " + growthRate*100 + "%.");

        //This section finds the expected value of the investment and displays it.
        //Using A = Pe^(rt) with Math.pow(), where eulersNumber is the value of e and the exponent is the growth rate times the years. Source: (Oracle, n.d.)
        expectedValue = initialInvestment * Math.pow(eulersNumber, growthRate * years);
        System.out.println("Expected Value: " + expectedValue);

    }
}

/*References
Arora, L. (2021, July 2). Pi constant in Java. Delft Stack. https://www.delftstack.com/howto/java/pi-in-java/
Oracle. (n.d.). Math (Java Platform SE 8). Java SE Documentation. https://docs.oracle.com/javase/8/docs/api/java/lang/Math.html
*/
