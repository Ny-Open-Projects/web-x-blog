// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133524779
// LeetCode 167. 两数之和II — Zig 版（方案2）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn twoSum(n: []const i32, target: i32, out: *[2]i32) void { // 定义函数/方法 twoSum
    var l: usize = 0; // 把 0; 写入 var l: usize
    var r: usize = n.len - 1; // 把 元素个数.长度 减 1; 写入 var r: usize
    while (l < r) { // 循环，直到不满足「左指针 小于 右指针」
        const s = n[l] + n[r]; // 把 元素个数[左指针] 加 元素个数[右指针] 存入 字符串
        if (s == target) {
            out[0] = @intCast(l + 1);
            out[1] = @intCast(r + 1);
            return;
        }
        if (s < target) l += 1 else r -= 1; // 若 字符串 小于 目标值) 左指针 累加 1 else 右指针 累减 1;
    }
    out[0] = 0;
    out[1] = 0; // 把 0; out[1] 赋值为 0; 写入 out[0]
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var out: [2]i32 = undefined; // 把 undefined; 写入 var out: [2]i32
    twoSum(&[_]i32{ 2, 7, 11, 15 }, 9, &out); // twoSum( 按位与 [_]i32{ 2, 7, 11, 15 }, 9, 按位与 out);
    if (out[0] != 1 or out[1] != 2) return error.TestFailed; // 若 out[0] 不等于 1 or out[1] 不等于 2，直接返回 error.TestFailed
    twoSum(&[_]i32{ 2, 3, 4 }, 6, &out); // twoSum( 按位与 [_]i32{ 2, 3, 4 }, 6, 按位与 out);
    if (out[0] != 1 or out[1] != 3) return error.TestFailed; // 若 out[0] 不等于 1 or out[1] 不等于 3，直接返回 error.TestFailed
    twoSum(&[_]i32{ -1, 0 }, -1, &out); // twoSum( 按位与 [_]i32{ 减 1, 0 }, 减 1, 按位与 out);
    if (out[0] != 1 or out[1] != 2) return error.TestFailed; // 若 out[0] 不等于 1 or out[1] 不等于 2，直接返回 error.TestFailed
    std.debug.print("PASS\n", .{});
} // 全部用例通过，输出 PASS
