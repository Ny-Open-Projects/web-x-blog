// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130470370
// LeetCode 933. 最近的请求次数 — Zig 版
const std = @import("std"); // 把 @import(「std」) 存入 std

// 方案3：push + 真出队（orderedRemove(0) 等价 TS 数组 shift）
const RecentCounter = struct { // 把 struct { 存入 RecentCounter
    q: std.ArrayList(i32),

    fn init(allocator: std.mem.Allocator) RecentCounter { // 定义函数/方法 init
        return .{ .q = std.ArrayList(i32).init(allocator) }; // 返回 { .节点 赋值为 std.ArrayList(i32).init(allocator) }
    }

    fn ping(self: *RecentCounter, t: i32) !usize { // 定义函数/方法 ping
        try self.q.append(t); // 把 另一字符串 追加到列表尾部
        while (self.q.items.len > 0 and self.q.items[0] < t - 3000) {
            _ = self.q.orderedRemove(0); // 真出队
        }
        return self.q.items.len; // 返回 self.节点.items.长度
    }
};

pub fn main() !void { // 程序入口：跑内嵌自测用例
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator); // 把 std.堆.ArenaAllocator.init(std.堆.page_allocator) 存入 arena
    defer arena.deinit(); // defer arena.deinit();
    var c = RecentCounter.init(arena.allocator()); // 把 RecentCounter.init(arena.allocator()) 存入 字符

    // 与 TS 事实源内嵌用例一致
    const want = [_]usize{ 1, 2, 3, 3 }; // 把 [_]usize{ 1, 2, 3, 3 } 存入 want
    const ts = [_]i32{ 1, 100, 3001, 3002 }; // 把 [_]i32{ 1, 100, 3001, 3002 } 存入 ts
    for (ts, want, 0..) |t, w, i| { // for (ts, want, 0..) 按位或 另一字符串, 权重, 下标 i 按位或 {
        const got = try c.ping(t); // 把 try 字符.ping(另一字符串) 存入 got
        if (got != w) { // 若 got 不等于 权重
            std.debug.print("FAIL case {d} got {d} want {d}\n", .{ i, got, w }); // 打印输出
            return error.TestFailed; // 返回 error.TestFailed
        }
    }
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
