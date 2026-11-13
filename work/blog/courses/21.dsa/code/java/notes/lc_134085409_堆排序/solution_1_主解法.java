// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134085409
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class HeapS1 { // 定义类型
  static void heapify(int[] arr, int n, int i) { // 定义函数/方法 heapify
    int largest = i, l = 2 * i + 1, r = 2 * i + 2;
    if (l < n && arr[l] > arr[largest])
      largest = l; // 若 左指针 小于 元素个数 且 数组[左指针] 超过 数组[largest]) largest 赋值为 左指针;
    if (r < n && arr[r] > arr[largest])
      largest = r; // 若 右指针 小于 元素个数 且 数组[右指针] 超过 数组[largest]) largest 赋值为 右指针;
    if (largest != i) { // 若 largest 不等于 下标 i
      int t = arr[i];
      arr[i] = arr[largest];
      arr[largest] = t;
      heapify(arr, n, largest); // heapify(数组, 元素个数, largest);
    }
  }

  static int[] heapSort(int[] arr) { // 定义函数/方法 heapSort
    int[] a = arr.clone(); // 把 数组.clone(); 写入 int[] a
    int n = a.length; // 把 数组.长度 存入 元素个数
    for (int i = n / 2 - 1; i >= 0; i--)
      heapify(a, n, i); // 让 下标 i 从 元素个数 除以 2 减 1 开始计数，下标 i 不低于 0 就继续
    for (int i = n - 1; i > 0; i--) { // 让 下标 i 从 元素个数 减 1 开始计数，下标 i 超过 0 就继续
      int t = a[0];
      a[0] = a[i];
      a[i] = t; // 把 数组[0]; 数组[0] 赋值为 数组[下标 i]; 数组[下标 i] 赋值为 另一字符串 存入 另一字符串
      heapify(a, i, 0); // heapify(数组, 下标 i, 0);
    }
    return a; // 返回 数组
  }

  static class MaxHeap { // static class MaxHeap {
    List<Integer> data = new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<Integer> data

    void push(int val) {
      data.add(val);
      up(data.size() - 1);
    } // void push(int 值) { data 追加 值); up(data.大小() 减 1); }

    Integer pop() { // 定义函数/方法 pop
      if (data.isEmpty()) return null; // 若 data.isEmpty()，直接返回 null
      int top = data.get(0); // 把 data 查找 0) 存入 top
      data.set(0, data.get(data.size() - 1)); // data.set(0, data 查找 data.大小() 减 1));
      data.remove(data.size() - 1); // data 弹出 data.大小() 减 1);
      down(0); // down(0);
      return top; // 返回 top
    }

    void up(int i) { // 定义函数/方法 up
      while (i > 0 && data.get(i) > data.get((i - 1) / 2)) {
        Collections.swap(data, i, (i - 1) / 2); // Collections.交换 data, 下标 i, (下标 i 减 1) 除以 2);
        i = (i - 1) / 2; // 把 (下标 i 减 1) 除以 2; 写入 下标 i
      }
    }

    void down(int i) { // 定义函数/方法 down
      int n = data.size(); // 把 data.大小() 存入 元素个数
      while (true) { // 循环，直到不满足「true」
        int l = 2 * i + 1,
            r = 2 * i + 2,
            m = i; // 把 2 乘 下标 i 加 1, 右指针 赋值为 2 乘 下标 i 加 2, 映射表 赋值为 下标 i 存入 左指针
        if (l < n && data.get(l) > data.get(m))
          m = l; // 若 左指针 小于 元素个数 且 data 查找 左指针) 超过 data 查找 映射表)) 映射表 赋值为 左指针;
        if (r < n && data.get(r) > data.get(m))
          m = r; // 若 右指针 小于 元素个数 且 data 查找 右指针) 超过 data 查找 映射表)) 映射表 赋值为 右指针;
        if (m == i) break; // 若 映射表 等于 下标 i) break;
        Collections.swap(data, i, m); // Collections.交换 data, 下标 i, 映射表);
        i = m; // 把 映射表; 写入 下标 i
      }
    }
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    boolean ok = true; // 把 true; 写入 boolean ok
    int[] hs = HeapS1.heapSort(new int[] {12, 11, 13, 5, 6, 7});
    if (!Arrays.equals(
        hs,
        new int[] {5, 6, 7, 11, 12, 13})) { // 若 取反 Arrays.equals(hs, new int[]{5, 6, 7, 11, 12, 13}
      ok = false;
      System.out.println("FAIL heapSort=" + Arrays.toString(hs)); // 打印输出
    }
    MaxHeap h = new MaxHeap(); // 把 new MaxHeap(); 写入 MaxHeap h
    for (int v : new int[] {4, 1, 9, 3}) h.push(v); // 把 值 压入栈/数组尾部
    List<Integer> pops = new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<Integer> pops
    for (int k = 0; k < 4; k++) pops.add(h.pop()); // 让 下标 k 从 0 开始计数，下标 k 小于 4 就继续
    List<Integer> want =
        Arrays.asList(9, 4, 3, 1); // 把 Arrays.asList(9, 4, 3, 1); 写入 List<Integer> want
    if (!pops.equals(want)) { // 若 取反 pops.equals(want
      ok = false;
      System.out.println("FAIL maxHeap pops=" + pops); // 打印输出
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
