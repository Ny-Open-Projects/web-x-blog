// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134859412
// LeetCode 1494. 并行课程II — Zig 版（方案2）
const std = @import("std"); // 把 @import(「std」) 存入 std
var nG: usize = 0; // 把 0; 写入 var nG: usize
var kG: usize = 0; // 把 0; 写入 var kG: usize
var prereqG: [16]i32 = undefined; // 把 undefined; 写入 var prereqG: [16]i32
fn go(done: i32) i32 { // 定义函数/方法 go
    if (done == (@as(i32, 1) << @intCast(nG)) - 1) return 0; // 若 done 等于 (@as(i32, 1) 小于 小于 @intCast(nG)) 减 1，直接返回 0
    var avail: i32 = 0; // 把 0; 写入 var avail: i32
    for (0..nG) |i| { // 让 下标 i 从 0 走到 nG 减一
        const bit = @as(i32, 1) << @intCast(i); // 把 @as(i32, 1) 小于 小于 @intCast(下标 i) 存入 bit
        if ((done & bit) == 0 and (done & prereqG[i]) == prereqG[i]) avail |= bit;
    }
    var cnt: usize = 0; // 把 0; 写入 var cnt: usize
    var chosen: i32 = 0; // 把 0; 写入 var chosen: i32
    var a = avail; // 把 avail 存入 数组
    while (a != 0 and cnt < kG) { // 循环，直到不满足「数组 不等于 0 and 计数 小于 kG」
        const low = a & (-a); // 把 数组 按位与 ( 减 数组) 存入 low
        chosen |= low; // 把 low; 写入 chosen |
        a ^= low; // 把 low; 写入 a ^
        cnt += 1; // 计数累加 1
    }
    return 1 + go(done | chosen); // 返回 1 加 go(done 按位或 chosen)
}
fn minNumberOfSemesters(n: usize, relations: []const [2]i32, k: usize) i32 { // 定义函数/方法 minNumberOfSemesters
    nG = n; // 把 元素个数; 写入 nG
    kG = k; // 把 下标 k; 写入 kG
    for (0..n) |i| prereqG[i] = 0; // 让 下标 i 从 0 走到 元素个数 减一
    for (relations) |r| prereqG[@intCast(r[1] - 1)] |= @as(i32, 1) << @intCast(r[0] - 1); // 逐个取出 relations 的元素（右指针）
    return go(0); // 返回 go(0)
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    const r1 = [_][2]i32{ .{ 2, 1 }, .{ 3, 1 }, .{ 1, 4 } }; // 把 [_][2]i32{ .{ 2, 1 }, .{ 3, 1 }, .{ 1, 4 } } 存入 r1
    if (minNumberOfSemesters(4, &r1, 2) != 3) return error.TestFailed;
    const r2 = [_][2]i32{ .{ 2, 1 }, .{ 3, 1 }, .{ 4, 1 }, .{ 1, 5 } };
    if (minNumberOfSemesters(5, &r2, 3) != 3) return error.TestFailed;
    const r0 = [_][2]i32{}; // 把 [_][2]i32{} 存入 r0
    if (minNumberOfSemesters(3, &r0, 2) != 2) return error.TestFailed;
    const r4 = [_][2]i32{ .{ 1, 2 }, .{ 2, 3 } }; // 把 [_][2]i32{ .{ 1, 2 }, .{ 2, 3 } } 存入 r4
    if (minNumberOfSemesters(4, &r4, 1) != 4) return error.TestFailed;
    std.debug.print("PASS\n", .{});
} // 全部用例通过，输出 PASS
