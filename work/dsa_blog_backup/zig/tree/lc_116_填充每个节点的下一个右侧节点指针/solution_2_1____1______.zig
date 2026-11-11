// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145386215
// LeetCode 116. 填充每个节点的下一个右侧节点指针 — Zig 版（方案2）
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

const NNode = struct { val: i32, left: ?*NNode, right: ?*NNode, next: ?*NNode };
fn nnew(v: i32, alloc: std.mem.Allocator) *NNode { // 定义函数/方法 nnew
    const n = alloc.create(NNode) catch unreachable; // 把 alloc.create(NNode) catch unreachable 存入 元素个数
    n.* = .{ .val = v, .left = null, .right = null, .next = null };
    return n; // 返回 元素个数
}
fn buildNTree(vals: []const i32, alloc: std.mem.Allocator) ?*NNode { // 定义函数/方法 buildNTree
    if (vals.len == 0) return null; // 若 vals.长度 等于 0，直接返回 null
    const root = nnew(vals[0], alloc); // 把 nnew(vals[0], alloc) 存入 根节点
    var q = std.ArrayList(*NNode).init(alloc); // 把 std.ArrayList( 乘 NNode).init(alloc) 存入 节点
    q.append(root) catch unreachable; // 把 根节点 追加到列表尾部
    var head: usize = 0; // 把 0; 写入 var head: usize
    var i: usize = 1; // 把 1; 写入 var i: usize
    while (head < q.items.len and i < vals.len) { // 循环，直到不满足「头节点 小于 节点.items.长度 and 下标 i 小于 vals.长度」
        const node = q.items[head]; // 把 节点.items[头节点] 存入 节点
        head += 1; // 头节点累加 1
        if (i < vals.len) {
            const c = nnew(vals[i], alloc);
            node.left = c;
            q.append(c) catch unreachable;
            i += 1;
        }
        if (i < vals.len) {
            const c = nnew(vals[i], alloc);
            node.right = c;
            q.append(c) catch unreachable;
            i += 1;
        }
    }
    return root; // 返回 根节点
}
fn connect(root: ?*NNode) ?*NNode { // 定义函数/方法 connect
    const r = root orelse return null; // 把 根节点 orelse return null 存入 右指针
    var q = std.ArrayList(*NNode).init(std.heap.page_allocator); // 把 std.ArrayList( 乘 NNode).init(std.堆.page_allocator) 存入 节点
    defer q.deinit(); // defer 节点.deinit();
    q.append(r) catch unreachable; // 把 右指针 追加到列表尾部
    var head: usize = 0; // 把 0; 写入 var head: usize
    while (head < q.items.len) { // 循环，直到不满足「头节点 小于 节点.items.长度」
        const size = q.items.len - head; // 把 节点.items.长度 减 头节点 存入 大小
        var prev: ?*NNode = null; // 把 null; 写入 var prev: ?*NNode
        for (0..size) |_| { // 让 _ 从 0 走到 大小 减一
            const node = q.items[head]; // 把 节点.items[头节点] 存入 节点
            head += 1; // 头节点累加 1
            if (prev) |p| p.next = node; // 若 前一个) 按位或 节点 按位或 节点.下一个 赋值为 节点;
            prev = node; // 把 节点; 写入 前一个
            if (node.left) |c| q.append(c) catch unreachable; // 若 节点.左边界) 按位或 字符 按位或 节点 追加 字符) catch unreachable;
            if (node.right) |c| q.append(c) catch unreachable; // 若 节点.右边界) 按位或 字符 按位或 节点 追加 字符) catch unreachable;
        }
    }
    return r; // 返回 右指针
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator); // 把 std.堆.ArenaAllocator.init(std.堆.page_allocator) 存入 arena
    defer arena.deinit(); // defer arena.deinit();
    const alloc = arena.allocator(); // 把 arena.allocator() 存入 alloc
    if (connect(null) != null) return error.TestFailed; // 若 connect(null) 不等于 null，直接返回 error.TestFailed
    const root = connect(buildNTree(&[_]i32{ 1, 2, 3, 4, 5, 6, 7 }, alloc)).?;
    var level: usize = 0; // 把 0; 写入 var level: usize
    var cur: ?*NNode = root; // 把 根节点; 写入 var cur: ?*NNode
    const want = [_][]const i32{ &[_]i32{1}, &[_]i32{ 2, 3 }, &[_]i32{ 4, 5, 6, 7 } };
    while (cur) |c| { // 循环，直到不满足「当前值) 按位或 字符 按位或」
        var cnt: usize = 0; // 把 0; 写入 var cnt: usize
        var node: ?*NNode = c; // 把 字符; 写入 var node: ?*NNode
        while (node) |n| { // 循环，直到不满足「节点) 按位或 元素个数 按位或」
            if (cnt >= want[level].len or n.val != want[level][cnt]) return error.TestFailed;
            cnt += 1; // 计数累加 1
            node = n.next; // 把 元素个数.下一个; 写入 节点
        }
        if (cnt != want[level].len) return error.TestFailed; // 若 计数 不等于 want[level].长度，直接返回 error.TestFailed
        cur = c.left; // 把 字符.左边界; 写入 当前值
        level += 1; // level累加 1
    }
    if (level != 3) return error.TestFailed; // 若 level 不等于 3，直接返回 error.TestFailed
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
