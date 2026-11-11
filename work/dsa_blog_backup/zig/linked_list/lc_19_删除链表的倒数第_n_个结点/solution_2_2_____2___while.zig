// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133746567
// LeetCode 19. 删除链表的倒数第N个结点 — Zig 版（方案2）
const std = @import("std"); // 把 @import(「std」) 存入 std
const LNode = struct { val: i32, next: ?*LNode }; // 把 struct { 值: i32, 下一个: ? 乘 LNode } 存入 LNode
fn buildList(alloc: std.mem.Allocator, vals: []const i32) ?*LNode { // 定义函数/方法 buildList
    var head: ?*LNode = null; // 把 null; 写入 var head: ?*LNode
    var tail: ?*LNode = null; // 把 null; 写入 var tail: ?*LNode
    for (vals) |v| { // 逐个取出 vals 的元素（值）
        const n = alloc.create(LNode) catch unreachable; // 把 alloc.create(LNode) catch unreachable 存入 元素个数
        n.* = .{ .val = v, .next = null }; // 把 { .值 赋值为 值, .下一个 赋值为 null }; 写入 n.*
        if (tail) |t| t.next = n else head = n; // 若 尾节点) 按位或 另一字符串 按位或 另一字符串.下一个 赋值为 元素个数 else 头节点 赋值为 元素个数;
        tail = n; // 把 元素个数; 写入 尾节点
    }
    return head; // 返回 头节点
}
fn toVec(h: ?*LNode, out: *std.ArrayList(i32)) void { // 定义函数/方法 toVec
    var cur = h; // 把 h 存入 当前值
    while (cur) |n| {
        out.append(n.val) catch unreachable;
        cur = n.next;
    }
}
fn removeNthFromEnd(head: ?*LNode, n: i32) ?*LNode { // 定义函数/方法 removeNthFromEnd
    // 重建法：zig 指针操作安全
    var vals: [4096]i32 = undefined; // 把 undefined; 写入 var vals: [4096]i32
    var len: usize = 0; // 把 0; 写入 var len: usize
    var cur = head; // 把 头节点 存入 当前值
    while (cur) |node| { // 循环，直到不满足「当前值) 按位或 节点 按位或」
        vals[len] = node.val; // 把 节点.值; 写入 vals[len]
        len += 1; // 长度累加 1
        cur = node.next; // 把 节点.下一个; 写入 当前值
    }
    const idx = len - @as(usize, @intCast(n)); // 把 长度 减 @as(usize, @intCast(元素个数)) 存入 idx
    var out: ?*LNode = null; // 把 null; 写入 var out: ?*LNode
    var tail: ?*LNode = null; // 把 null; 写入 var tail: ?*LNode
    for (0..len) |i| { // 让 下标 i 从 0 走到 长度 减一
        if (i == idx) continue; // 若 下标 i 等于 idx) continue;
        const nd = std.heap.page_allocator.create(LNode) catch unreachable; // 把 std.堆.page_allocator.create(LNode) catch unreachable 存入 nd
        nd.* = .{ .val = vals[i], .next = null }; // 把 { .值 赋值为 vals[下标 i], .下一个 赋值为 null }; 写入 nd.*
        if (tail) |t| t.next = nd else out = nd; // 若 尾节点) 按位或 另一字符串 按位或 另一字符串.下一个 赋值为 nd else out 赋值为 nd;
        tail = nd; // 把 nd; 写入 尾节点
    }
    return out; // 返回 out
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator); // 把 std.堆.ArenaAllocator.init(std.堆.page_allocator) 存入 arena
    defer arena.deinit(); // defer arena.deinit();
    const alloc = arena.allocator(); // 把 arena.allocator() 存入 alloc
    var out = std.ArrayList(i32).init(std.heap.page_allocator); // 把 std.ArrayList(i32).init(std.堆.page_allocator) 存入 out
    defer out.deinit(); // defer out.deinit();
    toVec(removeNthFromEnd(buildList(alloc, &[_]i32{ 1, 2, 3, 4, 5 }), 2), &out);
    if (out.items.len != 4 or out.items[3] != 5) return error.TestFailed;
    out.clearRetainingCapacity(); // out.clearRetainingCapacity();
    if (removeNthFromEnd(buildList(alloc, &[_]i32{1}), 1) != null) return error.TestFailed;
    toVec(removeNthFromEnd(buildList(alloc, &[_]i32{ 1, 2 }), 2), &out);
    if (out.items.len != 1 or out.items[0] != 2) return error.TestFailed;
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
