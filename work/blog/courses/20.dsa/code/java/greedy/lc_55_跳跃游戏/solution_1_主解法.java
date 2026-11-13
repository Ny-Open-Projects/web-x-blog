// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145241347
package com.webfault.dsa; // 引入依赖

class lc55_solution1 { // 定义类型
  static boolean canJump(int[] nums) { // 定义函数/方法 canJump
    int maxReach = 0; // 把 0 存入 maxReach
    for (int i = 0; i < nums.length; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 数组.长度 就继续
      if (i > maxReach) return false; // 若 下标 i 超过 maxReach，直接返回 false
      maxReach =
          Math.max(maxReach, i + nums[i]); // 把 Math.取较大值 maxReach, 下标 i 加 数组[下标 i]); 写入 maxReach
    }
    return true; // 返回 true
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    boolean a =
        canJump(new int[] {2, 3, 1, 1, 4}); // 把 canJump(new int[]{2, 3, 1, 1, 4}); 写入 boolean a
    if (!a) throw new RuntimeException("FAILED: canJump([2,3,1,1,4]) want true");
    boolean b =
        canJump(new int[] {3, 2, 1, 0, 4}); // 把 canJump(new int[]{3, 2, 1, 0, 4}); 写入 boolean b
    if (b) throw new RuntimeException("FAILED: canJump([3,2,1,0,4]) want false");
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
