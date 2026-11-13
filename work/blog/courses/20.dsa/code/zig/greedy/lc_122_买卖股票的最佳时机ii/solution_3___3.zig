// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133925028
// LeetCode 122. 买卖股票的最佳时机II — Zig 版（方案3）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn maxProfit(prices: []const i32) i32 { // 定义函数/方法 maxProfit
    var profit: i32 = 0; // 把 0; 写入 var profit: i32
    for (1..prices.len) |i| { // 逐个取出 1..价格序列.长度 的元素（下标 i）
        if (prices[i] > prices[i - 1]) profit += prices[i] - prices[i - 1];
    }
    return profit; // 返回 profit
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    if (maxProfit(&[_]i32{ 7, 1, 5, 3, 6, 4 }) != 7) return error.TestFailed;
    if (maxProfit(&[_]i32{ 1, 2, 3, 4, 5 }) != 4) return error.TestFailed;
    if (maxProfit(&[_]i32{ 7, 6, 4, 3, 1 }) != 0) return error.TestFailed;
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
