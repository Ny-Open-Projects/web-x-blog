// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145381786
// LeetCode 1329. 将矩阵按对角线排序 — Zig 版
const std = @import("std"); // 把 @import(「std」) 存入 std

// 方案2：优化版 —— 与 TS 事实源一致：按 r-c 分组收集对角线，升序排序，按原顺序写回（shift 取最小值）。
// Zig 无内建哈希表，按对角线编号 d = r-c 从 -(cols-1) 到 rows-1 逐条收集。
fn diagonalSort(allocator: std.mem.Allocator, mat: [][]i32) !void { // 定义函数/方法 diagonalSort
    const rows = mat.len; // 把 mat.长度 存入 行数
    const cols = mat[0].len; // 把 mat[0].长度 存入 列数
    const ris: isize = @intCast(rows); // 把 @intCast(行数); 写入 const ris: isize
    const cis: isize = @intCast(cols); // 把 @intCast(列数); 写入 const cis: isize
    var buf = try std.ArrayList(i32).initCapacity(allocator, rows + cols);
    defer buf.deinit(); // defer buf.deinit();
    const dmin = -(@as(isize, @intCast(cols)) - 1); // 把 减 (@as(isize, @intCast(列数)) 减 1) 存入 dmin
    const dmax = @as(isize, @intCast(rows)) - 1; // 把 @as(isize, @intCast(行数)) 减 1 存入 dmax
    var d: isize = dmin; // 把 dmin; 写入 var d: isize
    while (d <= dmax) : (d += 1) { // 循环，直到不满足「d 不超过 dmax) : (d 累加 1」
        buf.clearRetainingCapacity(); // buf.clearRetainingCapacity();
        const r0: isize = if (d > 0) d else 0; // 把 if (d 超过 0) d else 0; 写入 const r0: isize
        var r = r0; // 把 r0 存入 右指针
        while (r < ris) : (r += 1) { // 循环，直到不满足「右指针 小于 ris) : (右指针 累加 1」
            const c = r - d; // 把 右指针 减 d 存入 字符
            if (c < 0 or c >= cis) continue; // 若 字符 小于 0 or 字符 不低于 cis) continue;
            try buf.append(mat[@intCast(r)][@intCast(c)]); // 把 mat[@intCast(右指针 追加到列表尾部
        }
        std.sort.block(i32, buf.items, {}, std.sort.asc(i32)); // std.sort.block(i32, buf.items, {}, std.sort.asc(i32));
        var k: usize = 0; // 把 0; 写入 var k: usize
        r = r0; // 把 r0; 写入 右指针
        while (r < ris) : (r += 1) { // 循环，直到不满足「右指针 小于 ris) : (右指针 累加 1」
            const c = r - d; // 把 右指针 减 d 存入 字符
            if (c < 0 or c >= cis) continue; // 若 字符 小于 0 or 字符 不低于 cis) continue;
            mat[@intCast(r)][@intCast(c)] = buf.items[k]; // 把 buf.items[下标 k]; 写入 mat[@intCast(r)][@intCast(c)]
            k += 1; // 下标 k累加 1
        }
    }
}

fn matFromRows(allocator: std.mem.Allocator, rows: []const []const i32) ![][]i32 { // 定义函数/方法 matFromRows
    const m = try allocator.alloc([]i32, rows.len); // 把 try allocator.alloc([]i32, 行数.长度) 存入 映射表
    for (rows, 0..) |row, i| { // for (行数, 0..) 按位或 row, 下标 i 按位或 {
        m[i] = try allocator.dupe(i32, row); // 把 try allocator.dupe(i32, row); 写入 m[i]
    }
    return m; // 返回 映射表
}

fn eqMatrix(a: []const []i32, b: []const []const i32) bool { // 定义函数/方法 eqMatrix
    if (a.len != b.len) return false; // 若 数组.长度 不等于 b.长度，直接返回 false
    for (a, 0..) |row, i| { // for (数组, 0..) 按位或 row, 下标 i 按位或 {
        if (row.len != b[i].len) return false; // 若 row.长度 不等于 b[下标 i].长度，直接返回 false
        for (row, 0..) |v, j| { // for (row, 0..) 按位或 值, 下标 j 按位或 {
            if (v != b[i][j]) return false; // 若 值 不等于 b[下标 i][下标 j]，直接返回 false
        }
    }
    return true; // 返回 true
}

pub fn main() !void { // 程序入口：跑内嵌自测用例
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator); // 把 std.堆.ArenaAllocator.init(std.堆.page_allocator) 存入 arena
    defer arena.deinit(); // defer arena.deinit();
    const allocator = arena.allocator(); // 把 arena.allocator() 存入 allocator

    // 与 TS 事实源内嵌用例一致（输入深拷贝后排序，等价于 m.map(r => r.slice())）
    const src = [_][]const i32{ &.{ 3, 3, 1, 1 }, &.{ 2, 2, 1, 2 }, &.{ 1, 1, 1, 2 } };
    const exp = [_][]const i32{ &.{ 1, 1, 1, 1 }, &.{ 1, 2, 2, 2 }, &.{ 1, 2, 3, 3 } };
    const mat = try matFromRows(allocator, &src); // 把 try matFromRows(allocator, 按位与 src) 存入 mat
    try diagonalSort(allocator, mat); // try diagonalSort(allocator, mat);
    if (!eqMatrix(mat, &exp)) return error.TestFailed; // 若 取反 eqMatrix(mat, 按位与 exp)，直接返回 error.TestFailed
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
