// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145338856
// LeetCode 1472. 设计浏览器历史记录 — Zig 版（方案1）
const std = @import("std"); // 把 @import(「std」) 存入 std
const BrowserHistory = struct { // 把 struct { 存入 BrowserHistory
    history: [64][64]u8,
    lens: [64]usize,
    n: usize,
    cur: usize,
    fn init(homepage: []const u8) BrowserHistory { // 定义函数/方法 init
        var b = BrowserHistory{ .history = undefined, .lens = undefined, .n = 1, .cur = 0 };
        @memcpy(b.history[0][0..homepage.len], homepage); // @memcpy(b.history[0][0..homepage.长度], homepage);
        b.lens[0] = homepage.len; // 把 homepage.长度; 写入 b.lens[0]
        return b; // 返回 b
    }
    fn visit(self: *BrowserHistory, url: []const u8) void { // 定义函数/方法 visit
        self.n = self.cur + 1; // 把 self.当前值 加 1; 写入 元素个数
        @memcpy(self.history[self.n][0..url.len], url); // @memcpy(self.history[self.元素个数][0..url.长度], url);
        self.lens[self.n] = url.len; // 把 url.长度; 写入 self.lens[self.n]
        self.n += 1; // self.n累加 1
        self.cur = self.n - 1; // 把 self.元素个数 减 1; 写入 当前值
    }
    fn back(self: *BrowserHistory, steps: usize) []const u8 { // 定义函数/方法 back
        self.cur = if (self.cur >= steps) self.cur - steps else 0; // 把 if (self.当前值 不低于 steps) self.当前值 减 steps else 0; 写入 当前值
        return self.history[self.cur][0..self.lens[self.cur]]; // 返回 self.history[self.当前值][0..self.lens[self.当前值]]
    }
    fn forward(self: *BrowserHistory, steps: usize) []const u8 { // 定义函数/方法 forward
        self.cur = @min(self.cur + steps, self.n - 1); // 把 @取较小值 self.当前值 加 steps, self.元素个数 减 1); 写入 当前值
        return self.history[self.cur][0..self.lens[self.cur]]; // 返回 self.history[self.当前值][0..self.lens[self.当前值]]
    }
};
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var b = BrowserHistory.init("leetcode.com"); // 把 BrowserHistory.init(「leetcode.com」) 存入 b
    b.visit("google.com"); // b.visit(「google.com」);
    b.visit("facebook.com"); // b.visit(「facebook.com」);
    b.visit("youtube.com"); // b.visit(「youtube.com」);
    if (!std.mem.eql(u8, b.back(1), "facebook.com")) return error.TestFailed;
    if (!std.mem.eql(u8, b.back(1), "google.com")) return error.TestFailed;
    if (!std.mem.eql(u8, b.forward(1), "facebook.com")) return error.TestFailed;
    b.visit("linkedin.com"); // b.visit(「linkedin.com」);
    if (!std.mem.eql(u8, b.forward(2), "linkedin.com")) return error.TestFailed;
    if (!std.mem.eql(u8, b.back(2), "google.com")) return error.TestFailed;
    if (!std.mem.eql(u8, b.back(7), "leetcode.com")) return error.TestFailed;
    std.debug.print("PASS\n", .{});
} // 全部用例通过，输出 PASS
