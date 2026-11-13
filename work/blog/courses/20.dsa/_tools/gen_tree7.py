#!/usr/bin/env python3
# gen_tree7.py — tree 收官批：lc_109/lc_114/lc_116/lc_117 × 7语言
import sys, os; sys.path.insert(0, "/Users/Wang/Code/github/web-x-blog/work/blog/courses/20.dsa/_tools")
from langlib import emit, TREE_H, head_comment, EXT

B = {"109": "135270549", "114": "135637716", "116": "145386215", "117": "145386298"}
LANGNAME = {"rust": "Rust", "lua": "Lua", "c": "C", "cpp": "C++", "r": "R", "zig": "Zig", "dart": "Dart"}

# 109 需要 ListNode；116/117 用带 next 的节点（复用 TreeNode + next 字段单独定义）
A109 = {
"rust": '''{H}
#[derive(Debug)]
struct ListNode {{ val: i32, next: Option<Box<ListNode>> }}
fn build_list(vals: &[i32]) -> Option<Box<ListNode>> {{
    let mut head: Option<Box<ListNode>> = None;
    for &v in vals.iter().rev() {{
        let mut n = Box::new(ListNode {{ val: v, next: None }});
        n.next = head;
        head = Some(n);
    }}
    head
}}
fn sorted_list_to_bst(head: Option<Box<ListNode>>) -> Option<Rc<RefCell<TreeNode>>> {{
    let mut nodes: Vec<i32> = Vec::new();
    let mut cur = &head;
    while let Some(n) = cur {{
        nodes.push(n.val);
        cur = &n.next;
    }}
    fn build(nodes: &[i32], left: isize, right: isize) -> Option<Rc<RefCell<TreeNode>>> {{
        if left > right {{ return None; }}
        let mid = left + (right - left) / 2;
        let root = TreeNode::new(nodes[mid as usize]);
        root.borrow_mut().left = build(nodes, left, mid - 1);
        root.borrow_mut().right = build(nodes, mid + 1, right);
        Some(root)
    }}
    if nodes.is_empty() {{ None }} else {{ build(&nodes, 0, nodes.len() as isize - 1) }}
}}
fn inorder(n: Option<&Rc<RefCell<TreeNode>>>, out: &mut Vec<i32>) {{
    let node = match n {{ Some(x) => x, None => return }};
    let nb = node.borrow();
    inorder(nb.left.as_ref(), out);
    out.push(nb.val);
    inorder(nb.right.as_ref(), out);
}}
fn main() {{
    assert!(sorted_list_to_bst(None).is_none());
    let t = sorted_list_to_bst(build_list(&[1, 2, 3]));
    let mut out = Vec::new();
    inorder(t.as_ref(), &mut out);
    assert_eq!(out, vec![1, 2, 3]);
    // 结构验证：[1,2,3] 中点 2 为根
    let mut lvl = std::collections::VecDeque::new();
    lvl.push_back(t.clone().unwrap());
    let mut flat = Vec::new();
    while let Some(n) = lvl.pop_front() {{
        let nb = n.borrow();
        flat.push(nb.val);
        if let Some(c) = nb.left.clone() {{ lvl.push_back(c); }}
        if let Some(c) = nb.right.clone() {{ lvl.push_back(c); }}
    }}
    assert_eq!(flat, vec![2, 1, 3]);
    println!("PASS");
}}
''',
"lua": '''{H}
local ListNode = {{}}
ListNode.__index = ListNode
function ListNode.new(val, next) return setmetatable({{val = val, next = next}}, ListNode) end
local function build_list(vals)
    local head, cur = nil, nil
    for _, v in ipairs(vals) do
        local n = ListNode.new(v)
        if not head then head, cur = n, n else cur.next, cur = n, n end
    end
    return head
end
local function sorted_list_to_bst(head)
    local nodes = {{}}
    local cur = head
    while cur do nodes[#nodes + 1] = cur.val; cur = cur.next end
    local function build(left, right)
        if left > right then return nil end
        local mid = left + math.floor((right - left) / 2)
        local root = TreeNode.new(nodes[mid])
        root.left = build(left, mid - 1)
        root.right = build(mid + 1, right)
        return root
    end
    if #nodes == 0 then return nil end
    return build(1, #nodes)
end
local function inorder(n, out)
    if not n then return end
    inorder(n.left, out)
    out[#out + 1] = n.val
    inorder(n.right, out)
end
assert(sorted_list_to_bst(nil) == nil)
local t = sorted_list_to_bst(build_list({{1, 2, 3}}))
local out = {{}}
inorder(t, out)
assert(#out == 3 and out[1] == 1 and out[2] == 2 and out[3] == 3)
-- 结构验证：层序 [2,1,3]
local q, flat = {{t}}, {{}}
while #q > 0 do
    local n = table.remove(q, 1)
    flat[#flat + 1] = n.val
    if n.left then q[#q + 1] = n.left end
    if n.right then q[#q + 1] = n.right end
end
assert(#flat == 3 and flat[1] == 2 and flat[2] == 1 and flat[3] == 3)
print("PASS")
''',
"c": '''{H}
typedef struct ListNode {{ int val; struct ListNode *next; }} ListNode;
static ListNode *build_list(const int *vals, int n) {{
    ListNode *head = NULL, **cur = &head;
    for (int i = 0; i < n; i++) {{
        ListNode *node = malloc(sizeof(ListNode));
        node->val = vals[i]; node->next = NULL;
        *cur = node; cur = &node->next;
    }}
    return head;
}}
static TreeNode *build_bst(const int *nodes, int left, int right) {{
    if (left > right) return NULL;
    int mid = left + (right - left) / 2;
    TreeNode *root = malloc(sizeof(TreeNode));
    root->val = nodes[mid]; root->left = root->right = NULL;
    root->left = build_bst(nodes, left, mid - 1);
    root->right = build_bst(nodes, mid + 1, right);
    return root;
}}
static TreeNode *sorted_list_to_bst(ListNode *head) {{
    int nodes[4096], n = 0;
    for (ListNode *c = head; c; c = c->next) nodes[n++] = c->val;
    if (n == 0) return NULL;
    return build_bst(nodes, 0, n - 1);
}}
static void free_list(ListNode *h) {{ while (h) {{ ListNode *n = h->next; free(h); h = n; }} }}
int main(void) {{
    if (sorted_list_to_bst(NULL) != NULL) {{ printf("FAIL 0\\n"); return 1; }}
    int vals[] = {{1, 2, 3}};
    ListNode *l = build_list(vals, 3);
    TreeNode *t = sorted_list_to_bst(l);
    /* 中序 [1,2,3] 且层序 [2,1,3] */
    if (t->val != 2 || t->left->val != 1 || t->right->val != 3) {{ printf("FAIL shape\\n"); return 1; }}
    if (!(t->left->left == NULL && t->left->right == NULL && t->right->left == NULL && t->right->right == NULL)) {{ printf("FAIL leaves\\n"); return 1; }}
    free_list(l);
    free_tree(t);
    printf("PASS\\n");
    return 0;
}}
''',
"cpp": '''{H}
struct ListNode {{
    int val;
    ListNode *next;
    explicit ListNode(int v) : val(v), next(nullptr) {{}}
}};
static ListNode *buildList(const std::vector<int> &vals) {{
    ListNode dummy(0);
    ListNode *cur = &dummy;
    for (int v : vals) {{
        cur->next = new ListNode(v);
        cur = cur->next;
    }}
    return dummy.next;
}}
static TreeNode *buildBst(const std::vector<int> &nodes, int left, int right) {{
    if (left > right) return nullptr;
    int mid = left + (right - left) / 2;
    auto *root = new TreeNode(nodes[mid]);
    root->left = buildBst(nodes, left, mid - 1);
    root->right = buildBst(nodes, mid + 1, right);
    return root;
}}
static TreeNode *sortedListToBST(ListNode *head) {{
    std::vector<int> nodes;
    for (ListNode *c = head; c; c = c->next) nodes.push_back(c->val);
    if (nodes.empty()) return nullptr;
    return buildBst(nodes, 0, static_cast<int>(nodes.size()) - 1);
}}
static void inorder(TreeNode *n, std::vector<int> &out) {{
    if (!n) return;
    inorder(n->left, out);
    out.push_back(n->val);
    inorder(n->right, out);
}}
int main() {{
    assert(sortedListToBST(nullptr) == nullptr);
    auto *t = sortedListToBST(buildList({{1, 2, 3}}));
    std::vector<int> out;
    inorder(t, out);
    assert((out == std::vector<int>{{1, 2, 3}}));
    assert(t->val == 2 && t->left->val == 1 && t->right->val == 3);
    std::cout << "PASS" << std::endl;
    return 0;
}}
''',
"r": '''{H}
ListNode <- function(val, nxt = NULL) {{ e <- new.env(parent = emptyenv()); e$val <- val; e$nxt <- nxt; class(e) <- "ListNode"; e }}
build_list <- function(vals) {{
  head <- NULL; cur <- NULL
  for (v in vals) {{
    n <- ListNode(v)
    if (is.null(head)) {{ head <- n; cur <- n }} else {{ cur$nxt <- n; cur <- n }}
  }}
  head
}}
sorted_list_to_bst <- function(head) {{
  nodes <- integer(0); cur <- head
  while (!is.null(cur)) {{ nodes[[length(nodes) + 1L]] <- cur$val; cur <- cur$nxt }}
  if (length(nodes) == 0L) return(NULL)
  build <- function(left, right) {{
    if (left > right) return(NULL)
    mid <- left + (right - left) %/% 2L
    root <- TreeNode(nodes[mid])
    root$left <- build(left, mid - 1L)
    root$right <- build(mid + 1L, right)
    root
  }}
  build(1L, length(nodes))
}}
inorder_fn <- function(n) {{
  if (is.null(n)) return(integer(0))
  c(inorder_fn(n$left), n$val, inorder_fn(n$right))
}}
stopifnot(is.null(sorted_list_to_bst(NULL)))
t <- sorted_list_to_bst(build_list(c(1L, 2L, 3L)))
out <- inorder_fn(t)
stopifnot(identical(out, c(1L, 2L, 3L)))
stopifnot(t$val == 2L, t$left$val == 1L, t$right$val == 3L)
cat("PASS\\n")
''',
"zig": '''{H}
const ListNode = struct {{ val: i32, next: ?*ListNode }};
fn buildList(alloc: std.mem.Allocator, vals: []const i32) ?*ListNode {{
    var head: ?*ListNode = null;
    var tail: ?*ListNode = null;
    for (vals) |v| {{
        const n = alloc.create(ListNode) catch unreachable;
        n.* = .{{ .val = v, .next = null }};
        if (tail) |t| t.next = n else head = n;
        tail = n;
    }}
    return head;
}}
fn buildBst(nodes: []const i32, left: isize, right: isize, alloc: std.mem.Allocator) ?*TreeNode {{
    if (left > right) return null;
    const mid = left + @divTrunc(right - left, 2);
    const root = alloc.create(TreeNode) catch unreachable;
    root.* = .{{ .val = nodes[@intCast(mid)], .left = null, .right = null }};
    root.left = buildBst(nodes, left, mid - 1, alloc);
    root.right = buildBst(nodes, mid + 1, right, alloc);
    return root;
}}
fn sortedListToBST(head: ?*ListNode, alloc: std.mem.Allocator) ?*TreeNode {{
    var nodes = std.ArrayList(i32).init(alloc);
    var cur = head;
    while (cur) |c| {{
        nodes.append(c.val) catch unreachable;
        cur = c.next;
    }}
    if (nodes.items.len == 0) return null;
    return buildBst(nodes.items, 0, @as(isize, @intCast(nodes.items.len)) - 1, alloc);
}}
fn inorderFn(n: ?*TreeNode, out: *std.ArrayList(i32)) void {{
    const node = n orelse return;
    inorderFn(node.left, out);
    out.append(node.val) catch unreachable;
    inorderFn(node.right, out);
}}
pub fn main() !void {{
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();
    const alloc = arena.allocator();
    if (sortedListToBST(null, alloc) != null) return error.TestFailed;
    const t = sortedListToBST(buildList(alloc, &[_]i32{{ 1, 2, 3 }}), alloc).?;
    var out = std.ArrayList(i32).init(std.heap.page_allocator);
    defer out.deinit();
    inorderFn(t, &out);
    const want = [_]i32{{ 1, 2, 3 }};
    if (out.items.len != want.len) return error.TestFailed;
    for (want, 0..) |w, i| if (out.items[i] != w) return error.TestFailed;
    if (t.val != 2 or t.left.?.val != 1 or t.right.?.val != 3) return error.TestFailed;
    std.debug.print("PASS\\n", .{{}});
}}
''',
"dart": '''{H}
class LNode {
  final int val;
  LNode? next;
  LNode(this.val);
}
LNode? buildList(List<int> vals) {
  LNode? head;
  LNode? cur;
  for (final v in vals) {
    final n = LNode(v);
    if (head == null) {
      head = n;
    } else {
      cur!.next = n;
    }
    cur = n;
  }
  return head;
}
TreeNode? buildBst(List<int> nodes, int left, int right) {
  if (left > right) return null;
  final mid = left + (right - left) ~/ 2;
  final root = TreeNode(nodes[mid]);
  root.left = buildBst(nodes, left, mid - 1);
  root.right = buildBst(nodes, mid + 1, right);
  return root;
}
TreeNode? sortedListToBST(LNode? head) {
  final nodes = <int>[];
  var cur = head;
  while (cur != null) {
    nodes.add(cur.val);
    cur = cur.next;
  }
  if (nodes.isEmpty) return null;
  return buildBst(nodes, 0, nodes.length - 1);
}
void inorder(TreeNode? n, List<int> out) {
  if (n == null) return;
  inorder(n.left, out);
  out.add(n.val);
  inorder(n.right, out);
}
void main() {
  if (sortedListToBST(null) != null) throw StateError('c0');
  final t = sortedListToBST(buildList([1, 2, 3]));
  final out = <int>[];
  inorder(t, out);
  if (out.toString() != '[1, 2, 3]') throw StateError('c1');
  if (t!.val != 2 || t.left!.val != 1 || t.right!.val != 3) throw StateError('c2');
  print('PASS');
}
''',
}

A114 = {
"rust": '''{H}
fn flatten(root: Option<Rc<RefCell<TreeNode>>>) {{
    let mut prev: Option<Rc<RefCell<TreeNode>>> = None;
    fn dfs(node: Option<Rc<RefCell<TreeNode>>>, prev: &mut Option<Rc<RefCell<TreeNode>>>) {{
        let n = match node {{ Some(x) => x, None => return }};
        dfs(n.borrow().right.clone(), prev);
        dfs(n.borrow().left.clone(), prev);
        let mut nb = n.borrow_mut();
        nb.right = prev.take();
        nb.left = None;
        drop(nb);
        *prev = Some(n);
    }}
    dfs(root, &mut prev);
}}
fn main() {{
    let t = build_tree(&[Some(1), Some(2), Some(5), Some(3), Some(4), None, Some(6)]);
    flatten(t.clone());
    let mut cur = t;
    let mut got = Vec::new();
    while let Some(n) = cur {{
        let nb = n.borrow();
        assert!(nb.left.is_none(), "left must be null");
        got.push(nb.val);
        cur = nb.right.clone();
    }}
    assert_eq!(got, vec![1, 2, 3, 4, 5, 6]);
    let t2 = build_tree(&[Some(7)]);
    flatten(t2.clone());
    let mut got2 = Vec::new();
    let mut cur2 = t2;
    while let Some(n) = cur2 {{ got2.push(n.borrow().val); cur2 = n.borrow().right.clone(); }}
    assert_eq!(got2, vec![7]);
    let none: Option<Rc<RefCell<TreeNode>>> = None;
    flatten(none);
    println!("PASS");
}}
''',
"lua": '''{H}
local function flatten(root)
    local prev = nil
    local function dfs(node)
        if not node then return end
        dfs(node.right)
        dfs(node.left)
        node.right = prev
        node.left = nil
        prev = node
    end
    dfs(root)
    return root
end
local function chain(root)
    local out = {{}}
    while root do
        assert(root.left == nil, "left must be nil")
        out[#out + 1] = root.val
        root = root.right
    end
    return out
end
local t = flatten(build_tree({{1, 2, 5, 3, 4, "null", 6}}))
local c = chain(t)
assert(#c == 6 and c[1] == 1 and c[6] == 6 and c[2] == 2 and c[3] == 3 and c[4] == 4 and c[5] == 5)
local t2 = flatten(build_tree({{7}}))
local c2 = chain(t2)
assert(#c2 == 1 and c2[1] == 7)
assert(flatten(nil) == nil)
print("PASS")
''',
"c": '''{H}
static TreeNode *g_prev_114;
static void dfs_114(TreeNode *node) {{
    if (!node) return;
    dfs_114(node->right);
    dfs_114(node->left);
    node->right = g_prev_114;
    node->left = NULL;
    g_prev_114 = node;
}}
static TreeNode *flatten(TreeNode *root) {{
    g_prev_114 = NULL;
    dfs_114(root);
    return root;
}}
static int chain(TreeNode *root, int out[]) {{
    int cnt = 0;
    while (root) {{
        if (root->left) {{ printf("FAIL left\\n"); exit(1); }}
        out[cnt++] = root->val;
        root = root->right;
    }}
    return cnt;
}}
int main(void) {{
    int v1[] = {{1,2,5,3,4,INT_MIN_SN,6}};
    int w1[] = {{1,2,3,4,5,6}};
    int out[64], n;
    TreeNode *t = flatten(build_tree(v1, 7));
    n = chain(t, out);
    if (n != 6) {{ printf("FAIL len\\n"); return 1; }}
    for (int i = 0; i < 6; i++) if (out[i] != w1[i]) {{ printf("FAIL %d\\n", i); return 1; }}
    int v2[] = {{7}};
    TreeNode *t2 = flatten(build_tree(v2, 1));
    n = chain(t2, out);
    if (n != 1 || out[0] != 7) {{ printf("FAIL 2\\n"); return 1; }}
    if (flatten(NULL) != NULL) {{ printf("FAIL 3\\n"); return 1; }}
    printf("PASS\\n");
    return 0;
}}
''',
"cpp": '''{H}
static TreeNode *flatten(TreeNode *root) {{
    TreeNode *prev = nullptr;
    std::function<void(TreeNode *)> dfs = [&](TreeNode *node) {{
        if (!node) return;
        dfs(node->right);
        dfs(node->left);
        node->right = prev;
        node->left = nullptr;
        prev = node;
    }};
    dfs(root);
    return root;
}}
static std::vector<int> chain(TreeNode *root) {{
    std::vector<int> out;
    while (root) {{
        assert(root->left == nullptr);
        out.push_back(root->val);
        root = root->right;
    }}
    return out;
}}
int main() {{
    assert((chain(flatten(build_tree({{1, 2, 5, 3, 4, std::nullopt, 6}}))) == std::vector<int>{{1, 2, 3, 4, 5, 6}}));
    assert((chain(flatten(build_tree({{7}}))) == std::vector<int>{{7}}));
    assert(flatten(nullptr) == nullptr);
    std::cout << "PASS" << std::endl;
    return 0;
}}
''',
"r": '''{H}
flatten <- function(root) {{
  prev <- NULL
  dfs <- function(node) {{
    if (is.null(node)) return(invisible(NULL))
    dfs(node$right)
    dfs(node$left)
    node$right <- prev   # node 是 environment，<- 字段赋值即原地生效
    node$left <- NULL
    prev <<- node
  }}
  dfs(root)
  root
}}
chain <- function(root) {{
  out <- integer(0)
  while (!is.null(root)) {{
    stopifnot(is.null(root$left))
    out[[length(out) + 1L]] <- root$val
    root <- root$right
  }}
  out
}}
stopifnot(identical(chain(flatten(build_tree(list(1L, 2L, 5L, 3L, 4L, NA, 6L)))), 1:6))
stopifnot(identical(chain(flatten(build_tree(list(7L)))), 7L))
stopifnot(is.null(flatten(NULL)))
cat("PASS\\n")
''',
"zig": '''{H}
fn flatten(root: ?*TreeNode) void {{
    const D = struct {{
        var prev: ?*TreeNode = null;
        fn dfs(node: ?*TreeNode) void {{
            const n = node orelse return;
            dfs(n.right);
            dfs(n.left);
            n.right = prev;
            n.left = null;
            prev = n;
        }}
    }};
    D.prev = null;
    D.dfs(root);
}}
fn chain(root: ?*TreeNode, out: *std.ArrayList(i32)) void {{
    var cur = root;
    while (cur) |n| {{
        if (n.left != null) return; // left 必须为空：留给上层判长度失败
        out.append(n.val) catch unreachable;
        cur = n.right;
    }}
}}
pub fn main() !void {{
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();
    const alloc = arena.allocator();
    var out = std.ArrayList(i32).init(std.heap.page_allocator);
    defer out.deinit();
    const t = try buildTree(alloc, &[_]i32{{ 1, 2, 5, 3, 4, -1, 6 }});
    flatten(t);
    chain(t, &out);
    const w1 = [_]i32{{ 1, 2, 3, 4, 5, 6 }};
    if (out.items.len != w1.len) return error.TestFailed;
    for (w1, 0..) |w, i| if (out.items[i] != w) return error.TestFailed;
    out.clearRetainingCapacity();
    const t2 = try buildTree(alloc, &[_]i32{{7}});
    flatten(t2);
    chain(t2, &out);
    if (out.items.len != 1 or out.items[0] != 7) return error.TestFailed;
    flatten(null);
    std.debug.print("PASS\\n", .{{}});
}}
''',
"dart": '''{H}
TreeNode? flatten(TreeNode? root) {{
  TreeNode? prev;
  void dfs(TreeNode? node) {{
    if (node == null) return;
    dfs(node.right);
    dfs(node.left);
    node.right = prev;
    node.left = null;
    prev = node;
  }}
  dfs(root);
  return root;
}}
List<int> chain(TreeNode? root) {{
  final out = <int>[];
  var cur = root;
  while (cur != null) {{
    if (cur.left != null) throw StateError('left not null');
    out.add(cur.val);
    cur = cur.right;
  }}
  return out;
}}
void main() {{
  if (chain(flatten(buildTree([1, 2, 5, 3, 4, null, 6]))).toString() != '[1, 2, 3, 4, 5, 6]') throw StateError('c1');
  if (chain(flatten(buildTree([7]))).toString() != '[7]') throw StateError('c2');
  if (flatten(null) != null) throw StateError('c3');
  print('PASS');
}}
''',
}

# 116/117 共用：带 next 的节点 + 层级 next 链验证
A116 = {
"rust": '''{H}
#[derive(Debug)]
struct NNode {{ val: i32, left: Option<Box<NNode>>, right: Option<Box<NNode>>, next: Option<*mut NNode> }}
fn build_perfect(alloc: &mut Vec<Box<NNode>>, vals: &[i32]) -> Option<*mut NNode> {{
    if vals.is_empty() {{ return None; }}
    let mut nodes: Vec<*mut NNode> = Vec::new();
    for &v in vals {{
        alloc.push(Box::new(NNode {{ val: v, left: None, right: None, next: None }}));
        let p: *mut NNode = alloc.last().unwrap().as_mut() as *mut NNode;
        nodes.push(p);
    }}
    let mut i = 1;
    let mut head = 0;
    while i < nodes.len() {{
        let n = nodes[head];
        unsafe {{
            if i < nodes.len() {{ (*n).left = Some(Box::from_raw(nodes[i])); i += 1; }}
        }}
        head += 1;
    }}
    // 上述构造会破坏 Box 所有权，改用简单方式：预分配数组+索引
    None
}}
''',
}
# Rust 的 NNode 用裸指针太复杂，改用 Rc<RefCell> 风格（与 TreeNode 一致）

A116 = {
"rust": '''{H}
#[derive(Debug)]
struct NNode {{ val: i32, left: Option<Rc<RefCell<NNode>>>, right: Option<Rc<RefCell<NNode>>>, next: Option<Rc<RefCell<NNode>>> }}
impl NNode {{ fn new(v: i32) -> Rc<RefCell<NNode>> {{ Rc::new(RefCell::new(NNode {{ val: v, left: None, right: None, next: None }})) }} }}
fn build_ntree(vals: &[i32]) -> Option<Rc<RefCell<NNode>>> {{
    if vals.is_empty() {{ return None; }}
    let root = NNode::new(vals[0]);
    let mut q = vec![root.clone()];
    let mut i = 1;
    while !q.is_empty() && i < vals.len() {{
        let node = q.remove(0);
        if i < vals.len() {{ let c = NNode::new(vals[i]); node.borrow_mut().left = Some(c.clone()); q.push(c); i += 1; }}
        if i < vals.len() {{ let c = NNode::new(vals[i]); node.borrow_mut().right = Some(c.clone()); q.push(c); i += 1; }}
    }}
    Some(root)
}}
fn connect(root: Option<Rc<RefCell<NNode>>>) -> Option<Rc<RefCell<NNode>>> {{
    let root = root?;
    let mut queue = vec![root.clone()];
    while !queue.is_empty() {{
        let size = queue.len();
        let mut prev: Option<Rc<RefCell<NNode>>> = None;
        for _ in 0..size {{
            let node = queue.remove(0);
            if let Some(p) = prev {{ p.borrow_mut().next = Some(node.clone()); }}
            prev = Some(node.clone());
            let nb = node.borrow();
            if let Some(c) = nb.left.clone() {{ queue.push(c); }}
            if let Some(c) = nb.right.clone() {{ queue.push(c); }}
        }}
    }}
    Some(root)
}}
fn main() {{
    assert!(connect(None).is_none());
    let root = connect(build_ntree(&[1, 2, 3, 4, 5, 6, 7]));
    let mut levels: Vec<Vec<i32>> = Vec::new();
    let mut cur = root.clone();
    while let Some(c) = cur {{
        let mut vals = Vec::new();
        let mut node = Some(c.clone());
        while let Some(n) = node {{
            vals.push(n.borrow().val);
            node = n.borrow().next.clone();
        }}
        levels.push(vals);
        cur = c.borrow().left.clone();
    }}
    assert_eq!(levels, vec![vec![1], vec![2, 3], vec![4, 5, 6, 7]]);
    println!("PASS");
}}
''',
"lua": '''{H}
local NNode = {{}}
NNode.__index = NNode
function NNode.new(v) return setmetatable({{val = v, left = nil, right = nil, next = nil}}, NNode) end
local function build_ntree(vals)
    if #vals == 0 then return nil end
    local root = NNode.new(vals[1])
    local q = {{root}}
    local head, i = 1, 2
    while head <= #q and i <= #vals do
        local node = q[head]
        head = head + 1
        if i <= #vals then node.left = NNode.new(vals[i]); q[#q + 1] = node.left; i = i + 1 end
        if i <= #vals then node.right = NNode.new(vals[i]); q[#q + 1] = node.right; i = i + 1 end
    end
    return root
end
local function connect(root)
    if not root then return nil end
    local queue = {{root}}
    while #queue > 0 do
        local size = #queue
        local prev = nil
        for _ = 1, size do
            local node = table.remove(queue, 1)
            if prev then prev.next = node end
            prev = node
            if node.left then queue[#queue + 1] = node.left end
            if node.right then queue[#queue + 1] = node.right end
        end
    end
    return root
end
assert(connect(nil) == nil)
local root = connect(build_ntree({{1, 2, 3, 4, 5, 6, 7}}))
local levels = {{}}
local cur = root
while cur do
    local vals = {{}}
    local node = cur
    while node do
        vals[#vals + 1] = node.val
        node = node.next
    end
    levels[#levels + 1] = vals
    cur = cur.left
end
assert(#levels == 3)
assert(#levels[1] == 1 and levels[1][1] == 1)
assert(#levels[2] == 2 and levels[2][1] == 2 and levels[2][2] == 3)
assert(#levels[3] == 4 and levels[3][1] == 4 and levels[3][4] == 7)
print("PASS")
''',
"c": '''{H}
typedef struct NNode {{ int val; struct NNode *left, *right, *next; }} NNode;
static NNode *nnew(int v) {{ NNode *n = calloc(1, sizeof(NNode)); n->val = v; return n; }}
static void free_ntree(NNode *n) {{ if (!n) return; free_ntree(n->left); free_ntree(n->right); free(n); }}
static NNode *build_ntree(const int *vals, int n) {{
    if (n == 0) return NULL;
    NNode *root = nnew(vals[0]);
    NNode *q[256];
    int head = 0, tail = 0, i = 1;
    q[tail++] = root;
    while (head < tail && i < n) {{
        NNode *node = q[head++];
        if (i < n) {{ node->left = nnew(vals[i]); q[tail++] = node->left; i++; }}
        if (i < n) {{ node->right = nnew(vals[i]); q[tail++] = node->right; i++; }}
    }}
    return root;
}}
static NNode *connect(NNode *root) {{
    if (!root) return NULL;
    NNode *q[256];
    int head = 0, tail = 0;
    q[tail++] = root;
    while (head < tail) {{
        int size = tail - head;
        NNode *prev = NULL;
        for (int i = 0; i < size; i++) {{
            NNode *node = q[head++];
            if (prev) prev->next = node;
            prev = node;
            if (node->left) q[tail++] = node->left;
            if (node->right) q[tail++] = node->right;
        }}
    }}
    return root;
}}
int main(void) {{
    int vals[] = {{1,2,3,4,5,6,7}};
    if (connect(NULL) != NULL) {{ printf("FAIL nil\\n"); return 1; }}
    NNode *root = connect(build_ntree(vals, 7));
    NNode *cur = root;
    int level = 0;
    int want[3][4] = {{ {{1}}, {{2,3}}, {{4,5,6,7}} }};
    int wantn[3] = {{1, 2, 4}};
    while (cur) {{
        int cnt = 0;
        for (NNode *n = cur; n; n = n->next) {{
            if (cnt >= wantn[level] || n->val != want[level][cnt]) {{ printf("FAIL L%d\\n", level); return 1; }}
            cnt++;
        }}
        if (cnt != wantn[level]) {{ printf("FAIL L%d cnt\\n", level); return 1; }}
        cur = cur->left;
        level++;
    }}
    if (level != 3) {{ printf("FAIL levels\\n"); return 1; }}
    free_ntree(root);
    printf("PASS\\n");
    return 0;
}}
''',
"cpp": '''{H}
struct NNode {{
    int val;
    NNode *left = nullptr, *right = nullptr, *next = nullptr;
    explicit NNode(int v) : val(v) {{}}
}};
static NNode *buildNTree(const std::vector<int> &vals) {{
    if (vals.empty()) return nullptr;
    auto *root = new NNode(vals[0]);
    std::queue<NNode *> q;
    q.push(root);
    size_t i = 1;
    while (!q.empty() && i < vals.size()) {{
        auto *node = q.front();
        q.pop();
        if (i < vals.size()) {{ node->left = new NNode(vals[i]); q.push(node->left); ++i; }}
        if (i < vals.size()) {{ node->right = new NNode(vals[i]); q.push(node->right); ++i; }}
    }}
    return root;
}}
static NNode *connect(NNode *root) {{
    if (!root) return nullptr;
    std::queue<NNode *> q;
    q.push(root);
    while (!q.empty()) {{
        int size = static_cast<int>(q.size());
        NNode *prev = nullptr;
        for (int i = 0; i < size; ++i) {{
            auto *node = q.front();
            q.pop();
            if (prev) prev->next = node;
            prev = node;
            if (node->left) q.push(node->left);
            if (node->right) q.push(node->right);
        }}
    }}
    return root;
}}
int main() {{
    assert(connect(nullptr) == nullptr);
    auto *root = connect(buildNTree({{1, 2, 3, 4, 5, 6, 7}}));
    std::vector<std::vector<int>> levels;
    auto *cur = root;
    while (cur) {{
        std::vector<int> vals;
        for (auto *n = cur; n; n = n->next) vals.push_back(n->val);
        levels.push_back(vals);
        cur = cur->left;
    }}
    assert((levels == std::vector<std::vector<int>>{{{1}, {2, 3}, {4, 5, 6, 7}}}));
    std::cout << "PASS" << std::endl;
    return 0;
}}
''',
"r": '''{H}
NNode <- function(v) {{ e <- new.env(parent = emptyenv()); e$val <- v; e$left <- NULL; e$right <- NULL; e$nxt <- NULL; class(e) <- "NNode"; e }}
build_ntree <- function(vals) {{
  if (length(vals) == 0L) return(NULL)
  root <- NNode(vals[1L])
  q <- list(root); head <- 1L; i <- 2L
  while (head <= length(q) && i <= length(vals)) {{
    node <- q[[head]]; head <- head + 1L
    if (i <= length(vals)) {{ node$left <- NNode(vals[i]); q[[length(q) + 1L]] <- node$left; i <- i + 1L }}
    if (i <= length(vals)) {{ node$right <- NNode(vals[i]); q[[length(q) + 1L]] <- node$right; i <- i + 1L }}
  }}
  root
}}
connect <- function(root) {{
  if (is.null(root)) return(NULL)
  queue <- list(root)
  while (length(queue) > 0) {{
    size <- length(queue)
    prev <- NULL
    for (k in 1:size) {{
      node <- queue[[1L]]
      queue[[1L]] <- NULL
      if (!is.null(prev)) prev$nxt <- node
      prev <- node
      if (!is.null(node$left)) queue[[length(queue) + 1L]] <- node$left
      if (!is.null(node$right)) queue[[length(queue) + 1L]] <- node$right
    }}
  }}
  root
}}
stopifnot(is.null(connect(NULL)))
root <- connect(build_ntree(1:7))
levels <- list()
cur <- root
while (!is.null(cur)) {{
  vals <- integer(0)
  node <- cur
  while (!is.null(node)) {{ vals[[length(vals) + 1L]] <- node$val; node <- node$nxt }}
  levels[[length(levels) + 1L]] <- vals
  cur <- cur$left
}}
stopifnot(identical(levels, list(1L, 2:3, 4:7)))
cat("PASS\\n")
''',
"zig": '''{H}
const NNode = struct {{ val: i32, left: ?*NNode, right: ?*NNode, next: ?*NNode }};
fn nnew(v: i32, alloc: std.mem.Allocator) *NNode {{
    const n = alloc.create(NNode) catch unreachable;
    n.* = .{{ .val = v, .left = null, .right = null, .next = null }};
    return n;
}}
fn buildNTree(vals: []const i32, alloc: std.mem.Allocator) ?*NNode {{
    if (vals.len == 0) return null;
    const root = nnew(vals[0], alloc);
    var q = std.ArrayList(*NNode).init(alloc);
    q.append(root) catch unreachable;
    var head: usize = 0;
    var i: usize = 1;
    while (head < q.items.len and i < vals.len) {{
        const node = q.items[head];
        head += 1;
        if (i < vals.len) {{ const c = nnew(vals[i], alloc); node.left = c; q.append(c) catch unreachable; i += 1; }}
        if (i < vals.len) {{ const c = nnew(vals[i], alloc); node.right = c; q.append(c) catch unreachable; i += 1; }}
    }}
    return root;
}}
fn connect(root: ?*NNode) ?*NNode {{
    const r = root orelse return null;
    var q = std.ArrayList(*NNode).init(std.heap.page_allocator);
    defer q.deinit();
    q.append(r) catch unreachable;
    var head: usize = 0;
    while (head < q.items.len) {{
        const size = q.items.len - head;
        var prev: ?*NNode = null;
        for (0..size) |_| {{
            const node = q.items[head];
            head += 1;
            if (prev) |p| p.next = node;
            prev = node;
            if (node.left) |c| q.append(c) catch unreachable;
            if (node.right) |c| q.append(c) catch unreachable;
        }}
    }}
    return r;
}}
pub fn main() !void {{
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();
    const alloc = arena.allocator();
    if (connect(null) != null) return error.TestFailed;
    const root = connect(buildNTree(&[_]i32{{ 1, 2, 3, 4, 5, 6, 7 }}, alloc)).?;
    var level: usize = 0;
    var cur: ?*NNode = root;
    const want = [_][]const i32{{ &[_]i32{{1}}, &[_]i32{{ 2, 3 }}, &[_]i32{{ 4, 5, 6, 7 }} }};
    while (cur) |c| {{
        var cnt: usize = 0;
        var node: ?*NNode = c;
        while (node) |n| {{
            if (cnt >= want[level].len or n.val != want[level][cnt]) return error.TestFailed;
            cnt += 1;
            node = n.next;
        }}
        if (cnt != want[level].len) return error.TestFailed;
        cur = c.left;
        level += 1;
    }}
    if (level != 3) return error.TestFailed;
    std.debug.print("PASS\\n", .{{}});
}}
''',
"dart": '''{H}
class NNode {
  final int val;
  NNode? left, right, next;
  NNode(this.val);
}
NNode? buildNTree(List<int> vals) {
  if (vals.isEmpty) return null;
  final root = NNode(vals[0]);
  final q = <NNode>[root];
  var head = 0;
  var i = 1;
  while (head < q.length && i < vals.length) {
    final node = q[head++];
    if (i < vals.length) {
      node.left = NNode(vals[i]);
      q.add(node.left!);
      i++;
    }
    if (i < vals.length) {
      node.right = NNode(vals[i]);
      q.add(node.right!);
      i++;
    }
  }
  return root;
}
NNode? connect(NNode? root) {
  if (root == null) return null;
  final q = <NNode>[root];
  var head = 0;
  while (head < q.length) {
    final size = q.length - head;
    NNode? prev;
    for (var k = 0; k < size; k++) {
      final node = q[head++];
      if (prev != null) prev.next = node;
      prev = node;
      if (node.left != null) q.add(node.left!);
      if (node.right != null) q.add(node.right!);
    }
  }
  return root;
}
void main() {
  if (connect(null) != null) throw StateError('c0');
  final root = connect(buildNTree([1, 2, 3, 4, 5, 6, 7]))!;
  final levels = <List<int>>[];
  NNode? cur = root;
  while (cur != null) {
    final vals = <int>[];
    NNode? node = cur;
    while (node != null) {
      vals.add(node.val);
      node = node.next;
    }
    levels.add(vals);
    cur = cur.left;
  }
  if (levels.length != 3) throw StateError('levels');
  if (levels[0].toString() != '[1]' || levels[1].toString() != '[2, 3]' || levels[2].toString() != '[4, 5, 6, 7]') throw StateError('vals');
  print('PASS');
}
''',
}

# 117：O(1) 空间 dummy 链法（节点同 116）
def a117(lang, tmpl):
    return tmpl

A117 = {
"rust": '''{H}
#[derive(Debug)]
struct NNode {{ val: i32, left: Option<Rc<RefCell<NNode>>>, right: Option<Rc<RefCell<NNode>>>, next: Option<Rc<RefCell<NNode>>> }}
impl NNode {{ fn new(v: i32) -> Rc<RefCell<NNode>> {{ Rc::new(RefCell::new(NNode {{ val: v, left: None, right: None, next: None }})) }} }}
fn build_ntree(vals: &[i32]) -> Option<Rc<RefCell<NNode>>> {{
    if vals.is_empty() {{ return None; }}
    let root = NNode::new(vals[0]);
    let mut q = vec![root.clone()];
    let mut i = 1;
    while !q.is_empty() && i < vals.len() {{
        let node = q.remove(0);
        if i < vals.len() {{ let c = NNode::new(vals[i]); node.borrow_mut().left = Some(c.clone()); q.push(c); i += 1; }}
        if i < vals.len() {{ let c = NNode::new(vals[i]); node.borrow_mut().right = Some(c.clone()); q.push(c); i += 1; }}
    }}
    Some(root)
}}
fn connect(root: Option<Rc<RefCell<NNode>>>) -> Option<Rc<RefCell<NNode>>> {{
    let mut cur = match root.clone() {{ Some(x) => x, None => return None }};
    loop {{
        let dummy = NNode::new(0);
        let mut prev = dummy.clone();
        let mut node = Some(cur.clone());
        let mut any = false;
        while let Some(n) = node {{
            let nb = n.borrow();
            if let Some(l) = nb.left.clone() {{
                prev.borrow_mut().next = Some(l.clone());
                prev = l;
                any = true;
            }}
            if let Some(r) = nb.right.clone() {{
                prev.borrow_mut().next = Some(r.clone());
                prev = r;
                any = true;
            }}
            node = nb.next.clone();
        }}
        if !any {{ break; }}
        let nxt = dummy.borrow().next.clone();
        match nxt {{
            Some(n) => cur = n,
            None => break,
        }}
    }}
    root
}}
fn main() {{
    assert!(connect(None).is_none());
    let root = connect(build_ntree(&[1, 2, 3, 4, 5, 6, 7]));
    let mut levels: Vec<Vec<i32>> = Vec::new();
    let mut cur = root.clone();
    while let Some(c) = cur {{
        let mut vals = Vec::new();
        let mut node = Some(c.clone());
        while let Some(n) = node {{
            vals.push(n.borrow().val);
            node = n.borrow().next.clone();
        }}
        levels.push(vals);
        cur = c.borrow().left.clone().or_else(|| c.borrow().right.clone());
        if levels.len() > 5 {{ break; }}
    }}
    assert_eq!(levels, vec![vec![1], vec![2, 3], vec![4, 5, 6, 7]]);
    println!("PASS");
}}
''',
"lua": '''{H}
local NNode = {{}}
NNode.__index = NNode
function NNode.new(v) return setmetatable({{val = v, left = nil, right = nil, next = nil}}, NNode) end
local function build_ntree(vals)
    if #vals == 0 then return nil end
    local root = NNode.new(vals[1])
    local q = {{root}}
    local head, i = 1, 2
    while head <= #q and i <= #vals do
        local node = q[head]
        head = head + 1
        if i <= #vals then node.left = NNode.new(vals[i]); q[#q + 1] = node.left; i = i + 1 end
        if i <= #vals then node.right = NNode.new(vals[i]); q[#q + 1] = node.right; i = i + 1 end
    end
    return root
end
local function connect(root)
    if not root then return nil end
    local cur = root
    while cur do
        local dummy = NNode.new(0)
        local prev = dummy
        local node = cur
        while node do
            if node.left then prev.next = node.left; prev = prev.next end
            if node.right then prev.next = node.right; prev = prev.next end
            node = node.next
        end
        cur = dummy.next
    end
    return root
end
assert(connect(nil) == nil)
local root = connect(build_ntree({{1, 2, 3, 4, 5, 6, 7}}))
local levels = {{}}
local cur = root
while cur do
    local vals = {{}}
    local node = cur
    while node do
        vals[#vals + 1] = node.val
        node = node.next
    end
    levels[#levels + 1] = vals
    cur = cur.left or cur.right
    if #levels > 5 then break end
end
assert(#levels == 3)
assert(#levels[1] == 1 and levels[1][1] == 1)
assert(#levels[2] == 2 and levels[2][1] == 2 and levels[2][2] == 3)
assert(#levels[3] == 4 and levels[3][1] == 4 and levels[3][4] == 7)
print("PASS")
''',
"c": '''{H}
typedef struct NNode {{ int val; struct NNode *left, *right, *next; }} NNode;
static NNode *nnew(int v) {{ NNode *n = calloc(1, sizeof(NNode)); n->val = v; return n; }}
static void free_ntree(NNode *n) {{ if (!n) return; free_ntree(n->left); free_ntree(n->right); free(n); }}
static NNode *build_ntree(const int *vals, int n) {{
    if (n == 0) return NULL;
    NNode *root = nnew(vals[0]);
    NNode *q[256];
    int head = 0, tail = 0, i = 1;
    q[tail++] = root;
    while (head < tail && i < n) {{
        NNode *node = q[head++];
        if (i < n) {{ node->left = nnew(vals[i]); q[tail++] = node->left; i++; }}
        if (i < n) {{ node->right = nnew(vals[i]); q[tail++] = node->right; i++; }}
    }}
    return root;
}}
static NNode *connect(NNode *root) {{
    if (!root) return NULL;
    NNode *cur = root;
    while (cur) {{
        NNode dummy = {{0}};
        NNode *prev = &dummy;
        for (NNode *node = cur; node; node = node->next) {{
            if (node->left) {{ prev->next = node->left; prev = prev->next; }}
            if (node->right) {{ prev->next = node->right; prev = prev->next; }}
        }}
        cur = dummy.next;
    }}
    return root;
}}
int main(void) {{
    int vals[] = {{1,2,3,4,5,6,7}};
    if (connect(NULL) != NULL) {{ printf("FAIL nil\\n"); return 1; }}
    NNode *root = connect(build_ntree(vals, 7));
    int want[3][4] = {{ {{1}}, {{2,3}}, {{4,5,6,7}} }};
    int wantn[3] = {{1, 2, 4}};
    NNode *cur = root;
    int level = 0;
    while (cur && level < 3) {{
        int cnt = 0;
        for (NNode *n = cur; n; n = n->next) {{
            if (cnt >= wantn[level] || n->val != want[level][cnt]) {{ printf("FAIL L%d\\n", level); return 1; }}
            cnt++;
        }}
        if (cnt != wantn[level]) {{ printf("FAIL L%d cnt\\n", level); return 1; }}
        cur = cur->left ? cur->left : cur->right;
        level++;
    }}
    if (level != 3) {{ printf("FAIL levels\\n"); return 1; }}
    free_ntree(root);
    printf("PASS\\n");
    return 0;
}}
''',
"cpp": '''{H}
struct NNode {{
    int val;
    NNode *left = nullptr, *right = nullptr, *next = nullptr;
    explicit NNode(int v) : val(v) {{}}
}};
static NNode *buildNTree(const std::vector<int> &vals) {{
    if (vals.empty()) return nullptr;
    auto *root = new NNode(vals[0]);
    std::queue<NNode *> q;
    q.push(root);
    size_t i = 1;
    while (!q.empty() && i < vals.size()) {{
        auto *node = q.front();
        q.pop();
        if (i < vals.size()) {{ node->left = new NNode(vals[i]); q.push(node->left); ++i; }}
        if (i < vals.size()) {{ node->right = new NNode(vals[i]); q.push(node->right); ++i; }}
    }}
    return root;
}}
static NNode *connect(NNode *root) {{
    if (!root) return nullptr;
    NNode *cur = root;
    while (cur) {{
        NNode dummy(0);
        NNode *prev = &dummy;
        for (NNode *node = cur; node; node = node->next) {{
            if (node->left) {{ prev->next = node->left; prev = prev->next; }}
            if (node->right) {{ prev->next = node->right; prev = prev->next; }}
        }}
        cur = dummy.next;
    }}
    return root;
}}
int main() {{
    assert(connect(nullptr) == nullptr);
    auto *root = connect(buildNTree({{1, 2, 3, 4, 5, 6, 7}}));
    std::vector<std::vector<int>> levels;
    auto *cur = root;
    while (cur && levels.size() < 5) {{
        std::vector<int> vals;
        for (auto *n = cur; n; n = n->next) vals.push_back(n->val);
        levels.push_back(vals);
        cur = cur->left ? cur->left : cur->right;
    }}
    assert((levels == std::vector<std::vector<int>>{{{1}, {2, 3}, {4, 5, 6, 7}}}));
    std::cout << "PASS" << std::endl;
    return 0;
}}
''',
"r": '''{H}
NNode <- function(v) {{ e <- new.env(parent = emptyenv()); e$val <- v; e$left <- NULL; e$right <- NULL; e$nxt <- NULL; class(e) <- "NNode"; e }}
build_ntree <- function(vals) {{
  if (length(vals) == 0L) return(NULL)
  root <- NNode(vals[1L])
  q <- list(root); head <- 1L; i <- 2L
  while (head <= length(q) && i <= length(vals)) {{
    node <- q[[head]]; head <- head + 1L
    if (i <= length(vals)) {{ node$left <- NNode(vals[i]); q[[length(q) + 1L]] <- node$left; i <- i + 1L }}
    if (i <= length(vals)) {{ node$right <- NNode(vals[i]); q[[length(q) + 1L]] <- node$right; i <- i + 1L }}
  }}
  root
}}
connect <- function(root) {{
  if (is.null(root)) return(NULL)
  cur <- root
  while (!is.null(cur)) {{
    dummy <- NNode(0L)
    prev <- dummy
    node <- cur
    while (!is.null(node)) {{
      if (!is.null(node$left)) {{ prev$nxt <- node$left; prev <- prev$nxt }}
      if (!is.null(node$right)) {{ prev$nxt <- node$right; prev <- prev$nxt }}
      node <- node$nxt
    }}
    cur <- dummy$nxt
  }}
  root
}}
stopifnot(is.null(connect(NULL)))
root <- connect(build_ntree(1:7))
levels <- list()
cur <- root
while (!is.null(cur) && length(levels) < 5L) {{
  vals <- integer(0)
  node <- cur
  while (!is.null(node)) {{ vals[[length(vals) + 1L]] <- node$val; node <- node$nxt }}
  levels[[length(levels) + 1L]] <- vals
  cur <- if (!is.null(cur$left)) cur$left else cur$right
}}
stopifnot(identical(levels, list(1L, 2:3, 4:7)))
cat("PASS\\n")
''',
"zig": '''{H}
const NNode = struct {{ val: i32, left: ?*NNode, right: ?*NNode, next: ?*NNode }};
fn nnew(v: i32, alloc: std.mem.Allocator) *NNode {{
    const n = alloc.create(NNode) catch unreachable;
    n.* = .{{ .val = v, .left = null, .right = null, .next = null }};
    return n;
}}
fn buildNTree(vals: []const i32, alloc: std.mem.Allocator) ?*NNode {{
    if (vals.len == 0) return null;
    const root = nnew(vals[0], alloc);
    var q = std.ArrayList(*NNode).init(alloc);
    q.append(root) catch unreachable;
    var head: usize = 0;
    var i: usize = 1;
    while (head < q.items.len and i < vals.len) {{
        const node = q.items[head];
        head += 1;
        if (i < vals.len) {{ const c = nnew(vals[i], alloc); node.left = c; q.append(c) catch unreachable; i += 1; }}
        if (i < vals.len) {{ const c = nnew(vals[i], alloc); node.right = c; q.append(c) catch unreachable; i += 1; }}
    }}
    return root;
}}
fn connect(root: ?*NNode) ?*NNode {{
    var cur = root orelse return null;
    while (true) {{
        var dummy = NNode{{ .val = 0, .left = null, .right = null, .next = null }};
        var prev: *NNode = &dummy;
        var node: ?*NNode = cur;
        while (node) |n| {{
            if (n.left) |l| {{ prev.next = l; prev = l; }}
            if (n.right) |r| {{ prev.next = r; prev = r; }}
            node = n.next;
        }}
        cur = dummy.next orelse break;
    }}
    return root;
}}
pub fn main() !void {{
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();
    const alloc = arena.allocator();
    if (connect(null) != null) return error.TestFailed;
    const root = connect(buildNTree(&[_]i32{{ 1, 2, 3, 4, 5, 6, 7 }}, alloc)).?;
    var level: usize = 0;
    var cur: ?*NNode = root;
    const want = [_][]const i32{{ &[_]i32{{1}}, &[_]i32{{ 2, 3 }}, &[_]i32{{ 4, 5, 6, 7 }} }};
    while (cur != null and level < 3) {{
        var cnt: usize = 0;
        var node: ?*NNode = cur;
        while (node) |n| {{
            if (cnt >= want[level].len or n.val != want[level][cnt]) return error.TestFailed;
            cnt += 1;
            node = n.next;
        }}
        if (cnt != want[level].len) return error.TestFailed;
        const c = cur.?;
        cur = if (c.left) |l| l else c.right;
        level += 1;
    }}
    if (level != 3) return error.TestFailed;
    std.debug.print("PASS\\n", .{{}});
}}
''',
"dart": '''{H}
class NNode {
  final int val;
  NNode? left, right, next;
  NNode(this.val);
}
NNode? buildNTree(List<int> vals) {
  if (vals.isEmpty) return null;
  final root = NNode(vals[0]);
  final q = <NNode>[root];
  var head = 0;
  var i = 1;
  while (head < q.length && i < vals.length) {
    final node = q[head++];
    if (i < vals.length) {
      node.left = NNode(vals[i]);
      q.add(node.left!);
      i++;
    }
    if (i < vals.length) {
      node.right = NNode(vals[i]);
      q.add(node.right!);
      i++;
    }
  }
  return root;
}
NNode? connect(NNode? root) {
  if (root == null) return null;
  NNode? cur = root;
  while (cur != null) {
    final dummy = NNode(0);
    var prev = dummy;
    NNode? node = cur;
    while (node != null) {
      if (node.left != null) {
        prev.next = node.left;
        prev = prev.next!;
      }
      if (node.right != null) {
        prev.next = node.right;
        prev = prev.next!;
      }
      node = node.next;
    }
    cur = dummy.next;
  }
  return root;
}
void main() {
  if (connect(null) != null) throw StateError('c0');
  final root = connect(buildNTree([1, 2, 3, 4, 5, 6, 7]))!;
  final levels = <List<int>>[];
  NNode? cur = root;
  while (cur != null && levels.length < 5) {
    final vals = <int>[];
    NNode? node = cur;
    while (node != null) {
      vals.add(node.val);
      node = node.next;
    }
    levels.add(vals);
    cur = cur.left ?? cur.right;
  }
  if (levels.length != 3) throw StateError('levels');
  if (levels[0].toString() != '[1]' || levels[1].toString() != '[2, 3]' || levels[2].toString() != '[4, 5, 6, 7]') throw StateError('vals');
  print('PASS');
}
''',
}

PROBS = [
    ("lc_109_有序链表转换二叉搜索树", A109, "LeetCode 109. 有序链表转换二叉搜索树"),
    ("lc_114_二叉树展开为链表", A114, "LeetCode 114. 二叉树展开为链表"),
    ("lc_116_填充每个节点的下一个右侧节点指针", A116, "LeetCode 116. 填充每个节点的下一个右侧节点指针"),
    ("lc_117_填充每个节点的下一个右侧节点指针_ii", A117, "LeetCode 117. 填充每个节点的下一个右侧节点指针 II"),
]
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
