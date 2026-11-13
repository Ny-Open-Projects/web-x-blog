// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/93536806
package com.webfault.dsa; // 引入依赖

class Main { // 定义类型
  int[] insertion_sort(int[] arr) { // 定义函数/方法 insertion_sort
    for (int i = 1; i < arr.length; i++) { // 让 下标 i 从 1 开始计数，下标 i 小于 数组.长度 就继续
      int key = arr[i]; // 把 数组[下标 i] 存入 key
      int j = i - 1; // 把 下标 i 减 1 存入 下标 j
      while (j >= 0 && arr[j] > key) {
        arr[j + 1] = arr[j];
        j--;
      }
      arr[j + 1] = key; // 把 key; 写入 arr[j + 1]
    }
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
      int[] got =
          s.insertion_sort((int[]) c[0]); // 把 字符串.insertion_sort((int[]) 字符[0]); 写入 int[] got
      if (!java.util.Arrays.equals(got, (int[]) c[1])) {
        ok = false;
        System.out.println("FAIL got=" + java.util.Arrays.toString(got));
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
