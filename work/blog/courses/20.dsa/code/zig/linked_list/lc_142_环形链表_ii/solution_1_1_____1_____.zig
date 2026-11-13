// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133874671
// LeetCode 142. 环形链表II — Zig 版（方案1）
const std = @import("std"); // 把 @import(「std」) 存入 std
const LNode = struct { val: i32, next: ?*LNode }; // 把 struct { 值: i32, 下一个: ? 乘 LNode } 存入 LNode
fn buildWithCycle(alloc: std.mem.Allocator, vals: []const i32, pos: usize) ?*LNode { // 定义函数/方法 buildWithCycle
    var head: ?*LNode = null; // 把 null; 写入 var head: ?*LNode
    var tail: ?*LNode = null; // 把 null; 写入 var tail: ?*LNode
    var tailAt: ?*LNode = null; // 把 null; 写入 var tailAt: ?*LNode
    for (vals, 0..) |v, i| { // for (vals, 0..) 按位或 值, 下标 i 按位或 {
        const n = alloc.create(LNode) catch unreachable; // 把 alloc.create(LNode) catch unreachable 存入 元素个数
        n.* = .{ .val = v, .next = null }; // 把 { .值 赋值为 值, .下一个 赋值为 null }; 写入 n.*
        if (tail) |t| t.next = n else head = n; // 若 尾节点) 按位或 另一字符串 按位或 另一字符串.下一个 赋值为 元素个数 else 头节点 赋值为 元素个数;
        tail = n; // 把 元素个数; 写入 尾节点
        if (i + 1 == pos) tailAt = n; // 若 下标 i 加 1 等于 pos) tailAt 赋值为 元素个数;
    }
    if (tail) |t| t.next = tailAt; // 若 尾节点) 按位或 另一字符串 按位或 另一字符串.下一个 赋值为 tailAt;
    return head; // 返回 头节点
}
fn detectCycle(head: ?*LNode) ?*LNode { // 定义函数/方法 detectCycle
    var slow = head; // 把 头节点 存入 慢指针
    var fast = head; // 把 头节点 存入 快指针
    while (fast != null and fast.?.next != null) { // 循环，直到不满足「快指针 不等于 null and 快指针.?.下一个 不等于 null」
        slow = slow.?.next; // 把 慢指针.?.下一个; 写入 慢指针
        fast = fast.?.next.?.next; // 把 快指针.?.下一个.?.下一个; 写入 快指针
        if (slow != null and fast != null and slow.? == fast.?) { // 若 慢指针 不等于 null and 快指针 不等于 null and 慢指针.? 等于 快指针.?
            var p1 = head; // 把 头节点 存入 p1
            var p2 = slow; // 把 慢指针 存入 p2
            while (p1 != null and p2 != null and p1.? != p2.?) { // 循环，直到不满足「p1 不等于 null and p2 不等于 null and p1.? 不等于 p2.?」
                p1 = p1.?.next; // 把 p1.?.下一个; 写入 p1
                p2 = p2.?.next; // 把 p2.?.下一个; 写入 p2
            }
            return p1; // 返回 p1
        }
    }
    return null; // 返回 null
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator); // 把 std.堆.ArenaAllocator.init(std.堆.page_allocator) 存入 arena
    defer arena.deinit(); // defer arena.deinit();
    const alloc = arena.allocator(); // 把 arena.allocator() 存入 alloc
    const h = buildWithCycle(alloc, &[_]i32{ 3, 2, 0, -4 }, 2); // 把 buildWithCycle(alloc, 按位与 [_]i32{ 3, 2, 0, 减 4 }, 2) 存入 h
    const e = detectCycle(h); // 把 detectCycle(h) 存入 e
    if (e == null or e.?.val != 2) return error.TestFailed; // 若 e 等于 null or e.?.值 不等于 2，直接返回 error.TestFailed
    const s = try alloc.create(LNode); // 把 try alloc.create(LNode) 存入 字符串
    s.* = .{ .val = 1, .next = null }; // 把 { .值 赋值为 1, .下一个 赋值为 null }; 写入 s.*
    if (detectCycle(s) != null) return error.TestFailed; // 若 detectCycle(字符串) 不等于 null，直接返回 error.TestFailed
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
