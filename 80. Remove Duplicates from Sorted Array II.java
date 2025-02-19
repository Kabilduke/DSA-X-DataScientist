class Solution {
    public int removeDuplicates(int[] nums) {
        int n = nums.length;
        int count = 0;
        int seen = 1;

        for(int i = 1; i < n; i++){
            if(nums[i] == nums[i-1]){
                seen++;
            }else{
                seen = 1;
            }

            if (seen <= 2){
                nums[++count] = nums[i];
                
            }

        }
        
        return count+1;
    }
}
