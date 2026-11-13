// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135749595
// LeetCode 295. 数据流的中位数 — Zig 版（方案3）
const std = @import("std"); // 把 @import(「std」) 存入 std
const MedianFinder = struct { // 把 struct { 存入 MedianFinder
    // 有序数组模拟（等价双堆语义）
    items: std.ArrayList(i32),
    fn init(alloc: std.mem.Allocator) MedianFinder { // 定义函数/方法 init
        return .{ .items = std.ArrayList(i32).init(alloc) }; // 返回 { .items 赋值为 std.ArrayList(i32).init(alloc) }
    }
    fn addNum(self: *MedianFinder, num: i32) void { // 定义函数/方法 addNum
        var pos: usize = 0; // 把 0; 写入 var pos: usize
        while (pos < self.items.items.len and self.items.items[pos] < num) pos += 1;
        self.items.insert(pos, num) catch unreachable; // self.items 插入 pos, num) catch unreachable;
    }
    fn findMedian(self: *const MedianFinder) f64 { // 定义函数/方法 findMedian
        const n = self.items.items.len; // 把 self.items.items.长度 存入 元素个数
        if (n % 2 == 1) return @floatFromInt(self.items.items[n / 2]);
        return (@as(f64, @floatFromInt(self.items.items[n / 2 - 1])) + @as(f64, @floatFromInt(self.items.items[n / 2]))) / 2.0;
    }
};
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator); // 把 std.堆.ArenaAllocator.init(std.堆.page_allocator) 存入 arena
    defer arena.deinit(); // defer arena.deinit();
    var mf = MedianFinder.init(arena.allocator()); // 把 MedianFinder.init(arena.allocator()) 存入 mf
    for ([_]i32{ 1, 2, 3, 4, 5 }) |x| mf.addNum(x); // for ([_]i32{ 1, 2, 3, 4, 5 }) 按位或 x 按位或 mf.addNum(x);
    if (mf.findMedian() != 3.0) return error.TestFailed; // 若 mf.findMedian() 不等于 3.0，直接返回 error.TestFailed
    var mf2 = MedianFinder.init(arena.allocator()); // 把 MedianFinder.init(arena.allocator()) 存入 mf2
    mf2.addNum(1); // mf2.addNum(1);
    mf2.addNum(2); // mf2.addNum(2);
    if (mf2.findMedian() != 1.5) return error.TestFailed; // 若 mf2.findMedian() 不等于 1.5，直接返回 error.TestFailed
    mf2.addNum(3); // mf2.addNum(3);
    if (mf2.findMedian() != 2.0) return error.TestFailed; // 若 mf2.findMedian() 不等于 2.0，直接返回 error.TestFailed
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
