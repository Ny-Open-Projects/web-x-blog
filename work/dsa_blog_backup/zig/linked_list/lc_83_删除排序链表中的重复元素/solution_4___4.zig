// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133874590
// LeetCode 83. 删除排序链表中的重复元素 — Zig 版（方案4）
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
fn deleteDuplicates(head: ?*LNode) ?*LNode { // 定义函数/方法 deleteDuplicates
    var cur = head; // 把 头节点 存入 当前值
    while (cur) |node| { // 循环，直到不满足「当前值) 按位或 节点 按位或」
        if (node.next) |nxt| { // 若 节点.下一个) 按位或 nxt 按位或
            if (nxt.val == node.val) { // 若 nxt.值 等于 节点.值
                node.next = nxt.next; // 把 nxt.下一个; 写入 下一个
                continue; // 跳过本轮，进入下一次
            }
        }
        cur = node.next; // 把 节点.下一个; 写入 当前值
    }
    return head; // 返回 头节点
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator); // 把 std.堆.ArenaAllocator.init(std.堆.page_allocator) 存入 arena
    defer arena.deinit(); // defer arena.deinit();
    const alloc = arena.allocator(); // 把 arena.allocator() 存入 alloc
    var out = std.ArrayList(i32).init(std.heap.page_allocator); // 把 std.ArrayList(i32).init(std.堆.page_allocator) 存入 out
    defer out.deinit(); // defer out.deinit();
    toVec(deleteDuplicates(buildList(alloc, &[_]i32{ 1, 1, 2 })), &out);
    if (out.items.len != 2 or out.items[0] != 1 or out.items[1] != 2) return error.TestFailed;
    out.clearRetainingCapacity(); // out.clearRetainingCapacity();
    toVec(deleteDuplicates(buildList(alloc, &[_]i32{ 1, 1, 2, 3, 3 })), &out);
    if (out.items.len != 3 or out.items[2] != 3) return error.TestFailed;
    out.clearRetainingCapacity(); // out.clearRetainingCapacity();
    toVec(deleteDuplicates(buildList(alloc, &[_]i32{ 1, 1, 1 })), &out);
    if (out.items.len != 1) return error.TestFailed; // 若 out.items.长度 不等于 1，直接返回 error.TestFailed
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
