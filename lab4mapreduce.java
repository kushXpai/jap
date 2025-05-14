import java.util.*;
import java.util.stream.*;

public class lab4mapreduce {

    public static void main(String[] args) {
        // Sample list of integers
        List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5, 6);

        // 1. Filter: Get only even numbers
        List<Integer> evenNumbers = numbers.stream()
                                           .filter(n -> n % 2 == 0) // Lambda for filter
                                           .collect(Collectors.toList());
        System.out.println("Even Numbers: " + evenNumbers);

        // 2. Map: Square the even numbers
        List<Integer> squaredEvens = evenNumbers.stream()
                                                .map(n -> n * n) // Lambda for map
                                                .collect(Collectors.toList());
        System.out.println("Squared Even Numbers: " + squaredEvens);

        // 3. Reduce: Sum of the squared even numbers
        Optional<Integer> sumOfSquares = squaredEvens.stream()
                                                     .reduce((a, b) -> a + b); // Lambda for reduce

        // 4. Optional Handling
        if (sumOfSquares.isPresent()) {
            System.out.println("Sum of Squared Even Numbers: " + sumOfSquares.get());
        } else {
            System.out.println("No squared even numbers to sum.");
        }

        // 5. Optional function example: Get first even number
        Optional<Integer> firstEven = getFirstEven(numbers);
        System.out.println("First Even Number: " + firstEven.orElse(-1));
    }

    // Function that returns Optional<Integer>
    public static Optional<Integer> getFirstEven(List<Integer> list) {
        return list.stream()
                   .filter(n -> n % 2 == 0)
                   .findFirst(); // returns Optional
    }
}
