// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130482987
// LeetCode 621. 任务调度器 — Zig 版
const std = @import("std"); // 把 @import(「std」) 存入 std

// 方案4（26 位频率桶公式法）
fn leastInterval(tasks: []const []const u8, n: i32) i32 { // 定义函数/方法 leastInterval
    var freq = [_]i32{0} ** 26; // 把 [_]i32{0} 乘 乘 26 存入 频次表
    for (tasks) |t| { // 逐个取出 tasks 的元素（另一字符串）
        freq[t[0] - 'A'] += 1; // 把 1; 写入 freq[t[0] - 'A'] +
    }
    var max_freq: i32 = 0; // 把 0; 写入 var max_freq: i32
    for (freq) |f| { // 逐个取出 频次表 的元素（f）
        if (f > max_freq) max_freq = f; // 若 f 超过 max_freq) max_freq 赋值为 f;
    }
    var same: i32 = 0; // 把 0; 写入 var same: i32
    for (freq) |f| { // 逐个取出 频次表 的元素（f）
        if (f == max_freq) same += 1; // 若 f 等于 max_freq) same 累加 1;
    }
    const total: i32 = @intCast(tasks.len); // 把 @intCast(tasks.长度); 写入 const total: i32
    return @max((max_freq - 1) * (n + 1) + same, total); // 返回 @取较大值 (max_freq 减 1) 乘 (元素个数 加 1) 加 same, 总和)
}

pub fn main() !void { // 程序入口：跑内嵌自测用例
    // 与 TS 事实源内嵌用例一致
    const Case = struct { tasks: []const []const u8, n: i32, want: i32 };
    const cases = [_]Case{ // 把 [_]Case{ 存入 cases
        .{ .tasks = &.{ "A", "A", "A", "B", "B", "B" }, .n = 2, .want = 8 },
        .{ .tasks = &.{ "A", "A", "A", "A" }, .n = 2, .want = 10 },
        .{ .tasks = &.{ "A", "B", "C", "D" }, .n = 0, .want = 4 },
    };
    for (cases, 0..) |c, i| { // for (cases, 0..) 按位或 字符, 下标 i 按位或 {
        const got = leastInterval(c.tasks, c.n); // 把 leastInterval(字符.tasks, 字符.元素个数) 存入 got
        if (got != c.want) { // 若 got 不等于 字符.want
            std.debug.print("FAIL case {d} got {d} want {d}\n", .{ i, got, c.want }); // 打印输出
            return error.TestFailed; // 返回 error.TestFailed
        }
    }
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
