// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145045460
// LeetCode 503. 下一个更大元素 II — Zig 版（方案1）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn nextGreaterElements(nums: []const i32, out: []i32) void { // 定义函数/方法 nextGreaterElements
    const n = nums.len; // 把 数组.长度 存入 元素个数
    for (0..n) |i| out[i] = -1; // 让 下标 i 从 0 走到 元素个数 减一
    var st: [8192]usize = undefined; // 把 undefined; 写入 var st: [8192]usize
    var top: usize = 0; // 把 0; 写入 var top: usize
    for (0..2 * n) |i| { // for (0..2 乘 元素个数) 按位或 下标 i 按位或 {
        const ii = i % n; // 把 下标 i 对…取模 元素个数 存入 ii
        while (top > 0 and nums[st[top - 1]] < nums[ii]) { // 循环，直到不满足「top 超过 0 and 数组[st[top 减 1]] 小于 数组[ii]」
            out[st[top - 1]] = nums[ii]; // 把 数组[ii]; 写入 out[st[top - 1]]
            top -= 1; // top累减 1
        }
        if (i < n) { // 若 下标 i 小于 元素个数
            st[top] = ii; // 把 ii; 写入 st[top]
            top += 1; // top累加 1
        }
    }
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var out: [8]i32 = undefined; // 把 undefined; 写入 var out: [8]i32
    nextGreaterElements(&[_]i32{ 1, 2, 1 }, &out); // nextGreaterElements( 按位与 [_]i32{ 1, 2, 1 }, 按位与 out);
    if (out[0] != 2 or out[1] != -1 or out[2] != 2) return error.TestFailed;
    nextGreaterElements(&[_]i32{ 3, 2, 1 }, &out); // nextGreaterElements( 按位与 [_]i32{ 3, 2, 1 }, 按位与 out);
    if (out[0] != -1 or out[1] != 3 or out[2] != 3) return error.TestFailed;
    std.debug.print("PASS\n", .{});
} // 全部用例通过，输出 PASS
