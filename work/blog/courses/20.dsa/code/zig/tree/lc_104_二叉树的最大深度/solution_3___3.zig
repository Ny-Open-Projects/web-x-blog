// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130815631
// LeetCode 104. 二叉树的最大深度 — Zig 版（方案3：分治递归（紧凑版，附层序/相同树/中序辅助函数））
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

// 辅助：判断两棵树是否相同
fn sameTree(a: ?*TreeNode, b: ?*TreeNode) bool { // 定义函数/方法 sameTree
    if (a == null and b == null) return true; // 若 数组 等于 null and b 等于 null，直接返回 true
    if (a == null or b == null) return false; // 若 数组 等于 null or b 等于 null，直接返回 false
    return a.?.val == b.?.val and sameTree(a.?.left, b.?.left) and sameTree(a.?.right, b.?.right);
}

// 辅助：中序遍历
fn inorderT(n: ?*TreeNode, out: *std.ArrayList(i32)) !void { // 定义函数/方法 inorderT
    const node = n orelse return; // 把 元素个数 orelse return 存入 节点
    try inorderT(node.left, out); // try inorderT(节点.左边界, out);
    try out.append(node.val); // 把 节点.值 追加到列表尾部
    try inorderT(node.right, out); // try inorderT(节点.右边界, out);
}

// 主解法：分治递归，深度 = 1 + max(左子树深度, 右子树深度)
fn maxDepth(root: ?*TreeNode) i32 { // 定义函数/方法 maxDepth
    if (root == null) return 0; // 若 根节点 等于 null，直接返回 0
    const l = maxDepth(root.?.left); // 把 maxDepth(根节点.?.左边界) 存入 左指针
    const r = maxDepth(root.?.right); // 把 maxDepth(根节点.?.右边界) 存入 右指针
    return 1 + @max(l, r); // 返回 1 加 @取较大值 左指针, 右指针)
}

pub fn main() !void { // 程序入口：跑内嵌自测用例
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator); // 把 std.堆.ArenaAllocator.init(std.堆.page_allocator) 存入 arena
    defer arena.deinit(); // defer arena.deinit();
    const allocator = arena.allocator(); // 把 arena.allocator() 存入 allocator

    const t1 = [_]i32{ 3, 9, 20, -1, -1, 15, 7 }; // 把 [_]i32{3, 9, 20, 减 1, 减 1, 15, 7} 存入 t1
    const t2 = [_]i32{ 1, 2, 3, 4, 5, -1, -1, -1, 6 }; // 把 [_]i32{1, 2, 3, 4, 5, 减 1, 减 1, 减 1, 6} 存入 t2
    const t3 = [_]i32{}; // 把 [_]i32{} 存入 t3

    const Case = struct { vals: []const i32, want: i32 }; // 把 struct { vals: []const i32, want: i32 } 存入 Case
    const cases = [_]Case{ // 把 [_]Case{ 存入 cases
        .{ .vals = &t1, .want = 3 },
        .{ .vals = &t2, .want = 4 },
        .{ .vals = &t3, .want = 0 },
    };
    for (cases, 0..) |c, idx| { // for (cases, 0..) 按位或 字符, idx 按位或 {
        const got = maxDepth(try buildTree(allocator, c.vals)); // 把 maxDepth(try buildTree(allocator, 字符.vals)) 存入 got
        if (got != c.want) { // 若 got 不等于 字符.want
            std.debug.print("case {d} failed: got {d} want {d}\n", .{ idx, got, c.want }); // 打印输出
            return error.TestFailed; // 返回 error.TestFailed
        }
    }
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
