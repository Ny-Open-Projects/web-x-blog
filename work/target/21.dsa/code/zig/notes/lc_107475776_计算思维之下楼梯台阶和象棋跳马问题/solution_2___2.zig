// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107475776
// 计算思维之下楼梯台阶和象棋跳马问题 — Zig 版（方案2）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn climbStairsVariants(n: i32) i64 { // 定义函数/方法 climbStairsVariants
    if (n <= 1) return 1; // 若 元素个数 不超过 1，直接返回 1
    var a: i64 = 1; // 把 1; 写入 var a: i64
    var b: i64 = 1; // 把 1; 写入 var b: i64
    var i: i32 = 2; // 把 2; 写入 var i: i32
    while (i <= n) : (i += 1) { // 循环，直到不满足「下标 i 不超过 元素个数) : (下标 i 累加 1」
        const t = a + b; // 把 数组 加 b 存入 另一字符串
        a = b; // 把 b; 写入 数组
        b = t; // 把 另一字符串; 写入 b
    }
    return b; // 返回 b
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    if (climbStairsVariants(10) != 89 or climbStairsVariants(1) != 1 or climbStairsVariants(2) != 2) return error.TestFailed;
    std.debug.print("PASS\n", .{});
} // 全部用例通过，输出 PASS
