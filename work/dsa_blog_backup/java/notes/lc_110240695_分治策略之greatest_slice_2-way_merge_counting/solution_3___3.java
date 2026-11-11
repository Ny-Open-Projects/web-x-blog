// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/110240695
package com.webfault.dsa; // 引入依赖

class lc110240695_solution33 { // 定义类型
  // 分治 O(n log n)
  static class T { // static class T {
    int best, prefix, suffix, total; // int 当前最优, prefix, suffix, 总和;

    T(int b, int p, int s, int t) {
      best = b;
      prefix = p;
      suffix = s;
      total = t;
    }
  }

  static T helper(int[] arr, int lo, int hi) { // 定义函数/方法 helper
    if (hi - lo == 1) { // 若 右边界 减 左边界 等于 1
      int v = arr[lo]; // 把 数组[左边界] 存入 值
      return new T(v, v, v, v); // 返回 new T(值, 值, 值, 值)
    }
    int mi = lo + (hi - lo) / 2; // 把 (左边界 加 右边界) 除以 2 存入 mi
    T l = helper(arr, lo, mi); // 把 helper(数组, 左边界, mi); 写入 T l
    T r = helper(arr, mi, hi); // 把 helper(数组, mi, 右边界); 写入 T r
    int crossing = l.suffix + r.prefix; // 把 左指针.suffix 加 右指针.prefix 存入 crossing
    int best =
        Math.max(
            Math.max(l.best, r.best),
            crossing); // 把 Math.取较大值 Math.取较大值 左指针.当前最优, 右指针.当前最优), crossing) 存入 当前最优
    int prefix =
        Math.max(
            l.prefix, l.total + r.prefix); // 把 Math.取较大值 左指针.prefix, 左指针.总和 加 右指针.prefix) 存入 prefix
    int suffix =
        Math.max(
            r.suffix, r.total + l.suffix); // 把 Math.取较大值 右指针.suffix, 右指针.总和 加 左指针.suffix) 存入 suffix
    int total = l.total + r.total; // 把 左指针.总和 加 右指针.总和 存入 总和
    return new T(best, prefix, suffix, total); // 返回 new T(当前最优, prefix, suffix, 总和)
  }

  static int maxSubArrayDc(int[] arr) { // 定义函数/方法 maxSubArrayDc
    if (arr.length == 0) return 0; // 若 数组.长度 等于 0，直接返回 0
    return helper(arr, 0, arr.length).best; // 返回 helper(数组, 0, 数组.长度).当前最优
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    int r = maxSubArrayDc(new int[] {-2, 1, -3, 4, -1, 2, 1});
    if (r != 6) { // 若 右指针 不等于 6
      System.out.println("FAIL " + r); // 打印输出
      throw new RuntimeException("FAILED"); // throw new RuntimeException(「FAILED」);
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
