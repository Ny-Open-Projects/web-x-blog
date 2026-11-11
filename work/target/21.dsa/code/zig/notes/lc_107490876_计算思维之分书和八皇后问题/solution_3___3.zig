// 来源：https://blog.csdn.net/tyro_java/article/details/107490876
// LeetCode 107490876. 分书和八皇后问题 — Zig 版（方案3：八皇后递归 isSafe，行号 1..n）
const std = @import("std"); // 把 @import(「std」) 存入 std

var board: [8]i32 = undefined; // 把 undefined; 写入 var board: [8]i32
var sols: [100][8]i32 = undefined; // 把 undefined; 写入 var sols: [100][8]i32
var sol_count: usize = 0; // 把 0; 写入 var sol_count: usize
var cur_n: usize = 0; // 把 0; 写入 var cur_n: usize

fn isSafe(col: usize, row: i32) bool { // 定义判定函数 isSafe
    var c: usize = 0; // 把 0; 写入 var c: usize
    while (c < col) : (c += 1) { // 循环，直到不满足「字符 小于 col) : (字符 累加 1」
        const dc: i32 = @as(i32, @intCast(c)) - @as(i32, @intCast(col));
        if (board[c] == row or @abs(board[c] - row) == @abs(dc)) return false;
    }
    return true; // 返回 true
}

fn place(col: usize) void { // 定义函数/方法 place
    if (col == cur_n) { // 若 col 等于 cur_n
        sols[sol_count] = board; // 把 棋盘; 写入 sols[sol_count]
        sol_count += 1; // sol_count累加 1
        return; // return;
    }
    var row: i32 = 1; // 把 1; 写入 var row: i32
    while (row <= @as(i32, @intCast(cur_n))) : (row += 1) { // 循环，直到不满足「row 不超过 @as(i32, @intCast(cur_n))) : (row 累加 1」
        if (isSafe(col, row)) { // 若 isSafe(col, row
            board[col] = row; // 把 row; 写入 board[col]
            place(col + 1); // place(col 加 1);
        }
    }
}

pub fn main() !void { // 程序入口：跑内嵌自测用例
    const Case = struct { n: usize, count: usize, first: ?[8]i32, flen: usize };
    const cases = [_]Case{ // 把 [_]Case{ 存入 cases
        .{ .n = 8, .count = 92, .first = .{ 1, 5, 8, 6, 3, 7, 2, 4 }, .flen = 8 },
        .{ .n = 1, .count = 1, .first = .{ 1, 0, 0, 0, 0, 0, 0, 0 }, .flen = 1 },
        .{ .n = 2, .count = 0, .first = null, .flen = 0 },
        .{ .n = 4, .count = 2, .first = .{ 2, 4, 1, 3, 0, 0, 0, 0 }, .flen = 4 },
    };
    for (cases, 0..) |c, idx| { // for (cases, 0..) 按位或 字符, idx 按位或 {
        cur_n = c.n; // 把 字符.元素个数; 写入 cur_n
        sol_count = 0; // 把 0; 写入 sol_count
        place(0); // place(0);
        if (sol_count != c.count) { // 若 sol_count 不等于 字符.计数
            std.debug.print("case {d} count {d}\n", .{ idx, sol_count }); // 打印输出
            return error.TestFailed; // 返回 error.TestFailed
        }
        if (c.first) |f| { // 若 字符.first) 按位或 f 按位或
            var j: usize = 0; // 把 0; 写入 var j: usize
            while (j < c.flen) : (j += 1) { // 循环，直到不满足「下标 j 小于 字符.flen) : (下标 j 累加 1」
                if (sols[0][j] != f[j]) { // 若 sols[0][下标 j] 不等于 f[下标 j]
                    std.debug.print("case {d} first\n", .{idx}); // 打印输出
                    return error.TestFailed; // 返回 error.TestFailed
                }
            }
        }
    }
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
