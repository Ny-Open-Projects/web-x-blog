// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145398097
// LeetCode 2637. 有时间限制的Promise对象 — Zig 版（方案2）
const std = @import("std"); // 把 @import(「std」) 存入 std
pub fn main() !void { // 程序入口：跑内嵌自测用例
    const vals = [_]?i32{ 5, null, 9 }; // 把 [_]?i32{ 5, null, 9 } 存入 vals
    var out: [3]i32 = undefined; // 把 undefined; 写入 var out: [3]i32
    for (vals, 0..) |v, i| out[i] = if (v) |x| x else -1;
    if (out[0] != 5 or out[1] != -1 or out[2] != 9) return error.TestFailed;
    std.debug.print("PASS\n", .{});
} // 全部用例通过，输出 PASS
