import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.time.temporal.ChronoUnit;

public class lab5datetime {

    // Function to calculate days between two LocalDate
    public static long getDaysBetween(LocalDate start, LocalDate end) {
        return ChronoUnit.DAYS.between(start, end);
    }

    public static void main(String[] args) {
        // Current Date and DateTime
        LocalDate currentDate = LocalDate.now();
        LocalDateTime currentDateTime = LocalDateTime.now();
        System.out.println("Current Date: " + currentDate);
        System.out.println("Current DateTime: " + currentDateTime);

        // Date parsing and formatting
        String dateStr = "2024-05-10";
        LocalDate parsedDate = LocalDate.parse(dateStr);
        System.out.println("Parsed Date: " + parsedDate);

        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd MMM yyyy");
        String formatted = parsedDate.format(formatter);
        System.out.println("Formatted Date: " + formatted);

        // Add/Subtract days
        LocalDate plusDays = parsedDate.plusDays(5);
        LocalDate minusDays = parsedDate.minusDays(3);
        System.out.println("Add 5 days: " + plusDays);
        System.out.println("Subtract 3 days: " + minusDays);

        // Get parts of date
        int year = parsedDate.getYear();
        int month = parsedDate.getMonthValue();
        int day = parsedDate.getDayOfMonth();
        System.out.println("Year: " + year + ", Month: " + month + ", Day: " + day);

        // Difference in days
        LocalDate endDate = LocalDate.of(2024, 5, 20);
        long diffDays = getDaysBetween(parsedDate, endDate);
        System.out.println("Difference between " + parsedDate + " and " + endDate + " is: " + diffDays + " days");

        // Difference using LocalDateTime
        LocalDateTime dt1 = LocalDateTime.of(2024, 5, 1, 10, 30);
        LocalDateTime dt2 = LocalDateTime.of(2024, 5, 14, 5, 0);
        long diffDateTime = ChronoUnit.DAYS.between(dt1, dt2);
        System.out.println("LocalDateTime difference: " + diffDateTime + " days");
    }
}
