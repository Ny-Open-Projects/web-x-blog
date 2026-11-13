// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144993713
package com.webfault.dsa; // 引入依赖

class ListNode { // 定义类型
  int val; // int 值;
  ListNode next; // ListNode 下一个;

  ListNode(int v) {
    val = v;
  } // 把 值; } 写入 ListNode(int v) { val
}

class TreeNode109 { // 定义类型
  int val; // int 值;
  TreeNode109 left; // TreeNode109 左边界;
  TreeNode109 right; // TreeNode109 右边界;

  TreeNode109(int v) {
    val = v;
  } // 把 值; } 写入 TreeNode109(int v) { val
}

class Main { // 定义类型
  ListNode getMedian(ListNode left, ListNode right) { // 定义函数/方法 getMedian
    ListNode fast = left, slow = left; // 把 左边界, 慢指针 赋值为 左边界; 写入 ListNode fast
    while (fast != right && fast.next != right) {
      fast = fast.next.next;
      slow = slow.next;
    }
    return slow; // 返回 慢指针
  }

  TreeNode109 buildTree(ListNode left, ListNode right) { // 定义函数/方法 buildTree
    if (left == right) return null; // 若 左边界 等于 右边界，直接返回 null
    ListNode mid = getMedian(left, right); // 把 getMedian(左边界, 右边界); 写入 ListNode mid
    TreeNode109 root = new TreeNode109(mid.val); // 把 new TreeNode109(中点.值); 写入 TreeNode109 root
    root.left = buildTree(left, mid); // 把 buildTree(左边界, 中点); 写入 左边界
    root.right = buildTree(mid.next, right); // 把 buildTree(中点.下一个, 右边界); 写入 右边界
    return root; // 返回 根节点
  }

  TreeNode109 sortedListToBST(ListNode head) {
    return buildTree(head, null);
  }

  static ListNode buildList(int[] vals) { // 定义函数/方法 buildList
    ListNode head = null, cur = null; // 把 null, 当前值 赋值为 null; 写入 ListNode head
    for (int v : vals) { // for (int 值 : vals) {
      ListNode n = new ListNode(v); // 把 new ListNode(值); 写入 ListNode n
      if (head == null) head = n;
      else cur.next = n; // 若 头节点 等于 null) 头节点 赋值为 元素个数; else 当前值.下一个 赋值为 元素个数;
      cur = n; // 把 元素个数; 写入 当前值
    }
    return head; // 返回 头节点
  }

  static void inorder(TreeNode109 r, java.util.List<Integer> out) { // 定义函数/方法 inorder
    if (r == null) return; // 若 右指针 等于 null) return;
    inorder(r.left, out); // inorder(右指针.左边界, out);
    out.add(r.val); // out 追加 右指针.值);
    inorder(r.right, out); // inorder(右指针.右边界, out);
  }

  static int height(TreeNode109 r) { // 定义函数/方法 height
    if (r == null) return 0; // 若 右指针 等于 null，直接返回 0
    return 1
        + Math.max(
            height(r.left), height(r.right)); // 返回 1 加 Math.取较大值 height(右指针.左边界), height(右指针.右边界))
  }

  static boolean isBalanced(TreeNode109 r) { // 定义判定函数 isBalanced
    if (r == null) return true; // 若 右指针 等于 null，直接返回 true
    if (Math.abs(height(r.left) - height(r.right)) > 1) return false;
    return isBalanced(r.left)
        && isBalanced(r.right); // 返回 isBalanced(右指针.左边界) 且 isBalanced(右指针.右边界)
  }

  static boolean check(TreeNode109 r, int[] expected) { // 定义判定函数 check
    java.util.List<Integer> io = new java.util.ArrayList<>();
    inorder(r, io); // inorder(右指针, io);
    if (io.size() != expected.length) return false; // 若 io.大小() 不等于 expected.长度，直接返回 false
    for (int i = 0; i < expected.length; i++)
      if (io.get(i) != expected[i]) return false; // 让 下标 i 从 0 开始计数，下标 i 小于 expected.长度 就继续
    return isBalanced(r); // 返回 isBalanced(右指针)
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    Main s = new Main(); // 把 new Main(); 写入 Main s
    boolean ok = true; // 把 true; 写入 boolean ok
    if (s.sortedListToBST(null) != null) {
      ok = false;
      System.out.println("FAIL null case");
    }
    TreeNode109 r = s.sortedListToBST(buildList(new int[] {-10, -3, 0, 5, 9}));
    if (!check(r, new int[] {-10, -3, 0, 5, 9})) {
      ok = false;
      System.out.println("FAIL list case");
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
