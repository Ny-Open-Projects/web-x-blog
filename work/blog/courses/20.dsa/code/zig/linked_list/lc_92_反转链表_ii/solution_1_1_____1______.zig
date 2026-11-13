// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133657416
// LeetCode 92. 反转链表II — Zig 版（方案1）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn reverseBetween(vals: []const i32, left: i32, right: i32, out: []i32) void { // 定义函数/方法 reverseBetween
    @memcpy(out[0..vals.len], vals); // @memcpy(out[0..vals.长度], vals);
    var l: usize = @intCast(left - 1); // 把 @intCast(左边界 减 1); 写入 var l: usize
    var r: usize = @intCast(right - 1); // 把 @intCast(右边界 减 1); 写入 var r: usize
    while (l < r) { // 循环，直到不满足「左指针 小于 右指针」
        const t = out[l]; // 把 out[左指针] 存入 另一字符串
        out[l] = out[r]; // 把 out[右指针]; 写入 out[l]
        out[r] = t; // 把 另一字符串; 写入 out[r]
        l += 1; // 左指针累加 1
        r -= 1; // 右指针累减 1
    }
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var buf: [8]i32 = undefined; // 把 undefined; 写入 var buf: [8]i32
    reverseBetween(&[_]i32{ 1, 2, 3, 4, 5 }, 2, 4, &buf); // reverseBetween( 按位与 [_]i32{ 1, 2, 3, 4, 5 }, 2, 4, 按位与 buf);
    if (buf[1] != 4 or buf[3] != 2) return error.TestFailed; // 若 buf[1] 不等于 4 or buf[3] 不等于 2，直接返回 error.TestFailed
    reverseBetween(&[_]i32{ 1, 2, 3, 4, 5 }, 1, 4, &buf); // reverseBetween( 按位与 [_]i32{ 1, 2, 3, 4, 5 }, 1, 4, 按位与 buf);
    if (buf[0] != 4 or buf[3] != 1 or buf[4] != 5) return error.TestFailed;
    reverseBetween(&[_]i32{5}, 1, 1, &buf); // reverseBetween( 按位与 [_]i32{5}, 1, 1, 按位与 buf);
    if (buf[0] != 5) return error.TestFailed; // 若 buf[0] 不等于 5，直接返回 error.TestFailed
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
