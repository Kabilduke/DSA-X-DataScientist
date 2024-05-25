import java.util.*;

public class Distination {

    public static void main(String[] args) {

        List<List<String>> paths = new ArrayList<>();
        paths.add(Arrays.asList("London", "New York"));
        paths.add(Arrays.asList("New York", "kanniyakumari"));
        paths.add(Arrays.asList("Lima", "London"));

        Solution sol = new Solution();

        String Distination = sol.city(paths);
        System.out.println(Distination);
    }
}

class Solution{
    public String city(List<List<String>> paths){
        HashSet<String> set = new HashSet<>();

        for(List<String> path: paths){
            set.add(path.get(0));
        }
        for(List<String> path: paths){
            if(!set.contains(path.get(1))){
                return path.get(1);
            }

        }
        return "";
    }
}
