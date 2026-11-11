// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145233483
package com.webfault.dsa; // 引入依赖

class FindMinRotated { // 定义类型
  public int findMin(int[] nums) { // 定义函数/方法 findMin
    int low = 0; // 把 0 存入 low
    int high = nums.length - 1; // 把 数组.长度 减 1 存入 high
    while (low < high) { // 循环，直到不满足「low 小于 high」
      int pivot = low + (high - low) / 2; // 把 low 加 (high 减 low) 除以 2 存入 pivot
      if (nums[pivot] < nums[high]) { // 若 数组[pivot] 小于 数组[high]
        high = pivot; // 把 pivot; 写入 high
      } else { // 否则
        low = pivot + 1; // 把 pivot 加 1; 写入 low
      }
    }
    return nums[low]; // 返回 数组[low]
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    FindMinRotated s = new FindMinRotated(); // 把 new FindMinRotated(); 写入 FindMinRotated s
    int[][][] cases = { // 把 { 写入 int[][][] cases
      {{1, 2, 3}, {1}},
      {{3, 4, 5, 1, 2}, {1}},
      {{4, 5, 6, 7, 0, 1, 2}, {0}},
    };
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int[][] c : cases) { // for (int[][] 字符 : cases) {
      int got = s.findMin(c[0]); // 把 字符串.findMin(字符[0]) 存入 got
      if (got != c[1][0]) { // 若 got 不等于 字符[1][0]
        ok = false; // 把 false; 写入 ok
        System.out.println(
            "FAIL findMin(" + arrStr(c[0]) + ")=" + got + " want " + c[1][0]); // 打印输出
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }

  static String arrStr(int[] a) { // 定义函数/方法 arrStr
    StringBuilder sb = new StringBuilder("["); // 把 new StringBuilder(「[」); 写入 StringBuilder sb
    for (int i = 0; i < a.length; i++) {
      if (i > 0) sb.append(",");
      sb.append(a[i]);
    } // 让 下标 i 从 0 开始计数，下标 i 小于 数组.长度 就继续
    sb.append("]"); // 把 「]」 追加到列表尾部
    return sb.toString(); // 返回 sb.toString()
  }
}
