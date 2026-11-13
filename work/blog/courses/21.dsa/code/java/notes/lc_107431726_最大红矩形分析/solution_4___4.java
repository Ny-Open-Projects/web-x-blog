// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107431726
package com.webfault.dsa; // 引入依赖

class lcMaxRed { // 定义类型
  int maxRedRectangle(String[] matrix) { // 定义函数/方法 maxRedRectangle
    int n = matrix.length; // 把 矩阵.长度 存入 元素个数
    if (n == 0) return 0; // 若 元素个数 等于 0，直接返回 0
    int m = matrix[0].length(); // 把 矩阵[0].长度() 存入 映射表
    int ans = 0; // 把 0 存入 答案
    int[] height = new int[m + 2]; // 把 new int[映射表 加 2]; 写入 int[] height
    for (int k = 0; k < n; k++) { // 让 下标 k 从 0 开始计数，下标 k 小于 元素个数 就继续
      for (int i = 1; i <= m; i++) { // 让 下标 i 从 1 开始计数，下标 i 不超过 映射表 就继续
        if (matrix[k].charAt(i - 1) == '.')
          height[i] += 1; // 若 矩阵[下标 k] 取字符 下标 i 减 1) 等于 '.') height[下标 i] 累加 1;
        else height[i] = 0; // 否则
      }
      int[] stack = new int[m + 2]; // 把 new int[映射表 加 2]; 写入 int[] stack
      int sp = 0; // 把 0 存入 sp
      stack[sp++] = 0; // 把 0; 写入 stack[sp++]
      for (int i = 1; i < m + 2; i++) { // 让 下标 i 从 1 开始计数，下标 i 小于 映射表 加 2 就继续
        while (height[stack[sp - 1]] > height[i]) { // 循环，直到不满足「height[栈[sp 减 1]] 超过 height[下标 i]」
          int now_h = height[stack[--sp]]; // 把 height[栈[ 减一 sp]] 存入 now_h
          int width = i - stack[sp - 1] - 1; // 把 下标 i 减 栈[sp 减 1] 减 1 存入 width
          if (now_h * width > ans)
            ans = now_h * width; // 若 now_h 乘 width 超过 答案) 答案 赋值为 now_h 乘 width;
        }
        stack[sp++] = i; // 把 下标 i; 写入 stack[sp++]
      }
    }
    return ans; // 返回 答案
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    lcMaxRed s = new lcMaxRed(); // 把 new lcMaxRed(); 写入 lcMaxRed s
    String[][][] cases = { // 把 { 写入 String[][][] cases
      {{".....", "XXXXX", ".X...", "....."}},
      {{"X"}},
      {{"."}},
      {{".X"}, {"X."}} // {{「.X」}, {「.X」}}
    };
    int[] wants = {6, 0, 1, 1}; // 把 {6, 0, 1, 1}; 写入 int[] wants
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int i = 0; i < wants.length; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 wants.长度 就继续
      int got = s.maxRedRectangle(cases[i][0]); // 把 字符串.maxRedRectangle(cases[下标 i][0]) 存入 got
      if (got != wants[i]) {
        ok = false;
        System.out.println("FAIL case " + i + " got " + got + " want " + wants[i]);
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
