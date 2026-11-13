// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133911745
// LeetCode 45. 跳跃游戏II — Zig 版（方案2）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn jump(nums: []const i32) i32 { // 定义函数/方法 jump
    var position: usize = nums.len - 1; // 把 数组.长度 减 1; 写入 var position: usize
    var steps: i32 = 0; // 把 0; 写入 var steps: i32
    while (position > 0) { // 循环，直到不满足「position 超过 0」
        for (0..position) |i| { // 让 下标 i 从 0 走到 position 减一
            if (i + @as(usize, @intCast(nums[i])) >= position) { // 若 下标 i 加 @as(usize, @intCast(数组[下标 i])) 不低于 position
                position = i; // 把 下标 i; 写入 position
                steps += 1; // steps累加 1
                break; // 跳出循环
            }
        }
    }
    return steps; // 返回 steps
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    if (jump(&[_]i32{ 2, 3, 1, 1, 4 }) != 2) return error.TestFailed;
    if (jump(&[_]i32{ 2, 3, 0, 1, 4 }) != 2) return error.TestFailed;
    if (jump(&[_]i32{1}) != 0) return error.TestFailed; // 若 jump( 按位与 [_]i32{1}) 不等于 0，直接返回 error.TestFailed
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
