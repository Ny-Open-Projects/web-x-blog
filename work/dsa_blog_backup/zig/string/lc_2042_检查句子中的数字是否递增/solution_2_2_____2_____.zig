// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/138481618
// LeetCode 2042. 检查句子中的数字是否递增 — Zig 版（方案2）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn areNumbersAscending(s: []const u8) bool { // 定义函数/方法 areNumbersAscending
    var it = std.mem.tokenizeScalar(u8, s, ' '); // 把 std.mem.tokenizeScalar(u8, 字符串, ' ') 存入 it
    var prev: i64 = -1; // 把 减 1; 写入 var prev: i64
    while (it.next()) |tok| { // 循环，直到不满足「it.下一个()) 按位或 tok 按位或」
        if (tok.len > 0 and std.ascii.isDigit(tok[0])) { // 若 tok.长度 超过 0 and std.ascii.isDigit(tok[0]
            const num = std.fmt.parseInt(i64, tok, 10) catch 0; // 把 std.fmt.转整数(i64, tok, 10) catch 0 存入 num
            if (num <= prev) return false; // 若 num 不超过 前一个，直接返回 false
            prev = num; // 把 num; 写入 前一个
        }
    }
    return true; // 返回 true
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    if (!areNumbersAscending("1 box has 3 blue 4 red 6 green and 12 yellow marbles")) return error.TestFailed;
    if (areNumbersAscending("hello world 5 x 5")) return error.TestFailed;
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
