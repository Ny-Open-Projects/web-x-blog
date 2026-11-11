// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/104107934
// LeetCode 104107934. 滑动验证码识别 — Zig 版（方案4：SAD 绝对差和最佳窗口）
const std = @import("std"); // 把 @import(「std」) 存入 std

fn bestMatchWindow(bg: []const i32, puzzle: []const i32) struct { x: usize, score: i64 } { // 定义函数/方法 bestMatchWindow
    var best_x: usize = 0; // 把 0; 写入 var best_x: usize
    var best_score: i64 = std.math.maxInt(i64); // 把 std.math.maxInt(i64); 写入 var best_score: i64
    const n = puzzle.len; // 把 puzzle.长度 存入 元素个数
    var x: usize = 0; // 把 0; 写入 var x: usize
    while (x + n <= bg.len) : (x += 1) { // 循环，直到不满足「x 加 元素个数 不超过 bg.长度) : (x 累加 1」
        var score: i64 = 0; // 把 0; 写入 var score: i64
        for (0..n) |y| { // 让 y 从 0 走到 元素个数 减一
            score += @abs(bg[x + y] - puzzle[y]); // score累加 @取绝对值 bg[x 加 y] 减 puzzle[y])
        }
        if (score < best_score) { // 若 score 小于 best_score
            best_score = score; // 把 score; 写入 best_score
            best_x = x; // 把 x; 写入 best_x
        }
    }
    return .{ .x = best_x, .score = best_score }; // 返回 { .x 赋值为 best_x, .score 赋值为 best_score }
}

pub fn main() !void { // 程序入口：跑内嵌自测用例
    const bg = [_]i32{ 10, 10, 10, 10, 200, 200, 200, 200 }; // 把 [_]i32{ 10, 10, 10, 10, 200, 200, 200, 200 } 存入 bg
    const puzzle = [_]i32{ 10, 200, 200, 200 }; // 把 [_]i32{ 10, 200, 200, 200 } 存入 puzzle
    const r = bestMatchWindow(&bg, &puzzle); // 把 bestMatchWindow( 按位与 bg, 按位与 puzzle) 存入 右指针
    if (r.x != 3 or r.score != 0) return error.TestFailed; // 若 右指针.x 不等于 3 or 右指针.score 不等于 0，直接返回 error.TestFailed
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
