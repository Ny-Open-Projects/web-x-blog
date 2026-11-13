// 来源：https://blog.csdn.net/tyro_java/article/details/107490876
// LeetCode 107490876. 分书和八皇后问题 — Zig 版（方案4：八皇后显式栈迭代）
const std = @import("std"); // 把 @import(「std」) 存入 std

fn valid(x: i32, a: []const i32) bool { // 定义函数/方法 valid
    const y: i32 = @intCast(a.len + 1); // 把 @intCast(数组.长度 加 1); 写入 const y: i32
    for (a, 1..) |prev, i| { // for (数组, 1..) 按位或 前一个, 下标 i 按位或 {
        const ii: i32 = @intCast(i); // 把 @intCast(下标 i); 写入 const ii: i32
        if (x == prev or @abs(y - ii) == @abs(x - prev)) return false; // 若 x 等于 前一个 or @取绝对值 y 减 ii) 等于 @取绝对值 x 减 前一个)，直接返回 false
    }
    return true; // 返回 true
}

fn runCase(n: usize, sols: *[100][8]i32) usize { // 定义函数/方法 runCase
    var stack: [8192][9]i32 = undefined; // 把 undefined; 写入 var stack: [8192][9]i32
    var slen: [8192]usize = undefined; // 把 undefined; 写入 var slen: [8192]usize
    var top: usize = 0; // 把 0; 写入 var top: usize
    slen[top] = 0; // 把 0; 写入 slen[top]
    top += 1; // top累加 1
    var sol_count: usize = 0; // 把 0; 写入 var sol_count: usize
    while (top > 0) { // 循环，直到不满足「top 超过 0」
        top -= 1; // top累减 1
        const a = stack[top]; // 把 栈[top] 存入 数组
        const alen = slen[top]; // 把 slen[top] 存入 alen
        if (alen == n) { // 若 alen 等于 元素个数
            var j: usize = 0; // 把 0; 写入 var j: usize
            while (j < n) : (j += 1) sols[sol_count][j] = a[j];
            sol_count += 1; // sol_count累加 1
        } else { // 否则
            var i: usize = 1; // 把 1; 写入 var i: usize
            while (i <= n) : (i += 1) { // 循环，直到不满足「下标 i 不超过 元素个数) : (下标 i 累加 1」
                if (valid(@intCast(i), a[0..alen])) { // 若 valid(@intCast(下标 i), 数组[0..alen]
                    var j: usize = 0; // 把 0; 写入 var j: usize
                    while (j < alen) : (j += 1) stack[top][j] = a[j];
                    stack[top][alen] = @intCast(i); // 把 @intCast(下标 i); 写入 stack[top][alen]
                    slen[top] = alen + 1; // 把 alen 加 1; 写入 slen[top]
                    top += 1; // top累加 1
                }
            }
        }
    }
    return sol_count; // 返回 sol_count
}

pub fn main() !void { // 程序入口：跑内嵌自测用例
    var sols: [100][8]i32 = undefined; // 把 undefined; 写入 var sols: [100][8]i32
    const Case = struct { n: usize, count: usize, first: ?[8]i32, flen: usize };
    const cases = [_]Case{ // 把 [_]Case{ 存入 cases
        .{ .n = 8, .count = 92, .first = .{ 8, 4, 1, 3, 6, 2, 7, 5 }, .flen = 8 },
        .{ .n = 1, .count = 1, .first = .{ 1, 0, 0, 0, 0, 0, 0, 0 }, .flen = 1 },
        .{ .n = 2, .count = 0, .first = null, .flen = 0 },
        .{ .n = 4, .count = 2, .first = .{ 3, 1, 4, 2, 0, 0, 0, 0 }, .flen = 4 },
    };
    for (cases, 0..) |c, idx| { // for (cases, 0..) 按位或 字符, idx 按位或 {
        const count = runCase(c.n, &sols); // 把 runCase(字符.元素个数, 按位与 sols) 存入 计数
        if (count != c.count) { // 若 计数 不等于 字符.计数
            std.debug.print("case {d} count {d}\n", .{ idx, count }); // 打印输出
            return error.TestFailed; // 返回 error.TestFailed
        }
        if (c.first) |f| { // 若 字符.first) 按位或 f 按位或
            var j: usize = 0; // 把 0; 写入 var j: usize
            while (j < c.flen) : (j += 1) { // 循环，直到不满足「下标 j 小于 字符.flen) : (下标 j 累加 1」
                if (sols[0][j] != f[j]) return error.TestFailed; // 若 sols[0][下标 j] 不等于 f[下标 j]，直接返回 error.TestFailed
            }
        }
    }
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
