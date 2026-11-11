// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/108717090
// 减治策略之详解Dijkstra算法 — Zig 版（方案1）
const std = @import("std"); // 把 @import(「std」) 存入 std
const INF: i32 = 0x3f3f3f3f; // 把 0x3f3f3f3f; 写入 const INF: i32
fn dijkstraShortest(graph: []const []const [2]i32, start: usize) [8]i32 { // 定义函数/方法 dijkstraShortest
    const n = graph.len; // 把 graph.长度 存入 元素个数
    var dist: [8]i32 = undefined; // 把 undefined; 写入 var dist: [8]i32
    var visited: [8]bool = undefined; // 把 undefined; 写入 var visited: [8]bool
    for (0..n) |i| { // 让 下标 i 从 0 走到 元素个数 减一
        dist[i] = INF; // 把 INF; 写入 dist[i]
        visited[i] = false; // 把 false; 写入 visited[i]
    }
    dist[start] = 0; // 把 0; 写入 dist[start]
    while (true) { // 循环，直到不满足「true」
        var u: usize = std.math.maxInt(usize); // 把 std.math.maxInt(usize); 写入 var u: usize
        for (0..n) |i| { // 让 下标 i 从 0 走到 元素个数 减一
            if (!visited[i] and (u == std.math.maxInt(usize) or dist[i] < dist[u])) u = i;
        }
        if (u == std.math.maxInt(usize) or dist[u] == INF) break;
        visited[u] = true; // 把 true; 写入 visited[u]
        for (graph[u]) |e| { // for (graph[节点 u]) 按位或 e 按位或 {
            const v: usize = @intCast(e[0]); // 把 @intCast(e[0]); 写入 const v: usize
            if (dist[u] + e[1] < dist[v]) dist[v] = dist[u] + e[1];
        }
    }
    return dist; // 返回 dist
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    const g0 = [_][2]i32{ .{ 1, 10 }, .{ 2, 3 } }; // 把 [_][2]i32{ .{ 1, 10 }, .{ 2, 3 } } 存入 g0
    const g1 = [_][2]i32{ .{ 2, 1 }, .{ 3, 2 } }; // 把 [_][2]i32{ .{ 2, 1 }, .{ 3, 2 } } 存入 g1
    const g2 = [_][2]i32{ .{ 1, 4 }, .{ 3, 8 } }; // 把 [_][2]i32{ .{ 1, 4 }, .{ 3, 8 } } 存入 g2
    const g3 = [_][2]i32{.{ 4, 7 }}; // 把 [_][2]i32{.{ 4, 7 }} 存入 g3
    const g4 = [_][2]i32{}; // 把 [_][2]i32{} 存入 g4
    const g = [_][]const [2]i32{ &g0, &g1, &g2, &g3, &g4 };
    const d = dijkstraShortest(&g, 0); // 把 dijkstraShortest( 按位与 g, 0) 存入 d
    if (d[0] != 0 or d[1] != 7 or d[2] != 3 or d[3] != 9 or d[4] != 16) return error.TestFailed;
    std.debug.print("PASS\n", .{});
} // 全部用例通过，输出 PASS
