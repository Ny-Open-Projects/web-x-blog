// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133886377
// LeetCode 237. 删除链表中的节点 — Zig 版（方案3）
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
fn deleteNode(node: *LNode) void { // 定义函数/方法 deleteNode
    const next = node.next.?; // 把 节点.下一个.? 存入 下一个
    node.val = next.val; // 把 下一个.值; 写入 值
    node.next = next.next; // 把 下一个.下一个; 写入 下一个
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator); // 把 std.堆.ArenaAllocator.init(std.堆.page_allocator) 存入 arena
    defer arena.deinit(); // defer arena.deinit();
    const alloc = arena.allocator(); // 把 arena.allocator() 存入 alloc
    var out = std.ArrayList(i32).init(std.heap.page_allocator); // 把 std.ArrayList(i32).init(std.堆.page_allocator) 存入 out
    defer out.deinit(); // defer out.deinit();
    const l = buildList(alloc, &[_]i32{ 4, 5, 1, 9 }).?; // 把 buildList(alloc, 按位与 [_]i32{ 4, 5, 1, 9 }).? 存入 左指针
    deleteNode(l.next.?); // deleteNode(左指针.下一个.?);
    toVec(l, &out); // toVec(左指针, 按位与 out);
    if (out.items.len != 3 or out.items[0] != 4 or out.items[1] != 1 or out.items[2] != 9) return error.TestFailed;
    out.clearRetainingCapacity(); // out.clearRetainingCapacity();
    const l2 = buildList(alloc, &[_]i32{ 1, 2, 3 }).?; // 把 buildList(alloc, 按位与 [_]i32{ 1, 2, 3 }).? 存入 l2
    deleteNode(l2.next.?); // deleteNode(l2.下一个.?);
    toVec(l2, &out); // toVec(l2, 按位与 out);
    if (out.items.len != 2 or out.items[0] != 1 or out.items[1] != 3) return error.TestFailed;
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
