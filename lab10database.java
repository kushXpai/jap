import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

class DatabaseOperations {
    private Connection connection;
    
    public DatabaseOperations() {
        try {
            connection = DriverManager.getConnection("jdbc:sqlite:example.db");
        } catch (SQLException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }

    public void createTable() {
        try {
            Statement stmt = connection.createStatement();
            stmt.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)");
        } catch (SQLException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }

    public void insertData(String name) {
        try {
            PreparedStatement pstmt = connection.prepareStatement("INSERT INTO users (name) VALUES (?)");
            pstmt.setString(1, name);
            pstmt.executeUpdate();
        } catch (SQLException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }

    public void fetchData() {
        try {
            Statement stmt = connection.createStatement();
            ResultSet rs = stmt.executeQuery("SELECT * FROM users");
            while (rs.next()) {
                System.out.println(rs.getInt("id") + ": " + rs.getString("name"));
            }
        } catch (SQLException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }

    public void close() {
        try {
            connection.close();
        } catch (SQLException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}

class WorkerThread extends Thread {
    private DatabaseOperations dbOperations;
    
    public WorkerThread(DatabaseOperations dbOperations) {
        this.dbOperations = dbOperations;
    }
    
    @Override
    public void run() {
        dbOperations.insertData("John Doe");
        dbOperations.insertData("Jane Smith");
        dbOperations.fetchData();
    }
}

public class lab10database {
    public static void main(String[] args) {
        DatabaseOperations dbOperations = new DatabaseOperations();
        dbOperations.createTable();
        
        WorkerThread thread1 = new WorkerThread(dbOperations);
        WorkerThread thread2 = new WorkerThread(dbOperations);
        
        thread1.start();
        thread2.start();
        
        try {
            thread1.join();
            thread2.join();
        } catch (InterruptedException e) {
            System.out.println("Error: " + e.getMessage());
        }
        
        dbOperations.close();
    }
}
