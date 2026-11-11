// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134312127
// LeetCode 383. 赎金信 — Zig 版（方案1）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn canConstruct(ransom: []const u8, magazine: []const u8) bool { // 定义函数/方法 canConstruct
    var cnt = [_]i32{0} ** 26; // 把 [_]i32{0} 乘 乘 26 存入 计数
    for (magazine) |c| cnt[c - 'a'] += 1; // 逐个取出 magazine 的元素（字符）
    for (ransom) |c| { // 逐个取出 ransom 的元素（字符）
        cnt[c - 'a'] -= 1; // 把 1; 写入 cnt[c - 'a'] -
        if (cnt[c - 'a'] < 0) return false; // 若 计数[字符 减 '数组'] 小于 0，直接返回 false
    }
    return true; // 返回 true
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    if (canConstruct("a", "b")) return error.TestFailed; // 若 canConstruct(「数组」, 「数组」)，直接返回 error.TestFailed
    if (canConstruct("aa", "ab")) return error.TestFailed; // 若 canConstruct(「aa」, 「aa」)，直接返回 error.TestFailed
    if (!canConstruct("aa", "aab")) return error.TestFailed; // 若 取反 canConstruct(「aa」, 「aa」)，直接返回 error.TestFailed
    std.debug.print("PASS\n", .{});
} // 全部用例通过，输出 PASS
