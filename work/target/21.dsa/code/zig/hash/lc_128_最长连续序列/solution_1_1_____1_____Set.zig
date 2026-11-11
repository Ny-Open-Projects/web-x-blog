// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135167108
// LeetCode 128. 最长连续序列 — Zig 版（方案1）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn longestConsecutive(nums: []const i32, alloc: std.mem.Allocator) i32 { // 定义函数/方法 longestConsecutive
    if (nums.len == 0) return 0; // 若 数组.长度 等于 0，直接返回 0
    var set = std.AutoHashMap(i32, void).init(alloc); // 把 std.AutoHashMap(i32, void).init(alloc) 存入 set
    defer set.deinit(); // defer set.deinit();
    for (nums) |v| set.put(v, {}) catch unreachable; // 逐个取出 数组 的元素（值）
    var best: i32 = 0; // 把 0; 写入 var best: i32
    var it = set.keyIterator(); // 把 set.keyIterator() 存入 it
    while (it.next()) |kp| { // 循环，直到不满足「it.下一个()) 按位或 kp 按位或」
        const num = kp.*; // 把 kp. 乘 存入 num
        if (set.contains(num - 1)) continue; // 若 set 是否包含 num 减 1)) continue;
        var cur = num; // 把 num 存入 当前值
        var streak: i32 = 1; // 把 1; 写入 var streak: i32
        while (set.contains(cur + 1)) {
            cur += 1;
            streak += 1;
        } // 循环，直到不满足「set 是否包含 当前值 加 1)) { 当前值 累加 1; streak 累加 1; }」
        if (streak > best) best = streak; // 若 streak 超过 当前最优) 当前最优 赋值为 streak;
    }
    return best; // 返回 当前最优
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator); // 把 std.堆.ArenaAllocator.init(std.堆.page_allocator) 存入 arena
    defer arena.deinit(); // defer arena.deinit();
    const alloc = arena.allocator(); // 把 arena.allocator() 存入 alloc
    if (longestConsecutive(&[_]i32{ 100, 4, 200, 1, 3, 2 }, alloc) != 4) return error.TestFailed;
    if (longestConsecutive(&[_]i32{ 0, 3, 7, 2, 5, 8, 4, 6, 0, 1 }, alloc) != 9) return error.TestFailed;
    if (longestConsecutive(&[_]i32{}, alloc) != 0) return error.TestFailed;
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
