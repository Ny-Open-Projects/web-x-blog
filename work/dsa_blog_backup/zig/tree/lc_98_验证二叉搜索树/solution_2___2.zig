// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135314196
// LeetCode 98. 验证二叉搜索树 — Zig 版（方案2）
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

const BN = struct { n: *TreeNode, low: ?i64, high: ?i64 }; // 把 struct { 元素个数: 乘 TreeNode, low: ?i64, high: ?i64 } 存入 BN
fn isValidBST(root: ?*TreeNode) bool { // 定义判定函数 isValidBST
    const r = root orelse return true; // 把 根节点 orelse return true 存入 右指针
    var stack = std.ArrayList(BN).init(std.heap.page_allocator); // 把 std.ArrayList(BN).init(std.堆.page_allocator) 存入 栈
    defer stack.deinit(); // defer 栈.deinit();
    stack.append(.{ .n = r, .low = null, .high = null }) catch unreachable; // 把 { .元素个数 赋值为 右指针, .low 赋值为 null, .high 赋值为 null } 追加到列表尾部
    while (stack.items.len > 0) { // 循环，直到不满足「栈.items.长度 超过 0」
        const b = stack.pop().?; // 把 栈 弹出 ).? 存入 b
        const v: i64 = b.n.val; // 把 b.元素个数.值; 写入 const v: i64
        if (b.low) |l| if (v <= l) return false; // 若 b.low) 按位或 左指针 按位或 if (值 不超过 左指针，直接返回 false
        if (b.high) |h| if (v >= h) return false; // 若 b.high) 按位或 h 按位或 if (值 不低于 h，直接返回 false
        if (b.n.right) |c| stack.append(.{ .n = c, .low = v, .high = b.high }) catch unreachable;
        if (b.n.left) |c| stack.append(.{ .n = c, .low = b.low, .high = v }) catch unreachable;
    }
    return true; // 返回 true
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator); // 把 std.堆.ArenaAllocator.init(std.堆.page_allocator) 存入 arena
    defer arena.deinit(); // defer arena.deinit();
    const alloc = arena.allocator(); // 把 arena.allocator() 存入 alloc
    if (!isValidBST(try buildTree(alloc, &[_]i32{ 2, 1, 3 }))) return error.TestFailed;
    if (isValidBST(try buildTree(alloc, &[_]i32{ 5, 1, 4, -1, -1, 3, 6 }))) return error.TestFailed;
    if (!isValidBST(null)) return error.TestFailed; // 若 取反 isValidBST(null)，直接返回 error.TestFailed
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
