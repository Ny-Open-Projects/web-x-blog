// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/136391511
// LeetCode 404. 左叶子之和 — Zig 版（方案2）
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

fn isLeaf(n: ?*const TreeNode) bool { // 定义判定函数 isLeaf
    const node = n orelse return false; // 把 元素个数 orelse return false 存入 节点
    return node.left == null and node.right == null; // 返回 节点.左边界 等于 null and 节点.右边界 等于 null
}
fn sumOfLeftLeaves(root: ?*TreeNode) i32 { // 定义函数/方法 sumOfLeftLeaves
    const r = root orelse return 0; // 把 根节点 orelse return 0 存入 右指针
    var total: i32 = 0; // 把 0; 写入 var total: i32
    var stack = std.ArrayList(*TreeNode).init(std.heap.page_allocator); // 把 std.ArrayList( 乘 TreeNode).init(std.堆.page_allocator) 存入 栈
    defer stack.deinit(); // defer 栈.deinit();
    stack.append(r) catch unreachable; // 把 右指针 追加到列表尾部
    while (stack.items.len > 0) { // 循环，直到不满足「栈.items.长度 超过 0」
        const node = stack.pop().?; // 把 栈 弹出 ).? 存入 节点
        if (node.left) |l| { // 若 节点.左边界) 按位或 左指针 按位或
            if (isLeaf(l)) total += l.val else stack.append(l) catch unreachable; // 若 isLeaf(左指针)) 总和 累加 左指针.值 else 栈 追加 左指针) catch unreachable;
        }
        if (node.right) |rt| stack.append(rt) catch unreachable; // 若 节点.右边界) 按位或 rt 按位或 栈 追加 rt) catch unreachable;
    }
    return total; // 返回 总和
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator); // 把 std.堆.ArenaAllocator.init(std.堆.page_allocator) 存入 arena
    defer arena.deinit(); // defer arena.deinit();
    const alloc = arena.allocator(); // 把 arena.allocator() 存入 alloc
    if (sumOfLeftLeaves(try buildTree(alloc, &[_]i32{ 3, 9, 20, -1, -1, 15, 7 })) != 24) return error.TestFailed;
    if (sumOfLeftLeaves(null) != 0) return error.TestFailed; // 若 sumOfLeftLeaves(null) 不等于 0，直接返回 error.TestFailed
    if (sumOfLeftLeaves(try buildTree(alloc, &[_]i32{ 1, 2, 3, 4, 5 })) != 4) return error.TestFailed;
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
