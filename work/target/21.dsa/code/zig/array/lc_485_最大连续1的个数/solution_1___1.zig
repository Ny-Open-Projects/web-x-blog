// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134424807
// LeetCode 485. 最大连续1的个数 — Zig 版（方案1）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn findMaxConsecutiveOnes(nums: []const i32) i32 { // 定义函数/方法 findMaxConsecutiveOnes
    var best: i32 = 0; // 把 0; 写入 var best: i32
    var cur: i32 = 0; // 把 0; 写入 var cur: i32
    for (nums) |v| { // 逐个取出 数组 的元素（值）
        if (v == 1) { // 若 值 等于 1
            cur += 1; // 当前值累加 1
            if (cur > best) best = cur; // 若 当前值 超过 当前最优) 当前最优 赋值为 当前值;
        } else cur = 0; // 否则
    }
    return best; // 返回 当前最优
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    if (findMaxConsecutiveOnes(&[_]i32{ 1, 1, 0, 1, 1, 1 }) != 3) return error.TestFailed;
    if (findMaxConsecutiveOnes(&[_]i32{ 1, 0, 1, 1, 0, 1 }) != 2) return error.TestFailed;
    std.debug.print("PASS\n", .{});
} // 全部用例通过，输出 PASS
