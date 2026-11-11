// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/136684493
// LeetCode 230. 二叉搜索树中第K小的元素 — Zig 版（方案2）
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

fn kthSmallest(root: ?*TreeNode, k_in: i32) i32 { // 定义函数/方法 kthSmallest
    var k = k_in; // 把 k_in 存入 下标 k
    var stack = std.ArrayList(*TreeNode).init(std.heap.page_allocator); // 把 std.ArrayList( 乘 TreeNode).init(std.堆.page_allocator) 存入 栈
    defer stack.deinit(); // defer 栈.deinit();
    var cur: ?*TreeNode = root; // 把 根节点; 写入 var cur: ?*TreeNode
    while (cur != null or stack.items.len > 0) { // 循环，直到不满足「当前值 不等于 null or 栈.items.长度 超过 0」
        while (cur) |c| { // 循环，直到不满足「当前值) 按位或 字符 按位或」
            stack.append(c) catch unreachable; // 把 字符 追加到列表尾部
            cur = c.left; // 把 字符.左边界; 写入 当前值
        }
        const node = stack.pop().?; // 把 栈 弹出 ).? 存入 节点
        k -= 1; // 下标 k累减 1
        if (k == 0) return node.val; // 若 下标 k 等于 0，直接返回 节点.值
        cur = node.right; // 把 节点.右边界; 写入 当前值
    }
    return -1; // 返回 减 1
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator); // 把 std.堆.ArenaAllocator.init(std.堆.page_allocator) 存入 arena
    defer arena.deinit(); // defer arena.deinit();
    const alloc = arena.allocator(); // 把 arena.allocator() 存入 alloc
    const t = try buildTree(alloc, &[_]i32{ 3, 1, 4, -1, 2 });
    if (kthSmallest(t, 1) != 1) return error.TestFailed; // 若 kthSmallest(另一字符串, 1) 不等于 1，直接返回 error.TestFailed
    if (kthSmallest(t, 2) != 2) return error.TestFailed; // 若 kthSmallest(另一字符串, 2) 不等于 2，直接返回 error.TestFailed
    const t2 = try buildTree(alloc, &[_]i32{ 5, 3, 6, 2, 4, -1, -1, 1 });
    if (kthSmallest(t2, 3) != 3) return error.TestFailed; // 若 kthSmallest(t2, 3) 不等于 3，直接返回 error.TestFailed
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
