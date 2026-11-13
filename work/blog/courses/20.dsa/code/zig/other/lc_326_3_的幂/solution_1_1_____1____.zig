// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135359346
// LeetCode 326. 3的幂 — Zig 版（方案1）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn isPowerOfThree(n0: i64) bool { // 定义判定函数 isPowerOfThree
    var n = n0; // 把 n0 存入 元素个数
    while (n != 0 and @mod(n, 3) == 0) n = @divTrunc(n, 3);
    return n == 1; // 返回 元素个数 等于 1
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    if (!isPowerOfThree(27)) return error.TestFailed; // 若 取反 isPowerOfThree(27)，直接返回 error.TestFailed
    if (isPowerOfThree(0)) return error.TestFailed; // 若 isPowerOfThree(0)，直接返回 error.TestFailed
    if (!isPowerOfThree(9)) return error.TestFailed; // 若 取反 isPowerOfThree(9)，直接返回 error.TestFailed
    if (isPowerOfThree(-1)) return error.TestFailed; // 若 isPowerOfThree( 减 1)，直接返回 error.TestFailed
    if (!isPowerOfThree(1)) return error.TestFailed; // 若 取反 isPowerOfThree(1)，直接返回 error.TestFailed
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
