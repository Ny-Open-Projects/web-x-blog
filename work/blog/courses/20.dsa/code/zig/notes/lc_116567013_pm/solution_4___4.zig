// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/116567013
// LeetCode 116567013. PM — Zig 版（方案4：buildNext 单测）
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

pub fn main() !void { // 程序入口：跑内嵌自测用例
    var buf: [64]i64 = undefined; // 把 undefined; 写入 var buf: [64]i64
    buildNext("ababaca", &buf); // buildNext(「ababaca」, 按位与 buf);
    const w1 = [_]i64{ -1, 0, 0, 1, 2, 3, 0 }; // 把 [_]i64{ 减 1, 0, 0, 1, 2, 3, 0 } 存入 w1
    if (!std.mem.eql(i64, buf[0..7], &w1)) return error.TestFailed;
    buildNext("aaaa", &buf); // buildNext(「aaaa」, 按位与 buf);
    const w2 = [_]i64{ -1, 0, 1, 2 }; // 把 [_]i64{ 减 1, 0, 1, 2 } 存入 w2
    if (!std.mem.eql(i64, buf[0..4], &w2)) return error.TestFailed;
    buildNext("abcabc", &buf); // buildNext(「abcabc」, 按位与 buf);
    const w5 = [_]i64{ -1, 0, 0, 0, 1, 2 }; // 把 [_]i64{ 减 1, 0, 0, 0, 1, 2 } 存入 w5
    if (!std.mem.eql(i64, buf[0..6], &w5)) return error.TestFailed;
    buildNext("abcd", &buf); // buildNext(「abcd」, 按位与 buf);
    const w3 = [_]i64{ -1, 0, 0, 0 }; // 把 [_]i64{ 减 1, 0, 0, 0 } 存入 w3
    if (!std.mem.eql(i64, buf[0..4], &w3)) return error.TestFailed;
    buildNext("a", &buf); // buildNext(「数组」, 按位与 buf);
    const w4 = [_]i64{-1}; // 把 [_]i64{ 减 1} 存入 w4
    if (!std.mem.eql(i64, buf[0..1], &w4)) return error.TestFailed;
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
