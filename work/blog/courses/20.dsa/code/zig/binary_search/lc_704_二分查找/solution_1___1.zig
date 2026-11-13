// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134221939
// LeetCode 704. 二分查找 — Zig 版（方案1：经典二分查找，闭区间 [left, right]）

const std = @import("std"); // 把 @import(「std」) 存入 std

fn search(nums: []const i32, target: i32) i32 { // 定义函数/方法 search
    var left: i32 = 0; // 把 0; 写入 var left: i32
    var right: i32 = @as(i32, @intCast(nums.len)) - 1; // 把 @as(i32, @intCast(数组.长度)) 减 1; 写入 var right: i32
    while (left <= right) { // 循环，直到不满足「左边界 不超过 右边界」
        const mid = left + @divTrunc(right - left, 2); // 把 左边界 加 @divTrunc(右边界 减 左边界, 2) 存入 中点
        const idx: usize = @intCast(mid); // 把 @intCast(中点); 写入 const idx: usize
        if (nums[idx] == target) { // 若 数组[idx] 等于 目标值
            return mid; // 返回 中点
        } else if (nums[idx] < target) { // 否则，若 数组[idx] 小于 目标值
            left = mid + 1; // 把 中点 加 1; 写入 左边界
        } else { // 否则
            right = mid - 1; // 把 中点 减 1; 写入 右边界
        }
    }
    return -1; // 返回 减 1
}

pub fn main() !void { // 程序入口：跑内嵌自测用例
    const a1 = [_]i32{ 1, 2, 3 }; // 把 [_]i32{ 1, 2, 3 } 存入 a1
    const a2 = [_]i32{ -1, 0, 3, 5, 9, 12 }; // 把 [_]i32{ 减 1, 0, 3, 5, 9, 12 } 存入 a2
    if (search(&a1, 1) != 0) return error.TestFailed; // 若 search( 按位与 a1, 1) 不等于 0，直接返回 error.TestFailed
    if (search(&a2, 9) != 4) return error.TestFailed; // 若 search( 按位与 a2, 9) 不等于 4，直接返回 error.TestFailed
    if (search(&a2, 2) != -1) return error.TestFailed; // 若 search( 按位与 a2, 2) 不等于 减 1，直接返回 error.TestFailed
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
