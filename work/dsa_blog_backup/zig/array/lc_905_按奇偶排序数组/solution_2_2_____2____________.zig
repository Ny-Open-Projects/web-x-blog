// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134893847
// LeetCode 905. 按奇偶排序数组 — Zig 版（方案2）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn sortArrayByParity(nums: []i32) void { // 定义函数/方法 sortArrayByParity
    var pos: usize = 0; // 把 0; 写入 var pos: usize
    for (nums, 0..) |v, i| { // for (数组, 0..) 按位或 值, 下标 i 按位或 {
        if (@mod(v, 2) == 0) { // 若 @mod(值, 2) 等于 0
            const t = nums[pos]; // 把 数组[pos] 存入 另一字符串
            nums[pos] = nums[i]; // 把 数组[下标 i]; 写入 nums[pos]
            nums[i] = t; // 把 另一字符串; 写入 nums[i]
            pos += 1; // pos累加 1
        }
    }
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var v1 = [_]i32{ 3, 1, 2, 4 }; // 把 [_]i32{ 3, 1, 2, 4 } 存入 v1
    sortArrayByParity(&v1); // sortArrayByParity( 按位与 v1);
    if (@mod(v1[0], 2) != 0 or @mod(v1[1], 2) != 0 or @mod(v1[2], 2) != 1) return error.TestFailed;
    var v2 = [_]i32{ 1, 2, 3 }; // 把 [_]i32{ 1, 2, 3 } 存入 v2
    sortArrayByParity(&v2); // sortArrayByParity( 按位与 v2);
    if (v2[0] != 2 or v2[1] != 1 or v2[2] != 3) return error.TestFailed;
    std.debug.print("PASS\n", .{});
} // 全部用例通过，输出 PASS
