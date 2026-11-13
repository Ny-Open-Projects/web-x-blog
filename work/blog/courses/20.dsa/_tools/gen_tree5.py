#!/usr/bin/env python3
# gen_tree5.py — tree 第五批：lc_108/lc_654/lc_701/lc_112/lc_113 × 7语言
import sys, os; sys.path.insert(0, "/Users/Wang/Code/github/web-x-blog/work/blog/courses/20.dsa/_tools")
from langlib import emit, TREE_H, head_comment, EXT

B = {"108": "144993168", "654": "135911085", "701": "137040405", "112": "135991021", "113": "136044710"}
LANGNAME = {"rust": "Rust", "lua": "Lua", "c": "C", "cpp": "C++", "r": "R", "zig": "Zig", "dart": "Dart"}

# 需要相同树比较（108）与层序比较（701）
SAME = {
"rust": '''fn same_tree(p: Option<&Rc<RefCell<TreeNode>>>, q: Option<&Rc<RefCell<TreeNode>>>) -> bool {
    match (p, q) {
        (None, None) => true,
        (Some(a), Some(b)) => { let (a, b) = (a.borrow(), b.borrow()); a.val == b.val && same_tree(a.left.as_ref(), b.left.as_ref()) && same_tree(a.right.as_ref(), b.right.as_ref()) }
        _ => false,
    }
}
fn levels_flat(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<i32> {
    let mut out = Vec::new();
    let mut q: Vec<Rc<RefCell<TreeNode>>> = root.into_iter().collect();
    while !q.is_empty() {
        let mut nxt = Vec::new();
        for n in q { let b = n.borrow(); out.push(b.val); if let Some(c)=b.left.clone() {nxt.push(c);} if let Some(c)=b.right.clone() {nxt.push(c);} }
        q = nxt;
    }
    out
}
''',
"lua": '''local function same_tree(p, q)
    if not p and not q then return true end
    if not p or not q or p.val ~= q.val then return false end
    return same_tree(p.left, q.left) and same_tree(p.right, q.right)
end
local function levels_flat(root)
    if not root then return {} end
    local out, q = {}, {root}
    while #q > 0 do
        local n = #q
        for _ = 1, n do
            local node = table.remove(q, 1)
            out[#out + 1] = node.val
            if node.left then q[#q + 1] = node.left end
            if node.right then q[#q + 1] = node.right end
        end
    end
    return out
end
local function eq(a, b)
    if #a ~= #b then return false end
    for i = 1, #a do if a[i] ~= b[i] then return false end end
    return true
end
''',
"c": '''static int same_tree(const TreeNode *p, const TreeNode *q) {
    if (!p && !q) return 1;
    if (!p || !q || p->val != q->val) return 0;
    return same_tree(p->left, q->left) && same_tree(p->right, q->right);
}
static int levels_flat(TreeNode *root, int out[]) {
    if (!root) return 0;
    TreeNode *q[4096]; int head = 0, tail = 0, cnt = 0;
    q[tail++] = root;
    while (head < tail) {
        TreeNode *n = q[head++];
        out[cnt++] = n->val;
        if (n->left) q[tail++] = n->left;
        if (n->right) q[tail++] = n->right;
    }
    return cnt;
}
static int eqarr(const int *a, int n, const int *b, int m) {
    if (n != m) return 0;
    for (int i = 0; i < n; i++) if (a[i] != b[i]) return 0;
    return 1;
}
''',
"cpp": '''static bool sameTree(const TreeNode *p, const TreeNode *q) {
    if (!p && !q) return true;
    if (!p || !q || p->val != q->val) return false;
    return sameTree(p->left, q->left) && sameTree(p->right, q->right);
}
static std::vector<int> levelsFlat(TreeNode *root) {
    std::vector<int> out;
    if (!root) return out;
    std::queue<TreeNode *> q;
    q.push(root);
    while (!q.empty()) {
        auto *n = q.front(); q.pop();
        out.push_back(n->val);
        if (n->left) q.push(n->left);
        if (n->right) q.push(n->right);
    }
    return out;
}
''',
"r": '''same_tree <- function(p, q) {
  if (is.null(p) && is.null(q)) return(TRUE)
  if (is.null(p) || is.null(q) || p$val != q$val) return(FALSE)
  same_tree(p$left, q$left) && same_tree(p$right, q$right)
}
levels_flat <- function(root) unlist(tree_to_levels(root))
''',
"zig": '''fn sameTree(p: ?*const TreeNode, q: ?*const TreeNode) bool {
    if (p == null and q == null) return true;
    if (p == null or q == null) return false;
    const a = p.?;
    const b = q.?;
    return a.val == b.val and sameTree(a.left, b.left) and sameTree(a.right, b.right);
}
fn levelsFlat(root: ?*TreeNode, out: *std.ArrayList(i32)) void {
    const r = root orelse return;
    var q = std.ArrayList(*TreeNode).init(std.heap.page_allocator);
    defer q.deinit();
    q.append(r) catch unreachable;
    var head: usize = 0;
    while (head < q.items.len) {
        const node = q.items[head];
        head += 1;
        out.append(node.val) catch unreachable;
        if (node.left) |c| q.append(c) catch unreachable;
        if (node.right) |c| q.append(c) catch unreachable;
    }
}
''',
"dart": '''bool sameTree(TreeNode? p, TreeNode? q) {
  if (p == null && q == null) return true;
  if (p == null || q == null || p.val != q.val) return false;
  return sameTree(p.left, q.left) && sameTree(p.right, q.right);
}
List<int> levelsFlat(TreeNode? root) {
  if (root == null) return [];
  final out = <int>[];
  final q = <TreeNode>[root];
  var head = 0;
  while (head < q.length) {
    final n = q[head++];
    out.add(n.val);
    if (n.left != null) q.add(n.left!);
    if (n.right != null) q.add(n.right!);
  }
  return out;
}
''',
}

A108 = {
"rust": '''{H}{S}
fn helper(nums: &[i32], left: usize, right: isize) -> Option<Rc<RefCell<TreeNode>>> {{
    if left as isize > right {{ return None; }}
    let mid = (left as isize + (right - left as isize) / 2) as usize;
    let root = TreeNode::new(nums[mid]);
    root.borrow_mut().left = helper(nums, left, mid as isize - 1);
    root.borrow_mut().right = helper(nums, mid + 1, right);
    Some(root)
}}
fn sorted_array_to_bst(nums: Vec<i32>) -> Option<Rc<RefCell<TreeNode>>> {{
    if nums.is_empty() {{ return None; }}
    helper(&nums, 0, nums.len() as isize - 1)
}}
fn main() {{
    let got = sorted_array_to_bst(vec![-10, -3, 0, 5, 9]);
    let want = build_tree(&[Some(0), Some(-10), Some(5), None, Some(-3), None, Some(9)]);
    assert!(same_tree(got.as_ref(), want.as_ref()));
    assert!(same_tree(sorted_array_to_bst(vec![1]).as_ref(), build_tree(&[Some(1)]).as_ref()));
    assert!(sorted_array_to_bst(vec![]).is_none());
    println!("PASS");
}}
''',
"lua": '''{H}{S}
local function helper(nums, left, right)
    if left > right then return nil end
    local mid = left + math.floor((right - left) / 2)
    local root = TreeNode.new(nums[mid])
    root.left = helper(nums, left, mid - 1)
    root.right = helper(nums, mid + 1, right)
    return root
end
local function sorted_array_to_bst(nums)
    if #nums == 0 then return nil end
    return helper(nums, 1, #nums)
end
assert(same_tree(sorted_array_to_bst({{-10, -3, 0, 5, 9}}), build_tree({{0, -10, 5, "null", -3, "null", 9}})))
assert(same_tree(sorted_array_to_bst({{1}}), build_tree({{1}})))
assert(sorted_array_to_bst({{}}) == nil)
print("PASS")
''',
"c": '''{H}{S}
static TreeNode *helper(const int *nums, int left, int right) {{
    if (left > right) return NULL;
    int mid = left + (right - left) / 2;
    TreeNode *root = malloc(sizeof(TreeNode));
    root->val = nums[mid]; root->left = root->right = NULL;
    root->left = helper(nums, left, mid - 1);
    root->right = helper(nums, mid + 1, right);
    return root;
}}
static TreeNode *sorted_array_to_bst(const int *nums, int n) {{
    if (n == 0) return NULL;
    return helper(nums, 0, n - 1);
}}
int main(void) {{
    int in1[] = {{-10,-3,0,5,9}};
    int w1[] = {{0,-10,5,INT_MIN_SN,-3,INT_MIN_SN,9}};
    TreeNode *got = sorted_array_to_bst(in1, 5);
    TreeNode *want = build_tree(w1, 7);
    if (!same_tree(got, want)) {{ printf("FAIL 1\\n"); return 1; }}
    int in2[] = {{1}};
    TreeNode *got2 = sorted_array_to_bst(in2, 1);
    int w2[] = {{1}};
    if (!same_tree(got2, build_tree(w2, 1))) {{ printf("FAIL 2\\n"); return 1; }}
    if (sorted_array_to_bst(NULL, 0) != NULL) {{ printf("FAIL 3\\n"); return 1; }}
    printf("PASS\\n");
    return 0;
}}
''',
"cpp": '''{H}{S}
static TreeNode *helper(const std::vector<int> &nums, int left, int right) {{
    if (left > right) return nullptr;
    int mid = left + (right - left) / 2;
    auto *root = new TreeNode(nums[mid]);
    root->left = helper(nums, left, mid - 1);
    root->right = helper(nums, mid + 1, right);
    return root;
}}
static TreeNode *sortedArrayToBST(const std::vector<int> &nums) {{
    if (nums.empty()) return nullptr;
    return helper(nums, 0, static_cast<int>(nums.size()) - 1);
}}
int main() {{
    assert(sameTree(sortedArrayToBST({{-10, -3, 0, 5, 9}}), build_tree({{0, -10, 5, std::nullopt, -3, std::nullopt, 9}})));
    assert(sameTree(sortedArrayToBST({{1}}), build_tree({{1}})));
    assert(sortedArrayToBST({{}}) == nullptr);
    std::cout << "PASS" << std::endl;
    return 0;
}}
''',
"r": '''{H}{S}
helper <- function(nums, left, right) {{
  if (left > right) return(NULL)
  mid <- left + (right - left) %/% 2L
  root <- TreeNode(nums[mid])
  root$left <- helper(nums, left, mid - 1L)
  root$right <- helper(nums, mid + 1L, right)
  root
}}
sorted_array_to_bst <- function(nums) {{
  if (length(nums) == 0L) return(NULL)
  helper(nums, 1L, length(nums))
}}
stopifnot(same_tree(sorted_array_to_bst(c(-10L, -3L, 0L, 5L, 9L)), build_tree(list(0L, -10L, 5L, NA, -3L, NA, 9L))))
stopifnot(same_tree(sorted_array_to_bst(1L), build_tree(list(1L))))
stopifnot(is.null(sorted_array_to_bst(integer(0))))
cat("PASS\\n")
''',
"zig": '''{H}{S}
fn helper(nums: []const i32, left: isize, right: isize, alloc: std.mem.Allocator) !?*TreeNode {{
    if (left > right) return null;
    const mid = left + @divTrunc(right - left, 2);
    const root = try alloc.create(TreeNode);
    root.* = .{{ .val = nums[@intCast(mid)], .left = null, .right = null }};
    root.left = try helper(nums, left, mid - 1, alloc);
    root.right = try helper(nums, mid + 1, right, alloc);
    return root;
}}
fn sortedArrayToBST(nums: []const i32, alloc: std.mem.Allocator) !?*TreeNode {{
    if (nums.len == 0) return null;
    return helper(nums, 0, @as(isize, @intCast(nums.len)) - 1, alloc);
}}
pub fn main() !void {{
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();
    const alloc = arena.allocator();
    const got = try sortedArrayToBST(&[_]i32{{ -10, -3, 0, 5, 9 }}, alloc);
    const want = try buildTree(alloc, &[_]i32{{ 0, -10, 5, -1, -3, -1, 9 }});
    if (!sameTree(got, want)) return error.TestFailed;
    const got2 = try sortedArrayToBST(&[_]i32{{1}}, alloc);
    const want2 = try buildTree(alloc, &[_]i32{{1}});
    if (!sameTree(got2, want2)) return error.TestFailed;
    if ((try sortedArrayToBST(&[_]i32{{}}, alloc)) != null) return error.TestFailed;
    std.debug.print("PASS\\n", .{{}});
}}
''',
"dart": '''{H}{S}
TreeNode? helper(List<int> nums, int left, int right) {{
  if (left > right) return null;
  final mid = left + (right - left) ~/ 2;
  final root = TreeNode(nums[mid]);
  root.left = helper(nums, left, mid - 1);
  root.right = helper(nums, mid + 1, right);
  return root;
}}
TreeNode? sortedArrayToBST(List<int> nums) {{
  if (nums.isEmpty) return null;
  return helper(nums, 0, nums.length - 1);
}}
void main() {{
  if (!sameTree(sortedArrayToBST([-10, -3, 0, 5, 9]), buildTree([0, -10, 5, null, -3, null, 9]))) throw StateError('c1');
  if (!sameTree(sortedArrayToBST([1]), buildTree([1]))) throw StateError('c2');
  if (sortedArrayToBST([]) != null) throw StateError('c3');
  print('PASS');
}}
''',
}

A654 = {
"rust": '''{H}{S}
fn construct_maximum_binary_tree(nums: &[i32]) -> Option<Rc<RefCell<TreeNode>>> {{
    if nums.is_empty() {{ return None; }}
    let mut idx = 0;
    for i in 0..nums.len() {{
        if nums[i] > nums[idx] {{ idx = i; }}
    }}
    let root = TreeNode::new(nums[idx]);
    root.borrow_mut().left = construct_maximum_binary_tree(&nums[..idx]);
    root.borrow_mut().right = construct_maximum_binary_tree(&nums[idx + 1..]);
    Some(root)
}}
fn main() {{
    let t = construct_maximum_binary_tree(&[3, 2, 1, 6, 0, 5]);
    assert_eq!(t.as_ref().unwrap().borrow().val, 6);
    assert_eq!(construct_maximum_binary_tree(&[1]).unwrap().borrow().val, 1);
    assert_eq!(construct_maximum_binary_tree(&[3, 2, 1]).unwrap().borrow().val, 3);
    assert!(construct_maximum_binary_tree(&[]).is_none());
    // 完整结构验证：LC 官方 [3,2,1,6,0,5] → 根6, 左[3,2,1]构造, 右[0,5]构造
    let want = build_tree(&[Some(6), Some(3), Some(5), None, Some(2), Some(0), None, None, Some(1), None, None]);
    assert!(same_tree(t.as_ref(), want.as_ref()));
    println!("PASS");
}}
''',
"lua": '''{H}{S}
local function construct_maximum_binary_tree(nums)
    if #nums == 0 then return nil end
    local idx = 1
    for i = 1, #nums do
        if nums[i] > nums[idx] then idx = i end
    end
    local root = TreeNode.new(nums[idx])
    local left, right = {{}}, {{}}
    for i = 1, idx - 1 do left[#left + 1] = nums[i] end
    for i = idx + 1, #nums do right[#right + 1] = nums[i] end
    root.left = construct_maximum_binary_tree(left)
    root.right = construct_maximum_binary_tree(right)
    return root
end
local t = construct_maximum_binary_tree({{3, 2, 1, 6, 0, 5}})
assert(t.val == 6)
assert(same_tree(t, build_tree({{6, 3, 5, "null", 2, 0, "null", "null", 1, "null", "null"}})))
assert(construct_maximum_binary_tree({{1}}).val == 1)
assert(construct_maximum_binary_tree({{3, 2, 1}}).val == 3)
assert(construct_maximum_binary_tree({{}}) == nil)
print("PASS")
''',
"c": '''{H}{S}
static TreeNode *construct_maximum_binary_tree(const int *nums, int n) {{
    if (n == 0) return NULL;
    int idx = 0;
    for (int i = 0; i < n; i++) if (nums[i] > nums[idx]) idx = i;
    TreeNode *root = malloc(sizeof(TreeNode));
    root->val = nums[idx]; root->left = root->right = NULL;
    root->left = construct_maximum_binary_tree(nums, idx);
    root->right = construct_maximum_binary_tree(nums + idx + 1, n - idx - 1);
    return root;
}}
int main(void) {{
    int v[] = {{3,2,1,6,0,5}};
    int w[] = {{6,3,5,INT_MIN_SN,2,0,INT_MIN_SN,INT_MIN_SN,1,INT_MIN_SN,INT_MIN_SN}};
    TreeNode *t = construct_maximum_binary_tree(v, 6);
    if (t->val != 6) {{ printf("FAIL root\\n"); return 1; }}
    if (!same_tree(t, build_tree(w, 10))) {{ printf("FAIL shape\\n"); return 1; }}
    int v2[] = {{1}};
    if (construct_maximum_binary_tree(v2, 1)->val != 1) {{ printf("FAIL 2\\n"); return 1; }}
    int v3[] = {{3,2,1}};
    if (construct_maximum_binary_tree(v3, 3)->val != 3) {{ printf("FAIL 3\\n"); return 1; }}
    if (construct_maximum_binary_tree(NULL, 0) != NULL) {{ printf("FAIL 4\\n"); return 1; }}
    printf("PASS\\n");
    return 0;
}}
''',
"cpp": '''{H}{S}
static TreeNode *constructMaximumBinaryTree(const std::vector<int> &nums) {{
    if (nums.empty()) return nullptr;
    int idx = 0;
    for (int i = 0; i < static_cast<int>(nums.size()); ++i) if (nums[i] > nums[idx]) idx = i;
    auto *root = new TreeNode(nums[idx]);
    root->left = constructMaximumBinaryTree(std::vector<int>(nums.begin(), nums.begin() + idx));
    root->right = constructMaximumBinaryTree(std::vector<int>(nums.begin() + idx + 1, nums.end()));
    return root;
}}
int main() {{
    auto *t = constructMaximumBinaryTree({{3, 2, 1, 6, 0, 5}});
    assert(t->val == 6);
    assert(sameTree(t, build_tree({{6, 3, 5, std::nullopt, 2, 0, std::nullopt, std::nullopt, 1, std::nullopt, std::nullopt}})));
    assert(constructMaximumBinaryTree({{1}})->val == 1);
    assert(constructMaximumBinaryTree({{3, 2, 1}})->val == 3);
    assert(constructMaximumBinaryTree({{}}) == nullptr);
    std::cout << "PASS" << std::endl;
    return 0;
}}
''',
"r": '''{H}{S}
construct_maximum_binary_tree <- function(nums) {{
  if (length(nums) == 0L) return(NULL)
  idx <- which.max(nums)
  root <- TreeNode(nums[idx])
  root$left <- if (idx > 1L) construct_maximum_binary_tree(nums[1:(idx - 1L)]) else NULL
  root$right <- if (idx < length(nums)) construct_maximum_binary_tree(nums[(idx + 1L):length(nums)]) else NULL
  root
}}
t <- construct_maximum_binary_tree(c(3L, 2L, 1L, 6L, 0L, 5L))
stopifnot(t$val == 6L)
stopifnot(same_tree(t, build_tree(list(6L, 3L, 5L, NA, 2L, 0L, NA, NA, 1L, NA, NA))))
stopifnot(construct_maximum_binary_tree(1L)$val == 1L)
stopifnot(construct_maximum_binary_tree(c(3L, 2L, 1L))$val == 3L)
stopifnot(is.null(construct_maximum_binary_tree(integer(0))))
cat("PASS\\n")
''',
"zig": '''{H}{S}
fn constructMaximumBinaryTree(nums: []const i32, alloc: std.mem.Allocator) !?*TreeNode {{
    if (nums.len == 0) return null;
    var idx: usize = 0;
    for (nums, 0..) |v, i| {{
        if (v > nums[idx]) idx = i;
    }}
    const root = try alloc.create(TreeNode);
    root.* = .{{ .val = nums[idx], .left = null, .right = null }};
    root.left = try constructMaximumBinaryTree(nums[0..idx], alloc);
    root.right = try constructMaximumBinaryTree(nums[idx + 1 ..], alloc);
    return root;
}}
pub fn main() !void {{
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();
    const alloc = arena.allocator();
    const t = try constructMaximumBinaryTree(&[_]i32{{ 3, 2, 1, 6, 0, 5 }}, alloc);
    if (t.?.val != 6) return error.TestFailed;
    const want = try buildTree(alloc, &[_]i32{{ 6, 3, 5, -1, 2, 0, -1, -1, 1, -1, -1 }});
    if (!sameTree(t, want)) return error.TestFailed;
    const t2 = try constructMaximumBinaryTree(&[_]i32{{1}}, alloc);
    if (t2.?.val != 1) return error.TestFailed;
    const t3 = try constructMaximumBinaryTree(&[_]i32{{ 3, 2, 1 }}, alloc);
    if (t3.?.val != 3) return error.TestFailed;
    if ((try constructMaximumBinaryTree(&[_]i32{{}}, alloc)) != null) return error.TestFailed;
    std.debug.print("PASS\\n", .{{}});
}}
''',
"dart": '''{H}{S}
TreeNode? constructMaximumBinaryTree(List<int> nums) {{
  if (nums.isEmpty) return null;
  var idx = 0;
  for (var i = 0; i < nums.length; i++) {{
    if (nums[i] > nums[idx]) idx = i;
  }}
  final root = TreeNode(nums[idx]);
  root.left = constructMaximumBinaryTree(nums.sublist(0, idx));
  root.right = constructMaximumBinaryTree(nums.sublist(idx + 1));
  return root;
}}
void main() {{
  final t = constructMaximumBinaryTree([3, 2, 1, 6, 0, 5]);
  if (t!.val != 6) throw StateError('c1');
  if (!sameTree(t, buildTree([6, 3, 5, null, 2, 0, null, null, 1, null, null]))) throw StateError('c2');
  if (constructMaximumBinaryTree([1])!.val != 1) throw StateError('c3');
  if (constructMaximumBinaryTree([3, 2, 1])!.val != 3) throw StateError('c4');
  if (constructMaximumBinaryTree([]) != null) throw StateError('c5');
  print('PASS');
}}
''',
}

A701 = {
"rust": '''{H}{S}
fn insert_into_bst(root: Option<Rc<RefCell<TreeNode>>>, val: i32) -> Option<Rc<RefCell<TreeNode>>> {{
    match root {{
        None => Some(TreeNode::new(val)),
        Some(node) => {{
            let mut pos = node.clone();
            loop {{
                let (go_left, child) = {{
                    let pb = pos.borrow();
                    if val < pb.val {{ (true, pb.left.clone()) }} else {{ (false, pb.right.clone()) }}
                }};
                match child {{
                    Some(c) => pos = c,
                    None => {{
                        let mut pm = pos.borrow_mut();
                        if go_left {{ pm.left = Some(TreeNode::new(val)); }} else {{ pm.right = Some(TreeNode::new(val)); }}
                        break;
                    }}
                }}
            }}
            Some(node)
        }}
    }}
}}
fn main() {{
    let t = build_tree(&[Some(4), Some(2), Some(7), Some(1), Some(3)]);
    let got = levels_flat(insert_into_bst(t, 5));
    assert_eq!(got, vec![4, 2, 7, 1, 3, 5]);
    let got2 = insert_into_bst(None, 5);
    assert_eq!(levels_flat(got2), vec![5]);
    println!("PASS");
}}
''',
"lua": '''{H}{S}
local function insert_into_bst(root, val)
    if not root then return TreeNode.new(val) end
    local pos = root
    while pos do
        if val < pos.val then
            if not pos.left then pos.left = TreeNode.new(val); break end
            pos = pos.left
        else
            if not pos.right then pos.right = TreeNode.new(val); break end
            pos = pos.right
        end
    end
    return root
end
local t = build_tree({{4, 2, 7, 1, 3}})
assert(eq(levels_flat(insert_into_bst(t, 5)), {{4, 2, 7, 1, 3, 5}}))
assert(eq(levels_flat(insert_into_bst(nil, 5)), {{5}}))
print("PASS")
''',
"c": '''{H}{S}
static TreeNode *insert_into_bst(TreeNode *root, int val) {{
    if (!root) {{
        TreeNode *n = malloc(sizeof(TreeNode));
        n->val = val; n->left = n->right = NULL;
        return n;
    }}
    TreeNode *pos = root;
    while (pos) {{
        if (val < pos->val) {{
            if (!pos->left) {{ pos->left = malloc(sizeof(TreeNode)); pos->left->val = val; pos->left->left = pos->left->right = NULL; break; }}
            pos = pos->left;
        }} else {{
            if (!pos->right) {{ pos->right = malloc(sizeof(TreeNode)); pos->right->val = val; pos->right->left = pos->right->right = NULL; break; }}
            pos = pos->right;
        }}
    }}
    return root;
}}
int main(void) {{
    int v[] = {{4,2,7,1,3}};
    int w[] = {{4,2,7,1,3,5}};
    int out[64];
    int n = levels_flat(insert_into_bst(build_tree(v, 5), 5), out);
    if (!eqarr(out, n, w, 6)) {{ printf("FAIL 1\\n"); return 1; }}
    int n2 = levels_flat(insert_into_bst(NULL, 5), out);
    if (!eqarr(out, n2, w + 5, 1)) {{ printf("FAIL 2\\n"); return 1; }}
    printf("PASS\\n");
    return 0;
}}
''',
"cpp": '''{H}{S}
static TreeNode *insertIntoBST(TreeNode *root, int val) {{
    if (!root) return new TreeNode(val);
    TreeNode *pos = root;
    while (pos) {{
        if (val < pos->val) {{
            if (!pos->left) {{ pos->left = new TreeNode(val); break; }}
            pos = pos->left;
        }} else {{
            if (!pos->right) {{ pos->right = new TreeNode(val); break; }}
            pos = pos->right;
        }}
    }}
    return root;
}}
int main() {{
    assert((levelsFlat(insertIntoBST(build_tree({{4, 2, 7, 1, 3}}), 5)) == std::vector<int>{{4, 2, 7, 1, 3, 5}}));
    assert((levelsFlat(insertIntoBST(nullptr, 5)) == std::vector<int>{{5}}));
    std::cout << "PASS" << std::endl;
    return 0;
}}
''',
"r": '''{H}{S}
insert_into_bst <- function(root, val) {{
  if (is.null(root)) return(TreeNode(val))
  pos <- root
  repeat {{
    if (val < pos$val) {{
      if (is.null(pos$left)) {{ pos$left <- TreeNode(val); break }}
      pos <- pos$left
    }} else {{
      if (is.null(pos$right)) {{ pos$right <- TreeNode(val); break }}
      pos <- pos$right
    }}
  }}
  root
}}
stopifnot(identical(levels_flat(insert_into_bst(build_tree(list(4L, 2L, 7L, 1L, 3L)), 5L)), c(4L, 2L, 7L, 1L, 3L, 5L)))
stopifnot(identical(levels_flat(insert_into_bst(NULL, 5L)), 5L))
cat("PASS\\n")
''',
"zig": '''{H}{S}
fn insertIntoBST(root: ?*TreeNode, val: i32, alloc: std.mem.Allocator) ?*TreeNode {
    const r = root orelse {
        const n = alloc.create(TreeNode) catch unreachable;
        n.* = .{ .val = val, .left = null, .right = null };
        return n;
    };
    var pos: *TreeNode = r;
    while (true) {
        if (val < pos.val) {
            if (pos.left) |c| { pos = c; } else {
                const n = alloc.create(TreeNode) catch unreachable;
                n.* = .{ .val = val, .left = null, .right = null };
                pos.left = n;
                break;
            }
        } else {
            if (pos.right) |c| { pos = c; } else {
                const n = alloc.create(TreeNode) catch unreachable;
                n.* = .{ .val = val, .left = null, .right = null };
                pos.right = n;
                break;
            }
        }
    }
    return r;
}
pub fn main() !void {{
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();
    const alloc = arena.allocator();
    var out = std.ArrayList(i32).init(std.heap.page_allocator);
    defer out.deinit();
    const t = try buildTree(alloc, &[_]i32{{ 4, 2, 7, 1, 3 }});
    levelsFlat(insertIntoBST(t, 5, alloc), &out);
    const want = [_]i32{{ 4, 2, 7, 1, 3, 5 }};
    if (out.items.len != want.len) return error.TestFailed;
    for (want, 0..) |w, i| if (out.items[i] != w) return error.TestFailed;
    out.clearRetainingCapacity();
    levelsFlat(insertIntoBST(null, 5, alloc), &out);
    if (out.items.len != 1 or out.items[0] != 5) return error.TestFailed;
    std.debug.print("PASS\\n", .{{}});
}}
''',
"dart": '''{H}{S}
TreeNode? insertIntoBST(TreeNode? root, int val) {{
  if (root == null) return TreeNode(val);
  var pos = root;
  while (true) {{
    if (val < pos.val) {{
      if (pos.left == null) {{
        pos.left = TreeNode(val);
        break;
      }}
      pos = pos.left!;
    }} else {{
      if (pos.right == null) {{
        pos.right = TreeNode(val);
        break;
      }}
      pos = pos.right!;
    }}
  }}
  return root;
}}
void main() {{
  if (levelsFlat(insertIntoBST(buildTree([4, 2, 7, 1, 3]), 5)).toString() != '[4, 2, 7, 1, 3, 5]') throw StateError('c1');
  if (levelsFlat(insertIntoBST(null, 5)).toString() != '[5]') throw StateError('c2');
  print('PASS');
}}
''',
}

A112 = {
"rust": '''{H}
fn has_path_sum(root: Option<Rc<RefCell<TreeNode>>>, sum: i32) -> bool {{
    let node = match root {{ Some(x) => x, None => return false }};
    let nb = node.borrow();
    if nb.left.is_none() && nb.right.is_none() {{ return nb.val == sum; }}
    has_path_sum(nb.left.clone(), sum - nb.val) || has_path_sum(nb.right.clone(), sum - nb.val)
}}
fn main() {{
    let t = build_tree(&[Some(5), Some(4), Some(8), Some(11), None, Some(13), Some(4), Some(7), Some(2), None, None, None, Some(1)]);
    assert!(has_path_sum(t.clone(), 22));
    assert!(!has_path_sum(t, 1));
    assert!(!has_path_sum(None, 0));
    println!("PASS");
}}
''',
"lua": '''{H}
local function has_path_sum(root, sum)
    if not root then return false end
    if not root.left and not root.right then return root.val == sum end
    return has_path_sum(root.left, sum - root.val) or has_path_sum(root.right, sum - root.val)
end
local t = build_tree({{5, 4, 8, 11, "null", 13, 4, 7, 2, "null", "null", "null", 1}})
assert(has_path_sum(t, 22) == true)
assert(has_path_sum(t, 1) == false)
assert(has_path_sum(nil, 0) == false)
print("PASS")
''',
"c": '''{H}
static int has_path_sum(TreeNode *root, int sum) {{
    if (!root) return 0;
    if (!root->left && !root->right) return root->val == sum;
    return has_path_sum(root->left, sum - root->val) || has_path_sum(root->right, sum - root->val);
}}
int main(void) {{
    int v[] = {{5,4,8,11,INT_MIN_SN,13,4,7,2,INT_MIN_SN,INT_MIN_SN,INT_MIN_SN,1}};
    TreeNode *t = build_tree(v, 13);
    if (!has_path_sum(t, 22)) {{ printf("FAIL 1\\n"); return 1; }}
    if (has_path_sum(t, 1)) {{ printf("FAIL 2\\n"); return 1; }}
    if (has_path_sum(NULL, 0)) {{ printf("FAIL 3\\n"); return 1; }}
    printf("PASS\\n");
    return 0;
}}
''',
"cpp": '''{H}
static bool hasPathSum(TreeNode *root, int sum) {{
    if (!root) return false;
    if (!root->left && !root->right) return root->val == sum;
    return hasPathSum(root->left, sum - root->val) || hasPathSum(root->right, sum - root->val);
}}
int main() {{
    assert(hasPathSum(build_tree({{5, 4, 8, 11, std::nullopt, 13, 4, 7, 2, std::nullopt, std::nullopt, std::nullopt, 1}}), 22));
    assert(!hasPathSum(build_tree({{5, 4, 8, 11, std::nullopt, 13, 4, 7, 2, std::nullopt, std::nullopt, std::nullopt, 1}}), 1));
    assert(!hasPathSum(nullptr, 0));
    std::cout << "PASS" << std::endl;
    return 0;
}}
''',
"r": '''{H}
has_path_sum <- function(root, sum) {{
  if (is.null(root)) return(FALSE)
  if (is.null(root$left) && is.null(root$right)) return(root$val == sum)
  has_path_sum(root$left, sum - root$val) || has_path_sum(root$right, sum - root$val)
}}
t <- build_tree(list(5L, 4L, 8L, 11L, NA, 13L, 4L, 7L, 2L, NA, NA, NA, 1L))
stopifnot(has_path_sum(t, 22L))
stopifnot(!has_path_sum(t, 1L))
stopifnot(!has_path_sum(NULL, 0L))
cat("PASS\\n")
''',
"zig": '''{H}
fn hasPathSum(root: ?*TreeNode, sum: i32) bool {{
    const node = root orelse return false;
    if (node.left == null and node.right == null) return node.val == sum;
    return hasPathSum(node.left, sum - node.val) or hasPathSum(node.right, sum - node.val);
}}
pub fn main() !void {{
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();
    const t = try buildTree(arena.allocator(), &[_]i32{{ 5, 4, 8, 11, -1, 13, 4, 7, 2, -1, -1, -1, 1 }});
    if (!hasPathSum(t, 22)) return error.TestFailed;
    if (hasPathSum(t, 1)) return error.TestFailed;
    if (hasPathSum(null, 0)) return error.TestFailed;
    std.debug.print("PASS\\n", .{{}});
}}
''',
"dart": '''{H}
bool hasPathSum(TreeNode? root, int sum) {{
  if (root == null) return false;
  if (root.left == null && root.right == null) return root.val == sum;
  return hasPathSum(root.left, sum - root.val) || hasPathSum(root.right, sum - root.val);
}}
void main() {{
  final t = buildTree([5, 4, 8, 11, null, 13, 4, 7, 2, null, null, null, 1]);
  if (!hasPathSum(t, 22)) throw StateError('c1');
  if (hasPathSum(t, 1)) throw StateError('c2');
  if (hasPathSum(null, 0)) throw StateError('c3');
  print('PASS');
}}
''',
}

A113 = {
"rust": '''{H}
fn path_sum(root: Option<Rc<RefCell<TreeNode>>>, target: i32) -> Vec<Vec<i32>> {{
    let mut res = Vec::new();
    fn dfs(n: Option<&Rc<RefCell<TreeNode>>>, target: i32, path: &mut Vec<i32>, res: &mut Vec<Vec<i32>>) {{
        let node = match n {{ Some(x) => x, None => return }};
        let nb = node.borrow();
        path.push(nb.val);
        if nb.left.is_none() && nb.right.is_none() && nb.val == target {{
            res.push(path.clone());
        }} else {{
            dfs(nb.left.as_ref(), target - nb.val, path, res);
            dfs(nb.right.as_ref(), target - nb.val, path, res);
        }}
        path.pop();
    }}
    dfs(root.as_ref(), target, &mut Vec::new(), &mut res);
    res
}}
fn main() {{
    let t = build_tree(&[Some(5), Some(4), Some(8), Some(11), None, Some(13), Some(4), Some(7), Some(2), None, None, None, Some(1)]);
    let got = path_sum(t, 22);
    assert_eq!(got, vec![vec![5, 4, 11, 2], vec![5, 8, 4, 5]]);
    assert!(path_sum(None, 1).is_empty());
    println!("PASS");
}}
''',
"lua": '''{H}
local function path_sum(root, target)
    local res = {{}}
    local function dfs(n, t, path)
        if not n then return end
        path[#path + 1] = n.val
        if not n.left and not n.right and n.val == t then
            local cp = {{table.unpack(path)}}
            res[#res + 1] = cp
        else
            dfs(n.left, t - n.val, path)
            dfs(n.right, t - n.val, path)
        end
        path[#path] = nil
    end
    dfs(root, target, {{}})
    return res
end
local t = build_tree({{5, 4, 8, 11, "null", 13, 4, 7, 2, "null", "null", "null", 1}})
local got = path_sum(t, 22)
assert(#got == 2, "count")
local s1 = table.concat(got[1], ",")
local s2 = table.concat(got[2], ",")
assert((s1 == "5,4,11,2" and s2 == "5,8,4,5") or (s1 == "5,8,4,5" and s2 == "5,4,11,2"), "paths")
assert(#path_sum(nil, 1) == 0)
print("PASS")
''',
"c": '''{H}
static void dfs_ps(TreeNode *n, int t, int *path, int depth, int out[][64], int sizes[], int *cnt) {{
    if (!n) return;
    path[depth] = n->val;
    if (!n->left && !n->right && n->val == t) {{
        sizes[*cnt] = depth + 1;
        for (int i = 0; i <= depth; i++) out[*cnt][i] = path[i];
        (*cnt)++;
        return;
    }}
    dfs_ps(n->left, t - n->val, path, depth + 1, out, sizes, cnt);
    dfs_ps(n->right, t - n->val, path, depth + 1, out, sizes, cnt);
}}
static int path_sum(TreeNode *root, int target, int out[][64], int sizes[]) {{
    int path[64], cnt = 0;
    dfs_ps(root, target, path, 0, out, sizes, &cnt);
    return cnt;
}}
int main(void) {{
    int v[] = {{5,4,8,11,INT_MIN_SN,13,4,7,2,INT_MIN_SN,INT_MIN_SN,INT_MIN_SN,1}};
    int out[64][64], sizes[64];
    int n = path_sum(build_tree(v, 13), 22, out, sizes);
    if (n != 2) {{ printf("FAIL count %d\\n", n); return 1; }}
    int w1[] = {{5,4,11,2}}, w2[] = {{5,8,4,5}};
    int ok = 0;
    for (int c = 0; c < 2; c++) {{
        if (sizes[c] == 4) {{
            int m1 = 1, m2 = 1;
            for (int i = 0; i < 4; i++) {{ if (out[c][i] != w1[i]) m1 = 0; if (out[c][i] != w2[i]) m2 = 0; }}
            if (m1 || m2) ok++;
        }}
    }}
    if (ok != 2) {{ printf("FAIL paths\\n"); return 1; }}
    if (path_sum(NULL, 1, out, sizes) != 0) {{ printf("FAIL nil\\n"); return 1; }}
    printf("PASS\\n");
    return 0;
}}
''',
"cpp": '''{H}
static std::vector<std::vector<int>> pathSum(TreeNode *root, int target) {{
    std::vector<std::vector<int>> res;
    std::vector<int> path;
    std::function<void(TreeNode *, int)> dfs = [&](TreeNode *n, int t) {{
        if (!n) return;
        path.push_back(n->val);
        if (!n->left && !n->right && n->val == t) res.push_back(path);
        else {{
            dfs(n->left, t - n->val);
            dfs(n->right, t - n->val);
        }}
        path.pop_back();
    }};
    dfs(root, target);
    return res;
}}
int main() {{
    auto *t = build_tree({{5, 4, 8, 11, std::nullopt, 13, 4, 7, 2, std::nullopt, std::nullopt, std::nullopt, 1}});
    auto got = pathSum(t, 22);
    std::sort(got.begin(), got.end());
    assert((got == std::vector<std::vector<int>>{{{5, 4, 11, 2}, {5, 8, 4, 5}}}));
    assert(pathSum(nullptr, 1).empty());
    std::cout << "PASS" << std::endl;
    return 0;
}}
''',
"r": '''{H}
path_sum <- function(root, target) {{
  res <- list()
  dfs <- function(n, t, path) {{
    if (is.null(n)) return(invisible(NULL))
    path <- c(path, n$val)
    if (is.null(n$left) && is.null(n$right) && n$val == t) {{
      res[[length(res) + 1L]] <<- path
      return(invisible(NULL))
    }}
    dfs(n$left, t - n$val, path)
    dfs(n$right, t - n$val, path)
  }}
  dfs(root, target, integer(0))
  res
}}
t <- build_tree(list(5L, 4L, 8L, 11L, NA, 13L, 4L, 7L, 2L, NA, NA, NA, 1L))
got <- path_sum(t, 22L)
stopifnot(length(got) == 2L)
got <- got[order(vapply(got, function(x) paste(x, collapse = ","), ""))]
stopifnot(identical(got[[1]], c(5L, 4L, 11L, 2L)), identical(got[[2]], c(5L, 8L, 4L, 5L)))
stopifnot(length(path_sum(NULL, 1L)) == 0L)
cat("PASS\\n")
''',
"zig": '''{H}
fn pathSum(root: ?*TreeNode, target: i32, alloc: std.mem.Allocator) std.ArrayList(std.ArrayList(i32)) {{
    var res = std.ArrayList(std.ArrayList(i32)).init(alloc);
    const D = struct {{
        fn dfs(n: ?*TreeNode, t: i32, path: *std.ArrayList(i32), out: *std.ArrayList(std.ArrayList(i32))) void {{
            const node = n orelse return;
            path.append(node.val) catch unreachable;
            if (node.left == null and node.right == null and node.val == t) {{
                var cp = std.ArrayList(i32).init(out.allocator);
                cp.appendSlice(path.items) catch unreachable;
                out.append(cp) catch unreachable;
            }} else {{
                D.dfs(node.left, t - node.val, path, out);
                D.dfs(node.right, t - node.val, path, out);
            }}
            _ = path.pop();
        }}
    }};
    var path = std.ArrayList(i32).init(alloc);
    D.dfs(root, target, &path, &res);
    return res;
}}
pub fn main() !void {{
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();
    const alloc = arena.allocator();
    const t = try buildTree(alloc, &[_]i32{{ 5, 4, 8, 11, -1, 13, 4, 7, 2, -1, -1, -1, 1 }});
    const res = pathSum(t, 22, alloc);
    if (res.items.len != 2) return error.TestFailed;
    const w1 = [_]i32{{ 5, 4, 11, 2 }};
    const w2 = [_]i32{{ 5, 8, 4, 5 }};
    var found1 = false;
    var found2 = false;
    for (res.items) |r| {{
        if (r.items.len == 4) {{
            var m1 = true;
            var m2 = true;
            for (w1, 0..) |w, i| if (r.items[i] != w) m1 = false;
            for (w2, 0..) |w, i| if (r.items[i] != w) m2 = false;
            if (m1) found1 = true;
            if (m2) found2 = true;
        }}
    }}
    if (!found1 or !found2) return error.TestFailed;
    if (pathSum(null, 1, alloc).items.len != 0) return error.TestFailed;
    std.debug.print("PASS\\n", .{{}});
}}
''',
"dart": '''{H}
List<List<int>> pathSum(TreeNode? root, int target) {{
  final res = <List<int>>[];
  void dfs(TreeNode? n, int t, List<int> path) {{
    if (n == null) return;
    path.add(n.val);
    if (n.left == null && n.right == null && n.val == t) {{
      res.add(List<int>.from(path));
    }} else {{
      dfs(n.left, t - n.val, path);
      dfs(n.right, t - n.val, path);
    }}
    path.removeLast();
  }}
  dfs(root, target, []);
  return res;
}}
void main() {{
  final t = buildTree([5, 4, 8, 11, null, 13, 4, 7, 2, null, null, null, 1]);
  final got = pathSum(t, 22);
  if (got.length != 2) throw StateError('count');
  final set = got.map((p) => p.join(',')).toSet();
  if (!set.containsAll(['5,4,11,2', '5,8,4,5'])) throw StateError('paths');
  if (pathSum(null, 1).isNotEmpty) throw StateError('nil');
  print('PASS');
}}
''',
}

PROBS = [
    ("lc_108_将有序数组转换为二叉搜索树", A108, "LeetCode 108. 将有序数组转换为二叉搜索树", True),
    ("lc_654_最大二叉树", A654, "LeetCode 654. 最大二叉树", True),
    ("lc_701_二叉搜索树中的插入操作", A701, "LeetCode 701. 二叉搜索树中的插入操作", True),
    ("lc_112_路径总和", A112, "LeetCode 112. 路径总和", False),
]
count = 0
for prob, algo, title, use_same in PROBS:
    bid = B[prob.split("_")[1]]
    ts_dir = f"/Users/Wang/Code/github/web-x-blog/work/blog/courses/20.dsa/ts/tree/{prob}"
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
