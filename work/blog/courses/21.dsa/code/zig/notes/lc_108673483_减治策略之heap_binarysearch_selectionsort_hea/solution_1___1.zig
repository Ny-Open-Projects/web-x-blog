// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/108673483
// LeetCode 108673483. 减治策略 — Zig 版（方案1：二分查找）
const std = @import("std"); // 把 @import(「std」) 存入 std

fn binarySearch(arr: []const i32, target: i32) i32 { // 定义函数/方法 binarySearch
    var left: usize = 0; // 把 0; 写入 var left: usize
    var right: usize = arr.len; // 把 数组.长度; 写入 var right: usize
    while (left < right) { // 循环，直到不满足「左边界 小于 右边界」
        const mid = left + (right - left) / 2; // 把 左边界 加 (右边界 减 左边界) 除以 2 存入 中点
        if (arr[mid] == target) return @intCast(mid); // 若 数组[中点] 等于 目标值，直接返回 @intCast(中点)
        if (arr[mid] < target) left = mid + 1 else right = mid; // 若 数组[中点] 小于 目标值) 左边界 赋值为 中点 加 1 else 右边界 赋值为 中点;
    }
    return -1; // 返回 减 1
}

pub fn main() !void { // 程序入口：跑内嵌自测用例
    const a = [_]i32{ 1, 3, 5, 7, 9 }; // 把 [_]i32{ 1, 3, 5, 7, 9 } 存入 数组
    const empty = [_]i32{}; // 把 [_]i32{} 存入 empty
    const Case = struct { arr: []const i32, t: i32, want: i32 }; // 把 struct { 数组: []const i32, 另一字符串: i32, want: i32 } 存入 Case
    const cases = [_]Case{ // 把 [_]Case{ 存入 cases
        .{ .arr = &a, .t = 5, .want = 2 },
        .{ .arr = &a, .t = 4, .want = -1 },
        .{ .arr = &empty, .t = 5, .want = -1 },
        .{ .arr = &a, .t = 1, .want = 0 },
    };
    for (cases, 0..) |c, idx| { // for (cases, 0..) 按位或 字符, idx 按位或 {
        const got = binarySearch(c.arr, c.t); // 把 binarySearch(字符.数组, 字符.另一字符串) 存入 got
        if (got != c.want) { // 若 got 不等于 字符.want
            std.debug.print("case {d} failed: got {d} want {d}\n", .{ idx, got, c.want }); // 打印输出
            return error.TestFailed; // 返回 error.TestFailed
        }
    }
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
