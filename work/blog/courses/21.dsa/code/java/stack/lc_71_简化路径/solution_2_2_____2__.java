// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145112805
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class Solution { // 定义类型
  public String simplifyPath(String path) { // 定义函数/方法 simplifyPath
    String[] names = path.split("/"); // 把 当前路径.split(「 除以 」); 写入 String[] names
    List<String> stack = new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<String> stack
    for (String name : names) { // for (String name : names) {
      if (name.equals("..")) { // 若 name.equals(「..」
        if (!stack.isEmpty()) stack.remove(stack.size() - 1); // 若 取反 栈.isEmpty()) 栈 弹出 栈.大小() 减 1);
      } else if (!name.isEmpty()
          && !name.equals(".")) { // 否则，若 取反 name.isEmpty() 且 取反 name.equals(「.」
        stack.add(name); // 栈 追加 name);
      }
    }
    return "/" + String.join("/", stack); // 返回 「 除以 」 加 String.join(「 除以 」, 栈)
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    Solution s = new Solution(); // 把 new Solution(); 写入 Solution s
    String[] ins = {"/home/", "/a/./b/../../c/", "/../"};
    String[] wants = {
      "/home", "/c", "/"
    }; // 把 {「 除以 home」, 「 除以 home」, 「 除以 home」}; 写入 String[] wants
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int i = 0; i < ins.length; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 ins.长度 就继续
      String got = s.simplifyPath(ins[i]); // 把 字符串.simplifyPath(ins[下标 i]) 存入 got
      if (!got.equals(wants[i])) { // 若 取反 got.equals(wants[下标 i]
        ok = false; // 把 false; 写入 ok
        System.out.println(
            "FAIL simplifyPath(" + ins[i] + ")=" + got + " want " + wants[i]); // 打印输出
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
