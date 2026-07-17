class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int i = 0 , j = numbers.length - 1;
        int[] newArray = new int[2];
        while(i<j){
            int current_sum = numbers[i] + numbers[j];
            if(current_sum == target){
                newArray[0] = i + 1;
                newArray[1] = j + 1;
                return newArray;
            }
            else if(current_sum > target){
                j = j -1;
            }
            else{
                i=i+1;
            }
        }
        return newArray;
    }
}