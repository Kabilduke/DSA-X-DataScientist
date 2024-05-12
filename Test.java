public class Test{
    public static void main(String[] args){
        String[] arr = {"d", "b" , "c", "b", "c", "a"};
        int k = 2;
        int n = arr.length;
        int count = 0;

        for(int i = 0; i<n; i++){
            int j;

            for(j =0; j<n; j++){
                if(i !=j && arr[j] == arr[i]){
                    break;
                }
            }
            if(j ==n){
                count++;
            }
            
            if(count == k){
                System.out.println(arr[i]);
                return;
            }
        }
        System.out.println("");

    }
}