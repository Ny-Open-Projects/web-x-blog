// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133844403
// LeetCode 55. 跳跃游戏 — Zig 版（方案1）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn canJump(nums: []const i32) bool { // 定义函数/方法 canJump
    var max_reach: usize = 0; // 把 0; 写入 var max_reach: usize
    for (nums, 0..) |v, i| { // for (数组, 0..) 按位或 值, 下标 i 按位或 {
        if (i > max_reach) return false; // 若 下标 i 超过 max_reach，直接返回 false
        const r = i + @as(usize, @intCast(v)); // 把 下标 i 加 @as(usize, @intCast(值)) 存入 右指针
        if (r > max_reach) max_reach = r; // 若 右指针 超过 max_reach) max_reach 赋值为 右指针;
    }
    return true; // 返回 true
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    if (!canJump(&[_]i32{ 2, 3, 1, 1, 4 })) return error.TestFailed;
    if (canJump(&[_]i32{ 3, 2, 1, 0, 4 })) return error.TestFailed;
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
