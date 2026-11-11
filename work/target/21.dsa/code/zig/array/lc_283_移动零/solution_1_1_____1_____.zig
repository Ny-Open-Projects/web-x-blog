// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134055742
// LeetCode 283. 移动零 — Zig 版（方案1）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn moveZeroes(nums: []i32) void { // 定义函数/方法 moveZeroes
    var pos: usize = 0; // 把 0; 写入 var pos: usize
    for (nums, 0..) |v, i| { // for (数组, 0..) 按位或 值, 下标 i 按位或 {
        if (v != 0) { // 若 值 不等于 0
            const t = nums[pos]; // 把 数组[pos] 存入 另一字符串
            nums[pos] = nums[i]; // 把 数组[下标 i]; 写入 nums[pos]
            nums[i] = t; // 把 另一字符串; 写入 nums[i]
            pos += 1; // pos累加 1
        }
    }
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var v1 = [_]i32{ 0, 1, 0, 3, 12 }; // 把 [_]i32{ 0, 1, 0, 3, 12 } 存入 v1
    moveZeroes(&v1); // moveZeroes( 按位与 v1);
    if (v1[0] != 1 or v1[2] != 12 or v1[4] != 0) return error.TestFailed;
    var v2 = [_]i32{0}; // 把 [_]i32{0} 存入 v2
    moveZeroes(&v2); // moveZeroes( 按位与 v2);
    if (v2[0] != 0) return error.TestFailed; // 若 v2[0] 不等于 0，直接返回 error.TestFailed
    std.debug.print("PASS\n", .{});
} // 全部用例通过，输出 PASS
