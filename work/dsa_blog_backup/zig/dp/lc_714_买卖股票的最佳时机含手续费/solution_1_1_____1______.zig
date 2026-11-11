// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130741193
// LeetCode 714. 买卖股票的最佳时机含手续费 — Zig 版（方案1）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn maxProfitFee(prices: []const i32, fee: i32) i32 { // 定义函数/方法 maxProfitFee
    var hold: i32 = -prices[0]; // 把 减 价格序列[0]; 写入 var hold: i32
    var sold: i32 = 0; // 把 0; 写入 var sold: i32
    for (prices[1..]) |p| { // for (价格序列[1..]) 按位或 节点 按位或 {
        const nh = @max(hold, sold - p); // 把 @取较大值 hold, sold 减 节点) 存入 nh
        const ns = @max(sold, hold + p - fee); // 把 @取较大值 sold, hold 加 节点 减 fee) 存入 ns
        hold = nh; // 把 nh; 写入 hold
        sold = ns; // 把 ns; 写入 sold
    }
    return sold; // 返回 sold
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    if (maxProfitFee(&[_]i32{ 1, 3, 2, 8, 4, 9 }, 2) != 8) return error.TestFailed;
    if (maxProfitFee(&[_]i32{1}, 1) != 0) return error.TestFailed;
    std.debug.print("PASS\n", .{});
} // 全部用例通过，输出 PASS
