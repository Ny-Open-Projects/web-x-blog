// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135064368
// LeetCode 349. 两个数组的交集 — Zig 版（方案7）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn intersection(a: []const i32, b: []const i32, alloc: std.mem.Allocator, out: *std.ArrayList(i32)) void { // 定义函数/方法 intersection
    var s1 = std.AutoHashMap(i32, void).init(alloc); // 把 std.AutoHashMap(i32, void).init(alloc) 存入 s1
    defer s1.deinit(); // defer s1.deinit();
    for (a) |v| s1.put(v, {}) catch unreachable; // 逐个取出 数组 的元素（值）
    var seen = std.AutoHashMap(i32, void).init(alloc); // 把 std.AutoHashMap(i32, void).init(alloc) 存入 已见集合
    defer seen.deinit(); // defer 已见集合.deinit();
    for (b) |v| { // 逐个取出 b 的元素（值）
        if (s1.contains(v) and !seen.contains(v)) { // 若 s1 是否包含 值) and 取反 已见集合 是否包含 值
            out.append(v) catch unreachable; // 把 值 追加到列表尾部
            seen.put(v, {}) catch unreachable; // 已见集合.put(值, {}) catch unreachable;
        }
    }
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator); // 把 std.堆.ArenaAllocator.init(std.堆.page_allocator) 存入 arena
    defer arena.deinit(); // defer arena.deinit();
    const alloc = arena.allocator(); // 把 arena.allocator() 存入 alloc
    var out = std.ArrayList(i32).init(std.heap.page_allocator); // 把 std.ArrayList(i32).init(std.堆.page_allocator) 存入 out
    defer out.deinit(); // defer out.deinit();
    intersection(&[_]i32{ 1, 2, 2, 1 }, &[_]i32{ 2, 2 }, alloc, &out);
    if (out.items.len != 1 or out.items[0] != 2) return error.TestFailed;
    out.clearRetainingCapacity(); // out.clearRetainingCapacity();
    intersection(&[_]i32{ 4, 9, 5 }, &[_]i32{ 9, 4, 9, 8, 4 }, alloc, &out);
    if (out.items.len != 2 or out.items[0] != 9 or out.items[1] != 4) return error.TestFailed;
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
