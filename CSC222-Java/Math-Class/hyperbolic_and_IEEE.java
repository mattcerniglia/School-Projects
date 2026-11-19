/*Matthew Cerniglia
CSC222 Math Class - Complete
This program is using Math.IEEEremainder to find the remainder after full circles have been completed to find the end angle of the sprinkler head.
Further using arc functions to verify the angle and the values of cos, sin, and tan, then finding the hyperbolic values sinh, cosh, and tanh.
*/
public class hyperbolic_and_IEEE {

    //Main runs the sprinkler word problem, finds the final angle, verifies it using trig and inverse trig functions, then finds the hyperbolic functions.
    public static void main(String[] args) {

        //Word problem variables
        final int clicks = 27;                 //how many clicks the sprinkler head has turned
        final int degreesPerClick = 37;        //how many degrees the sprinkler head moves each click
        int totalDegrees;                      //total degrees turned before, used to find the angle after taking out the full circles
        double backInCircle;                   //the angle after taking out the full circles, used in every calculation after it

        //Trig variables
        double angleInRadians;                 //variable to store the angle in radians so the Math functions can use it
        double cosValue;                       //variable to store the cos of the angle, used later to check things
        double sinValue;                       //variable to store the sin of the angle, used later to check things
        double tanValue;                       //variable to store the tan of the angle, used later to check things

        //Verification variables
        double tanFromSinCos;                  //variable to store tan found by dividing sin by cos, to compare with tanValue
        double checkFor1;                      //variable to store sin^2 + cos^2, which should come out to 1
        double angleFromCos;                   //variable to store the angle in degrees found from the cos
        double angleFromSin;                   //variable to store the angle in degrees found from the sin
        double angleFromTan;                   //variable to store the angle in degrees found from the tan
        double recovered;                      //variable to store the full angle in degrees found from sin and cos

        //Hyperbolic variables
        double sinhValue;                      //variable to store the hyperbolic sin of the angle in radians
        double coshValue;                      //variable to store the hyperbolic cos of the angle in radians
        double tanhValue;                      //variable to store the hyperbolic tan of the angle in radians
        double tanhFromSinhCosh;               //variable to store tanh found by dividing sinh by cosh, to compare with tanhValue
        double checkHyperbolic;                //variable to store cosh^2 - sinh^2, which should come out to 1

        //This section prints out the word problem, using the number of clicks and degrees per click.
        //I am learning about these same properties in precalc, making a word problem helped the concept be realistic.
        System.out.println("Word Problem to draw figures from: A sprinkler head starting at 0 degrees rotates counterclockwise at a rate of " + degreesPerClick + " degrees per click.");
        System.out.println("After " + clicks + " clicks, what is the angle of the sprinkler head?");

        System.out.println("--------------------------------");

        //This section finds the total degrees the sprinkler head turned and puts it back into one circle (0 to 360). Source: (GeeksforGeeks, 2025)
        //IEEEremainder can return a negative value, so 360 is added in the next step when that happens.
        totalDegrees = clicks * degreesPerClick;
        backInCircle = Math.IEEEremainder(totalDegrees, 360);

        //Ensuring that if the angle is negative, we add 360 to bring it back into the range of [0, 360).
        if (backInCircle < 0) {
            backInCircle += 360;
        }

        //Begining of the solution verification, displaying the angle of the sprinkler head after cycle is completed.
        System.out.println("The angle of the sprinkler head after " + clicks + " clicks is: " + backInCircle + " degrees.");

        System.out.println("--------------------------------");

        //This section changes the angle to radians and finds the cos, sin, and tan of it. Source: (GeeksforGeeks, 2019; JavaSpring.net, 2026)
        //The values are saved in variables so the verification sections below can reuse them.
        System.out.println("Finding cos, sin, and tan of the angle:");
        angleInRadians = Math.toRadians(backInCircle);
        cosValue = Math.cos(angleInRadians);
        sinValue = Math.sin(angleInRadians);
        tanValue = Math.tan(angleInRadians);

        //Displaying the cos, sin, and tan values for the angle.
        System.out.println("cos(" + backInCircle + " degrees) = " + cosValue);
        System.out.println("sin(" + backInCircle + " degrees) = " + sinValue);
        System.out.println("tan(" + backInCircle + " degrees) = " + tanValue);

        System.out.println("--------------------------------");

        //This section checks the cos, sin, and tan values using tan = sin / cos and sin^2 + cos^2 = 1.
        System.out.println("Using relation between sin, cos, and tan to verify the angle:");

        //Tan can be expressed as a ratio between sin and cos: tan(θ) = sin(θ) / cos(θ).
        tanFromSinCos = sinValue / cosValue;

        //To verify that the equation is correct, absolute value of subtracting the original from the calculated tan values is taken.
        System.out.println("tan(" + backInCircle + " degrees) = sin(" + backInCircle + " degrees) / cos(" + backInCircle + " degrees) = " + tanFromSinCos);
        System.out.println("sin/cos matches tan? " + (Math.abs(tanFromSinCos - tanValue) < 1e-9));

        //sin^2 + cos^2 should equal 1, which is a fundamental identity in trigonometry.
        checkFor1 = sinValue * sinValue + cosValue * cosValue;

        //Here is the displayed verification results for sin^2 + cos^2.
        System.out.println("sin^2 + cos^2 should equal 1");
        System.out.println("sin^2(" + backInCircle + " degrees) + cos^2(" + backInCircle + " degrees) = " + checkFor1);

        System.out.println("--------------------------------");

        //This section uses acos, asin, and atan on the values to further verify the angle. Source: (JavaSpring.net, 2026)
        //Converted back to degrees using Math.toDegrees() method after applying inverse functions.
        System.out.println("Using the inverse functions to verify the angle:");
        angleFromCos = Math.toDegrees(Math.acos(cosValue));
        angleFromSin = Math.toDegrees(Math.asin(sinValue));
        angleFromTan = Math.toDegrees(Math.atan(tanValue));

        //Using acos, asin, and atan to find the angles from the calculated cos, sin, and tan values.
        System.out.println("acos(" + cosValue + ") = " + angleFromCos + " degrees");
        System.out.println("asin(" + sinValue + ") = " + angleFromSin + " degrees");
        System.out.println("atan(" + tanValue + ") = " + angleFromTan + " degrees");
        System.out.println("Each of these gives the reference angle, not the full angle.");

        System.out.println("--------------------------------");

        //This section gets the full original angle back from the sin and cos and checks that it matches. Source: (JavaSpring.net, 2026)
        //Using atan2 to recover the original angle from sin and cos values, which makes sure it is using the correct quadrant of the angle.
        recovered = Math.toDegrees(Math.atan2(sinValue, cosValue));
        if (recovered < 0) {
            recovered += 360;
        }

        //Another verification step to ensure that the recovered angle matches the original angle calculated from clicks and degrees per click.
        System.out.println("atan2(sin, cos) = " + recovered + " degrees");
        System.out.println("Matches original angle? " + (Math.abs(recovered - backInCircle) < 1e-9));

        System.out.println("--------------------------------");

        //This section finds the hyperbolic sin, cos, and tan of the angle in radians. Source: (Oracle, n.d.)
        //These work like sin, cos, and tan but are based on a hyperbola instead of a circle.
        System.out.println("Finding sinh, cosh, and tanh of the angle in radians:");
        sinhValue = Math.sinh(angleInRadians);
        coshValue = Math.cosh(angleInRadians);
        tanhValue = Math.tanh(angleInRadians);

        //Displaying the sinh, cosh, and tanh values for the angle.
        System.out.println("sinh(" + angleInRadians + " radians) = " + sinhValue);
        System.out.println("cosh(" + angleInRadians + " radians) = " + coshValue);
        System.out.println("tanh(" + angleInRadians + " radians) = " + tanhValue);

        System.out.println("--------------------------------");

        //This section checks the hyperbolic values using tanh = sinh / cosh and cosh^2 - sinh^2 = 1.
        //This is the same idea as the sin and cos checks above, but the hyperbolic identity uses subtraction.
        System.out.println("Using relation between sinh, cosh, and tanh to verify the values:");
        tanhFromSinhCosh = sinhValue / coshValue;
        checkHyperbolic = coshValue * coshValue - sinhValue * sinhValue;

        //Displaying the verification results for the hyperbolic functions.
        System.out.println("sinh/cosh = " + tanhFromSinhCosh);
        System.out.println("sinh/cosh matches tanh? " + (Math.abs(tanhFromSinhCosh - tanhValue) < 1e-9));
        System.out.println("cosh^2 - sinh^2 should equal 1");
        System.out.println("cosh^2(" + angleInRadians + " radians) - sinh^2(" + angleInRadians + " radians) = " + checkHyperbolic);

        System.out.println("--------------------------------");

        //This section just lets the user know the program is done.
        System.out.println("All calculations complete.");
    }
}

/*References
GeeksforGeeks. (2019, May 27). Trigonometric functions in Java with examples. https://www.geeksforgeeks.org/java/trigonometric-functions-in-java-with-examples/
GeeksforGeeks. (2025, May 12). Java Math IEEEremainder() method. https://www.geeksforgeeks.org/java/java-math-ieeeremainder-method/
JavaSpring.net. (2026, May 19). Trigonometric functions in Java: A comprehensive guide with examples. https://www.javaspring.net/blog/trigonometric-functions-in-java-with-examples/
Oracle. (n.d.). Math (Java Platform SE 8). Java SE Documentation. https://docs.oracle.com/javase/8/docs/api/java/lang/Math.html
*/
