package com.imooc.dddq.code;

public class L55 {
    public boolean canJump(int[] nums) {
        // 最远的位置
        int right = 0;
        for(int i = 0; i < nums.length; i ++) {
            // 初始化
            if (i == 0) {
                right = nums[0];
            } else if(i <= right) {
                right = Math.max(right, i + nums[i]);
            }
            if (right >= (nums.length - 1)) {
                return true;
            }
        }
        return false;
    }

    public static void main(String[] args){
//        int []nums = {3,2,1,0,4};
//        int []nums = {0};
        int [] nums = {2,3,1,1,4};
        System.out.println(new L55().canJump(nums));
    }
}
