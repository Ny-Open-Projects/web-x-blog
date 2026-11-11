import os

base107 = "/Users/Wang/Code/github/web-x-blog/work/target/21.dsa/java/tree/lc_107_二叉树的层序遍历_ii"
base35 = "/Users/Wang/Code/github/web-x-blog/work/target/21.dsa/java/binary_search/lc_35_搜索插入位置"

java107 = '''package com.webfault.dsa;

import java.util.*;

class TreeNode107 {
    int val;
    TreeNode107 left, right;
    TreeNode107(int v) { val = v; }
    TreeNode107(int v, TreeNode107 l, TreeNode107 r) { val = v; left = l; right = r; }
}

class L107 {
    List<List<Integer>> levelOrderBottom(TreeNode107 root) {
        List<List<Integer>> res = new ArrayList<>();
        if (root == null) return res;
        Deque<TreeNode107> q = new ArrayDeque<>();
        q.add(root);
        while (!q.isEmpty()) {
            int sz = q.size();
            List<Integer> level = new ArrayList<>();
            for (int i = 0; i < sz; i++) {
                TreeNode107 node = q.poll();
                level.add(node.val);
                if (node.left != null) q.add(node.left);
                if (node.right != null) q.add(node.right);
            }
            res.add(0, level);
        }
        return res;
    }
    public static void main(String[] args) {
        L107 s = new L107();
        boolean ok = true;
        if (!s.levelOrderBottom(null).isEmpty()) { ok = false; System.out.println("FAIL null"); }
        TreeNode107 root = new TreeNode107(3,
            new TreeNode107(9),
            new TreeNode107(20, new TreeNode107(15), new TreeNode107(7)));
        List<List<Integer>> got = s.levelOrderBottom(root);
        List<List<Integer>> want = new ArrayList<>();
        want.add(Arrays.asList(15, 7));
        want.add(Arrays.asList(9, 20));
        want.add(Arrays.asList(3));
        if (!got.equals(want)) { ok = false; System.out.println("FAIL demo got=" + got); }
        if (!ok) throw new RuntimeException("FAILED");
        System.out.println("PASS");
    }
}
'''

java35 = '''package com.webfault.dsa;

class L35 {
    int searchInsert(int[] nums, int target) {
        int left = 0, right = nums.length;
        while (left < right) {
            int mid = (left + right) / 2;
            if (nums[mid] < target) left = mid + 1;
            else right = mid;
        }
        return left;
    }
    public static void main(String[] args) {
        L35 s = new L35();
        boolean ok = true;
        if (s.searchInsert(new int[]{1, 3, 5, 6}, 5) != 2) { ok = false; System.out.println("FAIL 5"); }
        if (s.searchInsert(new int[]{1, 3, 5, 6}, 2) != 1) { ok = false; System.out.println("FAIL 2"); }
        if (s.searchInsert(new int[]{1, 3, 5, 6}, 7) != 4) { ok = false; System.out.println("FAIL 7"); }
        if (s.searchInsert(new int[]{1, 3, 5, 6}, 0) != 0) { ok = false; System.out.println("FAIL 0"); }
        if (s.searchInsert(new int[]{}, 5) != 0) { ok = false; System.out.println("FAIL empty"); }
        if (!ok) throw new RuntimeException("FAILED");
        System.out.println("PASS");
    }
}
'''

with open(os.path.join(base107, "solution_1_1_____1________.java"), "w") as f:
    f.write(java107)
with open(os.path.join(base35, "solution_1_1_____1_____.java"), "w") as f:
    f.write(java35)
print("wrote 2 java files")
