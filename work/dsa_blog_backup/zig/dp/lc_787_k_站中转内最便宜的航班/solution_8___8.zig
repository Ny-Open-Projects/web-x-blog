// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133472893
// LeetCode 787. K站中转内最便宜的航班 — Zig 版（方案8）
const std = @import("std"); // 把 @import(「std」) 存入 std
const INF: i32 = 0x3f3f3f3f; // 把 0x3f3f3f3f; 写入 const INF: i32
fn findCheapestPrice(n: usize, flights: []const [3]i32, src: usize, dst: usize, k: usize) i32 { // 定义函数/方法 findCheapestPrice
    var dist: [128]i32 = undefined; // 把 undefined; 写入 var dist: [128]i32
    for (0..n) |i| dist[i] = INF; // 让 下标 i 从 0 走到 元素个数 减一
    dist[src] = 0; // 把 0; 写入 dist[src]
    for (0..k + 1) |_| { // for (0..下标 k 加 1) 按位或 _ 按位或 {
        var nd: [128]i32 = undefined; // 把 undefined; 写入 var nd: [128]i32
        for (0..n) |i| nd[i] = dist[i]; // 让 下标 i 从 0 走到 元素个数 减一
        for (flights) |f| { // 逐个取出 flights 的元素（f）
            const u: usize = @intCast(f[0]); // 把 @intCast(f[0]); 写入 const u: usize
            const v: usize = @intCast(f[1]); // 把 @intCast(f[1]); 写入 const v: usize
            if (dist[u] != INF and dist[u] + f[2] < nd[v]) nd[v] = dist[u] + f[2];
        }
        for (0..n) |i| dist[i] = nd[i]; // 让 下标 i 从 0 走到 元素个数 减一
    }
    return if (dist[dst] == INF) -1 else dist[dst]; // 返回 if (dist[dst] 等于 INF) 减 1 else dist[dst]
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    const f = [_][3]i32{ .{ 0, 1, 100 }, .{ 1, 2, 100 }, .{ 2, 0, 100 }, .{ 1, 3, 600 }, .{ 2, 3, 200 } };
    if (findCheapestPrice(4, &f, 0, 3, 1) != 700) return error.TestFailed;
    if (findCheapestPrice(4, &f, 0, 0, 1) != 0) return error.TestFailed;
    if (findCheapestPrice(4, &f, 0, 3, 2) != 400) return error.TestFailed;
    std.debug.print("PASS\n", .{});
} // 全部用例通过，输出 PASS
