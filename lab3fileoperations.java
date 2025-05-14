import java.io.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class lab3fileoperations {

    public static void main(String[] args) {
        if (args.length < 2) {
            System.out.println("Usage: java ParallelFileSearch <directory_path> <search_text>");
            return;
        }

        String dirPath = args[0];
        String searchText = args[1];

        File rootDir = new File(dirPath);
        if (!rootDir.exists() || !rootDir.isDirectory()) {
            System.out.println("Invalid directory path.");
            return;
        }

        // Create a fixed thread pool executor
        ExecutorService executor = Executors.newFixedThreadPool(Runtime.getRuntime().availableProcessors());

        // Use a CompletionService to handle task completion
        CompletionService<Void> completionService = new ExecutorCompletionService<>(executor);

        // Traverse and submit tasks
        int taskCount = submitSearchTasks(rootDir, searchText, completionService);

        // Wait for all tasks to complete
        for (int i = 0; i < taskCount; i++) {
            try {
                completionService.take(); // Waits for a task to complete
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
                System.out.println("Search interrupted.");
            }
        }

        // Shutdown the executor
        executor.shutdown();
        System.out.println("Search completed.");
    }

    // Recursive function to submit file search tasks
    public static int submitSearchTasks(File dir, String searchText, CompletionService<Void> completionService) {
        int count = 0;

        File[] files = dir.listFiles();
        if (files == null) return 0;

        for (File file : files) {
            if (file.isDirectory()) {
                count += submitSearchTasks(file, searchText, completionService); // recursive
            } else {
                completionService.submit(() -> {
                    searchInFile(file, searchText);
                    return null;
                });
                count++;
            }
        }
        return count;
    }

    // Function to search text in a single file
    public static void searchInFile(File file, String searchText) {
        int occurrences = 0;

        try (BufferedReader reader = new BufferedReader(new FileReader(file))) {
            String line;
            Pattern pattern = Pattern.compile(Pattern.quote(searchText), Pattern.CASE_INSENSITIVE);
            while ((line = reader.readLine()) != null) {
                Matcher matcher = pattern.matcher(line);
                while (matcher.find()) {
                    occurrences++;
                }
            }
        } catch (IOException e) {
            System.err.println("Error reading file: " + file.getAbsolutePath());
            return;
        }

        if (occurrences > 0) {
            System.out.println("File: " + file.getAbsolutePath() + " | Count: " + occurrences);
        }
    }
}
