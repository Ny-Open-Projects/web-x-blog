// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135037359
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc93_solution33 { // 定义类型
  public List<String> restoreIpAddresses(String s) { // 定义函数/方法 restoreIpAddresses
    List<String> res = new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<String> res
    backtrack(0, new ArrayList<>(), s, res); // backtrack(0, new ArrayList 小于 超过 (), 字符串, 结果);
    return res; // 返回 结果
  }

  private void backtrack(
      int start, List<String> path, String s, List<String> res) { // 定义函数/方法 backtrack
    if (path.size() == 4) { // 若 当前路径.大小() 等于 4
      if (start == s.length()) { // 若 起点 等于 字符串.长度(
        res.add(String.join(".", path)); // 拼接为字符串
      }
      return; // return;
    }
    for (int length = 1; length <= 3; length++) { // 让 长度 从 1 开始计数，长度 不超过 3 就继续
      if (start + length > s.length()) break; // 若 起点 加 长度 超过 字符串.长度()) break;
      String segment = s.substring(start, start + length); // 把 字符串 截取 起点, 起点 加 长度) 存入 segment
      if ((segment.charAt(0) == '0' && segment.length() > 1) || Integer.parseInt(segment) > 255) {
        continue; // 跳过本轮，进入下一次
      }
      path.add(segment); // 当前路径 追加 segment);
      backtrack(start + length, path, s, res); // backtrack(起点 加 长度, 当前路径, 字符串, 结果);
      path.remove(path.size() - 1); // 当前路径 弹出 当前路径.大小() 减 1);
    }
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    lc93_solution33 s = new lc93_solution33(); // 把 new lc93_solution33(); 写入 lc93_solution33 s
    List<String> got =
        s.restoreIpAddresses(
            "25525511135"); // 把 字符串.restoreIpAddresses(「25525511135」); 写入 List<String> got
    List<String> want = Arrays.asList("255.255.11.135", "255.255.111.35");
    if (!got.equals(want)) { // 若 取反 got.equals(want
      System.out.println("FAIL restoreIpAddresses got " + got); // 打印输出
      throw new RuntimeException("FAILED"); // throw new RuntimeException(「FAILED」);
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
