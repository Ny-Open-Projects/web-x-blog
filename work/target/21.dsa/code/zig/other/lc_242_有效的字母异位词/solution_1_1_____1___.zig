// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135154838
// LeetCode 242. 有效的字母异位词 — Zig 版（方案1）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn isAnagram(s: []const u8, t: []const u8) bool { // 定义判定函数 isAnagram
    if (s.len != t.len) return false; // 若 字符串.长度 不等于 另一字符串.长度，直接返回 false
    var cnt = [_]i32{0} ** 256; // 把 [_]i32{0} 乘 乘 256 存入 计数
    for (s) |c| cnt[c] += 1; // 逐个取出 字符串 的元素（字符）
    for (t) |c| cnt[c] -= 1; // 逐个取出 另一字符串 的元素（字符）
    for (cnt) |v| if (v != 0) return false; // 逐个取出 计数 的元素（值）
    return true; // 返回 true
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    if (!isAnagram("anagram", "nagaram")) return error.TestFailed; // 若 取反 isAnagram(「anagram」, 「anagram」)，直接返回 error.TestFailed
    if (isAnagram("rat", "car")) return error.TestFailed; // 若 isAnagram(「rat」, 「rat」)，直接返回 error.TestFailed
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
