// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/113764246
// 图搜索之DFS详解 — Zig 版（方案1）
const std = @import("std"); // 把 @import(「std」) 存入 std
const G = struct { // 把 struct { 存入 G
    graph: []const []const i32,
    visited: [64]bool,
    order: std.ArrayList(i32),
};
fn dfsGo(g: *G, c: usize) void { // 定义函数/方法 dfsGo
    g.visited[c] = true; // 把 true; 写入 g.visited[c]
    g.order.append(@intCast(c)) catch unreachable; // 把 @intCast(字符 追加到列表尾部
    for (g.graph[c]) |nx| { // for (g.graph[字符]) 按位或 nx 按位或 {
        const u: usize = @intCast(nx); // 把 @intCast(nx); 写入 const u: usize
        if (!g.visited[u]) dfsGo(g, u); // 若 取反 g.已访问集合[节点 u]) dfsGo(g, 节点 u);
    }
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator); // 把 std.堆.ArenaAllocator.init(std.堆.page_allocator) 存入 arena
    defer arena.deinit(); // defer arena.deinit();
    const g0 = [_]i32{ 1, 2 }; // 把 [_]i32{ 1, 2 } 存入 g0
    const g1 = [_]i32{ 3, 4 }; // 把 [_]i32{ 3, 4 } 存入 g1
    const g2 = [_]i32{5}; // 把 [_]i32{5} 存入 g2
    const g3 = [_]i32{}; // 把 [_]i32{} 存入 g3
    const g4 = [_]i32{}; // 把 [_]i32{} 存入 g4
    const g5 = [_]i32{}; // 把 [_]i32{} 存入 g5
    const graph = [_][]const i32{ &g0, &g1, &g2, &g3, &g4, &g5 };
    var g = G{ .graph = &graph, .visited = undefined, .order = std.ArrayList(i32).init(std.heap.page_allocator) };
    defer g.order.deinit(); // defer g.order.deinit();
    for (0..6) |i| g.visited[i] = false; // 让 下标 i 从 0 走到 6 减一
    dfsGo(&g, 0); // dfsGo( 按位与 g, 0);
    const want = [_]i32{ 0, 1, 3, 4, 2, 5 }; // 把 [_]i32{ 0, 1, 3, 4, 2, 5 } 存入 want
    for (want, 0..) |w, i| if (g.order.items[i] != w) return error.TestFailed;
    std.debug.print("PASS\n", .{});
} // 全部用例通过，输出 PASS
