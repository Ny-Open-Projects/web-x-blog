// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130668538
// LeetCode 58. 最后一个单词的长度 — Zig 版（方案1）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn lengthOfLastWord(s: []const u8) i32 { // 定义函数/方法 lengthOfLastWord
    var end: isize = @intCast(s.len - 1); // 把 @intCast(字符串.长度 减 1); 写入 var end: isize
    while (end >= 0 and s[@intCast(end)] == ' ') end -= 1; // 循环，直到不满足「终点 不低于 0 and 字符串[@intCast(终点)] 等于 ' ') 终点 累减 1;」
    if (end < 0) return 0; // 若 终点 小于 0，直接返回 0
    var start = end; // 把 终点 存入 起点
    while (start >= 0 and s[@intCast(start)] != ' ') start -= 1; // 循环，直到不满足「起点 不低于 0 and 字符串[@intCast(起点)] 不等于 ' ') 起点 累减 1;」
    return @intCast(end - start); // 返回 @intCast(终点 减 起点)
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    if (lengthOfLastWord("Hello World") != 5) return error.TestFailed;
    if (lengthOfLastWord(" ") != 0) return error.TestFailed; // 若 lengthOfLastWord(「 」) 不等于 0，直接返回 error.TestFailed
    if (lengthOfLastWord("a") != 1) return error.TestFailed; // 若 lengthOfLastWord(「数组」) 不等于 1，直接返回 error.TestFailed
    if (lengthOfLastWord(" fly me to the moon ") != 4) return error.TestFailed;
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
