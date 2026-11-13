// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145233077
// LeetCode 35. 搜索插入位置 — Zig 版（方案1：二分查找）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn searchInsert(nums: []const i32, target: i32) usize { // 定义函数/方法 searchInsert
    var left: usize = 0; // 把 0; 写入 var left: usize
    var right: usize = nums.len; // 把 数组.长度; 写入 var right: usize
    while (left < right) { // 循环，直到不满足「左边界 小于 右边界」
        const mid = left + (right - left) / 2; // 把 左边界 加 (右边界 减 左边界) 除以 2 存入 中点
        if (nums[mid] < target) left = mid + 1 else right = mid; // 若 数组[中点] 小于 目标值) 左边界 赋值为 中点 加 1 else 右边界 赋值为 中点;
    }
    return left; // 返回 左边界
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    const a1 = [_]i32{ 1, 2, 3 }; // 把 [_]i32{ 1, 2, 3 } 存入 a1
    const a2 = [_]i32{ 1, 3, 5, 6 }; // 把 [_]i32{ 1, 3, 5, 6 } 存入 a2
    const Case = struct { nums: []const i32, t: i32, want: usize };
    const cases = [_]Case{ // 把 [_]Case{ 存入 cases
        .{ .nums = &a1, .t = 1, .want = 0 },
        .{ .nums = &a2, .t = 5, .want = 2 },
        .{ .nums = &a2, .t = 2, .want = 1 },
        .{ .nums = &a2, .t = 7, .want = 4 },
        .{ .nums = &a2, .t = 0, .want = 0 },
    };
    for (cases, 0..) |c, i| { // for (cases, 0..) 按位或 字符, 下标 i 按位或 {
        if (searchInsert(c.nums, c.t) != c.want) { // 若 searchInsert(字符.数组, 字符.另一字符串) 不等于 字符.want
            std.debug.print("FAIL case {d}\n", .{i}); // 打印输出
            return error.TestFailed; // 返回 error.TestFailed
        }
    }
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
