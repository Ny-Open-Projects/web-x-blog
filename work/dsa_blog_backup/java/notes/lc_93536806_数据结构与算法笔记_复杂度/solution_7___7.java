// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/93536806
package com.webfault.dsa; // 引入依赖

class Main { // 定义类型
  int[] merge(int[] left, int[] right) { // 定义函数/方法 merge
    int[] result =
        new int[left.length + right.length]; // 把 new int[左边界.长度 加 右边界.长度]; 写入 int[] result
    int i = 0, j = 0, k = 0; // 把 0, 下标 j 赋值为 0, 下标 k 赋值为 0 存入 下标 i
    while (i < left.length && j < right.length) { // 循环，直到不满足「下标 i 小于 左边界.长度 且 下标 j 小于 右边界.长度」
      if (left[i] <= right[j])
        result[k++] = left[i++]; // 若 左边界[下标 i] 不超过 右边界[下标 j]) 结果[下标 k 加一 ] 赋值为 左边界[下标 i 加一 ];
      else result[k++] = right[j++]; // 否则
    }
    while (i < left.length)
      result[k++] = left[i++]; // 循环，直到不满足「下标 i 小于 左边界.长度) 结果[下标 k 加一 ] 赋值为 左边界[下标 i 加一 ];」
    while (j < right.length)
      result[k++] = right[j++]; // 循环，直到不满足「下标 j 小于 右边界.长度) 结果[下标 k 加一 ] 赋值为 右边界[下标 j 加一 ];」
    return result; // 返回 结果
  }

  int[] merge_sort(int[] arr) { // 定义函数/方法 merge_sort
    if (arr.length <= 1) return arr; // 若 数组.长度 不超过 1，直接返回 数组
    int mid = arr.length / 2; // 把 数组.长度 除以 2 存入 中点
    int[] left = merge_sort(java.util.Arrays.copyOfRange(arr, 0, mid));
    int[] right = merge_sort(java.util.Arrays.copyOfRange(arr, mid, arr.length));
    return merge(left, right); // 返回 merge(左边界, 右边界)
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
      int[] got = s.merge_sort((int[]) c[0]); // 把 字符串.merge_sort((int[]) 字符[0]); 写入 int[] got
      if (!java.util.Arrays.equals(got, (int[]) c[1])) {
        ok = false;
        System.out.println("FAIL got=" + java.util.Arrays.toString(got));
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
