#!/usr/bin/env python3
# gen_tree6.py — tree 第六批：lc_98/lc_236/lc_572/lc_199/lc_429 × 7语言
import sys, os; sys.path.insert(0, "/Users/Wang/Code/github/web-x-blog/work/blog/courses/21.dsa/_tools")
from langlib import emit, TREE_H, head_comment, EXT

B = {"98": "135314196", "236": "136528287", "572": "137409838", "199": "134975159", "429": "137532387"}
LANGNAME = {"rust": "Rust", "lua": "Lua", "c": "C", "cpp": "C++", "r": "R", "zig": "Zig", "dart": "Dart"}

SAME = {
"rust": '''fn same_tree(p: Option<&Rc<RefCell<TreeNode>>>, q: Option<&Rc<RefCell<TreeNode>>>) -> bool {
    match (p, q) {
        (None, None) => true,
        (Some(a), Some(b)) => { let (a, b) = (a.borrow(), b.borrow()); a.val == b.val && same_tree(a.left.as_ref(), b.left.as_ref()) && same_tree(a.right.as_ref(), b.right.as_ref()) }
        _ => false,
    }
}
''',
"lua": '''local function same_tree(p, q)
    if not p and not q then return true end
    if not p or not q or p.val ~= q.val then return false end
    return same_tree(p.left, q.left) and same_tree(p.right, q.right)
end
''',
"c": '''static int same_tree(const TreeNode *p, const TreeNode *q) {
    if (!p && !q) return 1;
    if (!p || !q || p->val != q->val) return 0;
    return same_tree(p->left, q->left) && same_tree(p->right, q->right);
}
''',
"cpp": '''static bool sameTree(const TreeNode *p, const TreeNode *q) {
    if (!p && !q) return true;
    if (!p || !q || p->val != q->val) return false;
    return sameTree(p->left, q->left) && sameTree(p->right, q->right);
}
''',
"r": '''same_tree <- function(p, q) {
  if (is.null(p) && is.null(q)) return(TRUE)
  if (is.null(p) || is.null(q) || p$val != q$val) return(FALSE)
  same_tree(p$left, q$left) && same_tree(p$right, q$right)
}
''',
"zig": '''fn sameTree(p: ?*const TreeNode, q: ?*const TreeNode) bool {
    if (p == null and q == null) return true;
    if (p == null or q == null) return false;
    const a = p.?;
    const b = q.?;
    return a.val == b.val and sameTree(a.left, b.left) and sameTree(a.right, b.right);
}
''',
"dart": '''bool sameTree(TreeNode? p, TreeNode? q) {
  if (p == null && q == null) return true;
  if (p == null || q == null || p.val != q.val) return false;
  return sameTree(p.left, q.left) && sameTree(p.right, q.right);
}
''',
}

A98 = {
"rust": '''{H}
fn is_valid_bst(root: Option<Rc<RefCell<TreeNode>>>) -> bool {{
    let root = match root {{ Some(x) => x, None => return true }};
    let mut stack: Vec<(Rc<RefCell<TreeNode>>, Option<i64>, Option<i64>)> = vec![(root, None, None)];
    while let Some((node, low, high)) = stack.pop() {{
        let nb = node.borrow();
        let v = nb.val as i64;
        if let Some(l) = low {{
            if v <= l {{ return false; }}
        }}
        if let Some(h) = high {{
            if v >= h {{ return false; }}
        }}
        if let Some(r) = nb.right.clone() {{ stack.push((r, Some(v), high)); }}
        if let Some(l) = nb.left.clone() {{ stack.push((l, low, Some(v))); }}
    }}
    true
}}
fn main() {{
    assert!(is_valid_bst(build_tree(&[Some(2), Some(1), Some(3)])));
    assert!(!is_valid_bst(build_tree(&[Some(5), Some(1), Some(4), None, None, Some(3), Some(6)])));
    assert!(is_valid_bst(None));
    println!("PASS");
}}
''',
"lua": '''{H}
local function is_valid_bst(root)
    if not root then return true end
    local stack = {{{{root, nil, nil}}}}
    while #stack > 0 do
        local node, low, high = table.unpack(table.remove(stack))
        if low and node.val <= low then return false end
        if high and node.val >= high then return false end
        if node.right then stack[#stack + 1] = {{node.right, node.val, high}} end
        if node.left then stack[#stack + 1] = {{node.left, low, node.val}} end
    end
    return true
end
assert(is_valid_bst(build_tree({{2, 1, 3}})) == true)
assert(is_valid_bst(build_tree({{5, 1, 4, "null", "null", 3, 6}})) == false)
assert(is_valid_bst(nil) == true)
print("PASS")
''',
"c": '''{H}
typedef struct {{ TreeNode *n; int has_l, has_h; long low, high; }} BN;
static int is_valid_bst(TreeNode *root) {{
    if (!root) return 1;
    BN stack[256];
    int top = 0;
    stack[top++] = (BN){{root, 0, 0, 0, 0}};
    while (top > 0) {{
        BN b = stack[--top];
        long v = b.n->val;
        if (b.has_l && v <= b.low) return 0;
        if (b.has_h && v >= b.high) return 0;
        if (b.n->right) stack[top++] = (BN){{b.n->right, 1, b.has_h, v, b.high}};
        if (b.n->left) stack[top++] = (BN){{b.n->left, b.has_l, 1, b.low, v}};
    }}
    return 1;
}}
int main(void) {{
    int v1[] = {{2,1,3}};
    int v2[] = {{5,1,4,INT_MIN_SN,INT_MIN_SN,3,6}};
    if (!is_valid_bst(build_tree(v1, 3))) {{ printf("FAIL 1\\n"); return 1; }}
    if (is_valid_bst(build_tree(v2, 7))) {{ printf("FAIL 2\\n"); return 1; }}
    if (!is_valid_bst(NULL)) {{ printf("FAIL 3\\n"); return 1; }}
    printf("PASS\\n");
    return 0;
}}
''',
"cpp": '''{H}
static bool isValidBST(TreeNode *root) {{
    if (!root) return true;
    struct BN {{ TreeNode *n; std::optional<long> low, high; }};
    std::vector<BN> stack{{{{root, std::nullopt, std::nullopt}}}};
    while (!stack.empty()) {{
        auto [n, low, high] = stack.back();
        stack.pop_back();
        long v = n->val;
        if (low.has_value() && v <= *low) return false;
        if (high.has_value() && v >= *high) return false;
        if (n->right) stack.push_back({{n->right, v, high}});
        if (n->left) stack.push_back({{n->left, low, v}});
    }}
    return true;
}}
int main() {{
    assert(isValidBST(build_tree({{2, 1, 3}})));
    assert(!isValidBST(build_tree({{5, 1, 4, std::nullopt, std::nullopt, 3, 6}})));
    assert(isValidBST(nullptr));
    std::cout << "PASS" << std::endl;
    return 0;
}}
''',
"r": '''{H}
is_valid_bst <- function(root) {{
  if (is.null(root)) return(TRUE)
  stack <- list(list(root, NULL, NULL))
  while (length(stack) > 0) {{
    b <- stack[[length(stack)]]
    stack[[length(stack)]] <- NULL
    node <- b[[1]]; low <- b[[2]]; high <- b[[3]]
    v <- node$val
    if (!is.null(low) && v <= low) return(FALSE)
    if (!is.null(high) && v >= high) return(FALSE)
    if (!is.null(node$right)) stack[[length(stack) + 1L]] <- list(node$right, v, high)
    if (!is.null(node$left)) stack[[length(stack) + 1L]] <- list(node$left, low, v)
  }}
  TRUE
}}
stopifnot(is_valid_bst(build_tree(list(2L, 1L, 3L))))
stopifnot(!is_valid_bst(build_tree(list(5L, 1L, 4L, NA, NA, 3L, 6L))))
stopifnot(is_valid_bst(NULL))
cat("PASS\\n")
''',
"zig": '''{H}
const BN = struct {{ n: *TreeNode, low: ?i64, high: ?i64 }};
fn isValidBST(root: ?*TreeNode) bool {{
    const r = root orelse return true;
    var stack = std.ArrayList(BN).init(std.heap.page_allocator);
    defer stack.deinit();
    stack.append(.{{ .n = r, .low = null, .high = null }}) catch unreachable;
    while (stack.items.len > 0) {{
        const b = stack.pop().?;
        const v: i64 = b.n.val;
        if (b.low) |l| if (v <= l) return false;
        if (b.high) |h| if (v >= h) return false;
        if (b.n.right) |c| stack.append(.{{ .n = c, .low = v, .high = b.high }}) catch unreachable;
        if (b.n.left) |c| stack.append(.{{ .n = c, .low = b.low, .high = v }}) catch unreachable;
    }}
    return true;
}}
pub fn main() !void {{
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();
    const alloc = arena.allocator();
    if (!isValidBST(try buildTree(alloc, &[_]i32{{ 2, 1, 3 }}))) return error.TestFailed;
    if (isValidBST(try buildTree(alloc, &[_]i32{{ 5, 1, 4, -1, -1, 3, 6 }}))) return error.TestFailed;
    if (!isValidBST(null)) return error.TestFailed;
    std.debug.print("PASS\\n", .{{}});
}}
''',
"dart": '''{H}
class _BN {
  final TreeNode n;
  final int? low, high;
  _BN(this.n, this.low, this.high);
}
bool isValidBST(TreeNode? root) {{
  if (root == null) return true;
  final stack = <_BN>[_BN(root, null, null)];
  while (stack.isNotEmpty) {{
    final b = stack.removeLast();
    final v = b.n.val;
    if (b.low != null && v <= b.low!) return false;
    if (b.high != null && v >= b.high!) return false;
    if (b.n.right != null) stack.add(_BN(b.n.right!, v, b.high));
    if (b.n.left != null) stack.add(_BN(b.n.left!, b.low, v));
  }}
  return true;
}}
void main() {{
  if (!isValidBST(buildTree([2, 1, 3]))) throw StateError('c1');
  if (isValidBST(buildTree([5, 1, 4, null, null, 3, 6]))) throw StateError('c2');
  if (!isValidBST(null)) throw StateError('c3');
  print('PASS');
}}
''',
}

A236 = {
"rust": '''{H}
fn lca(n: Option<&Rc<RefCell<TreeNode>>>, p: i32, q: i32) -> Option<i32> {{
    let node = n?;
    let nb = node.borrow();
    if nb.val == p || nb.val == q {{ return Some(nb.val); }}
    let l = lca(nb.left.as_ref(), p, q);
    let r = lca(nb.right.as_ref(), p, q);
    if l.is_some() && r.is_some() {{ return Some(nb.val); }}
    l.or(r)
}}
fn lowest_common_ancestor(root: Option<Rc<RefCell<TreeNode>>>, p: i32, q: i32) -> i32 {{
    lca(root.as_ref(), p, q).unwrap_or(-1)
}}
fn main() {{
    let t = build_tree(&[Some(3), Some(5), Some(1), Some(6), Some(2), Some(0), Some(8), None, None, Some(7), Some(4)]);
    assert_eq!(lowest_common_ancestor(t.clone(), 5, 1), 3);
    assert_eq!(lowest_common_ancestor(t, 5, 4), 5);
    println!("PASS");
}}
''',
"lua": '''{H}
local function lca(n, p, q)
    if not n then return nil end
    if n.val == p or n.val == q then return n.val end
    local l = lca(n.left, p, q)
    local r = lca(n.right, p, q)
    if l and r then return n.val end
    if l then return l end
    return r
end
local function lowest_common_ancestor(root, p, q)
    return lca(root, p, q) or -1
end
local t = build_tree({{3, 5, 1, 6, 2, 0, 8, "null", "null", 7, 4}})
assert(lowest_common_ancestor(t, 5, 1) == 3)
assert(lowest_common_ancestor(t, 5, 4) == 5)
print("PASS")
''',
"c": '''{H}
static int lca(TreeNode *n, int p, int q, int *found) {{
    if (!n) return -1;
    if (n->val == p || n->val == q) {{ (*found)++; return n->val; }}
    int f_before = *found;
    int l = lca(n->left, p, q, found);
    int r = lca(n->right, p, q, found);
    if (*found >= 2) {{
        if (l != -1 && r != -1) return n->val;
        return (l != -1) ? l : r;
    }}
    if (*found > f_before) return (l != -1) ? l : r;
    return -1;
}}
static int lowest_common_ancestor(TreeNode *root, int p, int q) {{
    int found = 0;
    return lca(root, p, q, &found);
}}
int main(void) {{
    int v[] = {{3,5,1,6,2,0,8,INT_MIN_SN,INT_MIN_SN,7,4}};
    TreeNode *t = build_tree(v, 11);
    if (lowest_common_ancestor(t, 5, 1) != 3) {{ printf("FAIL 1\\n"); return 1; }}
    if (lowest_common_ancestor(t, 5, 4) != 5) {{ printf("FAIL 2\\n"); return 1; }}
    printf("PASS\\n");
    return 0;
}}
''',
"cpp": '''{H}
static int lca(TreeNode *n, int p, int q, int &found) {{
    if (!n) return -1;
    if (n->val == p || n->val == q) {{ ++found; return n->val; }}
    int before = found;
    int l = lca(n->left, p, q, found);
    int r = lca(n->right, p, q, found);
    if (l != -1 && r != -1) return n->val;
    if (found > before) return (l != -1) ? l : r;
    return -1;
}}
static int lowestCommonAncestor(TreeNode *root, int p, int q) {{
    int found = 0;
    return lca(root, p, q, found);
}}
int main() {{
    auto *t = build_tree({{3, 5, 1, 6, 2, 0, 8, std::nullopt, std::nullopt, 7, 4}});
    assert(lowestCommonAncestor(t, 5, 1) == 3);
    assert(lowestCommonAncestor(t, 5, 4) == 5);
    std::cout << "PASS" << std::endl;
    return 0;
}}
''',
"r": '''{H}
lca_fn <- function(n, p, q, found) {{
  if (is.null(n)) return(-1L)
  if (n$val == p || n$val == q) {{
    found$cnt <- found$cnt + 1L
    return(n$val)
  }}
  before <- found$cnt
  l <- lca_fn(n$left, p, q, found)
  r <- lca_fn(n$right, p, q, found)
  if (l != -1L && r != -1L) return(n$val)
  if (found$cnt > before) return(if (l != -1L) l else r)
  -1L
}}
lowest_common_ancestor <- function(root, p, q) {{
  found <- new.env(parent = emptyenv()); found$cnt <- 0L
  lca_fn(root, p, q, found)
}}
t <- build_tree(list(3L, 5L, 1L, 6L, 2L, 0L, 8L, NA, NA, 7L, 4L))
stopifnot(lowest_common_ancestor(t, 5L, 1L) == 3L)
stopifnot(lowest_common_ancestor(t, 5L, 4L) == 5L)
cat("PASS\\n")
''',
"zig": '''{H}
fn lca(n: ?*TreeNode, p: i32, q: i32, found: *i32) i32 {{
    const node = n orelse return -1;
    if (node.val == p or node.val == q) {{
        found.* += 1;
        return node.val;
    }}
    const before = found.*;
    const l = lca(node.left, p, q, found);
    const r = lca(node.right, p, q, found);
    if (l != -1 and r != -1) return node.val;
    if (found.* > before) return if (l != -1) l else r;
    return -1;
}}
fn lowestCommonAncestor(root: ?*TreeNode, p: i32, q: i32) i32 {{
    var found: i32 = 0;
    return lca(root, p, q, &found);
}}
pub fn main() !void {{
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();
    const t = try buildTree(arena.allocator(), &[_]i32{{ 3, 5, 1, 6, 2, 0, 8, -1, -1, 7, 4 }});
    if (lowestCommonAncestor(t, 5, 1) != 3) return error.TestFailed;
    if (lowestCommonAncestor(t, 5, 4) != 5) return error.TestFailed;
    std.debug.print("PASS\\n", .{{}});
}}
''',
"dart": '''{H}
class _F {
  int cnt = 0;
}
int lca(TreeNode? n, int p, int q, _F found) {{
  if (n == null) return -1;
  if (n.val == p || n.val == q) {{
    found.cnt++;
    return n.val;
  }}
  final before = found.cnt;
  final l = lca(n.left, p, q, found);
  final r = lca(n.right, p, q, found);
  if (l != -1 && r != -1) return n.val;
  if (found.cnt > before) return l != -1 ? l : r;
  return -1;
}}
int lowestCommonAncestor(TreeNode? root, int p, int q) {{
  return lca(root, p, q, _F());
}}
void main() {{
  final t = buildTree([3, 5, 1, 6, 2, 0, 8, null, null, 7, 4]);
  if (lowestCommonAncestor(t, 5, 1) != 3) throw StateError('c1');
  if (lowestCommonAncestor(t, 5, 4) != 5) throw StateError('c2');
  print('PASS');
}}
''',
}

A572 = {
"rust": '''{H}{S}
fn is_subtree(root: Option<Rc<RefCell<TreeNode>>>, sub: Option<Rc<RefCell<TreeNode>>>) -> bool {{
    fn check(a: Option<&Rc<RefCell<TreeNode>>>, b: Option<&Rc<RefCell<TreeNode>>>) -> bool {{
        match (a, b) {{
            (None, None) => true,
            (Some(x), Some(y)) => {{
                let (x, y) = (x.borrow(), y.borrow());
                x.val == y.val && check(x.left.as_ref(), y.left.as_ref()) && check(x.right.as_ref(), y.right.as_ref())
            }}
            _ => false,
        }}
    }}
    fn go(n: Option<&Rc<RefCell<TreeNode>>>, s: Option<&Rc<RefCell<TreeNode>>>) -> bool {{
        match n {{
            None => false,
            Some(x) => check(Some(x), s) || go(x.borrow().left.as_ref(), s) || go(x.borrow().right.as_ref(), s),
        }}
    }}
    go(root.as_ref(), sub.as_ref())
}}
fn main() {{
    assert!(is_subtree(build_tree(&[Some(3), Some(4), Some(5), Some(1), Some(2)]), build_tree(&[Some(4), Some(1), Some(2)])));
    assert!(!is_subtree(build_tree(&[Some(3), Some(4), Some(5), Some(1), Some(2), None, None, None, None, Some(0)]), build_tree(&[Some(4), Some(1), Some(2)])));
    assert!(!is_subtree(None, None));
    println!("PASS");
}}
''',
"lua": '''{H}{S}
local function check(a, b)
    if not a and not b then return true end
    if not a or not b or a.val ~= b.val then return false end
    return check(a.left, b.left) and check(a.right, b.right)
end
local function is_subtree(root, sub)
    if not root then return false end
    return check(root, sub) or is_subtree(root.left, sub) or is_subtree(root.right, sub)
end
assert(is_subtree(build_tree({{3, 4, 5, 1, 2}}), build_tree({{4, 1, 2}})) == true)
assert(is_subtree(build_tree({{3, 4, 5, 1, 2, "null", "null", "null", "null", 0}}), build_tree({{4, 1, 2}})) == false)
assert(is_subtree(nil, nil) == false)
print("PASS")
''',
"c": '''{H}{S}
static int check(const TreeNode *a, const TreeNode *b) {{
    if (!a && !b) return 1;
    if (!a || !b || a->val != b->val) return 0;
    return check(a->left, b->left) && check(a->right, b->right);
}}
static int is_subtree(const TreeNode *root, const TreeNode *sub) {{
    if (!root) return 0;
    return check(root, sub) || is_subtree(root->left, sub) || is_subtree(root->right, sub);
}}
int main(void) {{
    int a1[] = {{3,4,5,1,2}}, b[] = {{4,1,2}};
    int a2[] = {{3,4,5,1,2,INT_MIN_SN,INT_MIN_SN,INT_MIN_SN,INT_MIN_SN,0}};
    if (!is_subtree(build_tree(a1, 5), build_tree(b, 3))) {{ printf("FAIL 1\\n"); return 1; }}
    if (is_subtree(build_tree(a2, 10), build_tree(b, 3))) {{ printf("FAIL 2\\n"); return 1; }}
    if (is_subtree(NULL, NULL)) {{ printf("FAIL 3\\n"); return 1; }}
    printf("PASS\\n");
    return 0;
}}
''',
"cpp": '''{H}{S}
static bool check(const TreeNode *a, const TreeNode *b) {{
    if (!a && !b) return true;
    if (!a || !b || a->val != b->val) return false;
    return check(a->left, b->left) && check(a->right, b->right);
}}
static bool isSubtree(const TreeNode *root, const TreeNode *sub) {{
    if (!root) return false;
    return check(root, sub) || isSubtree(root->left, sub) || isSubtree(root->right, sub);
}}
int main() {{
    assert(isSubtree(build_tree({{3, 4, 5, 1, 2}}), build_tree({{4, 1, 2}})));
    assert(!isSubtree(build_tree({{3, 4, 5, 1, 2, std::nullopt, std::nullopt, std::nullopt, std::nullopt, 0}}), build_tree({{4, 1, 2}})));
    assert(!isSubtree(nullptr, nullptr));
    std::cout << "PASS" << std::endl;
    return 0;
}}
''',
"r": '''{H}{S}
check_fn <- function(a, b) {{
  if (is.null(a) && is.null(b)) return(TRUE)
  if (is.null(a) || is.null(b) || a$val != b$val) return(FALSE)
  check_fn(a$left, b$left) && check_fn(a$right, b$right)
}}
is_subtree <- function(root, sub) {{
  if (is.null(root)) return(FALSE)
  check_fn(root, sub) || is_subtree(root$left, sub) || is_subtree(root$right, sub)
}}
stopifnot(is_subtree(build_tree(list(3L, 4L, 5L, 1L, 2L)), build_tree(list(4L, 1L, 2L))))
stopifnot(!is_subtree(build_tree(list(3L, 4L, 5L, 1L, 2L, NA, NA, NA, NA, 0L)), build_tree(list(4L, 1L, 2L))))
stopifnot(!is_subtree(NULL, NULL))
cat("PASS\\n")
''',
"zig": '''{H}{S}
fn checkEq(a: ?*const TreeNode, b: ?*const TreeNode) bool {{
    if (a == null and b == null) return true;
    if (a == null or b == null) return false;
    const x = a.?;
    const y = b.?;
    return x.val == y.val and checkEq(x.left, y.left) and checkEq(x.right, y.right);
}}
fn isSubtree(root: ?*const TreeNode, sub: ?*const TreeNode) bool {{
    const n = root orelse return false;
    return checkEq(n, sub) or isSubtree(n.left, sub) or isSubtree(n.right, sub);
}}
pub fn main() !void {{
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();
    const alloc = arena.allocator();
    if (!isSubtree(try buildTree(alloc, &[_]i32{{ 3, 4, 5, 1, 2 }}), try buildTree(alloc, &[_]i32{{ 4, 1, 2 }}))) return error.TestFailed;
    if (isSubtree(try buildTree(alloc, &[_]i32{{ 3, 4, 5, 1, 2, -1, -1, -1, -1, 0 }}), try buildTree(alloc, &[_]i32{{ 4, 1, 2 }}))) return error.TestFailed;
    if (isSubtree(null, null)) return error.TestFailed;
    std.debug.print("PASS\\n", .{{}});
}}
''',
"dart": '''{H}{S}
bool checkEq(TreeNode? a, TreeNode? b) {{
  if (a == null && b == null) return true;
  if (a == null || b == null || a.val != b.val) return false;
  return checkEq(a.left, b.left) && checkEq(a.right, b.right);
}}
bool isSubtree(TreeNode? root, TreeNode? sub) {{
  if (root == null) return false;
  return checkEq(root, sub) || isSubtree(root.left, sub) || isSubtree(root.right, sub);
}}
void main() {{
  if (!isSubtree(buildTree([3, 4, 5, 1, 2]), buildTree([4, 1, 2]))) throw StateError('c1');
  if (isSubtree(buildTree([3, 4, 5, 1, 2, null, null, null, null, 0]), buildTree([4, 1, 2]))) throw StateError('c2');
  if (isSubtree(null, null)) throw StateError('c3');
  print('PASS');
}}
''',
}

A199 = {
"rust": '''{H}
fn right_side_view(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<i32> {{
    let mut result = Vec::new();
    fn dfs(n: Option<&Rc<RefCell<TreeNode>>>, depth: usize, result: &mut Vec<i32>) {{
        let node = match n {{ Some(x) => x, None => return }};
        if depth == result.len() {{ result.push(node.borrow().val); }}
        dfs(node.borrow().right.as_ref(), depth + 1, result);
        dfs(node.borrow().left.as_ref(), depth + 1, result);
    }}
    dfs(root.as_ref(), 0, &mut result);
    result
}}
fn main() {{
    assert_eq!(right_side_view(build_tree(&[Some(1), Some(2), Some(3), None, Some(5), None, Some(4)])), vec![1, 3, 4]);
    assert_eq!(right_side_view(None), Vec::<i32>::new());
    assert_eq!(right_side_view(build_tree(&[Some(1)])), vec![1]);
    println!("PASS");
}}
''',
"lua": '''{H}
local function right_side_view(root)
    local result = {{}}
    local function dfs(n, depth)
        if not n then return end
        if depth == #result then result[#result + 1] = n.val end
        dfs(n.right, depth + 1)
        dfs(n.left, depth + 1)
    end
    dfs(root, 0)
    return result
end
local function eq(a, b)
    if #a ~= #b then return false end
    for i = 1, #a do if a[i] ~= b[i] then return false end end
    return true
end
assert(eq(right_side_view(build_tree({{1, 2, 3, "null", 5, "null", 4}})), {{1, 3, 4}}))
assert(eq(right_side_view(nil), {{}}))
assert(eq(right_side_view(build_tree({{1}})), {{1}}))
print("PASS")
''',
"c": '''{H}
static void dfs_rsv(TreeNode *n, int depth, int *out, int *cnt) {{
    if (!n) return;
    if (depth == *cnt) out[(*cnt)++] = n->val;
    dfs_rsv(n->right, depth + 1, out, cnt);
    dfs_rsv(n->left, depth + 1, out, cnt);
}}
static int right_side_view(TreeNode *root, int out[]) {{
    int cnt = 0;
    dfs_rsv(root, 0, out, &cnt);
    return cnt;
}}
int main(void) {{
    int out[64], n;
    int v1[] = {{1,2,3,INT_MIN_SN,5,INT_MIN_SN,4}};
    int w1[] = {{1,3,4}};
    n = right_side_view(build_tree(v1, 7), out);
    if (n != 3 || out[0] != 1 || out[1] != 3 || out[2] != 4) {{ printf("FAIL 1\\n"); return 1; }}
    if (right_side_view(NULL, out) != 0) {{ printf("FAIL 2\\n"); return 1; }}
    int v3[] = {{1}};
    n = right_side_view(build_tree(v3, 1), out);
    if (n != 1 || out[0] != 1) {{ printf("FAIL 3\\n"); return 1; }}
    printf("PASS\\n");
    return 0;
}}
''',
"cpp": '''{H}
static std::vector<int> rightSideView(TreeNode *root) {{
    std::vector<int> result;
    std::function<void(TreeNode *, int)> dfs = [&](TreeNode *n, int depth) {{
        if (!n) return;
        if (depth == static_cast<int>(result.size())) result.push_back(n->val);
        dfs(n->right, depth + 1);
        dfs(n->left, depth + 1);
    }};
    dfs(root, 0);
    return result;
}}
int main() {{
    assert((rightSideView(build_tree({{1, 2, 3, std::nullopt, 5, std::nullopt, 4}})) == std::vector<int>{{1, 3, 4}}));
    assert(rightSideView(nullptr).empty());
    assert((rightSideView(build_tree({{1}})) == std::vector<int>{{1}}));
    std::cout << "PASS" << std::endl;
    return 0;
}}
''',
"r": '''{H}
right_side_view <- function(root) {{
  result <- integer(0)
  dfs <- function(n, depth) {{
    if (is.null(n)) return(invisible(NULL))
    if (depth == length(result)) result[[length(result) + 1L]] <<- n$val
    dfs(n$right, depth + 1L)
    dfs(n$left, depth + 1L)
  }}
  dfs(root, 0L)
  result
}}
stopifnot(identical(right_side_view(build_tree(list(1L, 2L, 3L, NA, 5L, NA, 4L))), c(1L, 3L, 4L)))
stopifnot(identical(right_side_view(NULL), integer(0)))
stopifnot(identical(right_side_view(build_tree(list(1L))), 1L))
cat("PASS\\n")
''',
"zig": '''{H}
fn rightSideView(root: ?*TreeNode, out: *std.ArrayList(i32)) void {{
    const D = struct {{
        fn dfs(n: ?*TreeNode, depth: usize, o: *std.ArrayList(i32)) void {{
            const node = n orelse return;
            if (depth == o.items.len) o.append(node.val) catch unreachable;
            dfs(node.right, depth + 1, o);
            dfs(node.left, depth + 1, o);
        }}
    }};
    D.dfs(root, 0, out);
}}
pub fn main() !void {{
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();
    const alloc = arena.allocator();
    var out = std.ArrayList(i32).init(std.heap.page_allocator);
    defer out.deinit();
    rightSideView(try buildTree(alloc, &[_]i32{{ 1, 2, 3, -1, 5, -1, 4 }}), &out);
    const w1 = [_]i32{{ 1, 3, 4 }};
    if (out.items.len != w1.len) return error.TestFailed;
    for (w1, 0..) |w, i| if (out.items[i] != w) return error.TestFailed;
    out.clearRetainingCapacity();
    rightSideView(null, &out);
    if (out.items.len != 0) return error.TestFailed;
    out.clearRetainingCapacity();
    rightSideView(try buildTree(alloc, &[_]i32{{1}}), &out);
    if (out.items.len != 1 or out.items[0] != 1) return error.TestFailed;
    std.debug.print("PASS\\n", .{{}});
}}
''',
"dart": '''{H}
List<int> rightSideView(TreeNode? root) {{
  final result = <int>[];
  void dfs(TreeNode? n, int depth) {{
    if (n == null) return;
    if (depth == result.length) result.add(n.val);
    dfs(n.right, depth + 1);
    dfs(n.left, depth + 1);
  }}
  dfs(root, 0);
  return result;
}}
void main() {{
  if (rightSideView(buildTree([1, 2, 3, null, 5, null, 4])).toString() != '[1, 3, 4]') throw StateError('c1');
  if (rightSideView(null).isNotEmpty) throw StateError('c2');
  if (rightSideView(buildTree([1])).toString() != '[1]') throw StateError('c3');
  print('PASS');
}}
''',
}

A429 = {
"rust": '''{H}
struct Node {{ val: i32, children: Vec<Node> }}
impl Node {{ fn new(v: i32) -> Node {{ Node {{ val: v, children: Vec::new() }} }} }}
fn level_order(root: Option<&Node>) -> Vec<Vec<i32>> {{
    let mut res = Vec::new();
    let root = match root {{ Some(x) => x, None => return res }};
    let mut q: Vec<&Node> = vec![root];
    while !q.is_empty() {{
        let mut level = Vec::new();
        let mut nxt = Vec::new();
        for n in q {{
            level.push(n.val);
            for c in &n.children {{ nxt.push(c); }}
        }}
        res.push(level);
        q = nxt;
    }}
    res
}}
fn main() {{
    let mut root = Node::new(1);
    let mut c3 = Node::new(3);
    c3.children = vec![Node::new(5), Node::new(6)];
    root.children = vec![c3, Node::new(2), Node::new(4)];
    assert_eq!(level_order(Some(&root)), vec![vec![1], vec![3, 2, 4], vec![5, 6]]);
    assert!(level_order(None).is_empty());
    println!("PASS");
}}
''',
"lua": '''{H}
local function new_node(v) return {{val = v, children = {{}}} end
local function level_order(root)
    if not root then return {{}} end
    local res = {{}}
    local q = {{root}}
    while #q > 0 do
        local level = {{}}
        local nxt = {{}}
        for i = 1, #q do
            local n = q[i]
            level[#level + 1] = n.val
            for _, c in ipairs(n.children) do nxt[#nxt + 1] = c end
        end
        res[#res + 1] = level
        q = nxt
    end
    return res
end
local root = new_node(1)
local c3 = new_node(3)
c3.children = {{new_node(5), new_node(6)}}
root.children = {{c3, new_node(2), new_node(4)}}
local a = level_order(root)
assert(#a == 3 and a[1][1] == 1 and a[2][1] == 3 and a[2][2] == 2 and a[2][3] == 4 and a[3][1] == 5 and a[3][2] == 6)
assert(#level_order(nil) == 0)
print("PASS")
''',
"c": '''{H}
typedef struct NNode {{ int val; struct NNode *children[16]; int nch; }} NNode;
static NNode *nnew(int v) {{
    NNode *n = calloc(1, sizeof(NNode));
    n->val = v;
    return n;
}}
static int level_order(NNode *root, int out[][64], int sizes[]) {{
    if (!root) return 0;
    NNode *q[256];
    int head = 0, tail = 0, nl = 0;
    q[tail++] = root;
    while (head < tail) {{
        int size = tail - head, cnt = 0;
        for (int i = 0; i < size; i++) {{
            NNode *n = q[head++];
            out[nl][cnt++] = n->val;
            for (int k = 0; k < n->nch; k++) q[tail++] = n->children[k];
        }}
        sizes[nl++] = cnt;
    }}
    return nl;
}}
int main(void) {{
    NNode *root = nnew(1), *c3 = nnew(3);
    c3->children[c3->nch++] = nnew(5);
    c3->children[c3->nch++] = nnew(6);
    root->children[root->nch++] = c3;
    root->children[root->nch++] = nnew(2);
    root->children[root->nch++] = nnew(4);
    int out[64][64], sizes[64];
    int n = level_order(root, out, sizes);
    if (n != 3 || sizes[0] != 1 || sizes[1] != 3 || sizes[2] != 2) {{ printf("FAIL shape\\n"); return 1; }}
    if (out[0][0] != 1 || out[1][0] != 3 || out[1][1] != 2 || out[1][2] != 4 || out[2][0] != 5 || out[2][1] != 6) {{ printf("FAIL vals\\n"); return 1; }}
    if (level_order(NULL, out, sizes) != 0) {{ printf("FAIL nil\\n"); return 1; }}
    printf("PASS\\n");
    return 0;
}}
''',
"cpp": '''{H}
struct NNode {{
    int val;
    std::vector<NNode *> children;
    explicit NNode(int v) : val(v) {{}}
}};
static std::vector<std::vector<int>> levelOrder(NNode *root) {{
    std::vector<std::vector<int>> res;
    if (!root) return res;
    std::queue<NNode *> q;
    q.push(root);
    while (!q.empty()) {{
        int size = static_cast<int>(q.size());
        std::vector<int> level;
        for (int i = 0; i < size; ++i) {{
            auto *n = q.front();
            q.pop();
            level.push_back(n->val);
            for (auto *c : n->children) q.push(c);
        }}
        res.push_back(std::move(level));
    }}
    return res;
}}
int main() {{
    auto *root = new NNode(1);
    auto *c3 = new NNode(3);
    c3->children = {{new NNode(5), new NNode(6)}};
    root->children = {{c3, new NNode(2), new NNode(4)}};
    assert((levelOrder(root) == std::vector<std::vector<int>>{{{1}, {3, 2, 4}, {5, 6}}}));
    assert(levelOrder(nullptr).empty());
    std::cout << "PASS" << std::endl;
    return 0;
}}
''',
"r": '''{H}
new_node <- function(v) {{ e <- new.env(parent = emptyenv()); e$val <- v; e$children <- list(); class(e) <- "NNode"; e }}
level_order <- function(root) {{
  if (is.null(root)) return(list())
  res <- list()
  q <- list(root)
  while (length(q) > 0) {{
    level <- integer(0); nxt <- list()
    for (n in q) {{
      level[[length(level) + 1L]] <- n$val
      for (c in n$children) nxt[[length(nxt) + 1L]] <- c
    }}
    res[[length(res) + 1L]] <- level
    q <- nxt
  }}
  res
}}
root <- new_node(1L)
c3 <- new_node(3L)
c3$children <- list(new_node(5L), new_node(6L))
root$children <- list(c3, new_node(2L), new_node(4L))
got <- level_order(root)
stopifnot(identical(got, list(1L, c(3L, 2L, 4L), c(5L, 6L))))
stopifnot(length(level_order(NULL)) == 0L)
cat("PASS\\n")
''',
"zig": '''{H}
const NNode = struct {{ val: i32, children: std.ArrayList(*NNode) }};
fn nnew(v: i32, alloc: std.mem.Allocator) *NNode {{
    const n = alloc.create(NNode) catch unreachable;
    n.* = .{{ .val = v, .children = std.ArrayList(*NNode).init(alloc) }};
    return n;
}}
fn levelOrder(root: ?*NNode, alloc: std.mem.Allocator) std.ArrayList(std.ArrayList(i32)) {{
    var res = std.ArrayList(std.ArrayList(i32)).init(alloc);
    const r = root orelse return res;
    var q = std.ArrayList(*NNode).init(alloc);
    q.append(r) catch unreachable;
    var head: usize = 0;
    while (head < q.items.len) {{
        const size = q.items.len - head;
        var level = std.ArrayList(i32).init(alloc);
        for (0..size) |_| {{
            const n = q.items[head];
            head += 1;
            level.append(n.val) catch unreachable;
            for (n.children.items) |c| q.append(c) catch unreachable;
        }}
        res.append(level) catch unreachable;
    }}
    return res;
}}
pub fn main() !void {{
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();
    const alloc = arena.allocator();
    const root = nnew(1, alloc);
    const c3 = nnew(3, alloc);
    c3.children.append(nnew(5, alloc)) catch unreachable;
    c3.children.append(nnew(6, alloc)) catch unreachable;
    root.children.append(c3) catch unreachable;
    root.children.append(nnew(2, alloc)) catch unreachable;
    root.children.append(nnew(4, alloc)) catch unreachable;
    const res = levelOrder(root, alloc);
    if (res.items.len != 3) return error.TestFailed;
    if (res.items[0].items[0] != 1) return error.TestFailed;
    if (res.items[1].items[0] != 3 or res.items[1].items[1] != 2 or res.items[1].items[2] != 4) return error.TestFailed;
    if (res.items[2].items[0] != 5 or res.items[2].items[1] != 6) return error.TestFailed;
    if (levelOrder(null, alloc).items.len != 0) return error.TestFailed;
    std.debug.print("PASS\\n", .{{}});
}}
''',
"dart": '''{H}
class NNode {
  final int val;
  final List<NNode> children = [];
  NNode(this.val);
}
List<List<int>> levelOrder(NNode? root) {
  if (root == null) return [];
  final res = <List<int>>[];
  var q = <NNode>[root];
  while (q.isNotEmpty) {
    final level = <int>[];
    final nxt = <NNode>[];
    for (final n in q) {
      level.add(n.val);
      nxt.addAll(n.children);
    }
    res.add(level);
    q = nxt;
  }
  return res;
}
void main() {
  final root = NNode(1);
  final c3 = NNode(3);
  c3.children.addAll([NNode(5), NNode(6)]);
  root.children.addAll([c3, NNode(2), NNode(4)]);
  final a = levelOrder(root);
  if (a.length != 3 || a[0][0] != 1) throw StateError('c1');
  if (a[1].length != 3 || a[1][0] != 3 || a[1][1] != 2 || a[1][2] != 4) throw StateError('c2');
  if (a[2].length != 2 || a[2][0] != 5 || a[2][1] != 6) throw StateError('c3');
  if (levelOrder(null).isNotEmpty) throw StateError('c4');
  print('PASS');
}
''',
}

PROBS = [
    ("lc_98_验证二叉搜索树", A98, "LeetCode 98. 验证二叉搜索树", False),
    ("lc_236_二叉树的最近公共祖先", A236, "LeetCode 236. 二叉树的最近公共祖先", False),
    ("lc_572_另一棵树的子树", A572, "LeetCode 572. 另一棵树的子树", True),
    ("lc_199_二叉树的右视图", A199, "LeetCode 199. 二叉树的右视图", False),
    ("lc_429_n_叉树的层序遍历", A429, "LeetCode 429. N叉树的层序遍历", False),
]
count = 0
for prob, algo, title, use_same in PROBS:
    bid = B[prob.split("_")[1]]
    ts_dir = f"/Users/Wang/Code/github/web-x-blog/work/blog/courses/21.dsa/ts/tree/{prob}"
    sols = sorted(f[:-3] for f in os.listdir(ts_dir) if f.startswith("solution_") and f.endswith(".ts"))
    for lang, tmpl in algo.items():
        ext = EXT[lang]
        for sol in sols:
            n = sol.replace("solution_", "").split("_")[0]
            head = head_comment(lang, bid, f"{title} — {LANGNAME[lang]} 版（方案{n}）")
            body = tmpl.replace("{H}", TREE_H[lang]).replace("{S}", SAME[lang] if use_same else "").replace("{{", "{").replace("}}", "}")
            emit(lang, f"tree/{prob}/{sol}.{ext}", head + "\n" + body)
            count += 1
print(f"emitted {count} files")
