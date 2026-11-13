// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135004189
// LeetCode 3. 无重复字符的最长子串 — Zig 版（方案3）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn lengthOfLongestSubstring(s: []const u8) i32 { // 定义函数/方法 lengthOfLongestSubstring
    var set = [_]bool{false} ** 256; // 把 [_]bool{false} 乘 乘 256 存入 set
    var left: usize = 0; // 把 0; 写入 var left: usize
    var max_len: i32 = 0; // 把 0; 写入 var max_len: i32
    for (s, 0..) |c, right| { // for (字符串, 0..) 按位或 字符, 右边界 按位或 {
        while (set[c]) { // 循环，直到不满足「set[字符]」
            set[s[left]] = false; // 把 false; 写入 set[s[left]]
            left += 1; // 左边界累加 1
        }
        set[c] = true; // 把 true; 写入 set[c]
        const len: i32 = @intCast(right - left + 1); // 把 @intCast(右边界 减 左边界 加 1); 写入 const len: i32
        if (len > max_len) max_len = len; // 若 长度 超过 max_len) max_len 赋值为 长度;
    }
    return max_len; // 返回 max_len
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    if (lengthOfLongestSubstring("abcabcbb") != 3) return error.TestFailed;
    if (lengthOfLongestSubstring("bbbbb") != 1) return error.TestFailed;
    if (lengthOfLongestSubstring("pwwkew") != 3) return error.TestFailed;
    if (lengthOfLongestSubstring("") != 0) return error.TestFailed; // 若 lengthOfLongestSubstring(「」) 不等于 0，直接返回 error.TestFailed
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
