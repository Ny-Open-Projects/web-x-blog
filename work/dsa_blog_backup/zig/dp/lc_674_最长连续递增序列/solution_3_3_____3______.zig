// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130771608
// LeetCode 674. 最长连续递增序列 — Zig 版（方案3）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn findLengthOfLCIS(nums: []const i32) i32 { // 定义函数/方法 findLengthOfLCIS
    if (nums.len == 0) return 0; // 若 数组.长度 等于 0，直接返回 0
    var best: i32 = 1; // 把 1; 写入 var best: i32
    var cur: i32 = 1; // 把 1; 写入 var cur: i32
    for (1..nums.len) |i| { // 逐个取出 1..数组.长度 的元素（下标 i）
        if (nums[i] > nums[i - 1]) { // 若 数组[下标 i] 超过 数组[下标 i 减 1]
            cur += 1; // 当前值累加 1
            if (cur > best) best = cur; // 若 当前值 超过 当前最优) 当前最优 赋值为 当前值;
        } else cur = 1; // 否则
    }
    return best; // 返回 当前最优
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    if (findLengthOfLCIS(&[_]i32{ 1, 3, 5, 4, 7 }) != 3) return error.TestFailed;
    if (findLengthOfLCIS(&[_]i32{ 2, 2, 2, 2, 2 }) != 1) return error.TestFailed;
    std.debug.print("PASS\n", .{});
} // 全部用例通过，输出 PASS
