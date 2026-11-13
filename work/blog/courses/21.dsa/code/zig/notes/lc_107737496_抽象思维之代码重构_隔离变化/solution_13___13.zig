// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496
// LeetCode 107737496. 代码重构_隔离变化 — Zig 版（方案13：微型正则匹配 match/matchhere/matchstar）
const std = @import("std"); // 把 @import(「std」) 存入 std

fn matchhere(re: []const u8, text: []const u8) bool { // 定义函数/方法 matchhere
    if (re.len == 0) return true; // 若 re.长度 等于 0，直接返回 true
    if (re.len >= 2 and re[1] == '*') return matchstar(re[0], re[2..], text);
    if (re[0] == '$' and re.len == 1) return text.len == 0; // 若 re[0] 等于 '$' and re.长度 等于 1，直接返回 text.长度 等于 0
    if (text.len > 0 and (re[0] == '.' or re[0] == text[0])) return matchhere(re[1..], text[1..]);
    return false; // 返回 false
}

fn matchstar(c: u8, re: []const u8, text: []const u8) bool { // 定义函数/方法 matchstar
    var i: usize = 0; // 把 0; 写入 var i: usize
    while (true) { // 循环，直到不满足「true」
        if (matchhere(re, text[i..])) return true; // 若 matchhere(re, text[下标 i..])，直接返回 true
        if (i >= text.len) break; // 若 下标 i 不低于 text.长度) break;
        if (text[i] != c and c != '.') break; // 若 text[下标 i] 不等于 字符 and 字符 不等于 '.') break;
        i += 1; // 下标 i累加 1
    }
    return false; // 返回 false
}

fn match(re: []const u8, text: []const u8) bool { // 定义函数/方法 match
    if (re.len > 0 and re[0] == '^') return matchhere(re[1..], text);
    var i: usize = 0; // 把 0; 写入 var i: usize
    while (true) { // 循环，直到不满足「true」
        if (matchhere(re, text[i..])) return true; // 若 matchhere(re, text[下标 i..])，直接返回 true
        if (i >= text.len) break; // 若 下标 i 不低于 text.长度) break;
        i += 1; // 下标 i累加 1
    }
    return false; // 返回 false
}

pub fn main() !void { // 程序入口：跑内嵌自测用例
    if (!match("abc", "xxabcxx")) return error.TestFailed; // 若 取反 match(「abc」, 「abc」)，直接返回 error.TestFailed
    if (!match("a.c", "axc")) return error.TestFailed; // 若 取反 match(「数组.字符」, 「数组.字符」)，直接返回 error.TestFailed
    if (!match("a*", "aaaa")) return error.TestFailed; // 若 取反 match(「数组 乘 」, 「数组 乘 」)，直接返回 error.TestFailed
    if (match("^a", "ba")) return error.TestFailed; // 若 match(「 按位异或 数组」, 「 按位异或 数组」)，直接返回 error.TestFailed
    if (!match("c$", "abc")) return error.TestFailed; // 若 取反 match(「字符$」, 「字符$」)，直接返回 error.TestFailed
    if (!match("a.*c", "aXYZc")) return error.TestFailed; // 若 取反 match(「数组. 乘 字符」, 「数组. 乘 字符」)，直接返回 error.TestFailed
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
