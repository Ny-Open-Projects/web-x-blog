// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145556343
// LeetCode 2166. 设计位集 — Zig 版（方案1）
const std = @import("std"); // 把 @import(「std」) 存入 std
const Bitset = struct { // 把 struct { 存入 Bitset
    n: usize,
    words: []u32,
    ones: usize,
    reverse: u32,
    fn init(alloc: std.mem.Allocator, size: usize) !Bitset { // 定义函数/方法 init
        const words = try alloc.alloc(u32, (size + 31) / 32); // 把 try alloc.alloc(u32, (大小 加 31) 除以 32) 存入 单词列表
        @memset(words, 0); // @memset(单词列表, 0);
        return .{ .n = size, .words = words, .ones = 0, .reverse = 0 };
    }
    fn get(self: *const Bitset, idx: usize) u32 { // 定义函数/方法 get
        return ((self.words[idx / 32] >> @intCast(idx % 32)) & 1) ^ self.reverse;
    }
    fn fix(self: *Bitset, idx: usize) void { // 定义函数/方法 fix
        if (self.get(idx) == 0) { // 若 self 查找 idx) 等于 0
            self.words[idx / 32] |= @as(u32, 1) << @intCast(idx % 32);
            self.ones += 1; // self.ones累加 1
        }
    }
    fn unfix(self: *Bitset, idx: usize) void { // 定义函数/方法 unfix
        if (self.get(idx) == 1) { // 若 self 查找 idx) 等于 1
            self.words[idx / 32] &= ~(@as(u32, 1) << @intCast(idx % 32));
            self.ones -= 1; // self.ones累减 1
        }
    }
    fn flip(self: *Bitset) void { // 定义函数/方法 flip
        self.reverse ^= 1; // 把 1; 写入 self.reverse ^
        self.ones = self.n - self.ones; // 把 self.元素个数 减 self.ones; 写入 self.ones
    }
    fn all(self: *const Bitset) bool {
        return self.ones == self.n;
    } // 定义函数/方法 all
    fn one(self: *const Bitset) bool {
        return self.ones > 0;
    } // 定义函数/方法 one
    fn toStr(self: *const Bitset, out: []u8) void { // 定义函数/方法 toStr
        for (0..self.n) |i| out[i] = '0' + @as(u8, @intCast(self.get(i))); // 逐个取出 0..self.元素个数 的元素（下标 i）
    }
};
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator); // 把 std.堆.ArenaAllocator.init(std.堆.page_allocator) 存入 arena
    defer arena.deinit(); // defer arena.deinit();
    var bs = try Bitset.init(arena.allocator(), 5); // 把 try Bitset.init(arena.allocator(), 5) 存入 bs
    var buf: [64]u8 = undefined; // 把 undefined; 写入 var buf: [64]u8
    bs.fix(0);
    bs.fix(3); // bs.fix(0); bs.fix(3);
    bs.toStr(&buf); // bs.toStr( 按位与 buf);
    if (!std.mem.eql(u8, buf[0..5], "10010")) return error.TestFailed;
    if (bs.ones != 2) return error.TestFailed; // 若 bs.ones 不等于 2，直接返回 error.TestFailed
    bs.flip(); // bs.flip();
    bs.toStr(&buf); // bs.toStr( 按位与 buf);
    if (!std.mem.eql(u8, buf[0..5], "01101")) return error.TestFailed;
    if (bs.ones != 3) return error.TestFailed; // 若 bs.ones 不等于 3，直接返回 error.TestFailed
    bs.unfix(0); // bs.unfix(0);
    bs.toStr(&buf); // bs.toStr( 按位与 buf);
    if (!std.mem.eql(u8, buf[0..5], "01101")) return error.TestFailed;
    if (bs.all() or !bs.one()) return error.TestFailed; // 若 bs.all() or 取反 bs.one()，直接返回 error.TestFailed
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
