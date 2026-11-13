// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/112548608
// LeetCode 112548608. 计算思维之经典农夫过河问题C++实现（DFS 求任一可行过河序列）
// 状态编码 4bit：bit3=农夫 bit2=狼(W) bit1=羊(S) bit0=菜(V)
const std = @import("std"); // 把 @import(「std」) 存入 std

fn invalid(s: u4) bool { // 定义函数/方法 invalid
    const h: u1 = @truncate(s >> 3); // 把 @truncate(字符串 超过 超过 3); 写入 const h: u1
    const w: u1 = @truncate(s >> 2); // 把 @truncate(字符串 超过 超过 2); 写入 const w: u1
    const sg: u1 = @truncate(s >> 1); // 把 @truncate(字符串 超过 超过 1); 写入 const sg: u1
    const v: u1 = @truncate(s); // 把 @truncate(字符串); 写入 const v: u1
    if (h != sg and sg == w) return true; // 若 h 不等于 sg and sg 等于 权重，直接返回 true
    if (h != sg and sg == v) return true; // 若 h 不等于 sg and sg 等于 值，直接返回 true
    return false; // 返回 false
}

var path_buf: [16]u8 = undefined; // 把 undefined; 写入 var path_buf: [16]u8
var path_len: usize = 0; // 把 0; 写入 var path_len: usize
var visited: [16]bool = undefined; // 把 undefined; 写入 var visited: [16]bool

fn go(st: u4) bool { // 定义函数/方法 go
    if (st == 15) return true; // 若 st 等于 15，直接返回 true
    if (visited[st]) return false; // 若 已访问集合[st]，直接返回 false
    visited[st] = true; // 把 true; 写入 visited[st]
    const roles = [4]u8{ '-', 'W', 'S', 'V' }; // 把 [4]u8{ ' 减 ', 'W', 'S', 'V' } 存入 roles
    var ri: usize = 0; // 把 0; 写入 var ri: usize
    while (ri < 4) : (ri += 1) { // 循环，直到不满足「ri 小于 4) : (ri 累加 1」
        const shift: u2 = if (ri == 0) 0 else @intCast(3 - ri); // W->2 S->1 V->0
        var ns: u4 = st ^ 8; // 农夫总是过河
        if (ri != 0) { // 若 ri 不等于 0
            if ((st >> 3 & 1) != (st >> shift & 1)) continue; // 出发前同岸
            ns = ns ^ (@as(u4, 1) << shift); // 把 ns 按位异或 (@as(u4, 1) 小于 小于 shift); 写入 ns
        }
        if (invalid(ns)) continue; // 若 invalid(ns)) continue;
        if (go(ns)) { // 若 go(ns
            path_buf[path_len] = roles[ri]; // 把 roles[ri]; 写入 path_buf[path_len]
            path_len += 1; // path_len累加 1
            return true; // 返回 true
        }
    }
    return false; // 返回 false
}

fn simulate(p: []const u8) bool { // 定义函数/方法 simulate
    var st: u4 = 0; // 把 0; 写入 var st: u4
    var i: usize = p.len; // 把 节点.长度; 写入 var i: usize
    while (i > 0) { // path 逆序存放，模拟按正序走
        i -= 1; // 下标 i累减 1
        const role = p[i]; // 把 节点[下标 i] 存入 role
        const before = st; // 把 st 存入 before
        st = st ^ 8; // 把 st 按位异或 8; 写入 st
        if (role != '-') { // 若 role 不等于 ' 减 '
            const shift: u2 = if (role == 'W') 2 else if (role == 'S') 1 else 0;
            if ((before >> 3 & 1) != (before >> shift & 1)) return false;
            st = st ^ (@as(u4, 1) << shift); // 把 st 按位异或 (@as(u4, 1) 小于 小于 shift); 写入 st
        }
        if (invalid(st)) return false; // 若 invalid(st)，直接返回 false
    }
    return st == 15; // 返回 st 等于 15
}

pub fn main() !void { // 程序入口：跑内嵌自测用例
    const want_path = [7]u8{ 'S', '-', 'W', 'S', 'V', '-', 'S' };
    const want_readable = "HS H HW HS HV H HS"; // 把 「HS H HW HS HV H HS」 存入 want_readable

    @memset(&visited, false); // @memset( 按位与 已访问集合, false);
    _ = go(0); // 把 go(0); 写入 _

    // case1: 路径一致（path_buf 逆序存放）
    if (path_len != 7) { // 若 path_len 不等于 7
        std.debug.print("FAIL length {d}\n", .{path_len}); // 打印输出
        return error.TestFailed; // 返回 error.TestFailed
    }
    for (want_path, 0..) |w, i| { // for (want_path, 0..) 按位或 权重, 下标 i 按位或 {
        if (path_buf[6 - i] != w) { // 若 path_buf[6 减 下标 i] 不等于 权重
            std.debug.print("FAIL path[{d}] got {c} want {c}\n", .{ i, path_buf[6 - i], w }); // 打印输出
            return error.TestFailed; // 返回 error.TestFailed
        }
    }

    // case2: 可读方案串
    var buf: [64]u8 = undefined; // 把 undefined; 写入 var buf: [64]u8
    var n: usize = 0; // 把 0; 写入 var n: usize
    for (0..7) |i| { // 让 下标 i 从 0 走到 7 减一
        const role = path_buf[6 - i]; // 把 path_buf[6 减 下标 i] 存入 role
        if (i != 0) { // 若 下标 i 不等于 0
            buf[n] = ' '; // 把 ' '; 写入 buf[n]
            n += 1; // 元素个数累加 1
        }
        buf[n] = 'H'; // 把 'H'; 写入 buf[n]
        n += 1; // 元素个数累加 1
        if (role != '-') { // 若 role 不等于 ' 减 '
            buf[n] = role; // 把 role; 写入 buf[n]
            n += 1; // 元素个数累加 1
        }
    }
    const got_readable = buf[0..n]; // 把 buf[0..元素个数] 存入 got_readable
    if (!std.mem.eql(u8, got_readable, want_readable)) { // 若 取反 std.mem.eql(u8, got_readable, want_readable
        std.debug.print("FAIL readable: {s}\n", .{got_readable}); // 打印输出
        return error.TestFailed; // 返回 error.TestFailed
    }

    // case3 + case4
    if (!simulate(path_buf[0..path_len])) { // 若 取反 simulate(path_buf[0..path_len]
        std.debug.print("FAIL simulate\n", .{}); // 打印输出
        return error.TestFailed; // 返回 error.TestFailed
    }

    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
