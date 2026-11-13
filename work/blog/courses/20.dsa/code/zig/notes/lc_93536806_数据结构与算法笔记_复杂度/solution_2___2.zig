// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/93536806
// 数据结构与算法笔记: 复杂度 — Zig 版（方案2）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn funcCalls(n: i32) i64 { // 定义函数/方法 funcCalls
    if (n <= 1) return 1; // 若 元素个数 不超过 1，直接返回 1
    return 2 * funcCalls(n - 1); // 返回 2 乘 funcCalls(元素个数 减 1)
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    if (funcCalls(1) != 1 or funcCalls(2) != 2 or funcCalls(5) != 16 or funcCalls(10) != 512) return error.TestFailed;
    std.debug.print("PASS\n", .{});
} // 全部用例通过，输出 PASS
