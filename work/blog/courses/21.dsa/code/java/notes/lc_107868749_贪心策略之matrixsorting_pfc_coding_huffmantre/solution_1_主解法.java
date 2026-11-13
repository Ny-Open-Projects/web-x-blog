// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107868749
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc107868749_solution1 { // 定义类型
  static int[][] matrixSort(int[][] matrix) { // 定义函数/方法 matrixSort
    int rows = matrix.length, cols = matrix[0].length; // 把 矩阵.长度, 列数 赋值为 矩阵[0].长度 存入 行数
    for (int c = 0; c < cols; c++) { // 让 字符 从 0 开始计数，字符 小于 列数 就继续
      int[] col = new int[rows]; // 把 new int[行数]; 写入 int[] col
      for (int r = 0; r < rows; r++) col[r] = matrix[r][c]; // 让 右指针 从 0 开始计数，右指针 小于 行数 就继续
      Arrays.sort(col); // 排序
      for (int r = 0; r < rows; r++) matrix[r][c] = col[r]; // 让 右指针 从 0 开始计数，右指针 小于 行数 就继续
    }
    for (int r = 0; r < rows; r++) Arrays.sort(matrix[r]); // 让 右指针 从 0 开始计数，右指针 小于 行数 就继续
    return matrix; // 返回 矩阵
  }

  static class Node { // static class Node {
    int weight; // int weight;
    Node left, right; // Node 左边界, 右边界;
    Character ch; // Character 字符;

    Node(int w, Character c) {
      weight = w;
      ch = c;
    } // 把 权重; 字符 赋值为 字符; } 写入 Node(int w, Character c) { weight

    Node(int w, Node l, Node r) {
      weight = w;
      left = l;
      right = r;
    }
  }

  static Node buildHuffman(Map<Character, Integer> freqs) { // 定义函数/方法 buildHuffman
    PriorityQueue<Node> pq = new PriorityQueue<>(Comparator.comparingInt(n -> n.weight));
    for (Map.Entry<Character, Integer> e : freqs.entrySet()) {
      pq.add(new Node(e.getValue(), e.getKey())); // 优先队列 追加 new Node(e.getValue(), e.getKey()));
    }
    while (pq.size() > 1) { // 循环，直到不满足「优先队列.大小() 超过 1」
      Node a = pq.poll(); // 把 优先队列.poll(); 写入 Node a
      Node b = pq.poll(); // 把 优先队列.poll(); 写入 Node b
      pq.add(
          new Node(a.weight + b.weight, a, b)); // 优先队列 追加 new Node(数组.weight 加 b.weight, 数组, b));
    }
    return pq.poll(); // 返回 优先队列.poll()
  }

  static void walk(Node node, String prefix, Map<Character, String> codes) { // 定义函数/方法 walk
    if (node.ch != null) { // 若 节点.字符 不等于 null
      codes.put(
          node.ch,
          prefix.isEmpty() ? "0" : prefix); // codes.put(节点.字符, prefix.isEmpty() ? 「0」 : prefix);
      return; // return;
    }
    walk(node.left, prefix + "0", codes); // walk(节点.左边界, prefix 加 「0」, codes);
    walk(node.right, prefix + "1", codes); // walk(节点.右边界, prefix 加 「1」, codes);
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    int[][] mat = {
      {5, 3, 4}, {1, 6, 2}, {7, 9, 8}
    }; // 把 {{5, 3, 4}, {1, 6, 2}, {7, 9, 8}}; 写入 int[][] mat
    matrixSort(mat); // matrixSort(mat);

    Map<Character, Integer> freqs = new LinkedHashMap<>();
    freqs.put('A', 5);
    freqs.put('B', 9);
    freqs.put('C', 12); // freqs.put('A', 5); freqs.put('B', 9); freqs.put('C', 12);
    freqs.put('D', 13);
    freqs.put('E', 16);
    freqs.put('F', 45); // freqs.put('D', 13); freqs.put('E', 16); freqs.put('F', 45);
    Node root = buildHuffman(freqs); // 把 buildHuffman(freqs); 写入 Node root
    Map<Character, String> codes =
        new HashMap<>(); // 把 new HashMap 小于 超过 (); 写入 Map<Character, String> codes
    walk(root, "", codes); // walk(根节点, 「」, codes);
    int totalBits = 0; // 把 0 存入 totalBits
    for (Map.Entry<Character, Integer> e : freqs.entrySet()) {
      totalBits +=
          e.getValue()
              * codes
                  .get(e.getKey())
                  .length(); // totalBits累加 e.getValue() 乘 codes 查找 e.getKey()).长度()
    }
    if (totalBits != 224) { // 若 totalBits 不等于 224
      System.out.println("FAIL totalBits " + totalBits); // 打印输出
      throw new RuntimeException("FAILED"); // throw new RuntimeException(「FAILED」);
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
