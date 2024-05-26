public class Kth {
    public static void main(String[] args){
        String word = "kabil";
        int k = 2;
        int n = word.length();
        String reverse = " ";

        for(int i = 0 ; i<n ; i++){
            
            char c = word.charAt(i);
            reverse =  c + reverse;

            //System.out.print(reverse);
        }
        System.out.println(reverse);
        System.err.println(word.charAt(k));
    }  
}
