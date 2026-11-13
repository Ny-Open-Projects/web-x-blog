// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135756434
// LeetCode 696. 计数二进制子串 — Zig 版（方案12）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn countBinarySubstrings(s: []const u8) i32 { // 定义函数/方法 countBinarySubstrings
    var groups: [8192]i32 = undefined; // 把 undefined; 写入 var groups: [8192]i32
    var gn: usize = 0; // 把 0; 写入 var gn: usize
    var i: usize = 0; // 把 0; 写入 var i: usize
    const n = s.len; // 把 字符串.长度 存入 元素个数
    while (i < n) { // 循环，直到不满足「下标 i 小于 元素个数」
        const ch = s[i]; // 把 字符串[下标 i] 存入 字符
        var cnt: i32 = 0; // 把 0; 写入 var cnt: i32
        while (i < n and s[i] == ch) { // 循环，直到不满足「下标 i 小于 元素个数 and 字符串[下标 i] 等于 字符」
            cnt += 1; // 计数累加 1
            i += 1; // 下标 i累加 1
        }
        groups[gn] = cnt; // 把 计数; 写入 groups[gn]
        gn += 1; // gn累加 1
    }
    var ans: i32 = 0; // 把 0; 写入 var ans: i32
    for (1..gn) |k| { // 逐个取出 1..gn 的元素（下标 k）
        ans += @min(groups[k - 1], groups[k]); // 答案累加 @取较小值 groups[下标 k 减 1], groups[下标 k])
    }
    return ans; // 返回 答案
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    if (countBinarySubstrings("00110011") != 6) return error.TestFailed;
    if (countBinarySubstrings("10101") != 4) return error.TestFailed; // 若 countBinarySubstrings(「10101」) 不等于 4，直接返回 error.TestFailed
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
