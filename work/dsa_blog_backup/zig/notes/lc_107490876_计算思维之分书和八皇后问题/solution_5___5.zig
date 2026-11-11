// 来源：https://blog.csdn.net/tyro_java/article/details/107490876
// LeetCode 107490876. 分书和八皇后问题 — Zig 版（方案5：八皇后布尔数组标记，行号 0..n-1）
const std = @import("std"); // 把 @import(「std」) 存入 std

var col_row: [8]i32 = undefined; // 把 undefined; 写入 var col_row: [8]i32
var rows: [8]bool = undefined; // 把 undefined; 写入 var rows: [8]bool
var diag1: [16]bool = undefined; // 把 undefined; 写入 var diag1: [16]bool
var diag2: [16]bool = undefined; // 把 undefined; 写入 var diag2: [16]bool
var sols: [100][8]i32 = undefined; // 把 undefined; 写入 var sols: [100][8]i32
var sol_count: usize = 0; // 把 0; 写入 var sol_count: usize
var N: usize = 0; // 把 0; 写入 var N: usize
var OFFSET: usize = 0; // 把 0; 写入 var OFFSET: usize

fn place(col: usize) void { // 定义函数/方法 place
    if (col == N) { // 若 col 等于 N
        sols[sol_count] = col_row; // 把 col_row; 写入 sols[sol_count]
        sol_count += 1; // sol_count累加 1
        return; // return;
    }
    var row: usize = 0; // 把 0; 写入 var row: usize
    while (row < N) : (row += 1) { // 循环，直到不满足「row 小于 N) : (row 累加 1」
        const d1: i32 = @as(i32, @intCast(col)) - @as(i32, @intCast(row)) + @as(i32, @intCast(OFFSET));
        const d2: i32 = @as(i32, @intCast(col)) + @as(i32, @intCast(row));
        if (rows[row] and diag1[@intCast(d1)] and diag2[@intCast(d2)]) { // 若 行数[row] and diag1[@intCast(d1)] and diag2[@intCast(d2)]
            col_row[col] = @intCast(row); // 把 @intCast(row); 写入 col_row[col]
            rows[row] = false; // 把 false; 写入 rows[row]
            diag1[@intCast(d1)] = false; // 把 false; 写入 diag1[@intCast(d1)]
            diag2[@intCast(d2)] = false; // 把 false; 写入 diag2[@intCast(d2)]
            place(col + 1); // place(col 加 1);
            rows[row] = true; // 把 true; 写入 rows[row]
            diag1[@intCast(d1)] = true; // 把 true; 写入 diag1[@intCast(d1)]
            diag2[@intCast(d2)] = true; // 把 true; 写入 diag2[@intCast(d2)]
        }
    }
}

fn nQueensBool(n: usize) usize { // 定义函数/方法 nQueensBool
    N = n; // 把 元素个数; 写入 N
    OFFSET = n - 1; // 把 元素个数 减 1; 写入 OFFSET
    for (0..n) |i| { // 让 下标 i 从 0 走到 元素个数 减一
        rows[i] = true; // 把 true; 写入 rows[i]
        col_row[i] = 0; // 把 0; 写入 col_row[i]
    }
    for (0..2 * n - 1) |i| { // for (0..2 乘 元素个数 减 1) 按位或 下标 i 按位或 {
        diag1[i] = true; // 把 true; 写入 diag1[i]
        diag2[i] = true; // 把 true; 写入 diag2[i]
    }
    sol_count = 0; // 把 0; 写入 sol_count
    place(0); // place(0);
    return sol_count; // 返回 sol_count
}

pub fn main() !void { // 程序入口：跑内嵌自测用例
    const Case = struct { n: usize, count: usize, first: ?[8]i32, flen: usize };
    const cases = [_]Case{ // 把 [_]Case{ 存入 cases
        .{ .n = 8, .count = 92, .first = .{ 0, 4, 7, 5, 2, 6, 1, 3 }, .flen = 8 },
        .{ .n = 1, .count = 1, .first = .{ 0, 0, 0, 0, 0, 0, 0, 0 }, .flen = 1 },
        .{ .n = 2, .count = 0, .first = null, .flen = 0 },
        .{ .n = 4, .count = 2, .first = .{ 1, 3, 0, 2, 0, 0, 0, 0 }, .flen = 4 },
    };
    for (cases, 0..) |c, idx| { // for (cases, 0..) 按位或 字符, idx 按位或 {
        const count = nQueensBool(c.n); // 把 nQueensBool(字符.元素个数) 存入 计数
        if (count != c.count) { // 若 计数 不等于 字符.计数
            std.debug.print("case {d} count {d}\n", .{ idx, count }); // 打印输出
            return error.TestFailed; // 返回 error.TestFailed
        }
        if (c.first) |f| { // 若 字符.first) 按位或 f 按位或
            var j: usize = 0; // 把 0; 写入 var j: usize
            while (j < c.flen) : (j += 1) { // 循环，直到不满足「下标 j 小于 字符.flen) : (下标 j 累加 1」
                if (sols[0][j] != f[j]) return error.TestFailed; // 若 sols[0][下标 j] 不等于 f[下标 j]，直接返回 error.TestFailed
            }
        }
    }
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
