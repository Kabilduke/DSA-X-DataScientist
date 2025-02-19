class Solution {
    public int hIndex(int[] citations) {
        int n = citations.length;
        int max_index = 0;
        Arrays.sort(citations);

        for(int i = 0; i< n; i++){
            
            int h_index = Math.min(n-i, citations[i]);

            max_index = Math.max(max_index, h_index);
        }
       
        return max_index;
    }
}
