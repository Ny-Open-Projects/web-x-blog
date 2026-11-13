// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144829143
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc673_solution222 { // 定义类型
  public int findNumberOfLIS(int[] nums) { // 定义函数/方法 findNumberOfLIS
    int n = nums.length; // 把 数组.长度 存入 元素个数
    int maxLen = 0, ans = 0; // 把 0, 答案 赋值为 0 存入 maxLen
    int[] dp = new int[n]; // 把 new int[元素个数]; 写入 int[] dp
    int[] cnt = new int[n]; // 把 new int[元素个数]; 写入 int[] cnt
    Arrays.fill(dp, 1); // Arrays.fill(DP 表, 1);
    Arrays.fill(cnt, 1); // Arrays.fill(计数, 1);
    for (int i = 0; i < n; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
      for (int j = 0; j < i; j++) { // 让 下标 j 从 0 开始计数，下标 j 小于 下标 i 就继续
        if (nums[j] < nums[i]) { // 若 数组[下标 j] 小于 数组[下标 i]
          if (dp[j] + 1 > dp[i]) { // 若 DP 表[下标 j] 加 1 超过 DP 表[下标 i]
            dp[i] = dp[j] + 1; // 把 DP 表[下标 j] 加 1; 写入 dp[i]
            cnt[i] = cnt[j]; // 把 计数[下标 j]; 写入 cnt[i]
          } else if (dp[j] + 1 == dp[i]) { // 否则，若 DP 表[下标 j] 加 1 等于 DP 表[下标 i]
            cnt[i] += cnt[j]; // cnt[i]累加 计数[下标 j]
          }
        }
      }
      if (dp[i] > maxLen) { // 若 DP 表[下标 i] 超过 maxLen
        maxLen = dp[i]; // 把 DP 表[下标 i]; 写入 maxLen
        ans = cnt[i]; // 把 计数[下标 i]; 写入 答案
      } else if (dp[i] == maxLen) { // 否则，若 DP 表[下标 i] 等于 maxLen
        ans += cnt[i]; // 答案累加 计数[下标 i]
      }
    }
    return ans; // 返回 答案
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    lc673_solution222 s =
        new lc673_solution222(); // 把 new lc673_solution222(); 写入 lc673_solution222 s
    int got =
        s.findNumberOfLIS(
            new int[] {1, 3, 5, 4, 7}); // 把 字符串.findNumberOfLIS(new int[]{1, 3, 5, 4, 7}) 存入 got
    if (got != 2) {
      System.out.println("FAIL got " + got);
      throw new RuntimeException("FAILED");
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
