// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135129920
// LeetCode 8. 字符串转换整数 (atoi) — Zig 版（方案2）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn myAtoi(s: []const u8) i32 { // 定义函数/方法 myAtoi
    var i: usize = 0; // 把 0; 写入 var i: usize
    const n = s.len; // 把 字符串.长度 存入 元素个数
    while (i < n and s[i] == ' ') i += 1; // 循环，直到不满足「下标 i 小于 元素个数 and 字符串[下标 i] 等于 ' ') 下标 i 累加 1;」
    var sign: i64 = 1; // 把 1; 写入 var sign: i64
    if (i < n and (s[i] == '+' or s[i] == '-')) { // 若 下标 i 小于 元素个数 and (字符串[下标 i] 等于 ' 加 ' or 字符串[下标 i] 等于 ' 减 '
        if (s[i] == '-') sign = -1; // 若 字符串[下标 i] 等于 ' 减 ') sign 赋值为 减 1;
        i += 1; // 下标 i累加 1
    }
    var ans: i64 = 0; // 把 0; 写入 var ans: i64
    while (i < n and std.ascii.isDigit(s[i])) { // 循环，直到不满足「下标 i 小于 元素个数 and std.ascii.isDigit(字符串[下标 i]」
        ans = ans * 10 + @as(i64, s[i] - '0'); // 把 答案 乘 10 加 @as(i64, 字符串[下标 i] 减 '0'); 写入 答案
        if (ans > 2147483648) ans = 2147483648; // 若 答案 超过 2147483648) 答案 赋值为 2147483648;
        i += 1; // 下标 i累加 1
    }
    ans *= sign; // 把 sign; 写入 ans *
    if (ans > 2147483647) return 2147483647; // 若 答案 超过 2147483647，直接返回 2147483647
    if (ans < -2147483648) return -2147483648; // 若 答案 小于 减 2147483648，直接返回 减 2147483648
    return @intCast(ans); // 返回 @intCast(答案)
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    if (myAtoi("42") != 42) return error.TestFailed; // 若 myAtoi(「42」) 不等于 42，直接返回 error.TestFailed
    if (myAtoi(" -42") != -42) return error.TestFailed; // 若 myAtoi(「 减 42」) 不等于 减 42，直接返回 error.TestFailed
    if (myAtoi("4193 with words") != 4193) return error.TestFailed; // 若 myAtoi(「4193 with 单词列表」) 不等于 4193，直接返回 error.TestFailed
    if (myAtoi("-91283472332") != -2147483648) return error.TestFailed;
    if (myAtoi("words and 987") != 0) return error.TestFailed; // 若 myAtoi(「单词列表 and 987」) 不等于 0，直接返回 error.TestFailed
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
