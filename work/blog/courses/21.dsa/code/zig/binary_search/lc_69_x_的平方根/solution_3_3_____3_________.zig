// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145299731
// LeetCode 69. x 的平方根 — Zig 版（3 ) 方案3：牛顿迭代）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn mySqrt(x: i64) i64 { // 定义函数/方法 mySqrt
    if (x < 2) return x; // 若 x 小于 2，直接返回 x
    var r: i64 = x; // 把 x; 写入 var r: i64
    while (r * r > x) { // 循环，直到不满足「右指针 乘 右指针 超过 x」
        r = @divTrunc(r + @divTrunc(x, r), 2); // 把 @divTrunc(右指针 加 @divTrunc(x, 右指针), 2); 写入 右指针
    }
    return r; // 返回 右指针
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
