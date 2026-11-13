// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133920771
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc65_solution522 { // 定义类型
  public boolean isNumber(String s) { // 定义判定函数 isNumber
    Map<String, Map<String, Integer>> graph = new HashMap<>();
    graph.put(
        "0",
        new HashMap<String, Integer>() {
          {
            put("blank", 0);
            put("sign", 1);
            put(".", 2);
            put("digit", 6);
          }
        });
    graph.put(
        "1",
        new HashMap<String, Integer>() {
          {
            put("digit", 6);
            put(".", 2);
          }
        });
    graph.put(
        "2",
        new HashMap<String, Integer>() {
          {
            put("digit", 3);
          }
        });
    graph.put(
        "3",
        new HashMap<String, Integer>() {
          {
            put("digit", 3);
            put("e", 4);
          }
        });
    graph.put(
        "4",
        new HashMap<String, Integer>() {
          {
            put("digit", 5);
            put("sign", 7);
          }
        });
    graph.put(
        "5",
        new HashMap<String, Integer>() {
          {
            put("digit", 5);
          }
        });
    graph.put(
        "6",
        new HashMap<String, Integer>() {
          {
            put("digit", 6);
            put(".", 3);
            put("e", 4);
          }
        });
    graph.put(
        "7",
        new HashMap<String, Integer>() {
          {
            put("digit", 5);
          }
        });

    String state = "0"; // 把 「0」 存入 state
    for (char ch : s.trim().toCharArray()) { // for (char 字符 : 字符串.trim().toCharArray()) {
      String c; // String 字符;
      if (ch >= '0' && ch <= '9') c = "digit"; // 若 字符 不低于 '0' 且 字符 不超过 '9') 字符 赋值为 「digit」;
      else if (ch == ' ') c = "blank"; // 否则，若 字符 等于 ' ') 字符 赋值为 「blank」;
      else if (ch == '+' || ch == '-') c = "sign"; // 否则，若 字符 等于 ' 加 ' 或 字符 等于 ' 减 ') 字符 赋值为 「sign」;
      else if (ch == '.') c = "."; // 否则，若 字符 等于 '.') 字符 赋值为 「.」;
      else if (ch == 'e' || ch == 'E') c = "e"; // 否则，若 字符 等于 'e' 或 字符 等于 'E') 字符 赋值为 「e」;
      else return false; // 否则
      Integer next = graph.get(state).get(c); // 把 graph 查找 state) 查找 字符) 存入 下一个
      if (next == null) return false; // 若 下一个 等于 null，直接返回 false
      state = String.valueOf(next); // 把 String.valueOf(下一个); 写入 state
    }
    return state.equals("3")
        || state.equals("5")
        || state.equals("6"); // 返回 state.equals(「3」) 或 state.equals(「3」) 或 state.equals(「3」)
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    lc65_solution522 s = new lc65_solution522(); // 把 new lc65_solution522(); 写入 lc65_solution522 s
    String[] tests = {
      "0", "abc", "2.5", "1e10", ".", "e9", " ", "4e", "++1", "2.", "1.2.3", "+5", "46.e3", "1e",
      "-1.", "3e+2"
    };
    boolean[] wants = {
      true, false, true, true, false, false, false, false, false, true, false, true, true, false,
      true, true
    };
    for (int i = 0; i < tests.length; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 tests.长度 就继续
      if (s.isNumber(tests[i]) != wants[i]) { // 若 字符串.isNumber(tests[下标 i]) 不等于 wants[下标 i]
        System.out.println("FAIL isNumber(" + tests[i] + ") want " + wants[i]); // 打印输出
        throw new RuntimeException("FAILED"); // throw new RuntimeException(「FAILED」);
      }
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
