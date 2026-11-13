// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496
// LeetCode 107737496. 代码重构_隔离变化 — Zig 版（方案11：Rule 循环游标）
const std = @import("std"); // 把 @import(「std」) 存入 std

const Rule = struct { // 把 struct { 存入 Rule
    data: []const u8,
    idx: usize = 0,

    fn init(r: []const u8) Rule { // 定义函数/方法 init
        return .{ .data = r }; // 返回 { .data 赋值为 右指针 }
    }
    fn next(self: *Rule) u8 { // 定义函数/方法 next
        const ch = self.data[self.idx]; // 把 self.data[self.idx] 存入 字符
        self.idx = (self.idx + 1) % self.data.len; // 把 (self.idx 加 1) 对…取模 self.data.长度; 写入 self.idx
        return ch; // 返回 字符
    }
    fn peek(self: *const Rule) u8 { // 定义函数/方法 peek
        return self.data[self.idx]; // 返回 self.data[self.idx]
    }
};

pub fn main() !void { // 程序入口：跑内嵌自测用例
    var r = Rule.init("ESVM"); // 把 Rule.init(「ESVM」) 存入 右指针
    var s1: [10]u8 = undefined; // 把 undefined; 写入 var s1: [10]u8
    for (0..10) |i| s1[i] = r.next(); // 让 下标 i 从 0 走到 10 减一
    var r2 = Rule.init("semv"); // 把 Rule.init(「semv」) 存入 r2
    var s2: [6]u8 = undefined; // 把 undefined; 写入 var s2: [6]u8
    for (0..6) |i| s2[i] = r2.next(); // 让 下标 i 从 0 走到 6 减一
    if (!std.mem.eql(u8, &s1, "ESVMESVMES")) return error.TestFailed;
    if (!std.mem.eql(u8, &s2, "semvse")) return error.TestFailed; // 若 取反 std.mem.eql(u8, 按位与 s2, 「semvse」)，直接返回 error.TestFailed
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
