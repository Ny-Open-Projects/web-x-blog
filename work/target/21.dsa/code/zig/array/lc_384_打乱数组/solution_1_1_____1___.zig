// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134350547
// LeetCode 384. 打乱数组 — Zig 版（方案1）
const std = @import("std"); // 把 @import(「std」) 存入 std
const ShuffleArray = struct { // 把 struct { 存入 ShuffleArray
    orig: []i32,
    cur: []i32,
    fn init(alloc: std.mem.Allocator, vals: []const i32) ShuffleArray { // 定义函数/方法 init
        return .{ .orig = alloc.dupe(i32, vals) catch unreachable, .cur = alloc.dupe(i32, vals) catch unreachable };
    }
    fn reset(self: *ShuffleArray) []i32 { // 定义函数/方法 reset
        @memcpy(self.cur, self.orig); // @memcpy(self.当前值, self.orig);
        return self.cur; // 返回 self.当前值
    }
    fn shuffle(self: *ShuffleArray) []i32 { // 定义函数/方法 shuffle
        var i: usize = self.cur.len; // 把 self.当前值.长度; 写入 var i: usize
        while (i > 1) { // 循环，直到不满足「下标 i 超过 1」
            i -= 1; // 下标 i累减 1
            const t = self.cur[i]; // 把 self.当前值[下标 i] 存入 另一字符串
            self.cur[i] = self.cur[0]; // 把 self.当前值[0]; 写入 self.cur[i]
            self.cur[0] = t; // 把 另一字符串; 写入 self.cur[0]
        }
        return self.cur; // 返回 self.当前值
    }
};
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator); // 把 std.堆.ArenaAllocator.init(std.堆.page_allocator) 存入 arena
    defer arena.deinit(); // defer arena.deinit();
    const alloc = arena.allocator(); // 把 arena.allocator() 存入 alloc
    var sa = ShuffleArray.init(alloc, &[_]i32{ 1, 2, 3 }); // 把 ShuffleArray.init(alloc, 按位与 [_]i32{ 1, 2, 3 }) 存入 sa
    const sh = sa.shuffle(); // 把 sa.shuffle() 存入 sh
    const sorted = alloc.dupe(i32, sh) catch unreachable; // 把 alloc.dupe(i32, sh) catch unreachable 存入 sorted
    std.sort.pdq(i32, sorted, {}, std.sort.asc(i32)); // std.sort.pdq(i32, sorted, {}, std.sort.asc(i32));
    if (sorted[0] != 1 or sorted[2] != 3) return error.TestFailed; // 若 sorted[0] 不等于 1 or sorted[2] 不等于 3，直接返回 error.TestFailed
    const r = sa.reset(); // 把 sa.reset() 存入 右指针
    if (r[0] != 1 or r[2] != 3) return error.TestFailed; // 若 右指针[0] 不等于 1 or 右指针[2] 不等于 3，直接返回 error.TestFailed
    std.debug.print("PASS\n", .{});
} // 全部用例通过，输出 PASS
