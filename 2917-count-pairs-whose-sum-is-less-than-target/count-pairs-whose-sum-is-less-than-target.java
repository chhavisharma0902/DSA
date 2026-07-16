class Solution {
    public int countPairs(List<Integer> nums, int target) {
        Collections.sort(nums);
        int i = 0 , j = nums.size() -1;
        int count = 0;
        while(i<j){
            if(nums.get(i)+nums.get(j) < target){
                count = count + (j - i);
                i = i + 1;
            }
            else{
                j = j - 1;
            }
        }
        return count;
    }
}