// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134053461
// 数据结构与算法之排序: 侏儒排序 — Zig 版（方案5）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn gnomeSort(nums: []i32) void { // 定义函数/方法 gnomeSort
    var i: usize = 0; // 把 0; 写入 var i: usize
    while (i < nums.len) { // 循环，直到不满足「下标 i 小于 数组.长度」
        if (i == 0 or nums[i - 1] <= nums[i]) { // 若 下标 i 等于 0 or 数组[下标 i 减 1] 不超过 数组[下标 i]
            i += 1; // 下标 i累加 1
        } else { // 否则
            const t = nums[i - 1]; // 把 数组[下标 i 减 1] 存入 另一字符串
            nums[i - 1] = nums[i]; // 把 数组[下标 i]; 写入 nums[i - 1]
            nums[i] = t; // 把 另一字符串; 写入 nums[i]
            i -= 1; // 下标 i累减 1
        }
    }
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var v1 = [_]i32{ 5, 4, 3, 2, 1 }; // 把 [_]i32{ 5, 4, 3, 2, 1 } 存入 v1
    gnomeSort(&v1); // gnomeSort( 按位与 v1);
    if (v1[0] != 1 or v1[4] != 5) return error.TestFailed; // 若 v1[0] 不等于 1 or v1[4] 不等于 5，直接返回 error.TestFailed
    std.debug.print("PASS\n", .{});
} // 全部用例通过，输出 PASS
