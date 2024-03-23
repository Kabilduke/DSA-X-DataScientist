class Solution {
    public void rotate(int[] nums, int k) {

        int n = nums.length;
        int[] rotated = new int[n];

        for(int i = 0 ; i < n; i++){
            rotated[(i+k)%n] = nums[i];
        }

        System.arraycopy(rotated, 0, nums, 0, n);

    }
}
