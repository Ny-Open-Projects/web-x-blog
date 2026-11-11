// 来源：https://blog.csdn.net/tyro_java/article/details/107490876
// LeetCode 107490876. 分书和八皇后问题 — Zig 版（方案6：八皇后不可变状态函数式）
const std = @import("std"); // 把 @import(「std」) 存入 std

const State = struct { // 把 struct { 存入 State
    col_row: [8]i32 = [_]i32{0} ** 8,
    col_len: usize = 0,
    rows: [8]bool = [_]bool{true} ** 8,
    diag1: [16]bool = [_]bool{true} ** 16,
    diag2: [16]bool = [_]bool{true} ** 16,
};

var sols: [100][8]i32 = undefined; // 把 undefined; 写入 var sols: [100][8]i32
var sol_count: usize = 0; // 把 0; 写入 var sol_count: usize

fn place(col: usize, n: usize, st: State) void { // 定义函数/方法 place
    if (col == n) { // 若 col 等于 元素个数
        var j: usize = 0; // 把 0; 写入 var j: usize
        while (j < st.col_len) : (j += 1) sols[sol_count][j] = st.col_row[j];
        sol_count += 1; // sol_count累加 1
        return; // return;
    }
    var row: usize = 0; // 把 0; 写入 var row: usize
    while (row < n) : (row += 1) { // 循环，直到不满足「row 小于 元素个数) : (row 累加 1」
        const d1 = col + n - 1 - row; // 把 col 加 元素个数 减 1 减 row 存入 d1
        const d2 = col + row; // 把 col 加 row 存入 d2
        if (st.rows[row] and st.diag1[d1] and st.diag2[d2]) { // 若 st.行数[row] and st.diag1[d1] and st.diag2[d2]
            // 值拷贝 = 不可变语义
            var ns = st; // 把 st 存入 ns
            ns.col_row[st.col_len] = @intCast(row); // 把 @intCast(row); 写入 ns.col_row[st.col_len]
            ns.col_len = st.col_len + 1; // 把 st.col_len 加 1; 写入 ns.col_len
            ns.rows[row] = false; // 把 false; 写入 ns.rows[row]
            ns.diag1[d1] = false; // 把 false; 写入 ns.diag1[d1]
            ns.diag2[d2] = false; // 把 false; 写入 ns.diag2[d2]
            place(col + 1, n, ns); // place(col 加 1, 元素个数, ns);
        }
    }
}

fn nQueensFunc(n: usize) usize { // 定义函数/方法 nQueensFunc
    sol_count = 0; // 把 0; 写入 sol_count
    place(0, n, State{}); // place(0, 元素个数, State{});
    return sol_count; // 返回 sol_count
}

pub fn main() !void { // 程序入口：跑内嵌自测用例
    const Case = struct { n: usize, count: usize, first: ?[8]i32, flen: usize };
    const cases = [_]Case{ // 把 [_]Case{ 存入 cases
        .{ .n = 8, .count = 92, .first = .{ 0, 4, 7, 5, 2, 6, 1, 3 }, .flen = 8 },
        .{ .n = 1, .count = 1, .first = .{ 0, 0, 0, 0, 0, 0, 0, 0 }, .flen = 1 },
        .{ .n = 2, .count = 0, .first = null, .flen = 0 },
        .{ .n = 4, .count = 2, .first = .{ 1, 3, 0, 2, 0, 0, 0, 0 }, .flen = 4 },
    };
    for (cases, 0..) |c, idx| { // for (cases, 0..) 按位或 字符, idx 按位或 {
        const count = nQueensFunc(c.n); // 把 nQueensFunc(字符.元素个数) 存入 计数
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
