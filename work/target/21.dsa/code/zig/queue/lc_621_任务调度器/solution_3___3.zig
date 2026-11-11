// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130482987
// LeetCode 621. 任务调度器 — Zig 版
const std = @import("std"); // 把 @import(「std」) 存入 std

// 方案3（贪心模拟，每轮取剩余次数最多的 n+1 个，最后一轮只计实际执行数）
fn leastInterval(tasks: []const []const u8, n: i32) i32 { // 定义函数/方法 leastInterval
    var count = [_]i32{0} ** 26; // 把 [_]i32{0} 乘 乘 26 存入 计数
    for (tasks) |t| { // 逐个取出 tasks 的元素（另一字符串）
        count[t[0] - 'A'] += 1; // 把 1; 写入 count[t[0] - 'A'] +
    }
    var cnt: [27]i32 = undefined; // 把 undefined; 写入 var cnt: [27]i32
    var cnt_len: usize = 0; // 把 0; 写入 var cnt_len: usize
    for (count) |v| { // 逐个取出 计数 的元素（值）
        if (v > 0) { // 若 值 超过 0
            cnt[cnt_len] = v; // 把 值; 写入 cnt[cnt_len]
            cnt_len += 1; // cnt_len累加 1
        }
    }
    var time: i32 = 0; // 把 0; 写入 var time: i32
    while (cnt_len > 0) { // 循环，直到不满足「cnt_len 超过 0」
        std.mem.sort(i32, cnt[0..cnt_len], {}, std.sort.desc(i32)); // 排序
        var used: i32 = 0; // 把 0; 写入 var used: i32
        const take: usize = @intCast(@min(n + 1, @as(i32, @intCast(cnt_len))));
        var i: usize = 0; // 把 0; 写入 var i: usize
        while (i < take) : (i += 1) { // 循环，直到不满足「下标 i 小于 take) : (下标 i 累加 1」
            if (cnt[i] > 0) { // 若 计数[下标 i] 超过 0
                cnt[i] -= 1; // cnt[i]累减 1
                used += 1; // 已用标记累加 1
            }
        }
        var new_len: usize = 0; // 把 0; 写入 var new_len: usize
        for (cnt[0..cnt_len]) |v| { // for (计数[0..cnt_len]) 按位或 值 按位或 {
            if (v > 0) { // 若 值 超过 0
                cnt[new_len] = v; // 把 值; 写入 cnt[new_len]
                new_len += 1; // new_len累加 1
            }
        }
        cnt_len = new_len; // 把 new_len; 写入 cnt_len
        time += if (cnt_len > 0) n + 1 else used; // time累加 if (cnt_len 超过 0) 元素个数 加 1 else 已用标记
    }
    return time; // 返回 time
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
