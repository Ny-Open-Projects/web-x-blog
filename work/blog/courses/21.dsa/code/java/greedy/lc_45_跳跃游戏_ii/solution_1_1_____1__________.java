// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145241433
package com.webfault.dsa; // 引入依赖

class lc45_solution111 { // 定义类型
  static int jump(int[] nums) { // 定义函数/方法 jump
    int n = nums.length; // 把 数组.长度 存入 元素个数
    int position = n - 1; // 把 元素个数 减 1 存入 position
    int steps = 0; // 把 0 存入 steps
    while (position > 0) { // 循环，直到不满足「position 超过 0」
      for (int i = 0; i < position; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 position 就继续
        if (i + nums[i] >= position) { // 若 下标 i 加 数组[下标 i] 不低于 position
          position = i; // 把 下标 i; 写入 position
          steps++; // steps 加一
          break; // 跳出循环
        }
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
