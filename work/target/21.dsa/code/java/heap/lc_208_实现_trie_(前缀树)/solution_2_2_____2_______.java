// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145248170
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc208_solution222 { // 定义类型
  static class Trie { // static class Trie {
    Map<String, Object> root =
        new HashMap<>(); // 把 new HashMap 小于 超过 (); 写入 Map<String, Object> root

    void insert(String word) { // 定义函数/方法 insert
      Map<String, Object> node = root; // 把 根节点; 写入 Map<String, Object> node
      for (char ch : word.toCharArray()) { // for (char 字符 : 单词.toCharArray()) {
        String s = String.valueOf(ch); // 把 String.valueOf(字符) 存入 字符串
        if (!node.containsKey(s)) node.put(s, new HashMap<String, Object>());
        node = (Map<String, Object>) node.get(s); // 把 (Map 小于 String, Object 超过 ) 节点 查找 字符串); 写入 节点
      }
      node.put("end", true); // 节点.put(「终点」, true);
    }

    boolean search(String word) { // 定义函数/方法 search
      Map<String, Object> node =
          startsWithNode(word); // 把 startsWithNode(单词); 写入 Map<String, Object> node
      return node != null && node.containsKey("end") && Boolean.TRUE.equals(node.get("end"));
    }

    boolean startsWith(String prefix) { // 定义函数/方法 startsWith
      return startsWithNode(prefix) != null; // 返回 startsWithNode(prefix) 不等于 null
    }

    Map<String, Object> startsWithNode(
        String prefix) { // Map 小于 String, Object 超过 startsWithNode(String prefix) {
      Map<String, Object> node = root; // 把 根节点; 写入 Map<String, Object> node
      for (char ch : prefix.toCharArray()) { // for (char 字符 : prefix.toCharArray()) {
        String s = String.valueOf(ch); // 把 String.valueOf(字符) 存入 字符串
        if (!node.containsKey(s)) return null; // 若 取反 节点.containsKey(字符串)，直接返回 null
        node = (Map<String, Object>) node.get(s); // 把 (Map 小于 String, Object 超过 ) 节点 查找 字符串); 写入 节点
      }
      return node; // 返回 节点
    }
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    Trie trie = new Trie(); // 把 new Trie(); 写入 Trie trie
    trie.insert("apple"); // trie 插入 「apple」);
    if (!trie.search("apple")) throw new RuntimeException("FAILED search apple");
    if (trie.search("app"))
      throw new RuntimeException(
          "FAILED search app"); // 若 trie.search(「app」)) throw new RuntimeException(「app」);
    if (!trie.startsWith("app")) throw new RuntimeException("FAILED startsWith app");
    trie.insert("app"); // trie 插入 「app」);
    if (!trie.search("app"))
      throw new RuntimeException(
          "FAILED search app2"); // 若 取反 trie.search(「app」)) throw new RuntimeException(「app」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
