// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134026430
// LeetCode 54. 螺旋矩阵 — Zig 版
const std = @import("std"); // 把 @import(「std」) 存入 std

// 方案1：四边界逐层收缩（isize 索引避免 usize 下溢）
fn spiralOrder(allocator: std.mem.Allocator, matrix: []const []const i32) !std.ArrayList(i32) { // 定义函数/方法 spiralOrder
    var result = std.ArrayList(i32).init(allocator); // 把 std.ArrayList(i32).init(allocator) 存入 结果
    if (matrix.len == 0 or matrix[0].len == 0) return result; // 若 矩阵.长度 等于 0 or 矩阵[0].长度 等于 0，直接返回 结果
    var top: isize = 0; // 把 0; 写入 var top: isize
    var bottom: isize = @intCast(matrix.len - 1); // 把 @intCast(矩阵.长度 减 1); 写入 var bottom: isize
    var left: isize = 0; // 把 0; 写入 var left: isize
    var right: isize = @intCast(matrix[0].len - 1); // 把 @intCast(矩阵[0].长度 减 1); 写入 var right: isize
    while (top <= bottom and left <= right) { // 循环，直到不满足「top 不超过 bottom and 左边界 不超过 右边界」
        var i: isize = left; // 把 左边界; 写入 var i: isize
        while (i <= right) : (i += 1) try result.append(matrix[@intCast(top)][@intCast(i)]);
        top += 1; // top累加 1
        i = top; // 把 top; 写入 下标 i
        while (i <= bottom) : (i += 1) try result.append(matrix[@intCast(i)][@intCast(right)]);
        right -= 1; // 右边界累减 1
        if (top <= bottom) { // 若 top 不超过 bottom
            i = right; // 把 右边界; 写入 下标 i
            while (i >= left) : (i -= 1) try result.append(matrix[@intCast(bottom)][@intCast(i)]);
            bottom -= 1; // bottom累减 1
        }
        if (left <= right) { // 若 左边界 不超过 右边界
            i = bottom; // 把 bottom; 写入 下标 i
            while (i >= top) : (i -= 1) try result.append(matrix[@intCast(i)][@intCast(left)]);
            left += 1; // 左边界累加 1
        }
    }
    return result; // 返回 结果
}

pub fn main() !void { // 程序入口：跑内嵌自测用例
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator); // 把 std.堆.ArenaAllocator.init(std.堆.page_allocator) 存入 arena
    defer arena.deinit(); // defer arena.deinit();
    const allocator = arena.allocator(); // 把 arena.allocator() 存入 allocator

    // 与 TS 事实源内嵌用例一致：空矩阵
    const empty = [_][]const i32{}; // 把 [_][]const i32{} 存入 empty
    const got = try spiralOrder(allocator, &empty); // 把 try spiralOrder(allocator, 按位与 empty) 存入 got
    if (got.items.len != 0) return error.TestFailed; // 若 got.items.长度 不等于 0，直接返回 error.TestFailed
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
