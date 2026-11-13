// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107524703
// LeetCode 107524703. 人鬼渡河问题 — Zig 版（方案4：方向入状态的 DFS 变体，断言无可行路径）
const std = @import("std"); // 把 @import(「std」) 存入 std

const D = [5][2]i32{ .{ 2, 0 }, .{ 1, 0 }, .{ 1, 1 }, .{ 0, 1 }, .{ 0, 2 } };

fn safe(r: i32, g: i32) bool { // 定义函数/方法 safe
    return 0 <= r and r <= 3 and 0 <= g and g <= 3 and (r == 0 or r == 3 or r == g);
}

var path_len: usize = 0; // 把 0; 写入 var path_len: usize
var visited: [4][4][2]bool = undefined; // 把 undefined; 写入 var visited: [4][4][2]bool

fn jump(dir: i32, r: i32, g: i32, step: i32) bool { // 定义函数/方法 jump
    if (r == 0 and g == 0 and @mod(step, 2) == 0) return true; // 若 右指针 等于 0 and g 等于 0 and @mod(步数, 2) 等于 0，直接返回 true
    const parity: usize = @intCast(@mod(step, 2)); // 把 @intCast(@mod(步数, 2)); 写入 const parity: usize
    const ru: usize = @intCast(r); // 把 @intCast(右指针); 写入 const ru: usize
    const gu: usize = @intCast(g); // 把 @intCast(g); 写入 const gu: usize
    if (visited[ru][gu][parity]) return false; // 若 已访问集合[ru][gu][parity]，直接返回 false
    visited[ru][gu][parity] = true; // 把 true; 写入 visited[ru][gu][parity]
    for (D) |d| { // 逐个取出 D 的元素（d）
        const nr = r + dir * d[0]; // 把 右指针 加 dir 乘 d[0] 存入 nr
        const ng = g + dir * d[1]; // 把 g 加 dir 乘 d[1] 存入 ng
        if (!safe(nr, ng)) continue; // 若 取反 safe(nr, ng)) continue;
        if (jump(-dir, nr, ng, step + 1)) { // 若 jump( 减 dir, nr, ng, 步数 加 1
            path_len += 1; // path_len累加 1
            return true; // 返回 true
        }
    }
    return false; // 返回 false
}

pub fn main() !void { // 程序入口：跑内嵌自测用例
    for (&visited) |*plane| { // for ( 按位与 已访问集合) 按位或 乘 plane 按位或 {
        for (plane) |*row| { // for (plane) 按位或 乘 row 按位或 {
            for (row) |*cell| cell.* = false; // 把 false; 写入 for (row) |*cell| cell.*
        }
    }
    _ = jump(-1, 3, 3, 0); // 把 jump( 减 1, 3, 3, 0); 写入 _
    // 与 TS 原文件一致：该变体断言返回空路径（parity 约束下无解）
    if (path_len != 0) { // 若 path_len 不等于 0
        std.debug.print("FAIL: got {d} moves\n", .{path_len}); // 打印输出
        return error.TestFailed; // 返回 error.TestFailed
    }
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
