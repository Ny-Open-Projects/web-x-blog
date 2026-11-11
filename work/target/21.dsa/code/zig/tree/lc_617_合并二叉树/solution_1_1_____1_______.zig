// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/136726698
// LeetCode 617. 合并二叉树 — Zig 版（方案1）
const std = @import("std"); // 把 @import(「std」) 存入 std

const TreeNode = struct { // 把 struct { 存入 TreeNode
    val: i32,
    left: ?*TreeNode,
    right: ?*TreeNode,
};

fn buildTree(allocator: std.mem.Allocator, vals: []const i32) !?*TreeNode { // 定义函数/方法 buildTree
    if (vals.len == 0 or vals[0] == -1) return null; // 若 vals.长度 等于 0 or vals[0] 等于 减 1，直接返回 null
    const root = try allocator.create(TreeNode); // 把 try allocator.create(TreeNode) 存入 根节点
    root.* = .{ .val = vals[0], .left = null, .right = null };
    var queue = std.ArrayList(*TreeNode).init(allocator); // 把 std.ArrayList( 乘 TreeNode).init(allocator) 存入 队列
    defer queue.deinit(); // defer 队列.deinit();
    try queue.append(root); // 把 根节点 追加到列表尾部
    var head: usize = 0; // 把 0; 写入 var head: usize
    var i: usize = 1; // 把 1; 写入 var i: usize
    while (head < queue.items.len and i < vals.len) { // 循环，直到不满足「头节点 小于 队列.items.长度 and 下标 i 小于 vals.长度」
        const node = queue.items[head]; // 把 队列.items[头节点] 存入 节点
        head += 1; // 头节点累加 1
        if (i < vals.len) { // 若 下标 i 小于 vals.长度
            if (vals[i] != -1) { // 若 vals[下标 i] 不等于 减 1
                const child = try allocator.create(TreeNode); // 把 try allocator.create(TreeNode) 存入 子节点
                child.* = .{ .val = vals[i], .left = null, .right = null };
                node.left = child; // 把 子节点; 写入 左边界
                try queue.append(child); // 把 子节点 追加到列表尾部
            }
            i += 1; // 下标 i累加 1
        }
        if (i < vals.len) { // 若 下标 i 小于 vals.长度
            if (vals[i] != -1) { // 若 vals[下标 i] 不等于 减 1
                const child = try allocator.create(TreeNode); // 把 try allocator.create(TreeNode) 存入 子节点
                child.* = .{ .val = vals[i], .left = null, .right = null };
                node.right = child; // 把 子节点; 写入 右边界
                try queue.append(child); // 把 子节点 追加到列表尾部
            }
            i += 1; // 下标 i累加 1
        }
    }
    return root; // 返回 根节点
}

fn sameTree(p: ?*const TreeNode, q: ?*const TreeNode) bool { // 定义函数/方法 sameTree
    if (p == null and q == null) return true; // 若 节点 等于 null and 节点 等于 null，直接返回 true
    if (p == null or q == null) return false; // 若 节点 等于 null or 节点 等于 null，直接返回 false
    const a = p.?; // 把 节点.? 存入 数组
    const b = q.?; // 把 节点.? 存入 b
    return a.val == b.val and sameTree(a.left, b.left) and sameTree(a.right, b.right);
}
fn mergeTrees(alloc: std.mem.Allocator, t1: ?*TreeNode, t2: ?*TreeNode) ?*TreeNode { // 定义函数/方法 mergeTrees
    const n1 = t1 orelse return t2; // 把 t1 orelse return t2 存入 n1
    const n2 = t2 orelse return n1; // 把 t2 orelse return n1 存入 n2
    n1.val += n2.val; // n1.val累加 n2.值
    n1.left = mergeTrees(alloc, n1.left, n2.left); // 把 mergeTrees(alloc, n1.左边界, n2.左边界); 写入 左边界
    n1.right = mergeTrees(alloc, n1.right, n2.right); // 把 mergeTrees(alloc, n1.右边界, n2.右边界); 写入 右边界
    return n1; // 返回 n1
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator); // 把 std.堆.ArenaAllocator.init(std.堆.page_allocator) 存入 arena
    defer arena.deinit(); // defer arena.deinit();
    const alloc = arena.allocator(); // 把 arena.allocator() 存入 alloc
    const Case = struct { a: []const i32, b: []const i32, w: []const i32 };
    const cases = [_]Case{ // 把 [_]Case{ 存入 cases
        .{ .a = &[_]i32{ 1, 3, 2, 5 }, .b = &[_]i32{ 2, 1, 3, -1, 4, -1, 7 }, .w = &[_]i32{ 3, 4, 5, 5, 4, -1, 7 } },
        .{ .a = &[_]i32{}, .b = &[_]i32{1}, .w = &[_]i32{1} },
        .{ .a = &[_]i32{1}, .b = &[_]i32{}, .w = &[_]i32{1} },
        .{ .a = &[_]i32{ 1, 2, 3 }, .b = &[_]i32{ 1, 2, 3 }, .w = &[_]i32{ 2, 4, 6 } },
    };
    for (cases, 0..) |c, i| { // for (cases, 0..) 按位或 字符, 下标 i 按位或 {
        const got = mergeTrees(alloc, try buildTree(alloc, c.a), try buildTree(alloc, c.b));
        const want = try buildTree(alloc, c.w); // 把 try buildTree(alloc, 字符.权重) 存入 want
        if (!sameTree(got, want)) { // 若 取反 sameTree(got, want
            std.debug.print("FAIL case {d}\n", .{i}); // 打印输出
            return error.TestFailed; // 返回 error.TestFailed
        }
    }
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
