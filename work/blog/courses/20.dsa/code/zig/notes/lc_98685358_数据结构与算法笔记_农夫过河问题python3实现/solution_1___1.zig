// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/98685358
// LeetCode 98685358. 农夫过河问题 — Zig 版（农夫过河问题：BFS 求最短过河序列，状态 (农夫,狼,羊,菜)，0=左岸 1=右岸）
// 状态编码为 4bit：bit3=农夫 bit2=狼 bit1=羊 bit0=菜
const std = @import("std"); // 把 @import(「std」) 存入 std

fn isSafe(s: u4) bool { // 定义判定函数 isSafe
    const farmer: u1 = @truncate(s >> 3); // 把 @truncate(字符串 超过 超过 3); 写入 const farmer: u1
    const wolf: u1 = @truncate(s >> 2); // 把 @truncate(字符串 超过 超过 2); 写入 const wolf: u1
    const goat: u1 = @truncate(s >> 1); // 把 @truncate(字符串 超过 超过 1); 写入 const goat: u1
    const cabbage: u1 = @truncate(s); // 把 @truncate(字符串); 写入 const cabbage: u1
    if (wolf == goat and farmer != wolf) return false; // 若 wolf 等于 goat and farmer 不等于 wolf，直接返回 false
    if (goat == cabbage and farmer != goat) return false; // 若 goat 等于 cabbage and farmer 不等于 goat，直接返回 false
    return true; // 返回 true
}

fn dec(s: u4) [4]i32 { // 定义函数/方法 dec
    return .{ // 返回 {
        @as(i32, @intCast((s >> 3) & 1)),
        @as(i32, @intCast((s >> 2) & 1)),
        @as(i32, @intCast((s >> 1) & 1)),
        @as(i32, @intCast(s & 1)),
    };
}

fn enc(v: [4]i32) u4 { // 定义函数/方法 enc
    return @intCast(v[0] * 8 + v[1] * 4 + v[2] * 2 + v[3]); // 返回 @intCast(值[0] 乘 8 加 值[1] 乘 4 加 值[2] 乘 2 加 值[3])
}

fn solve(path: *[16][4]i32) !usize { // 定义函数/方法 solve
    const start: u4 = 0; // 把 0; 写入 const start: u4
    const goal: u4 = 15; // 把 15; 写入 const goal: u4
    var prev: [16]i8 = undefined; // 把 undefined; 写入 var prev: [16]i8
    for (&prev) |*p| p.* = -2; // -2 未访问, -1 起点
    var q: [16]u4 = undefined; // 把 undefined; 写入 var q: [16]u4
    var head: usize = 0; // 把 0; 写入 var head: usize
    var tail: usize = 0; // 把 0; 写入 var tail: usize
    prev[start] = -1; // 把 减 1; 写入 prev[start]
    q[tail] = start; // 把 起点; 写入 q[tail]
    tail += 1; // 尾节点累加 1
    while (head < tail) { // 循环，直到不满足「头节点 小于 尾节点」
        const cur = q[head]; // 把 节点[头节点] 存入 当前值
        head += 1; // 头节点累加 1
        if (cur == goal) { // 若 当前值 等于 goal
            var n: usize = 0; // 把 0; 写入 var n: usize
            var tmp: [16]u4 = undefined; // 把 undefined; 写入 var tmp: [16]u4
            var k: i16 = cur; // 把 当前值; 写入 var k: i16
            while (k != -1) { // 循环，直到不满足「下标 k 不等于 减 1」
                tmp[n] = @intCast(k); // 把 @intCast(下标 k); 写入 tmp[n]
                n += 1; // 元素个数累加 1
                k = prev[@intCast(k)]; // 把 前一个[@intCast(下标 k)]; 写入 下标 k
            }
            var i: usize = 0; // 把 0; 写入 var i: usize
            while (i < n) : (i += 1) { // 循环，直到不满足「下标 i 小于 元素个数) : (下标 i 累加 1」
                path[i] = dec(tmp[n - 1 - i]); // 把 dec(临时变量[元素个数 减 1 减 下标 i]); 写入 path[i]
            }
            return n; // 返回 元素个数
        }
        const farmer: i32 = @intCast((cur >> 3) & 1); // 把 @intCast((当前值 超过 超过 3) 按位与 1); 写入 const farmer: i32
        var i: usize = 0; // 把 0; 写入 var i: usize
        while (i < 4) : (i += 1) { // 循环，直到不满足「下标 i 小于 4) : (下标 i 累加 1」
            const bit: i32 = @intCast((cur >> @intCast(3 - i)) & 1);
            if (i != 0 and bit != farmer) continue; // 若 下标 i 不等于 0 and bit 不等于 farmer) continue;
            var v = dec(cur); // 把 dec(当前值) 存入 值
            v[0] = 1 - farmer; // 把 1 减 farmer; 写入 v[0]
            if (i != 0) v[i] = 1 - farmer; // 若 下标 i 不等于 0) 值[下标 i] 赋值为 1 减 farmer;
            const nk = enc(v); // 把 enc(值) 存入 nk
            if (prev[nk] != -2) continue; // 若 前一个[nk] 不等于 减 2) continue;
            if (!isSafe(nk)) continue; // 若 取反 isSafe(nk)) continue;
            prev[nk] = @intCast(cur); // 把 @intCast(当前值); 写入 prev[nk]
            q[tail] = nk; // 把 nk; 写入 q[tail]
            tail += 1; // 尾节点累加 1
        }
    }
    return error.NoSolution; // 返回 error.NoSolution
}

pub fn main() !void { // 程序入口：跑内嵌自测用例
    const want = [8][4]i32{ // 把 [8][4]i32{ 存入 want
        .{ 0, 0, 0, 0 }, .{ 1, 0, 1, 0 }, .{ 0, 0, 1, 0 }, .{ 1, 1, 1, 0 },
        .{ 0, 1, 0, 0 }, .{ 1, 1, 0, 1 }, .{ 0, 1, 0, 1 }, .{ 1, 1, 1, 1 },
    };
    var path: [16][4]i32 = undefined; // 把 undefined; 写入 var path: [16][4]i32
    const n = solve(&path) catch { // 把 solve( 按位与 当前路径) catch { 存入 元素个数
        std.debug.print("FAILED: 无解\n", .{}); // 打印输出
        return error.NoSolution; // 返回 error.NoSolution
    };
    if (n != 8) { // 若 元素个数 不等于 8
        std.debug.print("FAILED: path length {d}\n", .{n}); // 打印输出
        return error.TestFailed; // 返回 error.TestFailed
    }
    for (want, 0..) |row, i| { // for (want, 0..) 按位或 row, 下标 i 按位或 {
        for (row, 0..) |x, j| { // for (row, 0..) 按位或 x, 下标 j 按位或 {
            if (path[i][j] != x) { // 若 当前路径[下标 i][下标 j] 不等于 x
                std.debug.print("FAILED: mismatch at {d},{d}\n", .{ i, j }); // 打印输出
                return error.TestFailed; // 返回 error.TestFailed
            }
        }
    }
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
