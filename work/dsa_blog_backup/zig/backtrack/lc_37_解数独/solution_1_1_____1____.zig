// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134045157
// LeetCode 37. 解数独 — Zig 版（方案1）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn validSudoku(b: *[9][9]u8, r: usize, c: usize, ch: u8) bool { // 定义函数/方法 validSudoku
    for (0..9) |i| { // 让 下标 i 从 0 走到 9 减一
        if (b[r][i] == ch or b[i][c] == ch) return false; // 若 b[右指针][下标 i] 等于 字符 or b[下标 i][字符] 等于 字符，直接返回 false
    }
    const br = r / 3 * 3; // 把 右指针 除以 3 乘 3 存入 br
    const bc = c / 3 * 3; // 把 字符 除以 3 乘 3 存入 bc
    for (br..br + 3) |i| { // for (br..br 加 3) 按位或 下标 i 按位或 {
        for (bc..bc + 3) |j| { // for (bc..bc 加 3) 按位或 下标 j 按位或 {
            if (b[i][j] == ch) return false; // 若 b[下标 i][下标 j] 等于 字符，直接返回 false
        }
    }
    return true; // 返回 true
}
fn dfsSudoku(b: *[9][9]u8) bool { // 定义函数/方法 dfsSudoku
    for (0..9) |r| { // 让 右指针 从 0 走到 9 减一
        for (0..9) |c| { // 让 字符 从 0 走到 9 减一
            if (b[r][c] == '.') { // 若 b[右指针][字符] 等于 '.'
                var ch: u8 = '1'; // 把 '1'; 写入 var ch: u8
                while (ch <= '9') : (ch += 1) { // 循环，直到不满足「字符 不超过 '9') : (字符 累加 1」
                    if (validSudoku(b, r, c, ch)) { // 若 validSudoku(b, 右指针, 字符, 字符
                        b[r][c] = ch; // 把 字符; 写入 b[r][c]
                        if (dfsSudoku(b)) return true; // 若 dfsSudoku(b)，直接返回 true
                        b[r][c] = '.'; // 把 '.'; 写入 b[r][c]
                    }
                }
                return false; // 返回 false
            }
        }
    }
    return true; // 返回 true
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var board = [9][9]u8{ // 把 [9][9]u8{ 存入 棋盘
        .{ '5', '3', '.', '.', '7', '.', '.', '.', '.' },
        .{ '6', '.', '.', '1', '9', '5', '.', '.', '.' },
        .{ '.', '9', '8', '.', '.', '.', '.', '6', '.' },
        .{ '8', '.', '.', '.', '6', '.', '.', '.', '3' },
        .{ '4', '.', '.', '8', '.', '3', '.', '.', '1' },
        .{ '7', '.', '.', '.', '2', '.', '.', '.', '6' },
        .{ '.', '6', '.', '.', '.', '.', '2', '8', '.' },
        .{ '.', '.', '.', '4', '1', '9', '.', '.', '5' },
        .{ '.', '.', '.', '.', '8', '.', '.', '7', '9' },
    };
    _ = dfsSudoku(&board); // 把 dfsSudoku( 按位与 棋盘); 写入 _
    const solved = [9][]const u8{ // 把 [9][]const u8{ 存入 solved
        "534678912", "672195348", "198342567",
        "859761423", "426853791", "713924856",
        "961537284", "287419635", "345286179",
    };
    for (solved, 0..) |row, r| { // for (solved, 0..) 按位或 row, 右指针 按位或 {
        for (row, 0..) |ch, c| { // for (row, 0..) 按位或 字符, 字符 按位或 {
            if (board[r][c] != ch) return error.TestFailed; // 若 棋盘[右指针][字符] 不等于 字符，直接返回 error.TestFailed
        }
    }
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
