// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133970744
// LeetCode 51. N皇后 — Zig 版（方案1）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn solveNQueens(n: usize, alloc: std.mem.Allocator, res: *std.ArrayList(std.ArrayList([]const u8))) void { // 定义函数/方法 solveNQueens
    const D = struct { // 把 struct { 存入 D
        fn dfs(nn: usize, row: usize, cols: []i32, out: *std.ArrayList(std.ArrayList([]const u8)), a: std.mem.Allocator) void { // 定义函数/方法 dfs
            if (row == nn) { // 若 row 等于 nn
                var board = std.ArrayList([]const u8).init(out.allocator); // 把 std.ArrayList([]const u8).init(out.allocator) 存入 棋盘
                for (0..nn) |r| { // 让 右指针 从 0 走到 nn 减一
                    var buf = a.alloc(u8, nn) catch unreachable; // 把 数组.alloc(u8, nn) catch unreachable 存入 buf
                    for (0..nn) |c| buf[c] = if (cols[r] == @as(i32, @intCast(c))) 'Q' else '.'; // 让 字符 从 0 走到 nn 减一
                    board.append(buf) catch unreachable; // 把 buf 追加到列表尾部
                }
                out.append(board) catch unreachable; // 把 棋盘 追加到列表尾部
                return; // return;
            }
            for (0..nn) |col| { // 让 col 从 0 走到 nn 减一
                var valid = true; // 把 true 存入 valid
                for (0..row) |r| { // 让 右指针 从 0 走到 row 减一
                    if (cols[r] == @as(i32, @intCast(col))) {
                        valid = false;
                        break;
                    }
                    const dr = @as(i32, @intCast(r)) - @as(i32, @intCast(row)); // 把 @as(i32, @intCast(右指针)) 减 @as(i32, @intCast(row)) 存入 dr
                    const dc = cols[r] - @as(i32, @intCast(col)); // 把 列数[右指针] 减 @as(i32, @intCast(col)) 存入 dc
                    if (dr * dr == dc * dc) {
                        valid = false;
                        break;
                    } // 若 dr 乘 dr 等于 dc 乘 dc) { valid 赋值为 false; break; }
                }
                if (valid) { // 若 valid
                    cols[row] = @intCast(col); // 把 @intCast(col); 写入 cols[row]
                    dfs(nn, row + 1, cols, out, a); // dfs(nn, row 加 1, 列数, out, 数组);
                }
            }
        }
    };
    const cols = alloc.alloc(i32, n) catch unreachable; // 把 alloc.alloc(i32, 元素个数) catch unreachable 存入 列数
    @memset(cols, -1); // @memset(列数, 减 1);
    D.dfs(n, 0, cols, res, alloc); // D.dfs(元素个数, 0, 列数, 结果, alloc);
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator); // 把 std.堆.ArenaAllocator.init(std.堆.page_allocator) 存入 arena
    defer arena.deinit(); // defer arena.deinit();
    const alloc = arena.allocator(); // 把 arena.allocator() 存入 alloc
    var res = std.ArrayList(std.ArrayList([]const u8)).init(std.heap.page_allocator);
    defer res.deinit(); // defer 结果.deinit();
    solveNQueens(4, alloc, &res); // solveNQueens(4, alloc, 按位与 结果);
    if (res.items.len != 2) return error.TestFailed; // 若 结果.items.长度 不等于 2，直接返回 error.TestFailed
    if (!std.mem.eql(u8, res.items[0].items[0], ".Q..")) return error.TestFailed;
    if (!std.mem.eql(u8, res.items[0].items[3], "..Q.")) return error.TestFailed;
    res.clearRetainingCapacity(); // 结果.clearRetainingCapacity();
    solveNQueens(1, alloc, &res); // solveNQueens(1, alloc, 按位与 结果);
    if (res.items.len != 1) return error.TestFailed; // 若 结果.items.长度 不等于 1，直接返回 error.TestFailed
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
