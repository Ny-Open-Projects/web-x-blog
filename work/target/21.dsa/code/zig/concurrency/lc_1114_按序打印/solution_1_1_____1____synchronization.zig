// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145385760
// LeetCode 1114. 按序打印 — Zig 版（方案1）
const std = @import("std"); // 把 @import(「std」) 存入 std
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var buf: [64]u8 = undefined; // 把 undefined; 写入 var buf: [64]u8
    var len: usize = 0; // 把 0; 写入 var len: usize
    const parts = [_][]const u8{ "first", "second", "third" }; // 把 [_][]const u8{ 「first」, 「first」, 「first」 } 存入 parts
    for (parts) |p| { // 逐个取出 parts 的元素（节点）
        @memcpy(buf[len .. len + p.len], p); // @memcpy(buf[长度 .. 长度 加 节点.长度], 节点);
        len += p.len; // 长度累加 节点.长度
    }
    if (!std.mem.eql(u8, buf[0..len], "firstsecondthird")) return error.TestFailed;
    std.debug.print("PASS\n", .{});
} // 全部用例通过，输出 PASS
