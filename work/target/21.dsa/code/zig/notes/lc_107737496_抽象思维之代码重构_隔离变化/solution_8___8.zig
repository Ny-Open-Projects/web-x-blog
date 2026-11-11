// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496
// LeetCode 107737496. 代码重构_隔离变化 — Zig 版（方案8：Filler 状态机 + hasNext 部分填充）
const std = @import("std"); // 把 @import(「std」) 存入 std

const Filler = struct { // 把 struct { 存入 Filler
    row_num: usize,
    col_num: usize,
    rule: [8]u8 = undefined,
    rule_len: usize = 0,
    pos_row: usize = 0,
    pos_col: usize = 0,
    idx: usize = 0,
    r_min: usize = 0,
    c_min: usize = 0,
    r_max: usize,
    c_max: usize,

    fn init(rn: usize, cn: usize) Filler { // 定义函数/方法 init
        return .{ .row_num = rn, .col_num = cn, .r_max = rn - 1, .c_max = cn - 1 };
    }
    fn setRule(self: *Filler, r: []const u8) void { // 定义函数/方法 setRule
        for (r, 0..) |ch, i| self.rule[i] = ch; // 把 字符; 写入 for (r, 0..) |ch, i| self.rule[i]
        self.rule_len = r.len; // 把 右指针.长度; 写入 self.rule_len
    }
    fn hasNext(self: *const Filler) bool { // 定义函数/方法 hasNext
        return self.r_min <= self.pos_row and self.pos_row <= self.r_max and
            self.c_min <= self.pos_col and self.pos_col <= self.c_max;
    }
    fn next(self: *Filler) struct { r: usize, c: usize } { // 定义函数/方法 next
        const r = self.pos_row; // 把 self.pos_row 存入 右指针
        const c = self.pos_col; // 把 self.pos_col 存入 字符
        self.advance(); // self.advance();
        return .{ .r = r, .c = c }; // 返回 { .右指针 赋值为 右指针, .字符 赋值为 字符 }
    }
    fn advance(self: *Filler) void { // 定义函数/方法 advance
        const cmd = self.rule[self.idx % 4]; // 把 self.rule[self.idx 对…取模 4] 存入 cmd
        if (cmd == 'E') { // 若 cmd 等于 'E'
            self.pos_row += 1; // self.pos_row累加 1
            if (self.pos_row == self.r_max) { // 若 self.pos_row 等于 self.r_max
                self.idx += 1; // self.idx累加 1
                self.c_min += 1; // self.c_min累加 1
            }
        } else if (cmd == 'S') { // 否则，若 cmd 等于 'S'
            self.pos_col += 1; // self.pos_col累加 1
            if (self.pos_col == self.c_max) { // 若 self.pos_col 等于 self.c_max
                self.idx += 1; // self.idx累加 1
                self.r_max -= 1; // self.r_max累减 1
            }
        } else if (cmd == 'V') { // 否则，若 cmd 等于 'V'
            self.pos_row -= 1; // self.pos_row累减 1
            if (self.pos_row == self.r_min) { // 若 self.pos_row 等于 self.r_min
                self.idx += 1; // self.idx累加 1
                self.c_max -= 1; // self.c_max累减 1
            }
        } else if (cmd == 'M') { // 否则，若 cmd 等于 'M'
            self.pos_col -= 1; // self.pos_col累减 1
            if (self.pos_col == self.c_min) { // 若 self.pos_col 等于 self.c_min
                self.idx += 1; // self.idx累加 1
                self.r_min += 1; // self.r_min累加 1
            }
        }
    }
};

fn fillMatrix(rn: usize, cn: usize, rule: []const u8, mat: *[8][8]i32) void { // 定义函数/方法 fillMatrix
    for (0..rn) |i| { // 让 下标 i 从 0 走到 rn 减一
        for (0..cn) |j| mat[i][j] = 0; // 让 下标 j 从 0 走到 cn 减一
    }
    var f = Filler.init(rn, cn); // 把 Filler.init(rn, cn) 存入 f
    f.setRule(rule); // f.setRule(rule);
    var i: i32 = 1; // 把 1; 写入 var i: i32
    while (f.hasNext()) { // 循环，直到不满足「f.hasNext(」
        const rc = f.next(); // 把 f.下一个() 存入 rc
        mat[rc.r][rc.c] = i; // 把 下标 i; 写入 mat[rc.r][rc.c]
        i += 1; // 下标 i累加 1
    }
}

pub fn main() !void { // 程序入口：跑内嵌自测用例
    var mat: [8][8]i32 = undefined; // 把 undefined; 写入 var mat: [8][8]i32
    const want1 = [6][6]i32{ // 把 [6][6]i32{ 存入 want1
        .{ 1, 0, 0, 0, 0, 0 },
        .{ 2, 0, 0, 0, 0, 0 },
        .{ 3, 0, 0, 0, 0, 0 },
        .{ 4, 0, 0, 0, 0, 0 },
        .{ 5, 0, 0, 0, 0, 0 },
        .{ 0, 0, 0, 0, 0, 0 },
    };
    fillMatrix(6, 6, "ESVM", &mat); // fillMatrix(6, 6, 「ESVM」, 按位与 mat);
    for (want1, 0..) |row, i| { // for (want1, 0..) 按位或 row, 下标 i 按位或 {
        for (row, 0..) |x, j| { // for (row, 0..) 按位或 x, 下标 j 按位或 {
            if (mat[i][j] != x) return error.TestFailed; // 若 mat[下标 i][下标 j] 不等于 x，直接返回 error.TestFailed
        }
    }
    const want2 = [3][3]i32{ .{ 1, 0, 0 }, .{ 2, 0, 0 }, .{ 0, 0, 0 } };
    fillMatrix(3, 3, "ESVM", &mat); // fillMatrix(3, 3, 「ESVM」, 按位与 mat);
    for (want2, 0..) |row, i| { // for (want2, 0..) 按位或 row, 下标 i 按位或 {
        for (row, 0..) |x, j| { // for (row, 0..) 按位或 x, 下标 j 按位或 {
            if (mat[i][j] != x) return error.TestFailed; // 若 mat[下标 i][下标 j] 不等于 x，直接返回 error.TestFailed
        }
    }
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
