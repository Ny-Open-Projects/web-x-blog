// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134588341
// LeetCode 541. 反转字符串II — Zig 版（方案1）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn reverseStr(s: []const u8, k: usize, out: []u8) void { // 定义函数/方法 reverseStr
    @memcpy(out[0..s.len], s); // @memcpy(out[0..字符串.长度], 字符串);
    var i: usize = 0; // 把 0; 写入 var i: usize
    while (i < s.len) : (i += 2 * k) { // 循环，直到不满足「下标 i 小于 字符串.长度) : (下标 i 累加 2 乘 下标 k」
        const end = @min(i + k, s.len); // 把 @取较小值 下标 i 加 下标 k, 字符串.长度) 存入 终点
        var l = i; // 把 下标 i 存入 左指针
        var r = end - 1; // 把 终点 减 1 存入 右指针
        while (l < r) : ({ // 循环，直到不满足「左指针 小于 右指针) : (」
            l += 1; // 左指针累加 1
            r -= 1; // 右指针累减 1
        }) { // }) {
            const t = out[l]; // 把 out[左指针] 存入 另一字符串
            out[l] = out[r]; // 把 out[右指针]; 写入 out[l]
            out[r] = t; // 把 另一字符串; 写入 out[r]
        }
    }
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var buf: [64]u8 = undefined; // 把 undefined; 写入 var buf: [64]u8
    reverseStr("abcdefg", 2, &buf); // reverseStr(「abcdefg」, 2, 按位与 buf);
    if (!std.mem.eql(u8, buf[0..7], "bacdfeg")) return error.TestFailed;
    reverseStr("abcd", 2, &buf); // reverseStr(「abcd」, 2, 按位与 buf);
    if (!std.mem.eql(u8, buf[0..4], "bacd")) return error.TestFailed;
    reverseStr("abc", 1, &buf); // reverseStr(「abc」, 1, 按位与 buf);
    if (!std.mem.eql(u8, buf[0..3], "abc")) return error.TestFailed; // 若 取反 std.mem.eql(u8, buf[0..3], 「abc」)，直接返回 error.TestFailed
    std.debug.print("PASS\n", .{});
} // 全部用例通过，输出 PASS
