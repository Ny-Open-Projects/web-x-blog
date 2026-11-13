// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/99759428
// 数据结构与算法之数组操作 — Zig 版（方案1）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn twoSum(nums: []const i32, target: i32, out: *[2]i32) bool { // 定义函数/方法 twoSum
    for (0..nums.len) |i| { // 逐个取出 0..数组.长度 的元素（下标 i）
        for (i + 1..nums.len) |j| { // for (下标 i 加 1..数组.长度) 按位或 下标 j 按位或 {
            if (nums[i] + nums[j] == target) { // 若 数组[下标 i] 加 数组[下标 j] 等于 目标值
                out[0] = @intCast(i); // 把 @intCast(下标 i); 写入 out[0]
                out[1] = @intCast(j); // 把 @intCast(下标 j); 写入 out[1]
                return true; // 返回 true
            }
        }
    }
    return false; // 返回 false
}
fn maxSubArray(nums: []const i32) i32 { // 定义函数/方法 maxSubArray
    var best = nums[0]; // 把 数组[0] 存入 当前最优
    var cur = nums[0]; // 把 数组[0] 存入 当前值
    for (nums[1..]) |v| { // for (数组[1..]) 按位或 值 按位或 {
        cur = if (cur > 0) cur + v else v; // 把 if (当前值 超过 0) 当前值 加 值 else 值; 写入 当前值
        if (cur > best) best = cur; // 若 当前值 超过 当前最优) 当前最优 赋值为 当前值;
    }
    return best; // 返回 当前最优
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var out: [2]i32 = undefined; // 把 undefined; 写入 var out: [2]i32
    if (!twoSum(&[_]i32{ 2, 7, 11, 15 }, 9, &out)) return error.TestFailed;
    if (out[0] != 0 or out[1] != 1) return error.TestFailed; // 若 out[0] 不等于 0 or out[1] 不等于 1，直接返回 error.TestFailed
    if (maxSubArray(&[_]i32{ -2, 1, -3, 4, -1, 2, 1, -5, 4 }) != 6) return error.TestFailed;
    std.debug.print("PASS\n", .{});
} // 全部用例通过，输出 PASS
