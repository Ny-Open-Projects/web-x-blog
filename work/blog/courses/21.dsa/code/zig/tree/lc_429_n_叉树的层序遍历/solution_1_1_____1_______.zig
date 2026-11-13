// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/137532387
// LeetCode 429. N叉树的层序遍历 — Zig 版（方案1）
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

const NNode = struct { val: i32, children: std.ArrayList(*NNode) };
fn nnew(v: i32, alloc: std.mem.Allocator) *NNode { // 定义函数/方法 nnew
    const n = alloc.create(NNode) catch unreachable; // 把 alloc.create(NNode) catch unreachable 存入 元素个数
    n.* = .{ .val = v, .children = std.ArrayList(*NNode).init(alloc) };
    return n; // 返回 元素个数
}
fn levelOrder(root: ?*NNode, alloc: std.mem.Allocator) std.ArrayList(std.ArrayList(i32)) { // 定义函数/方法 levelOrder
    var res = std.ArrayList(std.ArrayList(i32)).init(alloc); // 把 std.ArrayList(std.ArrayList(i32)).init(alloc) 存入 结果
    const r = root orelse return res; // 把 根节点 orelse return 结果 存入 右指针
    var q = std.ArrayList(*NNode).init(alloc); // 把 std.ArrayList( 乘 NNode).init(alloc) 存入 节点
    q.append(r) catch unreachable; // 把 右指针 追加到列表尾部
    var head: usize = 0; // 把 0; 写入 var head: usize
    while (head < q.items.len) { // 循环，直到不满足「头节点 小于 节点.items.长度」
        const size = q.items.len - head; // 把 节点.items.长度 减 头节点 存入 大小
        var level = std.ArrayList(i32).init(alloc); // 把 std.ArrayList(i32).init(alloc) 存入 level
        for (0..size) |_| { // 让 _ 从 0 走到 大小 减一
            const n = q.items[head]; // 把 节点.items[头节点] 存入 元素个数
            head += 1; // 头节点累加 1
            level.append(n.val) catch unreachable; // 把 元素个数.值 追加到列表尾部
            for (n.children.items) |c| q.append(c) catch unreachable; // 逐个取出 元素个数.children.items 的元素（字符）
        }
        res.append(level) catch unreachable; // 把 level 追加到列表尾部
    }
    return res; // 返回 结果
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator); // 把 std.堆.ArenaAllocator.init(std.堆.page_allocator) 存入 arena
    defer arena.deinit(); // defer arena.deinit();
    const alloc = arena.allocator(); // 把 arena.allocator() 存入 alloc
    const root = nnew(1, alloc); // 把 nnew(1, alloc) 存入 根节点
    const c3 = nnew(3, alloc); // 把 nnew(3, alloc) 存入 c3
    c3.children.append(nnew(5, alloc)) catch unreachable; // 把 nnew(5, alloc 追加到列表尾部
    c3.children.append(nnew(6, alloc)) catch unreachable; // 把 nnew(6, alloc 追加到列表尾部
    root.children.append(c3) catch unreachable; // 把 c3 追加到列表尾部
    root.children.append(nnew(2, alloc)) catch unreachable; // 把 nnew(2, alloc 追加到列表尾部
    root.children.append(nnew(4, alloc)) catch unreachable; // 把 nnew(4, alloc 追加到列表尾部
    const res = levelOrder(root, alloc); // 把 levelOrder(根节点, alloc) 存入 结果
    if (res.items.len != 3) return error.TestFailed; // 若 结果.items.长度 不等于 3，直接返回 error.TestFailed
    if (res.items[0].items[0] != 1) return error.TestFailed; // 若 结果.items[0].items[0] 不等于 1，直接返回 error.TestFailed
    if (res.items[1].items[0] != 3 or res.items[1].items[1] != 2 or res.items[1].items[2] != 4) return error.TestFailed;
    if (res.items[2].items[0] != 5 or res.items[2].items[1] != 6) return error.TestFailed;
    if (levelOrder(null, alloc).items.len != 0) return error.TestFailed;
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
