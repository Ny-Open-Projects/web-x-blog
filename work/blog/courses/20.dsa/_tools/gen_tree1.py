#!/usr/bin/env python3
# gen_tree1.py — tree 第一批：lc_100/lc_226/lc_700/lc_543/lc_110 × 7语言
import sys; sys.path.insert(0, "/Users/Wang/Code/github/web-x-blog/work/blog/courses/20.dsa/_tools")
from langlib import emit, TREE_H, head_comment, EXT

LANGNAME = {"rust": "Rust", "lua": "Lua", "c": "C", "cpp": "C++", "r": "R", "zig": "Zig", "dart": "Dart"}

B = {"100": "134622591", "226": "134541657", "700": "135005838", "543": "135572347", "110": "135170465"}
T = "/Users/Wang/Code/github/web-x-blog/work/blog/courses/20.dsa/ts/tree"

# ---------- lc_100 相同的树 ----------
A100 = {
"rust": '''{H}
fn is_same_tree(p: Option<&Rc<RefCell<TreeNode>>>, q: Option<&Rc<RefCell<TreeNode>>>) -> bool {
    match (p, q) {
        (None, None) => true,
        (Some(a), Some(b)) => {
            let (a, b) = (a.borrow(), b.borrow());
            a.val == b.val && is_same_tree(a.left.as_ref(), b.left.as_ref()) && is_same_tree(a.right.as_ref(), b.right.as_ref())
        }
        _ => false,
    }
}
fn main() {{
    let t = |v: &[Option<i32>]| build_tree(v);
    assert!(is_same_tree(None, None));
    assert!(is_same_tree(t(&[Some(1), Some(2), Some(3)]).as_ref(), t(&[Some(1), Some(2), Some(3)]).as_ref()));
    assert!(!is_same_tree(t(&[Some(1), Some(2), Some(3)]).as_ref(), t(&[Some(1), Some(2), Some(1)]).as_ref()));
    println!("PASS");
}}
''',
"lua": '''{H}
local function is_same_tree(p, q)
    if not p and not q then return true end
    if not p or not q or p.val ~= q.val then return false end
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)
end
assert(is_same_tree(nil, nil) == true)
assert(is_same_tree(build_tree({{1,2,3}}), build_tree({{1,2,3}})) == true)
assert(is_same_tree(build_tree({{1,2,3}}), build_tree({{1,2,1}})) == false)
print("PASS")
''',
"c": '''{H}
static int is_same_tree(const TreeNode *p, const TreeNode *q) {{
    if (!p && !q) return 1;
    if (!p || !q || p->val != q->val) return 0;
    return is_same_tree(p->left, q->left) && is_same_tree(p->right, q->right);
}}
int main(void) {{
    int s1[] = {{1,2,3}}, s2[] = {{1,2,1}};
    if (!is_same_tree(NULL, NULL)) {{ printf("FAIL 0\\n"); return 1; }}
    if (!is_same_tree(build_tree(s1, 3), build_tree(s1, 3))) {{ printf("FAIL 1\\n"); return 1; }}
    if (is_same_tree(build_tree(s1, 3), build_tree(s2, 3))) {{ printf("FAIL 2\\n"); return 1; }}
    printf("PASS\\n");
    return 0;
}}
''',
"cpp": '''{H}
static bool isSameTree(const TreeNode *p, const TreeNode *q) {{
    if (!p && !q) return true;
    if (!p || !q || p->val != q->val) return false;
    return isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
}}
int main() {{
    assert(isSameTree(nullptr, nullptr));
    assert(isSameTree(build_tree({{1, 2, 3}}), build_tree({{1, 2, 3}})));
    assert(!isSameTree(build_tree({{1, 2, 3}}), build_tree({{1, 2, 1}})));
    std::cout << "PASS" << std::endl;
    return 0;
}}
''',
"r": '''{H}
is_same_tree <- function(p, q) {{
  if (is.null(p) && is.null(q)) return(TRUE)
  if (is.null(p) || is.null(q) || p$val != q$val) return(FALSE)
  is_same_tree(p$left, q$left) && is_same_tree(p$right, q$right)
}}
stopifnot(is_same_tree(NULL, NULL))
stopifnot(is_same_tree(build_tree(list(1L, 2L, 3L)), build_tree(list(1L, 2L, 3L))))
stopifnot(!is_same_tree(build_tree(list(1L, 2L, 3L)), build_tree(list(1L, 2L, 1L))))
cat("PASS\\n")
''',
"zig": '''{H}
fn isSameTree(p: ?*const TreeNode, q: ?*const TreeNode) bool {{
    if (p == null and q == null) return true;
    if (p == null or q == null) return false;
    const a = p.?;
    const b = q.?;
    return a.val == b.val and isSameTree(a.left, b.left) and isSameTree(a.right, b.right);
}}
pub fn main() !void {{
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();
    const alloc = arena.allocator();
    const t1 = try buildTree(alloc, &[_]i32{{ 1, 2, 3 }});
    const t2 = try buildTree(alloc, &[_]i32{{ 1, 2, 3 }});
    const t3 = try buildTree(alloc, &[_]i32{{ 1, 2, 1 }});
    if (!isSameTree(null, null)) return error.TestFailed;
    if (!isSameTree(t1, t2)) return error.TestFailed;
    if (isSameTree(t1, t3)) return error.TestFailed;
    std.debug.print("PASS\\n", .{{}});
}}
''',
"dart": '''{H}
bool isSameTree(TreeNode? p, TreeNode? q) {{
  if (p == null && q == null) return true;
  if (p == null || q == null || p.val != q.val) return false;
  return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
}}
void main() {{
  final t1 = buildTree([1, 2, 3]);
  final t2 = buildTree([1, 2, 3]);
  final t3 = buildTree([1, 2, 1]);
  if (!isSameTree(null, null)) throw StateError('c0');
  if (!isSameTree(t1, t2)) throw StateError('c1');
  if (isSameTree(t1, t3)) throw StateError('c2');
  print('PASS');
}}
''',
}

# ---------- lc_226 翻转二叉树 ----------
A226 = {
"rust": '''{H}
fn invert_tree(root: Option<Rc<RefCell<TreeNode>>>) -> Option<Rc<RefCell<TreeNode>>> {{
    let root = root?;
    let mut stack = vec![root.clone()];
    while let Some(node) = stack.pop() {{
        let mut n = node.borrow_mut();
        let tmp = n.left.take();
        n.left = n.right.take();
        n.right = tmp;
        let (l, r) = (n.left.clone(), n.right.clone());
        drop(n);
        if let Some(c) = l {{ stack.push(c); }}
        if let Some(c) = r {{ stack.push(c); }}
    }}
    Some(root)
}}
fn levels(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<Vec<i32>> {{
    let mut res = Vec::new();
    let mut q: Vec<Rc<RefCell<TreeNode>>> = root.into_iter().collect();
    while !q.is_empty() {{
        let mut cur = Vec::new();
        let mut nxt = Vec::new();
        for n in q {{
            let nb = n.borrow();
            cur.push(nb.val);
            if let Some(c) = nb.left.clone() {{ nxt.push(c); }}
            if let Some(c) = nb.right.clone() {{ nxt.push(c); }}
        }}
        res.push(cur);
        q = nxt;
    }}
    res
}}
fn main() {{
    let t = build_tree(&[Some(4), Some(2), Some(7), Some(1), Some(3), Some(6), Some(9)]);
    let got = levels(invert_tree(t));
    assert_eq!(got, vec![vec![4], vec![7, 2], vec![9, 6, 3, 1]]);
    assert_eq!(levels(invert_tree(None)), Vec::<Vec<i32>>::new());
    println!("PASS");
}}
''',
"lua": '''{H}
local function invert_tree(root)
    if not root then return nil end
    local stack = {{root}}
    while #stack > 0 do
        local node = table.remove(stack)
        node.left, node.right = node.right, node.left
        if node.left then stack[#stack + 1] = node.left end
        if node.right then stack[#stack + 1] = node.right end
    end
    return root
end
local function levels(root)
    if not root then return {{}} end
    local res = {{}}
    local q = {{root}}
    while #q > 0 do
        local cur = {{}}
        local n = #q
        for i = 1, n do
            local node = table.remove(q, 1)
            cur[#cur + 1] = node.val
            if node.left then q[#q + 1] = node.left end
            if node.right then q[#q + 1] = node.right end
        end
        res[#res + 1] = cur
    end
    return res
end
local got = levels(invert_tree(build_tree({{4,2,7,1,3,6,9}})))
assert(#got == 3 and got[1][1] == 4 and got[2][1] == 7 and got[2][2] == 2 and got[3][1] == 9 and got[3][4] == 1, "invert failed")
assert(#levels(invert_tree(nil)) == 0)
print("PASS")
''',
"c": '''{H}
static TreeNode *invert_tree(TreeNode *root) {{
    if (!root) return NULL;
    TreeNode *stack[256];
    int top = 0;
    stack[top++] = root;
    while (top > 0) {{
        TreeNode *node = stack[--top];
        TreeNode *tmp = node->left; node->left = node->right; node->right = tmp;
        if (node->left) stack[top++] = node->left;
        if (node->right) stack[top++] = node->right;
    }}
    return root;
}}
static void levels(TreeNode *root, int *out, int *n) {{
    /* 只验证前 7 个层序值（用例树共 7 节点） */
    *n = 0;
    if (!root) return;
    TreeNode *q[256]; int head = 0, tail = 0;
    q[tail++] = root;
    while (head < tail) {{
        TreeNode *node = q[head++];
        out[(*n)++] = node->val;
        if (node->left) q[tail++] = node->left;
        if (node->right) q[tail++] = node->right;
    }}
}}
int main(void) {{
    int vals[] = {{4,2,7,1,3,6,9}};
    int want[] = {{4,7,2,9,6,3,1}};
    int got[16], n = 0;
    TreeNode *t = invert_tree(build_tree(vals, 7));
    levels(t, got, &n);
    for (int i = 0; i < 7; i++) if (got[i] != want[i]) {{ printf("FAIL %d\\n", i); return 1; }}
    if (invert_tree(NULL) != NULL) {{ printf("FAIL null\\n"); return 1; }}
    free_tree(t);
    printf("PASS\\n");
    return 0;
}}
''',
"cpp": '''{H}
static TreeNode *invertTree(TreeNode *root) {{
    if (!root) return nullptr;
    std::vector<TreeNode *> stack{{root}};
    while (!stack.empty()) {{
        auto *node = stack.back();
        stack.pop_back();
        std::swap(node->left, node->right);
        if (node->left) stack.push_back(node->left);
        if (node->right) stack.push_back(node->right);
    }}
    return root;
}}
static std::vector<int> levels(TreeNode *root) {{
    std::vector<int> out;
    if (!root) return out;
    std::queue<TreeNode *> q;
    q.push(root);
    while (!q.empty()) {{
        auto *n = q.front(); q.pop();
        out.push_back(n->val);
        if (n->left) q.push(n->left);
        if (n->right) q.push(n->right);
    }}
    return out;
}}
int main() {{
    auto *t = invertTree(build_tree({{4, 2, 7, 1, 3, 6, 9}}));
    assert((levels(t) == std::vector<int>{{4, 7, 2, 9, 6, 3, 1}}));
    assert(invertTree(nullptr) == nullptr);
    free_tree(t);
    std::cout << "PASS" << std::endl;
    return 0;
}}
''',
"r": '''{H}
invert_tree <- function(root) {{
  if (is.null(root)) return(NULL)
  stack <- list(root)
  while (length(stack) > 0) {{
    node <- stack[[length(stack)]]
    stack[[length(stack)]] <- NULL
    tmp <- node$left; node$left <- node$right; node$right <- tmp
    if (!is.null(node$left)) stack[[length(stack) + 1L]] <- node$left
    if (!is.null(node$right)) stack[[length(stack) + 1L]] <- node$right
  }}
  root
}}
lvl_vals <- function(root) unlist(tree_to_levels(root))
stopifnot(identical(lvl_vals(invert_tree(build_tree(list(4L, 2L, 7L, 1L, 3L, 6L, 9L)))), c(4L, 7L, 2L, 9L, 6L, 3L, 1L)))
stopifnot(is.null(invert_tree(NULL)))
cat("PASS\\n")
''',
"zig": '''{H}
fn invertTree(root: ?*TreeNode) ?*TreeNode {{
    const r = root orelse return null;
    var stack = std.ArrayList(*TreeNode).init(std.heap.page_allocator);
    defer stack.deinit();
    stack.append(r) catch unreachable;
    while (stack.items.len > 0) {{
        const node = stack.pop().?;
        const tmp = node.left;
        node.left = node.right;
        node.right = tmp;
        if (node.left) |c| stack.append(c) catch unreachable;
        if (node.right) |c| stack.append(c) catch unreachable;
    }}
    return r;
}}
fn levels(root: ?*TreeNode, out: *std.ArrayList(i32)) void {{
    const r = root orelse return;
    var q = std.ArrayList(*TreeNode).init(std.heap.page_allocator);
    defer q.deinit();
    q.append(r) catch unreachable;
    var head: usize = 0;
    while (head < q.items.len) {{
        const node = q.items[head];
        head += 1;
        out.append(node.val) catch unreachable;
        if (node.left) |c| q.append(c) catch unreachable;
        if (node.right) |c| q.append(c) catch unreachable;
    }}
}}
pub fn main() !void {{
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();
    const alloc = arena.allocator();
    const t = try buildTree(alloc, &[_]i32{{ 4, 2, 7, 1, 3, 6, 9 }});
    var out = std.ArrayList(i32).init(std.heap.page_allocator);
    defer out.deinit();
    levels(invertTree(t), &out);
    const want = [_]i32{{ 4, 7, 2, 9, 6, 3, 1 }};
    if (out.items.len != want.len) return error.TestFailed;
    for (want, 0..) |w, i| if (out.items[i] != w) return error.TestFailed;
    if (invertTree(null) != null) return error.TestFailed;
    std.debug.print("PASS\\n", .{{}});
}}
''',
"dart": '''{H}
TreeNode? invertTree(TreeNode? root) {{
  if (root == null) return null;
  final stack = <TreeNode>[root];
  while (stack.isNotEmpty) {{
    final node = stack.removeLast();
    final tmp = node.left;
    node.left = node.right;
    node.right = tmp;
    if (node.left != null) stack.add(node.left!);
    if (node.right != null) stack.add(node.right!);
  }}
  return root;
}}
void main() {{
  final t = invertTree(buildTree([4, 2, 7, 1, 3, 6, 9]));
  final flat = treeToLevels(t).map((l) => l.join(',')).join('|');
  if (flat != '4|7,2|9,6,3,1') throw StateError('invert failed: $flat');
  if (invertTree(null) != null) throw StateError('null failed');
  print('PASS');
}}
''',
}

# ---------- lc_700 BST 搜索 ----------
A700 = {
"rust": '''{H}
fn search_bst(root: Option<Rc<RefCell<TreeNode>>>, val: i32) -> Option<i32> {{
    let mut cur = root;
    while let Some(node) = cur {{
        let n = node.borrow();
        if n.val == val {{ return Some(n.val); }}
        cur = if n.val > val {{ n.left.clone() }} else {{ n.right.clone() }};
    }}
    None
}}
fn main() {{
    let t = build_tree(&[Some(4), Some(2), Some(7), Some(1), Some(3)]);
    assert_eq!(search_bst(t.clone(), 2), Some(2));
    assert_eq!(search_bst(t.clone(), 5), None);
    assert_eq!(search_bst(t.clone(), 4), Some(4));
    assert_eq!(search_bst(None, 1), None);
    println!("PASS");
}}
''',
"lua": '''{H}
local function search_bst(root, val)
    local cur = root
    while cur do
        if cur.val == val then return cur.val end
        if cur.val > val then cur = cur.left else cur = cur.right end
    end
    return nil
end
local t = build_tree({{4, 2, 7, 1, 3}})
assert(search_bst(t, 2) == 2)
assert(search_bst(t, 5) == nil)
assert(search_bst(t, 4) == 4)
assert(search_bst(nil, 1) == nil)
print("PASS")
''',
"c": '''{H}
static TreeNode *search_bst(TreeNode *root, int val) {{
    TreeNode *cur = root;
    while (cur) {{
        if (cur->val == val) return cur;
        else if (cur->val > val) cur = cur->left;
        else cur = cur->right;
    }}
    return NULL;
}}
int main(void) {{
    int vals[] = {{4,2,7,1,3}};
    TreeNode *t = build_tree(vals, 5);
    if (search_bst(t, 2)->val != 2) {{ printf("FAIL 1\\n"); return 1; }}
    if (search_bst(t, 5) != NULL) {{ printf("FAIL 2\\n"); return 1; }}
    if (search_bst(t, 4)->val != 4) {{ printf("FAIL 3\\n"); return 1; }}
    if (search_bst(NULL, 1) != NULL) {{ printf("FAIL 4\\n"); return 1; }}
    free_tree(t);
    printf("PASS\\n");
    return 0;
}}
''',
"cpp": '''{H}
static TreeNode *searchBST(TreeNode *root, int val) {{
    TreeNode *cur = root;
    while (cur) {{
        if (cur->val == val) return cur;
        else if (cur->val > val) cur = cur->left;
        else cur = cur->right;
    }}
    return nullptr;
}}
int main() {{
    auto *t = build_tree({{4, 2, 7, 1, 3}});
    assert(searchBST(t, 2) != nullptr && searchBST(t, 2)->val == 2);
    assert(searchBST(t, 5) == nullptr);
    assert(searchBST(t, 4)->val == 4);
    assert(searchBST(nullptr, 1) == nullptr);
    free_tree(t);
    std::cout << "PASS" << std::endl;
    return 0;
}}
''',
"r": '''{H}
search_bst <- function(root, val) {{
  cur <- root
  while (!is.null(cur)) {{
    if (cur$val == val) return(cur$val)
    if (cur$val > val) cur <- cur$left else cur <- cur$right
  }}
  NULL
}}
t <- build_tree(list(4L, 2L, 7L, 1L, 3L))
stopifnot(search_bst(t, 2L) == 2L)
stopifnot(is.null(search_bst(t, 5L)))
stopifnot(search_bst(t, 4L) == 4L)
stopifnot(is.null(search_bst(NULL, 1L)))
cat("PASS\\n")
''',
"zig": '''{H}
fn searchBST(root: ?*TreeNode, val: i32) ?i32 {{
    var cur = root;
    while (cur) |node| {{
        if (node.val == val) return node.val;
        cur = if (node.val > val) node.left else node.right;
    }}
    return null;
}}
pub fn main() !void {{
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();
    const t = try buildTree(arena.allocator(), &[_]i32{{ 4, 2, 7, 1, 3 }});
    if (searchBST(t, 2) != 2) return error.TestFailed;
    if (searchBST(t, 5) != null) return error.TestFailed;
    if (searchBST(t, 4) != 4) return error.TestFailed;
    if (searchBST(null, 1) != null) return error.TestFailed;
    std.debug.print("PASS\\n", .{{}});
}}
''',
"dart": '''{H}
int? searchBST(TreeNode? root, int val) {{
  var cur = root;
  while (cur != null) {{
    if (cur.val == val) return cur.val;
    cur = cur.val > val ? cur.left : cur.right;
  }}
  return null;
}}
void main() {{
  final t = buildTree([4, 2, 7, 1, 3]);
  if (searchBST(t, 2) != 2) throw StateError('c1');
  if (searchBST(t, 5) != null) throw StateError('c2');
  if (searchBST(t, 4) != 4) throw StateError('c3');
  if (searchBST(null, 1) != null) throw StateError('c4');
  print('PASS');
}}
''',
}

# ---------- lc_543 直径 ----------
A543 = {
"rust": '''{H}
fn diameter_of_binary_tree(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {{
    let mut ans = 0;
    fn depth(n: Option<&Rc<RefCell<TreeNode>>>, ans: &mut i32) -> i32 {{
        let node = match n {{ Some(x) => x, None => return 0 }};
        let nb = node.borrow();
        let l = depth(nb.left.as_ref(), ans);
        let r = depth(nb.right.as_ref(), ans);
        if l + r > *ans {{ *ans = l + r; }}
        1 + l.max(r)
    }}
    depth(root.as_ref(), &mut ans);
    ans
}}
fn main() {{
    let t = build_tree(&[Some(1), Some(2), Some(3), Some(4), Some(5)]);
    assert_eq!(diameter_of_binary_tree(t), 3);
    assert_eq!(diameter_of_binary_tree(None), 0);
    println!("PASS");
}}
''',
"lua": '''{H}
local function diameter_of_binary_tree(root)
    local ans = 0
    local function depth(n)
        if not n then return 0 end
        local l = depth(n.left)
        local r = depth(n.right)
        if l + r > ans then ans = l + r end
        return 1 + math.max(l, r)
    end
    depth(root)
    return ans
end
assert(diameter_of_binary_tree(build_tree({{1,2,3,4,5}})) == 3)
assert(diameter_of_binary_tree(nil) == 0)
print("PASS")
''',
"c": '''{H}
static int g_ans;
static int depth(TreeNode *n) {{
    if (!n) return 0;
    int l = depth(n->left), r = depth(n->right);
    if (l + r > g_ans) g_ans = l + r;
    return (l > r ? l : r) + 1;
}}
static int diameter_of_binary_tree(TreeNode *root) {{
    g_ans = 0;
    depth(root);
    return g_ans;
}}
int main(void) {{
    int vals[] = {{1,2,3,4,5}};
    TreeNode *t = build_tree(vals, 5);
    if (diameter_of_binary_tree(t) != 3) {{ printf("FAIL 1\\n"); return 1; }}
    if (diameter_of_binary_tree(NULL) != 0) {{ printf("FAIL 2\\n"); return 1; }}
    free_tree(t);
    printf("PASS\\n");
    return 0;
}}
''',
"cpp": '''{H}
static int diameterOfBinaryTree(TreeNode *root) {{
    int ans = 0;
    std::function<int(TreeNode *)> depth = [&](TreeNode *n) -> int {{
        if (!n) return 0;
        int l = depth(n->left), r = depth(n->right);
        ans = std::max(ans, l + r);
        return std::max(l, r) + 1;
    }};
    depth(root);
    return ans;
}}
int main() {{
    assert(diameterOfBinaryTree(build_tree({{1, 2, 3, 4, 5}})) == 3);
    assert(diameterOfBinaryTree(nullptr) == 0);
    std::cout << "PASS" << std::endl;
    return 0;
}}
''',
"r": '''{H}
diameter_of_binary_tree <- function(root) {{
  ans <- 0L
  depth <- function(n) {{
    if (is.null(n)) return(0L)
    l <- depth(n$left); r <- depth(n$right)
    if (l + r > ans) ans <<- l + r
    max(l, r) + 1L
  }}
  depth(root)
  ans
}}
stopifnot(diameter_of_binary_tree(build_tree(list(1L, 2L, 3L, 4L, 5L))) == 3L)
stopifnot(diameter_of_binary_tree(NULL) == 0L)
cat("PASS\\n")
''',
"zig": '''{H}
fn diameterOfBinaryTree(root: ?*TreeNode) i32 {{
    var ans: i32 = 0;
    const D = struct {{
        fn depth(n: ?*TreeNode, best: *i32) i32 {{
            const node = n orelse return 0;
            const l = depth(node.left, best);
            const r = depth(node.right, best);
            if (l + r > best.*) best.* = l + r;
            return @max(l, r) + 1;
        }}
    }};
    _ = D.depth(root, &ans);
    return ans;
}}
pub fn main() !void {{
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();
    const t = try buildTree(arena.allocator(), &[_]i32{{ 1, 2, 3, 4, 5 }});
    if (diameterOfBinaryTree(t) != 3) return error.TestFailed;
    if (diameterOfBinaryTree(null) != 0) return error.TestFailed;
    std.debug.print("PASS\\n", .{{}});
}}
''',
"dart": '''{H}
int diameterOfBinaryTree(TreeNode? root) {{
  var ans = 0;
  int depth(TreeNode? n) {{
    if (n == null) return 0;
    final l = depth(n.left);
    final r = depth(n.right);
    if (l + r > ans) ans = l + r;
    return (l > r ? l : r) + 1;
  }}
  depth(root);
  return ans;
}}
void main() {{
  if (diameterOfBinaryTree(buildTree([1, 2, 3, 4, 5])) != 3) throw StateError('c1');
  if (diameterOfBinaryTree(null) != 0) throw StateError('c2');
  print('PASS');
}}
''',
}

# ---------- lc_110 平衡二叉树 ----------
A110 = {
"rust": '''{H}
fn height(n: Option<&Rc<RefCell<TreeNode>>>) -> i32 {{
    let node = match n {{ Some(x) => x, None => return 0 }};
    let nb = node.borrow();
    1 + height(nb.left.as_ref()).max(height(nb.right.as_ref()))
}}
fn is_balanced(root: Option<&Rc<RefCell<TreeNode>>>) -> bool {{
    let node = match root {{ Some(x) => x, None => return true }};
    let nb = node.borrow();
    (height(nb.left.as_ref()) - height(nb.right.as_ref())).abs() <= 1
        && is_balanced(nb.left.as_ref())
        && is_balanced(nb.right.as_ref())
}}
fn main() {{
    let t1 = build_tree(&[Some(3), Some(9), Some(20), None, None, Some(15), Some(7)]);
    let t2 = build_tree(&[Some(1), Some(2), Some(2), Some(3), Some(3), None, None, Some(4), Some(4)]);
    assert!(is_balanced(t1.as_ref()));
    assert!(!is_balanced(t2.as_ref()));
    assert!(is_balanced(None));
    println!("PASS");
}}
''',
"lua": '''{H}
local function height(n)
    if not n then return 0 end
    return 1 + math.max(height(n.left), height(n.right))
end
local function is_balanced(root)
    if not root then return true end
    if math.abs(height(root.left) - height(root.right)) > 1 then return false end
    return is_balanced(root.left) and is_balanced(root.right)
end
assert(is_balanced(build_tree({{3, 9, 20, "null", "null", 15, 7}})) == true)
assert(is_balanced(build_tree({{1, 2, 2, 3, 3, "null", "null", 4, 4}})) == false)
assert(is_balanced(nil) == true)
print("PASS")
''',
"c": '''{H}
static int height(TreeNode *n) {{
    if (!n) return 0;
    int l = height(n->left), r = height(n->right);
    return (l > r ? l : r) + 1;
}}
static int is_balanced(TreeNode *root) {{
    if (!root) return 1;
    int lh = height(root->left), rh = height(root->right);
    int d = lh - rh;
    if (d < 0) d = -d;
    if (d > 1) return 0;
    return is_balanced(root->left) && is_balanced(root->right);
}}
int main(void) {{
    int v1[] = {{3,9,20,INT_MIN_SN,INT_MIN_SN,15,7}};
    int v2[] = {{1,2,2,3,3,INT_MIN_SN,INT_MIN_SN,4,4}};
    if (!is_balanced(build_tree(v1, 7))) {{ printf("FAIL 1\\n"); return 1; }}
    if (is_balanced(build_tree(v2, 9))) {{ printf("FAIL 2\\n"); return 1; }}
    if (!is_balanced(NULL)) {{ printf("FAIL 3\\n"); return 1; }}
    printf("PASS\\n");
    return 0;
}}
''',
"cpp": '''{H}
static int height(TreeNode *n) {{
    if (!n) return 0;
    return std::max(height(n->left), height(n->right)) + 1;
}}
static bool isBalanced(TreeNode *root) {{
    if (!root) return true;
    if (std::abs(height(root->left) - height(root->right)) > 1) return false;
    return isBalanced(root->left) && isBalanced(root->right);
}}
int main() {{
    assert(isBalanced(build_tree({{3, 9, 20, std::nullopt, std::nullopt, 15, 7}})));
    assert(!isBalanced(build_tree({{1, 2, 2, 3, 3, std::nullopt, std::nullopt, 4, 4}})));
    assert(isBalanced(nullptr));
    std::cout << "PASS" << std::endl;
    return 0;
}}
''',
"r": '''{H}
height <- function(n) {{
  if (is.null(n)) return(0L)
  max(height(n$left), height(n$right)) + 1L
}}
is_balanced <- function(root) {{
  if (is.null(root)) return(TRUE)
  if (abs(height(root$left) - height(root$right)) > 1) return(FALSE)
  is_balanced(root$left) && is_balanced(root$right)
}}
stopifnot(is_balanced(build_tree(list(3L, 9L, 20L, NA, NA, 15L, 7L))))
stopifnot(!is_balanced(build_tree(list(1L, 2L, 2L, 3L, 3L, NA, NA, 4L, 4L))))
stopifnot(is_balanced(NULL))
cat("PASS\\n")
''',
"zig": '''{H}
fn height(n: ?*TreeNode) i32 {{
    const node = n orelse return 0;
    return @max(height(node.left), height(node.right)) + 1;
}}
fn isBalanced(root: ?*TreeNode) bool {{
    const node = root orelse return true;
    const d = height(node.left) - height(node.right);
    if (d > 1 or d < -1) return false;
    return isBalanced(node.left) and isBalanced(node.right);
}}
pub fn main() !void {{
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();
    const alloc = arena.allocator();
    const t1 = try buildTree(alloc, &[_]i32{{ 3, 9, 20, -1, -1, 15, 7 }});
    const t2 = try buildTree(alloc, &[_]i32{{ 1, 2, 2, 3, 3, -1, -1, 4, 4 }});
    if (!isBalanced(t1)) return error.TestFailed;
    if (isBalanced(t2)) return error.TestFailed;
    if (!isBalanced(null)) return error.TestFailed;
    std.debug.print("PASS\\n", .{{}});
}}
''',
"dart": '''{H}
int height(TreeNode? n) {{
  if (n == null) return 0;
  return (height(n.left) > height(n.right) ? height(n.left) : height(n.right)) + 1;
}}
bool isBalanced(TreeNode? root) {{
  if (root == null) return true;
  final d = height(root.left) - height(root.right);
  if (d > 1 || d < -1) return false;
  return isBalanced(root.left) && isBalanced(root.right);
}}
void main() {{
  if (!isBalanced(buildTree([3, 9, 20, null, null, 15, 7]))) throw StateError('c1');
  if (isBalanced(buildTree([1, 2, 2, 3, 3, null, null, 4, 4]))) throw StateError('c2');
  if (!isBalanced(null)) throw StateError('c3');
  print('PASS');
}}
''',
}

# ---------- 发射 ----------
PROBS = [
    ("lc_100_相同的树", A100, "LeetCode 100. 相同的树"),
    ("lc_226_翻转二叉树", A226, "LeetCode 226. 翻转二叉树"),
    ("lc_700_二叉搜索树中的搜索", A700, "LeetCode 700. 二叉搜索树中的搜索"),
    ("lc_543_二叉树的直径", A543, "LeetCode 543. 二叉树的直径"),
    ("lc_110_平衡二叉树", A110, "LeetCode 110. 平衡二叉树"),
]
import os
count = 0
for prob, algo, title in PROBS:
    bid = B[prob.split("_")[1]]
    ts_dir = f"/Users/Wang/Code/github/web-x-blog/work/blog/courses/20.dsa/ts/tree/{prob}"
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
