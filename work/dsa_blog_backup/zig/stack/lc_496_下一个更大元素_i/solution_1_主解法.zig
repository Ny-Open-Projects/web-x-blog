// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145012016
// LeetCode 496. 下一个更大元素 I — Zig 版（方案1）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn nextGreaterElement(n1: []const i32, n2: []const i32, alloc: std.mem.Allocator, out: []i32) void { // 定义函数/方法 nextGreaterElement
    var next = std.AutoHashMap(i32, i32).init(alloc); // 把 std.AutoHashMap(i32, i32).init(alloc) 存入 下一个
    var st: [8192]i32 = undefined; // 把 undefined; 写入 var st: [8192]i32
    var top: usize = 0; // 把 0; 写入 var top: usize
    for (n2) |v| { // 逐个取出 n2 的元素（值）
        while (top > 0 and st[top - 1] < v) { // 循环，直到不满足「top 超过 0 and st[top 减 1] 小于 值」
            next.put(st[top - 1], v) catch unreachable; // 下一个.put(st[top 减 1], 值) catch unreachable;
            top -= 1; // top累减 1
        }
        st[top] = v; // 把 值; 写入 st[top]
        top += 1; // top累加 1
    }
    for (n1, 0..) |v, i| { // for (n1, 0..) 按位或 值, 下标 i 按位或 {
        out[i] = next.get(v) orelse -1; // 把 下一个 查找 值) orelse 减 1; 写入 out[i]
    }
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator); // 把 std.堆.ArenaAllocator.init(std.堆.page_allocator) 存入 arena
    defer arena.deinit(); // defer arena.deinit();
    const alloc = arena.allocator(); // 把 arena.allocator() 存入 alloc
    var out: [8]i32 = undefined; // 把 undefined; 写入 var out: [8]i32
    nextGreaterElement(&[_]i32{ 4, 1, 2 }, &[_]i32{ 1, 3, 4, 2 }, alloc, &out);
    if (out[0] != -1 or out[1] != 3 or out[2] != -1) return error.TestFailed;
    nextGreaterElement(&[_]i32{ 2, 4 }, &[_]i32{ 1, 2, 3, 4 }, alloc, &out);
    if (out[0] != 3 or out[1] != -1) return error.TestFailed; // 若 out[0] 不等于 3 or out[1] 不等于 减 1，直接返回 error.TestFailed
    std.debug.print("PASS\n", .{});
} // 全部用例通过，输出 PASS
