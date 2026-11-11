// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135424151
// LeetCode 292. Nim游戏 — Zig 版（方案1）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn canWinNim(n: i64) bool {
    return @mod(n, 4) != 0;
} // 定义函数/方法 canWinNim
pub fn main() !void { // 程序入口：跑内嵌自测用例
    if (canWinNim(4)) return error.TestFailed; // 若 canWinNim(4)，直接返回 error.TestFailed
    if (!canWinNim(1) or !canWinNim(2)) return error.TestFailed; // 若 取反 canWinNim(1) or 取反 canWinNim(2)，直接返回 error.TestFailed
    if (canWinNim(8)) return error.TestFailed; // 若 canWinNim(8)，直接返回 error.TestFailed
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
