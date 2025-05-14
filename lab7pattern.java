import java.util.Scanner;

public class lab7pattern {

    public static void printPattern(int rows) {
        int totalElements = 0;
        for (int i = 0; i < rows; i++) {
            totalElements += 2 * (rows - i) - 1;
        }

        int current = 2 * totalElements - 1;

        for (int i = 0; i < rows; i++) {
            for (int s = 0; s < i; s++) {
                System.out.print("   ");
            }

            int count = 2 * (rows - i) - 1;
            for (int j = 0; j < count; j++) {
                System.out.print(current + " ");
                current -= 2;
            }
            System.out.println();
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter number of rows: ");
        int n = scanner.nextInt();
        printPattern(n);
        scanner.close();
    }
}

