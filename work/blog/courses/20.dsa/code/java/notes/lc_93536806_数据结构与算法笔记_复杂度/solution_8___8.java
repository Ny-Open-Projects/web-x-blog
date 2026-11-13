// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/93536806
package com.webfault.dsa; // 引入依赖

class Main { // 定义类型
  void heapify(int[] arr, int size, int root) { // 定义函数/方法 heapify
    int largest = root; // 把 根节点 存入 largest
    int left = 2 * root + 1; // 把 2 乘 根节点 加 1 存入 左边界
    int right = 2 * root + 2; // 把 2 乘 根节点 加 2 存入 右边界
    if (left < size && arr[left] > arr[largest])
      largest = left; // 若 左边界 小于 大小 且 数组[左边界] 超过 数组[largest]) largest 赋值为 左边界;
    if (right < size && arr[right] > arr[largest])
      largest = right; // 若 右边界 小于 大小 且 数组[右边界] 超过 数组[largest]) largest 赋值为 右边界;
    if (largest != root) {
      int t = arr[root];
      arr[root] = arr[largest];
      arr[largest] = t;
      heapify(arr, size, largest);
    }
  }

  int[] heap_sort(int[] arr) { // 定义函数/方法 heap_sort
    int n = arr.length; // 把 数组.长度 存入 元素个数
    for (int i = n / 2 - 1; i >= 0; i--)
      heapify(arr, n, i); // 让 下标 i 从 元素个数 除以 2 减 1 开始计数，下标 i 不低于 0 就继续
    for (int i = n - 1; i > 0; i--) {
      int t = arr[0];
      arr[0] = arr[i];
      arr[i] = t;
      heapify(arr, i, 0);
    } // 让 下标 i 从 元素个数 减 1 开始计数，下标 i 超过 0 就继续
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
      int[] got = s.heap_sort((int[]) c[0]); // 把 字符串.heap_sort((int[]) 字符[0]); 写入 int[] got
      if (!java.util.Arrays.equals(got, (int[]) c[1])) {
        ok = false;
        System.out.println("FAIL got=" + java.util.Arrays.toString(got));
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
