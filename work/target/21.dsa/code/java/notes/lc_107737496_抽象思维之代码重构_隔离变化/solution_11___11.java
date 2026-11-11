// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496
package com.webfault.dsa; // 引入依赖

// 忠实翻译 python solution_11：规则类，不同字符表示不同前进命令，循环使用
class Main { // 定义类型

  static class Rule { // static class Rule {
    final char[] data; // final char[] data;
    int idx; // int idx;
    final int length; // final int 长度;

    Rule(String r) { // Rule(String 右指针) {
      this.data = r.toCharArray(); // 把 右指针.toCharArray(); 写入 this.data
      this.idx = 0; // 把 0; 写入 this.idx
      this.length = this.data.length; // 把 this.data.长度; 写入 长度
    }

    char next() { // 定义函数/方法 next
      char ch = data[idx]; // 把 data[idx]; 写入 char ch
      idx = (idx + 1) % length; // 把 (idx 加 1) 对…取模 长度; 写入 idx
      return ch; // 返回 字符
    }

    char peek() { // 定义函数/方法 peek
      return data[idx]; // 返回 data[idx]
    }
  }

  static String take(Rule r, int n) { // 定义函数/方法 take
    StringBuilder sb = new StringBuilder(); // 把 new StringBuilder(); 写入 StringBuilder sb
    for (int i = 0; i < n; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
      sb.append(r.next()); // 把 右指针.下一个( 追加到列表尾部
    }
    return sb.toString(); // 返回 sb.toString()
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    boolean ok = true; // 把 true; 写入 boolean ok

    Rule r = new Rule("ESVM"); // 把 new Rule(「ESVM」); 写入 Rule r
    if (r.peek() != 'E') { // 若 右指针.peek() 不等于 'E'
      ok = false; // 把 false; 写入 ok
      System.out.println("FAIL peek(ESVM)=" + r.peek() + " want E"); // 打印输出
    }
    String gotA = take(r, 10); // 把 take(右指针, 10) 存入 gotA
    if (!gotA.equals("ESVMESVMES")) { // 若 取反 gotA.equals(「ESVMESVMES」
      ok = false; // 把 false; 写入 ok
      System.out.println("FAIL Rule(ESVM)x10=" + gotA + " want ESVMESVMES"); // 打印输出
    }

    Rule r2 = new Rule("semv"); // 把 new Rule(「semv」); 写入 Rule r2
    if (r2.peek() != 's') { // 若 r2.peek() 不等于 '字符串'
      ok = false; // 把 false; 写入 ok
      System.out.println("FAIL peek(semv)=" + r2.peek() + " want s"); // 打印输出
    }
    String gotB = take(r2, 6); // 把 take(r2, 6) 存入 gotB
    if (!gotB.equals("semvse")) { // 若 取反 gotB.equals(「semvse」
      ok = false; // 把 false; 写入 ok
      System.out.println("FAIL Rule(semv)x6=" + gotB + " want semvse"); // 打印输出
    }

    if (!ok) { // 若 取反 ok
      throw new RuntimeException("FAILED"); // throw new RuntimeException(「FAILED」);
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
