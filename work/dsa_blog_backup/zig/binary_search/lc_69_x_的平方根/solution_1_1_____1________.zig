// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145299731
// LeetCode 69. x 的平方根 — Zig 版（1 ) 方案1：二分（精确区间判断））
const std = @import("std"); // 把 @import(「std」) 存入 std
fn mySqrt(x: i64) i64 { // 定义函数/方法 mySqrt
    if (x < 2) return x; // 若 x 小于 2，直接返回 x
    var lo: i64 = 1; // 把 1; 写入 var lo: i64
    var hi: i64 = @divTrunc(x, 2); // 把 @divTrunc(x, 2); 写入 var hi: i64
    while (lo <= hi) { // 循环，直到不满足「左边界 不超过 右边界」
        const m = lo + @divTrunc(hi - lo, 2); // 把 左边界 加 @divTrunc(右边界 减 左边界, 2) 存入 映射表
        if (m * m <= x and x < (m + 1) * (m + 1)) return m; // 若 映射表 乘 映射表 不超过 x and x 小于 (映射表 加 1) 乘 (映射表 加 1)，直接返回 映射表
        if (m * m > x) {
            hi = m - 1;
        } else {
            lo = m + 1;
        }
    }
    return lo; // 返回 左边界
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    const cases = [_][2]i64{ .{ 4, 2 }, .{ 8, 2 }, .{ 16, 4 }, .{ 2147395599, 46339 } };
    for (cases, 0..) |c, i| { // for (cases, 0..) 按位或 字符, 下标 i 按位或 {
        if (mySqrt(c[0]) != c[1]) { // 若 mySqrt(字符[0]) 不等于 字符[1]
            std.debug.print("FAIL case {d}\\n", .{i}); // 打印输出
            return error.TestFailed; // 返回 error.TestFailed
        }
    }
    std.debug.print("PASS\\n", .{}); // 全部用例通过，输出 PASS
}
