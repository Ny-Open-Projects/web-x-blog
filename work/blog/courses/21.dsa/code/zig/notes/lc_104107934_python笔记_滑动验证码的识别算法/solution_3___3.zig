// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/104107934
// LeetCode 104107934. 滑动验证码识别 — Zig 版（方案3：NCC 归一化互相关）
const std = @import("std"); // 把 @import(「std」) 存入 std

fn nccMatch(bg: []const i32, puzzle: []const i32) usize { // 定义函数/方法 nccMatch
    var best_x: usize = 0; // 把 0; 写入 var best_x: usize
    var best_score = -std.math.inf(f64); // 把 减 std.math.inf(f64) 存入 best_score
    const n = puzzle.len; // 把 puzzle.长度 存入 元素个数
    var x: usize = 0; // 把 0; 写入 var x: usize
    while (x + n <= bg.len) : (x += 1) { // 循环，直到不满足「x 加 元素个数 不超过 bg.长度) : (x 累加 1」
        var bw: f64 = 0; // 把 0; 写入 var bw: f64
        var pw: f64 = 0; // 把 0; 写入 var pw: f64
        for (0..n) |i| { // 让 下标 i 从 0 走到 元素个数 减一
            bw += @as(f64, @floatFromInt(bg[x + i])); // bw累加 @as(f64, @floatFromInt(bg[x 加 下标 i]))
            pw += @as(f64, @floatFromInt(puzzle[i])); // pw累加 @as(f64, @floatFromInt(puzzle[下标 i]))
        }
        bw /= @floatFromInt(n); // 把 @floatFromInt(元素个数); 写入 bw /
        pw /= @floatFromInt(n); // 把 @floatFromInt(元素个数); 写入 pw /
        var num: f64 = 0; // 把 0; 写入 var num: f64
        var db: f64 = 0; // 把 0; 写入 var db: f64
        var dp: f64 = 0; // 把 0; 写入 var dp: f64
        for (0..n) |i| { // 让 下标 i 从 0 走到 元素个数 减一
            const a = @as(f64, @floatFromInt(bg[x + i])) - bw; // 把 @as(f64, @floatFromInt(bg[x 加 下标 i])) 减 bw 存入 数组
            const b = @as(f64, @floatFromInt(puzzle[i])) - pw; // 把 @as(f64, @floatFromInt(puzzle[下标 i])) 减 pw 存入 b
            num += a * b; // num累加 数组 乘 b
            db += a * a; // db累加 数组 乘 数组
            dp += b * b; // DP 表累加 b 乘 b
        }
        const denom = @sqrt(db) * @sqrt(dp); // 把 @sqrt(db) 乘 @sqrt(DP 表) 存入 denom
        const score = if (denom != 0.0) num / denom else 0.0; // 把 if (denom 不等于 0.0) num 除以 denom else 0.0 存入 score
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
    if (nccMatch(&bg, &puzzle) != 3) return error.TestFailed; // 若 nccMatch( 按位与 bg, 按位与 puzzle) 不等于 3，直接返回 error.TestFailed
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
