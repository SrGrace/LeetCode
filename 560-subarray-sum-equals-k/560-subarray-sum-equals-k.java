class Solution {
    public int subarraySum(int[] nums, int k) {
        /*
        // O(n^2) O(1)
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
        */
        
        //O(n), O(n)
        int cnt = 0, sum = 0;
        HashMap<Integer, Integer> hsh = new HashMap <> ();
        hsh.put(0, 1);
        for(int i=0; i<nums.length; i++){
            sum += nums[i];
            if(hsh.containsKey(sum-k))
                cnt += hsh.get(sum-k);
            hsh.put(sum, hsh.getOrDefault(sum, 0)+1);
        }
        return cnt;
    }
}