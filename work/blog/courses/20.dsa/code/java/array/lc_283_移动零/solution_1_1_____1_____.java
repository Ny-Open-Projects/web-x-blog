// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145116601
package com.webfault.dsa; // 引入依赖

import java.util.Arrays; // 引入依赖

// 移动零：双指针原地交换，把 0 移到末尾，保持非零元素相对顺序。
// 忠实翻译自 Python 参考实现。
class lc283_solution111 { // 定义类型
  static int[] moveZeroes(int[] nums) { // 定义函数/方法 moveZeroes
    int[] res = nums.clone(); // 把 数组.clone(); 写入 int[] res
    int left = 0; // 把 0 存入 左边界
    for (int right = 0; right < res.length; right++) { // 让 右边界 从 0 开始计数，右边界 小于 结果.长度 就继续
      if (res[right] != 0) { // 若 结果[右边界] 不等于 0
        int tmp = res[left]; // 把 结果[左边界] 存入 临时变量
        res[left] = res[right]; // 把 结果[右边界]; 写入 res[left]
        res[right] = tmp; // 把 临时变量; 写入 res[right]
        left++; // 左边界 加一
      }
    }
    return res; // 返回 结果
  }

  static boolean eqIntArray(int[] a, int[] b) { // 定义函数/方法 eqIntArray
    if (a.length != b.length) return false; // 若 数组.长度 不等于 b.长度，直接返回 false
    for (int i = 0; i < a.length; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 数组.长度 就继续
      if (a[i] != b[i]) return false; // 若 数组[下标 i] 不等于 b[下标 i]，直接返回 false
    }
    return true; // 返回 true
  }

  static boolean selfCheck() { // 定义函数/方法 selfCheck
    // (args, expected) 取自 _tools/correctness_check.py 的 lc_283_移动零 cases
    int[][][] cases = { // 把 { 写入 int[][][] cases
      {{0, 1, 0, 3, 12}, {1, 3, 12, 0, 0}},
      {{0}, {0}},
      {{1, 2, 3}, {1, 2, 3}},
    };
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int k = 0; k < cases.length; k++) { // 让 下标 k 从 0 开始计数，下标 k 小于 cases.长度 就继续
      int[] got = moveZeroes(cases[k][0]); // 把 moveZeroes(cases[下标 k][0]); 写入 int[] got
      if (!eqIntArray(got, cases[k][1])) { // 若 取反 eqIntArray(got, cases[下标 k][1]
        ok = false; // 把 false; 写入 ok
        System.out.println(
            "FAIL case"
                + (k + 1)
                + ": got "
                + Arrays.toString(got) // 打印输出
                + " want "
                + Arrays.toString(cases[k][1])); // 加 「 want 」 加 Arrays.toString(cases[下标 k][1]));
      }
    }
    return ok; // 返回 ok
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    if (!selfCheck()) { // 若 取反 selfCheck(
      System.out.println("FAIL"); // 打印输出
      System.exit(1); // System.exit(1);
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
