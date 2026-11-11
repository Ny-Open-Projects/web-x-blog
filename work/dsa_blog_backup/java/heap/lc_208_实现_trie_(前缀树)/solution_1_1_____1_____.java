// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145248170
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc208_solution111 { // 定义类型
  static class TrieNode { // static class TrieNode {
    Map<Character, TrieNode> children =
        new HashMap<>(); // 把 new HashMap 小于 超过 (); 写入 Map<Character, TrieNode> children
    boolean isEnd = false; // 把 false; 写入 boolean isEnd
  }

  static class Trie { // static class Trie {
    TrieNode root = new TrieNode(); // 把 new TrieNode(); 写入 TrieNode root

    void insert(String word) { // 定义函数/方法 insert
      TrieNode node = root; // 把 根节点; 写入 TrieNode node
      for (char ch : word.toCharArray()) { // for (char 字符 : 单词.toCharArray()) {
        node.children.putIfAbsent(
            ch, new TrieNode()); // 节点.children.putIfAbsent(字符, new TrieNode());
        node = node.children.get(ch); // 把 节点.children 查找 字符); 写入 节点
      }
      node.isEnd = true; // 把 true; 写入 node.isEnd
    }

    boolean search(String word) { // 定义函数/方法 search
      TrieNode node = searchPrefix(word); // 把 searchPrefix(单词); 写入 TrieNode node
      return node != null && node.isEnd; // 返回 节点 不等于 null 且 节点.isEnd
    }

    boolean startsWith(String prefix) { // 定义函数/方法 startsWith
      return searchPrefix(prefix) != null; // 返回 searchPrefix(prefix) 不等于 null
    }

    TrieNode searchPrefix(String prefix) { // 定义函数/方法 searchPrefix
      TrieNode node = root; // 把 根节点; 写入 TrieNode node
      for (char ch : prefix.toCharArray()) { // for (char 字符 : prefix.toCharArray()) {
        if (!node.children.containsKey(ch))
          return null; // 若 取反 节点.children.containsKey(字符)，直接返回 null
        node = node.children.get(ch); // 把 节点.children 查找 字符); 写入 节点
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
