// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130588647
// LeetCode 123. 买卖股票的最佳时机III — Zig 版（方案1）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn maxProfitIII(prices: []const i32) i32 { // 定义函数/方法 maxProfitIII
    var buy1: i64 = std.math.minInt(i64) / 2; // 把 std.math.minInt(i64) 除以 2; 写入 var buy1: i64
    var sell1: i64 = 0; // 把 0; 写入 var sell1: i64
    var buy2: i64 = std.math.minInt(i64) / 2; // 把 std.math.minInt(i64) 除以 2; 写入 var buy2: i64
    var sell2: i64 = 0; // 把 0; 写入 var sell2: i64
    for (prices) |p| { // 逐个取出 价格序列 的元素（节点）
        buy1 = @max(buy1, -p); // 把 @取较大值 buy1, 减 节点); 写入 buy1
        sell1 = @max(sell1, buy1 + p); // 把 @取较大值 sell1, buy1 加 节点); 写入 sell1
        buy2 = @max(buy2, sell1 - p); // 把 @取较大值 buy2, sell1 减 节点); 写入 buy2
        sell2 = @max(sell2, buy2 + p); // 把 @取较大值 sell2, buy2 加 节点); 写入 sell2
    }
    return @intCast(sell2); // 返回 @intCast(sell2)
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    if (maxProfitIII(&[_]i32{ 1, 2, 3 }) != 2) return error.TestFailed;
    if (maxProfitIII(&[_]i32{ 1, 2, 3, 4, 5 }) != 4) return error.TestFailed;
    if (maxProfitIII(&[_]i32{ 7, 6, 4, 3, 1 }) != 0) return error.TestFailed;
    if (maxProfitIII(&[_]i32{ 3, 3, 5, 0, 0, 3, 1, 4 }) != 6) return error.TestFailed;
    if (maxProfitIII(&[_]i32{1}) != 0) return error.TestFailed; // 若 maxProfitIII( 按位与 [_]i32{1}) 不等于 0，直接返回 error.TestFailed
    if (maxProfitIII(&[_]i32{ 1, 2 }) != 1) return error.TestFailed;
    std.debug.print("PASS\n", .{});
} // 全部用例通过，输出 PASS
