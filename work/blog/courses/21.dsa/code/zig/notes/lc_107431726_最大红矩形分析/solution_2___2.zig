// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107431726
// LeetCode 107431726. 最大红矩形分析 — Zig 版（方案A：逐行高度 + 暴力区间 / 卡片扩展）
const std = @import("std"); // 把 @import(「std」) 存入 std

fn getResult(n: usize, m: usize, matrix: []const []const u8) i64 { // 定义函数/方法 getResult
    var ans: i64 = 0; // 把 0; 写入 var ans: i64
    var height: [66]i64 = undefined; // 把 undefined; 写入 var height: [66]i64
    for (&height) |*h| h.* = 0; // 把 0; 写入 for (&height) |*h| h.*
    for (0..n) |k| { // 让 下标 k 从 0 走到 元素个数 减一
        var i: usize = 1; // 把 1; 写入 var i: usize
        while (i <= m) : (i += 1) { // 循环，直到不满足「下标 i 不超过 映射表) : (下标 i 累加 1」
            if (matrix[k][i - 1] == '.') { // 若 矩阵[下标 k][下标 i 减 1] 等于 '.'
                height[i] += 1; // height[i]累加 1
            } else { // 否则
                height[i] = 0; // 把 0; 写入 height[i]
            }
        }
        var a: usize = 1; // 把 1; 写入 var a: usize
        while (a <= m) : (a += 1) { // 循环，直到不满足「数组 不超过 映射表) : (数组 累加 1」
            var min_h: i64 = 50000; // 把 50000; 写入 var min_h: i64
            var c = a; // 把 数组 存入 字符
            while (c <= m) : (c += 1) { // 循环，直到不满足「字符 不超过 映射表) : (字符 累加 1」
                if (height[c] < min_h) min_h = height[c]; // 若 height[字符] 小于 min_h) min_h 赋值为 height[字符];
            }
            const area = @as(i64, @intCast(m - a + 1)) * min_h; // 把 @as(i64, @intCast(映射表 减 数组 加 1)) 乘 min_h 存入 area
            if (area > ans) ans = area; // 若 area 超过 答案) 答案 赋值为 area;
        }
    }
    return ans; // 返回 答案
}

fn getResultCard(n: usize, m: usize, matrix: []const []const u8) i64 { // 定义函数/方法 getResultCard
    var ans: i64 = 0; // 把 0; 写入 var ans: i64
    var height: [66]i64 = undefined; // 把 undefined; 写入 var height: [66]i64
    for (&height) |*h| h.* = 0; // 把 0; 写入 for (&height) |*h| h.*
    for (0..n) |k| { // 让 下标 k 从 0 走到 元素个数 减一
        var i: usize = 1; // 把 1; 写入 var i: usize
        while (i <= m) : (i += 1) { // 循环，直到不满足「下标 i 不超过 映射表) : (下标 i 累加 1」
            if (matrix[k][i - 1] == '.') { // 若 矩阵[下标 k][下标 i 减 1] 等于 '.'
                height[i] += 1; // height[i]累加 1
            } else { // 否则
                height[i] = 0; // 把 0; 写入 height[i]
            }
        }
        var a: usize = 1; // 把 1; 写入 var a: usize
        while (a <= m) : (a += 1) { // 循环，直到不满足「数组 不超过 映射表) : (数组 累加 1」
            const cur_h = height[a]; // 把 height[数组] 存入 cur_h
            var lo: i64 = @as(i64, @intCast(a)) - 1; // 把 @as(i64, @intCast(数组)) 减 1; 写入 var lo: i64
            while (lo >= 1 and height[@intCast(lo)] >= cur_h) lo -= 1;
            var hi: usize = a + 1; // 把 数组 加 1; 写入 var hi: usize
            while (hi <= m and height[hi] >= cur_h) hi += 1; // 循环，直到不满足「右边界 不超过 映射表 and height[右边界] 不低于 cur_h) 右边界 累加 1;」
            const area = @as(i64, @intCast(hi - @as(usize, @intCast(lo)) - 1)) * cur_h;
            if (area > ans) ans = area; // 若 area 超过 答案) 答案 赋值为 area;
        }
    }
    return ans; // 返回 答案
}

pub fn main() !void { // 程序入口：跑内嵌自测用例
    const matrix = [_][]const u8{ ".....", "XXXXX", ".X...", "....." }; // 把 [_][]const u8{ 「.....」, 「.....」, 「.....」, 「.....」 } 存入 矩阵
    if (getResult(4, 5, &matrix) != 6) return error.TestFailed; // 若 getResult(4, 5, 按位与 矩阵) 不等于 6，直接返回 error.TestFailed
    if (getResultCard(4, 5, &matrix) != 6) return error.TestFailed; // 若 getResultCard(4, 5, 按位与 矩阵) 不等于 6，直接返回 error.TestFailed
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
