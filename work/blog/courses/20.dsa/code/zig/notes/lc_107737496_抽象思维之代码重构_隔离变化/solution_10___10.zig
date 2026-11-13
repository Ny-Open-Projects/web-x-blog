// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496
// LeetCode 107737496. 代码重构_隔离变化 — Zig 版（方案10：Filler+Matrix 组合 9x9 全螺旋）
const std = @import("std"); // 把 @import(「std」) 存入 std

const RCu = struct { r: usize, c: usize }; // 把 struct { 右指针: usize, 字符: usize } 存入 RCu

const Filler = struct { // 把 struct { 存入 Filler
    pos_row: usize = 0,
    pos_col: usize = 0,
    idx: usize = 0,
    r_min: usize = 0,
    c_min: usize = 0,
    r_max: usize,
    c_max: usize,

    fn init(rn: usize, cn: usize) Filler { // 定义函数/方法 init
        return .{ .r_max = rn - 1, .c_max = cn - 1 }; // 返回 { .r_max 赋值为 rn 减 1, .c_max 赋值为 cn 减 1 }
    }
    fn next(self: *Filler) RCu { // 定义函数/方法 next
        const res = RCu{ .r = self.pos_row, .c = self.pos_col }; // 把 RCu{ .右指针 赋值为 self.pos_row, .字符 赋值为 self.pos_col } 存入 结果
        const rule = "ESVM"; // 把 「ESVM」 存入 rule
        const cmd = rule[self.idx % 4]; // 把 rule[self.idx 对…取模 4] 存入 cmd
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
        return res; // 返回 结果
    }
};

fn fmtRow(buf: []u8, row: []const i32) ![]u8 { // 定义函数/方法 fmtRow
    var n: usize = 0; // 把 0; 写入 var n: usize
    for (row, 0..) |x, i| { // for (row, 0..) 按位或 x, 下标 i 按位或 {
        if (i != 0) { // 若 下标 i 不等于 0
            buf[n] = ' '; // 把 ' '; 写入 buf[n]
            n += 1; // 元素个数累加 1
        }
        var cell_buf: [16]u8 = undefined; // 把 undefined; 写入 var cell_buf: [16]u8
        const cell = try std.fmt.bufPrint(&cell_buf, "{d}", .{x}); // 把 try std.fmt.bufPrint( 按位与 cell_buf, 「{d}」, .{x}) 存入 cell
        if (cell.len < 2) { // 若 cell.长度 小于 2
            buf[n] = ' '; // 把 ' '; 写入 buf[n]
            n += 1; // 元素个数累加 1
        }
        for (cell) |ch| { // 逐个取出 cell 的元素（字符）
            buf[n] = ch; // 把 字符; 写入 buf[n]
            n += 1; // 元素个数累加 1
        }
    }
    return buf[0..n]; // 返回 buf[0..元素个数]
}

pub fn main() !void { // 程序入口：跑内嵌自测用例
    const rn: usize = 9; // 把 9; 写入 const rn: usize
    const cn: usize = 9; // 把 9; 写入 const cn: usize
    var obj = Filler.init(rn, cn); // 把 Filler.init(rn, cn) 存入 obj
    var m: [9][9]i32 = undefined; // 把 undefined; 写入 var m: [9][9]i32
    for (&m) |*row| { // for ( 按位与 映射表) 按位或 乘 row 按位或 {
        for (row) |*x| x.* = 0; // 把 0; 写入 for (row) |*x| x.*
    }
    for (0..rn * cn) |i| { // for (0..rn 乘 cn) 按位或 下标 i 按位或 {
        const rc = obj.next(); // 把 obj.下一个() 存入 rc
        m[rc.r][rc.c] = @intCast(i + 1); // 把 @intCast(下标 i 加 1); 写入 m[rc.r][rc.c]
    }
    const want = [9][]const u8{ // 把 [9][]const u8{ 存入 want
        " 1 32 31 30 29 28 27 26 25",
        " 2 33 56 55 54 53 52 51 24",
        " 3 34 57 72 71 70 69 50 23",
        " 4 35 58 73 80 79 68 49 22",
        " 5 36 59 74 81 78 67 48 21",
        " 6 37 60 75 76 77 66 47 20",
        " 7 38 61 62 63 64 65 46 19",
        " 8 39 40 41 42 43 44 45 18",
        " 9 10 11 12 13 14 15 16 17",
    };
    var buf: [64]u8 = undefined; // 把 undefined; 写入 var buf: [64]u8
    for (want, 0..) |w, i| { // for (want, 0..) 按位或 权重, 下标 i 按位或 {
        const got = try fmtRow(&buf, &m[i]); // 把 try fmtRow( 按位与 buf, 按位与 映射表[下标 i]) 存入 got
        if (!std.mem.eql(u8, got, w)) { // 若 取反 std.mem.eql(u8, got, 权重
            std.debug.print("matrix9 row {d} failed\n", .{i}); // 打印输出
            return error.TestFailed; // 返回 error.TestFailed
        }
    }
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
