class Solution {
    public int majorityElement(int[] nums) {
        int n = nums.length;

        if(n == 1){
            return nums[0];
        }
        
        int count = 1;
        int max_count = 0;
        Arrays.sort(nums);
        int i;

        for(i = 0; i< n-1; i++){
            if(nums[i] == nums[i+1]){
                count ++;

                if (count > n/2){
                    max_count = nums[i];
               }

            }else{
                count = 1;
            }
        }
        return max_count;
    
    }
}
