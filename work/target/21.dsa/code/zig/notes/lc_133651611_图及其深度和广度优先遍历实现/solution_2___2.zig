// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133651611
// LeetCode 133651611. 图及其深度和广度优先遍历实现 — Zig 版（方案2）
const std = @import("std"); // 把 @import(「std」) 存入 std

const MAXV = 16; // 把 16 存入 MAXV
const MAXDEG = 8; // 把 8 存入 MAXDEG

const Graph = struct { // 把 struct { 存入 Graph
    adj: [MAXV][MAXDEG]i32 = undefined,
    deg: [MAXV]usize = [_]usize{0} ** MAXV,

    fn addEdge(self: *Graph, from: usize, to: usize) void { // 定义函数/方法 addEdge
        self.adj[from][self.deg[from]] = @intCast(to); // 把 @intCast(to); 写入 self.adj[from][self.deg[from]]
        self.deg[from] += 1; // self.deg[from]累加 1
        self.adj[to][self.deg[to]] = @intCast(from); // 把 @intCast(from); 写入 self.adj[to][self.deg[to]]
        self.deg[to] += 1; // self.deg[to]累加 1
    }

    fn dfs(self: *const Graph, start: usize, out: []i32) usize { // 定义函数/方法 dfs
        var visited = [_]bool{false} ** MAXV; // 把 [_]bool{false} 乘 乘 MAXV 存入 已访问集合
        var len: usize = 0; // 把 0; 写入 var len: usize
        self.dfsHelper(start, &visited, out, &len); // self.dfsHelper(起点, 按位与 已访问集合, out, 按位与 长度);
        return len; // 返回 长度
    }

    fn dfsHelper(self: *const Graph, node: usize, visited: *[MAXV]bool, out: []i32, len: *usize) void { // 定义函数/方法 dfsHelper
        if (visited[node]) return; // 若 已访问集合[节点]) return;
        visited[node] = true; // 把 true; 写入 visited[node]
        out[len.*] = @intCast(node); // 把 @intCast(节点); 写入 out[len.*]
        len.* += 1; // 把 1; 写入 len.* +
        var i: usize = 0; // 把 0; 写入 var i: usize
        while (i < self.deg[node]) : (i += 1) { // 循环，直到不满足「下标 i 小于 self.deg[节点]) : (下标 i 累加 1」
            self.dfsHelper(@intCast(self.adj[node][i]), visited, out, len);
        }
    }

    fn bfs(self: *const Graph, start: usize, out: []i32) usize { // 定义函数/方法 bfs
        var visited = [_]bool{false} ** MAXV; // 把 [_]bool{false} 乘 乘 MAXV 存入 已访问集合
        var queue: [MAXV]usize = undefined; // 把 undefined; 写入 var queue: [MAXV]usize
        var head: usize = 0; // 把 0; 写入 var head: usize
        var tail: usize = 0; // 把 0; 写入 var tail: usize
        var len: usize = 0; // 把 0; 写入 var len: usize
        queue[tail] = start; // 把 起点; 写入 queue[tail]
        tail += 1; // 尾节点累加 1
        visited[start] = true; // 把 true; 写入 visited[start]
        while (head < tail) { // 循环，直到不满足「头节点 小于 尾节点」
            const node = queue[head]; // 把 队列[头节点] 存入 节点
            head += 1; // 头节点累加 1
            out[len] = @intCast(node); // 把 @intCast(节点); 写入 out[len]
            len += 1; // 长度累加 1
            var i: usize = 0; // 把 0; 写入 var i: usize
            while (i < self.deg[node]) : (i += 1) { // 循环，直到不满足「下标 i 小于 self.deg[节点]) : (下标 i 累加 1」
                const nb: usize = @intCast(self.adj[node][i]); // 把 @intCast(self.邻接表[节点][下标 i]); 写入 const nb: usize
                if (!visited[nb]) { // 若 取反 已访问集合[nb]
                    visited[nb] = true; // 把 true; 写入 visited[nb]
                    queue[tail] = nb; // 把 nb; 写入 queue[tail]
                    tail += 1; // 尾节点累加 1
                }
            }
        }
        return len; // 返回 长度
    }
};

fn eq(a: []const i32, b: []const i32) bool { // 定义函数/方法 eq
    return std.mem.eql(i32, a, b); // 返回 std.mem.eql(i32, 数组, b)
}

pub fn main() !void { // 程序入口：跑内嵌自测用例
    // case 1: 方形图 0-1-3-2-0
    var g1 = Graph{}; // 把 Graph{} 存入 g1
    g1.addEdge(0, 1); // g1.addEdge(0, 1);
    g1.addEdge(0, 2); // g1.addEdge(0, 2);
    g1.addEdge(1, 3); // g1.addEdge(1, 3);
    g1.addEdge(2, 3); // g1.addEdge(2, 3);

    var got: [8]i32 = undefined; // 把 undefined; 写入 var got: [8]i32
    const want1 = [_]i32{ 0, 1, 3, 2 }; // 把 [_]i32{ 0, 1, 3, 2 } 存入 want1
    if (g1.dfs(0, &got) != 4 or !eq(got[0..4], &want1)) return error.TestFailed;
    const want2 = [_]i32{ 0, 1, 2, 3 }; // 把 [_]i32{ 0, 1, 2, 3 } 存入 want2
    if (g1.bfs(0, &got) != 4 or !eq(got[0..4], &want2)) return error.TestFailed;

    // case 2: 从另一节点出发
    const want3 = [_]i32{ 2, 0, 1, 3 }; // 把 [_]i32{ 2, 0, 1, 3 } 存入 want3
    if (g1.dfs(2, &got) != 4 or !eq(got[0..4], &want3)) return error.TestFailed;
    const want4 = [_]i32{ 2, 0, 3, 1 }; // 把 [_]i32{ 2, 0, 3, 1 } 存入 want4
    if (g1.bfs(2, &got) != 4 or !eq(got[0..4], &want4)) return error.TestFailed;

    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
