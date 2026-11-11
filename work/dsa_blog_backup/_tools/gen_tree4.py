#!/usr/bin/env python3
# gen_tree4.py — tree 第四批（遍历家族）：lc_94/lc_144/lc_145/lc_257/lc_230 × 7语言
import sys, os; sys.path.insert(0, "/Users/Wang/Code/webfault-ai/dsa/_tools")
from langlib import emit, TREE_H, head_comment, EXT

B = {"94": "134915904", "144": "135122295", "145": "135185066", "257": "135666411", "230": "136684493"}
LANGNAME = {"rust": "Rust", "lua": "Lua", "c": "C", "cpp": "C++", "r": "R", "zig": "Zig", "dart": "Dart"}

# 遍历器骨架：order = 0 中序 / 1 前序 / 2 后序（同一 DFS，push 时机不同）
A94 = {
"rust": '''{H}
fn inorder_traversal(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<i32> {{
    let mut res = Vec::new();
    fn dfs(n: Option<&Rc<RefCell<TreeNode>>>, res: &mut Vec<i32>) {{
        let node = match n {{ Some(x) => x, None => return }};
        let nb = node.borrow();
        dfs(nb.left.as_ref(), res);
        res.push(nb.val);
        dfs(nb.right.as_ref(), res);
    }}
    dfs(root.as_ref(), &mut res);
    res
}}
fn main() {{
    assert_eq!(inorder_traversal(None), Vec::<i32>::new());
    assert_eq!(inorder_traversal(build_tree(&[Some(1), None, Some(2), None, Some(3)])), vec![1, 2, 3]);
    assert_eq!(inorder_traversal(build_tree(&[Some(1), Some(2), Some(3)])), vec![2, 1, 3]);
    println!("PASS");
}}
''',
"lua": '''{H}
local function inorder_traversal(root)
    local res = {{}}
    local function dfs(n)
        if not n then return end
        dfs(n.left)
        res[#res + 1] = n.val
        dfs(n.right)
    end
    dfs(root)
    return res
end
local function eq(a, b)
    if #a ~= #b then return false end
    for i = 1, #a do if a[i] ~= b[i] then return false end end
    return true
end
assert(eq(inorder_traversal(nil), {{}}))
assert(eq(inorder_traversal(build_tree({{1, "null", 2, "null", 3}})), {{1, 2, 3}}))
assert(eq(inorder_traversal(build_tree({{1, 2, 3}})), {{2, 1, 3}}))
print("PASS")
''',
"c": '''{H}
static void dfs_in(TreeNode *n, int *out, int *cnt) {{
    if (!n) return;
    dfs_in(n->left, out, cnt);
    out[(*cnt)++] = n->val;
    dfs_in(n->right, out, cnt);
}}
static int inorder_traversal(TreeNode *root, int out[]) {{
    int cnt = 0;
    dfs_in(root, out, &cnt);
    return cnt;
}}
static int eqarr(const int *a, int n, const int *b, int m) {{
    if (n != m) return 0;
    for (int i = 0; i < n; i++) if (a[i] != b[i]) return 0;
    return 1;
}}
int main(void) {{
    int out[64], n;
    int w2[] = {{1,2,3}}, w3[] = {{2,1,3}};
    int v2[] = {{1,INT_MIN_SN,2,INT_MIN_SN,3}};
    int v3[] = {{1,2,3}};
    if (inorder_traversal(NULL, out) != 0) {{ printf("FAIL 0\\n"); return 1; }}
    n = inorder_traversal(build_tree(v2, 5), out);
    if (!eqarr(out, n, w2, 3)) {{ printf("FAIL 1\\n"); return 1; }}
    n = inorder_traversal(build_tree(v3, 3), out);
    if (!eqarr(out, n, w3, 3)) {{ printf("FAIL 2\\n"); return 1; }}
    printf("PASS\\n");
    return 0;
}}
''',
"cpp": '''{H}
static std::vector<int> inorderTraversal(TreeNode *root) {{
    std::vector<int> res;
    std::function<void(TreeNode *)> dfs = [&](TreeNode *n) {{
        if (!n) return;
        dfs(n->left);
        res.push_back(n->val);
        dfs(n->right);
    }};
    dfs(root);
    return res;
}}
int main() {{
    assert(inorderTraversal(nullptr).empty());
    assert((inorderTraversal(build_tree({{1, std::nullopt, 2, std::nullopt, 3}})) == std::vector<int>{{1, 2, 3}}));
    assert((inorderTraversal(build_tree({{1, 2, 3}})) == std::vector<int>{{2, 1, 3}}));
    std::cout << "PASS" << std::endl;
    return 0;
}}
''',
"r": '''{H}
inorder_traversal <- function(root) {{
  res <- integer(0)
  dfs <- function(n) {{
    if (is.null(n)) return(invisible(NULL))
    dfs(n$left)
    res[[length(res) + 1L]] <<- n$val
    dfs(n$right)
  }}
  dfs(root)
  res
}}
stopifnot(identical(inorder_traversal(NULL), integer(0)))
stopifnot(identical(inorder_traversal(build_tree(list(1L, NA, 2L, NA, 3L))), c(1L, 2L, 3L)))
stopifnot(identical(inorder_traversal(build_tree(list(1L, 2L, 3L))), c(2L, 1L, 3L)))
cat("PASS\\n")
''',
"zig": '''{H}
fn inorderTraversal(root: ?*TreeNode, alloc: std.mem.Allocator) std.ArrayList(i32) {{
    var res = std.ArrayList(i32).init(alloc);
    const D = struct {{
        fn dfs(n: ?*TreeNode, out: *std.ArrayList(i32)) void {{
            const node = n orelse return;
            dfs(node.left, out);
            out.append(node.val) catch unreachable;
            dfs(node.right, out);
        }}
    }};
    D.dfs(root, &res);
    return res;
}}
pub fn main() !void {{
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();
    const alloc = arena.allocator();
    const eq = struct {{
        fn check(a: std.ArrayList(i32), b: []const i32) bool {{
            if (a.items.len != b.len) return false;
            for (b, 0..) |v, i| if (a.items[i] != v) return false;
            return true;
        }}
    }}.check;
    if (inorderTraversal(null, alloc).items.len != 0) return error.TestFailed;
    if (!eq(inorderTraversal(try buildTree(alloc, &[_]i32{{ 1, -1, 2, -1, 3 }}), alloc), &[_]i32{{ 1, 2, 3 }})) return error.TestFailed;
    if (!eq(inorderTraversal(try buildTree(alloc, &[_]i32{{ 1, 2, 3 }}), alloc), &[_]i32{{ 2, 1, 3 }})) return error.TestFailed;
    std.debug.print("PASS\\n", .{{}});
}}
''',
"dart": '''{H}
List<int> inorderTraversal(TreeNode? root) {{
  final res = <int>[];
  void dfs(TreeNode? n) {{
    if (n == null) return;
    dfs(n.left);
    res.add(n.val);
    dfs(n.right);
  }}
  dfs(root);
  return res;
}}
void main() {{
  if (inorderTraversal(null).isNotEmpty) throw StateError('c0');
  if (inorderTraversal(buildTree([1, null, 2, null, 3])).toString() != '[1, 2, 3]') throw StateError('c1');
  if (inorderTraversal(buildTree([1, 2, 3])).toString() != '[2, 1, 3]') throw StateError('c2');
  print('PASS');
}}
''',
}

A144 = {
"rust": '''{H}
fn preorder_traversal(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<i32> {{
    let root = match root {{ Some(x) => x, None => return vec![] }};
    let mut res = vec![root.borrow().val];
    res.extend(preorder_traversal(root.borrow().left.clone()));
    res.extend(preorder_traversal(root.borrow().right.clone()));
    res
}}
fn main() {{
    assert_eq!(preorder_traversal(build_tree(&[Some(1), Some(2), Some(3), None, Some(4), Some(5)])), vec![1, 2, 4, 3, 5]);
    assert!(preorder_traversal(None).is_empty());
    println!("PASS");
}}
''',
"lua": '''{H}
local function preorder_traversal(root)
    if not root then return {{}} end
    local res = {{root.val}}
    local l = preorder_traversal(root.left)
    local r = preorder_traversal(root.right)
    for _, v in ipairs(l) do res[#res + 1] = v end
    for _, v in ipairs(r) do res[#res + 1] = v end
    return res
end
local a = preorder_traversal(build_tree({{1, 2, 3, "null", 4, 5}}))
assert(#a == 5 and a[1] == 1 and a[2] == 2 and a[3] == 4 and a[4] == 3 and a[5] == 5)
assert(#preorder_traversal(nil) == 0)
print("PASS")
''',
"c": '''{H}
static void dfs_pre(TreeNode *n, int *out, int *cnt) {{
    if (!n) return;
    out[(*cnt)++] = n->val;
    dfs_pre(n->left, out, cnt);
    dfs_pre(n->right, out, cnt);
}}
static int preorder_traversal(TreeNode *root, int out[]) {{
    int cnt = 0;
    dfs_pre(root, out, &cnt);
    return cnt;
}}
int main(void) {{
    int out[64], n;
    int v[] = {{1,2,3,INT_MIN_SN,4,5}};
    int w[] = {{1,2,4,3,5}};
    n = preorder_traversal(build_tree(v, 6), out);
    if (n != 5) {{ printf("FAIL len\\n"); return 1; }}
    for (int i = 0; i < 5; i++) if (out[i] != w[i]) {{ printf("FAIL %d\\n", i); return 1; }}
    if (preorder_traversal(NULL, out) != 0) {{ printf("FAIL nil\\n"); return 1; }}
    printf("PASS\\n");
    return 0;
}}
''',
"cpp": '''{H}
static std::vector<int> preorderTraversal(TreeNode *root) {{
    if (!root) return {{}};
    std::vector<int> res{{root->val}};
    auto l = preorderTraversal(root->left);
    auto r = preorderTraversal(root->right);
    res.insert(res.end(), l.begin(), l.end());
    res.insert(res.end(), r.begin(), r.end());
    return res;
}}
int main() {{
    assert((preorderTraversal(build_tree({{1, 2, 3, std::nullopt, 4, 5}})) == std::vector<int>{{1, 2, 4, 3, 5}}));
    assert(preorderTraversal(nullptr).empty());
    std::cout << "PASS" << std::endl;
    return 0;
}}
''',
"r": '''{H}
preorder_traversal <- function(root) {{
  if (is.null(root)) return(integer(0))
  c(root$val, preorder_traversal(root$left), preorder_traversal(root$right))
}}
a <- preorder_traversal(build_tree(list(1L, 2L, 3L, NA, 4L, 5L)))
stopifnot(identical(a, c(1L, 2L, 4L, 3L, 5L)))
stopifnot(length(preorder_traversal(NULL)) == 0L)
cat("PASS\\n")
''',
"zig": '''{H}
fn preorderTraversal(root: ?*TreeNode, alloc: std.mem.Allocator) std.ArrayList(i32) {{
    var res = std.ArrayList(i32).init(alloc);
    const D = struct {{
        fn dfs(n: ?*TreeNode, out: *std.ArrayList(i32)) void {{
            const node = n orelse return;
            out.append(node.val) catch unreachable;
            dfs(node.left, out);
            dfs(node.right, out);
        }}
    }};
    D.dfs(root, &res);
    return res;
}}
pub fn main() !void {{
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();
    const alloc = arena.allocator();
    const res = preorderTraversal(try buildTree(alloc, &[_]i32{{ 1, 2, 3, -1, 4, 5 }}), alloc);
    const want = [_]i32{{ 1, 2, 4, 3, 5 }};
    if (res.items.len != want.len) return error.TestFailed;
    for (want, 0..) |w, i| if (res.items[i] != w) return error.TestFailed;
    if (preorderTraversal(null, alloc).items.len != 0) return error.TestFailed;
    std.debug.print("PASS\\n", .{{}});
}}
''',
"dart": '''{H}
List<int> preorderTraversal(TreeNode? root) {{
  if (root == null) return [];
  return [root.val, ...preorderTraversal(root.left), ...preorderTraversal(root.right)];
}}
void main() {{
  if (preorderTraversal(buildTree([1, 2, 3, null, 4, 5])).toString() != '[1, 2, 4, 3, 5]') throw StateError('c1');
  if (preorderTraversal(null).isNotEmpty) throw StateError('c2');
  print('PASS');
}}
''',
}

A145 = {
"rust": '''{H}
fn postorder_traversal(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<i32> {{
    let mut res = Vec::new();
    fn dfs(n: Option<&Rc<RefCell<TreeNode>>>, res: &mut Vec<i32>) {{
        let node = match n {{ Some(x) => x, None => return }};
        let nb = node.borrow();
        dfs(nb.left.as_ref(), res);
        dfs(nb.right.as_ref(), res);
        res.push(nb.val);
    }}
    dfs(root.as_ref(), &mut res);
    res
}}
fn main() {{
    assert_eq!(postorder_traversal(None), Vec::<i32>::new());
    assert_eq!(postorder_traversal(build_tree(&[Some(1), None, Some(2), None, Some(3)])), vec![3, 2, 1]);
    assert_eq!(postorder_traversal(build_tree(&[Some(1), Some(2), Some(3)])), vec![2, 3, 1]);
    println!("PASS");
}}
''',
"lua": '''{H}
local function postorder_traversal(root)
    local res = {{}}
    local function dfs(n)
        if not n then return end
        dfs(n.left)
        dfs(n.right)
        res[#res + 1] = n.val
    end
    dfs(root)
    return res
end
local function eq(a, b)
    if #a ~= #b then return false end
    for i = 1, #a do if a[i] ~= b[i] then return false end end
    return true
end
assert(eq(postorder_traversal(nil), {{}}))
assert(eq(postorder_traversal(build_tree({{1, "null", 2, "null", 3}})), {{3, 2, 1}}))
assert(eq(postorder_traversal(build_tree({{1, 2, 3}})), {{2, 3, 1}}))
print("PASS")
''',
"c": '''{H}
static void dfs_post(TreeNode *n, int *out, int *cnt) {{
    if (!n) return;
    dfs_post(n->left, out, cnt);
    dfs_post(n->right, out, cnt);
    out[(*cnt)++] = n->val;
}}
static int postorder_traversal(TreeNode *root, int out[]) {{
    int cnt = 0;
    dfs_post(root, out, &cnt);
    return cnt;
}}
static int eqarr(const int *a, int n, const int *b, int m) {{
    if (n != m) return 0;
    for (int i = 0; i < n; i++) if (a[i] != b[i]) return 0;
    return 1;
}}
int main(void) {{
    int out[64], n;
    int v2[] = {{1,INT_MIN_SN,2,INT_MIN_SN,3}};
    int v3[] = {{1,2,3}};
    int w2[] = {{3,2,1}}, w3[] = {{2,3,1}};
    if (postorder_traversal(NULL, out) != 0) {{ printf("FAIL 0\\n"); return 1; }}
    n = postorder_traversal(build_tree(v2, 5), out);
    if (!eqarr(out, n, w2, 3)) {{ printf("FAIL 1\\n"); return 1; }}
    n = postorder_traversal(build_tree(v3, 3), out);
    if (!eqarr(out, n, w3, 3)) {{ printf("FAIL 2\\n"); return 1; }}
    printf("PASS\\n");
    return 0;
}}
''',
"cpp": '''{H}
static std::vector<int> postorderTraversal(TreeNode *root) {{
    std::vector<int> res;
    std::function<void(TreeNode *)> dfs = [&](TreeNode *n) {{
        if (!n) return;
        dfs(n->left);
        dfs(n->right);
        res.push_back(n->val);
    }};
    dfs(root);
    return res;
}}
int main() {{
    assert(postorderTraversal(nullptr).empty());
    assert((postorderTraversal(build_tree({{1, std::nullopt, 2, std::nullopt, 3}})) == std::vector<int>{{3, 2, 1}}));
    assert((postorderTraversal(build_tree({{1, 2, 3}})) == std::vector<int>{{2, 3, 1}}));
    std::cout << "PASS" << std::endl;
    return 0;
}}
''',
"r": '''{H}
postorder_traversal <- function(root) {{
  res <- integer(0)
  dfs <- function(n) {{
    if (is.null(n)) return(invisible(NULL))
    dfs(n$left)
    dfs(n$right)
    res[[length(res) + 1L]] <<- n$val
  }}
  dfs(root)
  res
}}
stopifnot(identical(postorder_traversal(NULL), integer(0)))
stopifnot(identical(postorder_traversal(build_tree(list(1L, NA, 2L, NA, 3L))), c(3L, 2L, 1L)))
stopifnot(identical(postorder_traversal(build_tree(list(1L, 2L, 3L))), c(2L, 3L, 1L)))
cat("PASS\\n")
''',
"zig": '''{H}
fn postorderTraversal(root: ?*TreeNode, alloc: std.mem.Allocator) std.ArrayList(i32) {{
    var res = std.ArrayList(i32).init(alloc);
    const D = struct {{
        fn dfs(n: ?*TreeNode, out: *std.ArrayList(i32)) void {{
            const node = n orelse return;
            dfs(node.left, out);
            dfs(node.right, out);
            out.append(node.val) catch unreachable;
        }}
    }};
    D.dfs(root, &res);
    return res;
}}
pub fn main() !void {{
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();
    const alloc = arena.allocator();
    const eq = struct {{
        fn check(a: std.ArrayList(i32), b: []const i32) bool {{
            if (a.items.len != b.len) return false;
            for (b, 0..) |v, i| if (a.items[i] != v) return false;
            return true;
        }}
    }}.check;
    if (postorderTraversal(null, alloc).items.len != 0) return error.TestFailed;
    if (!eq(postorderTraversal(try buildTree(alloc, &[_]i32{{ 1, -1, 2, -1, 3 }}), alloc), &[_]i32{{ 3, 2, 1 }})) return error.TestFailed;
    if (!eq(postorderTraversal(try buildTree(alloc, &[_]i32{{ 1, 2, 3 }}), alloc), &[_]i32{{ 2, 3, 1 }})) return error.TestFailed;
    std.debug.print("PASS\\n", .{{}});
}}
''',
"dart": '''{H}
List<int> postorderTraversal(TreeNode? root) {{
  final res = <int>[];
  void dfs(TreeNode? n) {{
    if (n == null) return;
    dfs(n.left);
    dfs(n.right);
    res.add(n.val);
  }}
  dfs(root);
  return res;
}}
void main() {{
  if (postorderTraversal(null).isNotEmpty) throw StateError('c0');
  if (postorderTraversal(buildTree([1, null, 2, null, 3])).toString() != '[3, 2, 1]') throw StateError('c1');
  if (postorderTraversal(buildTree([1, 2, 3])).toString() != '[2, 3, 1]') throw StateError('c2');
  print('PASS');
}}
''',
}

A257 = {
"rust": '''{H}
fn binary_tree_paths(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<String> {{
    let mut paths = Vec::new();
    fn dfs(n: Option<&Rc<RefCell<TreeNode>>>, path: String, paths: &mut Vec<String>) {{
        let node = match n {{ Some(x) => x, None => return }};
        let nb = node.borrow();
        let path = format!("{{}}{{}}", path, nb.val);
        if nb.left.is_none() && nb.right.is_none() {{
            paths.push(path);
        }} else {{
            let p2 = format!("{{}}->", path);
            dfs(nb.left.as_ref(), p2.clone(), paths);
            dfs(nb.right.as_ref(), p2, paths);
        }}
    }}
    dfs(root.as_ref(), String::new(), &mut paths);
    paths
}}
fn main() {{
    assert_eq!(binary_tree_paths(build_tree(&[Some(1), Some(2), Some(3)])), vec!["1->2", "1->3"]);
    assert_eq!(binary_tree_paths(build_tree(&[Some(1)])), vec!["1"]);
    assert!(binary_tree_paths(None).is_empty());
    println!("PASS");
}}
''',
"lua": '''{H}
local function binary_tree_paths(root)
    local paths = {{}}
    local function dfs(n, path)
        if not n then return end
        path = path .. n.val
        if not n.left and not n.right then
            paths[#paths + 1] = path
        else
            path = path .. "->"
            dfs(n.left, path)
            dfs(n.right, path)
        end
    end
    dfs(root, "")
    return paths
end
local a = binary_tree_paths(build_tree({{1, 2, 3}}))
assert(#a == 2 and a[1] == "1->2" and a[2] == "1->3")
local b = binary_tree_paths(build_tree({{1}}))
assert(#b == 1 and b[1] == "1")
assert(#binary_tree_paths(nil) == 0)
print("PASS")
''',
"c": '''{H}
#include <string.h>
static void dfs_paths(TreeNode *n, char *path, char (*paths)[64], int *cnt) {{
    if (!n) return;
    char buf[64];
    snprintf(buf, sizeof(buf), "%s%d", path, n->val);
    if (!n->left && !n->right) {{
        snprintf(paths[(*cnt)++], 64, "%s", buf);
        return;
    }}
    strcat(buf, "->");
    dfs_paths(n->left, buf, paths, cnt);
    dfs_paths(n->right, buf, paths, cnt);
}}
static int binary_tree_paths(TreeNode *root, char (*paths)[64]) {{
    int cnt = 0;
    dfs_paths(root, "", paths, &cnt);
    return cnt;
}}
int main(void) {{
    char paths[64][64];
    int n = binary_tree_paths(build_tree((int[]){{1,2,3}}, 3), paths);
    if (n != 2 || strcmp(paths[0], "1->2") != 0 || strcmp(paths[1], "1->3") != 0) {{ printf("FAIL 1\\n"); return 1; }}
    n = binary_tree_paths(build_tree((int[]){{1}}, 1), paths);
    if (n != 1 || strcmp(paths[0], "1") != 0) {{ printf("FAIL 2\\n"); return 1; }}
    if (binary_tree_paths(NULL, paths) != 0) {{ printf("FAIL 3\\n"); return 1; }}
    printf("PASS\\n");
    return 0;
}}
''',
"cpp": '''{H}
static std::vector<std::string> binaryTreePaths(TreeNode *root) {{
    std::vector<std::string> paths;
    std::function<void(TreeNode *, std::string)> dfs = [&](TreeNode *n, std::string path) {{
        if (!n) return;
        path += std::to_string(n->val);
        if (!n->left && !n->right) {{
            paths.push_back(path);
            return;
        }}
        path += "->";
        dfs(n->left, path);
        dfs(n->right, path);
    }};
    dfs(root, "");
    return paths;
}}
int main() {{
    assert((binaryTreePaths(build_tree({{1, 2, 3}})) == std::vector<std::string>{{"1->2", "1->3"}}));
    assert((binaryTreePaths(build_tree({{1}})) == std::vector<std::string>{{"1"}}));
    assert(binaryTreePaths(nullptr).empty());
    std::cout << "PASS" << std::endl;
    return 0;
}}
''',
"r": '''{H}
binary_tree_paths <- function(root) {{
  paths <- character(0)
  dfs <- function(n, path) {{
    if (is.null(n)) return(invisible(NULL))
    path <- paste0(path, n$val)
    if (is.null(n$left) && is.null(n$right)) {{
      paths[[length(paths) + 1L]] <<- path
      return(invisible(NULL))
    }}
    path <- paste0(path, "->")
    dfs(n$left, path)
    dfs(n$right, path)
  }}
  dfs(root, "")
  paths
}}
stopifnot(identical(binary_tree_paths(build_tree(list(1L, 2L, 3L))), c("1->2", "1->3")))
stopifnot(identical(binary_tree_paths(build_tree(list(1L))), "1"))
stopifnot(length(binary_tree_paths(NULL)) == 0L)
cat("PASS\\n")
''',
"zig": '''{H}
fn binaryTreePaths(root: ?*TreeNode, alloc: std.mem.Allocator) std.ArrayList([]const u8) {{
    var paths = std.ArrayList([]const u8).init(alloc);
    const D = struct {{
        fn dfs(n: ?*TreeNode, path: []const u8, out: *std.ArrayList([]const u8), a: std.mem.Allocator) void {{
            const node = n orelse return;
            var buf = std.ArrayList(u8).init(a);
            buf.appendSlice(path) catch unreachable;
            buf.writer().print("{{d}}", .{{node.val}}) catch unreachable;
            if (node.left == null and node.right == null) {{
                out.append(buf.toOwnedSlice() catch unreachable) catch unreachable;
                return;
            }}
            buf.appendSlice("->") catch unreachable;
            const p2 = a.dupe(u8, buf.items) catch unreachable;
            dfs(node.left, p2, out, a);
            dfs(node.right, buf.toOwnedSlice() catch unreachable, out, a);
        }}
    }};
    D.dfs(root, "", &paths, alloc);
    return paths;
}}
pub fn main() !void {{
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();
    const alloc = arena.allocator();
    var paths = binaryTreePaths(try buildTree(alloc, &[_]i32{{ 1, 2, 3 }}), alloc);
    if (paths.items.len != 2) return error.TestFailed;
    if (!std.mem.eql(u8, paths.items[0], "1->2") or !std.mem.eql(u8, paths.items[1], "1->3")) return error.TestFailed;
    paths = binaryTreePaths(try buildTree(alloc, &[_]i32{{1}}), alloc);
    if (paths.items.len != 1 or !std.mem.eql(u8, paths.items[0], "1")) return error.TestFailed;
    if (binaryTreePaths(null, alloc).items.len != 0) return error.TestFailed;
    std.debug.print("PASS\\n", .{{}});
}}
''',
"dart": '''{H}
List<String> binaryTreePaths(TreeNode? root) {{
  final paths = <String>[];
  void dfs(TreeNode? n, String path) {{
    if (n == null) return;
    path += n.val.toString();
    if (n.left == null && n.right == null) {{
      paths.add(path);
      return;
    }}
    path += '->';
    dfs(n.left, path);
    dfs(n.right, path);
  }}
  dfs(root, '');
  return paths;
}}
void main() {{
  if (binaryTreePaths(buildTree([1, 2, 3])).toString() != '[1->2, 1->3]') throw StateError('c1');
  if (binaryTreePaths(buildTree([1])).toString() != '[1]') throw StateError('c2');
  if (binaryTreePaths(null).isNotEmpty) throw StateError('c3');
  print('PASS');
}}
''',
}

A230 = {
"rust": '''{H}
fn kth_smallest(root: Option<Rc<RefCell<TreeNode>>>, k: i32) -> i32 {{
    let mut k = k;
    let mut stack: Vec<Rc<RefCell<TreeNode>>> = Vec::new();
    let mut cur = root;
    while cur.is_some() || !stack.is_empty() {{
        while let Some(c) = cur {{
            stack.push(c.clone());
            cur = c.borrow().left.clone();
        }}
        let node = stack.pop().unwrap();
        k -= 1;
        if k == 0 {{ return node.borrow().val; }}
        cur = node.borrow().right.clone();
    }}
    -1
}}
fn main() {{
    let t = build_tree(&[Some(3), Some(1), Some(4), None, Some(2)]);
    assert_eq!(kth_smallest(t.clone(), 1), 1);
    assert_eq!(kth_smallest(t, 2), 2);
    let t2 = build_tree(&[Some(5), Some(3), Some(6), Some(2), Some(4), None, None, Some(1)]);
    assert_eq!(kth_smallest(t2, 3), 3);
    println!("PASS");
}}
''',
"lua": '''{H}
local function kth_smallest(root, k)
    local stack = {{}}
    local cur = root
    while cur or #stack > 0 do
        while cur do
            stack[#stack + 1] = cur
            cur = cur.left
        end
        cur = table.remove(stack)
        k = k - 1
        if k == 0 then return cur.val end
        cur = cur.right
    end
    return -1
end
local t = build_tree({{3, 1, 4, "null", 2}})
assert(kth_smallest(t, 1) == 1)
assert(kth_smallest(t, 2) == 2)
local t2 = build_tree({{5, 3, 6, 2, 4, "null", "null", 1}})
assert(kth_smallest(t2, 3) == 3)
print("PASS")
''',
"c": '''{H}
static int kth_smallest(TreeNode *root, int k) {{
    TreeNode *stack[256];
    int top = 0;
    TreeNode *cur = root;
    while (cur || top > 0) {{
        while (cur) {{ stack[top++] = cur; cur = cur->left; }}
        cur = stack[--top];
        k--;
        if (k == 0) return cur->val;
        cur = cur->right;
    }}
    return -1;
}}
int main(void) {{
    int v1[] = {{3,1,4,INT_MIN_SN,2}};
    int v2[] = {{5,3,6,2,4,INT_MIN_SN,INT_MIN_SN,1}};
    TreeNode *t = build_tree(v1, 5);
    if (kth_smallest(t, 1) != 1) {{ printf("FAIL 1\\n"); return 1; }}
    if (kth_smallest(t, 2) != 2) {{ printf("FAIL 2\\n"); return 1; }}
    TreeNode *t2 = build_tree(v2, 8);
    if (kth_smallest(t2, 3) != 3) {{ printf("FAIL 3\\n"); return 1; }}
    printf("PASS\\n");
    return 0;
}}
''',
"cpp": '''{H}
static int kthSmallest(TreeNode *root, int k) {{
    std::vector<TreeNode *> stack;
    TreeNode *cur = root;
    while (cur || !stack.empty()) {{
        while (cur) {{ stack.push_back(cur); cur = cur->left; }}
        cur = stack.back();
        stack.pop_back();
        --k;
        if (k == 0) return cur->val;
        cur = cur->right;
    }}
    return -1;
}}
int main() {{
    auto *t = build_tree({{3, 1, 4, std::nullopt, 2}});
    assert(kthSmallest(t, 1) == 1);
    assert(kthSmallest(t, 2) == 2);
    auto *t2 = build_tree({{5, 3, 6, 2, 4, std::nullopt, std::nullopt, 1}});
    assert(kthSmallest(t2, 3) == 3);
    std::cout << "PASS" << std::endl;
    return 0;
}}
''',
"r": '''{H}
kth_smallest <- function(root, k) {{
  stack <- list(); cur <- root
  while (!is.null(cur) || length(stack) > 0) {{
    while (!is.null(cur)) {{
      stack[[length(stack) + 1L]] <- cur
      cur <- cur$left
    }}
    cur <- stack[[length(stack)]]
    stack[[length(stack)]] <- NULL
    k <- k - 1L
    if (k == 0L) return(cur$val)
    cur <- cur$right
  }}
  -1L
}}
t <- build_tree(list(3L, 1L, 4L, NA, 2L))
stopifnot(kth_smallest(t, 1L) == 1L)
stopifnot(kth_smallest(t, 2L) == 2L)
t2 <- build_tree(list(5L, 3L, 6L, 2L, 4L, NA, NA, 1L))
stopifnot(kth_smallest(t2, 3L) == 3L)
cat("PASS\\n")
''',
"zig": '''{H}
fn kthSmallest(root: ?*TreeNode, k_in: i32) i32 {{
    var k = k_in;
    var stack = std.ArrayList(*TreeNode).init(std.heap.page_allocator);
    defer stack.deinit();
    var cur: ?*TreeNode = root;
    while (cur != null or stack.items.len > 0) {{
        while (cur) |c| {{
            stack.append(c) catch unreachable;
            cur = c.left;
        }}
        const node = stack.pop().?;
        k -= 1;
        if (k == 0) return node.val;
        cur = node.right;
    }}
    return -1;
}}
pub fn main() !void {{
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();
    const alloc = arena.allocator();
    const t = try buildTree(alloc, &[_]i32{{ 3, 1, 4, -1, 2 }});
    if (kthSmallest(t, 1) != 1) return error.TestFailed;
    if (kthSmallest(t, 2) != 2) return error.TestFailed;
    const t2 = try buildTree(alloc, &[_]i32{{ 5, 3, 6, 2, 4, -1, -1, 1 }});
    if (kthSmallest(t2, 3) != 3) return error.TestFailed;
    std.debug.print("PASS\\n", .{{}});
}}
''',
"dart": '''{H}
int kthSmallest(TreeNode? root, int k) {{
  final stack = <TreeNode>[];
  var cur = root;
  while (cur != null || stack.isNotEmpty) {{
    while (cur != null) {{
      stack.add(cur);
      cur = cur.left;
    }}
    cur = stack.removeLast();
    k--;
    if (k == 0) return cur.val;
    cur = cur.right;
  }}
  return -1;
}}
void main() {{
  final t = buildTree([3, 1, 4, null, 2]);
  if (kthSmallest(t, 1) != 1) throw StateError('c1');
  if (kthSmallest(t, 2) != 2) throw StateError('c2');
  final t2 = buildTree([5, 3, 6, 2, 4, null, null, 1]);
  if (kthSmallest(t2, 3) != 3) throw StateError('c3');
  print('PASS');
}}
''',
}

PROBS = [
    ("lc_94_二叉树的中序遍历", A94, "LeetCode 94. 二叉树的中序遍历"),
    ("lc_144_二叉树的前序遍历", A144, "LeetCode 144. 二叉树的前序遍历"),
    ("lc_145_二叉树的后序遍历", A145, "LeetCode 145. 二叉树的后序遍历"),
    ("lc_257_二叉树的所有路径", A257, "LeetCode 257. 二叉树的所有路径"),
    ("lc_230_二叉搜索树中第_k_小的元素", A230, "LeetCode 230. 二叉搜索树中第K小的元素"),
]
count = 0
for prob, algo, title in PROBS:
    bid = B[prob.split("_")[1]]
    ts_dir = f"/Users/Wang/Code/webfault-ai/dsa/ts/tree/{prob}"
    sols = sorted(f[:-3] for f in os.listdir(ts_dir) if f.startswith("solution_") and f.endswith(".ts"))
    for lang, tmpl in algo.items():
        ext = EXT[lang]
        for sol in sols:
            n = sol.replace("solution_", "").split("_")[0]
            head = head_comment(lang, bid, f"{title} — {LANGNAME[lang]} 版（方案{n}）")
            body = tmpl.replace("{H}", TREE_H[lang]).replace("{{", "{").replace("}}", "}")
            emit(lang, f"tree/{prob}/{sol}.{ext}", head + "\n" + body)
            count += 1
print(f"emitted {count} files")
