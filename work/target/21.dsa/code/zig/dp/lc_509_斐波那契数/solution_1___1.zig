// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130510175
// LeetCode 509. 斐波那契数 — Zig 版（方案1）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn fib(n: i32) i32 {
    if (n < 2) return n;
    var a: i32 = 0;
    var b: i32 = 1;
    var i: i32 = 2;
    while (i <= n) : (i += 1) {
        const t = a + b;
        a = b;
        b = t;
    }
    return b;
} // 定义函数/方法 fib
pub fn main() !void {
    if (fib(2) != 1 or fib(3) != 2 or fib(4) != 3 or fib(10) != 55) return error.TestFailed;
    std.debug.print("PASS\n", .{});
} // 程序入口：跑内嵌自测用例
