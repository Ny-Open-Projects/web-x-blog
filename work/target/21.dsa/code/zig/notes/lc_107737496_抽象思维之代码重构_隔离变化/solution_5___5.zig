// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496
// LeetCode 107737496. 代码重构_隔离变化 — Zig 版（方案5：Matrix 封装 set/call）
const std = @import("std"); // 把 @import(「std」) 存入 std

const Matrix = struct { // 把 struct { 存入 Matrix
    row: usize,
    col: usize,
    buf: [8][8]i32 = [_][8]i32{[_]i32{0} ** 8} ** 8,

    fn init(r: usize, c: usize) Matrix { // 定义函数/方法 init
        return .{ .row = r, .col = c }; // 返回 { .row 赋值为 右指针, .col 赋值为 字符 }
    }
    fn set(self: *Matrix, r: usize, c: usize, v: i32) void { // 定义函数/方法 set
        self.buf[r][c] = v; // 把 值; 写入 self.buf[r][c]
    }
    fn call(self: *const Matrix, r: usize, c: usize) i32 { // 定义函数/方法 call
        return self.buf[r][c]; // 返回 self.buf[右指针][字符]
    }
};

pub fn main() !void { // 程序入口：跑内嵌自测用例
    var m = Matrix.init(4, 5); // 把 Matrix.init(4, 5) 存入 映射表
    var i: usize = 0; // 把 0; 写入 var i: usize
    while (i < 4) : (i += 1) { // 循环，直到不满足「下标 i 小于 4) : (下标 i 累加 1」
        var j: usize = 0; // 把 0; 写入 var j: usize
        while (j < 5) : (j += 1) { // 循环，直到不满足「下标 j 小于 5) : (下标 j 累加 1」
            m.set(i, j, @intCast(i * j)); // 映射表.set(下标 i, 下标 j, @intCast(下标 i 乘 下标 j));
        }
    }
    if (m.call(2, 3) != 6) return error.TestFailed; // 若 映射表.call(2, 3) 不等于 6，直接返回 error.TestFailed
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
