// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/136847926
// LeetCode 502. IPO — Zig 版（方案1）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn findMaximizedCapital(k: i32, w0: i64, profits: []const i64, capital: []const i64) i64 { // 定义函数/方法 findMaximizedCapital
    var w = w0; // 把 w0 存入 权重
    var used = [_]bool{false} ** 64; // 把 [_]bool{false} 乘 乘 64 存入 已用标记
    var t: i32 = 0; // 把 0; 写入 var t: i32
    while (t < k) : (t += 1) { // 循环，直到不满足「另一字符串 小于 下标 k) : (另一字符串 累加 1」
        var best: i64 = -1; // 把 减 1; 写入 var best: i64
        var best_j: i64 = -1; // 把 减 1; 写入 var best_j: i64
        for (profits, 0..) |p, j| { // for (profits, 0..) 按位或 节点, 下标 j 按位或 {
            if (!used[j] and capital[j] <= w and p > best) {
                best = p;
                best_j = @intCast(j);
            }
        }
        if (best_j < 0) break; // 若 best_j 小于 0) break;
        w += best; // 权重累加 当前最优
        used[@intCast(best_j)] = true; // 把 true; 写入 used[@intCast(best_j)]
    }
    return w; // 返回 权重
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    if (findMaximizedCapital(2, 0, &[_]i64{ 1, 2, 3 }, &[_]i64{ 0, 1, 1 }) != 4) return error.TestFailed;
    if (findMaximizedCapital(3, 0, &[_]i64{ 1, 2, 3 }, &[_]i64{ 0, 1, 2 }) != 6) return error.TestFailed;
    if (findMaximizedCapital(1, 0, &[_]i64{ 1, 2 }, &[_]i64{ 1, 2 }) != 0) return error.TestFailed;
    if (findMaximizedCapital(2, 1, &[_]i64{ 1, 2, 3 }, &[_]i64{ 1, 1, 2 }) != 6) return error.TestFailed;
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
