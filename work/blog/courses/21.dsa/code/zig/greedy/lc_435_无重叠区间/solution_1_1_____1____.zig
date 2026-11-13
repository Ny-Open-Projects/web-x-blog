// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135941089
// LeetCode 435. 无重叠区间 — Zig 版（方案1）
const std = @import("std"); // 把 @import(「std」) 存入 std
const IV = struct { s: i32, e: i32 }; // 把 struct { 字符串: i32, e: i32 } 存入 IV
fn eraseOverlapIntervals(intervals: []const [2]i32) i32 { // 定义函数/方法 eraseOverlapIntervals
    if (intervals.len == 0) return 0; // 若 intervals.长度 等于 0，直接返回 0
    var arr: [256]IV = undefined; // 把 undefined; 写入 var arr: [256]IV
    for (intervals, 0..) |iv, i| arr[i] = .{ .s = iv[0], .e = iv[1] };
    const S = struct { // 把 struct { 存入 S
        fn lt(_: void, a: IV, b: IV) bool {
            return a.e < b.e;
        } // 定义函数/方法 lt
    };
    std.sort.pdq(IV, arr[0..intervals.len], {}, S.lt); // std.sort.pdq(IV, 数组[0..intervals.长度], {}, S.lt);
    var count: i32 = 1; // 把 1; 写入 var count: i32
    var end: i32 = arr[0].e; // 把 数组[0].e; 写入 var end: i32
    for (1..intervals.len) |i| { // 逐个取出 1..intervals.长度 的元素（下标 i）
        if (arr[i].s >= end) {
            count += 1;
            end = arr[i].e;
        } // 若 数组[下标 i].字符串 不低于 终点) { 计数 累加 1; 终点 赋值为 数组[下标 i].e; }
    }
    return @as(i32, @intCast(intervals.len)) - count; // 返回 @as(i32, @intCast(intervals.长度)) 减 计数
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    if (eraseOverlapIntervals(&[_][2]i32{ .{ 1, 2 }, .{ 2, 3 }, .{ 3, 4 }, .{ 1, 3 } }) != 1) return error.TestFailed;
    if (eraseOverlapIntervals(&[_][2]i32{}) != 0) return error.TestFailed;
    if (eraseOverlapIntervals(&[_][2]i32{ .{ 1, 2 }, .{ 1, 2 }, .{ 1, 2 } }) != 2) return error.TestFailed;
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
