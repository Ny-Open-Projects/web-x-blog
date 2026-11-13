// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145386116
// LeetCode 3100. 换水问题 II — Zig 版（方案1）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn maxBottlesDrunk(nb_in: i32, ne_in: i32) i32 { // 定义函数/方法 maxBottlesDrunk
    var drunk = nb_in; // 把 nb_in 存入 drunk
    var empty = nb_in; // 把 nb_in 存入 empty
    var ne = ne_in; // 把 ne_in 存入 ne
    while (empty >= ne) { // 循环，直到不满足「empty 不低于 ne」
        empty -= ne; // empty累减 ne
        ne += 1; // ne累加 1
        drunk += 1; // drunk累加 1
        empty += 1; // empty累加 1
    }
    return drunk; // 返回 drunk
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    if (maxBottlesDrunk(10, 3) != 13) return error.TestFailed; // 若 maxBottlesDrunk(10, 3) 不等于 13，直接返回 error.TestFailed
    if (maxBottlesDrunk(1, 2) != 1) return error.TestFailed; // 若 maxBottlesDrunk(1, 2) 不等于 1，直接返回 error.TestFailed
    std.debug.print("PASS\n", .{});
} // 全部用例通过，输出 PASS
