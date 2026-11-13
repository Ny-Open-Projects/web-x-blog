// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/116567013
// LeetCode 116567013. PM — Zig 版（方案3：KMP，next 表失配大步跳跃）
const std = @import("std"); // 把 @import(「std」) 存入 std

fn buildNext(p: []const u8, out: []i64) void { // 定义函数/方法 buildNext
    const m = p.len; // 把 节点.长度 存入 映射表
    for (out[0..m]) |*x| x.* = -1; // 把 减 1; 写入 for (out[0..m]) |*x| x.*
    var j: i64 = 0; // 把 0; 写入 var j: i64
    var t: i64 = -1; // 把 减 1; 写入 var t: i64
    while (j < @as(i64, @intCast(m)) - 1) { // 循环，直到不满足「下标 j 小于 @as(i64, @intCast(映射表)) 减 1」
        if (t < 0 or p[@intCast(j)] == p[@intCast(t)]) { // 若 另一字符串 小于 0 or 节点[@intCast(下标 j)] 等于 节点[@intCast(另一字符串)]
            j += 1; // 下标 j累加 1
            t += 1; // 另一字符串累加 1
            out[@intCast(j)] = t; // 把 另一字符串; 写入 out[@intCast(j)]
        } else { // 否则
            t = out[@intCast(t)]; // 把 out[@intCast(另一字符串)]; 写入 另一字符串
        }
    }
}

fn kmpMatch(p: []const u8, t: []const u8, next_buf: []i64) i64 { // 定义函数/方法 kmpMatch
    buildNext(p, next_buf); // buildNext(节点, next_buf);
    const n = t.len; // 把 另一字符串.长度 存入 元素个数
    const m = p.len; // 把 节点.长度 存入 映射表
    var i: i64 = 0; // 把 0; 写入 var i: i64
    var j: i64 = 0; // 把 0; 写入 var j: i64
    while (j < @as(i64, @intCast(m)) and i < @as(i64, @intCast(n))) {
        if (j < 0 or t[@intCast(i)] == p[@intCast(j)]) { // 若 下标 j 小于 0 or 另一字符串[@intCast(下标 i)] 等于 节点[@intCast(下标 j)]
            i += 1; // 下标 i累加 1
            j += 1; // 下标 j累加 1
        } else { // 否则
            j = next_buf[@intCast(j)]; // 把 next_buf[@intCast(下标 j)]; 写入 下标 j
        }
    }
    if (j == @as(i64, @intCast(m))) return i - j; // 若 下标 j 等于 @as(i64, @intCast(映射表))，直接返回 下标 i 减 下标 j
    return -1; // 返回 减 1
}

pub fn main() !void { // 程序入口：跑内嵌自测用例
    var next_buf: [64]i64 = undefined; // 把 undefined; 写入 var next_buf: [64]i64
    const T = "now is the time for all good people to come"; // 把 「now is the time for all good people to come」 存入 T
    const Case = struct { p: []const u8, t: []const u8, want: i64 };
    const cases = [_]Case{ // 把 [_]Case{ 存入 cases
        .{ .p = "people", .t = T, .want = 29 },
        .{ .p = "all", .t = T, .want = 20 },
        .{ .p = "no", .t = T, .want = 0 },
        .{ .p = "xyz", .t = T, .want = -1 },
        .{ .p = "a", .t = "", .want = -1 },
    };
    for (cases, 0..) |c, idx| { // for (cases, 0..) 按位或 字符, idx 按位或 {
        if (kmpMatch(c.p, c.t, &next_buf) != c.want) { // 若 kmpMatch(字符.节点, 字符.另一字符串, 按位与 next_buf) 不等于 字符.want
            std.debug.print("case {d} failed\n", .{idx}); // 打印输出
            return error.TestFailed; // 返回 error.TestFailed
        }
    }
    if (kmpMatch("aaaa", "aaaaa", &next_buf) != 0) return error.TestFailed;
    if (kmpMatch("aaab", "aaabaaa", &next_buf) != 0) return error.TestFailed;

    buildNext("ababaca", &next_buf); // buildNext(「ababaca」, 按位与 next_buf);
    const w1 = [_]i64{ -1, 0, 0, 1, 2, 3, 0 }; // 把 [_]i64{ 减 1, 0, 0, 1, 2, 3, 0 } 存入 w1
    if (!std.mem.eql(i64, next_buf[0..7], &w1)) return error.TestFailed;
    buildNext("aaaa", &next_buf); // buildNext(「aaaa」, 按位与 next_buf);
    const w2 = [_]i64{ -1, 0, 1, 2 }; // 把 [_]i64{ 减 1, 0, 1, 2 } 存入 w2
    if (!std.mem.eql(i64, next_buf[0..4], &w2)) return error.TestFailed;
    buildNext("abcd", &next_buf); // buildNext(「abcd」, 按位与 next_buf);
    const w3 = [_]i64{ -1, 0, 0, 0 }; // 把 [_]i64{ 减 1, 0, 0, 0 } 存入 w3
    if (!std.mem.eql(i64, next_buf[0..4], &w3)) return error.TestFailed;
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
