// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107435426
// 字典序最大问题分析 — Zig 版（方案1）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn lexicographicallyLargest(arr: []i32, n: usize) void { // 定义函数/方法 lexicographicallyLargest
    for (0..arr.len) |i| { // 逐个取出 0..数组.长度 的元素（下标 i）
        for (i + 1..arr.len) |j| { // for (下标 i 加 1..数组.长度) 按位或 下标 j 按位或 {
            if (arr[i] < arr[j]) { // 若 数组[下标 i] 小于 数组[下标 j]
                const t = arr[i]; // 把 数组[下标 i] 存入 另一字符串
                arr[i] = arr[j]; // 把 数组[下标 j]; 写入 arr[i]
                arr[j] = t; // 把 另一字符串; 写入 arr[j]
            }
        }
    }
    _ = n; // 把 元素个数; 写入 _
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var v1 = [_]i32{ 1, 2, 3 }; // 把 [_]i32{ 1, 2, 3 } 存入 v1
    lexicographicallyLargest(&v1, 3); // lexicographicallyLargest( 按位与 v1, 3);
    if (v1[0] != 3 or v1[2] != 1) return error.TestFailed; // 若 v1[0] 不等于 3 or v1[2] 不等于 1，直接返回 error.TestFailed
    var v2 = [_]i32{ 4, 2, 9, 7 }; // 把 [_]i32{ 4, 2, 9, 7 } 存入 v2
    lexicographicallyLargest(&v2, 4); // lexicographicallyLargest( 按位与 v2, 4);
    if (v2[0] != 9 or v2[3] != 2) return error.TestFailed; // 若 v2[0] 不等于 9 or v2[3] 不等于 2，直接返回 error.TestFailed
    std.debug.print("PASS\n", .{});
} // 全部用例通过，输出 PASS
