// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107524703
// LeetCode 107524703. 人鬼渡河问题 — Zig 版（方案2：DFS+奇偶步求解）
const std = @import("std"); // 把 @import(「std」) 存入 std

const D = [5][2]i32{ .{ 2, 0 }, .{ 1, 0 }, .{ 1, 1 }, .{ 0, 1 }, .{ 0, 2 } };

fn safe(r: i32, g: i32) bool { // 定义函数/方法 safe
    return 0 <= r and r <= 3 and 0 <= g and g <= 3 and (r == 0 or r == 3 or r == g);
}

var path_buf: [32][2]i32 = undefined; // 把 undefined; 写入 var path_buf: [32][2]i32
var path_len: usize = 0; // 把 0; 写入 var path_len: usize
var visited: [4][4][2]bool = undefined; // 把 undefined; 写入 var visited: [4][4][2]bool

fn dfs(r: i32, g: i32, step: i32) bool { // 定义函数/方法 dfs
    if (r == 0 and g == 0) return true; // 若 右指针 等于 0 and g 等于 0，直接返回 true
    const parity: usize = @intCast(@mod(step, 2)); // 把 @intCast(@mod(步数, 2)); 写入 const parity: usize
    const ru: usize = @intCast(r); // 把 @intCast(右指针); 写入 const ru: usize
    const gu: usize = @intCast(g); // 把 @intCast(g); 写入 const gu: usize
    if (visited[ru][gu][parity]) return false; // 若 已访问集合[ru][gu][parity]，直接返回 false
    visited[ru][gu][parity] = true; // 把 true; 写入 visited[ru][gu][parity]
    const odd = @mod(step, 2) == 1; // 把 @mod(步数, 2) 等于 1 存入 odd
    for (D) |d| { // 逐个取出 D 的元素（d）
        const dr = d[0]; // 把 d[0] 存入 dr
        const dg = d[1]; // 把 d[1] 存入 dg
        var nr: i32 = undefined; // 把 undefined; 写入 var nr: i32
        var ng: i32 = undefined; // 把 undefined; 写入 var ng: i32
        var skip = false; // 把 false 存入 skip
        if (odd) { // 若 odd
            if (r < dr or g < dg) { // 若 右指针 小于 dr or g 小于 dg
                skip = true; // 把 true; 写入 skip
            } else { // 否则
                nr = r - dr; // 把 右指针 减 dr; 写入 nr
                ng = g - dg; // 把 g 减 dg; 写入 ng
            }
        } else { // 否则
            if ((3 - r) < dr or (3 - g) < dg) { // 若 (3 减 右指针) 小于 dr or (3 减 g) 小于 dg
                skip = true; // 把 true; 写入 skip
            } else { // 否则
                nr = r + dr; // 把 右指针 加 dr; 写入 nr
                ng = g + dg; // 把 g 加 dg; 写入 ng
            }
        }
        if (skip) continue; // 若 skip) continue;
        if (!safe(nr, ng)) continue; // 若 取反 safe(nr, ng)) continue;
        if (dfs(nr, ng, step + 1)) { // 若 dfs(nr, ng, 步数 加 1
            path_buf[path_len][0] = dr; // 把 dr; 写入 path_buf[path_len][0]
            path_buf[path_len][1] = dg; // 把 dg; 写入 path_buf[path_len][1]
            path_len += 1; // path_len累加 1
            return true; // 返回 true
        }
    }
    return false; // 返回 false
}

pub fn main() !void { // 程序入口：跑内嵌自测用例
    const want = [11][2]i32{ // 把 [11][2]i32{ 存入 want
        .{ 1, 1 }, .{ 1, 0 }, .{ 0, 2 }, .{ 0, 1 }, .{ 2, 0 },
        .{ 1, 1 }, .{ 2, 0 }, .{ 0, 1 }, .{ 0, 2 }, .{ 1, 0 },
        .{ 1, 1 },
    };
    for (&visited) |*plane| { // for ( 按位与 已访问集合) 按位或 乘 plane 按位或 {
        for (plane) |*row| { // for (plane) 按位或 乘 row 按位或 {
            for (row) |*cell| cell.* = false; // 把 false; 写入 for (row) |*cell| cell.*
        }
    }
    _ = dfs(3, 3, 1); // 把 dfs(3, 3, 1); 写入 _
    if (path_len != 11) { // 若 path_len 不等于 11
        std.debug.print("solve length mismatch: {d}\n", .{path_len}); // 打印输出
        return error.TestFailed; // 返回 error.TestFailed
    }
    for (want, 0..) |w, i| { // for (want, 0..) 按位或 权重, 下标 i 按位或 {
        if (path_buf[10 - i][0] != w[0] or path_buf[10 - i][1] != w[1]) {
            std.debug.print("solve at {d} mismatch\n", .{i}); // 打印输出
            return error.TestFailed; // 返回 error.TestFailed
        }
    }
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
