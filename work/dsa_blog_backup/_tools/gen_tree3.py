#!/usr/bin/env python3
# gen_tree3.py — tree 第三批（BFS 层序家族）：lc_102/lc_107/lc_637/lc_515/lc_513 × 7语言
import sys, os; sys.path.insert(0, "/Users/Wang/Code/webfault-ai/dsa/_tools")
from langlib import emit, TREE_H, head_comment, EXT

B = {"102": "130877211", "107": "131038644", "637": "131302535", "515": "137236962", "513": "137408649"}
LANGNAME = {"rust": "Rust", "lua": "Lua", "c": "C", "cpp": "C++", "r": "R", "zig": "Zig", "dart": "Dart"}

A102 = {
"rust": '''{H}
fn level_order(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<Vec<i32>> {{
    let root = match root {{ Some(x) => x, None => return vec![] }};
    let mut res = Vec::new();
    let mut q = vec![root];
    while !q.is_empty() {{
        let size = q.len();
        let mut level = Vec::new();
        for _ in 0..size {{
            let node = q.remove(0);
            let nb = node.borrow();
            level.push(nb.val);
            if let Some(c) = nb.left.clone() {{ q.push(c); }}
            if let Some(c) = nb.right.clone() {{ q.push(c); }}
        }}
        res.push(level);
    }}
    res
}}
fn main() {{
    assert_eq!(level_order(None), Vec::<Vec<i32>>::new());
    assert_eq!(level_order(build_tree(&[Some(3), Some(9), Some(20), None, None, Some(15), Some(7)])), vec![vec![3], vec![9, 20], vec![15, 7]]);
    assert_eq!(level_order(build_tree(&[Some(1)])), vec![vec![1]]);
    println!("PASS");
}}
''',
"lua": '''{H}
local function level_order(root)
    if not root then return {{}} end
    local res = {{}}
    local q = {{root}}
    while #q > 0 do
        local size = #q
        local level = {{}}
        for _ = 1, size do
            local node = table.remove(q, 1)
            level[#level + 1] = node.val
            if node.left then q[#q + 1] = node.left end
            if node.right then q[#q + 1] = node.right end
        end
        res[#res + 1] = level
    end
    return res
end
local function s(t) local p = {{}} for i, l in ipairs(t) do p[i] = table.concat(l, ",") end return table.concat(p, "|") end
assert(s(level_order(nil)) == "")
assert(s(level_order(build_tree({{3, 9, 20, "null", "null", 15, 7}}))) == "3|9,20|15,7")
assert(s(level_order(build_tree({{1}}))) == "1")
print("PASS")
''',
"c": '''{H}
static int level_order(TreeNode *root, int out[][64], int *levels) {{
    if (!root) {{ *levels = 0; return 0; }}
    TreeNode *q[4096];
    int head = 0, tail = 0, nl = 0;
    q[tail++] = root;
    while (head < tail) {{
        int size = tail - head;
        int cnt = 0;
        for (int i = 0; i < size; i++) {{
            TreeNode *n = q[head++];
            out[nl][cnt++] = n->val;
            if (n->left) q[tail++] = n->left;
            if (n->right) q[tail++] = n->right;
        }}
        levels[nl++] = cnt;
    }}
    return nl;
}}
int main(void) {{
    int v[] = {{3,9,20,INT_MIN_SN,INT_MIN_SN,15,7}};
    int out[64][64], levels[64], n;
    n = level_order(NULL, out, levels);
    if (n != 0) {{ printf("FAIL 0\\n"); return 1; }}
    n = level_order(build_tree(v, 7), out, levels);
    int w1[] = {{3}}, w2[] = {{9,20}}, w3[] = {{15,7}};
    if (n != 3 || levels[0] != 1 || levels[1] != 2 || levels[2] != 2) {{ printf("FAIL shape\\n"); return 1; }}
    if (out[0][0] != 3 || out[1][0] != 9 || out[1][1] != 20 || out[2][0] != 15 || out[2][1] != 7) {{ printf("FAIL vals\\n"); return 1; }}
    (void)w1; (void)w2; (void)w3;
    int v2[] = {{1}};
    n = level_order(build_tree(v2, 1), out, levels);
    if (n != 1 || out[0][0] != 1) {{ printf("FAIL 1\\n"); return 1; }}
    printf("PASS\\n");
    return 0;
}}
''',
"cpp": '''{H}
static std::vector<std::vector<int>> levelOrder(TreeNode *root) {{
    if (!root) return {{}};
    std::vector<std::vector<int>> res;
    std::queue<TreeNode *> q;
    q.push(root);
    while (!q.empty()) {{
        int size = static_cast<int>(q.size());
        std::vector<int> level;
        for (int i = 0; i < size; ++i) {{
            auto *n = q.front();
            q.pop();
            level.push_back(n->val);
            if (n->left) q.push(n->left);
            if (n->right) q.push(n->right);
        }}
        res.push_back(std::move(level));
    }}
    return res;
}}
int main() {{
    assert((levelOrder(nullptr) == std::vector<std::vector<int>>{{}}));
    assert((levelOrder(build_tree({{3, 9, 20, std::nullopt, std::nullopt, 15, 7}})) == std::vector<std::vector<int>>{{{3}, {9, 20}, {15, 7}}}));
    assert((levelOrder(build_tree({{1}})) == std::vector<std::vector<int>>{{{1}}}));
    std::cout << "PASS" << std::endl;
    return 0;
}}
''',
"r": '''{H}
level_order <- function(root) tree_to_levels(root)
stopifnot(identical(level_order(NULL), list()))
stopifnot(identical(level_order(build_tree(list(3L, 9L, 20L, NA, NA, 15L, 7L))), list(3L, c(9L, 20L), c(15L, 7L))))
stopifnot(identical(level_order(build_tree(list(1L))), list(1L)))
cat("PASS\\n")
''',
"zig": '''{H}
fn levelOrder(root: ?*TreeNode, alloc: std.mem.Allocator) std.ArrayList(std.ArrayList(i32)) {{
    var res = std.ArrayList(std.ArrayList(i32)).init(alloc);
    const r = root orelse return res;
    var q = std.ArrayList(*TreeNode).init(alloc);
    q.append(r) catch unreachable;
    var head: usize = 0;
    while (head < q.items.len) {{
        const size = q.items.len - head;
        var level = std.ArrayList(i32).init(alloc);
        for (0..size) |_| {{
            const node = q.items[head];
            head += 1;
            level.append(node.val) catch unreachable;
            if (node.left) |c| q.append(c) catch unreachable;
            if (node.right) |c| q.append(c) catch unreachable;
        }}
        res.append(level) catch unreachable;
    }}
    return res;
}}
pub fn main() !void {{
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();
    const alloc = arena.allocator();
    var res = levelOrder(null, alloc);
    if (res.items.len != 0) return error.TestFailed;
    res = levelOrder(try buildTree(alloc, &[_]i32{{ 3, 9, 20, -1, -1, 15, 7 }}), alloc);
    if (res.items.len != 3) return error.TestFailed;
    if (res.items[0].items[0] != 3) return error.TestFailed;
    if (res.items[1].items[0] != 9 or res.items[1].items[1] != 20) return error.TestFailed;
    if (res.items[2].items[0] != 15 or res.items[2].items[1] != 7) return error.TestFailed;
    res = levelOrder(try buildTree(alloc, &[_]i32{{1}}), alloc);
    if (res.items.len != 1 or res.items[0].items[0] != 1) return error.TestFailed;
    std.debug.print("PASS\\n", .{{}});
}}
''',
"dart": '''{H}
List<List<int>> levelOrder(TreeNode? root) {{
  if (root == null) return [];
  final res = <List<int>>[];
  final q = <TreeNode>[root];
  var head = 0;
  while (head < q.length) {{
    final size = q.length - head;
    final level = <int>[];
    for (var i = 0; i < size; i++) {{
      final n = q[head++];
      level.add(n.val);
      if (n.left != null) q.add(n.left!);
      if (n.right != null) q.add(n.right!);
    }}
    res.add(level);
  }}
  return res;
}}
String s(List<List<int>> t) => t.map((l) => l.join(',')).join('|');
void main() {{
  if (s(levelOrder(null)) != '') throw StateError('c0');
  if (s(levelOrder(buildTree([3, 9, 20, null, null, 15, 7]))) != '3|9,20|15,7') throw StateError('c1');
  if (s(levelOrder(buildTree([1]))) != '1') throw StateError('c2');
  print('PASS');
}}
''',
}

A107 = {
"rust": '''{H}
fn level_order_bottom(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<Vec<i32>> {{
    let root = match root {{ Some(x) => x, None => return vec![] }};
    let mut res = Vec::new();
    let mut q = vec![root];
    while !q.is_empty() {{
        let size = q.len();
        let mut level = Vec::new();
        for _ in 0..size {{
            let node = q.remove(0);
            let nb = node.borrow();
            level.push(nb.val);
            if let Some(c) = nb.left.clone() {{ q.push(c); }}
            if let Some(c) = nb.right.clone() {{ q.push(c); }}
        }}
        res.insert(0, level);
    }}
    res
}}
fn main() {{
    assert_eq!(level_order_bottom(None), Vec::<Vec<i32>>::new());
    assert_eq!(level_order_bottom(build_tree(&[Some(3), Some(9), Some(20), None, None, Some(15), Some(7)])), vec![vec![15, 7], vec![9, 20], vec![3]]);
    println!("PASS");
}}
''',
"lua": '''{H}
local function level_order_bottom(root)
    if not root then return {{}} end
    local res = {{}}
    local q = {{root}}
    while #q > 0 do
        local size = #q
        local level = {{}}
        for _ = 1, size do
            local node = table.remove(q, 1)
            level[#level + 1] = node.val
            if node.left then q[#q + 1] = node.left end
            if node.right then q[#q + 1] = node.right end
        end
        table.insert(res, 1, level)
    end
    return res
end
local function s(t) local p = {{}} for i, l in ipairs(t) do p[i] = table.concat(l, ",") end return table.concat(p, "|") end
assert(s(level_order_bottom(nil)) == "")
assert(s(level_order_bottom(build_tree({{3, 9, 20, "null", "null", 15, 7}}))) == "15,7|9,20|3")
print("PASS")
''',
"c": '''{H}
static int level_order_bottom(TreeNode *root, int out[][64], int levels[]) {{
    if (!root) {{ return 0; }}
    TreeNode *q[4096];
    int head = 0, tail = 0;
    int tmp[64][64], tl[64], nl = 0;
    q[tail++] = root;
    while (head < tail) {{
        int size = tail - head, cnt = 0;
        for (int i = 0; i < size; i++) {{
            TreeNode *n = q[head++];
            tmp[nl][cnt++] = n->val;
            if (n->left) q[tail++] = n->left;
            if (n->right) q[tail++] = n->right;
        }}
        tl[nl++] = cnt;
    }}
    for (int i = 0; i < nl; i++) {{ /* 反转 */
        levels[i] = tl[nl - 1 - i];
        for (int j = 0; j < tl[nl - 1 - i]; j++) out[i][j] = tmp[nl - 1 - i][j];
    }}
    return nl;
}}
int main(void) {{
    int v[] = {{3,9,20,INT_MIN_SN,INT_MIN_SN,15,7}};
    int out[64][64], levels[64], n;
    if (level_order_bottom(NULL, out, levels) != 0) {{ printf("FAIL 0\\n"); return 1; }}
    n = level_order_bottom(build_tree(v, 7), out, levels);
    if (n != 3 || out[0][0] != 15 || out[0][1] != 7 || out[1][0] != 9 || out[1][1] != 20 || out[2][0] != 3) {{ printf("FAIL 1\\n"); return 1; }}
    printf("PASS\\n");
    return 0;
}}
''',
"cpp": '''{H}
static std::vector<std::vector<int>> levelOrderBottom(TreeNode *root) {{
    std::vector<std::vector<int>> res;
    if (!root) return res;
    std::queue<TreeNode *> q;
    q.push(root);
    while (!q.empty()) {{
        int size = static_cast<int>(q.size());
        std::vector<int> level;
        for (int i = 0; i < size; ++i) {{
            auto *n = q.front();
            q.pop();
            level.push_back(n->val);
            if (n->left) q.push(n->left);
            if (n->right) q.push(n->right);
        }}
        res.insert(res.begin(), std::move(level));
    }}
    return res;
}}
int main() {{
    assert((levelOrderBottom(nullptr) == std::vector<std::vector<int>>{{}}));
    assert((levelOrderBottom(build_tree({{3, 9, 20, std::nullopt, std::nullopt, 15, 7}})) == std::vector<std::vector<int>>{{{15, 7}, {9, 20}, {3}}}));
    std::cout << "PASS" << std::endl;
    return 0;
}}
''',
"r": '''{H}
level_order_bottom <- function(root) rev(tree_to_levels(root))
stopifnot(identical(level_order_bottom(NULL), list()))
stopifnot(identical(level_order_bottom(build_tree(list(3L, 9L, 20L, NA, NA, 15L, 7L))), list(c(15L, 7L), c(9L, 20L), 3L)))
cat("PASS\\n")
''',
"zig": '''{H}
fn levelOrderBottom(root: ?*TreeNode, alloc: std.mem.Allocator) std.ArrayList(std.ArrayList(i32)) {{
    var res = std.ArrayList(std.ArrayList(i32)).init(alloc);
    const r = root orelse return res;
    var q = std.ArrayList(*TreeNode).init(alloc);
    q.append(r) catch unreachable;
    var head: usize = 0;
    while (head < q.items.len) {{
        const size = q.items.len - head;
        var level = std.ArrayList(i32).init(alloc);
        for (0..size) |_| {{
            const node = q.items[head];
            head += 1;
            level.append(node.val) catch unreachable;
            if (node.left) |c| q.append(c) catch unreachable;
            if (node.right) |c| q.append(c) catch unreachable;
        }}
        res.insert(0, level) catch unreachable;
    }}
    return res;
}}
pub fn main() !void {{
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();
    const alloc = arena.allocator();
    if (levelOrderBottom(null, alloc).items.len != 0) return error.TestFailed;
    const res = levelOrderBottom(try buildTree(alloc, &[_]i32{{ 3, 9, 20, -1, -1, 15, 7 }}), alloc);
    if (res.items.len != 3) return error.TestFailed;
    if (res.items[0].items[0] != 15 or res.items[0].items[1] != 7) return error.TestFailed;
    if (res.items[1].items[0] != 9 or res.items[1].items[1] != 20) return error.TestFailed;
    if (res.items[2].items[0] != 3) return error.TestFailed;
    std.debug.print("PASS\\n", .{{}});
}}
''',
"dart": '''{H}
List<List<int>> levelOrderBottom(TreeNode? root) {{
  if (root == null) return [];
  final res = <List<int>>[];
  final q = <TreeNode>[root];
  var head = 0;
  while (head < q.length) {{
    final size = q.length - head;
    final level = <int>[];
    for (var i = 0; i < size; i++) {{
      final n = q[head++];
      level.add(n.val);
      if (n.left != null) q.add(n.left!);
      if (n.right != null) q.add(n.right!);
    }}
    res.insert(0, level);
  }}
  return res;
}}
String s(List<List<int>> t) => t.map((l) => l.join(',')).join('|');
void main() {{
  if (s(levelOrderBottom(null)) != '') throw StateError('c0');
  if (s(levelOrderBottom(buildTree([3, 9, 20, null, null, 15, 7]))) != '15,7|9,20|3') throw StateError('c1');
  print('PASS');
}}
''',
}

A637 = {
"rust": '''{H}
fn average_of_levels(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<f64> {{
    let root = match root {{ Some(x) => x, None => return vec![] }};
    let mut res = Vec::new();
    let mut q = vec![root];
    while !q.is_empty() {{
        let size = q.len();
        let mut sum = 0i64;
        for _ in 0..size {{
            let node = q.remove(0);
            let nb = node.borrow();
            sum += nb.val as i64;
            if let Some(c) = nb.left.clone() {{ q.push(c); }}
            if let Some(c) = nb.right.clone() {{ q.push(c); }}
        }}
        res.push(sum as f64 / size as f64);
    }}
    res
}}
fn main() {{
    let got = average_of_levels(build_tree(&[Some(3), Some(9), Some(20), Some(15), Some(7)]));
    let want = vec![3.0, 14.5, 11.0];
    assert_eq!(got, want);
    assert_eq!(average_of_levels(build_tree(&[Some(1)])), vec![1.0]);
    println!("PASS");
}}
''',
"lua": '''{H}
local function average_of_levels(root)
    if not root then return {{}} end
    local res = {{}}
    local q = {{root}}
    while #q > 0 do
        local size = #q
        local sum = 0
        for _ = 1, size do
            local node = table.remove(q, 1)
            sum = sum + node.val
            if node.left then q[#q + 1] = node.left end
            if node.right then q[#q + 1] = node.right end
        end
        res[#res + 1] = sum / size
    end
    return res
end
local a = average_of_levels(build_tree({{3, 9, 20, 15, 7}}))
assert(#a == 3 and a[1] == 3.0 and a[2] == 14.5 and a[3] == 11.0)
local b = average_of_levels(build_tree({{1}}))
assert(#b == 1 and b[1] == 1.0)
print("PASS")
''',
"c": '''{H}
#include <math.h>
static int average_of_levels(TreeNode *root, double out[]) {{
    if (!root) return 0;
    TreeNode *q[4096];
    int head = 0, tail = 0, nl = 0;
    q[tail++] = root;
    while (head < tail) {{
        int size = tail - head;
        long sum = 0;
        for (int i = 0; i < size; i++) {{
            TreeNode *n = q[head++];
            sum += n->val;
            if (n->left) q[tail++] = n->left;
            if (n->right) q[tail++] = n->right;
        }}
        out[nl++] = (double)sum / size;
    }}
    return nl;
}}
int main(void) {{
    int v[] = {{3,9,20,15,7}};
    double out[64];
    int n = average_of_levels(build_tree(v, 5), out);
    if (n != 3 || fabs(out[0] - 3.0) > 1e-9 || fabs(out[1] - 14.5) > 1e-9 || fabs(out[2] - 11.0) > 1e-9) {{ printf("FAIL 1\\n"); return 1; }}
    int v2[] = {{1}};
    n = average_of_levels(build_tree(v2, 1), out);
    if (n != 1 || fabs(out[0] - 1.0) > 1e-9) {{ printf("FAIL 2\\n"); return 1; }}
    printf("PASS\\n");
    return 0;
}}
''',
"cpp": '''{H}
static std::vector<double> averageOfLevels(TreeNode *root) {{
    std::vector<double> res;
    if (!root) return res;
    std::queue<TreeNode *> q;
    q.push(root);
    while (!q.empty()) {{
        int size = static_cast<int>(q.size());
        long sum = 0;
        for (int i = 0; i < size; ++i) {{
            auto *n = q.front();
            q.pop();
            sum += n->val;
            if (n->left) q.push(n->left);
            if (n->right) q.push(n->right);
        }}
        res.push_back(static_cast<double>(sum) / size);
    }}
    return res;
}}
int main() {{
    assert((averageOfLevels(build_tree({{3, 9, 20, 15, 7}})) == std::vector<double>{{3.0, 14.5, 11.0}}));
    assert((averageOfLevels(build_tree({{1}})) == std::vector<double>{{1.0}}));
    std::cout << "PASS" << std::endl;
    return 0;
}}
''',
"r": '''{H}
average_of_levels <- function(root) {{
  lv <- tree_to_levels(root)
  vapply(lv, function(x) sum(as.numeric(x)) / length(x), numeric(1))
}}
a <- average_of_levels(build_tree(list(3L, 9L, 20L, 15L, 7L)))
stopifnot(length(a) == 3L, all(abs(a - c(3, 14.5, 11)) < 1e-9))
b <- average_of_levels(build_tree(list(1L)))
stopifnot(length(b) == 1L, abs(b - 1) < 1e-9)
cat("PASS\\n")
''',
"zig": '''{H}
fn averageOfLevels(root: ?*TreeNode, alloc: std.mem.Allocator) std.ArrayList(f64) {{
    var res = std.ArrayList(f64).init(alloc);
    const r = root orelse return res;
    var q = std.ArrayList(*TreeNode).init(alloc);
    q.append(r) catch unreachable;
    var head: usize = 0;
    while (head < q.items.len) {{
        const size = q.items.len - head;
        var sum: i64 = 0;
        for (0..size) |_| {{
            const node = q.items[head];
            head += 1;
            sum += node.val;
            if (node.left) |c| q.append(c) catch unreachable;
            if (node.right) |c| q.append(c) catch unreachable;
        }}
        res.append(@as(f64, @floatFromInt(sum)) / @as(f64, @floatFromInt(size))) catch unreachable;
    }}
    return res;
}}
pub fn main() !void {{
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();
    const alloc = arena.allocator();
    const res = averageOfLevels(try buildTree(alloc, &[_]i32{{ 3, 9, 20, 15, 7 }}), alloc);
    if (res.items.len != 3) return error.TestFailed;
    if (@abs(res.items[0] - 3.0) > 1e-9 or @abs(res.items[1] - 14.5) > 1e-9 or @abs(res.items[2] - 11.0) > 1e-9) return error.TestFailed;
    const r2 = averageOfLevels(try buildTree(alloc, &[_]i32{{1}}), alloc);
    if (r2.items.len != 1 or @abs(r2.items[0] - 1.0) > 1e-9) return error.TestFailed;
    std.debug.print("PASS\\n", .{{}});
}}
''',
"dart": '''{H}
List<double> averageOfLevels(TreeNode? root) {{
  if (root == null) return [];
  final res = <double>[];
  var q = <TreeNode>[root];
  while (q.isNotEmpty) {{
    final size = q.length;
    var sum = 0;
    final nxt = <TreeNode>[];
    for (final n in q) {{
      sum += n.val;
      if (n.left != null) nxt.add(n.left!);
      if (n.right != null) nxt.add(n.right!);
    }}
    res.add(sum / size);
    q = nxt;
  }}
  return res;
}}
void main() {{
  final a = averageOfLevels(buildTree([3, 9, 20, 15, 7]));
  if (a.length != 3 || (a[0] - 3).abs() > 1e-9 || (a[1] - 14.5).abs() > 1e-9 || (a[2] - 11).abs() > 1e-9) throw StateError('c1');
  final b = averageOfLevels(buildTree([1]));
  if (b.length != 1 || (b[0] - 1).abs() > 1e-9) throw StateError('c2');
  print('PASS');
}}
''',
}

A515 = {
"rust": '''{H}
fn largest_values(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<i32> {{
    let root = match root {{ Some(x) => x, None => return vec![] }};
    let mut res = Vec::new();
    let mut q = vec![root];
    while !q.is_empty() {{
        let size = q.len();
        let mut mx = i32::MIN;
        for _ in 0..size {{
            let node = q.remove(0);
            let nb = node.borrow();
            if nb.val > mx {{ mx = nb.val; }}
            if let Some(c) = nb.left.clone() {{ q.push(c); }}
            if let Some(c) = nb.right.clone() {{ q.push(c); }}
        }}
        res.push(mx);
    }}
    res
}}
fn main() {{
    assert_eq!(largest_values(build_tree(&[Some(1), Some(3), Some(2), Some(5), Some(3), None, Some(9)])), vec![1, 3, 9]);
    assert_eq!(largest_values(None), Vec::<i32>::new());
    println!("PASS");
}}
''',
"lua": '''{H}
local function largest_values(root)
    if not root then return {{}} end
    local res = {{}}
    local q = {{root}}
    while #q > 0 do
        local size = #q
        local mx = -math.huge
        for _ = 1, size do
            local node = table.remove(q, 1)
            if node.val > mx then mx = node.val end
            if node.left then q[#q + 1] = node.left end
            if node.right then q[#q + 1] = node.right end
        end
        res[#res + 1] = mx
    end
    return res
end
local a = largest_values(build_tree({{1, 3, 2, 5, 3, "null", 9}}))
assert(#a == 3 and a[1] == 1 and a[2] == 3 and a[3] == 9)
assert(#largest_values(nil) == 0)
print("PASS")
''',
"c": '''{H}
static int largest_values(TreeNode *root, int out[]) {{
    if (!root) return 0;
    TreeNode *q[4096];
    int head = 0, tail = 0, nl = 0;
    q[tail++] = root;
    while (head < tail) {{
        int size = tail - head, mx = INT_MIN_SN;
        for (int i = 0; i < size; i++) {{
            TreeNode *n = q[head++];
            if (n->val > mx) mx = n->val;
            if (n->left) q[tail++] = n->left;
            if (n->right) q[tail++] = n->right;
        }}
        out[nl++] = mx;
    }}
    return nl;
}}
int main(void) {{
    int v[] = {{1,3,2,5,3,INT_MIN_SN,9}};
    int out[64];
    int n = largest_values(build_tree(v, 7), out);
    if (n != 3 || out[0] != 1 || out[1] != 3 || out[2] != 9) {{ printf("FAIL 1\\n"); return 1; }}
    if (largest_values(NULL, out) != 0) {{ printf("FAIL 2\\n"); return 1; }}
    printf("PASS\\n");
    return 0;
}}
''',
"cpp": '''{H}
static std::vector<int> largestValues(TreeNode *root) {{
    std::vector<int> res;
    if (!root) return res;
    std::queue<TreeNode *> q;
    q.push(root);
    while (!q.empty()) {{
        int size = static_cast<int>(q.size());
        int mx = INT_MIN;
        for (int i = 0; i < size; ++i) {{
            auto *n = q.front();
            q.pop();
            mx = std::max(mx, n->val);
            if (n->left) q.push(n->left);
            if (n->right) q.push(n->right);
        }}
        res.push_back(mx);
    }}
    return res;
}}
int main() {{
    assert((largestValues(build_tree({{1, 3, 2, 5, 3, std::nullopt, 9}})) == std::vector<int>{{1, 3, 9}}));
    assert(largestValues(nullptr).empty());
    std::cout << "PASS" << std::endl;
    return 0;
}}
''',
"r": '''{H}
largest_values <- function(root) vapply(tree_to_levels(root), max, integer(1))
a <- largest_values(build_tree(list(1L, 3L, 2L, 5L, 3L, NA, 9L)))
stopifnot(identical(a, c(1L, 3L, 9L)))
stopifnot(length(largest_values(NULL)) == 0L)
cat("PASS\\n")
''',
"zig": '''{H}
fn largestValues(root: ?*TreeNode, alloc: std.mem.Allocator) std.ArrayList(i32) {{
    var res = std.ArrayList(i32).init(alloc);
    const r = root orelse return res;
    var q = std.ArrayList(*TreeNode).init(alloc);
    q.append(r) catch unreachable;
    var head: usize = 0;
    while (head < q.items.len) {{
        const size = q.items.len - head;
        var mx: i32 = std.math.minInt(i32);
        for (0..size) |_| {{
            const node = q.items[head];
            head += 1;
            if (node.val > mx) mx = node.val;
            if (node.left) |c| q.append(c) catch unreachable;
            if (node.right) |c| q.append(c) catch unreachable;
        }}
        res.append(mx) catch unreachable;
    }}
    return res;
}}
pub fn main() !void {{
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();
    const alloc = arena.allocator();
    const res = largestValues(try buildTree(alloc, &[_]i32{{ 1, 3, 2, 5, 3, -1, 9 }}), alloc);
    if (res.items.len != 3 or res.items[0] != 1 or res.items[1] != 3 or res.items[2] != 9) return error.TestFailed;
    if (largestValues(null, alloc).items.len != 0) return error.TestFailed;
    std.debug.print("PASS\\n", .{{}});
}}
''',
"dart": '''{H}
List<int> largestValues(TreeNode? root) {{
  if (root == null) return [];
  final res = <int>[];
  var q = <TreeNode>[root];
  while (q.isNotEmpty) {{
    var mx = -0x8000000000000000;
    final nxt = <TreeNode>[];
    for (final n in q) {{
      if (n.val > mx) mx = n.val;
      if (n.left != null) nxt.add(n.left!);
      if (n.right != null) nxt.add(n.right!);
    }}
    res.add(mx);
    q = nxt;
  }}
  return res;
}}
void main() {{
  final a = largestValues(buildTree([1, 3, 2, 5, 3, null, 9]));
  if (a.length != 3 || a[0] != 1 || a[1] != 3 || a[2] != 9) throw StateError('c1');
  if (largestValues(null).isNotEmpty) throw StateError('c2');
  print('PASS');
}}
''',
}

A513 = {
"rust": '''{H}
fn find_bottom_left_value(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {{
    let root = root.unwrap();
    let mut q = vec![root];
    let mut leftmost = 0;
    while !q.is_empty() {{
        let size = q.len();
        leftmost = q[0].borrow().val;
        for _ in 0..size {{
            let node = q.remove(0);
            let nb = node.borrow();
            if let Some(c) = nb.left.clone() {{ q.push(c); }}
            if let Some(c) = nb.right.clone() {{ q.push(c); }}
        }}
    }}
    leftmost
}}
fn main() {{
    assert_eq!(find_bottom_left_value(build_tree(&[Some(1), Some(2), Some(3), Some(4), Some(5), Some(6), Some(7)])), 4);
    assert_eq!(find_bottom_left_value(build_tree(&[Some(2), Some(1), Some(3)])), 1);
    println!("PASS");
}}
''',
"lua": '''{H}
local function find_bottom_left_value(root)
    local q = {{root}}
    local leftmost = root.val
    while #q > 0 do
        local size = #q
        leftmost = q[1].val
        for _ = 1, size do
            local node = table.remove(q, 1)
            if node.left then q[#q + 1] = node.left end
            if node.right then q[#q + 1] = node.right end
        end
    end
    return leftmost
end
assert(find_bottom_left_value(build_tree({{1, 2, 3, 4, 5, 6, 7}})) == 4)
assert(find_bottom_left_value(build_tree({{2, 1, 3}})) == 1)
print("PASS")
''',
"c": '''{H}
static int find_bottom_left_value(TreeNode *root) {{
    TreeNode *q[4096];
    int head = 0, tail = 0, leftmost = root->val;
    q[tail++] = root;
    while (head < tail) {{
        int size = tail - head;
        leftmost = q[head]->val;
        for (int i = 0; i < size; i++) {{
            TreeNode *n = q[head++];
            if (n->left) q[tail++] = n->left;
            if (n->right) q[tail++] = n->right;
        }}
    }}
    return leftmost;
}}
int main(void) {{
    int v1[] = {{1,2,3,4,5,6,7}};
    int v2[] = {{2,1,3}};
    if (find_bottom_left_value(build_tree(v1, 7)) != 4) {{ printf("FAIL 1\\n"); return 1; }}
    if (find_bottom_left_value(build_tree(v2, 3)) != 1) {{ printf("FAIL 2\\n"); return 1; }}
    printf("PASS\\n");
    return 0;
}}
''',
"cpp": '''{H}
static int findBottomLeftValue(TreeNode *root) {{
    std::queue<TreeNode *> q;
    q.push(root);
    int leftmost = root->val;
    while (!q.empty()) {{
        int size = static_cast<int>(q.size());
        leftmost = q.front()->val;
        for (int i = 0; i < size; ++i) {{
            auto *n = q.front();
            q.pop();
            if (n->left) q.push(n->left);
            if (n->right) q.push(n->right);
        }}
    }}
    return leftmost;
}}
int main() {{
    assert(findBottomLeftValue(build_tree({{1, 2, 3, 4, 5, 6, 7}})) == 4);
    assert(findBottomLeftValue(build_tree({{2, 1, 3}})) == 1);
    std::cout << "PASS" << std::endl;
    return 0;
}}
''',
"r": '''{H}
find_bottom_left_value <- function(root) {{
  lv <- tree_to_levels(root)
  lv[[length(lv)]][1L]
}}
stopifnot(find_bottom_left_value(build_tree(list(1L, 2L, 3L, 4L, 5L, 6L, 7L))) == 4L)
stopifnot(find_bottom_left_value(build_tree(list(2L, 1L, 3L))) == 1L)
cat("PASS\\n")
''',
"zig": '''{H}
fn findBottomLeftValue(root: ?*TreeNode) i32 {{
    const r = root.?;
    var q = std.ArrayList(*TreeNode).init(std.heap.page_allocator);
    defer q.deinit();
    q.append(r) catch unreachable;
    var head: usize = 0;
    var leftmost: i32 = r.val;
    while (head < q.items.len) {{
        const size = q.items.len - head;
        leftmost = q.items[head].val;
        for (0..size) |_| {{
            const node = q.items[head];
            head += 1;
            if (node.left) |c| q.append(c) catch unreachable;
            if (node.right) |c| q.append(c) catch unreachable;
        }}
    }}
    return leftmost;
}}
pub fn main() !void {{
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();
    const alloc = arena.allocator();
    if (findBottomLeftValue(try buildTree(alloc, &[_]i32{{ 1, 2, 3, 4, 5, 6, 7 }})) != 4) return error.TestFailed;
    if (findBottomLeftValue(try buildTree(alloc, &[_]i32{{ 2, 1, 3 }})) != 1) return error.TestFailed;
    std.debug.print("PASS\\n", .{{}});
}}
''',
"dart": '''{H}
int findBottomLeftValue(TreeNode? root) {{
  var q = <TreeNode>[root!];
  var leftmost = root.val;
  while (q.isNotEmpty) {{
    leftmost = q.first.val;
    final size = q.length;
    for (var i = 0; i < size; i++) {{
      final n = q.removeAt(0);
      if (n.left != null) q.add(n.left!);
      if (n.right != null) q.add(n.right!);
    }}
  }}
  return leftmost;
}}
void main() {{
  if (findBottomLeftValue(buildTree([1, 2, 3, 4, 5, 6, 7])) != 4) throw StateError('c1');
  if (findBottomLeftValue(buildTree([2, 1, 3])) != 1) throw StateError('c2');
  print('PASS');
}}
''',
}

PROBS = [
    ("lc_102_二叉树的层序遍历", A102, "LeetCode 102. 二叉树的层序遍历"),
    ("lc_107_二叉树的层序遍历_ii", A107, "LeetCode 107. 二叉树的层序遍历 II"),
    ("lc_637_二叉树的层平均值", A637, "LeetCode 637. 二叉树的层平均值"),
    ("lc_515_在每个树行中找最大值", A515, "LeetCode 515. 在每个树行中找最大值"),
    ("lc_513_找树左下角的值", A513, "LeetCode 513. 找树左下角的值"),
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
