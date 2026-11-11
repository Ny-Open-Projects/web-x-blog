// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145091772
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc701_solution_1_1_____1___ { // 定义类型
  static class TreeNode { // static class TreeNode {
    int val; // int 值;
    TreeNode left, right; // TreeNode 左边界, 右边界;

    TreeNode(int v) {
      val = v;
    } // 把 值; } 写入 TreeNode(int v) { val
  }

  public TreeNode insertIntoBST(TreeNode root, int val) { // 定义函数/方法 insertIntoBST
    if (root == null) return new TreeNode(val); // 若 根节点 等于 null，直接返回 new TreeNode(值)
    TreeNode pos = root; // 把 根节点; 写入 TreeNode pos
    while (pos != null) { // 循环，直到不满足「pos 不等于 null」
      if (val < pos.val) { // 若 值 小于 pos.值
        if (pos.left == null) { // 若 pos.左边界 等于 null
          pos.left = new TreeNode(val); // 把 new TreeNode(值); 写入 左边界
          break; // 跳出循环
        } else { // 否则
          pos = pos.left; // 把 pos.左边界; 写入 pos
        }
      } else { // 否则
        if (pos.right == null) { // 若 pos.右边界 等于 null
          pos.right = new TreeNode(val); // 把 new TreeNode(值); 写入 右边界
          break; // 跳出循环
        } else { // 否则
          pos = pos.right; // 把 pos.右边界; 写入 pos
        }
      }
    }
    return root; // 返回 根节点
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

  static List<Integer> toList(TreeNode root) { // 定义函数/方法 toList
    List<Integer> res = new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<Integer> res
    Deque<TreeNode> stack =
        new ArrayDeque<>(); // 把 new ArrayDeque 小于 超过 (); 写入 Deque<TreeNode> stack
    stack.push(root); // 把 根节点 压入栈/数组尾部
    while (!stack.isEmpty()) { // 循环，直到不满足「取反 栈.isEmpty(」
      TreeNode node = stack.pop(); // 弹出栈顶元素
      if (node != null) { // 若 节点 不等于 null
        res.add(node.val); // 结果 追加 节点.值);
        if (node.right != null) stack.push(node.right); // 若 节点.右边界 不等于 null) 栈 追加 节点.右边界);
        if (node.left != null) stack.push(node.left); // 若 节点.左边界 不等于 null) 栈 追加 节点.左边界);
      }
    }
    return res; // 返回 结果
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    lc701_solution_1_1_____1___ s = new lc701_solution_1_1_____1___();
    Object[][] cases = { // 把 { 写入 Object[][] cases
      {new Integer[] {4, 2, 7, 1, 3}, 5, Arrays.asList(4, 2, 1, 3, 7, 5)},
      {null, 5, Arrays.asList(5)},
      {new Integer[] {8, 4, null, 2}, 6, Arrays.asList(8, 4, 2, 6)},
    };
    boolean ok = true; // 把 true; 写入 boolean ok
    for (Object[] c : cases) { // for (Object[] 字符 : cases) {
      TreeNode root = c[0] == null ? null : build((Integer[]) c[0]);
      List<Integer> got = toList(s.insertIntoBST(root, (Integer) c[1]));
      @SuppressWarnings("unchecked") // @SuppressWarnings(「unchecked」)
      List<Integer> want =
          (List<Integer>) c[2]; // 把 (List 小于 Integer 超过 ) 字符[2]; 写入 List<Integer> want
      if (!got.equals(want)) { // 若 取反 got.equals(want
        ok = false; // 把 false; 写入 ok
        System.out.println("FAIL insertIntoBST got=" + got + " want=" + want); // 打印输出
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
