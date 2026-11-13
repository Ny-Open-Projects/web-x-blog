// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145386116
// LeetCode 1518. 换水问题 — Zig 版（方案1）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn numWaterBottles(numBottles: i32, numExchange: i32) i32 { // 定义函数/方法 numWaterBottles
    var ans = numBottles; // 把 numBottles 存入 答案
    var empty = numBottles; // 把 numBottles 存入 empty
    while (empty >= numExchange) { // 循环，直到不满足「empty 不低于 numExchange」
        const newB = @divTrunc(empty, numExchange); // 把 @divTrunc(empty, numExchange) 存入 newB
        ans += newB; // 答案累加 newB
        empty = newB + @mod(empty, numExchange); // 把 newB 加 @mod(empty, numExchange); 写入 empty
    }
    return ans; // 返回 答案
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    if (numWaterBottles(9, 3) != 13) return error.TestFailed; // 若 numWaterBottles(9, 3) 不等于 13，直接返回 error.TestFailed
    if (numWaterBottles(15, 4) != 19) return error.TestFailed; // 若 numWaterBottles(15, 4) 不等于 19，直接返回 error.TestFailed
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
