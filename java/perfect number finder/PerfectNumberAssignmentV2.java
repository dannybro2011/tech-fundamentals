import java.util.Scanner; //import scanner 
/* the purpose of this program is to determine 
	perfect numbers between 1 and 200 and later allow
	users to determine the upper limit of the search */
public class Main {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in); //instantiate scanner
        System.out.println("Perfect numbers between 1 and 200: ");
		long i; //initial index
		long j; //second index
		long tester; //test value
		for(i = 1; i < 200; i++) { //for loop to start searching for perfect numbers within the range 1-upperLimit
			tester = 0; //placeholder variable for perfect numbers
			for(j = 1; j < i; j++) { //for loop to start checking if a number below i is its proper divisor
				if(i % j == 0) { //if statement check individually for proper divisor
				tester += j; //add j to tester if j is a proper divisor 
				} 
			}
			if(tester == i) { //if statement to check if tester represents a perfect number
				System.out.println(tester + " is a perfect number!"); //print the perfect number
			}
		}

        //expand program to take user specified upper limit if they want
        //prompt user
        System.out.println("Want to specify an upper limit? Enter yes or no (not case sensitive)");
        //store input
        String input = scan.next();
        //logic to ask if user want to specify upper limit
        if (input.equalsIgnoreCase("Yes")) {
            upperLimitSpecify();
        } else if (input.equalsIgnoreCase("No")) {
            System.out.println("No problem, have a nice day!");
        } else {
            System.out.println("Invalid Input");
        }

		scan.close(); //close scanner
	}

    public static void upperLimitSpecify() {
        Scanner scan = new Scanner(System.in); //instantiate scanner
		long i; //initial index
		long j; //second index
		long tester; //test value
		System.out.print("Enter an upper limit: "); //prompt user for upper limit input
		long upperLimit = scan.nextLong(); //get the user input
		for(i = 1; i < upperLimit; i++) { //for loop to start searching for perfect numbers within the range 1-upperLimit
			tester = 0; //placeholder variable for perfect numbers
			for(j = 1; j < i; j++) { //for loop to start checking if a number below i is its proper divisor
				if(i % j == 0) { //if statement check individually for proper divisor
				tester += j; //add j to tester if j is a proper divisor 
				} 
			}
			if(tester == i) { //if statement to check if tester represents a perfect number
				System.out.println(tester + " is a perfect number!"); //print the perfect number
			}
		}
		scan.close(); //close scanner
    }
}
