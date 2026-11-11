// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134915904
// LeetCode 94. 二叉树的中序遍历 — Zig 版（方案7）
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

fn inorderTraversal(root: ?*TreeNode, alloc: std.mem.Allocator) std.ArrayList(i32) { // 定义函数/方法 inorderTraversal
    var res = std.ArrayList(i32).init(alloc); // 把 std.ArrayList(i32).init(alloc) 存入 结果
    const D = struct { // 把 struct { 存入 D
        fn dfs(n: ?*TreeNode, out: *std.ArrayList(i32)) void { // 定义函数/方法 dfs
            const node = n orelse return; // 把 元素个数 orelse return 存入 节点
            dfs(node.left, out); // dfs(节点.左边界, out);
            out.append(node.val) catch unreachable; // 把 节点.值 追加到列表尾部
            dfs(node.right, out); // dfs(节点.右边界, out);
        }
    };
    D.dfs(root, &res); // D.dfs(根节点, 按位与 结果);
    return res; // 返回 结果
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator); // 把 std.堆.ArenaAllocator.init(std.堆.page_allocator) 存入 arena
    defer arena.deinit(); // defer arena.deinit();
    const alloc = arena.allocator(); // 把 arena.allocator() 存入 alloc
    const eq = struct { // 把 struct { 存入 eq
        fn check(a: std.ArrayList(i32), b: []const i32) bool { // 定义判定函数 check
            if (a.items.len != b.len) return false; // 若 数组.items.长度 不等于 b.长度，直接返回 false
            for (b, 0..) |v, i| if (a.items[i] != v) return false; // 把 值) return false; 写入 for (b, 0..) |v, i| if (a.items[i] !
            return true; // 返回 true
        }
    }.check; // }.check;
    if (inorderTraversal(null, alloc).items.len != 0) return error.TestFailed;
    if (!eq(inorderTraversal(try buildTree(alloc, &[_]i32{ 1, -1, 2, -1, 3 }), alloc), &[_]i32{ 1, 2, 3 })) return error.TestFailed;
    if (!eq(inorderTraversal(try buildTree(alloc, &[_]i32{ 1, 2, 3 }), alloc), &[_]i32{ 2, 1, 3 })) return error.TestFailed;
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
