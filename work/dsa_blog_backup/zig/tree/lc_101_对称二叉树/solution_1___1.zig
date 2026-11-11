// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135586474
// LeetCode 101. 对称二叉树 — Zig 版（方案1）
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

fn isMirror(l: ?*const TreeNode, r: ?*const TreeNode) bool { // 定义判定函数 isMirror
    if (l == null and r == null) return true; // 若 左指针 等于 null and 右指针 等于 null，直接返回 true
    if (l == null or r == null) return false; // 若 左指针 等于 null or 右指针 等于 null，直接返回 false
    const a = l.?; // 把 左指针.? 存入 数组
    const b = r.?; // 把 右指针.? 存入 b
    return a.val == b.val and isMirror(a.left, b.right) and isMirror(b.left, a.right);
}
fn isSymmetric(root: ?*TreeNode) bool { // 定义判定函数 isSymmetric
    const node = root orelse return true; // 把 根节点 orelse return true 存入 节点
    return isMirror(node.left, node.right); // 返回 isMirror(节点.左边界, 节点.右边界)
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator); // 把 std.堆.ArenaAllocator.init(std.堆.page_allocator) 存入 arena
    defer arena.deinit(); // defer arena.deinit();
    const alloc = arena.allocator(); // 把 arena.allocator() 存入 alloc
    if (!isSymmetric(null)) return error.TestFailed; // 若 取反 isSymmetric(null)，直接返回 error.TestFailed
    if (!isSymmetric(try buildTree(alloc, &[_]i32{ 1, 2, 2, 3, 4, 4, 3 }))) return error.TestFailed;
    if (isSymmetric(try buildTree(alloc, &[_]i32{ 1, 2, 2, -1, 3, -1, 3 }))) return error.TestFailed;
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
