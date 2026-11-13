// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/113548046
// 图搜索之BFS详解 — Zig 版（方案1）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn bfsOrder(graph: []const []const i32, start: usize, out: *std.ArrayList(i32)) void { // 定义函数/方法 bfsOrder
    const n = graph.len; // 把 graph.长度 存入 元素个数
    var visited: [64]bool = undefined; // 把 undefined; 写入 var visited: [64]bool
    for (0..n) |i| visited[i] = false; // 让 下标 i 从 0 走到 元素个数 减一
    var queue: [64]usize = undefined; // 把 undefined; 写入 var queue: [64]usize
    var head: usize = 0; // 把 0; 写入 var head: usize
    var tail: usize = 0; // 把 0; 写入 var tail: usize
    visited[start] = true; // 把 true; 写入 visited[start]
    queue[tail] = start; // 把 起点; 写入 queue[tail]
    tail += 1; // 尾节点累加 1
    while (head < tail) { // 循环，直到不满足「头节点 小于 尾节点」
        const c = queue[head]; // 把 队列[头节点] 存入 字符
        head += 1; // 头节点累加 1
        out.append(@intCast(c)) catch unreachable; // 把 @intCast(字符 追加到列表尾部
        for (graph[c]) |nx| { // for (graph[字符]) 按位或 nx 按位或 {
            const u: usize = @intCast(nx); // 把 @intCast(nx); 写入 const u: usize
            if (!visited[u]) { // 若 取反 已访问集合[节点 u]
                visited[u] = true; // 把 true; 写入 visited[u]
                queue[tail] = u; // 把 节点 u; 写入 queue[tail]
                tail += 1; // 尾节点累加 1
            }
        }
    }
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var out = std.ArrayList(i32).init(std.heap.page_allocator); // 把 std.ArrayList(i32).init(std.堆.page_allocator) 存入 out
    defer out.deinit(); // defer out.deinit();
    const g0 = [_]i32{ 1, 2 }; // 把 [_]i32{ 1, 2 } 存入 g0
    const g1 = [_]i32{ 3, 4 }; // 把 [_]i32{ 3, 4 } 存入 g1
    const g2 = [_]i32{5}; // 把 [_]i32{5} 存入 g2
    const g3 = [_]i32{}; // 把 [_]i32{} 存入 g3
    const g4 = [_]i32{}; // 把 [_]i32{} 存入 g4
    const g5 = [_]i32{}; // 把 [_]i32{} 存入 g5
    const g = [_][]const i32{ &g0, &g1, &g2, &g3, &g4, &g5 };
    bfsOrder(&g, 0, &out); // bfsOrder( 按位与 g, 0, 按位与 out);
    for (out.items, 0..) |v, i| if (v != @as(i32, @intCast(i))) return error.TestFailed;
    std.debug.print("PASS\n", .{});
} // 全部用例通过，输出 PASS
