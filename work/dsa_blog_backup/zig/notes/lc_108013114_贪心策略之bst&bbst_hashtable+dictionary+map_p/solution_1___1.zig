// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/108013114
// LeetCode 108013114. 贪心策略之BST&BBST_hashtable+dictionary+map — Zig 版（贪心策略之 BST/BBST/哈希表：Kruskal 最小生成树（并查集 + 排序））
const std = @import("std"); // 把 @import(「std」) 存入 std

const Edge = struct { u: i32, v: i32, w: i32 }; // 把 struct { 节点 u: i32, 值: i32, 权重: i32 } 存入 Edge

var parent: [101]i32 = undefined; // 把 undefined; 写入 var parent: [101]i32

fn find(x: i32) i32 { // 定义函数/方法 find
    var xi = x; // 把 x 存入 xi
    if (parent[@intCast(xi)] == -1) parent[@intCast(xi)] = xi; // 若 parent[@intCast(xi)] 等于 减 1) parent[@intCast(xi)] 赋值为 xi;
    while (parent[@intCast(xi)] != xi) { // 循环，直到不满足「parent[@intCast(xi)] 不等于 xi」
        const px = parent[@intCast(xi)]; // 把 parent[@intCast(xi)] 存入 px
        parent[@intCast(xi)] = parent[@intCast(px)]; // 把 parent[@intCast(px)]; 写入 parent[@intCast(xi)]
        xi = parent[@intCast(xi)]; // 把 parent[@intCast(xi)]; 写入 xi
    }
    return xi; // 返回 xi
}

fn kruskalMst(edges: []const Edge) i32 { // 定义函数/方法 kruskalMst
    for (0..parent.len) |i| parent[i] = -1; // 逐个取出 0..parent.长度 的元素（下标 i）
    // 拷贝并按权重排序
    var buf: [64]Edge = undefined; // 把 undefined; 写入 var buf: [64]Edge
    const n = edges.len; // 把 边集.长度 存入 元素个数
    for (edges, 0..) |e, i| buf[i] = e; // 把 e; 写入 for (edges, 0..) |e, i| buf[i]
    var i: usize = 0; // 把 0; 写入 var i: usize
    while (i + 1 < n) : (i += 1) { // 循环，直到不满足「下标 i 加 1 小于 元素个数) : (下标 i 累加 1」
        var j: usize = 0; // 把 0; 写入 var j: usize
        while (j + 1 < n - i) : (j += 1) { // 循环，直到不满足「下标 j 加 1 小于 元素个数 减 下标 i) : (下标 j 累加 1」
            if (buf[j].w > buf[j + 1].w) { // 若 buf[下标 j].权重 超过 buf[下标 j 加 1].权重
                const t = buf[j]; // 把 buf[下标 j] 存入 另一字符串
                buf[j] = buf[j + 1]; // 把 buf[下标 j 加 1]; 写入 buf[j]
                buf[j + 1] = t; // 把 另一字符串; 写入 buf[j + 1]
            }
        }
    }
    var total: i32 = 0; // 把 0; 写入 var total: i32
    for (buf[0..n]) |e| { // for (buf[0..元素个数]) 按位或 e 按位或 {
        const ru = find(e.u); // 把 find(e.节点 u) 存入 ru
        const rv = find(e.v); // 把 find(e.值) 存入 rv
        if (ru != rv) { // 若 ru 不等于 rv
            parent[@intCast(ru)] = rv; // 把 rv; 写入 parent[@intCast(ru)]
            total += e.w; // 总和累加 e.权重
        }
    }
    return total; // 返回 总和
}

pub fn main() !void { // 程序入口：跑内嵌自测用例
    const e0 = [_]Edge{ .{ .u = 0, .v = 1, .w = 10 }, .{ .u = 0, .v = 2, .w = 6 }, .{ .u = 0, .v = 3, .w = 5 }, .{ .u = 1, .v = 3, .w = 15 }, .{ .u = 2, .v = 3, .w = 4 } };
    const e1 = [_]Edge{ .{ .u = 0, .v = 1, .w = 1 }, .{ .u = 1, .v = 2, .w = 2 }, .{ .u = 2, .v = 3, .w = 3 }, .{ .u = 3, .v = 4, .w = 4 } };
    const e2 = [_]Edge{ .{ .u = 0, .v = 1, .w = 2 }, .{ .u = 1, .v = 2, .w = 3 } };
    const empty = [_]Edge{}; // 把 [_]Edge{} 存入 empty
    const Case = struct { edges: []const Edge, want: i32 }; // 把 struct { 边集: []const Edge, want: i32 } 存入 Case
    const cases = [_]Case{ // 把 [_]Case{ 存入 cases
        .{ .edges = &e0, .want = 19 },
        .{ .edges = &e1, .want = 10 },
        .{ .edges = &e2, .want = 5 },
        .{ .edges = &empty, .want = 0 },
    };
    for (cases, 0..) |c, idx| { // for (cases, 0..) 按位或 字符, idx 按位或 {
        const got = kruskalMst(c.edges); // 把 kruskalMst(字符.边集) 存入 got
        if (got != c.want) { // 若 got 不等于 字符.want
            std.debug.print("case {d} failed: got {d} want {d}\n", .{ idx, got, c.want }); // 打印输出
            return error.TestFailed; // 返回 error.TestFailed
        }
    }
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
