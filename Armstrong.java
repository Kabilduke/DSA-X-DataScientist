public class Armstrong {
    public static void main(String args[]){
        int num = 407;
        int temp = num; 
        int n = String.valueOf(num).length();
        int sum = 0;

        while(temp != 0){
            int digit = temp%10;
            sum += Math.pow(digit, n);
            temp = temp/10;
        }
        if(sum == num){
            System.out.println("Armstrong number");
        }else{
            System.out.println("Not an Armstrong number");
        }
    }
    
}
