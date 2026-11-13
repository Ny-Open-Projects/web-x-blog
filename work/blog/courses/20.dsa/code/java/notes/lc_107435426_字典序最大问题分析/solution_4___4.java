// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107435426
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class Lc107 { // 定义类型
  List<Integer> getResult(int n, int[] ele) { // 定义函数/方法 getResult
    List<Integer> ans =
        new ArrayList<Integer>(); // 把 new ArrayList 小于 Integer 超过 (); 写入 List<Integer> ans
    ArrayDeque<Integer> stack = new ArrayDeque<Integer>();
    int[] maxElement = new int[n]; // 把 new int[元素个数]; 写入 int[] maxElement
    maxElement[n - 1] = ele[n - 1]; // 把 ele[元素个数 减 1]; 写入 maxElement[n - 1]
    for (int i = n - 2; i >= 0; i--)
      maxElement[i] = Math.max(maxElement[i + 1], ele[i]); // 让 下标 i 从 元素个数 减 2 开始计数，下标 i 不低于 0 就继续
    int i = 0; // 把 0 存入 下标 i
    while (i < n) { // 循环，直到不满足「下标 i 小于 元素个数」
      int mx = maxElement[i]; // 把 maxElement[下标 i] 存入 mx
      if (!stack.isEmpty() && ele[stack.peek()] > mx) { // 若 取反 栈.isEmpty() 且 ele[栈.peek()] 超过 mx
        ans.add(ele[stack.pop()]); // 弹出栈顶元素
      } else { // 否则
        while (mx != ele[i]) { // 循环，直到不满足「mx 不等于 ele[下标 i]」
          stack.push(i); // 把 下标 i 压入栈/数组尾部
          i++; // 下标 i 加一
        }
        ans.add(ele[i]); // 答案 追加 ele[下标 i]);
        i++; // 下标 i 加一
      }
    }
    while (!stack.isEmpty())
      ans.add(ele[stack.pop()]); // 循环，直到不满足「取反 栈.isEmpty()) 答案 追加 ele[栈 弹出 )]);」
    return ans; // 返回 答案
  }

  int rangeMax(int[] ele, int i) { // 定义函数/方法 rangeMax
    int mx = ele[i]; // 把 ele[下标 i] 存入 mx
    for (int j = i + 1; j < ele.length; j++)
      if (ele[j] > mx) mx = ele[j]; // 让 下标 j 从 下标 i 加 1 开始计数，下标 j 小于 ele.长度 就继续
    return mx; // 返回 mx
  }

  List<Integer> suffixMax(int[] ele) { // 定义函数/方法 suffixMax
    int n = ele.length; // 把 ele.长度 存入 元素个数
    List<Integer> res =
        new ArrayList<Integer>(); // 把 new ArrayList 小于 Integer 超过 (); 写入 List<Integer> res
    for (int x = 0; x < n; x++) res.add(0); // 让 x 从 0 开始计数，x 小于 元素个数 就继续
    res.set(n - 1, ele[n - 1]); // 结果.set(元素个数 减 1, ele[元素个数 减 1]);
    for (int i = n - 2; i >= 0; i--)
      res.set(i, Math.max(res.get(i + 1), ele[i])); // 让 下标 i 从 元素个数 减 2 开始计数，下标 i 不低于 0 就继续
    return res; // 返回 结果
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    Lc107 s = new Lc107(); // 把 new Lc107(); 写入 Lc107 s
    boolean ok = true; // 把 true; 写入 boolean ok
    List<Integer> a = s.getResult(5, new int[] {4, 1, 3, 5, 2});
    if (!a.equals(Arrays.asList(5, 3, 2, 1, 4))) {
      ok = false;
      System.out.println("FAIL getResult1 " + a);
    }
    List<Integer> a2 = s.getResult(4, new int[] {3, 1, 4, 2});
    if (!a2.equals(Arrays.asList(4, 2, 1, 3))) {
      ok = false;
      System.out.println("FAIL getResult2 " + a2);
    }
    if (s.rangeMax(new int[] {4, 1, 3, 5, 2}, 0) != 5) {
      ok = false;
      System.out.println("FAIL rangeMax");
    }
    if (!s.suffixMax(new int[] {4, 1, 3, 5, 2}).equals(Arrays.asList(5, 5, 5, 5, 2))) {
      ok = false;
      System.out.println("FAIL suffixMax");
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
