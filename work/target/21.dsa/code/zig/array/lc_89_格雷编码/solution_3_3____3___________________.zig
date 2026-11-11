// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134866839
// LeetCode 89. 格雷编码 — Zig 版（方案3）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn grayCode(n: i32, out: []i32) usize { // 定义函数/方法 grayCode
    const m: usize = @as(usize, 1) << @intCast(n); // 把 @as(usize, 1) 小于 小于 @intCast(元素个数); 写入 const m: usize
    for (0..m) |i| out[i] = @intCast(i ^ (i >> 1)); // 让 下标 i 从 0 走到 映射表 减一
    return m; // 返回 映射表
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var out: [4096]i32 = undefined; // 把 undefined; 写入 var out: [4096]i32
    const n2 = grayCode(2, &out); // 把 grayCode(2, 按位与 out) 存入 n2
    if (n2 != 4 or out[0] != 0 or out[1] != 1 or out[2] != 3 or out[3] != 2) return error.TestFailed;
    const n1 = grayCode(1, &out); // 把 grayCode(1, 按位与 out) 存入 n1
    if (n1 != 2 or out[0] != 0 or out[1] != 1) return error.TestFailed;
    const n3 = grayCode(3, &out); // 把 grayCode(3, 按位与 out) 存入 n3
    if (n3 != 8) return error.TestFailed; // 若 n3 不等于 8，直接返回 error.TestFailed
    std.debug.print("PASS\n", .{});
} // 全部用例通过，输出 PASS
