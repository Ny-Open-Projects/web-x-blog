// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134204437
// LeetCode 79. 单词搜索 — Zig 版（方案1）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn exist(board_in: []const []u8, word: []const u8) bool { // 定义函数/方法 exist
    const board = board_in; // 把 board_in 存入 棋盘
    const rows = board.len; // 把 棋盘.长度 存入 行数
    const cols = board[0].len; // 把 棋盘[0].长度 存入 列数
    const D = struct { // 把 struct { 存入 D
        fn dfs(b: []const []u8, w: []const u8, i: isize, j: isize, k: usize) bool { // 定义函数/方法 dfs
            if (k == w.len) return true; // 若 下标 k 等于 权重.长度，直接返回 true
            if (i < 0 or i >= @as(isize, @intCast(b.len)) or j < 0 or j >= @as(isize, @intCast(b[0].len))) return false;
            const ui: usize = @intCast(i); // 把 @intCast(下标 i); 写入 const ui: usize
            const uj: usize = @intCast(j); // 把 @intCast(下标 j); 写入 const uj: usize
            if (b[ui][uj] != w[k]) return false; // 若 b[ui][uj] 不等于 权重[下标 k]，直接返回 false
            const saved = b[ui][uj]; // 把 b[ui][uj] 存入 saved
            b[ui][uj] = '#'; // 把 '#'; 写入 b[ui][uj]
            const found = dfs(b, w, i + 1, j, k + 1) or dfs(b, w, i - 1, j, k + 1) or dfs(b, w, i, j + 1, k + 1) or dfs(b, w, i, j - 1, k + 1);
            b[ui][uj] = saved; // 把 saved; 写入 b[ui][uj]
            return found; // 返回 found
        }
    };
    for (0..rows) |i| { // 让 下标 i 从 0 走到 行数 减一
        for (0..cols) |j| { // 让 下标 j 从 0 走到 列数 减一
            if (D.dfs(board, word, @intCast(i), @intCast(j), 0)) return true; // 若 D.dfs(棋盘, 单词, @intCast(下标 i), @intCast(下标 j), 0)，直接返回 true
        }
    }
    return false; // 返回 false
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator); // 把 std.堆.ArenaAllocator.init(std.堆.page_allocator) 存入 arena
    defer arena.deinit(); // defer arena.deinit();
    const alloc = arena.allocator(); // 把 arena.allocator() 存入 alloc
    const b0 = alloc.dupe(u8, "ABCE") catch unreachable; // 把 alloc.dupe(u8, 「ABCE」) catch unreachable 存入 b0
    const b1 = alloc.dupe(u8, "SFCS") catch unreachable; // 把 alloc.dupe(u8, 「SFCS」) catch unreachable 存入 b1
    const b2 = alloc.dupe(u8, "ADEE") catch unreachable; // 把 alloc.dupe(u8, 「ADEE」) catch unreachable 存入 b2
    const board = [_][]u8{ b0, b1, b2 }; // 把 [_][]u8{ b0, b1, b2 } 存入 棋盘
    if (!exist(&board, "ABCCED")) return error.TestFailed; // 若 取反 exist( 按位与 棋盘, 「ABCCED」)，直接返回 error.TestFailed
    if (!exist(&board, "SEE")) return error.TestFailed; // 若 取反 exist( 按位与 棋盘, 「SEE」)，直接返回 error.TestFailed
    if (exist(&board, "ABCB")) return error.TestFailed; // 若 exist( 按位与 棋盘, 「ABCB」)，直接返回 error.TestFailed
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
