// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130726302
// LeetCode 150. 逆波兰表达式求值 — Zig 版（方案1）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn evalRPN(tokens: []const []const u8) i64 { // 定义函数/方法 evalRPN
    var st: [4096]i64 = undefined; // 把 undefined; 写入 var st: [4096]i64
    var top: usize = 0; // 把 0; 写入 var top: usize
    for (tokens) |t| { // 逐个取出 tokens 的元素（另一字符串）
        if (t.len == 1 and (t[0] == '+' or t[0] == '-' or t[0] == '*' or t[0] == '/') and t.len == 1) {
            if (std.mem.eql(u8, t, "+") or std.mem.eql(u8, t, "-") or std.mem.eql(u8, t, "*") or std.mem.eql(u8, t, "/")) {
                const b = st[top - 1]; // 把 st[top 减 1] 存入 b
                top -= 1; // top累减 1
                const a = st[top - 1]; // 把 st[top 减 1] 存入 数组
                top -= 1; // top累减 1
                var r: i64 = 0; // 把 0; 写入 var r: i64
                if (t[0] == '+') r = a + b // 若 另一字符串[0] 等于 ' 加 ') 右指针 赋值为 数组 加 b
                else if (t[0] == '-') r = a - b // 否则，若 另一字符串[0] 等于 ' 减 ') 右指针 赋值为 数组 减 b
                else if (t[0] == '*') r = a * b // 否则，若 另一字符串[0] 等于 ' 乘 ') 右指针 赋值为 数组 乘 b
                else r = @divTrunc(a, b); // 否则
                st[top] = r; // 把 右指针; 写入 st[top]
                top += 1; // top累加 1
            }
        } else { // 否则
            st[top] = std.fmt.parseInt(i64, t, 10) catch unreachable; // 把 std.fmt.转整数(i64, 另一字符串, 10) catch unreachable; 写入 st[top]
            top += 1; // top累加 1
        }
    }
    return st[0]; // 返回 st[0]
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    if (evalRPN(&[_][]const u8{ "2", "1", "+", "3", "*" }) != 9) return error.TestFailed;
    if (evalRPN(&[_][]const u8{ "4", "13", "5", "/", "+" }) != 6) return error.TestFailed;
    if (evalRPN(&[_][]const u8{ "10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+" }) != 22) return error.TestFailed;
    std.debug.print("PASS\n", .{});
} // 全部用例通过，输出 PASS
