// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133922762
// LeetCode 160. 相交链表 — Zig 版（方案1）
const std = @import("std"); // 把 @import(「std」) 存入 std
const LNode = struct { val: i32, next: ?*LNode }; // 把 struct { 值: i32, 下一个: ? 乘 LNode } 存入 LNode
fn getIntersectionNode(a: ?*LNode, b: ?*LNode) ?*LNode { // 定义函数/方法 getIntersectionNode
    if (a == null or b == null) return null; // 若 数组 等于 null or b 等于 null，直接返回 null
    var p1 = a; // 把 数组 存入 p1
    var p2 = b; // 把 b 存入 p2
    while (p1 != p2) { // 循环，直到不满足「p1 不等于 p2」
        p1 = if (p1) |x| x.next else b; // 把 if (p1) 按位或 x 按位或 x.下一个 else b; 写入 p1
        p2 = if (p2) |y| y.next else a; // 把 if (p2) 按位或 y 按位或 y.下一个 else 数组; 写入 p2
    }
    return p1; // 返回 p1
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator); // 把 std.堆.ArenaAllocator.init(std.堆.page_allocator) 存入 arena
    defer arena.deinit(); // defer arena.deinit();
    const alloc = arena.allocator(); // 把 arena.allocator() 存入 alloc
    const shared = try alloc.create(LNode); // 把 try alloc.create(LNode) 存入 shared
    shared.* = .{ .val = 8, .next = null }; // 把 { .值 赋值为 8, .下一个 赋值为 null }; 写入 shared.*
    const n4 = try alloc.create(LNode); // 把 try alloc.create(LNode) 存入 n4
    n4.* = .{ .val = 4, .next = null }; // 把 { .值 赋值为 4, .下一个 赋值为 null }; 写入 n4.*
    shared.next = n4; // 把 n4; 写入 下一个
    const n5 = try alloc.create(LNode); // 把 try alloc.create(LNode) 存入 n5
    n5.* = .{ .val = 5, .next = null }; // 把 { .值 赋值为 5, .下一个 赋值为 null }; 写入 n5.*
    n4.next = n5; // 把 n5; 写入 下一个
    const a1 = try alloc.create(LNode); // 把 try alloc.create(LNode) 存入 a1
    a1.* = .{ .val = 4, .next = null }; // 把 { .值 赋值为 4, .下一个 赋值为 null }; 写入 a1.*
    const a2 = try alloc.create(LNode); // 把 try alloc.create(LNode) 存入 a2
    a2.* = .{ .val = 1, .next = shared }; // 把 { .值 赋值为 1, .下一个 赋值为 shared }; 写入 a2.*
    a1.next = a2; // 把 a2; 写入 下一个
    const b1 = try alloc.create(LNode); // 把 try alloc.create(LNode) 存入 b1
    b1.* = .{ .val = 5, .next = null }; // 把 { .值 赋值为 5, .下一个 赋值为 null }; 写入 b1.*
    const b2 = try alloc.create(LNode); // 把 try alloc.create(LNode) 存入 b2
    b2.* = .{ .val = 6, .next = null }; // 把 { .值 赋值为 6, .下一个 赋值为 null }; 写入 b2.*
    b1.next = b2; // 把 b2; 写入 下一个
    const b3 = try alloc.create(LNode); // 把 try alloc.create(LNode) 存入 b3
    b3.* = .{ .val = 1, .next = shared }; // 把 { .值 赋值为 1, .下一个 赋值为 shared }; 写入 b3.*
    b2.next = b3; // 把 b3; 写入 下一个
    if (getIntersectionNode(a1, b1) != shared) return error.TestFailed;
    const x = try alloc.create(LNode); // 把 try alloc.create(LNode) 存入 x
    x.* = .{ .val = 1, .next = null }; // 把 { .值 赋值为 1, .下一个 赋值为 null }; 写入 x.*
    const y = try alloc.create(LNode); // 把 try alloc.create(LNode) 存入 y
    y.* = .{ .val = 1, .next = null }; // 把 { .值 赋值为 1, .下一个 赋值为 null }; 写入 y.*
    if (getIntersectionNode(x, y) != null) return error.TestFailed; // 若 getIntersectionNode(x, y) 不等于 null，直接返回 error.TestFailed
    if (getIntersectionNode(null, null) != null) return error.TestFailed;
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
