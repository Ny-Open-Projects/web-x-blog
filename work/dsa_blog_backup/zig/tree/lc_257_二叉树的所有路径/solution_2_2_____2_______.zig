// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135666411
// LeetCode 257. 二叉树的所有路径 — Zig 版（方案2）
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

fn binaryTreePaths(root: ?*TreeNode, alloc: std.mem.Allocator) std.ArrayList([]const u8) { // 定义函数/方法 binaryTreePaths
    var paths = std.ArrayList([]const u8).init(alloc); // 把 std.ArrayList([]const u8).init(alloc) 存入 paths
    const D = struct { // 把 struct { 存入 D
        fn dfs(n: ?*TreeNode, path: []const u8, out: *std.ArrayList([]const u8), a: std.mem.Allocator) void { // 定义函数/方法 dfs
            const node = n orelse return; // 把 元素个数 orelse return 存入 节点
            var buf = std.ArrayList(u8).init(a); // 把 std.ArrayList(u8).init(数组) 存入 buf
            buf.appendSlice(path) catch unreachable; // buf.appendSlice(当前路径) catch unreachable;
            buf.writer().print("{d}", .{node.val}) catch unreachable; // 打印输出
            if (node.left == null and node.right == null) { // 若 节点.左边界 等于 null and 节点.右边界 等于 null
                out.append(buf.toOwnedSlice() catch unreachable) catch unreachable; // 把 buf.toOwnedSlice( 追加到列表尾部
                return; // return;
            }
            buf.appendSlice("->") catch unreachable; // buf.appendSlice(「 减 超过 」) catch unreachable;
            const p2 = a.dupe(u8, buf.items) catch unreachable; // 把 数组.dupe(u8, buf.items) catch unreachable 存入 p2
            dfs(node.left, p2, out, a); // dfs(节点.左边界, p2, out, 数组);
            dfs(node.right, buf.toOwnedSlice() catch unreachable, out, a); // dfs(节点.右边界, buf.toOwnedSlice() catch unreachable, out, 数组);
        }
    };
    D.dfs(root, "", &paths, alloc); // D.dfs(根节点, 「」, 按位与 paths, alloc);
    return paths; // 返回 paths
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator); // 把 std.堆.ArenaAllocator.init(std.堆.page_allocator) 存入 arena
    defer arena.deinit(); // defer arena.deinit();
    const alloc = arena.allocator(); // 把 arena.allocator() 存入 alloc
    var paths = binaryTreePaths(try buildTree(alloc, &[_]i32{ 1, 2, 3 }), alloc);
    if (paths.items.len != 2) return error.TestFailed; // 若 paths.items.长度 不等于 2，直接返回 error.TestFailed
    if (!std.mem.eql(u8, paths.items[0], "1->2") or !std.mem.eql(u8, paths.items[1], "1->3")) return error.TestFailed;
    paths = binaryTreePaths(try buildTree(alloc, &[_]i32{1}), alloc);
    if (paths.items.len != 1 or !std.mem.eql(u8, paths.items[0], "1")) return error.TestFailed;
    if (binaryTreePaths(null, alloc).items.len != 0) return error.TestFailed;
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
