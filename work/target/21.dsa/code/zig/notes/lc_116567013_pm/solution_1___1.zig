// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/116567013
// LeetCode 116567013. PM — Zig 版（方案1：Brute-Force 主串指针回退）
const std = @import("std"); // 把 @import(「std」) 存入 std

fn matchV1(p: []const u8, t: []const u8) i64 { // 定义函数/方法 matchV1
    const n = t.len; // 把 另一字符串.长度 存入 元素个数
    const m = p.len; // 把 节点.长度 存入 映射表
    var i: usize = 0; // 把 0; 写入 var i: usize
    var j: usize = 0; // 把 0; 写入 var j: usize
    while (j < m and i < n) { // 循环，直到不满足「下标 j 小于 映射表 and 下标 i 小于 元素个数」
        if (t[i] == p[j]) { // 若 另一字符串[下标 i] 等于 节点[下标 j]
            i += 1; // 下标 i累加 1
            j += 1; // 下标 j累加 1
        } else { // 否则
            i = i + 1 - j; // 主串回退到本次对齐的下一位置
            j = 0; // 把 0; 写入 下标 j
        }
    }
    if (j == m) return @intCast(i - j); // 若 下标 j 等于 映射表，直接返回 @intCast(下标 i 减 下标 j)
    return -1; // 返回 减 1
}

pub fn main() !void { // 程序入口：跑内嵌自测用例
    const T = "now is the time for all good people to come"; // 把 「now is the time for all good people to come」 存入 T
    const Case = struct { p: []const u8, t: []const u8, want: i64 };
    const cases = [_]Case{ // 把 [_]Case{ 存入 cases
        .{ .p = "people", .t = T, .want = 29 },
        .{ .p = "good", .t = T, .want = 24 },
        .{ .p = "xyz", .t = T, .want = -1 },
        .{ .p = "a", .t = "", .want = -1 },
        .{ .p = "is", .t = T, .want = 4 },
    };
    for (cases, 0..) |c, idx| { // for (cases, 0..) 按位或 字符, idx 按位或 {
        const got = matchV1(c.p, c.t); // 把 matchV1(字符.节点, 字符.另一字符串) 存入 got
        if (got != c.want) { // 若 got 不等于 字符.want
            std.debug.print("case {d} failed: matchV1({s})={d} want {d}\n", .{ idx, c.p, got, c.want }); // 打印输出
            return error.TestFailed; // 返回 error.TestFailed
        }
    }
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
