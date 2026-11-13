import os

base = "/Users/Wang/Code/github/web-x-blog/work/blog/courses/20.dsa/java/tree/lc_109_有序链表转换二叉搜索树"

common = '''
class ListNode {
    int val;
    ListNode next;
    ListNode(int v) { val = v; }
}
class TreeNode109 {
    int val;
    TreeNode109 left;
    TreeNode109 right;
    TreeNode109(int v) { val = v; }
}
'''

helpers = '''
    static ListNode buildList(int[] vals) {
        ListNode head = null, cur = null;
        for (int v : vals) {
            ListNode n = new ListNode(v);
            if (head == null) head = n; else cur.next = n;
            cur = n;
        }
        return head;
    }
    static void inorder(TreeNode109 r, java.util.List<Integer> out) {
        if (r == null) return;
        inorder(r.left, out);
        out.add(r.val);
        inorder(r.right, out);
    }
    static int height(TreeNode109 r) {
        if (r == null) return 0;
        return 1 + Math.max(height(r.left), height(r.right));
    }
    static boolean isBalanced(TreeNode109 r) {
        if (r == null) return true;
        if (Math.abs(height(r.left) - height(r.right)) > 1) return false;
        return isBalanced(r.left) && isBalanced(r.right);
    }
    static boolean check(TreeNode109 r, int[] expected) {
        java.util.List<Integer> io = new java.util.ArrayList<>();
        inorder(r, io);
        if (io.size() != expected.length) return false;
        for (int i = 0; i < expected.length; i++) if (io.get(i) != expected[i]) return false;
        return isBalanced(r);
    }
'''

variant1 = '''
class L109a {
    java.util.List<ListNode> nodeList;
    TreeNode109 build(int left, int right) {
        if (left > right) return null;
        int mid = (left + right) / 2;
        TreeNode109 root = new TreeNode109(nodeList.get(mid).val);
        root.left = build(left, mid - 1);
        root.right = build(mid + 1, right);
        return root;
    }
    TreeNode109 sortedListToBST(ListNode head) {
        nodeList = new java.util.ArrayList<>();
        ListNode p = head;
        while (p != null) { nodeList.add(p); p = p.next; }
        return build(0, nodeList.size() - 1);
    }
%s
    public static void main(String[] args) {
        L109a s = new L109a();
        boolean ok = true;
        if (s.sortedListToBST(null) != null) { ok = false; System.out.println("FAIL null case"); }
        TreeNode109 r = s.sortedListToBST(buildList(new int[]{-10, -3, 0, 5, 9}));
        if (!check(r, new int[]{-10, -3, 0, 5, 9})) { ok = false; System.out.println("FAIL list case"); }
        if (!ok) throw new RuntimeException("FAILED");
        System.out.println("PASS");
    }
}
'''

variant2 = '''
class L109b {
    ListNode getMedian(ListNode left, ListNode right) {
        ListNode fast = left, slow = left;
        while (fast != right && fast.next != right) { fast = fast.next.next; slow = slow.next; }
        return slow;
    }
    TreeNode109 buildTree(ListNode left, ListNode right) {
        if (left == right) return null;
        ListNode mid = getMedian(left, right);
        TreeNode109 root = new TreeNode109(mid.val);
        root.left = buildTree(left, mid);
        root.right = buildTree(mid.next, right);
        return root;
    }
    TreeNode109 sortedListToBST(ListNode head) { return buildTree(head, null); }
%s
    public static void main(String[] args) {
        L109b s = new L109b();
        boolean ok = true;
        if (s.sortedListToBST(null) != null) { ok = false; System.out.println("FAIL null case"); }
        TreeNode109 r = s.sortedListToBST(buildList(new int[]{-10, -3, 0, 5, 9}));
        if (!check(r, new int[]{-10, -3, 0, 5, 9})) { ok = false; System.out.println("FAIL list case"); }
        if (!ok) throw new RuntimeException("FAILED");
        System.out.println("PASS");
    }
}
'''

variant3 = '''
class L109c {
    ListNode cur;
    int getLength(ListNode head) { int l = 0; while (head != null) { l++; head = head.next; } return l; }
    TreeNode109 buildTree(int left, int right) {
        if (left > right) return null;
        int mid = (left + right + 1) / 2;
        TreeNode109 root = new TreeNode109(0);
        root.left = buildTree(left, mid - 1);
        if (cur != null) { root.val = cur.val; cur = cur.next; }
        root.right = buildTree(mid + 1, right);
        return root;
    }
    TreeNode109 sortedListToBST(ListNode head) { cur = head; int len = getLength(head); return buildTree(0, len - 1); }
%s
    public static void main(String[] args) {
        L109c s = new L109c();
        boolean ok = true;
        if (s.sortedListToBST(null) != null) { ok = false; System.out.println("FAIL null case"); }
        TreeNode109 r = s.sortedListToBST(buildList(new int[]{-10, -3, 0, 5, 9}));
        if (!check(r, new int[]{-10, -3, 0, 5, 9})) { ok = false; System.out.println("FAIL list case"); }
        if (!ok) throw new RuntimeException("FAILED");
        System.out.println("PASS");
    }
}
'''

variant4 = '''
class L109d {
    TreeNode109 travese(ListNode head, ListNode tail) {
        if (head == tail) return null;
        ListNode fast = head, slow = head;
        while (fast != tail && fast.next != tail) { slow = slow.next; fast = fast.next.next; }
        TreeNode109 root = new TreeNode109(slow.val);
        root.left = travese(head, slow);
        root.right = travese(slow.next, tail);
        return root;
    }
    TreeNode109 sortedListToBST(ListNode head) { return travese(head, null); }
%s
    public static void main(String[] args) {
        L109d s = new L109d();
        boolean ok = true;
        if (s.sortedListToBST(null) != null) { ok = false; System.out.println("FAIL null case"); }
        TreeNode109 r = s.sortedListToBST(buildList(new int[]{-10, -3, 0, 5, 9}));
        if (!check(r, new int[]{-10, -3, 0, 5, 9})) { ok = false; System.out.println("FAIL list case"); }
        if (!ok) throw new RuntimeException("FAILED");
        System.out.println("PASS");
    }
}
'''

mapping = {
    "solution_1___1.java": variant1,
    "solution_2_1____1___.java": variant2,
    "solution_3_2____2____________.java": variant3,
    "solution_4_3_____3_____.java": variant4,
}

for fn, v in mapping.items():
    content = "package com.webfault.dsa;\n" + common + v % helpers
    with open(os.path.join(base, fn), "w") as f:
        f.write(content)
print("wrote", len(mapping))
