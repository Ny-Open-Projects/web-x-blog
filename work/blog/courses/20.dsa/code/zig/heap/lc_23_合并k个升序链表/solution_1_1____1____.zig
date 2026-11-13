// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134283831
// LeetCode 23. 合并K个升序链表 — Zig 版（方案1）
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
fn mergeKLists(alloc: std.mem.Allocator, lists: []const ?*LNode) ?*LNode { // 定义函数/方法 mergeKLists
    var ptrs = alloc.dupe(?*LNode, lists) catch unreachable; // 把 alloc.dupe(? 乘 LNode, lists) catch unreachable 存入 ptrs
    const dummy = alloc.create(LNode) catch unreachable; // 把 alloc.create(LNode) catch unreachable 存入 哨兵节点
    dummy.* = .{ .val = 0, .next = null }; // 把 { .值 赋值为 0, .下一个 赋值为 null }; 写入 dummy.*
    var tail = dummy; // 把 哨兵节点 存入 尾节点
    while (true) { // 循环，直到不满足「true」
        var best_i: ?usize = null; // 把 null; 写入 var best_i: ?usize
        for (ptrs, 0..) |p, i| { // for (ptrs, 0..) 按位或 节点, 下标 i 按位或 {
            if (p) |node| { // 若 节点) 按位或 节点 按位或
                if (best_i == null or node.val < ptrs[best_i.?].?.val) best_i = i;
            }
        }
        const bi = best_i orelse break; // 把 best_i orelse break 存入 bi
        tail.next = ptrs[bi]; // 把 ptrs[bi]; 写入 下一个
        ptrs[bi] = ptrs[bi].?.next; // 把 ptrs[bi].?.下一个; 写入 ptrs[bi]
        tail = tail.next.?; // 把 尾节点.下一个.?; 写入 尾节点
    }
    return dummy.next; // 返回 哨兵节点.下一个
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator); // 把 std.堆.ArenaAllocator.init(std.堆.page_allocator) 存入 arena
    defer arena.deinit(); // defer arena.deinit();
    const alloc = arena.allocator(); // 把 arena.allocator() 存入 alloc
    const lists = [_]?*LNode{ // 把 [_]? 乘 LNode{ 存入 lists
        buildList(alloc, &[_]i32{ 1, 4, 5 }),
        buildList(alloc, &[_]i32{ 1, 3, 4 }),
        buildList(alloc, &[_]i32{ 2, 6 }),
    };
    var out = std.ArrayList(i32).init(std.heap.page_allocator); // 把 std.ArrayList(i32).init(std.堆.page_allocator) 存入 out
    defer out.deinit(); // defer out.deinit();
    listToVec(mergeKLists(alloc, &lists), &out); // listToVec(mergeKLists(alloc, 按位与 lists), 按位与 out);
    const want = [_]i32{ 1, 1, 2, 3, 4, 4, 5, 6 }; // 把 [_]i32{ 1, 1, 2, 3, 4, 4, 5, 6 } 存入 want
    if (out.items.len != want.len) return error.TestFailed; // 若 out.items.长度 不等于 want.长度，直接返回 error.TestFailed
    for (want, 0..) |w, i| if (out.items[i] != w) return error.TestFailed;
    out.clearRetainingCapacity(); // out.clearRetainingCapacity();
    listToVec(mergeKLists(alloc, &[_]?*LNode{}), &out); // listToVec(mergeKLists(alloc, 按位与 [_]? 乘 LNode{}), 按位与 out);
    if (out.items.len != 0) return error.TestFailed; // 若 out.items.长度 不等于 0，直接返回 error.TestFailed
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
