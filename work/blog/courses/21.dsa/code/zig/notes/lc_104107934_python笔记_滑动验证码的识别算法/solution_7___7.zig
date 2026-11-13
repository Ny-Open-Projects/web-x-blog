// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/104107934
// LeetCode 104107934. 滑动验证码识别 — Zig 版（方案7：合成数据 + 识别全流程）
const std = @import("std"); // 把 @import(「std」) 存入 std

fn detectEdges(image: []const i32, edges: []bool) void { // 定义函数/方法 detectEdges
    for (edges) |*e| e.* = false; // 把 false; 写入 for (edges) |*e| e.*
    var i: usize = 1; // 把 1; 写入 var i: usize
    while (i < image.len) : (i += 1) { // 循环，直到不满足「下标 i 小于 image.长度) : (下标 i 累加 1」
        edges[i] = @abs(image[i] - image[i - 1]) > 50; // 把 @取绝对值 image[下标 i] 减 image[下标 i 减 1]) 超过 50; 写入 edges[i]
    }
}

fn recognizeCaptcha(bg: []const i32, puzzle: []const i32) usize { // 定义函数/方法 recognizeCaptcha
    var bg_edges: [64]bool = undefined; // 把 undefined; 写入 var bg_edges: [64]bool
    var puzzle_edges: [64]bool = undefined; // 把 undefined; 写入 var puzzle_edges: [64]bool
    detectEdges(bg, &bg_edges); // detectEdges(bg, 按位与 bg_edges);
    detectEdges(puzzle, &puzzle_edges); // detectEdges(puzzle, 按位与 puzzle_edges);
    var best_x: usize = 0; // 把 0; 写入 var best_x: usize
    var best_score: i64 = -1; // 把 减 1; 写入 var best_score: i64
    var x: usize = 0; // 把 0; 写入 var x: usize
    while (x + puzzle.len <= bg.len) : (x += 1) { // 循环，直到不满足「x 加 puzzle.长度 不超过 bg.长度) : (x 累加 1」
        var score: i64 = 0; // 把 0; 写入 var score: i64
        for (0..puzzle.len) |y| { // 逐个取出 0..puzzle.长度 的元素（y）
            if (bg_edges[x + y] and puzzle_edges[y]) score += 1; // 若 bg_edges[x 加 y] and puzzle_edges[y]) score 累加 1;
        }
        if (score > best_score) { // 若 score 超过 best_score
            best_score = score; // 把 score; 写入 best_score
            best_x = x; // 把 x; 写入 best_x
        }
    }
    return best_x; // 返回 best_x
}

pub fn main() !void { // 程序入口：跑内嵌自测用例
    // 合成数据：build_synthetic(8,3,4) → bg[3..6] = 200
    const bg = [_]i32{ 10, 10, 10, 200, 200, 200, 200, 10 }; // 把 [_]i32{ 10, 10, 10, 200, 200, 200, 200, 10 } 存入 bg
    const puzzle = [_]i32{ 200, 200, 200, 200 }; // 把 [_]i32{ 200, 200, 200, 200 } 存入 puzzle
    // 与 TS 原文件一致：合成数据下 puzzle 边缘全平，识别结果为 0
    if (recognizeCaptcha(&bg, &puzzle) != 0) return error.TestFailed;
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
