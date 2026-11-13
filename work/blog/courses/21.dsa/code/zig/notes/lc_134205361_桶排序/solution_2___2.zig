// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134205361
// 数据结构与算法之排序: 桶排序 — Zig 版（方案2）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn getIndex(arr: []const i32, k: i32) i32 { // 定义函数/方法 getIndex
    for (arr) |v| if (v == k) return k; // 逐个取出 数组 的元素（值）
    return -1; // 返回 减 1
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    const a = [_]i32{ 1, 2, 3 }; // 把 [_]i32{ 1, 2, 3 } 存入 数组
    if (getIndex(&a, 1) != 1) return error.TestFailed; // 若 getIndex( 按位与 数组, 1) 不等于 1，直接返回 error.TestFailed
    if (getIndex(&a, 3) != 3) return error.TestFailed; // 若 getIndex( 按位与 数组, 3) 不等于 3，直接返回 error.TestFailed
    if (getIndex(&a, 5) != -1) return error.TestFailed; // 若 getIndex( 按位与 数组, 5) 不等于 减 1，直接返回 error.TestFailed
    std.debug.print("PASS\n", .{});
} // 全部用例通过，输出 PASS
