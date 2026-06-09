class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> res = new ArrayList<>();

        for (int i = 0; i < nums.length; i++){
            int a = nums[i];
            if (i > 0 && nums[i-1] == a){
                continue;
            }

            int l = i + 1;
            int r = nums.length - 1;

            while(l < r){
                int threeSum = a + nums[l] + nums[r];
                if (threeSum > 0){
                    r--;
                }else if (threeSum < 0){
                    l++;
                }else{
                    res.add(Arrays.asList(a, nums[l], nums[r]));
                    l++;
                    r--;
                    while (l < r && nums[l] == nums[l-1]){
                        l++;
                    }
                }
            }
        }

        return res;
    }
}
