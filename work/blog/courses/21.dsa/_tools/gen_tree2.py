#!/usr/bin/env python3
# gen_tree2.py — tree 第二批：lc_101/lc_111/lc_222/lc_404/lc_617 × 7语言
import sys, os; sys.path.insert(0, "/Users/Wang/Code/github/web-x-blog/work/blog/courses/21.dsa/_tools")
from langlib import emit, TREE_H, head_comment, EXT

B = {"101": "135586474", "111": "135759583", "222": "136210437", "404": "136391511", "617": "136726698"}
LANGNAME = {"rust": "Rust", "lua": "Lua", "c": "C", "cpp": "C++", "r": "R", "zig": "Zig", "dart": "Dart"}

A101 = {
"rust": '''{H}
fn is_symmetric(root: Option<Rc<RefCell<TreeNode>>>) -> bool {{
    fn is_mirror(l: Option<&Rc<RefCell<TreeNode>>>, r: Option<&Rc<RefCell<TreeNode>>>) -> bool {{
        match (l, r) {{
            (None, None) => true,
            (Some(a), Some(b)) => {{
                let (a, b) = (a.borrow(), b.borrow());
                a.val == b.val && is_mirror(a.left.as_ref(), b.right.as_ref()) && is_mirror(a.right.as_ref(), b.left.as_ref())
            }}
            _ => false,
        }}
    }}
    let node = match root {{ Some(x) => x, None => return true }};
    let nb = node.borrow();
    is_mirror(nb.left.as_ref(), nb.right.as_ref())
}}
fn main() {{
    assert!(is_symmetric(None));
    assert!(is_symmetric(build_tree(&[Some(1), Some(2), Some(2), Some(3), Some(4), Some(4), Some(3)])));
    assert!(!is_symmetric(build_tree(&[Some(1), Some(2), Some(2), None, Some(3), None, Some(3)])));
    println!("PASS");
}}
''',
"lua": '''{H}
local function is_symmetric(root)
    local function is_mirror(l, r)
        if not l and not r then return true end
        if not l or not r then return false end
        return l.val == r.val and is_mirror(l.left, r.right) and is_mirror(r.left, l.right)
    end
    if not root then return true end
    return is_mirror(root.left, root.right)
end
assert(is_symmetric(nil) == true)
assert(is_symmetric(build_tree({{1,2,2,3,4,4,3}})) == true)
assert(is_symmetric(build_tree({{1,2,2,"null",3,"null",3}})) == false)
print("PASS")
''',
"c": '''{H}
static int is_mirror(const TreeNode *l, const TreeNode *r) {{
    if (!l && !r) return 1;
    if (!l || !r || l->val != r->val) return 0;
    return is_mirror(l->left, r->right) && is_mirror(r->left, l->right);
}}
static int is_symmetric(const TreeNode *root) {{
    if (!root) return 1;
    return is_mirror(root->left, root->right);
}}
int main(void) {{
    int v1[] = {{1,2,2,3,4,4,3}};
    int v2[] = {{1,2,2,INT_MIN_SN,3,INT_MIN_SN,3}};
    if (!is_symmetric(NULL)) {{ printf("FAIL 0\\n"); return 1; }}
    if (!is_symmetric(build_tree(v1, 7))) {{ printf("FAIL 1\\n"); return 1; }}
    if (is_symmetric(build_tree(v2, 7))) {{ printf("FAIL 2\\n"); return 1; }}
    printf("PASS\\n");
    return 0;
}}
''',
"cpp": '''{H}
static bool isMirror(const TreeNode *l, const TreeNode *r) {{
    if (!l && !r) return true;
    if (!l || !r || l->val != r->val) return false;
    return isMirror(l->left, r->right) && isMirror(r->left, l->right);
}}
static bool isSymmetric(const TreeNode *root) {{
    if (!root) return true;
    return isMirror(root->left, root->right);
}}
int main() {{
    assert(isSymmetric(nullptr));
    assert(isSymmetric(build_tree({{1, 2, 2, 3, 4, 4, 3}})));
    assert(!isSymmetric(build_tree({{1, 2, 2, std::nullopt, 3, std::nullopt, 3}})));
    std::cout << "PASS" << std::endl;
    return 0;
}}
''',
"r": '''{H}
is_mirror <- function(l, r) {{
  if (is.null(l) && is.null(r)) return(TRUE)
  if (is.null(l) || is.null(r) || l$val != r$val) return(FALSE)
  is_mirror(l$left, r$right) && is_mirror(r$left, l$right)
}}
is_symmetric <- function(root) {{
  if (is.null(root)) return(TRUE)
  is_mirror(root$left, root$right)
}}
stopifnot(is_symmetric(NULL))
stopifnot(is_symmetric(build_tree(list(1L, 2L, 2L, 3L, 4L, 4L, 3L))))
stopifnot(!is_symmetric(build_tree(list(1L, 2L, 2L, NA, 3L, NA, 3L))))
cat("PASS\\n")
''',
"zig": '''{H}
fn isMirror(l: ?*const TreeNode, r: ?*const TreeNode) bool {{
    if (l == null and r == null) return true;
    if (l == null or r == null) return false;
    const a = l.?;
    const b = r.?;
    return a.val == b.val and isMirror(a.left, b.right) and isMirror(b.left, a.right);
}}
fn isSymmetric(root: ?*TreeNode) bool {{
    const node = root orelse return true;
    return isMirror(node.left, node.right);
}}
pub fn main() !void {{
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();
    const alloc = arena.allocator();
    if (!isSymmetric(null)) return error.TestFailed;
    if (!isSymmetric(try buildTree(alloc, &[_]i32{{ 1, 2, 2, 3, 4, 4, 3 }}))) return error.TestFailed;
    if (isSymmetric(try buildTree(alloc, &[_]i32{{ 1, 2, 2, -1, 3, -1, 3 }}))) return error.TestFailed;
    std.debug.print("PASS\\n", .{{}});
}}
''',
"dart": '''{H}
bool isSymmetric(TreeNode? root) {{
  bool isMirror(TreeNode? l, TreeNode? r) {{
    if (l == null && r == null) return true;
    if (l == null || r == null || l.val != r.val) return false;
    return isMirror(l.left, r.right) && isMirror(r.left, l.right);
  }}
  if (root == null) return true;
  return isMirror(root.left, root.right);
}}
void main() {{
  if (!isSymmetric(null)) throw StateError('c0');
  if (!isSymmetric(buildTree([1, 2, 2, 3, 4, 4, 3]))) throw StateError('c1');
  if (isSymmetric(buildTree([1, 2, 2, null, 3, null, 3]))) throw StateError('c2');
  print('PASS');
}}
''',
}

A111 = {
"rust": '''{H}
fn min_depth(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {{
    let root = match root {{ Some(x) => x, None => return 0 }};
    let mut q: Vec<(Rc<RefCell<TreeNode>>, i32)> = vec![(root, 1)];
    let mut head = 0;
    while head < q.len() {{
        let (node, l) = q[head].clone();
        head += 1;
        let nb = node.borrow();
        if nb.left.is_none() && nb.right.is_none() {{
            return l;
        }}
        if let Some(c) = nb.left.clone() {{ q.push((c, l + 1)); }}
        if let Some(c) = nb.right.clone() {{ q.push((c, l + 1)); }}
    }}
    0
}}
fn main() {{
    assert_eq!(min_depth(build_tree(&[Some(3), Some(9), Some(20), None, None, Some(15), Some(7)])), 2);
    assert_eq!(min_depth(build_tree(&[Some(2), None, Some(3), None, Some(4), None, Some(5), None, Some(6)])), 5);
    assert_eq!(min_depth(None), 0);
    assert_eq!(min_depth(build_tree(&[Some(1)])), 1);
    assert_eq!(min_depth(build_tree(&[Some(1), Some(2)])), 2);
    println!("PASS");
}}
''',
"lua": '''{H}
local function min_depth(root)
    if not root then return 0 end
    local q = {{{root, 1}}}
    local head = 1
    while head <= #q do
        local n, l = table.unpack(q[head])
        head = head + 1
        if not n.left and not n.right then return l end
        if n.left then q[#q + 1] = {{n.left, l + 1}} end
        if n.right then q[#q + 1] = {{n.right, l + 1}} end
    end
    return 0
end
assert(min_depth(build_tree({{3, 9, 20, "null", "null", 15, 7}})) == 2)
assert(min_depth(build_tree({{2, "null", 3, "null", 4, "null", 5, "null", 6}})) == 5)
assert(min_depth(nil) == 0)
assert(min_depth(build_tree({{1}})) == 1)
assert(min_depth(build_tree({{1, 2}})) == 2)
print("PASS")
''',
"c": '''{H}
typedef struct {{ TreeNode *n; int l; }} QN;
static int min_depth(TreeNode *root) {{
    if (!root) return 0;
    QN q[4096];
    int head = 0, tail = 0;
    q[tail].n = root; q[tail].l = 1; tail++;
    while (head < tail) {{
        TreeNode *n = q[head].n; int l = q[head].l; head++;
        if (!n->left && !n->right) return l;
        if (n->left) {{ q[tail].n = n->left; q[tail].l = l + 1; tail++; }}
        if (n->right) {{ q[tail].n = n->right; q[tail].l = l + 1; tail++; }}
    }}
    return 0;
}}
int main(void) {{
    int v1[] = {{3,9,20,INT_MIN_SN,INT_MIN_SN,15,7}};
    int v2[] = {{2,INT_MIN_SN,3,INT_MIN_SN,4,INT_MIN_SN,5,INT_MIN_SN,6}};
    if (min_depth(build_tree(v1, 7)) != 2) {{ printf("FAIL 1\\n"); return 1; }}
    if (min_depth(build_tree(v2, 9)) != 5) {{ printf("FAIL 2\\n"); return 1; }}
    if (min_depth(NULL) != 0) {{ printf("FAIL 3\\n"); return 1; }}
    int v4[] = {{1}}; if (min_depth(build_tree(v4, 1)) != 1) {{ printf("FAIL 4\\n"); return 1; }}
    int v5[] = {{1,2}}; if (min_depth(build_tree(v5, 2)) != 2) {{ printf("FAIL 5\\n"); return 1; }}
    printf("PASS\\n");
    return 0;
}}
''',
"cpp": '''{H}
static int minDepth(TreeNode *root) {{
    if (!root) return 0;
    std::queue<std::pair<TreeNode *, int>> q;
    q.push({{root, 1}});
    while (!q.empty()) {{
        auto [n, l] = q.front();
        q.pop();
        if (!n->left && !n->right) return l;
        if (n->left) q.push({{n->left, l + 1}});
        if (n->right) q.push({{n->right, l + 1}});
    }}
    return 0;
}}
int main() {{
    assert(minDepth(build_tree({{3, 9, 20, std::nullopt, std::nullopt, 15, 7}})) == 2);
    assert(minDepth(build_tree({{2, std::nullopt, 3, std::nullopt, 4, std::nullopt, 5, std::nullopt, 6}})) == 5);
    assert(minDepth(nullptr) == 0);
    assert(minDepth(build_tree({{1}})) == 1);
    assert(minDepth(build_tree({{1, 2}})) == 2);
    std::cout << "PASS" << std::endl;
    return 0;
}}
''',
"r": '''{H}
min_depth <- function(root) {{
  if (is.null(root)) return(0L)
  q <- list(list(root, 1L))
  head <- 1L
  while (head <= length(q)) {{
    n <- q[[head]][[1]]; l <- q[[head]][[2]]
    head <- head + 1L
    if (is.null(n$left) && is.null(n$right)) return(l)
    if (!is.null(n$left)) q[[length(q) + 1L]] <- list(n$left, l + 1L)
    if (!is.null(n$right)) q[[length(q) + 1L]] <- list(n$right, l + 1L)
  }}
  0L
}}
stopifnot(min_depth(build_tree(list(3L, 9L, 20L, NA, NA, 15L, 7L))) == 2L)
stopifnot(min_depth(build_tree(list(2L, NA, 3L, NA, 4L, NA, 5L, NA, 6L))) == 5L)
stopifnot(min_depth(NULL) == 0L)
stopifnot(min_depth(build_tree(list(1L))) == 1L)
stopifnot(min_depth(build_tree(list(1L, 2L))) == 2L)
cat("PASS\\n")
''',
"zig": '''{H}
fn minDepth(root: ?*TreeNode) i32 {{
    const r = root orelse return 0;
    const QN = struct {{ n: *TreeNode, l: i32 }};
    var q = std.ArrayList(QN).init(std.heap.page_allocator);
    defer q.deinit();
    q.append(.{{ .n = r, .l = 1 }}) catch unreachable;
    var head: usize = 0;
    while (head < q.items.len) {{
        const it = q.items[head];
        head += 1;
        if (it.n.left == null and it.n.right == null) return it.l;
        if (it.n.left) |c| q.append(.{{ .n = c, .l = it.l + 1 }}) catch unreachable;
        if (it.n.right) |c| q.append(.{{ .n = c, .l = it.l + 1 }}) catch unreachable;
    }}
    return 0;
}}
pub fn main() !void {{
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();
    const alloc = arena.allocator();
    if (minDepth(try buildTree(alloc, &[_]i32{{ 3, 9, 20, -1, -1, 15, 7 }})) != 2) return error.TestFailed;
    if (minDepth(try buildTree(alloc, &[_]i32{{ 2, -1, 3, -1, 4, -1, 5, -1, 6 }})) != 5) return error.TestFailed;
    if (minDepth(null) != 0) return error.TestFailed;
    if (minDepth(try buildTree(alloc, &[_]i32{{1}})) != 1) return error.TestFailed;
    if (minDepth(try buildTree(alloc, &[_]i32{{ 1, 2 }})) != 2) return error.TestFailed;
    std.debug.print("PASS\\n", .{{}});
}}
''',
"dart": '''{H}
int minDepth(TreeNode? root) {{
  if (root == null) return 0;
  final q = <List<dynamic>>[[root, 1]];
  var head = 0;
  while (head < q.length) {{
    final n = q[head][0] as TreeNode;
    final l = q[head][1] as int;
    head++;
    if (n.left == null && n.right == null) return l;
    if (n.left != null) q.add([n.left!, l + 1]);
    if (n.right != null) q.add([n.right!, l + 1]);
  }}
  return 0;
}}
void main() {{
  if (minDepth(buildTree([3, 9, 20, null, null, 15, 7])) != 2) throw StateError('c1');
  if (minDepth(buildTree([2, null, 3, null, 4, null, 5, null, 6])) != 5) throw StateError('c2');
  if (minDepth(null) != 0) throw StateError('c3');
  if (minDepth(buildTree([1])) != 1) throw StateError('c4');
  if (minDepth(buildTree([1, 2])) != 2) throw StateError('c5');
  print('PASS');
}}
''',
}

A222 = {
"rust": '''{H}
fn count_nodes(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {{
    let node = match root {{ Some(x) => x, None => return 0 }};
    let mut lh = 0;
    let mut r = node.borrow().left.clone();
    while let Some(x) = r {{ lh += 1; r = x.borrow().left.clone(); }}
    let mut rh = 0;
    r = node.borrow().right.clone();
    while let Some(x) = r {{ rh += 1; r = x.borrow().right.clone(); }}
    if lh == rh {{ return (1 << (lh + 1)) - 1; }}
    let nb = node.borrow();
    1 + count_nodes(nb.left.clone()) + count_nodes(nb.right.clone())
}}
fn main() {{
    assert_eq!(count_nodes(build_tree(&[Some(1), Some(2), Some(3), Some(4), Some(5), Some(6)])), 6);
    assert_eq!(count_nodes(None), 0);
    assert_eq!(count_nodes(build_tree(&[Some(1)])), 1);
    assert_eq!(count_nodes(build_tree(&[Some(1), Some(2), Some(3), Some(4), Some(5), Some(6), Some(7), Some(8)])), 8);
    println!("PASS");
}}
''',
"lua": '''{H}
local function count_nodes(root)
    if not root then return 0 end
    local lh, r = 0, root
    while r do lh = lh + 1; r = r.left end
    local rh = 0; r = root
    while r do rh = rh + 1; r = r.right end
    if lh == rh then return (1 << lh) - 1 end
    return 1 + count_nodes(root.left) + count_nodes(root.right)
end
assert(count_nodes(build_tree({{1,2,3,4,5,6}})) == 6)
assert(count_nodes(nil) == 0)
assert(count_nodes(build_tree({{1}})) == 1)
assert(count_nodes(build_tree({{1,2,3,4,5,6,7,8}})) == 8)
print("PASS")
''',
"c": '''{H}
static int count_nodes(TreeNode *root) {{
    if (!root) return 0;
    int lh = 0; TreeNode *r = root;
    while (r) {{ lh++; r = r->left; }}
    int rh = 0; r = root;
    while (r) {{ rh++; r = r->right; }}
    if (lh == rh) return (1 << lh) - 1;
    return 1 + count_nodes(root->left) + count_nodes(root->right);
}}
int main(void) {{
    int v1[] = {{1,2,3,4,5,6}};
    int v4[] = {{1,2,3,4,5,6,7,8}};
    if (count_nodes(build_tree(v1, 6)) != 6) {{ printf("FAIL 1\\n"); return 1; }}
    if (count_nodes(NULL) != 0) {{ printf("FAIL 2\\n"); return 1; }}
    int v3[] = {{1}};
    if (count_nodes(build_tree(v3, 1)) != 1) {{ printf("FAIL 3\\n"); return 1; }}
    if (count_nodes(build_tree(v4, 8)) != 8) {{ printf("FAIL 4\\n"); return 1; }}
    printf("PASS\\n");
    return 0;
}}
''',
"cpp": '''{H}
static int countNodes(TreeNode *root) {{
    if (!root) return 0;
    int lh = 0;
    for (TreeNode *r = root; r; r = r->left) ++lh;
    int rh = 0;
    for (TreeNode *r = root; r; r = r->right) ++rh;
    if (lh == rh) return (1 << lh) - 1;
    return 1 + countNodes(root->left) + countNodes(root->right);
}}
int main() {{
    assert(countNodes(build_tree({{1, 2, 3, 4, 5, 6}})) == 6);
    assert(countNodes(nullptr) == 0);
    assert(countNodes(build_tree({{1}})) == 1);
    assert(countNodes(build_tree({{1, 2, 3, 4, 5, 6, 7, 8}})) == 8);
    std::cout << "PASS" << std::endl;
    return 0;
}}
''',
"r": '''{H}
count_nodes <- function(root) {{
  if (is.null(root)) return(0L)
  lh <- 0L; r <- root
  while (!is.null(r)) {{ lh <- lh + 1L; r <- r$left }}
  rh <- 0L; r <- root
  while (!is.null(r)) {{ rh <- rh + 1L; r <- r$right }}
  if (lh == rh) return((2^lh) - 1L)
  1L + count_nodes(root$left) + count_nodes(root$right)
}}
stopifnot(count_nodes(build_tree(list(1L, 2L, 3L, 4L, 5L, 6L))) == 6L)
stopifnot(count_nodes(NULL) == 0L)
stopifnot(count_nodes(build_tree(list(1L))) == 1L)
stopifnot(count_nodes(build_tree(list(1L, 2L, 3L, 4L, 5L, 6L, 7L, 8L))) == 8L)
cat("PASS\\n")
''',
"zig": '''{H}
fn countNodes(root: ?*TreeNode) i32 {{
    const node = root orelse return 0;
    var lh: i32 = 0;
    var r: ?*TreeNode = node.left;
    while (r) |x| {{ lh += 1; r = x.left; }}
    var rh: i32 = 0;
    r = node.right;
    while (r) |x| {{ rh += 1; r = x.right; }}
    if (lh == rh) return (@as(i32, 1) << @intCast(lh + 1)) - 1;
    return 1 + countNodes(node.left) + countNodes(node.right);
}}
pub fn main() !void {{
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();
    const alloc = arena.allocator();
    if (countNodes(try buildTree(alloc, &[_]i32{{ 1, 2, 3, 4, 5, 6 }})) != 6) return error.TestFailed;
    if (countNodes(null) != 0) return error.TestFailed;
    if (countNodes(try buildTree(alloc, &[_]i32{{1}})) != 1) return error.TestFailed;
    if (countNodes(try buildTree(alloc, &[_]i32{{ 1, 2, 3, 4, 5, 6, 7, 8 }})) != 8) return error.TestFailed;
    std.debug.print("PASS\\n", .{{}});
}}
''',
"dart": '''{H}
int countNodes(TreeNode? root) {{
  if (root == null) return 0;
  var lh = 0;
  var r = root.left;
  while (r != null) {{
    lh++;
    r = r.left;
  }}
  var rh = 0;
  r = root.right;
  while (r != null) {{
    rh++;
    r = r.right;
  }}
  if (lh == rh) return (1 << (lh + 1)) - 1;
  return 1 + countNodes(root.left) + countNodes(root.right);
}}
void main() {{
  if (countNodes(buildTree([1, 2, 3, 4, 5, 6])) != 6) throw StateError('c1');
  if (countNodes(null) != 0) throw StateError('c2');
  if (countNodes(buildTree([1])) != 1) throw StateError('c3');
  if (countNodes(buildTree([1, 2, 3, 4, 5, 6, 7, 8])) != 8) throw StateError('c4');
  print('PASS');
}}
''',
}

A404 = {
"rust": '''{H}
fn is_leaf(n: Option<&Rc<RefCell<TreeNode>>>) -> bool {{
    match n {{
        Some(x) => {{ let b = x.borrow(); b.left.is_none() && b.right.is_none() }}
        None => false,
    }}
}}
fn sum_of_left_leaves(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {{
    let root = match root {{ Some(x) => x, None => return 0 }};
    let mut total = 0;
    let mut stack = vec![root];
    while let Some(node) = stack.pop() {{
        let nb = node.borrow();
        if let Some(l) = nb.left.as_ref() {{
            if is_leaf(Some(l)) {{
                total += l.borrow().val;
            }} else {{
                stack.push(l.clone());
            }}
        }}
        if let Some(r) = nb.right.as_ref() {{
            stack.push(r.clone());
        }}
    }}
    total
}}
fn main() {{
    assert_eq!(sum_of_left_leaves(build_tree(&[Some(3), Some(9), Some(20), None, None, Some(15), Some(7)])), 24);
    assert_eq!(sum_of_left_leaves(None), 0);
    assert_eq!(sum_of_left_leaves(build_tree(&[Some(1), Some(2), Some(3), Some(4), Some(5)])), 4);
    println!("PASS");
}}
''',
"lua": '''{H}
local function is_leaf(n)
    return n and not n.left and not n.right
end
local function sum_of_left_leaves(root)
    if not root then return 0 end
    local total = 0
    local stack = {{root}}
    while #stack > 0 do
        local node = table.remove(stack)
        if node.left then
            if is_leaf(node.left) then total = total + node.left.val
            else stack[#stack + 1] = node.left end
        end
        if node.right then stack[#stack + 1] = node.right end
    end
    return total
end
assert(sum_of_left_leaves(build_tree({{3, 9, 20, "null", "null", 15, 7}})) == 24)
assert(sum_of_left_leaves(nil) == 0)
assert(sum_of_left_leaves(build_tree({{1, 2, 3, 4, 5}})) == 4)
print("PASS")
''',
"c": '''{H}
static int is_leaf(const TreeNode *n) {{ return n && !n->left && !n->right; }}
static int sum_of_left_leaves(TreeNode *root) {{
    if (!root) return 0;
    int total = 0;
    TreeNode *stack[256];
    int top = 0;
    stack[top++] = root;
    while (top > 0) {{
        TreeNode *node = stack[--top];
        if (node->left) {{
            if (is_leaf(node->left)) total += node->left->val;
            else stack[top++] = node->left;
        }}
        if (node->right) stack[top++] = node->right;
    }}
    return total;
}}
int main(void) {{
    int v1[] = {{3,9,20,INT_MIN_SN,INT_MIN_SN,15,7}};
    int v3[] = {{1,2,3,4,5}};
    if (sum_of_left_leaves(build_tree(v1, 7)) != 24) {{ printf("FAIL 1\\n"); return 1; }}
    if (sum_of_left_leaves(NULL) != 0) {{ printf("FAIL 2\\n"); return 1; }}
    if (sum_of_left_leaves(build_tree(v3, 5)) != 4) {{ printf("FAIL 3\\n"); return 1; }}
    printf("PASS\\n");
    return 0;
}}
''',
"cpp": '''{H}
static bool isLeaf(const TreeNode *n) {{ return n && !n->left && !n->right; }}
static int sumOfLeftLeaves(TreeNode *root) {{
    if (!root) return 0;
    int total = 0;
    std::vector<TreeNode *> stack{{root}};
    while (!stack.empty()) {{
        auto *node = stack.back();
        stack.pop_back();
        if (node->left) {{
            if (isLeaf(node->left)) total += node->left->val;
            else stack.push_back(node->left);
        }}
        if (node->right) stack.push_back(node->right);
    }}
    return total;
}}
int main() {{
    assert(sumOfLeftLeaves(build_tree({{3, 9, 20, std::nullopt, std::nullopt, 15, 7}})) == 24);
    assert(sumOfLeftLeaves(nullptr) == 0);
    assert(sumOfLeftLeaves(build_tree({{1, 2, 3, 4, 5}})) == 4);
    std::cout << "PASS" << std::endl;
    return 0;
}}
''',
"r": '''{H}
is_leaf <- function(n) !is.null(n) && is.null(n$left) && is.null(n$right)
sum_of_left_leaves <- function(root) {{
  if (is.null(root)) return(0L)
  total <- 0L
  stack <- list(root)
  while (length(stack) > 0) {{
    node <- stack[[length(stack)]]
    stack[[length(stack)]] <- NULL
    if (!is.null(node$left)) {{
      if (is_leaf(node$left)) total <- total + node$left$val
      else stack[[length(stack) + 1L]] <- node$left
    }}
    if (!is.null(node$right)) stack[[length(stack) + 1L]] <- node$right
  }}
  total
}}
stopifnot(sum_of_left_leaves(build_tree(list(3L, 9L, 20L, NA, NA, 15L, 7L))) == 24L)
stopifnot(sum_of_left_leaves(NULL) == 0L)
stopifnot(sum_of_left_leaves(build_tree(list(1L, 2L, 3L, 4L, 5L))) == 4L)
cat("PASS\\n")
''',
"zig": '''{H}
fn isLeaf(n: ?*const TreeNode) bool {{
    const node = n orelse return false;
    return node.left == null and node.right == null;
}}
fn sumOfLeftLeaves(root: ?*TreeNode) i32 {{
    const r = root orelse return 0;
    var total: i32 = 0;
    var stack = std.ArrayList(*TreeNode).init(std.heap.page_allocator);
    defer stack.deinit();
    stack.append(r) catch unreachable;
    while (stack.items.len > 0) {{
        const node = stack.pop().?;
        if (node.left) |l| {{
            if (isLeaf(l)) total += l.val else stack.append(l) catch unreachable;
        }}
        if (node.right) |rt| stack.append(rt) catch unreachable;
    }}
    return total;
}}
pub fn main() !void {{
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();
    const alloc = arena.allocator();
    if (sumOfLeftLeaves(try buildTree(alloc, &[_]i32{{ 3, 9, 20, -1, -1, 15, 7 }})) != 24) return error.TestFailed;
    if (sumOfLeftLeaves(null) != 0) return error.TestFailed;
    if (sumOfLeftLeaves(try buildTree(alloc, &[_]i32{{ 1, 2, 3, 4, 5 }})) != 4) return error.TestFailed;
    std.debug.print("PASS\\n", .{{}});
}}
''',
"dart": '''{H}
bool isLeaf(TreeNode? n) => n != null && n.left == null && n.right == null;
int sumOfLeftLeaves(TreeNode? root) {{
  if (root == null) return 0;
  var total = 0;
  final stack = <TreeNode>[root];
  while (stack.isNotEmpty) {{
    final node = stack.removeLast();
    if (node.left != null) {{
      if (isLeaf(node.left)) {{
        total += node.left!.val;
      }} else {{
        stack.add(node.left!);
      }}
    }}
    if (node.right != null) stack.add(node.right!);
  }}
  return total;
}}
void main() {{
  if (sumOfLeftLeaves(buildTree([3, 9, 20, null, null, 15, 7])) != 24) throw StateError('c1');
  if (sumOfLeftLeaves(null) != 0) throw StateError('c2');
  if (sumOfLeftLeaves(buildTree([1, 2, 3, 4, 5])) != 4) throw StateError('c3');
  print('PASS');
}}
''',
}

A617 = {
"rust": '''{H}
fn same_tree(p: Option<&Rc<RefCell<TreeNode>>>, q: Option<&Rc<RefCell<TreeNode>>>) -> bool {{
    match (p, q) {{
        (None, None) => true,
        (Some(a), Some(b)) => {{
            let (a, b) = (a.borrow(), b.borrow());
            a.val == b.val && same_tree(a.left.as_ref(), b.left.as_ref()) && same_tree(a.right.as_ref(), b.right.as_ref())
        }}
        _ => false,
    }}
}}
fn merge_trees(t1: Option<Rc<RefCell<TreeNode>>>, t2: Option<Rc<RefCell<TreeNode>>>) -> Option<Rc<RefCell<TreeNode>>> {{
    let n1 = match t1 {{ Some(x) => x, None => return t2 }};
    if let Some(n2) = t2 {{
        n1.borrow_mut().val += n2.borrow().val;
        let (l, r) = (n2.borrow().left.clone(), n2.borrow().right.clone());
        let (l1, r1) = (n1.borrow().left.clone(), n1.borrow().right.clone());
        {{ let mut b = n1.borrow_mut(); b.left = merge_trees(l1, l); b.right = merge_trees(r1, r); }}
    }}
    Some(n1)
}}
fn main() {{
    let m = |a: &[Option<i32>], b: &[Option<i32>], w: &[Option<i32>]| {{
        let got = merge_trees(build_tree(a), build_tree(b));
        let want = build_tree(w);
        assert!(same_tree(got.as_ref(), want.as_ref()));
    }};
    m(&[Some(1), Some(3), Some(2), Some(5)], &[Some(2), Some(1), Some(3), None, Some(4), None, Some(7)], &[Some(3), Some(4), Some(5), Some(5), Some(4), None, Some(7)]);
    m(&[], &[Some(1)], &[Some(1)]);
    m(&[Some(1)], &[], &[Some(1)]);
    m(&[Some(1), Some(2), Some(3)], &[Some(1), Some(2), Some(3)], &[Some(2), Some(4), Some(6)]);
    println!("PASS");
}}
''',
"lua": '''{H}
local function same_tree(p, q)
    if not p and not q then return true end
    if not p or not q or p.val ~= q.val then return false end
    return same_tree(p.left, q.left) and same_tree(p.right, q.right)
end
local function merge_trees(t1, t2)
    if not t1 then return t2 end
    if not t2 then return t1 end
    t1.val = t1.val + t2.val
    t1.left = merge_trees(t1.left, t2.left)
    t1.right = merge_trees(t1.right, t2.right)
    return t1
end
local function check(a, b, w)
    assert(same_tree(merge_trees(build_tree(a), build_tree(b)), build_tree(w)), "merge failed")
end
check({{1,3,2,5}}, {{2,1,3,"null",4,"null",7}}, {{3,4,5,5,4,"null",7}})
check({{}}, {{1}}, {{1}})
check({{1}}, {{}}, {{1}})
check({{1,2,3}}, {{1,2,3}}, {{2,4,6}})
print("PASS")
''',
"c": '''{H}
static int same_tree(const TreeNode *p, const TreeNode *q) {{
    if (!p && !q) return 1;
    if (!p || !q || p->val != q->val) return 0;
    return same_tree(p->left, q->left) && same_tree(p->right, q->right);
}}
static TreeNode *merge_trees(TreeNode *t1, TreeNode *t2) {{
    if (!t1) return t2;
    if (!t2) return t1;
    t1->val += t2->val;
    t1->left = merge_trees(t1->left, t2->left);
    t1->right = merge_trees(t1->right, t2->right);
    return t1;
}}
static void check(const int *a, int na, const int *b, int nb, const int *w, int nw) {{
    TreeNode *got = merge_trees(build_tree(a, na), build_tree(b, nb));
    TreeNode *want = build_tree(w, nw);
    if (!same_tree(got, want)) {{ printf("FAIL merge\\n"); exit(1); }}
}}
int main(void) {{
    int a1[] = {{1,3,2,5}}, b1[] = {{2,1,3,INT_MIN_SN,4,INT_MIN_SN,7}}, w1[] = {{3,4,5,5,4,INT_MIN_SN,7}};
    int a2[] = {{0}}, b2[] = {{1}}, w2[] = {{1}};  /* 空树用长度0表达 */
    int a4[] = {{1,2,3}}, b4[] = {{1,2,3}}, w4[] = {{2,4,6}};
    check(a1, 4, b1, 7, w1, 7);
    if (!same_tree(merge_trees(NULL, build_tree(b2, 1)), build_tree(w2, 1))) {{ printf("FAIL 2\\n"); return 1; }}
    if (!same_tree(merge_trees(build_tree(b2, 1), NULL), build_tree(w2, 1))) {{ printf("FAIL 3\\n"); return 1; }}
    check(a4, 3, b4, 3, w4, 3);
    (void)a2;
    printf("PASS\\n");
    return 0;
}}
''',
"cpp": '''{H}
static bool sameTree(const TreeNode *p, const TreeNode *q) {{
    if (!p && !q) return true;
    if (!p || !q || p->val != q->val) return false;
    return sameTree(p->left, q->left) && sameTree(p->right, q->right);
}}
static TreeNode *mergeTrees(TreeNode *t1, TreeNode *t2) {{
    if (!t1) return t2;
    if (!t2) return t1;
    t1->val += t2->val;
    t1->left = mergeTrees(t1->left, t2->left);
    t1->right = mergeTrees(t1->right, t2->right);
    return t1;
}}
static void check(std::vector<std::optional<int>> a, std::vector<std::optional<int>> b, std::vector<std::optional<int>> w) {{
    assert(sameTree(mergeTrees(build_tree(a), build_tree(b)), build_tree(w)));
}}
int main() {{
    check({{1, 3, 2, 5}}, {{2, 1, 3, std::nullopt, 4, std::nullopt, 7}}, {{3, 4, 5, 5, 4, std::nullopt, 7}});
    check({{}}, {{1}}, {{1}});
    check({{1}}, {{}}, {{1}});
    check({{1, 2, 3}}, {{1, 2, 3}}, {{2, 4, 6}});
    std::cout << "PASS" << std::endl;
    return 0;
}}
''',
"r": '''{H}
same_tree <- function(p, q) {{
  if (is.null(p) && is.null(q)) return(TRUE)
  if (is.null(p) || is.null(q) || p$val != q$val) return(FALSE)
  same_tree(p$left, q$left) && same_tree(p$right, q$right)
}}
merge_trees <- function(t1, t2) {{
  if (is.null(t1)) return(t2)
  if (is.null(t2)) return(t1)
  t1$val <- t1$val + t2$val
  t1$left <- merge_trees(t1$left, t2$left)
  t1$right <- merge_trees(t1$right, t2$right)
  t1
}}
check <- function(a, b, w) stopifnot(same_tree(merge_trees(build_tree(a), build_tree(b)), build_tree(w)))
check(list(1L, 3L, 2L, 5L), list(2L, 1L, 3L, NA, 4L, NA, 7L), list(3L, 4L, 5L, 5L, 4L, NA, 7L))
check(list(), list(1L), list(1L))
check(list(1L), list(), list(1L))
check(list(1L, 2L, 3L), list(1L, 2L, 3L), list(2L, 4L, 6L))
cat("PASS\\n")
''',
"zig": '''{H}
fn sameTree(p: ?*const TreeNode, q: ?*const TreeNode) bool {{
    if (p == null and q == null) return true;
    if (p == null or q == null) return false;
    const a = p.?;
    const b = q.?;
    return a.val == b.val and sameTree(a.left, b.left) and sameTree(a.right, b.right);
}}
fn mergeTrees(alloc: std.mem.Allocator, t1: ?*TreeNode, t2: ?*TreeNode) ?*TreeNode {{
    const n1 = t1 orelse return t2;
    const n2 = t2 orelse return n1;
    n1.val += n2.val;
    n1.left = mergeTrees(alloc, n1.left, n2.left);
    n1.right = mergeTrees(alloc, n1.right, n2.right);
    return n1;
}}
pub fn main() !void {{
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();
    const alloc = arena.allocator();
    const Case = struct {{ a: []const i32, b: []const i32, w: []const i32 }};
    const cases = [_]Case{{
        .{{ .a = &[_]i32{{ 1, 3, 2, 5 }}, .b = &[_]i32{{ 2, 1, 3, -1, 4, -1, 7 }}, .w = &[_]i32{{ 3, 4, 5, 5, 4, -1, 7 }} }},
        .{{ .a = &[_]i32{{}}, .b = &[_]i32{{1}}, .w = &[_]i32{{1}} }},
        .{{ .a = &[_]i32{{1}}, .b = &[_]i32{{}}, .w = &[_]i32{{1}} }},
        .{{ .a = &[_]i32{{ 1, 2, 3 }}, .b = &[_]i32{{ 1, 2, 3 }}, .w = &[_]i32{{ 2, 4, 6 }} }},
    }};
    for (cases, 0..) |c, i| {{
        const got = mergeTrees(alloc, try buildTree(alloc, c.a), try buildTree(alloc, c.b));
        const want = try buildTree(alloc, c.w);
        if (!sameTree(got, want)) {{
            std.debug.print("FAIL case {{d}}\\n", .{{i}});
            return error.TestFailed;
        }}
    }}
    std.debug.print("PASS\\n", .{{}});
}}
''',
"dart": '''{H}
bool sameTree(TreeNode? p, TreeNode? q) {{
  if (p == null && q == null) return true;
  if (p == null || q == null || p.val != q.val) return false;
  return sameTree(p.left, q.left) && sameTree(p.right, q.right);
}}
TreeNode? mergeTrees(TreeNode? t1, TreeNode? t2) {{
  if (t1 == null) return t2;
  if (t2 == null) return t1;
  t1.val += t2.val;
  t1.left = mergeTrees(t1.left, t2.left);
  t1.right = mergeTrees(t1.right, t2.right);
  return t1;
}}
void check(List<int?> a, List<int?> b, List<int?> w) {{
  if (!sameTree(mergeTrees(buildTree(a), buildTree(b)), buildTree(w))) throw StateError('merge failed');
}}
void main() {{
  check([1, 3, 2, 5], [2, 1, 3, null, 4, null, 7], [3, 4, 5, 5, 4, null, 7]);
  check([], [1], [1]);
  check([1], [], [1]);
  check([1, 2, 3], [1, 2, 3], [2, 4, 6]);
  print('PASS');
}}
''',
}

PROBS = [
    ("lc_101_对称二叉树", A101, "LeetCode 101. 对称二叉树"),
    ("lc_111_二叉树的最小深度", A111, "LeetCode 111. 二叉树的最小深度"),
    ("lc_222_完全二叉树的节点个数", A222, "LeetCode 222. 完全二叉树的节点个数"),
    ("lc_404_左叶子之和", A404, "LeetCode 404. 左叶子之和"),
    ("lc_617_合并二叉树", A617, "LeetCode 617. 合并二叉树"),
]
count = 0
for prob, algo, title in PROBS:
    bid = B[prob.split("_")[1]]
    ts_dir = f"/Users/Wang/Code/github/web-x-blog/work/blog/courses/21.dsa/ts/tree/{prob}"
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
