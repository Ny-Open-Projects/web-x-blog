// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/104107934
// LeetCode 104107934. 滑动验证码识别 — Zig 版（方案2：Sobel 中心差分边缘 + 匹配）
const std = @import("std"); // 把 @import(「std」) 存入 std

fn detectEdgesSobel(image: []const i32, edges: []bool) void { // 定义函数/方法 detectEdgesSobel
    const n = image.len; // 把 image.长度 存入 元素个数
    for (edges) |*e| e.* = false; // 把 false; 写入 for (edges) |*e| e.*
    if (n < 2) return; // 若 元素个数 小于 2) return;
    edges[0] = @abs(image[1] - image[0]) > 50; // 把 @取绝对值 image[1] 减 image[0]) 超过 50; 写入 edges[0]
    var i: usize = 1; // 把 1; 写入 var i: usize
    while (i < n - 1) : (i += 1) { // 循环，直到不满足「下标 i 小于 元素个数 减 1) : (下标 i 累加 1」
        edges[i] = @abs(image[i + 1] - image[i - 1]) > 50;
    }
    edges[n - 1] = @abs(image[n - 1] - image[n - 2]) > 50;
}

fn recognizeCaptcha(bg: []const i32, puzzle: []const i32) usize { // 定义函数/方法 recognizeCaptcha
    var bg_edges: [64]bool = undefined; // 把 undefined; 写入 var bg_edges: [64]bool
    var puzzle_edges: [64]bool = undefined; // 把 undefined; 写入 var puzzle_edges: [64]bool
    detectEdgesSobel(bg, &bg_edges); // detectEdgesSobel(bg, 按位与 bg_edges);
    detectEdgesSobel(puzzle, &puzzle_edges); // detectEdgesSobel(puzzle, 按位与 puzzle_edges);
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
    const bg = [_]i32{ 10, 10, 10, 10, 200, 200, 200, 200 }; // 把 [_]i32{ 10, 10, 10, 10, 200, 200, 200, 200 } 存入 bg
    const puzzle = [_]i32{ 10, 200, 200, 200 }; // 把 [_]i32{ 10, 200, 200, 200 } 存入 puzzle
    if (recognizeCaptcha(&bg, &puzzle) != 3) return error.TestFailed;
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
