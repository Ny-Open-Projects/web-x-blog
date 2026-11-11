#!/usr/bin/env python3
# gen_fix_lc104.py — 补齐 tree/lc_104 二叉树的最大深度 缺失的 8 个解法 × 7 语言
# 方案2-9 对应 TS 仓库同名文件（分治递归的不同 harness 风格 + 辅助函数变体）
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from langlib import emit, TREE_H, EXT

BLOG = "来源（blog）：https://blog.csdn.net/tyro_java/article/details/130815631"
REL = "tree/lc_104_二叉树的最大深度"

# 每个方案的用例 (层序数组, 期望深度)，None = null
S2_CASES = [([], 0), ([1, 2, 3, 4, 5], 3)]
S3_CASES = [([3, 9, 20, None, None, 15, 7], 3), ([1, 2, 3, 4, 5, None, None, None, 6], 4), ([], 0)]
S4_CASES = [([3, 9, 20, None, None, 15, 7], 3), ([1, 2, 3, 4, 5], 3)]
S6_CASES = [([], 0), ([3, 9, 20, None, None, 15, 7], 3), ([1, 2, 3, 4, 5], 3), ([1, None, 2, None, 3], 3)]
SOL_CASES = {2: S2_CASES, 3: S3_CASES, 4: S4_CASES, 5: S2_CASES, 6: S6_CASES, 7: S4_CASES, 8: S2_CASES, 9: S6_CASES}
SOL_DESC = {
    2: "方案2：分治递归 1+max(左深,右深) — python 风格自测",
    3: "方案3：分治递归（紧凑版，附层序/相同树/中序辅助函数）",
    4: "方案4：分治递归 + 树遍历辅助（中序/自底向上层序/根叶路径/层均值）",
    5: "方案5：分治递归 1+max(左深,右深) — python 风格自测",
    6: "方案6：分治递归（assertEq 风格自测）",
    7: "方案7：分治递归 + 树遍历辅助（中序/自底向上层序/根叶路径/层均值）",
    8: "方案8：分治递归 1+max(左深,右深) — python 风格自测",
    9: "方案9：分治递归（assertEq 风格自测）",
}
HAS_S3_HELP = {3}
HAS_S47_HELP = {4, 7}

def rs_v(vals):
    return "vec![]" if not vals else "vec![" + ", ".join("Some(%d)" % v if v is not None else "None" for v in vals) + "]"

def cpp_v(vals):
    if not vals:
        return "{}"
    return "{" + ", ".join(str(v) if v is not None else "std::nullopt" for v in vals) + "}"

def lua_v(vals):
    return "{" + ", ".join(str(v) if v is not None else '"null"' for v in vals) + "}"

def r_v(vals):
    if not vals:
        return "list()"
    return "list(" + ", ".join("%dL" % v if v is not None else "NA" for v in vals) + ")"

def dart_v(vals):
    return "<int?>[" + ", ".join(str(v) if v is not None else "null" for v in vals) + "]"

def zig_decl(name, vals):
    return "    const %s = [_]i32{%s};" % (name, ", ".join(str(v) if v is not None else "-1" for v in vals))

# ---------- Rust ----------
def gen_rust(sol):
    cases = ",\n        ".join("(%s, %d)" % (rs_v(v), w) for v, w in SOL_CASES[sol])
    helpers = ""
    if sol in HAS_S3_HELP:
        helpers = '''
// 辅助：层序遍历按层分组
fn level_list(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<Vec<i32>> {
    let mut res: Vec<Vec<i32>> = vec![];
    let mut level: Vec<Rc<RefCell<TreeNode>>> = root.into_iter().collect();
    while !level.is_empty() {
        let mut vals = vec![];
        let mut nxt = vec![];
        for node in &level {
            let b = node.borrow();
            vals.push(b.val);
            if let Some(l) = b.left.clone() { nxt.push(l); }
            if let Some(r) = b.right.clone() { nxt.push(r); }
        }
        res.push(vals);
        level = nxt;
    }
    res
}

// 辅助：判断两棵树是否相同
fn same_tree(a: Option<Rc<RefCell<TreeNode>>>, b: Option<Rc<RefCell<TreeNode>>>) -> bool {
    match (a, b) {
        (None, None) => true,
        (Some(x), Some(y)) => {
            let (xv, yv) = (x.borrow().val, y.borrow().val);
            if xv != yv { return false; }
            let (xl, xr) = (x.borrow().left.clone(), x.borrow().right.clone());
            let (yl, yr) = (y.borrow().left.clone(), y.borrow().right.clone());
            same_tree(xl, yl) && same_tree(xr, yr)
        }
        _ => false,
    }
}

// 辅助：中序遍历
fn inorder_t(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<i32> {
    fn go(n: Option<&Rc<RefCell<TreeNode>>>, out: &mut Vec<i32>) {
        if let Some(x) = n {
            let b = x.borrow();
            go(b.left.as_ref(), out);
            out.push(b.val);
            go(b.right.as_ref(), out);
        }
    }
    let mut out = vec![];
    go(root.as_ref(), &mut out);
    out
}
'''
    if sol in HAS_S47_HELP:
        helpers = '''
// 辅助：中序遍历
fn inorder(root: Option<Rc<RefCell<TreeNode>>>, out: &mut Vec<i32>) {
    if let Some(n) = root {
        let b = n.borrow();
        inorder(b.left.clone(), out);
        out.push(b.val);
        inorder(b.right.clone(), out);
    }
}

// 辅助：自底向上层序遍历
fn level_order_bottom(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<Vec<i32>> {
    let mut res: Vec<Vec<i32>> = vec![];
    let mut level: Vec<Rc<RefCell<TreeNode>>> = root.into_iter().collect();
    while !level.is_empty() {
        let mut vals = vec![];
        let mut nxt = vec![];
        for node in &level {
            let b = node.borrow();
            vals.push(b.val);
            if let Some(l) = b.left.clone() { nxt.push(l); }
            if let Some(r) = b.right.clone() { nxt.push(r); }
        }
        res.insert(0, vals);
        level = nxt;
    }
    res
}

// 辅助：所有根到叶路径
fn binary_tree_paths(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<String> {
    fn dfs(n: Option<&Rc<RefCell<TreeNode>>>, path: String, out: &mut Vec<String>) {
        if let Some(node) = n {
            let b = node.borrow();
            let mut path = path + &b.val.to_string();
            if b.left.is_none() && b.right.is_none() {
                out.push(path);
            } else {
                path += "->";
                dfs(b.left.as_ref(), path.clone(), out);
                dfs(b.right.as_ref(), path, out);
            }
        }
    }
    let mut out = vec![];
    dfs(root.as_ref(), String::new(), &mut out);
    out
}

// 辅助：每层节点均值
fn average_of_levels(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<f64> {
    let mut result = vec![];
    let mut level: Vec<Rc<RefCell<TreeNode>>> = root.into_iter().collect();
    while !level.is_empty() {
        let mut total = 0.0;
        let mut nxt = vec![];
        for node in &level {
            let b = node.borrow();
            total += b.val as f64;
            if let Some(l) = b.left.clone() { nxt.push(l); }
            if let Some(r) = b.right.clone() { nxt.push(r); }
        }
        result.push(total / level.len() as f64);
        level = nxt;
    }
    result
}
'''
    return '''// %s
// LeetCode 104. 二叉树的最大深度 — Rust 版（%s）
use std::rc::Rc;
use std::cell::RefCell;

#[derive(Debug)]
struct TreeNode {
    val: i32,
    left: Option<Rc<RefCell<TreeNode>>>,
    right: Option<Rc<RefCell<TreeNode>>>,
}

impl TreeNode {
    fn new(val: i32) -> Rc<RefCell<TreeNode>> {
        Rc::new(RefCell::new(TreeNode { val, left: None, right: None }))
    }
}

fn build_tree(vals: &[Option<i32>]) -> Option<Rc<RefCell<TreeNode>>> {
    if vals.is_empty() || vals[0].is_none() {
        return None;
    }
    let root = TreeNode::new(vals[0].unwrap());
    let mut queue: Vec<Rc<RefCell<TreeNode>>> = vec![root.clone()];
    let mut i = 1;
    while !queue.is_empty() && i < vals.len() {
        let node = queue.remove(0);
        if i < vals.len() {
            if let Some(v) = vals[i] {
                let child = TreeNode::new(v);
                node.borrow_mut().left = Some(child.clone());
                queue.push(child);
            }
            i += 1;
        }
        if i < vals.len() {
            if let Some(v) = vals[i] {
                let child = TreeNode::new(v);
                node.borrow_mut().right = Some(child.clone());
                queue.push(child);
            }
            i += 1;
        }
    }
    Some(root)
}
%s
// 主解法：分治递归，深度 = 1 + max(左子树深度, 右子树深度)
fn max_depth(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
    match root {
        None => 0,
        Some(node) => {
            let b = node.borrow();
            let l = max_depth(b.left.clone());
            let r = max_depth(b.right.clone());
            1 + if l > r { l } else { r }
        }
    }
}

fn main() {
    let tests: Vec<(Vec<Option<i32>>, i32)> = vec![
        %s,
    ];
    for (idx, (vals, want)) in tests.iter().enumerate() {
        let got = max_depth(build_tree(vals));
        assert_eq!(got, *want, "case {} failed", idx);
    }
    println!("PASS");
}
''' % (BLOG, SOL_DESC[sol], helpers, cases)

# ---------- Lua ----------
def gen_lua(sol):
    cases = ",\n    ".join("{%s, %d}" % (lua_v(v), w) for v, w in SOL_CASES[sol])
    helpers = ""
    if sol in HAS_S3_HELP:
        helpers = '''
-- 辅助：层序遍历按层分组
local function level_list(root)
    local res = {}
    local queue = {}
    if root then queue[1] = root end
    local head = 1
    while head <= #queue do
        local nxt = {}
        local vals = {}
        local tail = head
        for i = head, #queue do
            local node = queue[i]
            vals[#vals + 1] = node.val
            if node.left then nxt[#nxt + 1] = node.left end
            if node.right then nxt[#nxt + 1] = node.right end
        end
        res[#res + 1] = vals
        queue = nxt
        head = 1
    end
    return res
end

-- 辅助：判断两棵树是否相同
local function same_tree(a, b)
    if not a and not b then return true end
    if not a or not b then return false end
    return a.val == b.val and same_tree(a.left, b.left) and same_tree(a.right, b.right)
end

-- 辅助：中序遍历
local function inorder_t(root)
    if not root then return {} end
    local out = {}
    for _, v in ipairs(inorder_t(root.left)) do out[#out + 1] = v end
    out[#out + 1] = root.val
    for _, v in ipairs(inorder_t(root.right)) do out[#out + 1] = v end
    return out
end
'''
    if sol in HAS_S47_HELP:
        helpers = '''
-- 辅助：中序遍历
local function inorder(root, out)
    out = out or {}
    if not root then return out end
    inorder(root.left, out)
    out[#out + 1] = root.val
    inorder(root.right, out)
    return out
end

-- 辅助：自底向上层序遍历
local function level_order_bottom(root)
    local res = {}
    local queue = {}
    if root then queue[1] = root end
    while #queue > 0 do
        local vals = {}
        local nxt = {}
        for i = 1, #queue do
            local node = queue[i]
            vals[#vals + 1] = node.val
            if node.left then nxt[#nxt + 1] = node.left end
            if node.right then nxt[#nxt + 1] = node.right end
        end
        table.insert(res, 1, vals)
        queue = nxt
    end
    return res
end

-- 辅助：所有根到叶路径
local function binary_tree_paths(root)
    local out = {}
    local function dfs(n, path)
        if not n then return end
        path = path .. tostring(n.val)
        if not n.left and not n.right then
            out[#out + 1] = path
            return
        end
        path = path .. "->"
        dfs(n.left, path)
        dfs(n.right, path)
    end
    dfs(root, "")
    return out
end

-- 辅助：每层节点均值
local function average_of_levels(root)
    local result = {}
    local queue = {}
    if root then queue[1] = root end
    while #queue > 0 do
        local total = 0
        local nxt = {}
        for i = 1, #queue do
            local node = queue[i]
            total = total + node.val
            if node.left then nxt[#nxt + 1] = node.left end
            if node.right then nxt[#nxt + 1] = node.right end
        end
        result[#result + 1] = total / #queue
        queue = nxt
    end
    return result
end
'''
    return '''-- %s
-- LeetCode 104. 二叉树的最大深度 — Lua 版（%s）
%s

local TreeNode = {}
TreeNode.__index = TreeNode
function TreeNode.new(val)
    return setmetatable({val = val, left = nil, right = nil}, TreeNode)
end

local function build_tree(vals)
    if not vals or #vals == 0 or vals[1] == "null" then return nil end
    local root = TreeNode.new(vals[1])
    local queue = {root}
    local head = 1
    local i = 2
    while head <= #queue and i <= #vals do
        local node = queue[head]
        head = head + 1
        if i <= #vals then
            if vals[i] ~= "null" then
                node.left = TreeNode.new(vals[i])
                queue[#queue + 1] = node.left
            end
            i = i + 1
        end
        if i <= #vals then
            if vals[i] ~= "null" then
                node.right = TreeNode.new(vals[i])
                queue[#queue + 1] = node.right
            end
            i = i + 1
        end
    end
    return root
end
%s
-- 主解法：分治递归，深度 = 1 + max(左子树深度, 右子树深度)
local function max_depth(root)
    if not root then return 0 end
    local l = max_depth(root.left)
    local r = max_depth(root.right)
    if l > r then return 1 + l else return 1 + r end
end

-- 自测：与 blog 方案用例一致
local tests = {
    %s,
}
for idx, t in ipairs(tests) do
    local got = max_depth(build_tree(t[1]))
    local want = t[2]
    assert(got == want, string.format("case %%d failed: got %%d want %%d", idx, got, want))
end
print("PASS")
''' % (BLOG, SOL_DESC[sol], "-- harness：层序数组建树，\"null\" 表示空节点", helpers, cases)

# ---------- C ----------
def c_vals(vals):
    return ", ".join(str(v) if v is not None else "INT_MIN_SN" for v in vals)

def gen_c(sol):
    rows = []
    for v, w in SOL_CASES[sol]:
        if not v:
            rows.append("{{INT_MIN_SN}, 0, %d}" % w)
        else:
            rows.append("{%s, %d, %d}" % ("{" + c_vals(v) + "}", len(v), w))
    cases = ",\n        ".join(rows)
    maxn = max((len(v) for v, _ in SOL_CASES[sol]), default=1)
    helpers = ""
    if sol in HAS_S3_HELP:
        helpers = '''
// 辅助：判断两棵树是否相同
static int same_tree(TreeNode *a, TreeNode *b) {
    if (!a && !b) return 1;
    if (!a || !b) return 0;
    return a->val == b->val && same_tree(a->left, b->left) && same_tree(a->right, b->right);
}

// 辅助：中序遍历写入数组，返回长度
static int inorder_t(TreeNode *n, int *out) {
    static int k = 0; (void)out; (void)n; return k; /* 见下方非 static 版本 */
}
'''
        # 上面 inorder_t 占位避免递归 static 复杂化，改为简单实现
        helpers = '''
// 辅助：判断两棵树是否相同
static int same_tree(TreeNode *a, TreeNode *b) {
    if (!a && !b) return 1;
    if (!a || !b) return 0;
    return a->val == b->val && same_tree(a->left, b->left) && same_tree(a->right, b->right);
}

// 辅助：中序遍历打印
static void inorder_t(TreeNode *n) {
    if (!n) return;
    inorder_t(n->left);
    printf("%d ", n->val);
    inorder_t(n->right);
}
'''
    if sol in HAS_S47_HELP:
        helpers = '''
// 辅助：中序遍历打印
static void inorder(TreeNode *n) {
    if (!n) return;
    inorder(n->left);
    printf("%d ", n->val);
    inorder(n->right);
}

// 辅助：自底向上层序遍历打印（每层一行，最底层先输出）
static void level_order_bottom(TreeNode *root) {
    if (!root) return;
    TreeNode *level[64]; int ln = 0;
    level[ln++] = root;
    TreeNode *levels[16][64]; int lens[16]; int depth = 0;
    while (ln > 0) {
        lens[depth] = ln;
        for (int i = 0; i < ln; i++) levels[depth][i] = level[i];
        int nn = 0;
        for (int i = 0; i < ln; i++) {
            if (level[i]->left) level[nn++] = level[i]->left;
            if (level[i]->right) level[nn++] = level[i]->right;
        }
        ln = nn; depth++;
    }
    for (int d = depth - 1; d >= 0; d--) {
        for (int i = 0; i < lens[d]; i++) printf("%d ", levels[d][i]->val);
        printf("\\n");
    }
}

// 辅助：打印所有根到叶路径
static void binary_tree_paths(TreeNode *n, char *path) {
    if (!n) return;
    char buf[256];
    snprintf(buf, sizeof(buf), "%%s%%d", path, n->val);
    if (!n->left && !n->right) { printf("%%s\\n", buf); return; }
    char buf2[256];
    snprintf(buf2, sizeof(buf2), "%%s->", buf);
    binary_tree_paths(n->left, buf2);
    binary_tree_paths(n->right, buf2);
}

// 辅助：每层节点均值打印
static void average_of_levels(TreeNode *root) {
    if (!root) return;
    TreeNode *level[64]; int ln = 0;
    level[ln++] = root;
    while (ln > 0) {
        double total = 0;
        TreeNode *nxt[64]; int nn = 0;
        for (int i = 0; i < ln; i++) {
            total += level[i]->val;
            if (level[i]->left) nxt[nn++] = level[i]->left;
            if (level[i]->right) nxt[nn++] = level[i]->right;
        }
        printf("%%.1f ", total / ln);
        ln = nn;
        memcpy(level, nxt, sizeof(TreeNode *) * nn);
    }
    printf("\\n");
}
'''
    return '''// %s
// LeetCode 104. 二叉树的最大深度 — C 版（%s）
// 注：辅助函数在 C 版以打印形式呈现（返回结构见 Rust/C++/Dart/Lua/R 版）
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define INT_MIN_SN (-2147483647 - 1)
typedef struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
} TreeNode;
static TreeNode *build_tree(const int *vals, int n) {
    if (n == 0 || vals[0] == INT_MIN_SN) return NULL;
    TreeNode *root = malloc(sizeof(TreeNode));
    root->val = vals[0]; root->left = root->right = NULL;
    TreeNode **queue = malloc(sizeof(TreeNode *) * n);
    int head = 0, tail = 0, i = 1;
    queue[tail++] = root;
    while (head < tail && i < n) {
        TreeNode *node = queue[head++];
        if (i < n) {
            if (vals[i] != INT_MIN_SN) {
                node->left = malloc(sizeof(TreeNode));
                node->left->val = vals[i]; node->left->left = node->left->right = NULL;
                queue[tail++] = node->left;
            }
            i++;
        }
        if (i < n) {
            if (vals[i] != INT_MIN_SN) {
                node->right = malloc(sizeof(TreeNode));
                node->right->val = vals[i]; node->right->left = node->right->right = NULL;
                queue[tail++] = node->right;
            }
            i++;
        }
    }
    free(queue);
    return root;
}
static void free_tree(TreeNode *n) {
    if (!n) return;
    free_tree(n->left);
    free_tree(n->right);
    free(n);
}
%s
// 主解法：分治递归，深度 = 1 + max(左子树深度, 右子树深度)
int max_depth(TreeNode *root) {
    if (!root) return 0;
    int l = max_depth(root->left);
    int r = max_depth(root->right);
    return 1 + (l > r ? l : r);
}

int main(void) {
    struct { int vals[%d]; int n; int want; } tests[] = {
        %s,
    };
    for (int idx = 0; idx < %d; idx++) {
        TreeNode *t = build_tree(tests[idx].vals, tests[idx].n);
        int got = max_depth(t);
        if (got != tests[idx].want) {
            printf("case %%d failed: got %%d want %%d\\n", idx, got, tests[idx].want);
            return 1;
        }
        free_tree(t);
    }
    printf("PASS\\n");
    return 0;
}
''' % (BLOG, SOL_DESC[sol], helpers, max(maxn, 1), cases, len(SOL_CASES[sol]))

# ---------- C++ ----------
def gen_cpp(sol):
    cases = ",\n        ".join("{%s, %d}" % (cpp_v(v), w) for v, w in SOL_CASES[sol])
    helpers = ""
    if sol in HAS_S3_HELP:
        helpers = '''
// 辅助：层序遍历按层分组
static std::vector<std::vector<int>> level_list(TreeNode *root) {
    std::vector<std::vector<int>> res;
    std::vector<TreeNode *> level;
    if (root) level.push_back(root);
    while (!level.empty()) {
        std::vector<int> vals;
        std::vector<TreeNode *> nxt;
        for (auto *node : level) {
            vals.push_back(node->val);
            if (node->left) nxt.push_back(node->left);
            if (node->right) nxt.push_back(node->right);
        }
        res.push_back(vals);
        level = nxt;
    }
    return res;
}

// 辅助：判断两棵树是否相同
static bool same_tree(TreeNode *a, TreeNode *b) {
    if (!a && !b) return true;
    if (!a || !b) return false;
    return a->val == b->val && same_tree(a->left, b->left) && same_tree(a->right, b->right);
}

// 辅助：中序遍历
static void inorder_t(TreeNode *n, std::vector<int> &out) {
    if (!n) return;
    inorder_t(n->left, out);
    out.push_back(n->val);
    inorder_t(n->right, out);
}
'''
    if sol in HAS_S47_HELP:
        helpers = '''
// 辅助：中序遍历
static void inorder(TreeNode *n, std::vector<int> &out) {
    if (!n) return;
    inorder(n->left, out);
    out.push_back(n->val);
    inorder(n->right, out);
}

// 辅助：自底向上层序遍历
static std::vector<std::vector<int>> level_order_bottom(TreeNode *root) {
    std::vector<std::vector<int>> res;
    if (!root) return res;
    std::vector<TreeNode *> level{root};
    while (!level.empty()) {
        std::vector<int> vals;
        std::vector<TreeNode *> nxt;
        for (auto *node : level) {
            vals.push_back(node->val);
            if (node->left) nxt.push_back(node->left);
            if (node->right) nxt.push_back(node->right);
        }
        res.insert(res.begin(), vals);
        level = nxt;
    }
    return res;
}

// 辅助：所有根到叶路径
static void binary_tree_paths(TreeNode *n, std::string path, std::vector<std::string> &out) {
    if (!n) return;
    path += std::to_string(n->val);
    if (!n->left && !n->right) { out.push_back(path); return; }
    path += "->";
    binary_tree_paths(n->left, path, out);
    binary_tree_paths(n->right, path, out);
}

// 辅助：每层节点均值
static std::vector<double> average_of_levels(TreeNode *root) {
    std::vector<double> result;
    if (!root) return result;
    std::vector<TreeNode *> level{root};
    while (!level.empty()) {
        double total = 0;
        std::vector<TreeNode *> nxt;
        for (auto *node : level) {
            total += node->val;
            if (node->left) nxt.push_back(node->left);
            if (node->right) nxt.push_back(node->right);
        }
        result.push_back(total / level.size());
        level = nxt;
    }
    return result;
}
'''
    return '''// %s
// LeetCode 104. 二叉树的最大深度 — C++ 版（%s）
#include <cassert>
#include <cstdint>
#include <iostream>
#include <optional>
#include <queue>
#include <string>
#include <vector>
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    explicit TreeNode(int v) : val(v), left(nullptr), right(nullptr) {}
};
static TreeNode *build_tree(const std::vector<std::optional<int>> &vals) {
    if (vals.empty() || !vals[0].has_value()) return nullptr;
    auto *root = new TreeNode(*vals[0]);
    std::queue<TreeNode *> q;
    q.push(root);
    size_t i = 1;
    while (!q.empty() && i < vals.size()) {
        TreeNode *node = q.front();
        q.pop();
        if (i < vals.size()) {
            if (vals[i].has_value()) {
                node->left = new TreeNode(*vals[i]);
                q.push(node->left);
            }
            ++i;
        }
        if (i < vals.size()) {
            if (vals[i].has_value()) {
                node->right = new TreeNode(*vals[i]);
                q.push(node->right);
            }
            ++i;
        }
    }
    return root;
}
static void free_tree(TreeNode *n) {
    if (!n) return;
    free_tree(n->left);
    free_tree(n->right);
    delete n;
}
%s
// 主解法：分治递归，深度 = 1 + max(左子树深度, 右子树深度)
int max_depth(TreeNode *root) {
    if (!root) return 0;
    int l = max_depth(root->left);
    int r = max_depth(root->right);
    return 1 + (l > r ? l : r);
}

int main() {
    std::vector<std::pair<std::vector<std::optional<int>>, int>> tests = {
        %s,
    };
    for (size_t idx = 0; idx < tests.size(); ++idx) {
        TreeNode *t = build_tree(tests[idx].first);
        int got = max_depth(t);
        assert(got == tests[idx].second && "case failed");
        free_tree(t);
    }
    std::cout << "PASS" << std::endl;
    return 0;
}
''' % (BLOG, SOL_DESC[sol], helpers, cases)

# ---------- R ----------
def gen_r(sol):
    cases = ",\n  ".join("list(%s, %dL)" % (r_v(v), w) for v, w in SOL_CASES[sol])
    helpers = ""
    if sol in HAS_S3_HELP:
        helpers = '''
# 辅助：层序遍历按层分组
level_list <- function(root) {
  res <- list()
  queue <- if (is.null(root)) list() else list(root)
  while (length(queue) > 0) {
    vals <- c()
    nxt <- list()
    for (node in queue) {
      vals <- c(vals, node$val)
      if (!is.null(node$left)) nxt[[length(nxt) + 1L]] <- node$left
      if (!is.null(node$right)) nxt[[length(nxt) + 1L]] <- node$right
    }
    res[[length(res) + 1L]] <- vals
    queue <- nxt
  }
  res
}

# 辅助：判断两棵树是否相同
same_tree <- function(a, b) {
  if (is.null(a) && is.null(b)) return(TRUE)
  if (is.null(a) || is.null(b)) return(FALSE)
  a$val == b$val && same_tree(a$left, b$left) && same_tree(a$right, b$right)
}

# 辅助：中序遍历
inorder_t <- function(root) {
  if (is.null(root)) return(c())
  c(inorder_t(root$left), root$val, inorder_t(root$right))
}
'''
    if sol in HAS_S47_HELP:
        helpers = '''
# 辅助：中序遍历
inorder <- function(root, out = c()) {
  if (is.null(root)) return(out)
  out <- inorder(root$left, out)
  out <- c(out, root$val)
  inorder(root$right, out)
}

# 辅助：自底向上层序遍历
level_order_bottom <- function(root) {
  res <- list()
  queue <- if (is.null(root)) list() else list(root)
  while (length(queue) > 0) {
    vals <- c()
    nxt <- list()
    for (node in queue) {
      vals <- c(vals, node$val)
      if (!is.null(node$left)) nxt[[length(nxt) + 1L]] <- node$left
      if (!is.null(node$right)) nxt[[length(nxt) + 1L]] <- node$right
    }
    res <- c(list(vals), res)
    queue <- nxt
  }
  res
}

# 辅助：所有根到叶路径
binary_tree_paths <- function(root) {
  out <- character(0)
  dfs <- function(n, path) {
    if (is.null(n)) return(invisible(NULL))
    path <- paste0(path, as.character(n$val))
    if (is.null(n$left) && is.null(n$right)) {
      out <<- c(out, path)
      return(invisible(NULL))
    }
    path <- paste0(path, "->")
    dfs(n$left, path)
    dfs(n$right, path)
  }
  dfs(root, "")
  out
}

# 辅助：每层节点均值
average_of_levels <- function(root) {
  result <- c()
  queue <- if (is.null(root)) list() else list(root)
  while (length(queue) > 0) {
    total <- 0
    nxt <- list()
    for (node in queue) {
      total <- total + node$val
      if (!is.null(node$left)) nxt[[length(nxt) + 1L]] <- node$left
      if (!is.null(node$right)) nxt[[length(nxt) + 1L]] <- node$right
    }
    result <- c(result, total / length(queue))
    queue <- nxt
  }
  result
}
'''
    return '''# %s
# LeetCode 104. 二叉树的最大深度 — R 版（%s）
%s

TreeNode <- function(val, left = NULL, right = NULL) {
  e <- new.env(parent = emptyenv())
  e$val <- val; e$left <- left; e$right <- right
  class(e) <- "TreeNode"
  e
}
build_tree <- function(vals) {
  if (length(vals) == 0 || is.na(vals[[1]])) return(NULL)
  root <- TreeNode(vals[[1]])
  queue <- list(root)
  head <- 1L
  i <- 2L
  while (head <= length(queue) && i <= length(vals)) {
    node <- queue[[head]]
    head <- head + 1L
    if (i <= length(vals)) {
      if (!is.na(vals[[i]])) {
        node$left <- TreeNode(vals[[i]])
        queue[[length(queue) + 1L]] <- node$left
      }
      i <- i + 1L
    }
    if (i <= length(vals)) {
      if (!is.na(vals[[i]])) {
        node$right <- TreeNode(vals[[i]])
        queue[[length(queue) + 1L]] <- node$right
      }
      i <- i + 1L
    }
  }
  root
}
%s
# 主解法：分治递归，深度 = 1 + max(左子树深度, 右子树深度)
max_depth <- function(root) {
  if (is.null(root)) return(0L)
  l <- max_depth(root$left)
  r <- max_depth(root$right)
  1L + max(l, r)
}

# 自测：与 blog 方案用例一致
tests <- list(
  %s
)
for (idx in seq_along(tests)) {
  got <- max_depth(build_tree(tests[[idx]][[1]]))
  want <- tests[[idx]][[2]]
  stopifnot(got == want)
}
cat("PASS\\n")
''' % (BLOG, SOL_DESC[sol], "# harness：层序数组建树，NA 表示空节点；节点用 environment 引用语义", helpers, cases)

# ---------- Zig ----------
def gen_zig(sol):
    decls = []
    entries = []
    for i, (v, w) in enumerate(SOL_CASES[sol]):
        name = "t%d" % (i + 1)
        decls.append(zig_decl(name, v))
        entries.append(".{ .vals = &%s, .want = %d }" % (name, w))
    cases = ",\n        ".join(entries)
    helpers = ""
    if sol in HAS_S3_HELP:
        helpers = '''
// 辅助：判断两棵树是否相同
fn sameTree(a: ?*TreeNode, b: ?*TreeNode) bool {
    if (a == null and b == null) return true;
    if (a == null or b == null) return false;
    return a.?.val == b.?.val and sameTree(a.?.left, b.?.left) and sameTree(a.?.right, b.?.right);
}

// 辅助：中序遍历
fn inorderT(n: ?*TreeNode, out: *std.ArrayList(i32)) !void {
    const node = n orelse return;
    try inorderT(node.left, out);
    try out.append(node.val);
    try inorderT(node.right, out);
}
'''
    if sol in HAS_S47_HELP:
        helpers = '''
// 辅助：中序遍历
fn inorder(n: ?*TreeNode, out: *std.ArrayList(i32)) !void {
    const node = n orelse return;
    try inorder(node.left, out);
    try out.append(node.val);
    try inorder(node.right, out);
}
'''
    return '''// %s
// LeetCode 104. 二叉树的最大深度 — Zig 版（%s）
const std = @import("std");

const TreeNode = struct {
    val: i32,
    left: ?*TreeNode,
    right: ?*TreeNode,
};

fn buildTree(allocator: std.mem.Allocator, vals: []const i32) !?*TreeNode {
    if (vals.len == 0 or vals[0] == -1) return null;
    const root = try allocator.create(TreeNode);
    root.* = .{ .val = vals[0], .left = null, .right = null };
    var queue = std.ArrayList(*TreeNode).init(allocator);
    defer queue.deinit();
    try queue.append(root);
    var head: usize = 0;
    var i: usize = 1;
    while (head < queue.items.len and i < vals.len) {
        const node = queue.items[head];
        head += 1;
        if (i < vals.len) {
            if (vals[i] != -1) {
                const child = try allocator.create(TreeNode);
                child.* = .{ .val = vals[i], .left = null, .right = null };
                node.left = child;
                try queue.append(child);
            }
            i += 1;
        }
        if (i < vals.len) {
            if (vals[i] != -1) {
                const child = try allocator.create(TreeNode);
                child.* = .{ .val = vals[i], .left = null, .right = null };
                node.right = child;
                try queue.append(child);
            }
            i += 1;
        }
    }
    return root;
}
%s
// 主解法：分治递归，深度 = 1 + max(左子树深度, 右子树深度)
fn maxDepth(root: ?*TreeNode) i32 {
    if (root == null) return 0;
    const l = maxDepth(root.?.left);
    const r = maxDepth(root.?.right);
    return 1 + @max(l, r);
}

pub fn main() !void {
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();
    const allocator = arena.allocator();

%s

    const Case = struct { vals: []const i32, want: i32 };
    const cases = [_]Case{
        %s,
    };
    for (cases, 0..) |c, idx| {
        const got = maxDepth(try buildTree(allocator, c.vals));
        if (got != c.want) {
            std.debug.print("case {d} failed: got {d} want {d}\\n", .{ idx, got, c.want });
            return error.TestFailed;
        }
    }
    std.debug.print("PASS\\n", .{});
}
''' % (BLOG, SOL_DESC[sol], helpers, "\n".join(decls), cases)

# ---------- Dart ----------
def gen_dart(sol):
    cases = ",\n    ".join("%s: %d" % (dart_v(v), w) for v, w in SOL_CASES[sol])
    helpers = ""
    if sol in HAS_S3_HELP:
        helpers = '''
// 辅助：层序遍历按层分组
List<List<int>> levelList(TreeNode? root) {
  final res = <List<int>>[];
  var level = <TreeNode?>[root];
  while (level.isNotEmpty) {
    final vals = <int>[];
    final nxt = <TreeNode?>[];
    for (final n in level) {
      if (n == null) continue;
      vals.add(n.val);
      nxt.add(n.left);
      nxt.add(n.right);
    }
    res.add(vals);
    level = nxt;
  }
  return res;
}

// 辅助：判断两棵树是否相同
bool sameTree(TreeNode? a, TreeNode? b) {
  if (a == null && b == null) return true;
  if (a == null || b == null) return false;
  return a.val == b.val && sameTree(a.left, b.left) && sameTree(a.right, b.right);
}

// 辅助：中序遍历
List<int> inorderT(TreeNode? n) {
  if (n == null) return [];
  return [...inorderT(n.left), n.val, ...inorderT(n.right)];
}
'''
    if sol in HAS_S47_HELP:
        helpers = '''
// 辅助：中序遍历
List<int> inorder(TreeNode? n, [List<int>? out]) {
  out ??= <int>[];
  if (n == null) return out;
  inorder(n.left, out);
  out.add(n.val);
  inorder(n.right, out);
  return out;
}

// 辅助：自底向上层序遍历
List<List<int>> levelOrderBottom(TreeNode? root) {
  final res = <List<int>>[];
  var level = <TreeNode?>[root];
  while (level.isNotEmpty) {
    final vals = <int>[];
    final nxt = <TreeNode?>[];
    for (final n in level) {
      if (n == null) continue;
      vals.add(n.val);
      nxt.add(n.left);
      nxt.add(n.right);
    }
    res.insert(0, vals);
    level = nxt;
  }
  return res;
}

// 辅助：所有根到叶路径
List<String> binaryTreePaths(TreeNode? root) {
  final out = <String>[];
  void dfs(TreeNode? n, String path) {
    if (n == null) return;
    path += n.val.toString();
    if (n.left == null && n.right == null) {
      out.add(path);
      return;
    }
    path += '->';
    dfs(n.left, path);
    dfs(n.right, path);
  }
  dfs(root, '');
  return out;
}

// 辅助：每层节点均值
List<double> averageOfLevels(TreeNode? root) {
  final result = <double>[];
  var level = <TreeNode?>[root];
  while (level.isNotEmpty) {
    var total = 0.0;
    final nxt = <TreeNode?>[];
    for (final n in level) {
      if (n == null) continue;
      total += n.val;
      nxt.add(n.left);
      nxt.add(n.right);
    }
    result.add(total / level.length);
    level = nxt;
  }
  return result;
}
'''
    return '''// %s
// LeetCode 104. 二叉树的最大深度 — Dart 版（%s）
%s

class TreeNode {
  int val;
  TreeNode? left;
  TreeNode? right;
  TreeNode(this.val);
}

TreeNode? buildTree(List<int?> vals) {
  if (vals.isEmpty || vals[0] == null) return null;
  final root = TreeNode(vals[0]!);
  final queue = <TreeNode>[root];
  var head = 0;
  var i = 1;
  while (head < queue.length && i < vals.length) {
    final node = queue[head++];
    if (i < vals.length) {
      if (vals[i] != null) {
        node.left = TreeNode(vals[i]!);
        queue.add(node.left!);
      }
      i++;
    }
    if (i < vals.length) {
      if (vals[i] != null) {
        node.right = TreeNode(vals[i]!);
        queue.add(node.right!);
      }
      i++;
    }
  }
  return root;
}
%s
// 主解法：分治递归，深度 = 1 + max(左子树深度, 右子树深度)
int maxDepth(TreeNode? root) {
  if (root == null) return 0;
  final l = maxDepth(root.left);
  final r = maxDepth(root.right);
  return 1 + (l > r ? l : r);
}

void main() {
  final tests = <List<int?>, int>{
    %s,
  };
  var idx = 0;
  for (final entry in tests.entries) {
    final got = maxDepth(buildTree(entry.key));
    if (got != entry.value) {
      throw StateError('case $idx failed: got $got want ${entry.value}');
    }
    idx++;
  }
  print('PASS');
}
''' % (BLOG, SOL_DESC[sol], "// harness：层序数组建树，null 表示空节点", helpers, cases)

GENS = {"rust": gen_rust, "lua": gen_lua, "c": gen_c, "cpp": gen_cpp, "r": gen_r, "zig": gen_zig, "dart": gen_dart}

def main():
    for lang, fn in GENS.items():
        ext = EXT[lang]
        for sol in range(2, 10):
            name = "solution_%d___%d.%s" % (sol, sol, ext)
            emit(lang, REL + "/" + name, fn(sol))
        print("%s: 8 files emitted" % lang)

if __name__ == "__main__":
    main()
