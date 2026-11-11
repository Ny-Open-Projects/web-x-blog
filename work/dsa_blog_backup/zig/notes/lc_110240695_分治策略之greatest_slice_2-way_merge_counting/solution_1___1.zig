// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/110240695
// LeetCode 110240695. 分治策略之 greatest slice — Zig 版（方案A：暴力枚举所有子段）
const std = @import("std"); // 把 @import(「std」) 存入 std

fn maxSubArrayBf(arr: []const i32) i64 { // 定义函数/方法 maxSubArrayBf
    var best: i64 = std.math.minInt(i64); // 把 std.math.minInt(i64); 写入 var best: i64
    for (0..arr.len) |i| { // 逐个取出 0..数组.长度 的元素（下标 i）
        var s: i64 = 0; // 把 0; 写入 var s: i64
        for (i..arr.len) |j| { // 逐个取出 下标 i..数组.长度 的元素（下标 j）
            s += arr[j]; // 字符串累加 数组[下标 j]
            if (s > best) best = s; // 若 字符串 超过 当前最优) 当前最优 赋值为 字符串;
        }
    }
    return best; // 返回 当前最优
}

pub fn main() !void { // 程序入口：跑内嵌自测用例
    const a0 = [_]i32{ -2, 1, -3, 4, -1, 2, 1, -5, 4 }; // 把 [_]i32{ 减 2, 1, 减 3, 4, 减 1, 2, 1, 减 5, 4 } 存入 a0
    const a1 = [_]i32{1}; // 把 [_]i32{1} 存入 a1
    const a2 = [_]i32{ -1, -2, -3 }; // 把 [_]i32{ 减 1, 减 2, 减 3 } 存入 a2
    const a3 = [_]i32{ 5, 4, -1, 7, 8 }; // 把 [_]i32{ 5, 4, 减 1, 7, 8 } 存入 a3
    const Case = struct { arr: []const i32, want: i64 }; // 把 struct { 数组: []const i32, want: i64 } 存入 Case
    const cases = [_]Case{ // 把 [_]Case{ 存入 cases
        .{ .arr = &a0, .want = 6 },
        .{ .arr = &a1, .want = 1 },
        .{ .arr = &a2, .want = -1 },
        .{ .arr = &a3, .want = 23 },
    };
    for (cases, 0..) |c, idx| { // for (cases, 0..) 按位或 字符, idx 按位或 {
        if (maxSubArrayBf(c.arr) != c.want) { // 若 maxSubArrayBf(字符.数组) 不等于 字符.want
            std.debug.print("case {d} failed\n", .{idx}); // 打印输出
            return error.TestFailed; // 返回 error.TestFailed
        }
    }
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
