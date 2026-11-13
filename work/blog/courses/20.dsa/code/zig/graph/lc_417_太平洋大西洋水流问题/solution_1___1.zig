// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133982215
// LeetCode 417. 太平洋大西洋水流问题 — Zig 版
const std = @import("std"); // 把 @import(「std」) 存入 std

const MAXD = 8; // 把 8 存入 MAXD

var g_m: usize = 0; // 把 0; 写入 var g_m: usize
var g_n: usize = 0; // 把 0; 写入 var g_n: usize
var g_mat: []const []const i32 = &.{}; // 把 按位与 .{}; 写入 var g_mat: []const []const i32

// 方案1（DFS 反向流动，从海洋边界出发）
fn dfs(r: usize, c: usize, flow: *[MAXD][MAXD]bool) void { // 定义函数/方法 dfs
    flow[r][c] = true; // 把 true; 写入 flow[r][c]
    const dr = [_]isize{ -1, 1, 0, 0 }; // 把 [_]isize{ 减 1, 1, 0, 0 } 存入 dr
    const dc = [_]isize{ 0, 0, -1, 1 }; // 把 [_]isize{ 0, 0, 减 1, 1 } 存入 dc
    var k: usize = 0; // 把 0; 写入 var k: usize
    while (k < 4) : (k += 1) { // 循环，直到不满足「下标 k 小于 4) : (下标 k 累加 1」
        const nr = @as(isize, @intCast(r)) + dr[k]; // 把 @as(isize, @intCast(右指针)) 加 dr[下标 k] 存入 nr
        const nc = @as(isize, @intCast(c)) + dc[k]; // 把 @as(isize, @intCast(字符)) 加 dc[下标 k] 存入 nc
        if (nr >= 0 and nc >= 0) { // 若 nr 不低于 0 and nc 不低于 0
            const ur: usize = @intCast(nr); // 把 @intCast(nr); 写入 const ur: usize
            const uc: usize = @intCast(nc); // 把 @intCast(nc); 写入 const uc: usize
            if (ur < g_m and uc < g_n and !flow[ur][uc] and // 若 ur 小于 g_m and uc 小于 g_n and 取反 flow[ur][uc] and
                g_mat[ur][uc] >= g_mat[r][c]) // 把 g_mat[右指针][字符]) 写入 g_mat[ur][uc] >
            {
                dfs(ur, uc, flow); // dfs(ur, uc, flow);
            }
        }
    }
}

// 返回结果个数，res 按行优先填充 0 基坐标；mat 为 null 时返回 0
fn pacificAtlantic(
    mat: ?[]const []const i32,
    m: usize,
    n: usize,
    res: *[MAXD * MAXD][2]usize,
) usize { // ) usize {
    const matrix = mat orelse return 0; // 把 mat orelse return 0 存入 矩阵
    if (m == 0 or n == 0) return 0; // 若 映射表 等于 0 or 元素个数 等于 0，直接返回 0
    g_m = m; // 把 映射表; 写入 g_m
    g_n = n; // 把 元素个数; 写入 g_n
    g_mat = matrix; // 把 矩阵; 写入 g_mat
    var pacific: [MAXD][MAXD]bool = undefined; // 把 undefined; 写入 var pacific: [MAXD][MAXD]bool
    var atlantic: [MAXD][MAXD]bool = undefined; // 把 undefined; 写入 var atlantic: [MAXD][MAXD]bool
    @memset(&pacific, [1]bool{false} ** MAXD); // @memset( 按位与 pacific, [1]bool{false} 乘 乘 MAXD);
    @memset(&atlantic, [1]bool{false} ** MAXD); // @memset( 按位与 atlantic, [1]bool{false} 乘 乘 MAXD);

    var r: usize = 0; // 把 0; 写入 var r: usize
    while (r < m) : (r += 1) { // 循环，直到不满足「右指针 小于 映射表) : (右指针 累加 1」
        dfs(r, 0, &pacific); // dfs(右指针, 0, 按位与 pacific);
        dfs(r, n - 1, &atlantic); // dfs(右指针, 元素个数 减 1, 按位与 atlantic);
    }
    var c: usize = 0; // 把 0; 写入 var c: usize
    while (c < n) : (c += 1) { // 循环，直到不满足「字符 小于 元素个数) : (字符 累加 1」
        dfs(0, c, &pacific); // dfs(0, 字符, 按位与 pacific);
        dfs(m - 1, c, &atlantic); // dfs(映射表 减 1, 字符, 按位与 atlantic);
    }

    var cnt: usize = 0; // 把 0; 写入 var cnt: usize
    r = 0; // 把 0; 写入 右指针
    while (r < m) : (r += 1) { // 循环，直到不满足「右指针 小于 映射表) : (右指针 累加 1」
        c = 0; // 把 0; 写入 字符
        while (c < n) : (c += 1) { // 循环，直到不满足「字符 小于 元素个数) : (字符 累加 1」
            if (pacific[r][c] and atlantic[r][c]) { // 若 pacific[右指针][字符] and atlantic[右指针][字符]
                res[cnt] = .{ r, c }; // 把 { 右指针, 字符 }; 写入 res[cnt]
                cnt += 1; // 计数累加 1
            }
        }
    }
    return cnt; // 返回 计数
}

pub fn main() !void { // 程序入口：跑内嵌自测用例
    // 空输入：null 矩阵应返回 []
    var res: [MAXD * MAXD][2]usize = undefined; // 把 undefined; 写入 var res: [MAXD * MAXD][2]usize
    const got = pacificAtlantic(null, 5, 5, &res); // 把 pacificAtlantic(null, 5, 5, 按位与 结果) 存入 got
    if (got != 0) return error.NullMatrixShouldYieldEmpty; // 若 got 不等于 0，直接返回 error.NullMatrixShouldYieldEmpty
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
