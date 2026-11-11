// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/116567013
// LeetCode 116567013. PM — Zig 版（方案2：Brute-Force 双循环对齐）
const std = @import("std"); // 把 @import(「std」) 存入 std

fn matchV2(p: []const u8, t: []const u8) i64 { // 定义函数/方法 matchV2
    const n = t.len; // 把 另一字符串.长度 存入 元素个数
    const m = p.len; // 把 节点.长度 存入 映射表
    if (m == 0 or n < m) return -1; // 若 映射表 等于 0 or 元素个数 小于 映射表，直接返回 减 1
    var i: usize = 0; // 把 0; 写入 var i: usize
    while (i <= n - m) : (i += 1) { // 循环，直到不满足「下标 i 不超过 元素个数 减 映射表) : (下标 i 累加 1」
        var j: usize = 0; // 把 0; 写入 var j: usize
        while (j < m and t[i + j] == p[j]) : (j += 1) {}
        if (j == m) return @intCast(i); // 若 下标 j 等于 映射表，直接返回 @intCast(下标 i)
    }
    return -1; // 返回 减 1
}

pub fn main() !void { // 程序入口：跑内嵌自测用例
    const T = "now is the time for all good people to come"; // 把 「now is the time for all good people to come」 存入 T
    const Case = struct { p: []const u8, t: []const u8, want: i64 };
    const cases = [_]Case{ // 把 [_]Case{ 存入 cases
        .{ .p = "people", .t = T, .want = 29 },
        .{ .p = "time", .t = T, .want = 11 },
        .{ .p = "all", .t = T, .want = 20 },
        .{ .p = "xyz", .t = T, .want = -1 },
        .{ .p = "a", .t = "", .want = -1 },
        .{ .p = "is", .t = T, .want = 4 },
    };
    for (cases, 0..) |c, idx| { // for (cases, 0..) 按位或 字符, idx 按位或 {
        const got = matchV2(c.p, c.t); // 把 matchV2(字符.节点, 字符.另一字符串) 存入 got
        if (got != c.want) { // 若 got 不等于 字符.want
            std.debug.print("case {d} failed\n", .{idx}); // 打印输出
            return error.TestFailed; // 返回 error.TestFailed
        }
    }
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
