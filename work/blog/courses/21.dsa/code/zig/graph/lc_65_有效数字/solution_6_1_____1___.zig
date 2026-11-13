// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133920771
// LeetCode 65. 有效数字 — Zig 版
const std = @import("std"); // 把 @import(「std」) 存入 std

// 方案6（确定有限状态自动机 DFA，其余字符 lowercase）
// 字符类：0=blank 1=sign 2='.' 3=digit 4='e' 5=other（-1 表示无转移）
// 与 TS 的 graph 一致；非数字/空白/符号字符统一 lowercase，'E' 归并为 'e'
const CLS_BLANK = 0; // 把 0 存入 CLS_BLANK
const CLS_SIGN = 1; // 把 1 存入 CLS_SIGN
const CLS_DOT = 2; // 把 2 存入 CLS_DOT
const CLS_DIGIT = 3; // 把 3 存入 CLS_DIGIT
const CLS_E = 4; // 把 4 存入 CLS_E
const CLS_OTHER = 5; // 把 5 存入 CLS_OTHER
const CLS_N = 6; // 把 6 存入 CLS_N

const trans = [8][CLS_N]i32{ // 把 [8][CLS_N]i32{ 存入 trans
    .{ 0, 1, 2, 6, -1, -1 },
    .{ -1, -1, 2, 6, -1, -1 },
    .{ -1, -1, -1, 3, -1, -1 },
    .{ -1, -1, -1, 3, 4, -1 },
    .{ -1, 7, -1, 5, -1, -1 },
    .{ -1, -1, -1, 5, -1, -1 },
    .{ -1, -1, 3, 6, 4, -1 },
    .{ -1, -1, -1, 5, -1, -1 },
};

fn isNumber(s: []const u8) bool { // 定义判定函数 isNumber
    const t = std.mem.trim(u8, s, " \t\n\r\x0b\x0c"); // 等价于 TS 的 trim()
    var state: i32 = 0; // 把 0; 写入 var state: i32
    for (t) |ch0| { // 逐个取出 另一字符串 的元素（ch0）
        const ch = if (ch0 >= 'A' and ch0 <= 'Z') ch0 - 'A' + 'a' else ch0; // lowercase
        var cls: usize = CLS_OTHER; // 把 CLS_OTHER; 写入 var cls: usize
        if (ch >= '0' and ch <= '9') { // 若 字符 不低于 '0' and 字符 不超过 '9'
            cls = CLS_DIGIT; // 把 CLS_DIGIT; 写入 cls
        } else if (ch == ' ') { // 否则，若 字符 等于 ' '
            cls = CLS_BLANK; // 把 CLS_BLANK; 写入 cls
        } else if (ch == '+' or ch == '-') { // 否则，若 字符 等于 ' 加 ' or 字符 等于 ' 减 '
            cls = CLS_SIGN; // 把 CLS_SIGN; 写入 cls
        } else if (ch == '.') { // 否则，若 字符 等于 '.'
            cls = CLS_DOT; // 把 CLS_DOT; 写入 cls
        } else if (ch == 'e') { // 否则，若 字符 等于 'e'
            cls = CLS_E; // 把 CLS_E; 写入 cls
        }
        const ns = trans[@intCast(state)][cls]; // 把 trans[@intCast(state)][cls] 存入 ns
        if (ns < 0) return false; // 若 ns 小于 0，直接返回 false
        state = ns; // 把 ns; 写入 state
    }
    return state == 3 or state == 5 or state == 6; // 返回 state 等于 3 or state 等于 5 or state 等于 6
}

pub fn main() !void { // 程序入口：跑内嵌自测用例
    if (!isNumber("0")) return error.ShouldBeTrue; // 若 取反 isNumber(「0」)，直接返回 error.ShouldBeTrue
    if (isNumber("abc")) return error.ShouldBeFalse; // 若 isNumber(「abc」)，直接返回 error.ShouldBeFalse
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
