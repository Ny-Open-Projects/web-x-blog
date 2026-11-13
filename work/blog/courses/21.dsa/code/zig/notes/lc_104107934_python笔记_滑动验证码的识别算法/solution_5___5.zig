// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/104107934
// LeetCode 104107934. 滑动验证码识别 — Zig 版（方案5：边缘匹配 findGap 响应曲线）
const std = @import("std"); // 把 @import(「std」) 存入 std

fn detectEdges(image: []const i32, edges: []bool) void { // 定义函数/方法 detectEdges
    for (edges) |*e| e.* = false; // 把 false; 写入 for (edges) |*e| e.*
    var i: usize = 1; // 把 1; 写入 var i: usize
    while (i < image.len) : (i += 1) { // 循环，直到不满足「下标 i 小于 image.长度) : (下标 i 累加 1」
        edges[i] = @abs(image[i] - image[i - 1]) > 50; // 把 @取绝对值 image[下标 i] 减 image[下标 i 减 1]) 超过 50; 写入 edges[i]
    }
}

fn findGap(bg: []const i32, puzzle: []const i32, responses: []i64) usize { // 定义函数/方法 findGap
    var bg_edges: [64]bool = undefined; // 把 undefined; 写入 var bg_edges: [64]bool
    var puzzle_edges: [64]bool = undefined; // 把 undefined; 写入 var puzzle_edges: [64]bool
    detectEdges(bg, &bg_edges); // detectEdges(bg, 按位与 bg_edges);
    detectEdges(puzzle, &puzzle_edges); // detectEdges(puzzle, 按位与 puzzle_edges);
    var len: usize = 0; // 把 0; 写入 var len: usize
    var x: usize = 0; // 把 0; 写入 var x: usize
    while (x + puzzle.len <= bg.len) : (x += 1) { // 循环，直到不满足「x 加 puzzle.长度 不超过 bg.长度) : (x 累加 1」
        var score: i64 = 0; // 把 0; 写入 var score: i64
        for (0..puzzle.len) |y| { // 逐个取出 0..puzzle.长度 的元素（y）
            if (bg_edges[x + y] and puzzle_edges[y]) score += 1; // 若 bg_edges[x 加 y] and puzzle_edges[y]) score 累加 1;
        }
        responses[len] = score; // 把 score; 写入 responses[len]
        len += 1; // 长度累加 1
    }
    var best_x: usize = 0; // 把 0; 写入 var best_x: usize
    for (1..len) |i| { // 逐个取出 1..长度 的元素（下标 i）
        if (responses[i] > responses[best_x]) best_x = i; // 若 responses[下标 i] 超过 responses[best_x]) best_x 赋值为 下标 i;
    }
    return best_x; // 返回 best_x
}

pub fn main() !void { // 程序入口：跑内嵌自测用例
    const bg = [_]i32{ 10, 10, 10, 10, 200, 200, 200, 200 }; // 把 [_]i32{ 10, 10, 10, 10, 200, 200, 200, 200 } 存入 bg
    const puzzle = [_]i32{ 10, 200, 200, 200 }; // 把 [_]i32{ 10, 200, 200, 200 } 存入 puzzle
    var responses: [64]i64 = undefined; // 把 undefined; 写入 var responses: [64]i64
    const bx = findGap(&bg, &puzzle, &responses); // 把 findGap( 按位与 bg, 按位与 puzzle, 按位与 responses) 存入 bx
    if (bx != 3) return error.TestFailed; // 若 bx 不等于 3，直接返回 error.TestFailed
    const want = [_]i64{ 0, 0, 0, 1, 0 }; // 把 [_]i64{ 0, 0, 0, 1, 0 } 存入 want
    for (want, 0..) |w, i| { // for (want, 0..) 按位或 权重, 下标 i 按位或 {
        if (responses[i] != w) return error.TestFailed; // 若 responses[下标 i] 不等于 权重，直接返回 error.TestFailed
    }
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
