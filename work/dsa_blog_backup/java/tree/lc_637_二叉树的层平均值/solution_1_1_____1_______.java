// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145091296
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc637_solution_1_1_____1_______ { // 定义类型
  static class TreeNode { // static class TreeNode {
    int val; // int 值;
    TreeNode left; // TreeNode 左边界;
    TreeNode right; // TreeNode 右边界;

    TreeNode(int v) {
      val = v;
    } // 把 值; } 写入 TreeNode(int v) { val
  }

  public List<Double> averageOfLevels(TreeNode root) { // 定义函数/方法 averageOfLevels
    List<Double> res = new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<Double> res
    if (root == null) return res; // 若 根节点 等于 null，直接返回 结果
    Deque<TreeNode> q = new ArrayDeque<>(); // 把 new ArrayDeque 小于 超过 (); 写入 Deque<TreeNode> q
    q.offer(root); // 节点.offer(根节点);
    while (!q.isEmpty()) { // 循环，直到不满足「取反 节点.isEmpty(」
      int size = q.size(); // 把 节点.大小() 存入 大小
      double sum = 0; // 把 0 存入 累计和
      for (int i = 0; i < size; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 大小 就继续
        TreeNode n = q.poll(); // 把 节点.poll(); 写入 TreeNode n
        sum += n.val; // 累计和累加 元素个数.值
        if (n.left != null) q.offer(n.left); // 若 元素个数.左边界 不等于 null) 节点.offer(元素个数.左边界);
        if (n.right != null) q.offer(n.right); // 若 元素个数.右边界 不等于 null) 节点.offer(元素个数.右边界);
      }
      res.add(sum / size); // 结果 追加 累计和 除以 大小);
    }
    return res; // 返回 结果
  }

  static TreeNode build(Integer[] vals) { // 定义函数/方法 build
    if (vals.length == 0 || vals[0] == null)
      return null; // 若 vals.长度 等于 0 或 vals[0] 等于 null，直接返回 null
    TreeNode root = new TreeNode(vals[0]); // 把 new TreeNode(vals[0]); 写入 TreeNode root
    Queue<TreeNode> q = new ArrayDeque<>(); // 把 new ArrayDeque 小于 超过 (); 写入 Queue<TreeNode> q
    q.offer(root); // 节点.offer(根节点);
    int i = 1; // 把 1 存入 下标 i
    while (!q.isEmpty() && i < vals.length) { // 循环，直到不满足「取反 节点.isEmpty() 且 下标 i 小于 vals.长度」
      TreeNode n = q.poll(); // 把 节点.poll(); 写入 TreeNode n
      if (i < vals.length && vals[i] != null) { // 若 下标 i 小于 vals.长度 且 vals[下标 i] 不等于 null
        n.left = new TreeNode(vals[i]); // 把 new TreeNode(vals[下标 i]); 写入 左边界
        q.offer(n.left); // 节点.offer(元素个数.左边界);
      }
      i++; // 下标 i 加一
      if (i < vals.length && vals[i] != null) { // 若 下标 i 小于 vals.长度 且 vals[下标 i] 不等于 null
        n.right = new TreeNode(vals[i]); // 把 new TreeNode(vals[下标 i]); 写入 右边界
        q.offer(n.right); // 节点.offer(元素个数.右边界);
      }
      i++; // 下标 i 加一
    }
    return root; // 返回 根节点
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    lc637_solution_1_1_____1_______ s = new lc637_solution_1_1_____1_______();
    Object[][] cases = { // 把 { 写入 Object[][] cases
      {new Integer[] {3, 9, 20, 15, 7}, new Double[] {3.0, 14.5, 11.0}},
      {new Integer[] {5}, new Double[] {5.0}},
      {new Integer[] {1, 2, 3}, new Double[] {1.0, 2.5}},
    };
    boolean ok = true; // 把 true; 写入 boolean ok
    for (Object[] c : cases) { // for (Object[] 字符 : cases) {
      List<Double> got = s.averageOfLevels(build((Integer[]) c[0]));
      Double[] want = (Double[]) c[1]; // 把 (Double[]) 字符[1]; 写入 Double[] want
      if (got.size() != want.length) { // 若 got.大小() 不等于 want.长度
        ok = false; // 把 false; 写入 ok
        System.out.println("FAIL size got=" + got + " want=" + Arrays.toString(want)); // 打印输出
        continue; // 跳过本轮，进入下一次
      }
      for (int i = 0; i < want.length; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 want.长度 就继续
        if (Math.abs(got.get(i) - want[i])
            > 1e-9) { // 若 Math.取绝对值 got 查找 下标 i) 减 want[下标 i]) 超过 1e 减 9
          ok = false; // 把 false; 写入 ok
          System.out.println(
              "FAIL averageOfLevels got=" + got + " want=" + Arrays.toString(want)); // 打印输出
          break; // 跳出循环
        }
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
