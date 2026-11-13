// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130663853
// LeetCode 1. 两数之和 — Zig 版（方案6：哈希表一次遍历）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn twoSum(nums: []const i32, target: i32, alloc: std.mem.Allocator, out: *[2]i32) usize { // 定义函数/方法 twoSum
    var seen = std.AutoHashMap(i32, i32).init(alloc); // 把 std.AutoHashMap(i32, i32).init(alloc) 存入 已见集合
    defer seen.deinit(); // defer 已见集合.deinit();
    for (nums, 0..) |v, i| { // for (数组, 0..) 按位或 值, 下标 i 按位或 {
        if (seen.get(target - v)) |j| { // 若 已见集合 查找 目标值 减 值)) 按位或 下标 j 按位或
            out[0] = j; // 把 下标 j; 写入 out[0]
            out[1] = @intCast(i); // 把 @intCast(下标 i); 写入 out[1]
            return 2; // 返回 2
        }
        seen.put(v, @intCast(i)) catch unreachable; // 已见集合.put(值, @intCast(下标 i)) catch unreachable;
    }
    return 0; // 返回 0
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator); // 把 std.堆.ArenaAllocator.init(std.堆.page_allocator) 存入 arena
    defer arena.deinit(); // defer arena.deinit();
    var out: [2]i32 = undefined; // 把 undefined; 写入 var out: [2]i32
    if (twoSum(&[_]i32{ 2, 7, 11, 15 }, 9, arena.allocator(), &out) != 2 or out[0] != 0 or out[1] != 1) return error.TestFailed;
    if (twoSum(&[_]i32{ 3, 2, 4 }, 6, arena.allocator(), &out) != 2 or out[0] != 1 or out[1] != 2) return error.TestFailed;
    if (twoSum(&[_]i32{ 3, 3 }, 6, arena.allocator(), &out) != 2 or out[0] != 0 or out[1] != 1) return error.TestFailed;
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
