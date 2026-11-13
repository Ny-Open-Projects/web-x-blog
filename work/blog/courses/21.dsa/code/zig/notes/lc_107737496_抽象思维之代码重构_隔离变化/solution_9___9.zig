// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496
// LeetCode 107737496. 代码重构_隔离变化 — Zig 版（方案9：规则串状态机，8 方向字母）
const std = @import("std"); // 把 @import(「std」) 存入 std

const RC = struct { r: i32, c: i32 }; // 把 struct { 右指针: i32, 字符: i32 } 存入 RC

const Filler = struct { // 把 struct { 存入 Filler
    row_num: i32,
    col_num: i32,
    pos_row: i32 = 0,
    pos_col: i32 = 0,
    idx: usize = 0,
    r_min: i32 = 0,
    c_min: i32 = 0,
    r_max: i32,
    c_max: i32,
    rule: []const u8 = "ESVM",

    fn init(rn: i32, cn: i32) Filler { // 定义函数/方法 init
        return .{ .row_num = rn, .col_num = cn, .r_max = rn - 1, .c_max = cn - 1 };
    }
    fn setRule(self: *Filler, rule: []const u8) void { // 定义函数/方法 setRule
        self.rule = rule; // 把 rule; 写入 self.rule
    }
    fn next(self: *Filler) RC { // 定义函数/方法 next
        const res = RC{ .r = self.pos_row, .c = self.pos_col }; // 把 RC{ .右指针 赋值为 self.pos_row, .字符 赋值为 self.pos_col } 存入 结果
        const ch = self.rule[self.idx % self.rule.len]; // 把 self.rule[self.idx 对…取模 self.rule.长度] 存入 字符
        if (ch == 'E') { // 若 字符 等于 'E'
            self.pos_row += 1; // self.pos_row累加 1
            if (self.pos_row == self.r_max) { // 若 self.pos_row 等于 self.r_max
                self.idx += 1; // self.idx累加 1
                self.c_min += 1; // self.c_min累加 1
            }
        } else if (ch == 'S') { // 否则，若 字符 等于 'S'
            self.pos_col += 1; // self.pos_col累加 1
            if (self.pos_col == self.c_max) { // 若 self.pos_col 等于 self.c_max
                self.idx += 1; // self.idx累加 1
                self.r_max -= 1; // self.r_max累减 1
            }
        } else if (ch == 'V') { // 否则，若 字符 等于 'V'
            self.pos_row -= 1; // self.pos_row累减 1
            if (self.pos_row == self.r_min) { // 若 self.pos_row 等于 self.r_min
                self.idx += 1; // self.idx累加 1
                self.c_max -= 1; // self.c_max累减 1
            }
        } else if (ch == 'M') { // 否则，若 字符 等于 'M'
            self.pos_col -= 1; // self.pos_col累减 1
            if (self.pos_col == self.c_min) { // 若 self.pos_col 等于 self.c_min
                self.idx += 1; // self.idx累加 1
                self.r_min += 1; // self.r_min累加 1
            }
        } else if (ch == 'e') { // 否则，若 字符 等于 'e'
            self.pos_row += 1; // self.pos_row累加 1
            if (self.pos_row == self.r_max) { // 若 self.pos_row 等于 self.r_max
                self.idx += 1; // self.idx累加 1
                self.c_max -= 1; // self.c_max累减 1
            }
        } else if (ch == 's') { // 否则，若 字符 等于 '字符串'
            self.pos_col += 1; // self.pos_col累加 1
            if (self.pos_col == self.c_max) { // 若 self.pos_col 等于 self.c_max
                self.idx += 1; // self.idx累加 1
                self.r_min += 1; // self.r_min累加 1
            }
        } else if (ch == 'v') { // 否则，若 字符 等于 '值'
            self.pos_row -= 1; // self.pos_row累减 1
            if (self.pos_row == self.r_min) { // 若 self.pos_row 等于 self.r_min
                self.idx += 1; // self.idx累加 1
                self.c_min += 1; // self.c_min累加 1
            }
        } else if (ch == 'm') { // 否则，若 字符 等于 '映射表'
            self.pos_col -= 1; // self.pos_col累减 1
            if (self.pos_col == self.c_min) { // 若 self.pos_col 等于 self.c_min
                self.idx += 1; // self.idx累加 1
                self.r_max -= 1; // self.r_max累减 1
            }
        }
        return res; // 返回 结果
    }
};

fn testFiller(rule: []const u8, rn: i32, cn: i32, seq: *[16][2]i32) void { // 定义函数/方法 testFiller
    var obj = Filler.init(rn, cn); // 把 Filler.init(rn, cn) 存入 obj
    obj.setRule(rule); // obj.setRule(rule);
    for (0..@intCast(rn * cn)) |i| { // for (0..@intCast(rn 乘 cn)) 按位或 下标 i 按位或 {
        const rc = obj.next(); // 把 obj.下一个() 存入 rc
        seq[i][0] = rc.r; // 把 rc.右指针; 写入 seq[i][0]
        seq[i][1] = rc.c; // 把 rc.字符; 写入 seq[i][1]
    }
}

pub fn main() !void { // 程序入口：跑内嵌自测用例
    var seq: [16][2]i32 = undefined; // 把 undefined; 写入 var seq: [16][2]i32
    const want_esvm = [16][2]i32{ // 把 [16][2]i32{ 存入 want_esvm
        .{ 0, 0 }, .{ 1, 0 }, .{ 2, 0 }, .{ 3, 0 }, .{ 3, 1 }, .{ 3, 2 }, .{ 3, 3 }, .{ 2, 3 },
        .{ 1, 3 }, .{ 0, 3 }, .{ 0, 2 }, .{ 0, 1 }, .{ 1, 1 }, .{ 2, 1 }, .{ 2, 2 }, .{ 1, 2 },
    };
    testFiller("ESVM", 4, 4, &seq); // testFiller(「ESVM」, 4, 4, 按位与 seq);
    for (want_esvm, 0..) |w, i| { // for (want_esvm, 0..) 按位或 权重, 下标 i 按位或 {
        if (seq[i][0] != w[0] or seq[i][1] != w[1]) return error.TestFailed;
    }
    const want_semv = [16][2]i32{ // 把 [16][2]i32{ 存入 want_semv
        .{ 0, 0 }, .{ 0, 1 }, .{ 0, 2 }, .{ 0, 3 }, .{ 1, 3 }, .{ 2, 3 }, .{ 3, 3 }, .{ 3, 2 },
        .{ 3, 1 }, .{ 3, 0 }, .{ 2, 0 }, .{ 1, 0 }, .{ 1, 1 }, .{ 1, 2 }, .{ 2, 2 }, .{ 2, 1 },
    };
    testFiller("semv", 4, 4, &seq); // testFiller(「semv」, 4, 4, 按位与 seq);
    for (want_semv, 0..) |w, i| { // for (want_semv, 0..) 按位或 权重, 下标 i 按位或 {
        if (seq[i][0] != w[0] or seq[i][1] != w[1]) return error.TestFailed;
    }
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
