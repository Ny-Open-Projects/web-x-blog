// 来源：https://blog.csdn.net/tyro_java/article/details/107490876
// LeetCode 107490876. 分书和八皇后问题 — Zig 版（方案1：分书，共享 assigned + 回溯）
const std = @import("std"); // 把 @import(「std」) 存入 std

const LIKE = [5][5]i32{ // 把 [5][5]i32{ 存入 LIKE
    .{ 0, 0, 1, 1, 0 },
    .{ 1, 1, 0, 0, 1 },
    .{ 0, 1, 1, 0, 1 },
    .{ 0, 0, 0, 1, 0 },
    .{ 0, 1, 0, 0, 1 },
};

var assigned: [5]i32 = undefined; // 把 undefined; 写入 var assigned: [5]i32
var results: [16][5]i32 = undefined; // 把 undefined; 写入 var results: [16][5]i32
var result_count: usize = 0; // 把 0; 写入 var result_count: usize

fn tryAssign(reader: usize) void { // 定义函数/方法 tryAssign
    if (reader == 5) { // 若 reader 等于 5
        results[result_count] = assigned; // 把 assigned; 写入 results[result_count]
        result_count += 1; // result_count累加 1
        return; // return;
    }
    var book: usize = 0; // 把 0; 写入 var book: usize
    while (book < 5) : (book += 1) { // 循环，直到不满足「book 小于 5) : (book 累加 1」
        if (LIKE[reader][book] == 1 and assigned[book] == -1) { // 若 LIKE[reader][book] 等于 1 and assigned[book] 等于 减 1
            assigned[book] = @intCast(reader); // 把 @intCast(reader); 写入 assigned[book]
            tryAssign(reader + 1); // tryAssign(reader 加 1);
            assigned[book] = -1; // 回溯
        }
    }
}

pub fn main() !void { // 程序入口：跑内嵌自测用例
    const want = [2][5]i32{ .{ 1, 2, 0, 3, 4 }, .{ 1, 4, 0, 3, 2 } };
    assigned = .{ -1, -1, -1, -1, -1 }; // 把 { 减 1, 减 1, 减 1, 减 1, 减 1 }; 写入 assigned
    tryAssign(0); // tryAssign(0);
    if (result_count != 2) { // 若 result_count 不等于 2
        std.debug.print("count mismatch {d}\n", .{result_count}); // 打印输出
        return error.TestFailed; // 返回 error.TestFailed
    }
    for (want, 0..) |w, i| { // for (want, 0..) 按位或 权重, 下标 i 按位或 {
        for (w, 0..) |x, j| { // for (权重, 0..) 按位或 x, 下标 j 按位或 {
            if (results[i][j] != x) { // 若 results[下标 i][下标 j] 不等于 x
                std.debug.print("scheme {d} mismatch\n", .{i}); // 打印输出
                return error.TestFailed; // 返回 error.TestFailed
            }
        }
    }
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
