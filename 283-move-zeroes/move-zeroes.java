class Solution {
    public void moveZeroes(int[] nums) {
        int left = 0; // Points to where the next non-zero should go

        // 'right' scans the array from start to end
        for (int right = 0; right < nums.length; right++) {
            if (nums[right] != 0) {
                
                // Optimization: Only swap if left and right are at different positions
                if (left != right) {
                    int temp = nums[left];
                    nums[left] = nums[right];
                    nums[right] = temp;
                }
                
                // Move the target pointer forward
                left++;
            }
        }
    }
}
