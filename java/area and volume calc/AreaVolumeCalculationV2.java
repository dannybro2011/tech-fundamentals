import java.util.Scanner; // import scanner

/* the purpose of this object-oriented program is to create classes
   and methods for area and volume calculations */

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in); // instantiate scanner
        System.out.println("Pick a calculation. Input either: Area, Cylinder, Cube, Sphere (not case sensitive). Then press enter:");
        String input = scan.next();

        if (input.equalsIgnoreCase("Area")) {
            Rectangle.printArea(scan);
        } else if (input.equalsIgnoreCase("Cube")) {
            Cube.printCubeVolume(scan);
        } else if (input.equalsIgnoreCase("Cylinder")) {
            Cylinder.printCylinderVolume(scan);
        } else if (input.equalsIgnoreCase("Sphere")) {
            Sphere.printSphereVolume(scan);
        } else {
            System.out.println("Invalid input.");
        }

        scan.close(); // close main scanner
    }
}

class Rectangle {
    public static void printArea(Scanner scan) {
        
        System.out.println("Enter two numbers to find the area of a Rectangle, one for length and one for width (Press Enter after each):");

        //check input errors
        while (!scan.hasNextInt()) {
            System.out.println("Try entering a number");
            scan.next();
        }

        //make variables for calculation, get user input
        int l = scan.nextInt();
        int w = scan.nextInt();
        int area = l * w;

        //print calculation
        System.out.println("The Area of Length: " + l + " Width: " + w + " is: " + area);
        
    }
}

class Cube {
    public static void printCubeVolume(Scanner scan) {
        
        System.out.println("Enter one number for the length of a cube (Press Enter after):");

        //check input errors
        while (!scan.hasNextInt()) {
            System.out.println("Try entering a number");
            scan.next();
        }

        //make variables for calculation, get user input
        int l = scan.nextInt();
        int volume = l * l * l;

        //print calculation
        System.out.println("The Volume of a cube of Length: " + l + " is: " + volume);
        
    }
}

class Cylinder{
    public static void printCylinderVolume(Scanner scan) {
        
        System.out.println("Enter two numbers, one for radius and one for height (Press Enter after each):");
        
        //check input errors
        while (!scan.hasNextDouble()) {
            System.out.println("Try entering a number");
            scan.next();
        }

        //make variables for calculation, get user input
        double r = scan.nextDouble();
        double h = scan.nextDouble();
        double p = 3.14;
        double volume = p*(r*r)*h;
        
        //print calculation
        System.out.println("The Volume of a Cylinder of Radius: " + r + " Height: " + h + " " + volume);
        
    }
}

class Sphere{
    public static void printSphereVolume(Scanner scan) {
        
        System.out.println("Enter one number for the Radius of a sphere (Press Enter after):");

        //check input errors
        while (!scan.hasNextDouble()) {
            System.out.println("Try entering a number");
            scan.next();
        }

        //make variables for calculation, get user input
        double r = scan.nextDouble();
        double p = 3.14;
        double volume = (4/3)*p*(r*r*r);

        //print calculation
        System.out.println("The Volume of a sphere of Radius: " + r + " is: " + volume);
        
    }
}