// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145582435
// LeetCode 3105. 最长的严格递增或递减子数组 — Zig 版（方案3）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn longestMonotonicSubarray(nums: []const i32) i32 { // 定义函数/方法 longestMonotonicSubarray
    if (nums.len == 0) return 0; // 若 数组.长度 等于 0，直接返回 0
    var inc: i32 = 1; // 把 1; 写入 var inc: i32
    var dec: i32 = 1; // 把 1; 写入 var dec: i32
    var best: i32 = 1; // 把 1; 写入 var best: i32
    for (1..nums.len) |i| { // 逐个取出 1..数组.长度 的元素（下标 i）
        if (nums[i] > nums[i - 1]) { // 若 数组[下标 i] 超过 数组[下标 i 减 1]
            inc += 1; // inc累加 1
            dec = 1; // 把 1; 写入 dec
        } else if (nums[i] < nums[i - 1]) { // 否则，若 数组[下标 i] 小于 数组[下标 i 减 1]
            dec += 1; // dec累加 1
            inc = 1; // 把 1; 写入 inc
        } else { // 否则
            inc = 1; // 把 1; 写入 inc
            dec = 1; // 把 1; 写入 dec
        }
        best = @max(best, @max(inc, dec)); // 把 @取较大值 当前最优, @取较大值 inc, dec)); 写入 当前最优
    }
    return best; // 返回 当前最优
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    if (longestMonotonicSubarray(&[_]i32{ 1, 2, 3, 4, 5 }) != 5) return error.TestFailed;
    if (longestMonotonicSubarray(&[_]i32{ 5, 4, 3, 2, 1 }) != 5) return error.TestFailed;
    if (longestMonotonicSubarray(&[_]i32{ 1, 4, 3, 2, 5 }) != 3) return error.TestFailed;
    std.debug.print("PASS\n", .{});
} // 全部用例通过，输出 PASS
