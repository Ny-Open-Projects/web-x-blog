// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130743564
package com.webfault.dsa; // 引入依赖

import java.util.ArrayList; // 引入依赖
import java.util.List; // 引入依赖

// 忠实翻译 python solution_6：Morris 中序遍历（临时接右指针，用完即拆）
class Main { // 定义类型

  static class TreeNode { // static class TreeNode {
    int val; // int 值;
    TreeNode left; // TreeNode 左边界;
    TreeNode right; // TreeNode 右边界;

    TreeNode(int v) { // TreeNode(int 值) {
      this.val = v; // 把 值; 写入 值
    }
  }

  static List<Integer> inorderTraversal(TreeNode root) { // 定义函数/方法 inorderTraversal
    List<Integer> res =
        new ArrayList<Integer>(); // 把 new ArrayList 小于 Integer 超过 (); 写入 List<Integer> res
    TreeNode cur = root; // 把 根节点; 写入 TreeNode cur
    while (cur != null) { // 循环，直到不满足「当前值 不等于 null」
      if (cur.left == null) { // 若 当前值.左边界 等于 null
        res.add(cur.val); // 结果 追加 当前值.值);
        cur = cur.right; // 把 当前值.右边界; 写入 当前值
      } else { // 否则
        TreeNode pred = cur.left; // 把 当前值.左边界; 写入 TreeNode pred
        while (pred.right != null
            && pred.right != cur) { // 循环，直到不满足「pred.右边界 不等于 null 且 pred.右边界 不等于 当前值」
          pred = pred.right; // 把 pred.右边界; 写入 pred
        }
        if (pred.right == null) { // 若 pred.右边界 等于 null
          pred.right = cur; // 把 当前值; 写入 右边界
          cur = cur.left; // 把 当前值.左边界; 写入 当前值
        } else { // 否则
          pred.right = null; // 把 null; 写入 右边界
          res.add(cur.val); // 结果 追加 当前值.值);
          cur = cur.right; // 把 当前值.右边界; 写入 当前值
        }
      }
    }
    return res; // 返回 结果
  }

  static TreeNode buildTree(Integer[] vals) { // 定义函数/方法 buildTree
    if (vals == null || vals.length == 0) { // 若 vals 等于 null 或 vals.长度 等于 0
      return null; // 返回 null
    }
    TreeNode root = new TreeNode(vals[0]); // 把 new TreeNode(vals[0]); 写入 TreeNode root
    List<TreeNode> q =
        new ArrayList<TreeNode>(); // 把 new ArrayList 小于 TreeNode 超过 (); 写入 List<TreeNode> q
    q.add(root); // 节点 追加 根节点);
    int i = 1; // 把 1 存入 下标 i
    while (i < vals.length) { // 循环，直到不满足「下标 i 小于 vals.长度」
      TreeNode node = q.remove(0); // 把 节点 弹出 0); 写入 TreeNode node
      if (vals[i] != null) { // 若 vals[下标 i] 不等于 null
        node.left = new TreeNode(vals[i]); // 把 new TreeNode(vals[下标 i]); 写入 左边界
        q.add(node.left); // 节点 追加 节点.左边界);
      }
      i++; // 下标 i 加一
      if (i < vals.length) { // 若 下标 i 小于 vals.长度
        if (vals[i] != null) { // 若 vals[下标 i] 不等于 null
          node.right = new TreeNode(vals[i]); // 把 new TreeNode(vals[下标 i]); 写入 右边界
          q.add(node.right); // 节点 追加 节点.右边界);
        }
        i++; // 下标 i 加一
      }
    }
    return root; // 返回 根节点
  }

  static boolean eq(List<Integer> a, int[] b) { // 定义函数/方法 eq
    if (a.size() != b.length) { // 若 数组.大小() 不等于 b.长度
      return false; // 返回 false
    }
    for (int i = 0; i < b.length; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 b.长度 就继续
      if (a.get(i).intValue() != b[i]) { // 若 数组 查找 下标 i).intValue() 不等于 b[下标 i]
        return false; // 返回 false
      }
    }
    return true; // 返回 true
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    boolean ok = true; // 把 true; 写入 boolean ok
    Integer[][] inputs = { // 把 { 写入 Integer[][] inputs
      {1, null, 2, null, 3},
      {1, 2, 3, 4},
    };
    int[][] wants = { // 把 { 写入 int[][] wants
      {1, 2, 3},
      {4, 2, 1, 3},
    };
    for (int k = 0; k < inputs.length; k++) { // 让 下标 k 从 0 开始计数，下标 k 小于 inputs.长度 就继续
      List<Integer> got = inorderTraversal(buildTree(inputs[k]));
      if (!eq(got, wants[k])) { // 若 取反 eq(got, wants[下标 k]
        ok = false; // 把 false; 写入 ok
        System.out.println(
            "FAIL inorderTraversal("
                + java.util.Arrays.toString(inputs[k])
                + ")="
                + got // 打印输出
                + " want "
                + java.util.Arrays.toString(
                    wants[k])); // 加 「 want 」 加 java.util.Arrays.toString(wants[下标 k]));
      }
    }
    if (!eq(inorderTraversal(null), new int[] {})) { // 若 取反 eq(inorderTraversal(null), new int[] {}
      ok = false; // 把 false; 写入 ok
      System.out.println("FAIL inorderTraversal(null) 非空"); // 打印输出
    }
    if (!ok) { // 若 取反 ok
      throw new RuntimeException("FAILED"); // throw new RuntimeException(「FAILED」);
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
