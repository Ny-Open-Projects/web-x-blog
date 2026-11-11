// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496
// LeetCode 107737496. 代码重构_隔离变化 — Zig 版（方案3：螺旋矩阵递归填充）
const std = @import("std"); // 把 @import(「std」) 存入 std

var M: [6][6]i32 = undefined; // 把 undefined; 写入 var M: [6][6]i32

fn fillSpiral(num0: i32, begin: usize, size: usize) void { // 定义函数/方法 fillSpiral
    var num = num0; // 把 num0 存入 num
    if (size == 0) return; // 若 大小 等于 0) return;
    if (size == 1) { // 若 大小 等于 1
        M[begin][begin] = num; // 把 num; 写入 M[begin][begin]
        return; // return;
    }
    var j: usize = 0; // 把 0; 写入 var j: usize
    while (j < size - 1) : (j += 1) { // 循环，直到不满足「下标 j 小于 大小 减 1) : (下标 j 累加 1」
        M[begin + j][begin] = num; // 把 num; 写入 M[begin + j][begin]
        num += 1; // num累加 1
    }
    j = 0; // 把 0; 写入 下标 j
    while (j < size - 1) : (j += 1) { // 循环，直到不满足「下标 j 小于 大小 减 1) : (下标 j 累加 1」
        M[begin + size - 1][begin + j] = num; // 把 num; 写入 M[begin + size - 1][begin + j]
        num += 1; // num累加 1
    }
    j = size - 1; // 把 大小 减 1; 写入 下标 j
    while (j > 0) { // 循环，直到不满足「下标 j 超过 0」
        M[begin + j][begin + size - 1] = num; // 把 num; 写入 M[begin + j][begin + size - 1]
        num += 1; // num累加 1
        j -= 1; // 下标 j累减 1
    }
    j = size - 1; // 把 大小 减 1; 写入 下标 j
    while (j > 0) { // 循环，直到不满足「下标 j 超过 0」
        M[begin][begin + j] = num; // 把 num; 写入 M[begin][begin + j]
        num += 1; // num累加 1
        j -= 1; // 下标 j累减 1
    }
    fillSpiral(num, begin + 1, size - 2); // fillSpiral(num, begin 加 1, 大小 减 2);
}

fn fmtRow(buf: []u8, row: []const i32) ![]u8 { // 定义函数/方法 fmtRow
    var n: usize = 0; // 把 0; 写入 var n: usize
    for (row, 0..) |x, i| { // for (row, 0..) 按位或 x, 下标 i 按位或 {
        if (i != 0) { // 若 下标 i 不等于 0
            buf[n] = ' '; // 把 ' '; 写入 buf[n]
            n += 1; // 元素个数累加 1
        }
        var cell_buf: [16]u8 = undefined; // 把 undefined; 写入 var cell_buf: [16]u8
        const cell = try std.fmt.bufPrint(&cell_buf, "{d}", .{x}); // 把 try std.fmt.bufPrint( 按位与 cell_buf, 「{d}」, .{x}) 存入 cell
        if (cell.len < 2) { // 若 cell.长度 小于 2
            buf[n] = ' '; // 把 ' '; 写入 buf[n]
            n += 1; // 元素个数累加 1
        }
        for (cell) |ch| { // 逐个取出 cell 的元素（字符）
            buf[n] = ch; // 把 字符; 写入 buf[n]
            n += 1; // 元素个数累加 1
        }
    }
    return buf[0..n]; // 返回 buf[0..元素个数]
}

pub fn main() !void { // 程序入口：跑内嵌自测用例
    fillSpiral(1, 0, 6); // fillSpiral(1, 0, 6);
    const want = [6][]const u8{ // 把 [6][]const u8{ 存入 want
        " 1 20 19 18 17 16",
        " 2 21 32 31 30 15",
        " 3 22 33 36 29 14",
        " 4 23 34 35 28 13",
        " 5 24 25 26 27 12",
        " 6  7  8  9 10 11",
    };
    var buf: [64]u8 = undefined; // 把 undefined; 写入 var buf: [64]u8
    for (want, 0..) |w, i| { // for (want, 0..) 按位或 权重, 下标 i 按位或 {
        const got = try fmtRow(&buf, &M[i]); // 把 try fmtRow( 按位与 buf, 按位与 M[下标 i]) 存入 got
        if (!std.mem.eql(u8, got, w)) { // 若 取反 std.mem.eql(u8, got, 权重
            std.debug.print("spiral6 row {d} failed\n", .{i}); // 打印输出
            return error.TestFailed; // 返回 error.TestFailed
        }
    }
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
