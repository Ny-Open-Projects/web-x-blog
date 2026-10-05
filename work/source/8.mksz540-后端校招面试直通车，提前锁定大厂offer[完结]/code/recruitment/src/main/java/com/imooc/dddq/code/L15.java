package com.imooc.dddq.code;


import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class L15 {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        int length = nums.length;
        List<List<Integer>> results = new ArrayList<>();
        // 枚举a
        for(int i = 0; i < length; i ++) {
            // 去重
            if (i > 0 && nums[i] == nums[i-1]) {
                continue;
            }
            int R = length - 1;
            // 枚举b
            for(int L = i + 1; L < length; L ++) {
                // 去重
                if (L > i + 1 && nums[L] == nums[L-1]) {
                    continue;
                }
                // 枚举c
                while(L < R && nums[L] + nums[R] + nums[i] > 0) {
                    R -= 1;
                }
                if (L == R) {
                    break;
                }
                if (nums[L] + nums[R] + nums[i] == 0) {
                    List<Integer> result = new ArrayList<>();
                    result.add(nums[L]);
                    result.add(nums[R]);
                    result.add(nums[i]);
                    results.add(result);
                }
            }
        }
        return results;
    }

    public static void main(String[] args) {
        int[] nums = {-1, 0, 1, 2, -1, -4};
        System.out.println(new L15().threeSum(nums));
    }
}
