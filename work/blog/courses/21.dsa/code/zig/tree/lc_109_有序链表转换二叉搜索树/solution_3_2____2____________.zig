// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135270549
// LeetCode 109. 有序链表转换二叉搜索树 — Zig 版（方案3）
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

const ListNode = struct { val: i32, next: ?*ListNode }; // 把 struct { 值: i32, 下一个: ? 乘 ListNode } 存入 ListNode
fn buildList(alloc: std.mem.Allocator, vals: []const i32) ?*ListNode { // 定义函数/方法 buildList
    var head: ?*ListNode = null; // 把 null; 写入 var head: ?*ListNode
    var tail: ?*ListNode = null; // 把 null; 写入 var tail: ?*ListNode
    for (vals) |v| { // 逐个取出 vals 的元素（值）
        const n = alloc.create(ListNode) catch unreachable; // 把 alloc.create(ListNode) catch unreachable 存入 元素个数
        n.* = .{ .val = v, .next = null }; // 把 { .值 赋值为 值, .下一个 赋值为 null }; 写入 n.*
        if (tail) |t| t.next = n else head = n; // 若 尾节点) 按位或 另一字符串 按位或 另一字符串.下一个 赋值为 元素个数 else 头节点 赋值为 元素个数;
        tail = n; // 把 元素个数; 写入 尾节点
    }
    return head; // 返回 头节点
}
fn buildBst(nodes: []const i32, left: isize, right: isize, alloc: std.mem.Allocator) ?*TreeNode { // 定义函数/方法 buildBst
    if (left > right) return null; // 若 左边界 超过 右边界，直接返回 null
    const mid = left + @divTrunc(right - left, 2); // 把 左边界 加 @divTrunc(右边界 减 左边界, 2) 存入 中点
    const root = alloc.create(TreeNode) catch unreachable; // 把 alloc.create(TreeNode) catch unreachable 存入 根节点
    root.* = .{ .val = nodes[@intCast(mid)], .left = null, .right = null };
    root.left = buildBst(nodes, left, mid - 1, alloc); // 把 buildBst(nodes, 左边界, 中点 减 1, alloc); 写入 左边界
    root.right = buildBst(nodes, mid + 1, right, alloc); // 把 buildBst(nodes, 中点 加 1, 右边界, alloc); 写入 右边界
    return root; // 返回 根节点
}
fn sortedListToBST(head: ?*ListNode, alloc: std.mem.Allocator) ?*TreeNode { // 定义函数/方法 sortedListToBST
    var nodes = std.ArrayList(i32).init(alloc); // 把 std.ArrayList(i32).init(alloc) 存入 nodes
    var cur = head; // 把 头节点 存入 当前值
    while (cur) |c| { // 循环，直到不满足「当前值) 按位或 字符 按位或」
        nodes.append(c.val) catch unreachable; // 把 字符.值 追加到列表尾部
        cur = c.next; // 把 字符.下一个; 写入 当前值
    }
    if (nodes.items.len == 0) return null; // 若 nodes.items.长度 等于 0，直接返回 null
    return buildBst(nodes.items, 0, @as(isize, @intCast(nodes.items.len)) - 1, alloc);
}
fn inorderFn(n: ?*TreeNode, out: *std.ArrayList(i32)) void { // 定义函数/方法 inorderFn
    const node = n orelse return; // 把 元素个数 orelse return 存入 节点
    inorderFn(node.left, out); // inorderFn(节点.左边界, out);
    out.append(node.val) catch unreachable; // 把 节点.值 追加到列表尾部
    inorderFn(node.right, out); // inorderFn(节点.右边界, out);
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator); // 把 std.堆.ArenaAllocator.init(std.堆.page_allocator) 存入 arena
    defer arena.deinit(); // defer arena.deinit();
    const alloc = arena.allocator(); // 把 arena.allocator() 存入 alloc
    if (sortedListToBST(null, alloc) != null) return error.TestFailed;
    const t = sortedListToBST(buildList(alloc, &[_]i32{ 1, 2, 3 }), alloc).?;
    var out = std.ArrayList(i32).init(std.heap.page_allocator); // 把 std.ArrayList(i32).init(std.堆.page_allocator) 存入 out
    defer out.deinit(); // defer out.deinit();
    inorderFn(t, &out); // inorderFn(另一字符串, 按位与 out);
    const want = [_]i32{ 1, 2, 3 }; // 把 [_]i32{ 1, 2, 3 } 存入 want
    if (out.items.len != want.len) return error.TestFailed; // 若 out.items.长度 不等于 want.长度，直接返回 error.TestFailed
    for (want, 0..) |w, i| if (out.items[i] != w) return error.TestFailed;
    if (t.val != 2 or t.left.?.val != 1 or t.right.?.val != 3) return error.TestFailed;
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
