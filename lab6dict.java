import java.util.*;

public class lab6dict {

    public static Map<String, List<String>> groupAndSortOwners(Map<String, String> fileMap) {
        Map<String, List<String>> groupedMap = new HashMap<>();

        // Grouping
        for (Map.Entry<String, String> entry : fileMap.entrySet()) {
            String file = entry.getKey();
            String owner = entry.getValue();
            groupedMap.computeIfAbsent(owner, k -> new ArrayList<>()).add(file);
        }

        // Sorting file names alphabetically
        for (List<String> fileList : groupedMap.values()) {
            Collections.sort(fileList);
        }

        return groupedMap;
    }

    public static void main(String[] args) {
        Map<String, String> files = new HashMap<>();
        files.put("Input.txt", "Albert");
        files.put("Code.py", "Stan");
        files.put("Output.txt", "Albert");
        files.put("btech.txt", "Albert");

        Map<String, List<String>> result = groupAndSortOwners(files);

        for (Map.Entry<String, List<String>> entry : result.entrySet()) {
            System.out.println(entry.getKey() + ": " + entry.getValue());
        }
    }
}