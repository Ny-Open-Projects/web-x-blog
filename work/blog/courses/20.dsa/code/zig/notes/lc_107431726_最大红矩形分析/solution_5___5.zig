// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107431726
// LeetCode 107431726. 最大红矩形分析 — Zig 版（方案E：逐行高度 + 单调栈）
const std = @import("std"); // 把 @import(「std」) 存入 std

fn maxRedRectangle(matrix: []const []const u8) i64 { // 定义函数/方法 maxRedRectangle
    const n = matrix.len; // 把 矩阵.长度 存入 元素个数
    const m = matrix[0].len; // 把 矩阵[0].长度 存入 映射表
    var ans: i64 = 0; // 把 0; 写入 var ans: i64
    var height: [66]i64 = undefined; // 把 undefined; 写入 var height: [66]i64
    for (&height) |*h| h.* = 0; // 把 0; 写入 for (&height) |*h| h.*
    var stack: [66]usize = undefined; // 把 undefined; 写入 var stack: [66]usize
    for (0..n) |k| { // 让 下标 k 从 0 走到 元素个数 减一
        var i: usize = 1; // 把 1; 写入 var i: usize
        while (i <= m) : (i += 1) { // 循环，直到不满足「下标 i 不超过 映射表) : (下标 i 累加 1」
            if (matrix[k][i - 1] == '.') { // 若 矩阵[下标 k][下标 i 减 1] 等于 '.'
                height[i] += 1; // height[i]累加 1
            } else { // 否则
                height[i] = 0; // 把 0; 写入 height[i]
            }
        }
        var top: usize = 0; // 把 0; 写入 var top: usize
        stack[top] = 0; // 把 0; 写入 stack[top]
        top += 1; // top累加 1
        var idx: usize = 1; // 把 1; 写入 var idx: usize
        while (idx <= m + 1) : (idx += 1) { // 循环，直到不满足「idx 不超过 映射表 加 1) : (idx 累加 1」
            const hi: i64 = if (idx <= m) height[idx] else 0; // 把 if (idx 不超过 映射表) height[idx] else 0; 写入 const hi: i64
            while (height[stack[top - 1]] > hi) { // 循环，直到不满足「height[栈[top 减 1]] 超过 右边界」
                top -= 1; // top累减 1
                const now_h = height[stack[top]]; // 把 height[栈[top]] 存入 now_h
                const width = idx - stack[top - 1] - 1; // 把 idx 减 栈[top 减 1] 减 1 存入 width
                const area = now_h * @as(i64, @intCast(width)); // 把 now_h 乘 @as(i64, @intCast(width)) 存入 area
                if (area > ans) ans = area; // 若 area 超过 答案) 答案 赋值为 area;
            }
            stack[top] = idx; // 把 idx; 写入 stack[top]
            top += 1; // top累加 1
        }
    }
    return ans; // 返回 答案
}

pub fn main() !void { // 程序入口：跑内嵌自测用例
    const matrix = [_][]const u8{ ".....", "XXXXX", ".X...", "....." }; // 把 [_][]const u8{ 「.....」, 「.....」, 「.....」, 「.....」 } 存入 矩阵
    if (maxRedRectangle(&matrix) != 6) return error.TestFailed; // 若 maxRedRectangle( 按位与 矩阵) 不等于 6，直接返回 error.TestFailed
    const m2 = [_][]const u8{ "...", "...", "..." }; // 把 [_][]const u8{ 「...」, 「...」, 「...」 } 存入 m2
    if (maxRedRectangle(&m2) != 9) return error.TestFailed; // 若 maxRedRectangle( 按位与 m2) 不等于 9，直接返回 error.TestFailed
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
