// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135917076
// LeetCode 567. 字符串的排列 — Zig 版（方案3）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn cntEq(a: *const [26]i32, b: *const [26]i32) bool { // 定义函数/方法 cntEq
    for (a, b) |x, y| if (x != y) return false; // 把 y) return false; 写入 for (a, b) |x, y| if (x !
    return true; // 返回 true
}
fn checkInclusion(s1: []const u8, s2: []const u8) bool { // 定义判定函数 checkInclusion
    const m = s1.len; // 把 s1.长度 存入 映射表
    const n = s2.len; // 把 s2.长度 存入 元素个数
    if (m > n) return false; // 若 映射表 超过 元素个数，直接返回 false
    var s1c = [_]i32{0} ** 26; // 把 [_]i32{0} 乘 乘 26 存入 s1c
    var s2c = [_]i32{0} ** 26; // 把 [_]i32{0} 乘 乘 26 存入 s2c
    for (0..m) |i| { // 让 下标 i 从 0 走到 映射表 减一
        s1c[s1[i] - 'a'] += 1; // 把 1; 写入 s1c[s1[i] - 'a'] +
        s2c[s2[i] - 'a'] += 1; // 把 1; 写入 s2c[s2[i] - 'a'] +
    }
    if (cntEq(&s1c, &s2c)) return true; // 若 cntEq( 按位与 s1c, 按位与 s2c)，直接返回 true
    for (m..n) |i| { // 逐个取出 映射表..元素个数 的元素（下标 i）
        s2c[s2[i] - 'a'] += 1; // 把 1; 写入 s2c[s2[i] - 'a'] +
        s2c[s2[i - m] - 'a'] -= 1; // 把 1; 写入 s2c[s2[i - m] - 'a'] -
        if (cntEq(&s1c, &s2c)) return true; // 若 cntEq( 按位与 s1c, 按位与 s2c)，直接返回 true
    }
    return false; // 返回 false
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    if (!checkInclusion("ab", "eidbaooo")) return error.TestFailed; // 若 取反 checkInclusion(「ab」, 「ab」)，直接返回 error.TestFailed
    if (checkInclusion("ab", "eidboaoo")) return error.TestFailed; // 若 checkInclusion(「ab」, 「ab」)，直接返回 error.TestFailed
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
