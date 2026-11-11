// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107579658
// LeetCode 107579658. 转换视角，提炼共性 — Zig 版（抽象思维之转换视角：统一分书问题与八皇后的回溯框架）
// queen=false: 分书问题（5人，like 偏好矩阵）; queen=true: 八皇后
const std = @import("std"); // 把 @import(「std」) 存入 std

const LIKE = [5][5]i32{ // 把 [5][5]i32{ 存入 LIKE
    .{ 0, 0, 1, 1, 0 },
    .{ 1, 1, 0, 0, 1 },
    .{ 0, 1, 1, 0, 1 },
    .{ 0, 0, 0, 1, 0 },
    .{ 0, 1, 0, 0, 1 },
};

const Ctx = struct { // 把 struct { 存入 Ctx
    queen: bool,
    size: usize,
    q: [8]i32,
    rows: [8]bool,
    diag1: [16]bool,
    diag2: [16]bool,
    results: [64][8]i32 = undefined,
    result_count: usize = 0,

    fn isValid(self: *const Ctx, row: usize, col: usize) bool { // 定义判定函数 isValid
        if (self.queen) return true; // 若 self.queen，直接返回 true
        return LIKE[row][col] == 1; // 返回 LIKE[row][col] 等于 1
    }

    fn isSafe(self: *const Ctx, row: usize, col: usize) bool { // 定义判定函数 isSafe
        if (self.queen) { // 若 self.queen
            return self.rows[row] and self.diag1[col + self.size - 1 - row] and self.diag2[col + row];
        }
        return self.rows[row]; // 返回 self.行数[row]
    }

    fn place(self: *Ctx, col: usize) void { // 定义函数/方法 place
        if (col == self.size) { // 若 col 等于 self.大小
            self.results[self.result_count] = self.q; // 把 self.节点; 写入 self.results[self.result_count]
            self.result_count += 1; // self.result_count累加 1
            return; // return;
        }
        var row: usize = 0; // 把 0; 写入 var row: usize
        while (row < self.size) : (row += 1) { // 循环，直到不满足「row 小于 self.大小) : (row 累加 1」
            if (!self.isValid(row, col)) continue; // 若 取反 self.isValid(row, col)) continue;
            if (!self.isSafe(row, col)) continue; // 若 取反 self.isSafe(row, col)) continue;
            self.q[col] = @intCast(row); // 把 @intCast(row); 写入 self.q[col]
            self.rows[row] = false; // 把 false; 写入 self.rows[row]
            if (self.queen) { // 若 self.queen
                self.diag1[col + self.size - 1 - row] = false; // 把 false; 写入 self.diag1[col + self.size - 1 - row]
                self.diag2[col + row] = false; // 把 false; 写入 self.diag2[col + row]
            }
            self.place(col + 1); // self.place(col 加 1);
            self.rows[row] = true; // 把 true; 写入 self.rows[row]
            if (self.queen) { // 若 self.queen
                self.diag1[col + self.size - 1 - row] = true; // 把 true; 写入 self.diag1[col + self.size - 1 - row]
                self.diag2[col + row] = true; // 把 true; 写入 self.diag2[col + row]
            }
        }
    }
};

fn solveUnified(queen: bool) Ctx { // 定义函数/方法 solveUnified
    const size: usize = if (queen) 8 else 5; // 把 if (queen) 8 else 5; 写入 const size: usize
    var ctx = Ctx{ // 把 Ctx{ 存入 ctx
        .queen = queen,
        .size = size,
        .q = [_]i32{-1} ** 8,
        .rows = [_]bool{true} ** 8,
        .diag1 = [_]bool{true} ** 16,
        .diag2 = [_]bool{true} ** 16,
    };
    ctx.place(0); // ctx.place(0);
    return ctx; // 返回 ctx
}

pub fn main() !void { // 程序入口：跑内嵌自测用例
    const want = [2][5]i32{ .{ 1, 2, 0, 3, 4 }, .{ 1, 4, 0, 3, 2 } };
    const ctx = solveUnified(false); // 把 solveUnified(false) 存入 ctx
    if (ctx.result_count != 2) { // 若 ctx.result_count 不等于 2
        std.debug.print("FAIL count {d}\n", .{ctx.result_count}); // 打印输出
        return error.TestFailed; // 返回 error.TestFailed
    }
    for (want, 0..) |w, i| { // for (want, 0..) 按位或 权重, 下标 i 按位或 {
        for (w, 0..) |x, j| { // for (权重, 0..) 按位或 x, 下标 j 按位或 {
            if (ctx.results[i][j] != x) { // 若 ctx.results[下标 i][下标 j] 不等于 x
                std.debug.print("FAIL results[{d}][{d}]\n", .{ i, j }); // 打印输出
                return error.TestFailed; // 返回 error.TestFailed
            }
        }
    }
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
