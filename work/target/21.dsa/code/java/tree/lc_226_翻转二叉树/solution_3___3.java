// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134625776
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class Lc226 { // 定义类型
  static class TreeNode {
    int val;
    TreeNode left, right;

    TreeNode(int v) {
      val = v;
    }
  }

  TreeNode invertTree(TreeNode root) { // 定义函数/方法 invertTree
    if (root == null) return null; // 若 根节点 等于 null，直接返回 null
    Deque<TreeNode> st = new ArrayDeque<>(); // 把 new ArrayDeque 小于 超过 (); 写入 Deque<TreeNode> st
    st.push(root); // 把 根节点 压入栈/数组尾部
    while (!st.isEmpty()) { // 循环，直到不满足「取反 st.isEmpty(」
      TreeNode node = st.pop(); // 弹出栈顶元素
      TreeNode t = node.left;
      node.left = node.right;
      node.right = t; // 把 节点.左边界; 节点.左边界 赋值为 节点.右边界; 节点.右边界 赋值为 另一字符串; 写入 TreeNode t
      if (node.left != null) st.push(node.left); // 若 节点.左边界 不等于 null) st 追加 节点.左边界);
      if (node.right != null) st.push(node.right); // 若 节点.右边界 不等于 null) st 追加 节点.右边界);
    }
    return root; // 返回 根节点
  }

  TreeNode build(Integer[] vals) { // 定义函数/方法 build
    if (vals.length == 0 || vals[0] == null)
      return null; // 若 vals.长度 等于 0 或 vals[0] 等于 null，直接返回 null
    TreeNode root = new TreeNode(vals[0]); // 把 new TreeNode(vals[0]); 写入 TreeNode root
    Deque<TreeNode> q = new ArrayDeque<>();
    q.offer(root);
    int i = 1; // 把 1 存入 下标 i
    while (i < vals.length) { // 循环，直到不满足「下标 i 小于 vals.长度」
      TreeNode node = q.poll(); // 把 节点.poll(); 写入 TreeNode node
      if (vals[i] != null) {
        node.left = new TreeNode(vals[i]);
        q.offer(node.left);
      }
      i++; // 下标 i 加一
      if (i < vals.length) { // 若 下标 i 小于 vals.长度
        if (vals[i] != null) {
          node.right = new TreeNode(vals[i]);
          q.offer(node.right);
        }
        i++; // 下标 i 加一
      }
    }
    return root; // 返回 根节点
  }

  List<Integer> toList(TreeNode root) { // 定义函数/方法 toList
    List<Integer> res = new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<Integer> res
    if (root == null) return res; // 若 根节点 等于 null，直接返回 结果
    LinkedList<TreeNode> q = new LinkedList<>();
    q.offer(root);
    while (!q.isEmpty()) { // 循环，直到不满足「取反 节点.isEmpty(」
      TreeNode n = q.poll(); // 把 节点.poll(); 写入 TreeNode n
      if (n != null) {
        res.add(n.val);
        q.offer(n.left);
        q.offer(n.right);
      } else res.add(null); // 否则
    }
    while (!res.isEmpty() && res.get(res.size() - 1) == null) res.remove(res.size() - 1);
    return res; // 返回 结果
  }

  public static void main(String[] args) { // public static void main(String[] args){
    Lc226 s = new Lc226(); // 把 new Lc226(); 写入 Lc226 s
    TreeNode root =
        s.build(
            new Integer[] {
              4, 2, 7, 1, 3, 6, 9
            }); // 把 字符串.build(new Integer[]{4,2,7,1,3,6,9}); 写入 TreeNode root
    List<Integer> got =
        s.toList(s.invertTree(root)); // 把 字符串.toList(字符串.invertTree(根节点)); 写入 List<Integer> got
    List<Integer> want =
        Arrays.asList(4, 7, 2, 9, 6, 3, 1); // 把 Arrays.asList(4,7,2,9,6,3,1); 写入 List<Integer> want
    boolean ok = true; // 把 true; 写入 boolean ok
    if (got.size() != want.size()) ok = false; // 若 got.大小() 不等于 want.大小()) ok 赋值为 false;
    else
      for (int i = 0; i < want.size(); i++) if (!want.get(i).equals(got.get(i))) ok = false; // 否则
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
