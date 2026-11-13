// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135004886
// LeetCode 165. 比较版本号 — Zig 版（方案1）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn segVal(s: []const u8) i64 { // 定义函数/方法 segVal
    if (s.len == 0) return 0; // 若 字符串.长度 等于 0，直接返回 0
    return std.fmt.parseInt(i64, s, 10) catch 0; // 返回 std.fmt.转整数(i64, 字符串, 10) catch 0
}
fn compareVersion(v1: []const u8, v2: []const u8) i32 { // 定义函数/方法 compareVersion
    var it1 = std.mem.splitScalar(u8, v1, '.'); // 把 std.mem.splitScalar(u8, v1, '.') 存入 it1
    var it2 = std.mem.splitScalar(u8, v2, '.'); // 把 std.mem.splitScalar(u8, v2, '.') 存入 it2
    while (true) { // 循环，直到不满足「true」
        const s1 = it1.next(); // 把 it1.下一个() 存入 s1
        const s2 = it2.next(); // 把 it2.下一个() 存入 s2
        if (s1 == null and s2 == null) break; // 若 s1 等于 null and s2 等于 null) break;
        const a = if (s1) |x| segVal(x) else 0; // 把 if (s1) 按位或 x 按位或 segVal(x) else 0 存入 数组
        const b = if (s2) |x| segVal(x) else 0; // 把 if (s2) 按位或 x 按位或 segVal(x) else 0 存入 b
        if (a < b) return -1; // 若 数组 小于 b，直接返回 减 1
        if (a > b) return 1; // 若 数组 超过 b，直接返回 1
    }
    return 0; // 返回 0
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    if (compareVersion("1.01", "1.001") != 0) return error.TestFailed; // 若 compareVersion(「1.01」, 「1.01」) 不等于 0，直接返回 error.TestFailed
    if (compareVersion("1.0", "1.0.0") != 0) return error.TestFailed; // 若 compareVersion(「1.0」, 「1.0」) 不等于 0，直接返回 error.TestFailed
    if (compareVersion("0.1", "1.1") != -1) return error.TestFailed; // 若 compareVersion(「0.1」, 「0.1」) 不等于 减 1，直接返回 error.TestFailed
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
