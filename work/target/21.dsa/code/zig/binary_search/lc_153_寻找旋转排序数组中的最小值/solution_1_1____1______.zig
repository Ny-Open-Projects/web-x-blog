// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145233483
// LeetCode 153. 寻找旋转排序数组中的最小值 — Zig 版（方案1：二分查找）

const std = @import("std"); // 把 @import(「std」) 存入 std

fn findMin(nums: []const i32) i32 { // 定义函数/方法 findMin
    var low: i32 = 0; // 把 0; 写入 var low: i32
    var high: i32 = @as(i32, @intCast(nums.len)) - 1; // 把 @as(i32, @intCast(数组.长度)) 减 1; 写入 var high: i32
    while (low < high) { // 循环，直到不满足「low 小于 high」
        const pivot = low + @divTrunc(high - low, 2); // 防溢出写法
        const p: usize = @intCast(pivot); // 把 @intCast(pivot); 写入 const p: usize
        const h: usize = @intCast(high); // 把 @intCast(high); 写入 const h: usize
        if (nums[p] < nums[h]) { // 若 数组[节点] 小于 数组[h]
            high = pivot; // 把 pivot; 写入 high
        } else { // 否则
            low = pivot + 1; // 把 pivot 加 1; 写入 low
        }
    }
    const l: usize = @intCast(low); // 把 @intCast(low); 写入 const l: usize
    return nums[l]; // 返回 数组[左指针]
}

pub fn main() !void { // 程序入口：跑内嵌自测用例
    const a1 = [_]i32{ 1, 2, 3 }; // 把 [_]i32{ 1, 2, 3 } 存入 a1
    const a2 = [_]i32{ 3, 4, 5, 1, 2 }; // 把 [_]i32{ 3, 4, 5, 1, 2 } 存入 a2
    const a3 = [_]i32{ 4, 5, 6, 7, 0, 1, 2 }; // 把 [_]i32{ 4, 5, 6, 7, 0, 1, 2 } 存入 a3
    const a4 = [_]i32{ 11, 13, 15, 17 }; // 把 [_]i32{ 11, 13, 15, 17 } 存入 a4
    if (findMin(&a1) != 1) return error.TestFailed; // 若 findMin( 按位与 a1) 不等于 1，直接返回 error.TestFailed
    if (findMin(&a2) != 1) return error.TestFailed; // 若 findMin( 按位与 a2) 不等于 1，直接返回 error.TestFailed
    if (findMin(&a3) != 0) return error.TestFailed; // 若 findMin( 按位与 a3) 不等于 0，直接返回 error.TestFailed
    if (findMin(&a4) != 11) return error.TestFailed; // 若 findMin( 按位与 a4) 不等于 11，直接返回 error.TestFailed
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
