// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134032039
// LeetCode 48. 旋转矩阵 — Zig 版
const std = @import("std"); // 把 @import(「std」) 存入 std

// 方案2：先上下翻转行（交换行切片），再沿主对角线转置（原地修改）
fn rotate(matrix: [][]i32) void { // 定义函数/方法 rotate
    const n = matrix.len; // 把 矩阵.长度 存入 元素个数
    var i: usize = 0; // 把 0; 写入 var i: usize
    while (i < n / 2) : (i += 1) { // 循环，直到不满足「下标 i 小于 元素个数 除以 2) : (下标 i 累加 1」
        const tmp = matrix[i]; // 把 矩阵[下标 i] 存入 临时变量
        matrix[i] = matrix[n - 1 - i]; // 把 矩阵[元素个数 减 1 减 下标 i]; 写入 matrix[i]
        matrix[n - 1 - i] = tmp; // 把 临时变量; 写入 matrix[n - 1 - i]
    }
    i = 0; // 把 0; 写入 下标 i
    while (i < n) : (i += 1) { // 循环，直到不满足「下标 i 小于 元素个数) : (下标 i 累加 1」
        var j: usize = 0; // 把 0; 写入 var j: usize
        while (j < i) : (j += 1) { // 循环，直到不满足「下标 j 小于 下标 i) : (下标 j 累加 1」
            const tmp = matrix[i][j]; // 把 矩阵[下标 i][下标 j] 存入 临时变量
            matrix[i][j] = matrix[j][i]; // 把 矩阵[下标 j][下标 i]; 写入 matrix[i][j]
            matrix[j][i] = tmp; // 把 临时变量; 写入 matrix[j][i]
        }
    }
}

fn matFromRows(allocator: std.mem.Allocator, rows: []const []const i32) ![][]i32 { // 定义函数/方法 matFromRows
    const m = try allocator.alloc([]i32, rows.len); // 把 try allocator.alloc([]i32, 行数.长度) 存入 映射表
    for (rows, 0..) |row, i| { // for (行数, 0..) 按位或 row, 下标 i 按位或 {
        m[i] = try allocator.dupe(i32, row); // 把 try allocator.dupe(i32, row); 写入 m[i]
    }
    return m; // 返回 映射表
}

fn eqMatrix(a: []const []i32, b: []const []const i32) bool { // 定义函数/方法 eqMatrix
    if (a.len != b.len) return false; // 若 数组.长度 不等于 b.长度，直接返回 false
    for (a, 0..) |row, i| { // for (数组, 0..) 按位或 row, 下标 i 按位或 {
        if (row.len != b[i].len) return false; // 若 row.长度 不等于 b[下标 i].长度，直接返回 false
        for (row, 0..) |v, j| { // for (row, 0..) 按位或 值, 下标 j 按位或 {
            if (v != b[i][j]) return false; // 若 值 不等于 b[下标 i][下标 j]，直接返回 false
        }
    }
    return true; // 返回 true
}

pub fn main() !void { // 程序入口：跑内嵌自测用例
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator); // 把 std.堆.ArenaAllocator.init(std.堆.page_allocator) 存入 arena
    defer arena.deinit(); // defer arena.deinit();
    const allocator = arena.allocator(); // 把 arena.allocator() 存入 allocator

    // 与 TS 事实源内嵌用例一致（LeetCode 官方示例）
    const c1in = [_][]const i32{ &.{ 1, 2, 3 }, &.{ 4, 5, 6 }, &.{ 7, 8, 9 } };
    const c1exp = [_][]const i32{ &.{ 7, 4, 1 }, &.{ 8, 5, 2 }, &.{ 9, 6, 3 } };
    const c2in = [_][]const i32{ &.{ 5, 1, 9, 11 }, &.{ 2, 4, 8, 10 }, &.{ 13, 3, 6, 7 }, &.{ 15, 14, 12, 16 } };
    const c2exp = [_][]const i32{ &.{ 15, 13, 2, 5 }, &.{ 14, 3, 4, 1 }, &.{ 12, 6, 8, 9 }, &.{ 16, 7, 10, 11 } };

    const Case = struct { in: []const []const i32, exp: []const []const i32 };
    const cases = [_]Case{ // 把 [_]Case{ 存入 cases
        .{ .in = &c1in, .exp = &c1exp },
        .{ .in = &c2in, .exp = &c2exp },
    };
    for (cases, 0..) |c, idx| { // for (cases, 0..) 按位或 字符, idx 按位或 {
        const m = try matFromRows(allocator, c.in); // 把 try matFromRows(allocator, 字符.in) 存入 映射表
        rotate(m); // rotate(映射表);
        if (!eqMatrix(m, c.exp)) { // 若 取反 eqMatrix(映射表, 字符.exp
            std.debug.print("case {d} failed\n", .{idx}); // 打印输出
            return error.TestFailed; // 返回 error.TestFailed
        }
    }
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
