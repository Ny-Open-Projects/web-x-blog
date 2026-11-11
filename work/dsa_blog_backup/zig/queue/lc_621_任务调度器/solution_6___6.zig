// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130482987
// LeetCode 621. 任务调度器 — Zig 版
const std = @import("std"); // 把 @import(「std」) 存入 std

// 方案6（公式法另一写法：Counter 值列表 + count(freq)）
// Zig 无内建哈希表：先 26 桶计数，再收集为值数组 list，等价 Counter 值列表
fn leastInterval(tasks: []const []const u8, n: i32) i32 { // 定义函数/方法 leastInterval
    var cnt = [_]i32{0} ** 26; // 把 [_]i32{0} 乘 乘 26 存入 计数
    for (tasks) |t| { // 逐个取出 tasks 的元素（另一字符串）
        cnt[t[0] - 'A'] += 1; // 把 1; 写入 cnt[t[0] - 'A'] +
    }
    var list: [26]i32 = undefined; // 把 undefined; 写入 var list: [26]i32
    var list_len: usize = 0; // 把 0; 写入 var list_len: usize
    for (cnt) |v| { // 逐个取出 计数 的元素（值）
        if (v > 0) { // 若 值 超过 0
            list[list_len] = v; // 把 值; 写入 list[list_len]
            list_len += 1; // list_len累加 1
        }
    }
    var freq: i32 = 0; // 把 0; 写入 var freq: i32
    for (list[0..list_len]) |v| { // for (列表[0..list_len]) 按位或 值 按位或 {
        if (v > freq) freq = v; // 若 值 超过 频次表) 频次表 赋值为 值;
    }
    var same: i32 = 0; // 把 0; 写入 var same: i32
    for (list[0..list_len]) |v| { // for (列表[0..list_len]) 按位或 值 按位或 {
        if (v == freq) same += 1; // 若 值 等于 频次表) same 累加 1;
    }
    const total: i32 = @intCast(tasks.len); // 把 @intCast(tasks.长度); 写入 const total: i32
    return @max((freq - 1) * (n + 1) + same, total); // 返回 @取较大值 (频次表 减 1) 乘 (元素个数 加 1) 加 same, 总和)
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
