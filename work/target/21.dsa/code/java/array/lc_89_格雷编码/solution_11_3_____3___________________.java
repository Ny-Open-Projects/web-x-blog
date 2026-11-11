// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130456218
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class Lc89 { // 定义类型
  List<Integer> grayCode(int n) { // 定义函数/方法 grayCode
    if (n == 0) {
      List<Integer> r = new ArrayList<>();
      r.add(0);
      return r;
    }
    List<String> codes = recursionFn(n); // 把 recursionFn(元素个数); 写入 List<String> codes
    List<Integer> res = new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<Integer> res
    for (String x : codes)
      res.add(Integer.parseInt(x, 2)); // for (String x : codes) 结果 追加 Integer.转整数(x, 2));
    return res; // 返回 结果
  }

  List<String> recursionFn(int k) { // 定义函数/方法 recursionFn
    if (k == 1) {
      List<String> r = new ArrayList<>();
      r.add("0");
      r.add("1");
      return r;
    }
    List<String> prev = recursionFn(k - 1); // 把 recursionFn(下标 k 减 1); 写入 List<String> prev
    List<String> result = new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<String> result
    String prefix = "1" + "0".repeat(k - 1); // 把 「1」 加 「1」.repeat(下标 k 减 1) 存入 prefix
    for (int i = prev.size() - 1; i >= 0; i--) { // 让 下标 i 从 前一个.大小() 减 1 开始计数，下标 i 不低于 0 就继续
      String item = prev.get(i); // 把 前一个 查找 下标 i) 存入 item
      result.add(
          prefix.substring(0, prefix.length() - item.length())
              + item); // 结果 追加 prefix 截取 0, prefix.长度() 减 item.长度()) 加 item);
    }
    List<String> out = new ArrayList<>(prev); // 把 new ArrayList 小于 超过 (前一个); 写入 List<String> out
    out.addAll(result); // out.addAll(结果);
    return out; // 返回 out
  }

  public static void main(String[] args) { // public static void main(String[] args){
    Lc89 s = new Lc89(); // 把 new Lc89(); 写入 Lc89 s
    boolean ok = true; // 把 true; 写入 boolean ok
    List<Integer> g0 = s.grayCode(0);
    if (!(g0.size() == 1 && g0.get(0) == 0)) {
      ok = false;
      System.out.println("FAIL0");
    } // 打印输出
    List<Integer> g1 = s.grayCode(1);
    if (!(g1.size() == 2 && g1.get(0) == 0 && g1.get(1) == 1)) {
      ok = false;
      System.out.println("FAIL1");
    } // 打印输出
    List<Integer> g2 = s.grayCode(2); // 把 字符串.grayCode(2); 写入 List<Integer> g2
    int[] w = {0, 1, 3, 2}; // 把 {0,1,3,2}; 写入 int[] w
    if (g2.size() != 4) {
      ok = false;
      System.out.println("FAIL2size");
    } // 若 g2.大小() 不等于 4){ok 赋值为 false;System.out.输出(「FAIL2size」);}
    else
      for (int i = 0; i < 4; i++)
        if (g2.get(i) != w[i]) {
          ok = false;
          System.out.println("FAIL2v");
        } // 否则
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
