// 来源：https://blog.csdn.net/tyro_java/article/details/107490876
// LeetCode 107490876. 分书和八皇后问题 — Zig 版（方案7：八皇后位置对列表）
const std = @import("std"); // 把 @import(「std」) 存入 std

const Pair = struct { row: i32, col: i32 }; // 把 struct { row: i32, col: i32 } 存入 Pair

var positions: [8]Pair = undefined; // 把 undefined; 写入 var positions: [8]Pair
var plen: usize = 0; // 把 0; 写入 var plen: usize
var sols: [100][8]i32 = undefined; // 把 undefined; 写入 var sols: [100][8]i32
var sol_count: usize = 0; // 把 0; 写入 var sol_count: usize
var N: usize = 0; // 把 0; 写入 var N: usize

fn safe(r: i32, c: i32) bool { // 定义函数/方法 safe
    var i: usize = 0; // 把 0; 写入 var i: usize
    while (i < plen) : (i += 1) { // 循环，直到不满足「下标 i 小于 plen) : (下标 i 累加 1」
        if (positions[i].row == r or @abs(positions[i].row - r) == @abs(positions[i].col - c)) return false;
    }
    return true; // 返回 true
}

fn solve(col: usize) void { // 定义函数/方法 solve
    if (col == N) { // 若 col 等于 N
        var i: usize = 0; // 把 0; 写入 var i: usize
        while (i < N) : (i += 1) sols[sol_count][i] = positions[i].row;
        sol_count += 1; // sol_count累加 1
        return; // return;
    }
    var r: i32 = 0; // 把 0; 写入 var r: i32
    while (r < @as(i32, @intCast(N))) : (r += 1) { // 循环，直到不满足「右指针 小于 @as(i32, @intCast(N))) : (右指针 累加 1」
        if (safe(r, @intCast(col))) { // 若 safe(右指针, @intCast(col
            positions[plen] = .{ .row = r, .col = @intCast(col) };
            plen += 1; // plen累加 1
            solve(col + 1); // solve(col 加 1);
            plen -= 1; // plen累减 1
        }
    }
}

fn nQueensSimple(n: usize) usize { // 定义函数/方法 nQueensSimple
    N = n; // 把 元素个数; 写入 N
    plen = 0; // 把 0; 写入 plen
    sol_count = 0; // 把 0; 写入 sol_count
    solve(0); // solve(0);
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
        const count = nQueensSimple(c.n); // 把 nQueensSimple(字符.元素个数) 存入 计数
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
