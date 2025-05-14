public class lab8quadratic {
    
    public static String findRoots(double a, double b, double c) {
        // Calculate discriminant
        double discriminant = b * b - 4 * a * c;
        
        // If discriminant is negative, roots are imaginary
        if (discriminant < 0) {
            return "No Real Roots";
        }
        
        // Calculate the two roots
        double root1 = (-b + Math.sqrt(discriminant)) / (2 * a);
        double root2 = (-b - Math.sqrt(discriminant)) / (2 * a);
        
        return "The roots are: " + root1 + " and " + root2;
    }

    public static void main(String[] args) {
        java.util.Scanner scanner = new java.util.Scanner(System.in);
        
        System.out.print("Enter coefficient a: ");
        double a = scanner.nextDouble();
        
        System.out.print("Enter coefficient b: ");
        double b = scanner.nextDouble();
        
        System.out.print("Enter coefficient c: ");
        double c = scanner.nextDouble();
        
        System.out.println(findRoots(a, b, c));
        scanner.close();
    }
}

