// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135759583
// LeetCode 111. 二叉树的最小深度 — Zig 版（方案8）
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

fn minDepth(root: ?*TreeNode) i32 { // 定义函数/方法 minDepth
    const r = root orelse return 0; // 把 根节点 orelse return 0 存入 右指针
    const QN = struct { n: *TreeNode, l: i32 }; // 把 struct { 元素个数: 乘 TreeNode, 左指针: i32 } 存入 QN
    var q = std.ArrayList(QN).init(std.heap.page_allocator); // 把 std.ArrayList(QN).init(std.堆.page_allocator) 存入 节点
    defer q.deinit(); // defer 节点.deinit();
    q.append(.{ .n = r, .l = 1 }) catch unreachable; // 把 { .元素个数 赋值为 右指针, .左指针 赋值为 1 } 追加到列表尾部
    var head: usize = 0; // 把 0; 写入 var head: usize
    while (head < q.items.len) { // 循环，直到不满足「头节点 小于 节点.items.长度」
        const it = q.items[head]; // 把 节点.items[头节点] 存入 it
        head += 1; // 头节点累加 1
        if (it.n.left == null and it.n.right == null) return it.l; // 若 it.元素个数.左边界 等于 null and it.元素个数.右边界 等于 null，直接返回 it.左指针
        if (it.n.left) |c| q.append(.{ .n = c, .l = it.l + 1 }) catch unreachable;
        if (it.n.right) |c| q.append(.{ .n = c, .l = it.l + 1 }) catch unreachable;
    }
    return 0; // 返回 0
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator); // 把 std.堆.ArenaAllocator.init(std.堆.page_allocator) 存入 arena
    defer arena.deinit(); // defer arena.deinit();
    const alloc = arena.allocator(); // 把 arena.allocator() 存入 alloc
    if (minDepth(try buildTree(alloc, &[_]i32{ 3, 9, 20, -1, -1, 15, 7 })) != 2) return error.TestFailed;
    if (minDepth(try buildTree(alloc, &[_]i32{ 2, -1, 3, -1, 4, -1, 5, -1, 6 })) != 5) return error.TestFailed;
    if (minDepth(null) != 0) return error.TestFailed; // 若 minDepth(null) 不等于 0，直接返回 error.TestFailed
    if (minDepth(try buildTree(alloc, &[_]i32{1})) != 1) return error.TestFailed;
    if (minDepth(try buildTree(alloc, &[_]i32{ 1, 2 })) != 2) return error.TestFailed;
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
