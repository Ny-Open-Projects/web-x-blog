// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130709323
// LeetCode 877. 石子游戏 — Zig 版（方案2）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn stoneGame(piles: []const i32) bool { // 定义函数/方法 stoneGame
    _ = piles; // 把 piles; 写入 _
    return true; // 返回 true
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    if (!stoneGame(&[_]i32{ 5, 3, 4, 5 })) return error.TestFailed;
    if (!stoneGame(&[_]i32{ 3, 7, 2, 3 })) return error.TestFailed;
    std.debug.print("PASS\n", .{});
} // 全部用例通过，输出 PASS
