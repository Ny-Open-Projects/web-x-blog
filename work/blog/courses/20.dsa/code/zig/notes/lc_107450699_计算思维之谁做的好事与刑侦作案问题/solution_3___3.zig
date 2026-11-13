// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107450699
// 计算思维之谁做的好事 — Zig 版（方案3）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn findGoodMan() u8 { // 定义函数/方法 findGoodMan
    const men = [_]u8{ 'A', 'B', 'C', 'D' }; // 把 [_]u8{ 'A', 'B', 'C', 'D' } 存入 men
    for (men) |m| { // 逐个取出 men 的元素（映射表）
        var t: i32 = 0; // 把 0; 写入 var t: i32
        if (m != 'A') t += 1; // 若 映射表 不等于 'A') 另一字符串 累加 1;
        if (m == 'C') t += 1; // 若 映射表 等于 'C') 另一字符串 累加 1;
        if (m == 'D') t += 1; // 若 映射表 等于 'D') 另一字符串 累加 1;
        if (m != 'D') t += 1; // 若 映射表 不等于 'D') 另一字符串 累加 1;
        if (t == 3) return m; // 若 另一字符串 等于 3，直接返回 映射表
    }
    return '?'; // 返回 '?'
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    if (findGoodMan() != 'C') return error.TestFailed; // 若 findGoodMan() 不等于 'C'，直接返回 error.TestFailed
    std.debug.print("PASS\n", .{});
} // 全部用例通过，输出 PASS
