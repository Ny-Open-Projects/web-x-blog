// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134191965
package com.webfault.dsa; // 引入依赖

class lc134191965_solution11 { // 定义类型
  static void countingSortByDigit(int[] nums, int exp) { // 定义函数/方法 countingSortByDigit
    int n = nums.length; // 把 数组.长度 存入 元素个数
    int[] output = new int[n]; // 把 new int[元素个数]; 写入 int[] output
    int[] count = new int[10]; // 把 new int[10]; 写入 int[] count
    for (int i = 0; i < n; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
      int index = nums[i] / exp; // 把 数组[下标 i] 除以 exp 存入 index
      count[index % 10]++; // 计数[index 对…取模 10] 加一 ;
    }
    for (int i = 1; i < 10; i++) count[i] += count[i - 1]; // 让 下标 i 从 1 开始计数，下标 i 小于 10 就继续
    for (int i = n - 1; i >= 0; i--) { // 让 下标 i 从 元素个数 减 1 开始计数，下标 i 不低于 0 就继续
      int index = nums[i] / exp; // 把 数组[下标 i] 除以 exp 存入 index
      output[count[index % 10] - 1] = nums[i]; // 把 数组[下标 i]; 写入 output[count[index % 10] - 1]
      count[index % 10]--; // 计数[index 对…取模 10] 减一 ;
    }
    for (int i = 0; i < n; i++) nums[i] = output[i]; // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
  }

  static int[] radixSort(int[] nums) { // 定义函数/方法 radixSort
    if (nums.length == 0) return nums; // 若 数组.长度 等于 0，直接返回 数组
    int maxNum = 0; // 把 0 存入 maxNum
    for (int v : nums)
      if (v > maxNum) maxNum = v; // 把 值; 写入 for (int v : nums) if (v > maxNum) maxNum
    int exp = 1; // 把 1 存入 exp
    while (maxNum / exp > 0) { // 循环，直到不满足「maxNum 除以 exp 超过 0」
      countingSortByDigit(nums, exp); // countingSortByDigit(数组, exp);
      exp *= 10; // 把 10; 写入 exp *
    }
    return nums; // 返回 数组
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    int[][][] cases = { // 把 { 写入 int[][][] cases
      {{1, 2, 3}, {1, 2, 3}},
      {
        {100, 34, 1002, 1234, 66, 137, 49, 102, 9, 108, 102, 101, 104, 109, 102},
        {9, 34, 49, 66, 100, 101, 102, 102, 102, 104, 108, 109, 137, 1002, 1234}
      },
      {{5, 4, 3, 2, 1}, {1, 2, 3, 4, 5}},
      {{1, 2, 3, 4, 5}, {1, 2, 3, 4, 5}},
      {{3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5}, {1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9}},
      {{}, {}},
    };
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int[][] c : cases) { // for (int[][] 字符 : cases) {
      int[] in = c[0].clone(); // 把 字符[0].clone(); 写入 int[] in
      int[] want = c[1]; // 把 字符[1]; 写入 int[] want
      int[] got = radixSort(in); // 把 radixSort(in); 写入 int[] got
      if (got.length != want.length) {
        ok = false;
        System.out.println("FAIL len " + got.length + " want " + want.length);
        continue;
      }
      for (int i = 0; i < want.length; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 want.长度 就继续
        if (got[i] != want[i]) {
          ok = false;
          System.out.println(
              "FAIL "
                  + java.util.Arrays.toString(c[0])
                  + " got "
                  + java.util.Arrays.toString(got)
                  + " want "
                  + java.util.Arrays.toString(want));
          break;
        }
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
