class Solution {
    public int subarraySum(int[] nums, int k) {
        int cnt = 0;
        for(int st=0; st<nums.length; st++){
            int sum = 0;
            for(int ed=st; ed<nums.length; ed++){
                sum += nums[ed];
                if(sum == k)
                    cnt++;
            }
        }
        return cnt;
    }
}