// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134934324
// LeetCode 914. 卡牌分组 — Zig 版（方案9）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn gcdFn(a: i32, b: i32) i32 { // 定义函数/方法 gcdFn
    var x = a; // 把 数组 存入 x
    var y = b; // 把 b 存入 y
    while (y != 0) { // 循环，直到不满足「y 不等于 0」
        const t = @mod(x, y); // 把 @mod(x, y) 存入 另一字符串
        x = y; // 把 y; 写入 x
        y = t; // 把 另一字符串; 写入 y
    }
    return x; // 返回 x
}
fn hasGroupsSizeX(deck: []const i32) bool { // 定义函数/方法 hasGroupsSizeX
    var counts = [_]i32{0} ** 65536; // 把 [_]i32{0} 乘 乘 65536 存入 counts
    for (deck) |c| counts[@intCast(c + 32768)] += 1; // 逐个取出 deck 的元素（字符）
    var g: i32 = 0; // 把 0; 写入 var g: i32
    for (counts) |v| { // 逐个取出 counts 的元素（值）
        if (v > 0) g = gcdFn(g, v); // 若 值 超过 0) g 赋值为 gcdFn(g, 值);
    }
    return g >= 2; // 返回 g 不低于 2
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    if (!hasGroupsSizeX(&[_]i32{ 1, 2, 3, 4, 4, 3, 2, 1 })) return error.TestFailed;
    if (hasGroupsSizeX(&[_]i32{ 1, 1, 1, 2, 2, 2, 3, 3 })) return error.TestFailed;
    if (hasGroupsSizeX(&[_]i32{1})) return error.TestFailed; // 若 hasGroupsSizeX( 按位与 [_]i32{1})，直接返回 error.TestFailed
    std.debug.print("PASS\n", .{});
} // 全部用例通过，输出 PASS
