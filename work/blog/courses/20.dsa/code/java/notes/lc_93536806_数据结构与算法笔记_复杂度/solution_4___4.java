// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/93536806
package com.webfault.dsa; // 引入依赖

class Main { // 定义类型
  int partition(int[] arr, int left, int right) { // 定义函数/方法 partition
    int pivot = arr[right]; // 把 数组[右边界] 存入 pivot
    int i = left; // 把 左边界 存入 下标 i
    for (int j = left; j < right; j++) { // 让 下标 j 从 左边界 开始计数，下标 j 小于 右边界 就继续
      if (arr[j] < pivot) {
        int t = arr[i];
        arr[i] = arr[j];
        arr[j] = t;
        i++;
      }
    }
    int t = arr[i];
    arr[i] = arr[right];
    arr[right] = t; // 把 数组[下标 i]; 数组[下标 i] 赋值为 数组[右边界]; 数组[右边界] 赋值为 另一字符串 存入 另一字符串
    return i; // 返回 下标 i
  }

  void quick_sort(int[] arr, int left, int right) { // 定义函数/方法 quick_sort
    if (left < right) { // 若 左边界 小于 右边界
      int p = partition(arr, left, right); // 把 partition(数组, 左边界, 右边界) 存入 节点
      quick_sort(arr, left, p - 1); // quick_sort(数组, 左边界, 节点 减 1);
      quick_sort(arr, p + 1, right); // quick_sort(数组, 节点 加 1, 右边界);
    }
  }

  int[] quick_sort(int[] arr) { // 定义函数/方法 quick_sort
    if (arr.length > 0)
      quick_sort(arr, 0, arr.length - 1); // 若 数组.长度 超过 0) quick_sort(数组, 0, 数组.长度 减 1);
    return arr; // 返回 数组
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    Main s = new Main(); // 把 new Main(); 写入 Main s
    Object[][] cases = { // 把 { 写入 Object[][] cases
      {new int[] {3, 1, 4, 1, 5, 9, 2, 6}, new int[] {1, 1, 2, 3, 4, 5, 6, 9}},
      {new int[] {}, new int[] {}},
      {new int[] {5}, new int[] {5}},
      {new int[] {2, 1}, new int[] {1, 2}},
    };
    boolean ok = true; // 把 true; 写入 boolean ok
    for (Object[] c : cases) { // for (Object[] 字符 : cases) {
      int[] got = s.quick_sort((int[]) c[0]); // 把 字符串.quick_sort((int[]) 字符[0]); 写入 int[] got
      if (!java.util.Arrays.equals(got, (int[]) c[1])) {
        ok = false;
        System.out.println("FAIL got=" + java.util.Arrays.toString(got));
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
