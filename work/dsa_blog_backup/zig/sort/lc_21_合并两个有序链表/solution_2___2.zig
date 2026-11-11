// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133594090
// LeetCode 21. 合并两个有序链表 — Zig 版（方案2）
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
fn listToVec(head: ?*LNode, out: *std.ArrayList(i32)) void { // 定义函数/方法 listToVec
    var cur = head; // 把 头节点 存入 当前值
    while (cur) |n| { // 循环，直到不满足「当前值) 按位或 元素个数 按位或」
        out.append(n.val) catch unreachable; // 把 元素个数.值 追加到列表尾部
        cur = n.next; // 把 元素个数.下一个; 写入 当前值
    }
}
fn mergeTwoLists(alloc: std.mem.Allocator, l1_in: ?*LNode, l2_in: ?*LNode) ?*LNode { // 定义函数/方法 mergeTwoLists
    const dummy = alloc.create(LNode) catch unreachable; // 把 alloc.create(LNode) catch unreachable 存入 哨兵节点
    dummy.* = .{ .val = 0, .next = null }; // 把 { .值 赋值为 0, .下一个 赋值为 null }; 写入 dummy.*
    var p = dummy; // 把 哨兵节点 存入 节点
    var l1 = l1_in; // 把 l1_in 存入 l1
    var l2 = l2_in; // 把 l2_in 存入 l2
    while (l1 != null and l2 != null) { // 循环，直到不满足「l1 不等于 null and l2 不等于 null」
        if (l1.?.val < l2.?.val) { // 若 l1.?.值 小于 l2.?.值
            p.next = l1; // 把 l1; 写入 下一个
            l1 = l1.?.next; // 把 l1.?.下一个; 写入 l1
        } else { // 否则
            p.next = l2; // 把 l2; 写入 下一个
            l2 = l2.?.next; // 把 l2.?.下一个; 写入 l2
        }
        p = p.next.?; // 把 节点.下一个.?; 写入 节点
    }
    p.next = if (l1) |x| x else l2; // 把 if (l1) 按位或 x 按位或 x else l2; 写入 下一个
    return dummy.next; // 返回 哨兵节点.下一个
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator); // 把 std.堆.ArenaAllocator.init(std.堆.page_allocator) 存入 arena
    defer arena.deinit(); // defer arena.deinit();
    const alloc = arena.allocator(); // 把 arena.allocator() 存入 alloc
    var out = std.ArrayList(i32).init(std.heap.page_allocator); // 把 std.ArrayList(i32).init(std.堆.page_allocator) 存入 out
    defer out.deinit(); // defer out.deinit();
    const got = mergeTwoLists(alloc, buildList(alloc, &[_]i32{ 1, 2, 4 }), buildList(alloc, &[_]i32{ 1, 3, 4 }));
    listToVec(got, &out); // listToVec(got, 按位与 out);
    const want = [_]i32{ 1, 1, 2, 3, 4, 4 }; // 把 [_]i32{ 1, 1, 2, 3, 4, 4 } 存入 want
    if (out.items.len != want.len) return error.TestFailed; // 若 out.items.长度 不等于 want.长度，直接返回 error.TestFailed
    for (want, 0..) |w, i| if (out.items[i] != w) return error.TestFailed;
    if (mergeTwoLists(alloc, null, null) != null) return error.TestFailed;
    out.clearRetainingCapacity(); // out.clearRetainingCapacity();
    listToVec(mergeTwoLists(alloc, null, buildList(alloc, &[_]i32{0})), &out);
    if (out.items.len != 1 or out.items[0] != 0) return error.TestFailed;
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
