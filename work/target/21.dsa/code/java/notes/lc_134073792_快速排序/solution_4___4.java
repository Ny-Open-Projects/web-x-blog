// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134073792
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class QuickS4 { // 定义类型
  static int[] toArr(List<Integer> l) { // 定义函数/方法 toArr
    int[] a = new int[l.size()]; // 把 new int[左指针.大小()]; 写入 int[] a
    for (int i = 0; i < a.length; i++) a[i] = l.get(i); // 让 下标 i 从 0 开始计数，下标 i 小于 数组.长度 就继续
    return a; // 返回 数组
  }

  static int[] qs(int[] arr) { // 定义函数/方法 qs
    if (arr.length < 1) return new int[0]; // 若 数组.长度 小于 1，直接返回 new int[0]
    int pivotIndex = arr.length / 2; // 把 数组.长度 除以 2 存入 pivotIndex
    int pivot = arr[pivotIndex]; // 把 数组[pivotIndex] 存入 pivot
    List<Integer> left = new ArrayList<>(), right = new ArrayList<>();
    for (int idx = 0; idx < arr.length; idx++) { // 让 idx 从 0 开始计数，idx 小于 数组.长度 就继续
      if (idx == pivotIndex) continue; // 若 idx 等于 pivotIndex) continue;
      int x = arr[idx]; // 把 数组[idx] 存入 x
      if (x < pivot) left.add(x); // 若 x 小于 pivot) 左边界 追加 x);
      else if (x > pivot) right.add(x); // 否则，若 x 超过 pivot) 右边界 追加 x);
    }
    int[] l = qs(toArr(left)); // 把 qs(toArr(左边界)); 写入 int[] l
    int[] r = qs(toArr(right)); // 把 qs(toArr(右边界)); 写入 int[] r
    int[] res = new int[l.length + 1 + r.length]; // 把 new int[左指针.长度 加 1 加 右指针.长度]; 写入 int[] res
    System.arraycopy(l, 0, res, 0, l.length); // System.arraycopy(左指针, 0, 结果, 0, 左指针.长度);
    res[l.length] = pivot; // 把 pivot; 写入 res[l.length]
    System.arraycopy(
        r, 0, res, l.length + 1, r.length); // System.arraycopy(右指针, 0, 结果, 左指针.长度 加 1, 右指针.长度);
    return res; // 返回 结果
  }

  static int[] quickSortV1(int[] arr) { // 定义函数/方法 quickSortV1
    int[] res = qs(arr); // 把 qs(数组); 写入 int[] res
    System.arraycopy(res, 0, arr, 0, arr.length); // System.arraycopy(结果, 0, 数组, 0, 数组.长度);
    return arr; // 返回 数组
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    int[][][] cases = { // 把 { 写入 int[][][] cases
      {{15, 4, 23, 52, 1}, {1, 4, 15, 23, 52}},
      {{3, 1, 2, 5, 4}, {1, 2, 3, 4, 5}},
      {{}, {}},
    };
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int[][] c : cases) { // for (int[][] 字符 : cases) {
      int[] in = c[0].clone(); // 把 字符[0].clone(); 写入 int[] in
      quickSortV1(in); // quickSortV1(in);
      if (!Arrays.equals(in, c[1])) { // 若 取反 Arrays.equals(in, 字符[1]
        ok = false; // 把 false; 写入 ok
        System.out.println(
            "FAIL "
                + Arrays.toString(c[0])
                + " -> "
                + Arrays.toString(in)
                + " want "
                + Arrays.toString(c[1])); // 打印输出
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
