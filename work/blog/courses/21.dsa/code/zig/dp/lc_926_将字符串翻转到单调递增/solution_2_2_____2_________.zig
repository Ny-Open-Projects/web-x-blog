// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130659442
// LeetCode 926. 将字符串翻转到单调递增 — Zig 版（方案2）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn minFlipsMonoIncr(s: []const u8) i32 { // 定义函数/方法 minFlipsMonoIncr
    var ones: i32 = 0; // 把 0; 写入 var ones: i32
    var flips: i32 = 0; // 把 0; 写入 var flips: i32
    for (s) |c| { // 逐个取出 字符串 的元素（字符）
        if (c == '1') { // 若 字符 等于 '1'
            ones += 1; // ones累加 1
        } else { // 否则
            flips += 1; // flips累加 1
            if (ones < flips) flips = ones; // 若 ones 小于 flips) flips 赋值为 ones;
        }
    }
    return flips; // 返回 flips
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    if (minFlipsMonoIncr("00110") != 1) return error.TestFailed; // 若 minFlipsMonoIncr(「00110」) 不等于 1，直接返回 error.TestFailed
    if (minFlipsMonoIncr("010110") != 2) return error.TestFailed; // 若 minFlipsMonoIncr(「010110」) 不等于 2，直接返回 error.TestFailed
    if (minFlipsMonoIncr("00011000") != 2) return error.TestFailed; // 若 minFlipsMonoIncr(「00011000」) 不等于 2，直接返回 error.TestFailed
    std.debug.print("PASS\n", .{});
} // 全部用例通过，输出 PASS
