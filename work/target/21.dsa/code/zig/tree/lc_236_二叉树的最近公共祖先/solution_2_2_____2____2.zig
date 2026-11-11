// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/136528287
// LeetCode 236. 二叉树的最近公共祖先 — Zig 版（方案2）
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

fn lca(n: ?*TreeNode, p: i32, q: i32, found: *i32) i32 { // 定义函数/方法 lca
    const node = n orelse return -1; // 把 元素个数 orelse return 减 1 存入 节点
    if (node.val == p or node.val == q) { // 若 节点.值 等于 节点 or 节点.值 等于 节点
        found.* += 1; // 把 1; 写入 found.* +
        return node.val; // 返回 节点.值
    }
    const before = found.*; // 把 found. 乘 存入 before
    const l = lca(node.left, p, q, found); // 把 lca(节点.左边界, 节点, 节点, found) 存入 左指针
    const r = lca(node.right, p, q, found); // 把 lca(节点.右边界, 节点, 节点, found) 存入 右指针
    if (l != -1 and r != -1) return node.val; // 若 左指针 不等于 减 1 and 右指针 不等于 减 1，直接返回 节点.值
    if (found.* > before) return if (l != -1) l else r; // 若 found. 乘 超过 before，直接返回 if (左指针 不等于 减 1) 左指针 else 右指针
    return -1; // 返回 减 1
}
fn lowestCommonAncestor(root: ?*TreeNode, p: i32, q: i32) i32 { // 定义函数/方法 lowestCommonAncestor
    var found: i32 = 0; // 把 0; 写入 var found: i32
    return lca(root, p, q, &found); // 返回 lca(根节点, 节点, 节点, 按位与 found)
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator); // 把 std.堆.ArenaAllocator.init(std.堆.page_allocator) 存入 arena
    defer arena.deinit(); // defer arena.deinit();
    const t = try buildTree(arena.allocator(), &[_]i32{ 3, 5, 1, 6, 2, 0, 8, -1, -1, 7, 4 });
    if (lowestCommonAncestor(t, 5, 1) != 3) return error.TestFailed;
    if (lowestCommonAncestor(t, 5, 4) != 5) return error.TestFailed;
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
