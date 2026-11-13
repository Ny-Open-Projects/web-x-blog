// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135949307
// LeetCode 452. 用最少数量的箭引爆气球 — Zig 版（方案2）
const std = @import("std"); // 把 @import(「std」) 存入 std
const IV = struct { s: i32, e: i32 }; // 把 struct { 字符串: i32, e: i32 } 存入 IV
fn findMinArrowShots(points: []const [2]i32) i32 { // 定义函数/方法 findMinArrowShots
    if (points.len == 0) return 0; // 若 points.长度 等于 0，直接返回 0
    var arr: [256]IV = undefined; // 把 undefined; 写入 var arr: [256]IV
    for (points, 0..) |p, i| arr[i] = .{ .s = p[0], .e = p[1] };
    const S = struct { // 把 struct { 存入 S
        fn lt(_: void, a: IV, b: IV) bool {
            return a.e < b.e;
        } // 定义函数/方法 lt
    };
    std.sort.pdq(IV, arr[0..points.len], {}, S.lt); // std.sort.pdq(IV, 数组[0..points.长度], {}, S.lt);
    var arrows: i32 = 1; // 把 1; 写入 var arrows: i32
    var end: i32 = arr[0].e; // 把 数组[0].e; 写入 var end: i32
    for (1..points.len) |k| { // 逐个取出 1..points.长度 的元素（下标 k）
        if (arr[k].s > end) {
            arrows += 1;
            end = arr[k].e;
        } // 若 数组[下标 k].字符串 超过 终点) { arrows 累加 1; 终点 赋值为 数组[下标 k].e; }
    }
    return arrows; // 返回 arrows
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    if (findMinArrowShots(&[_][2]i32{ .{ 10, 16 }, .{ 2, 8 }, .{ 1, 6 }, .{ 7, 12 } }) != 2) return error.TestFailed;
    if (findMinArrowShots(&[_][2]i32{}) != 0) return error.TestFailed;
    if (findMinArrowShots(&[_][2]i32{ .{ 1, 2 }, .{ 3, 4 }, .{ 5, 6 }, .{ 7, 8 } }) != 4) return error.TestFailed;
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
