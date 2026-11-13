// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496
// LeetCode 107737496. 代码重构_隔离变化 — Zig 版（方案4：螺旋矩阵方向模拟 placeFill）
const std = @import("std"); // 把 @import(「std」) 存入 std

fn placeFill(n: usize, m: *[8][8]i32) void { // 定义函数/方法 placeFill
    for (0..n) |i| { // 让 下标 i 从 0 走到 元素个数 减一
        for (0..n) |j| m[i][j] = 0; // 让 下标 j 从 0 走到 元素个数 减一
    }
    var row: usize = 0; // 把 0; 写入 var row: usize
    var col: usize = 0; // 把 0; 写入 var col: usize
    var direction: u8 = 'D'; // 把 'D'; 写入 var direction: u8
    var num: i32 = 1; // 把 1; 写入 var num: i32
    const total: i32 = @intCast(n * n); // 把 @intCast(元素个数 乘 元素个数); 写入 const total: i32
    while (num <= total) { // 循环，直到不满足「num 不超过 总和」
        m[row][col] = num; // 把 num; 写入 m[row][col]
        num += 1; // num累加 1
        if (direction == 'D') { // 若 direction 等于 'D'
            if (row + 1 < n and m[row + 1][col] == 0) { // 若 row 加 1 小于 元素个数 and 映射表[row 加 1][col] 等于 0
                row += 1; // row累加 1
            } else { // 否则
                direction = 'R'; // 把 'R'; 写入 direction
                col += 1; // col累加 1
            }
        } else if (direction == 'R') { // 否则，若 direction 等于 'R'
            if (col + 1 < n and m[row][col + 1] == 0) { // 若 col 加 1 小于 元素个数 and 映射表[row][col 加 1] 等于 0
                col += 1; // col累加 1
            } else { // 否则
                direction = 'U'; // 把 'U'; 写入 direction
                row -= 1; // row累减 1
            }
        } else if (direction == 'U') { // 否则，若 direction 等于 'U'
            if (row >= 1 and m[row - 1][col] == 0) { // 若 row 不低于 1 and 映射表[row 减 1][col] 等于 0
                row -= 1; // row累减 1
            } else { // 否则
                direction = 'L'; // 把 'L'; 写入 direction
                col -= 1; // col累减 1
            }
        } else { // 否则
            if (col >= 1 and m[row][col - 1] == 0) { // 若 col 不低于 1 and 映射表[row][col 减 1] 等于 0
                col -= 1; // col累减 1
            } else { // 否则
                direction = 'D'; // 把 'D'; 写入 direction
                row += 1; // row累加 1
            }
        }
    }
}

fn eqMat(a: *[8][8]i32, want: []const []const i32, n: usize) bool { // 定义函数/方法 eqMat
    for (0..n) |i| { // 让 下标 i 从 0 走到 元素个数 减一
        for (0..n) |j| { // 让 下标 j 从 0 走到 元素个数 减一
            if (a[i][j] != want[i][j]) return false; // 若 数组[下标 i][下标 j] 不等于 want[下标 i][下标 j]，直接返回 false
        }
    }
    return true; // 返回 true
}

pub fn main() !void { // 程序入口：跑内嵌自测用例
    var got: [8][8]i32 = undefined; // 把 undefined; 写入 var got: [8][8]i32
    const want3 = [3][]const i32{ &.{ 1, 8, 7 }, &.{ 2, 9, 6 }, &.{ 3, 4, 5 } };
    placeFill(3, &got); // placeFill(3, 按位与 got);
    if (!eqMat(&got, &want3, 3)) return error.TestFailed; // 若 取反 eqMat( 按位与 got, 按位与 want3, 3)，直接返回 error.TestFailed
    const want4 = [4][]const i32{ &.{ 1, 12, 11, 10 }, &.{ 2, 13, 16, 9 }, &.{ 3, 14, 15, 8 }, &.{ 4, 5, 6, 7 } };
    placeFill(4, &got); // placeFill(4, 按位与 got);
    if (!eqMat(&got, &want4, 4)) return error.TestFailed; // 若 取反 eqMat( 按位与 got, 按位与 want4, 4)，直接返回 error.TestFailed
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
