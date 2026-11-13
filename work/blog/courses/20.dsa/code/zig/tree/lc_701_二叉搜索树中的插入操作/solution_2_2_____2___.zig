// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/137040405
// LeetCode 701. 二叉搜索树中的插入操作 — Zig 版（方案2）
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
fn sameTree(p: ?*const TreeNode, q: ?*const TreeNode) bool { // 定义函数/方法 sameTree
    if (p == null and q == null) return true; // 若 节点 等于 null and 节点 等于 null，直接返回 true
    if (p == null or q == null) return false; // 若 节点 等于 null or 节点 等于 null，直接返回 false
    const a = p.?; // 把 节点.? 存入 数组
    const b = q.?; // 把 节点.? 存入 b
    return a.val == b.val and sameTree(a.left, b.left) and sameTree(a.right, b.right);
}
fn levelsFlat(root: ?*TreeNode, out: *std.ArrayList(i32)) void { // 定义函数/方法 levelsFlat
    const r = root orelse return; // 把 根节点 orelse return 存入 右指针
    var q = std.ArrayList(*TreeNode).init(std.heap.page_allocator);
    defer q.deinit(); // defer 节点.deinit();
    q.append(r) catch unreachable; // 把 右指针 追加到列表尾部
    var head: usize = 0; // 把 0; 写入 var head: usize
    while (head < q.items.len) { // 循环，直到不满足「头节点 小于 节点.items.长度」
        const node = q.items[head]; // 把 节点.items[头节点] 存入 节点
        head += 1; // 头节点累加 1
        out.append(node.val) catch unreachable; // 把 节点.值 追加到列表尾部
        if (node.left) |c| q.append(c) catch unreachable; // 若 节点.左边界) 按位或 字符 按位或 节点 追加 字符) catch unreachable;
        if (node.right) |c| q.append(c) catch unreachable; // 若 节点.右边界) 按位或 字符 按位或 节点 追加 字符) catch unreachable;
    }
}

fn insertIntoBST(root: ?*TreeNode, val: i32, alloc: std.mem.Allocator) ?*TreeNode { // 定义函数/方法 insertIntoBST
    const r = root orelse { // 把 根节点 orelse { 存入 右指针
        const n = alloc.create(TreeNode) catch unreachable; // 把 alloc.create(TreeNode) catch unreachable 存入 元素个数
        n.* = .{ .val = val, .left = null, .right = null }; // 把 { .值 赋值为 值, .左边界 赋值为 null, .右边界 赋值为 null }; 写入 n.*
        return n; // 返回 元素个数
    };
    var pos: *TreeNode = r; // 把 右指针; 写入 var pos: *TreeNode
    while (true) { // 循环，直到不满足「true」
        if (val < pos.val) { // 若 值 小于 pos.值
            if (pos.left) |c| {
                pos = c;
            } else { // 若 pos.左边界) 按位或 字符 按位或 { pos 赋值为 字符; } else
                const n = alloc.create(TreeNode) catch unreachable; // 把 alloc.create(TreeNode) catch unreachable 存入 元素个数
                n.* = .{ .val = val, .left = null, .right = null }; // 把 { .值 赋值为 值, .左边界 赋值为 null, .右边界 赋值为 null }; 写入 n.*
                pos.left = n; // 把 元素个数; 写入 左边界
                break; // 跳出循环
            }
        } else { // 否则
            if (pos.right) |c| {
                pos = c;
            } else { // 若 pos.右边界) 按位或 字符 按位或 { pos 赋值为 字符; } else
                const n = alloc.create(TreeNode) catch unreachable; // 把 alloc.create(TreeNode) catch unreachable 存入 元素个数
                n.* = .{ .val = val, .left = null, .right = null }; // 把 { .值 赋值为 值, .左边界 赋值为 null, .右边界 赋值为 null }; 写入 n.*
                pos.right = n; // 把 元素个数; 写入 右边界
                break; // 跳出循环
            }
        }
    }
    return r; // 返回 右指针
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator); // 把 std.堆.ArenaAllocator.init(std.堆.page_allocator) 存入 arena
    defer arena.deinit(); // defer arena.deinit();
    const alloc = arena.allocator(); // 把 arena.allocator() 存入 alloc
    var out = std.ArrayList(i32).init(std.heap.page_allocator); // 把 std.ArrayList(i32).init(std.堆.page_allocator) 存入 out
    defer out.deinit(); // defer out.deinit();
    const t = try buildTree(alloc, &[_]i32{ 4, 2, 7, 1, 3 }); // 把 try buildTree(alloc, 按位与 [_]i32{ 4, 2, 7, 1, 3 }) 存入 另一字符串
    levelsFlat(insertIntoBST(t, 5, alloc), &out); // levelsFlat(insertIntoBST(另一字符串, 5, alloc), 按位与 out);
    const want = [_]i32{ 4, 2, 7, 1, 3, 5 }; // 把 [_]i32{ 4, 2, 7, 1, 3, 5 } 存入 want
    if (out.items.len != want.len) return error.TestFailed; // 若 out.items.长度 不等于 want.长度，直接返回 error.TestFailed
    for (want, 0..) |w, i| if (out.items[i] != w) return error.TestFailed;
    out.clearRetainingCapacity(); // out.clearRetainingCapacity();
    levelsFlat(insertIntoBST(null, 5, alloc), &out); // levelsFlat(insertIntoBST(null, 5, alloc), 按位与 out);
    if (out.items.len != 1 or out.items[0] != 5) return error.TestFailed;
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
