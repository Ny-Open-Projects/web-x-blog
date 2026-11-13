// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/104107934
// LeetCode 104107934. 滑动验证码识别 — Zig 版（方案6：合成滑块数据 buildSynthetic）
const std = @import("std"); // 把 @import(「std」) 存入 std

fn buildSynthetic(bg: []i32, puzzle: []i32, gap_start: usize, puzzle_len: usize) void { // 定义函数/方法 buildSynthetic
    for (bg) |*v| v.* = 10; // 把 10; 写入 for (bg) |*v| v.*
    var i = gap_start; // 把 gap_start 存入 下标 i
    while (i < @min(gap_start + puzzle_len, bg.len)) : (i += 1) {
        bg[i] = 200; // 把 200; 写入 bg[i]
    }
    for (0..puzzle_len) |k| { // 让 下标 k 从 0 走到 puzzle_len 减一
        puzzle[k] = bg[gap_start + k]; // 把 bg[gap_start 加 下标 k]; 写入 puzzle[k]
    }
}

pub fn main() !void { // 程序入口：跑内嵌自测用例
    var bg: [8]i32 = undefined; // 把 undefined; 写入 var bg: [8]i32
    var puzzle: [4]i32 = undefined; // 把 undefined; 写入 var puzzle: [4]i32
    buildSynthetic(&bg, &puzzle, 3, 4); // buildSynthetic( 按位与 bg, 按位与 puzzle, 3, 4);
    const want_bg = [_]i32{ 10, 10, 10, 200, 200, 200, 200, 10 }; // 把 [_]i32{ 10, 10, 10, 200, 200, 200, 200, 10 } 存入 want_bg
    const want_pz = [_]i32{ 200, 200, 200, 200 }; // 把 [_]i32{ 200, 200, 200, 200 } 存入 want_pz
    for (want_bg, 0..) |w, i| { // for (want_bg, 0..) 按位或 权重, 下标 i 按位或 {
        if (bg[i] != w) return error.TestFailed; // 若 bg[下标 i] 不等于 权重，直接返回 error.TestFailed
    }
    for (want_pz, 0..) |w, i| { // for (want_pz, 0..) 按位或 权重, 下标 i 按位或 {
        if (puzzle[i] != w) return error.TestFailed; // 若 puzzle[下标 i] 不等于 权重，直接返回 error.TestFailed
    }
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
