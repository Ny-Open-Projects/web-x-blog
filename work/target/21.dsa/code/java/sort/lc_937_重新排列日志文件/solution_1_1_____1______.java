// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145374559
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class ReorderS1 { // 定义类型
  static String[] reorderLogFiles(String[] logs) { // 定义函数/方法 reorderLogFiles
    List<String> letterLogs =
        new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<String> letterLogs
    List<String> digitLogs =
        new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<String> digitLogs
    for (String log : logs) { // for (String log : logs) {
      int sp = log.indexOf(' '); // 把 log 查找 ' ') 存入 sp
      String content = log.substring(sp + 1); // 把 log 截取 sp 加 1) 存入 content
      if (content.charAt(0) >= '0' && content.charAt(0) <= '9') digitLogs.add(log);
      else letterLogs.add(log); // 否则
    }
    letterLogs.sort(
        (a, b) -> { // 排序
          String ca = a.substring(a.indexOf(' ') + 1); // 把 数组 截取 数组 查找 ' ') 加 1) 存入 ca
          String cb = b.substring(b.indexOf(' ') + 1); // 把 b 截取 b 查找 ' ') 加 1) 存入 cb
          int cmp = ca.compareTo(cb); // 把 ca.compareTo(cb) 存入 cmp
          if (cmp != 0) return cmp; // 若 cmp 不等于 0，直接返回 cmp
          return a.substring(0, a.indexOf(' '))
              .compareTo(
                  b.substring(
                      0, b.indexOf(' '))); // 返回 数组 截取 0, 数组 查找 ' ')).compareTo(b 截取 0, b 查找 ' ')))
        }); // });
    List<String> result =
        new ArrayList<>(letterLogs); // 把 new ArrayList 小于 超过 (letterLogs); 写入 List<String> result
    result.addAll(digitLogs); // 结果.addAll(digitLogs);
    return result.toArray(new String[0]); // 返回 结果.toArray(new String[0])
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    String[] logs = {
      "dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"
    };
    String[] got =
        ReorderS1.reorderLogFiles(logs); // 把 ReorderS1.reorderLogFiles(logs); 写入 String[] got
    String[] want = {
      "let1 art can", "let3 art zero", "let2 own kit dig", "dig1 8 1 5 1", "dig2 3 6"
    };
    boolean ok = Arrays.equals(got, want); // 把 Arrays.equals(got, want); 写入 boolean ok
    if (!ok) {
      System.out.println("FAIL " + Arrays.toString(got));
      throw new RuntimeException("FAILED");
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
