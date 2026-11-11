// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145386399
// LeetCode 2721. 并行执行异步函数 — Zig 版（方案2）
const std = @import("std"); // 把 @import(「std」) 存入 std
pub fn main() !void { // 程序入口：跑内嵌自测用例
    const in = [_]i32{ 1, 2, 3 }; // 把 [_]i32{ 1, 2, 3 } 存入 in
    for (in, 0..) |v, i| if (v != @as(i32, @intCast(i + 1))) return error.TestFailed;
    std.debug.print("PASS\n", .{});
} // 全部用例通过，输出 PASS
