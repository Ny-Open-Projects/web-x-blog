// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130753613
// LeetCode 392. 判断子序列 — Zig 版（方案3）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn isSubsequence(s: []const u8, t: []const u8) bool { // 定义判定函数 isSubsequence
    var i: usize = 0; // 把 0; 写入 var i: usize
    for (t) |c| { // 逐个取出 另一字符串 的元素（字符）
        if (i < s.len and s[i] == c) i += 1; // 若 下标 i 小于 字符串.长度 and 字符串[下标 i] 等于 字符) 下标 i 累加 1;
    }
    return i == s.len; // 返回 下标 i 等于 字符串.长度
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    if (!isSubsequence("abc", "ahbgdc")) return error.TestFailed; // 若 取反 isSubsequence(「abc」, 「abc」)，直接返回 error.TestFailed
    if (isSubsequence("axc", "ahbgdc")) return error.TestFailed; // 若 isSubsequence(「axc」, 「axc」)，直接返回 error.TestFailed
    std.debug.print("PASS\n", .{});
} // 全部用例通过，输出 PASS
