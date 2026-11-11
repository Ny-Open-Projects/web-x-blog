// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130778527
// LeetCode 125. 验证回文串 — Zig 版（方案1）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn isPalindrome(s: []const u8) bool { // 定义判定函数 isPalindrome
    var fbuf: [8192]u8 = undefined; // 把 undefined; 写入 var fbuf: [8192]u8
    var n: usize = 0; // 把 0; 写入 var n: usize
    for (s) |c| { // 逐个取出 字符串 的元素（字符）
        if (std.ascii.isAlphanumeric(c)) { // 若 std.ascii.isAlphanumeric(字符
            fbuf[n] = std.ascii.toLower(c); // 把 std.ascii.toLower(字符); 写入 fbuf[n]
            n += 1; // 元素个数累加 1
        }
    }
    if (n == 0) return true; // 若 元素个数 等于 0，直接返回 true
    var i: usize = 0; // 把 0; 写入 var i: usize
    var j: usize = n - 1; // 把 元素个数 减 1; 写入 var j: usize
    while (i < j) { // 循环，直到不满足「下标 i 小于 下标 j」
        if (fbuf[i] != fbuf[j]) return false; // 若 fbuf[下标 i] 不等于 fbuf[下标 j]，直接返回 false
        i += 1; // 下标 i累加 1
        j -= 1; // 下标 j累减 1
    }
    return true; // 返回 true
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    if (!isPalindrome("A man, a plan, a canal: Panama")) return error.TestFailed;
    if (isPalindrome("race a car")) return error.TestFailed; // 若 isPalindrome(「race 数组 car」)，直接返回 error.TestFailed
    if (!isPalindrome(" ")) return error.TestFailed; // 若 取反 isPalindrome(「 」)，直接返回 error.TestFailed
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
