class Solution {
    public void sortColors(int[] nums) {
        int i = 0 , k = 0 , j = nums.length - 1;
        while(k<=j){
            if(nums[k]==2){
                int x = nums[k];
                nums[k] = nums[j];
                nums[j] = x;
                j = j - 1;
            }
            else if(nums[k]==0){
                int y = nums[k];
                nums[k] = nums[i];
                nums[i] = y;
                i = i + 1;
                k = k + 1;
            }
            else{
                k = k + 1;
            }
            
        }
        
    }
}