// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496
// LeetCode 107737496. 代码重构_隔离变化 — Zig 版（方案7：螺旋矩阵分派表 place）
const std = @import("std"); // 把 @import(「std」) 存入 std

const Move = struct { // 把 struct { 存入 Move
    row: usize,
    col: usize,
    next_dir: u8 = 0, // 0 表示不变向
};

fn place(row: usize, col: usize, direction: u8, n: usize, m: *const [8][8]i32) Move { // 定义函数/方法 place
    return switch (direction) { // 定义函数/方法 switch
        'D' => if (row + 1 < n and m[row + 1][col] == 0)
            Move{ .row = row + 1, .col = col } // 把 row 加 1, .col 赋值为 col } 写入 Move{ .row
        else // 否则
            Move{ .row = row, .col = col + 1, .next_dir = 'R' },
        'R' => if (col + 1 < n and m[row][col + 1] == 0)
            Move{ .row = row, .col = col + 1 } // 把 row, .col 赋值为 col 加 1 } 写入 Move{ .row
        else // 否则
            Move{ .row = row - 1, .col = col, .next_dir = 'U' },
        'U' => if (row >= 1 and m[row - 1][col] == 0)
            Move{ .row = row - 1, .col = col } // 把 row 减 1, .col 赋值为 col } 写入 Move{ .row
        else // 否则
            Move{ .row = row, .col = col - 1, .next_dir = 'L' },
        else => if (col >= 1 and m[row][col - 1] == 0) // 否则
            Move{ .row = row, .col = col - 1 } // 把 row, .col 赋值为 col 减 1 } 写入 Move{ .row
        else // 否则
            Move{ .row = row + 1, .col = col, .next_dir = 'D' },
    };
}

fn fillSpiral(n: usize, m: *[8][8]i32) void { // 定义函数/方法 fillSpiral
    for (0..n) |i| { // 让 下标 i 从 0 走到 元素个数 减一
        for (0..n) |j| m[i][j] = 0; // 让 下标 j 从 0 走到 元素个数 减一
    }
    var row: usize = 0; // 把 0; 写入 var row: usize
    var col: usize = 0; // 把 0; 写入 var col: usize
    var direction: u8 = 'D'; // 把 'D'; 写入 var direction: u8
    var num: i32 = 1; // 把 1; 写入 var num: i32
    while (num <= @as(i32, @intCast(n * n))) { // 循环，直到不满足「num 不超过 @as(i32, @intCast(元素个数 乘 元素个数」
        m[row][col] = num; // 把 num; 写入 m[row][col]
        num += 1; // num累加 1
        const mv = place(row, col, direction, n, m); // 把 place(row, col, direction, 元素个数, 映射表) 存入 mv
        row = mv.row; // 把 mv.row; 写入 row
        col = mv.col; // 把 mv.col; 写入 col
        if (mv.next_dir != 0) direction = mv.next_dir; // 若 mv.next_dir 不等于 0) direction 赋值为 mv.next_dir;
    }
}

pub fn main() !void { // 程序入口：跑内嵌自测用例
    var m: [8][8]i32 = undefined; // 把 undefined; 写入 var m: [8][8]i32
    const want3 = [3][3]i32{ .{ 1, 8, 7 }, .{ 2, 9, 6 }, .{ 3, 4, 5 } };
    fillSpiral(3, &m); // fillSpiral(3, 按位与 映射表);
    for (want3, 0..) |row, i| { // for (want3, 0..) 按位或 row, 下标 i 按位或 {
        for (row, 0..) |x, j| { // for (row, 0..) 按位或 x, 下标 j 按位或 {
            if (m[i][j] != x) return error.TestFailed; // 若 映射表[下标 i][下标 j] 不等于 x，直接返回 error.TestFailed
        }
    }
    const want4 = [4][4]i32{ .{ 1, 12, 11, 10 }, .{ 2, 13, 16, 9 }, .{ 3, 14, 15, 8 }, .{ 4, 5, 6, 7 } };
    fillSpiral(4, &m); // fillSpiral(4, 按位与 映射表);
    for (want4, 0..) |row, i| { // for (want4, 0..) 按位或 row, 下标 i 按位或 {
        for (row, 0..) |x, j| { // for (row, 0..) 按位或 x, 下标 j 按位或 {
            if (m[i][j] != x) return error.TestFailed; // 若 映射表[下标 i][下标 j] 不等于 x，直接返回 error.TestFailed
        }
    }
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
