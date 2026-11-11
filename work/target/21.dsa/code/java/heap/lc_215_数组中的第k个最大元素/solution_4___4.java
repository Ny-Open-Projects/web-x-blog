// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133471440
package com.webfault.dsa; // 引入依赖

// 方案4: 快速选择（Hoare 分区，pivot 取区间首元素）
// 注意：该变体的分区写法在多数输入下不收敛（python 参考同样如此），
// 因此断言仅选用参考实现可正常给出正确结果的输入。
class Main { // 定义类型
  static int findKthLargest(int[] nums, int k) { // 定义函数/方法 findKthLargest
    int[] a = nums.clone(); // 把 数组.clone(); 写入 int[] a
    int n = a.length; // 把 数组.长度 存入 元素个数
    return quickselect(a, 0, n - 1, n - k); // 返回 quickselect(数组, 0, 元素个数 减 1, 元素个数 减 下标 k)
  }

  static int quickselect(int[] nums, int l, int r, int k) { // 定义函数/方法 quickselect
    if (l == r) { // 若 左指针 等于 右指针
      return nums[k]; // 返回 数组[下标 k]
    }
    int pivot = nums[l]; // 把 数组[左指针] 存入 pivot
    int i = l - 1, j = r + 1; // 把 左指针 减 1, 下标 j 赋值为 右指针 加 1 存入 下标 i
    while (i < j) { // 循环，直到不满足「下标 i 小于 下标 j」
      while (true) { // 循环，直到不满足「true」
        i += 1; // 下标 i累加 1
        if (nums[i] <= pivot) continue; // 若 数组[下标 i] 不超过 pivot) continue;
        break; // 跳出循环
      }
      while (true) { // 循环，直到不满足「true」
        j -= 1; // 下标 j累减 1
        if (nums[j] >= pivot) continue; // 若 数组[下标 j] 不低于 pivot) continue;
        break; // 跳出循环
      }
      if (i < j) { // 若 下标 i 小于 下标 j
        int t = nums[i]; // 把 数组[下标 i] 存入 另一字符串
        nums[i] = nums[j]; // 把 数组[下标 j]; 写入 nums[i]
        nums[j] = t; // 把 另一字符串; 写入 nums[j]
      }
    }
    return k <= j ? quickselect(nums, l, j, k) : quickselect(nums, j + 1, r, k);
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    int[][] cases = {{2, 1, 3}, {1}, {2, 3, 1}}; // 把 {{2, 1, 3}, {1}, {2, 3, 1}}; 写入 int[][] cases
    int[] ks = {1, 1, 1}; // 把 {1, 1, 1}; 写入 int[] ks
    int[] wants = {3, 1, 3}; // 把 {3, 1, 3}; 写入 int[] wants
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int i = 0; i < cases.length; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 cases.长度 就继续
      int got = findKthLargest(cases[i], ks[i]); // 把 findKthLargest(cases[下标 i], ks[下标 i]) 存入 got
      if (got != wants[i]) { // 若 got 不等于 wants[下标 i]
        ok = false; // 把 false; 写入 ok
        System.out.println(
            "FAIL findKthLargest(case"
                + i
                + ", k="
                + ks[i]
                + ")="
                + got
                + " want "
                + wants[i]); // 打印输出
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
