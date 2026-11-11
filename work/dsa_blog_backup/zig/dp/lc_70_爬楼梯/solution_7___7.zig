// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130506068
// LeetCode 70. 爬楼梯 — Zig 版（方案7）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn climbStairs(n: i32) i32 {
    if (n <= 2) return n;
    var a: i32 = 1;
    var b: i32 = 2;
    var i: i32 = 3;
    while (i <= n) : (i += 1) {
        const t = a + b;
        a = b;
        b = t;
    }
    return b;
} // 定义函数/方法 climbStairs
pub fn main() !void {
    if (climbStairs(2) != 2 or climbStairs(3) != 3 or climbStairs(10) != 89) return error.TestFailed;
    std.debug.print("PASS\n", .{});
} // 程序入口：跑内嵌自测用例
