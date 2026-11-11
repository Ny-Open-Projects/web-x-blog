// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135572347
// LeetCode 543. 二叉树的直径 — Zig 版（方案1）
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

fn diameterOfBinaryTree(root: ?*TreeNode) i32 { // 定义函数/方法 diameterOfBinaryTree
    var ans: i32 = 0; // 把 0; 写入 var ans: i32
    const D = struct { // 把 struct { 存入 D
        fn depth(n: ?*TreeNode, best: *i32) i32 { // 定义函数/方法 depth
            const node = n orelse return 0; // 把 元素个数 orelse return 0 存入 节点
            const l = depth(node.left, best); // 把 深度(节点.左边界, 当前最优) 存入 左指针
            const r = depth(node.right, best); // 把 深度(节点.右边界, 当前最优) 存入 右指针
            if (l + r > best.*) best.* = l + r; // 若 左指针 加 右指针 超过 当前最优. 乘 ) 当前最优. 乘 赋值为 左指针 加 右指针;
            return @max(l, r) + 1; // 返回 @取较大值 左指针, 右指针) 加 1
        }
    };
    _ = D.depth(root, &ans); // 把 D.深度(根节点, 按位与 答案); 写入 _
    return ans; // 返回 答案
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator); // 把 std.堆.ArenaAllocator.init(std.堆.page_allocator) 存入 arena
    defer arena.deinit(); // defer arena.deinit();
    const t = try buildTree(arena.allocator(), &[_]i32{ 1, 2, 3, 4, 5 });
    if (diameterOfBinaryTree(t) != 3) return error.TestFailed; // 若 diameterOfBinaryTree(另一字符串) 不等于 3，直接返回 error.TestFailed
    if (diameterOfBinaryTree(null) != 0) return error.TestFailed; // 若 diameterOfBinaryTree(null) 不等于 0，直接返回 error.TestFailed
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
