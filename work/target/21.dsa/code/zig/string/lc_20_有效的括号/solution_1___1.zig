// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133759617
// LeetCode 20. 有效的括号 — Zig 版（方案1）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn isValid(s: []const u8) bool { // 定义判定函数 isValid
    var stack: [8192]u8 = undefined; // 把 undefined; 写入 var stack: [8192]u8
    var top: usize = 0; // 把 0; 写入 var top: usize
    for (s) |ch| { // 逐个取出 字符串 的元素（字符）
        switch (ch) { // switch (字符) {
            ')' => {
                if (top == 0 or stack[top - 1] != '(') return false; // 若 top 等于 0 or 栈[top 减 1] 不等于 '('，直接返回 false
                top -= 1; // top累减 1
            },
            ']' => {
                if (top == 0 or stack[top - 1] != '[') return false; // 若 top 等于 0 or 栈[top 减 1] 不等于 '['，直接返回 false
                top -= 1; // top累减 1
            },
            '}' => {
                if (top == 0 or stack[top - 1] != '{') return false; // 若 top 等于 0 or 栈[top 减 1] 不等于 '{'，直接返回 false
                top -= 1; // top累减 1
            },
            else => { // 否则
                stack[top] = ch; // 把 字符; 写入 stack[top]
                top += 1; // top累加 1
            },
        }
    }
    return top == 0; // 返回 top 等于 0
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    const tests = [_][]const u8{ "(", "()", "()[]{}", "(]", "([)]", "abc" }; // 把 [_][]const u8{ 「(」, 「(」, 「(」, 「(」, 「(」, 「(」 } 存入 tests
    const want = [_]bool{ false, true, true, false, false, false }; // 把 [_]bool{ false, true, true, false, false, false } 存入 want
    for (tests, want) |t, w| { // for (tests, want) 按位或 另一字符串, 权重 按位或 {
        if (isValid(t) != w) return error.TestFailed; // 若 isValid(另一字符串) 不等于 权重，直接返回 error.TestFailed
    }
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
