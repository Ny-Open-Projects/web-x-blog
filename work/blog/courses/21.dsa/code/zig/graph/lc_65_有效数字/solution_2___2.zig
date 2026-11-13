// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133920771
// LeetCode 65. 有效数字 — Zig 版
const std = @import("std"); // 把 @import(「std」) 存入 std

// 方案2（线性扫描）
fn isNumber(s: []const u8) bool { // 定义判定函数 isNumber
    const t = std.mem.trim(u8, s, " \t\n\r\x0b\x0c"); // 等价于 TS 的 trim()
    if (t.len == 0) return false; // 若 另一字符串.长度 等于 0，直接返回 false
    var has_dot = false; // 把 false 存入 has_dot
    var has_e = false; // 把 false 存入 has_e
    var has_digit = false; // 把 false 存入 has_digit
    var i: usize = 0; // 把 0; 写入 var i: usize
    while (i < t.len) : (i += 1) { // 循环，直到不满足「下标 i 小于 另一字符串.长度) : (下标 i 累加 1」
        const c = t[i]; // 把 另一字符串[下标 i] 存入 字符
        if (c == '.') { // 若 字符 等于 '.'
            if (has_dot or has_e) return false; // 若 has_dot or has_e，直接返回 false
            has_dot = true; // 把 true; 写入 has_dot
        } else if (c == 'e' or c == 'E') { // 否则，若 字符 等于 'e' or 字符 等于 'E'
            if (has_e or !has_digit) return false; // 若 has_e or 取反 has_digit，直接返回 false
            has_e = true; // 把 true; 写入 has_e
            has_digit = false; // 把 false; 写入 has_digit
        } else if (c == '+' or c == '-') { // 否则，若 字符 等于 ' 加 ' or 字符 等于 ' 减 '
            if (i > 0 and t[i - 1] != 'e' and t[i - 1] != 'E') return false;
        } else if (c >= '0' and c <= '9') { // 否则，若 字符 不低于 '0' and 字符 不超过 '9'
            has_digit = true; // 把 true; 写入 has_digit
        } else { // 否则
            return false; // 返回 false
        }
    }
    return has_digit; // 返回 has_digit
}

pub fn main() !void { // 程序入口：跑内嵌自测用例
    if (isNumber("abc")) return error.ShouldBeFalse; // 若 isNumber(「abc」)，直接返回 error.ShouldBeFalse
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
