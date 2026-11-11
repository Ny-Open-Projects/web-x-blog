// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496
// LeetCode 107737496. 代码重构_隔离变化 — Zig 版（方案12：Location/Rule/Filler 组合）
const std = @import("std"); // 把 @import(「std」) 存入 std

const Rule = struct { // 把 struct { 存入 Rule
    data: []const u8,
    idx: usize = 0,

    fn init(r: []const u8) Rule { // 定义函数/方法 init
        return .{ .data = r }; // 返回 { .data 赋值为 右指针 }
    }
    fn current(self: *const Rule) u8 { // 定义函数/方法 current
        return self.data[self.idx]; // 返回 self.data[self.idx]
    }
    fn advance(self: *Rule) void { // 定义函数/方法 advance
        self.idx = (self.idx + 1) % self.data.len; // 把 (self.idx 加 1) 对…取模 self.data.长度; 写入 self.idx
    }
};

const RC = struct { r: i32, c: i32 }; // 把 struct { 右指针: i32, 字符: i32 } 存入 RC

const Filler = struct { // 把 struct { 存入 Filler
    pos_row: i32 = 0,
    pos_col: i32 = 0,
    r_min: i32 = 0,
    c_min: i32 = 0,
    r_max: i32,
    c_max: i32,
    cmd: Rule,

    fn init(rn: i32, cn: i32, rule: []const u8) Filler { // 定义函数/方法 init
        return .{ .r_max = rn - 1, .c_max = cn - 1, .cmd = Rule.init(rule) };
    }
    fn next(self: *Filler) RC { // 定义函数/方法 next
        const res = RC{ .r = self.pos_row, .c = self.pos_col }; // 把 RC{ .右指针 赋值为 self.pos_row, .字符 赋值为 self.pos_col } 存入 结果
        const ch = self.cmd.current(); // 把 self.cmd.current() 存入 字符
        if (ch == 'E') { // 若 字符 等于 'E'
            self.pos_row += 1; // self.pos_row累加 1
            if (self.pos_row == self.r_max) { // 若 self.pos_row 等于 self.r_max
                self.cmd.advance(); // self.cmd.advance();
                self.c_min += 1; // self.c_min累加 1
            }
        } else if (ch == 'S') { // 否则，若 字符 等于 'S'
            self.pos_col += 1; // self.pos_col累加 1
            if (self.pos_col == self.c_max) { // 若 self.pos_col 等于 self.c_max
                self.cmd.advance(); // self.cmd.advance();
                self.r_max -= 1; // self.r_max累减 1
            }
        } else if (ch == 'V') { // 否则，若 字符 等于 'V'
            self.pos_row -= 1; // self.pos_row累减 1
            if (self.pos_row == self.r_min) { // 若 self.pos_row 等于 self.r_min
                self.cmd.advance(); // self.cmd.advance();
                self.c_max -= 1; // self.c_max累减 1
            }
        } else if (ch == 'M') { // 否则，若 字符 等于 'M'
            self.pos_col -= 1; // self.pos_col累减 1
            if (self.pos_col == self.c_min) { // 若 self.pos_col 等于 self.c_min
                self.cmd.advance(); // self.cmd.advance();
                self.r_min += 1; // self.r_min累加 1
            }
        }
        return res; // 返回 结果
    }
};

pub fn main() !void { // 程序入口：跑内嵌自测用例
    var obj = Filler.init(4, 4, "ESVM"); // 把 Filler.init(4, 4, 「ESVM」) 存入 obj
    const want = [16][2]i32{ // 把 [16][2]i32{ 存入 want
        .{ 0, 0 }, .{ 1, 0 }, .{ 2, 0 }, .{ 3, 0 }, .{ 3, 1 }, .{ 3, 2 }, .{ 3, 3 }, .{ 2, 3 },
        .{ 1, 3 }, .{ 0, 3 }, .{ 0, 2 }, .{ 0, 1 }, .{ 1, 1 }, .{ 2, 1 }, .{ 2, 2 }, .{ 1, 2 },
    };
    for (want) |w| { // 逐个取出 want 的元素（权重）
        const rc = obj.next(); // 把 obj.下一个() 存入 rc
        if (rc.r != w[0] or rc.c != w[1]) return error.TestFailed; // 若 rc.右指针 不等于 权重[0] or rc.字符 不等于 权重[1]，直接返回 error.TestFailed
    }
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
