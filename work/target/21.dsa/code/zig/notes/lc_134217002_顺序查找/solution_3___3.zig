// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134217002
// 数据结构与算法之查找: 顺序查找 — Zig 版（方案3）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn seqSearch(arr: []const i32, key: i32) i32 { // 定义函数/方法 seqSearch
    for (arr, 0..) |v, i| { // for (数组, 0..) 按位或 值, 下标 i 按位或 {
        if (v == key) return @intCast(i); // 若 值 等于 key，直接返回 @intCast(下标 i)
    }
    return -1; // 返回 减 1
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    const a = [_]i32{ 1, 2, 3 }; // 把 [_]i32{ 1, 2, 3 } 存入 数组
    if (seqSearch(&a, 1) != 0) return error.TestFailed; // 若 seqSearch( 按位与 数组, 1) 不等于 0，直接返回 error.TestFailed
    if (seqSearch(&a, 2) != 1) return error.TestFailed; // 若 seqSearch( 按位与 数组, 2) 不等于 1，直接返回 error.TestFailed
    if (seqSearch(&a, 4) != -1) return error.TestFailed; // 若 seqSearch( 按位与 数组, 4) 不等于 减 1，直接返回 error.TestFailed
    std.debug.print("PASS\n", .{});
} // 全部用例通过，输出 PASS
