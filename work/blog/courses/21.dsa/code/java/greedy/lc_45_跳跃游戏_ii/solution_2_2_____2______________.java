// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145241433
package com.webfault.dsa; // 引入依赖

class lc45_solution222 { // 定义类型
  static int jump(int[] nums) { // 定义函数/方法 jump
    int n = nums.length; // 把 数组.长度 存入 元素个数
    int maxPos = 0, end = 0, steps = 0; // 把 0, 终点 赋值为 0, steps 赋值为 0 存入 maxPos
    for (int i = 0; i < n - 1; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 减 1 就继续
      maxPos = Math.max(maxPos, i + nums[i]); // 把 Math.取较大值 maxPos, 下标 i 加 数组[下标 i]); 写入 maxPos
      if (i == end) { // 若 下标 i 等于 终点
        end = maxPos; // 把 maxPos; 写入 终点
        steps++; // steps 加一
      }
    }
    return steps; // 返回 steps
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    int got = jump(new int[] {2, 3, 1, 1, 4}); // 把 jump(new int[]{2, 3, 1, 1, 4}) 存入 got
    if (got != 2) throw new RuntimeException("FAILED: got " + got + " want 2");
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
