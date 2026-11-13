// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/108673483
// LeetCode 108673483. 减治策略 — Zig 版（方案3：Boyer-Moore 摩尔投票求多数元素）
const std = @import("std"); // 把 @import(「std」) 存入 std

fn majorityElement(arr: []const i32) i32 { // 定义函数/方法 majorityElement
    var candidate: i32 = 0; // 把 0; 写入 var candidate: i32
    var count: i32 = 0; // 把 0; 写入 var count: i32
    for (arr) |num| { // 逐个取出 数组 的元素（num）
        if (count == 0) { // 若 计数 等于 0
            candidate = num; // 把 num; 写入 candidate
        }
        if (num == candidate) { // 若 num 等于 candidate
            count += 1; // 计数累加 1
        } else { // 否则
            count -= 1; // 计数累减 1
        }
    }
    var cnt: i32 = 0; // 把 0; 写入 var cnt: i32
    for (arr) |num| { // 逐个取出 数组 的元素（num）
        if (num == candidate) cnt += 1; // 若 num 等于 candidate) 计数 累加 1;
    }
    if (cnt > @divTrunc(@as(i32, @intCast(arr.len)), 2)) return candidate;
    return -1; // 返回 减 1
}

pub fn main() !void { // 程序入口：跑内嵌自测用例
    const Case = struct { arr: []const i32, want: i32 }; // 把 struct { 数组: []const i32, want: i32 } 存入 Case
    const cases = [_]Case{ // 把 [_]Case{ 存入 cases
        .{ .arr = &[_]i32{ 2, 2, 1, 1, 1, 1, 1 }, .want = 1 },
        .{ .arr = &[_]i32{ 1, 2, 3 }, .want = -1 },
        .{ .arr = &[_]i32{ 3, 3, 4 }, .want = 3 },
    };
    for (cases, 0..) |c, idx| { // for (cases, 0..) 按位或 字符, idx 按位或 {
        const got = majorityElement(c.arr); // 把 majorityElement(字符.数组) 存入 got
        if (got != c.want) { // 若 got 不等于 字符.want
            std.debug.print("case {d} failed: got {d} want {d}\n", .{ idx, got, c.want }); // 打印输出
            return error.TestFailed; // 返回 error.TestFailed
        }
    }
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
