// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130521152
// LeetCode 746. 使用最小花费爬楼梯 — Zig 版（方案1）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn minCostClimbingStairs(cost: []const i32) i32 { // 定义函数/方法 minCostClimbingStairs
    var a: i32 = 0; // 把 0; 写入 var a: i32
    var b: i32 = 0; // 把 0; 写入 var b: i32
    for (2..cost.len + 1) |i| { // for (2..cost.长度 加 1) 按位或 下标 i 按位或 {
        const x = a + cost[i - 2]; // 把 数组 加 cost[下标 i 减 2] 存入 x
        const y = b + cost[i - 1]; // 把 b 加 cost[下标 i 减 1] 存入 y
        const t = if (x < y) x else y; // 把 if (x 小于 y) x else y 存入 另一字符串
        a = b; // 把 b; 写入 数组
        b = t; // 把 另一字符串; 写入 b
    }
    return b; // 返回 b
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    if (minCostClimbingStairs(&[_]i32{ 10, 15, 20 }) != 15) return error.TestFailed;
    if (minCostClimbingStairs(&[_]i32{ 1, 100, 1, 1, 1, 100, 1, 1, 100, 1 }) != 6) return error.TestFailed;
    std.debug.print("PASS\n", .{});
} // 全部用例通过，输出 PASS
