import java.util.Date;
import java.util.HashMap;
import java.util.Map;
import java.util.UUID;
import java.util.Scanner;

// a. New class to store notification data (Date and Message)
class NotificationVO {
    private final Date date;
    private final String message;

    public NotificationVO(Date date, String message) {
        this.date = date;
        this.message = message;
    }

    public Date getDate() {
        return date;
    }

    public String getMessage() {
        return message;
    }
}

// b. New interface with updated method signatures
interface NotificationDAO {
    UUID addNotification(Date date, String message); // c.i: now accepts message
    NotificationVO getNotification(UUID id);         // c.i: returns NotificationVO
}

// c.iii. Implements the new interface with the modified logic
class MapNotificationDAO implements NotificationDAO {
    private final Map<UUID, NotificationVO> notifications = new HashMap<>();

    @Override
    public UUID addNotification(Date date, String message) {
        UUID id = UUID.randomUUID();
        notifications.put(id, new NotificationVO(date, message));
        return id;
    }

    @Override
    public NotificationVO getNotification(UUID id) {
        return notifications.get(id);
    }
}

// Refactored NotificationService
public class lab1refactor {
    private final NotificationDAO storage; // c.iv: storage is passed via constructor

    // c.iv: Constructor accepting NotificationDAO
    public lab1refactor(NotificationDAO storage) {
        this.storage = storage;
    }

    // c.ii.1: Modified to accept a message
    public UUID raiseNotification(String message) {
        return this.storage.addNotification(new Date(), message);
    }

    // c.ii.2: Uses NotificationVO to get date
    public Date getNotificationTime(UUID id) {
        NotificationVO vo = this.storage.getNotification(id);
        return (vo != null) ? vo.getDate() : null;
    }

    // c.ii.3: New method to return message from VO
    public String getNotificationMessage(UUID id) {
        NotificationVO vo = this.storage.getNotification(id);
        return (vo != null) ? vo.getMessage() : null;
    }

    // d. Accepts count and messages from command line
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter number of notifications: ");
        int count = Integer.parseInt(scanner.nextLine());

        NotificationDAO dao = new MapNotificationDAO();
        lab1refactor service = new lab1refactor(dao);

        for (int i = 1; i <= count; i++) {
            System.out.print("Enter notification message " + i + ": ");
            String message = scanner.nextLine();

            UUID id = service.raiseNotification(message);
            System.out.println("Notification ID: " + id);
            System.out.println("Time: " + service.getNotificationTime(id));
            System.out.println("Message: " + service.getNotificationMessage(id));
            System.out.println("-----");
        }

        scanner.close();
    }
}
