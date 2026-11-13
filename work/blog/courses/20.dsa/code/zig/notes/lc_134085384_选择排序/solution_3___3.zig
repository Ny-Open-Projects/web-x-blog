// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134085384
// 数据结构与算法之排序: 选择排序 — Zig 版（方案3）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn selectionSort(nums: []i32) void { // 定义函数/方法 selectionSort
    const n = nums.len; // 把 数组.长度 存入 元素个数
    for (0..n - 1) |i| { // for (0..元素个数 减 1) 按位或 下标 i 按位或 {
        var m = i; // 把 下标 i 存入 映射表
        for (i + 1..n) |j| { // for (下标 i 加 1..元素个数) 按位或 下标 j 按位或 {
            if (nums[j] < nums[m]) m = j; // 若 数组[下标 j] 小于 数组[映射表]) 映射表 赋值为 下标 j;
        }
        const t = nums[i]; // 把 数组[下标 i] 存入 另一字符串
        nums[i] = nums[m]; // 把 数组[映射表]; 写入 nums[i]
        nums[m] = t; // 把 另一字符串; 写入 nums[m]
    }
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var v1 = [_]i32{ 5, 4, 3, 2, 1 }; // 把 [_]i32{ 5, 4, 3, 2, 1 } 存入 v1
    selectionSort(&v1); // selectionSort( 按位与 v1);
    if (v1[0] != 1 or v1[4] != 5) return error.TestFailed; // 若 v1[0] 不等于 1 or v1[4] 不等于 5，直接返回 error.TestFailed
    std.debug.print("PASS\n", .{});
} // 全部用例通过，输出 PASS
