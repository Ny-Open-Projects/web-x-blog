// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130687299
// LeetCode 1027. 最长等差数列 — Zig 版（方案2）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn longestArithSeqLength(nums: []const i32) i32 { // 定义函数/方法 longestArithSeqLength
    const n = nums.len; // 把 数组.长度 存入 元素个数
    if (n <= 2) return @intCast(n); // 若 元素个数 不超过 2，直接返回 @intCast(元素个数)
    var best: i32 = 2; // 把 2; 写入 var best: i32
    for (0..n) |i| { // 让 下标 i 从 0 走到 元素个数 减一
        for (i + 1..n) |j| { // for (下标 i 加 1..元素个数) 按位或 下标 j 按位或 {
            const d = nums[j] - nums[i]; // 把 数组[下标 j] 减 数组[下标 i] 存入 d
            var cur: i32 = 2; // 把 2; 写入 var cur: i32
            var last = nums[j]; // 把 数组[下标 j] 存入 last
            for (j + 1..n) |k| { // for (下标 j 加 1..元素个数) 按位或 下标 k 按位或 {
                if (nums[k] - last == d) { // 若 数组[下标 k] 减 last 等于 d
                    cur += 1; // 当前值累加 1
                    last = nums[k]; // 把 数组[下标 k]; 写入 last
                }
            }
            if (cur > best) best = cur; // 若 当前值 超过 当前最优) 当前最优 赋值为 当前值;
        }
    }
    return best; // 返回 当前最优
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    if (longestArithSeqLength(&[_]i32{ 9, 4, 7, 2, 10 }) != 3) return error.TestFailed;
    if (longestArithSeqLength(&[_]i32{ 3, 6, 9, 12 }) != 4) return error.TestFailed;
    std.debug.print("PASS\n", .{});
} // 全部用例通过，输出 PASS
