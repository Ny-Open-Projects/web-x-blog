// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/108673483
package com.webfault.dsa; // 引入依赖

class notes108_qs { // 定义类型
  int quickSelect(int[] arr, int k) { // 定义函数/方法 quickSelect
    int[] a = arr.clone(); // 把 数组.clone(); 写入 int[] a
    return select(a, 0, a.length - 1, k); // 返回 select(数组, 0, 数组.长度 减 1, 下标 k)
  }

  int select(int[] a, int lo, int hi, int k) { // 定义函数/方法 select
    if (lo == hi) return a[lo]; // 若 左边界 等于 右边界，直接返回 数组[左边界]
    int pivot = a[hi]; // 把 数组[右边界] 存入 pivot
    int i = lo; // 把 左边界 存入 下标 i
    for (int j = lo; j < hi; j++) { // 让 下标 j 从 左边界 开始计数，下标 j 小于 右边界 就继续
      if (a[j] <= pivot) { // 若 数组[下标 j] 不超过 pivot
        int tmp = a[i];
        a[i] = a[j];
        a[j] = tmp; // 把 数组[下标 i]; 数组[下标 i] 赋值为 数组[下标 j]; 数组[下标 j] 赋值为 临时变量 存入 临时变量
        i++; // 下标 i 加一
      }
    }
    int tmp = a[i];
    a[i] = a[hi];
    a[hi] = tmp; // 把 数组[下标 i]; 数组[下标 i] 赋值为 数组[右边界]; 数组[右边界] 赋值为 临时变量 存入 临时变量
    if (i == k) return a[i]; // 若 下标 i 等于 下标 k，直接返回 数组[下标 i]
    else if (i > k)
      return select(a, lo, i - 1, k); // 否则，若 下标 i 超过 下标 k) return select(数组, 左边界, 下标 i 减 1, 下标 k);
    else return select(a, i + 1, hi, k); // 否则
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    notes108_qs s = new notes108_qs(); // 把 new notes108_qs(); 写入 notes108_qs s
    boolean ok = true; // 把 true; 写入 boolean ok
    if (s.quickSelect(new int[] {3, 1, 4, 1, 5, 9, 2, 6}, 2) != 2) {
      ok = false;
      System.out.println("FAIL1");
    }
    if (s.quickSelect(new int[] {3, 1, 4, 1, 5, 9, 2, 6}, 3) != 3) {
      ok = false;
      System.out.println("FAIL2");
    }
    if (s.quickSelect(new int[] {3, 1, 4, 1, 5, 9, 2, 6}, 0) != 1) {
      ok = false;
      System.out.println("FAIL3");
    }
    if (s.quickSelect(new int[] {3, 1, 4, 1, 5, 9, 2, 6}, 7) != 9) {
      ok = false;
      System.out.println("FAIL4");
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
