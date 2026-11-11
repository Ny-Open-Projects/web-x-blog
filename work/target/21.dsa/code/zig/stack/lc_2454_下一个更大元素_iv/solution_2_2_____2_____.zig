// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145397916
// LeetCode 2454. 下一个更大元素 IV — Zig 版（方案2）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn secondGreater(nums: []const i32, out: []i32) void { // 定义函数/方法 secondGreater
    const n = nums.len; // 把 数组.长度 存入 元素个数
    for (0..n) |i| out[i] = -1; // 让 下标 i 从 0 走到 元素个数 减一
    var s1: [4096]usize = undefined; // 把 undefined; 写入 var s1: [4096]usize
    var t1: usize = 0; // 把 0; 写入 var t1: usize
    var s2: [4096]usize = undefined; // 把 undefined; 写入 var s2: [4096]usize
    var t2: usize = 0; // 把 0; 写入 var t2: usize
    for (0..n) |i| { // 让 下标 i 从 0 走到 元素个数 减一
        while (t2 > 0 and nums[s2[t2 - 1]] < nums[i]) { // 循环，直到不满足「t2 超过 0 and 数组[s2[t2 减 1]] 小于 数组[下标 i]」
            t2 -= 1; // t2累减 1
            out[s2[t2]] = nums[i]; // 把 数组[下标 i]; 写入 out[s2[t2]]
        }
        while (t1 > 0 and nums[s1[t1 - 1]] < nums[i]) { // 循环，直到不满足「t1 超过 0 and 数组[s1[t1 减 1]] 小于 数组[下标 i]」
            t1 -= 1; // t1累减 1
            s2[t2] = s1[t1]; // 把 s1[t1]; 写入 s2[t2]
            t2 += 1; // t2累加 1
        }
        s1[t1] = i; // 把 下标 i; 写入 s1[t1]
        t1 += 1; // t1累加 1
    }
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var out: [8]i32 = undefined; // 把 undefined; 写入 var out: [8]i32
    secondGreater(&[_]i32{ 2, 4, 0, 9, 6 }, &out); // secondGreater( 按位与 [_]i32{ 2, 4, 0, 9, 6 }, 按位与 out);
    if (out[0] != 9 or out[2] != 6 or out[4] != -1) return error.TestFailed;
    secondGreater(&[_]i32{ 5, 4, 3, 2, 1 }, &out); // secondGreater( 按位与 [_]i32{ 5, 4, 3, 2, 1 }, 按位与 out);
    if (out[0] != -1) return error.TestFailed; // 若 out[0] 不等于 减 1，直接返回 error.TestFailed
    std.debug.print("PASS\n", .{});
} // 全部用例通过，输出 PASS
