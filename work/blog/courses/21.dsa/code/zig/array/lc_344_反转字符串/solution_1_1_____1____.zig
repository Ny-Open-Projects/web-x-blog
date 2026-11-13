// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134135902
// LeetCode 344. 反转字符串 — Zig 版（方案1）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn reverseString(s: []u8) void { // 定义函数/方法 reverseString
    if (s.len == 0) return; // 若 字符串.长度 等于 0) return;
    var i: usize = 0; // 把 0; 写入 var i: usize
    var j: usize = s.len - 1; // 把 字符串.长度 减 1; 写入 var j: usize
    while (i < j) : ({ // 循环，直到不满足「下标 i 小于 下标 j) : (」
        i += 1; // 下标 i累加 1
        j -= 1; // 下标 j累减 1
    }) { // }) {
        const t = s[i]; // 把 字符串[下标 i] 存入 另一字符串
        s[i] = s[j]; // 把 字符串[下标 j]; 写入 s[i]
        s[j] = t; // 把 另一字符串; 写入 s[j]
    }
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var buf1 = [_]u8{ 'h', 'e', 'l', 'l', 'o' }; // 把 [_]u8{ 'h', 'e', '左指针', '左指针', 'o' } 存入 buf1
    reverseString(&buf1); // reverseString( 按位与 buf1);
    if (!std.mem.eql(u8, &buf1, "olleh")) return error.TestFailed;
    var buf2 = [_]u8{ 'H', 'a', 'n', 'n', 'a', 'h' }; // 把 [_]u8{ 'H', '数组', '元素个数', '元素个数', '数组', 'h' } 存入 buf2
    reverseString(&buf2); // reverseString( 按位与 buf2);
    if (!std.mem.eql(u8, &buf2, "hannaH")) return error.TestFailed;
    std.debug.print("PASS\n", .{});
} // 全部用例通过，输出 PASS
