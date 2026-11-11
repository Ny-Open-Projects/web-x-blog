// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/136210437
// LeetCode 222. 完全二叉树的节点个数 — Zig 版（方案1）
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

fn countNodes(root: ?*TreeNode) i32 { // 定义函数/方法 countNodes
    const node = root orelse return 0; // 把 根节点 orelse return 0 存入 节点
    var lh: i32 = 0; // 把 0; 写入 var lh: i32
    var r: ?*TreeNode = node.left; // 把 节点.左边界; 写入 var r: ?*TreeNode
    while (r) |x| {
        lh += 1;
        r = x.left;
    } // 循环，直到不满足「右指针) 按位或 x 按位或 { lh 累加 1; 右指针 赋值为 x.左边界; }」
    var rh: i32 = 0; // 把 0; 写入 var rh: i32
    r = node.right; // 把 节点.右边界; 写入 右指针
    while (r) |x| {
        rh += 1;
        r = x.right;
    } // 循环，直到不满足「右指针) 按位或 x 按位或 { rh 累加 1; 右指针 赋值为 x.右边界; }」
    if (lh == rh) return (@as(i32, 1) << @intCast(lh + 1)) - 1; // 若 lh 等于 rh，直接返回 (@as(i32, 1) 小于 小于 @intCast(lh 加 1)) 减 1
    return 1 + countNodes(node.left) + countNodes(node.right); // 返回 1 加 countNodes(节点.左边界) 加 countNodes(节点.右边界)
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator); // 把 std.堆.ArenaAllocator.init(std.堆.page_allocator) 存入 arena
    defer arena.deinit(); // defer arena.deinit();
    const alloc = arena.allocator(); // 把 arena.allocator() 存入 alloc
    if (countNodes(try buildTree(alloc, &[_]i32{ 1, 2, 3, 4, 5, 6 })) != 6) return error.TestFailed;
    if (countNodes(null) != 0) return error.TestFailed; // 若 countNodes(null) 不等于 0，直接返回 error.TestFailed
    if (countNodes(try buildTree(alloc, &[_]i32{1})) != 1) return error.TestFailed;
    if (countNodes(try buildTree(alloc, &[_]i32{ 1, 2, 3, 4, 5, 6, 7, 8 })) != 8) return error.TestFailed;
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
