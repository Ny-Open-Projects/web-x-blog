// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130671359
// LeetCode 337. 打家劫舍III — Zig 版（方案1）
const std = @import("std"); // 把 @import(「std」) 存入 std
const NN: i32 = -2147483648; // 把 减 2147483648; 写入 const NN: i32
fn dfsT(vals: []const i32, i: usize) [2]i64 { // 定义函数/方法 dfsT
    if (i >= vals.len or vals[i] == NN) return .{ 0, 0 }; // 若 下标 i 不低于 vals.长度 or vals[下标 i] 等于 NN，直接返回 { 0, 0 }
    const l = dfsT(vals, 2 * i + 1); // 把 dfsT(vals, 2 乘 下标 i 加 1) 存入 左指针
    const r = dfsT(vals, 2 * i + 2); // 把 dfsT(vals, 2 乘 下标 i 加 2) 存入 右指针
    const inc: i64 = vals[i] + l[1] + r[1]; // 把 vals[下标 i] 加 左指针[1] 加 右指针[1]; 写入 const inc: i64
    const lm = @max(l[0], l[1]); // 把 @取较大值 左指针[0], 左指针[1]) 存入 lm
    const rm = @max(r[0], r[1]); // 把 @取较大值 右指针[0], 右指针[1]) 存入 rm
    return .{ inc, lm + rm }; // 返回 { inc, lm 加 rm }
}
fn robTree(vals: []const i32) i32 { // 定义函数/方法 robTree
    const r = dfsT(vals, 0); // 把 dfsT(vals, 0) 存入 右指针
    return @intCast(@max(r[0], r[1])); // 返回 @intCast(@取较大值 右指针[0], 右指针[1]))
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    if (robTree(&[_]i32{ 3, 2, 3, NN, 3, NN, 1 }) != 7) return error.TestFailed;
    if (robTree(&[_]i32{ 3, 4, 5, 1, 3, NN, 1 }) != 9) return error.TestFailed;
    if (robTree(&[_]i32{}) != 0) return error.TestFailed; // 若 robTree( 按位与 [_]i32{}) 不等于 0，直接返回 error.TestFailed
    std.debug.print("PASS\n", .{});
} // 全部用例通过，输出 PASS
