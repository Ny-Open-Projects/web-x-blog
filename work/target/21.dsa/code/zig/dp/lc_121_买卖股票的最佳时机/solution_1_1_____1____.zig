// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130515763
// LeetCode 121. 买卖股票的最佳时机 — Zig 版（方案1）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn maxProfit(prices: []const i32) i32 { // 定义函数/方法 maxProfit
    var min_p: i32 = std.math.maxInt(i32); // 把 std.math.maxInt(i32); 写入 var min_p: i32
    var best: i32 = 0; // 把 0; 写入 var best: i32
    for (prices) |p| { // 逐个取出 价格序列 的元素（节点）
        if (p < min_p) min_p = p; // 若 节点 小于 min_p) min_p 赋值为 节点;
        if (p - min_p > best) best = p - min_p; // 若 节点 减 min_p 超过 当前最优) 当前最优 赋值为 节点 减 min_p;
    }
    return best; // 返回 当前最优
}
pub fn main() !void {
    if (maxProfit(&[_]i32{ 7, 1, 5, 3, 6, 4 }) != 5) return error.TestFailed;
    if (maxProfit(&[_]i32{ 7, 6, 4, 3, 1 }) != 0) return error.TestFailed;
    std.debug.print("PASS\n", .{});
} // 程序入口：跑内嵌自测用例
