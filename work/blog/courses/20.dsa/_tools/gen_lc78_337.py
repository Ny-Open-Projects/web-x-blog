import os

base78 = "/Users/Wang/Code/github/web-x-blog/work/blog/courses/20.dsa/java/backtrack/lc_78_子集"
base337 = "/Users/Wang/Code/github/web-x-blog/work/blog/courses/20.dsa/java/dp/lc_337_打家劫舍_iii"

# ---- lc_78 subsets ----
expected_subsets = '''        List<List<Integer>> want = new ArrayList<>();
        want.add(new ArrayList<>());
        want.add(Arrays.asList(1));
        want.add(Arrays.asList(2));
        want.add(Arrays.asList(3));
        want.add(Arrays.asList(1,2));
        want.add(Arrays.asList(1,3));
        want.add(Arrays.asList(2,3));
        want.add(Arrays.asList(1,2,3));'''

sethelper = '''    static String key(List<Integer> x) { int[] t = new int[x.size()]; for (int i = 0; i < x.size(); i++) t[i] = x.get(i); java.util.Arrays.sort(t); return java.util.Arrays.toString(t); }
    static boolean sameSet(List<List<Integer>> a, List<List<Integer>> b) {
        if (a.size() != b.size()) return false;
        Set<String> sa = new HashSet<>(), sb = new HashSet<>();
        for (List<Integer> x : a) sa.add(key(x));
        for (List<Integer> x : b) sb.add(key(x));
        return sa.equals(sb);
    }'''

backtrack_body = '''    List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        List<Integer> path = new ArrayList<>();
        backtrack(0, path, nums, result);
        return result;
    }
    void backtrack(int start, List<Integer> path, int[] nums, List<List<Integer>> result) {
        result.add(new ArrayList<>(path));
        for (int i = start; i < nums.length; i++) {
            path.add(nums[i]);
            backtrack(i + 1, path, nums, result);
            path.remove(path.size() - 1);
        }
    }'''

iter_body = '''    List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        res.add(new ArrayList<>());
        for (int num : nums) {
            int sz = res.size();
            for (int i = 0; i < sz; i++) {
                List<Integer> cur = new ArrayList<>(res.get(i));
                cur.add(num);
                res.add(cur);
            }
        }
        return res;
    }'''

def lc78_class(cls, body):
    return '''package com.webfault.dsa;

import java.util.*;
class %s {
%s
%s
    public static void main(String[] args) {
        %s s = new %s();
        List<List<Integer>> got = s.subsets(new int[]{1, 2, 3});
        boolean ok = true;
        if (!sameSet(got, want)) { ok = false; System.out.println("FAIL got=" + got); }
        if (!ok) throw new RuntimeException("FAILED");
        System.out.println("PASS");
    }
}
''' % (cls, body, sethelper, cls, cls)

# Note: 'want' must be defined; we prepend it inside main via expected_subsets text.
# Rebuild with want declaration injected.
def lc78_class2(cls, body):
    return '''package com.webfault.dsa;

import java.util.*;
class %s {
%s
%s
    public static void main(String[] args) {
        %s s = new %s();
%s
        List<List<Integer>> got = s.subsets(new int[]{1, 2, 3});
        boolean ok = true;
        if (!sameSet(got, want)) { ok = false; System.out.println("FAIL got=" + got); }
        if (!ok) throw new RuntimeException("FAILED");
        System.out.println("PASS");
    }
}
''' % (cls, body, sethelper, cls, cls, expected_subsets)

mapping78 = {
    "solution_1___1.java": lc78_class2("Sub1", backtrack_body),
    "solution_2___2.java": lc78_class2("Sub2", backtrack_body),
    "solution_3___3.java": lc78_class2("Sub3", iter_body),
}

# ---- lc_337 house robber III ----
tree = '''class TreeNode337 { int val; TreeNode337 left, right; TreeNode337(int v){val=v;} TreeNode337(int v, TreeNode337 l, TreeNode337 r){val=v; left=l; right=r;} }'''

def lc337_class(cls, body):
    return '''package com.webfault.dsa;

import java.util.*;
%s
class %s {
%s
    public static void main(String[] args) {
        %s s = new %s();
        boolean ok = true;
        if (s.rob(null) != 0) { ok = false; System.out.println("FAIL null"); }
        TreeNode337 single = new TreeNode337(5);
        if (s.rob(single) != 5) { ok = false; System.out.println("FAIL single"); }
        TreeNode337 root = new TreeNode337(3,
            new TreeNode337(2, null, new TreeNode337(3)),
            new TreeNode337(3, null, new TreeNode337(1)));
        if (s.rob(root) != 7) { ok = false; System.out.println("FAIL demo got=" + s.rob(root)); }
        if (!ok) throw new RuntimeException("FAILED");
        System.out.println("PASS");
    }
}
''' % (tree, cls, body, cls, cls)

rob_body = '''    int rob(TreeNode337 root) {
        int[] st = dfs(root);
        return Math.max(st[0], st[1]);
    }
    int[] dfs(TreeNode337 node) {
        if (node == null) return new int[]{0, 0};
        int[] l = dfs(node.left);
        int[] r = dfs(node.right);
        int selected = node.val + l[1] + r[1];
        int notSelected = Math.max(l[0], l[1]) + Math.max(r[0], r[1]);
        return new int[]{selected, notSelected};
    }'''

mapping337 = {
    "solution_1_1_____1___________.java": lc337_class("Hr1", rob_body),
    "solution_2_2_____2______________.java": lc337_class("Hr2", rob_body),
}

for fn, content in mapping78.items():
    with open(os.path.join(base78, fn), "w") as f:
        f.write(content)
for fn, content in mapping337.items():
    with open(os.path.join(base337, fn), "w") as f:
        f.write(content)
print("wrote", len(mapping78) + len(mapping337))
