// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135637716
// LeetCode 114. 二叉树展开为链表 — Zig 版（方案1）
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

fn flatten(root: ?*TreeNode) void { // 定义函数/方法 flatten
    const D = struct { // 把 struct { 存入 D
        var prev: ?*TreeNode = null; // 把 null; 写入 var prev: ?*TreeNode
        fn dfs(node: ?*TreeNode) void { // 定义函数/方法 dfs
            const n = node orelse return; // 把 节点 orelse return 存入 元素个数
            dfs(n.right); // dfs(元素个数.右边界);
            dfs(n.left); // dfs(元素个数.左边界);
            n.right = prev; // 把 前一个; 写入 右边界
            n.left = null; // 把 null; 写入 左边界
            prev = n; // 把 元素个数; 写入 前一个
        }
    };
    D.prev = null; // 把 null; 写入 前一个
    D.dfs(root); // D.dfs(根节点);
}
fn chain(root: ?*TreeNode, out: *std.ArrayList(i32)) void { // 定义函数/方法 chain
    var cur = root; // 把 根节点 存入 当前值
    while (cur) |n| { // 循环，直到不满足「当前值) 按位或 元素个数 按位或」
        if (n.left != null) return; // left 必须为空：留给上层判长度失败
        out.append(n.val) catch unreachable; // 把 元素个数.值 追加到列表尾部
        cur = n.right; // 把 元素个数.右边界; 写入 当前值
    }
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator); // 把 std.堆.ArenaAllocator.init(std.堆.page_allocator) 存入 arena
    defer arena.deinit(); // defer arena.deinit();
    const alloc = arena.allocator(); // 把 arena.allocator() 存入 alloc
    var out = std.ArrayList(i32).init(std.heap.page_allocator); // 把 std.ArrayList(i32).init(std.堆.page_allocator) 存入 out
    defer out.deinit(); // defer out.deinit();
    const t = try buildTree(alloc, &[_]i32{ 1, 2, 5, 3, 4, -1, 6 });
    flatten(t); // flatten(另一字符串);
    chain(t, &out); // chain(另一字符串, 按位与 out);
    const w1 = [_]i32{ 1, 2, 3, 4, 5, 6 }; // 把 [_]i32{ 1, 2, 3, 4, 5, 6 } 存入 w1
    if (out.items.len != w1.len) return error.TestFailed; // 若 out.items.长度 不等于 w1.长度，直接返回 error.TestFailed
    for (w1, 0..) |w, i| if (out.items[i] != w) return error.TestFailed;
    out.clearRetainingCapacity(); // out.clearRetainingCapacity();
    const t2 = try buildTree(alloc, &[_]i32{7}); // 把 try buildTree(alloc, 按位与 [_]i32{7}) 存入 t2
    flatten(t2); // flatten(t2);
    chain(t2, &out); // chain(t2, 按位与 out);
    if (out.items.len != 1 or out.items[0] != 7) return error.TestFailed;
    flatten(null); // flatten(null);
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
