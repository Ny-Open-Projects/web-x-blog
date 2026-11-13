// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134066015
// LeetCode 41. 缺失的第一个正数 — Zig 版（方案9）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn firstMissingPositive(nums: []const i32, alloc: std.mem.Allocator) i32 { // 定义函数/方法 firstMissingPositive
    if (nums.len == 0) return 1; // 若 数组.长度 等于 0，直接返回 1
    var pos = std.ArrayList(i32).init(alloc); // 把 std.ArrayList(i32).init(alloc) 存入 pos
    for (nums) |v| if (v > 0) pos.append(v) catch unreachable; // 逐个取出 数组 的元素（值）
    if (pos.items.len == 0) return 1; // 若 pos.items.长度 等于 0，直接返回 1
    std.sort.pdq(i32, pos.items, {}, std.sort.asc(i32)); // std.sort.pdq(i32, pos.items, {}, std.sort.asc(i32));
    if (pos.items[0] != 1) return 1; // 若 pos.items[0] 不等于 1，直接返回 1
    const n = pos.items.len; // 把 pos.items.长度 存入 元素个数
    for (0..n - 1) |i| { // for (0..元素个数 减 1) 按位或 下标 i 按位或 {
        if (pos.items[i + 1] - pos.items[i] > 1) return pos.items[i] + 1;
    }
    return pos.items[n - 1] + 1; // 返回 pos.items[元素个数 减 1] 加 1
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator); // 把 std.堆.ArenaAllocator.init(std.堆.page_allocator) 存入 arena
    defer arena.deinit(); // defer arena.deinit();
    const alloc = arena.allocator(); // 把 arena.allocator() 存入 alloc
    if (firstMissingPositive(&[_]i32{ 1, 2, 0 }, alloc) != 3) return error.TestFailed;
    if (firstMissingPositive(&[_]i32{ 3, 4, -1, 1 }, alloc) != 2) return error.TestFailed;
    if (firstMissingPositive(&[_]i32{ 7, 8, 9, 11, 12 }, alloc) != 1) return error.TestFailed;
    if (firstMissingPositive(&[_]i32{}, alloc) != 1) return error.TestFailed;
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
