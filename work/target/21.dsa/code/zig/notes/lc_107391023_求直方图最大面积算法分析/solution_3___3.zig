// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107391023
// 求直方图最大面积算法分析 — Zig 版（方案3）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn getResult(h: []const i32) i32 { // 定义函数/方法 getResult
    var st: [4096]usize = undefined; // 把 undefined; 写入 var st: [4096]usize
    var top: usize = 0; // 把 0; 写入 var top: usize
    var best: i32 = 0; // 把 0; 写入 var best: i32
    for (0..h.len + 1) |i| { // for (0..h.长度 加 1) 按位或 下标 i 按位或 {
        const cur = if (i < h.len) h[i] else 0; // 把 if (下标 i 小于 h.长度) h[下标 i] else 0 存入 当前值
        while (top > 0 and h[st[top - 1]] >= cur) { // 循环，直到不满足「top 超过 0 and h[st[top 减 1]] 不低于 当前值」
            top -= 1; // top累减 1
            const t = st[top]; // 把 st[top] 存入 另一字符串
            const left: i64 = if (top > 0) @intCast(st[top - 1]) else -1;
            const width: i64 = @as(i64, @intCast(i)) - left - 1; // 把 @as(i64, @intCast(下标 i)) 减 左边界 减 1; 写入 const width: i64
            const area: i32 = @intCast(@as(i64, h[t]) * width); // 把 @intCast(@as(i64, h[另一字符串]) 乘 width); 写入 const area: i32
            if (area > best) best = area; // 若 area 超过 当前最优) 当前最优 赋值为 area;
        }
        st[top] = i; // 把 下标 i; 写入 st[top]
        top += 1; // top累加 1
    }
    return best; // 返回 当前最优
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    if (getResult(&[_]i32{ 0, 2, 3, 3, 3, 2, 0 }) != 10) return error.TestFailed;
    if (getResult(&[_]i32{ 0, 2, 1, 5, 6, 2, 3, 0 }) != 10) return error.TestFailed;
    std.debug.print("PASS\n", .{});
} // 全部用例通过，输出 PASS
