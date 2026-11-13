// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133986698
// LeetCode 133. 克隆图 — Zig 版
const std = @import("std"); // 把 @import(「std」) 存入 std

const MAX_NODES = 101; // 把 101 存入 MAX_NODES
const MAX_DEGREE = 16; // 把 16 存入 MAX_DEGREE

const GNode = struct { // 把 struct { 存入 GNode
    val: i32 = 0,
    ncount: usize = 0,
    neighbors: [MAX_DEGREE]*GNode = undefined,
};

fn newNode(allocator: std.mem.Allocator, val: i32) !*GNode { // 定义函数/方法 newNode
    const n = try allocator.create(GNode); // 把 try allocator.create(GNode) 存入 元素个数
    n.* = .{ .val = val }; // 把 { .值 赋值为 值 }; 写入 n.*
    return n; // 返回 元素个数
}

// visited：数组模拟 Map<*GNode, *GNode>（指针线性查找，测试规模小）
const VMap = struct { // 把 struct { 存入 VMap
    orig: [MAX_NODES]*GNode = undefined,
    copy: [MAX_NODES]*GNode = undefined,
    len: usize = 0,

    fn get(self: *const VMap, o: *GNode) ?*GNode { // 定义函数/方法 get
        var i: usize = 0; // 把 0; 写入 var i: usize
        while (i < self.len) : (i += 1) { // 循环，直到不满足「下标 i 小于 self.长度) : (下标 i 累加 1」
            if (self.orig[i] == o) return self.copy[i]; // 若 self.orig[下标 i] 等于 o，直接返回 self.copy[下标 i]
        }
        return null; // 返回 null
    }

    fn put(self: *VMap, o: *GNode, c: *GNode) void { // 定义函数/方法 put
        self.orig[self.len] = o; // 把 o; 写入 self.orig[self.len]
        self.copy[self.len] = c; // 把 字符; 写入 self.copy[self.len]
        self.len += 1; // self.len累加 1
    }
};

// 方案3（DFS 递归，visited 以节点对象为键）
fn dfsClone(allocator: std.mem.Allocator, n: *GNode, visited: *VMap) anyerror!*GNode { // 定义函数/方法 dfsClone
    if (visited.get(n)) |hit| return hit; // 若 已访问集合 查找 元素个数)) 按位或 hit 按位或 return hit;
    const clone = try newNode(allocator, n.val); // 把 try newNode(allocator, 元素个数.值) 存入 clone
    visited.put(n, clone); // 已访问集合.put(元素个数, clone);
    var i: usize = 0; // 把 0; 写入 var i: usize
    while (i < n.ncount) : (i += 1) { // 循环，直到不满足「下标 i 小于 元素个数.ncount) : (下标 i 累加 1」
        clone.neighbors[clone.ncount] = try dfsClone(allocator, n.neighbors[i], visited);
        clone.ncount += 1; // clone.ncount累加 1
    }
    return clone; // 返回 clone
}

fn cloneGraph(allocator: std.mem.Allocator, node: ?*GNode) !?*GNode { // 定义函数/方法 cloneGraph
    const root = node orelse return null; // 把 节点 orelse return null 存入 根节点
    var visited = VMap{}; // 把 VMap{} 存入 已访问集合
    return try dfsClone(allocator, root, &visited); // 返回 try dfsClone(allocator, 根节点, 按位与 已访问集合)
}

fn buildGraph(allocator: std.mem.Allocator, adj: []const []const i32) !*GNode { // 定义函数/方法 buildGraph
    var nodes: [MAX_NODES]*GNode = undefined; // 把 undefined; 写入 var nodes: [MAX_NODES]*GNode
    var i: usize = 1; // 把 1; 写入 var i: usize
    while (i <= adj.len) : (i += 1) { // 循环，直到不满足「下标 i 不超过 邻接表.长度) : (下标 i 累加 1」
        nodes[i] = try newNode(allocator, @intCast(i)); // 把 try newNode(allocator, @intCast(下标 i)); 写入 nodes[i]
    }
    for (adj, 0..) |nbrs, idx| { // for (邻接表, 0..) 按位或 nbrs, idx 按位或 {
        for (nbrs) |nb| { // 逐个取出 nbrs 的元素（nb）
            const dst = nodes[idx + 1]; // 把 nodes[idx 加 1] 存入 dst
            dst.neighbors[dst.ncount] = nodes[@intCast(nb)]; // 把 nodes[@intCast(nb)]; 写入 dst.neighbors[dst.ncount]
            dst.ncount += 1; // dst.ncount累加 1
        }
    }
    return nodes[1]; // 返回 nodes[1]
}

// 收集签名：每个节点的邻居值列表（排序后），按节点 val 索引；count == -1 表示未访问
const Sig = struct { // 把 struct { 存入 Sig
    count: i32 = -1,
    vals: [MAX_DEGREE]i32 = undefined,
};

fn signature(node: *GNode, vis: *[MAX_NODES]Sig) void { // 定义函数/方法 signature
    const vi: usize = @intCast(node.val); // 把 @intCast(节点.值); 写入 const vi: usize
    vis[vi].count = @intCast(node.ncount); // 把 @intCast(节点.ncount); 写入 计数
    var i: usize = 0; // 把 0; 写入 var i: usize
    while (i < node.ncount) : (i += 1) { // 循环，直到不满足「下标 i 小于 节点.ncount) : (下标 i 累加 1」
        vis[vi].vals[i] = node.neighbors[i].val; // 把 节点.neighbors[下标 i].值; 写入 vis[vi].vals[i]
    }
    // 插入排序
    var a: usize = 1; // 把 1; 写入 var a: usize
    while (a < node.ncount) : (a += 1) { // 循环，直到不满足「数组 小于 节点.ncount) : (数组 累加 1」
        const key = vis[vi].vals[a]; // 把 vis[vi].vals[数组] 存入 key
        var j: usize = a; // 把 数组; 写入 var j: usize
        while (j > 0 and vis[vi].vals[j - 1] > key) : (j -= 1) {
            vis[vi].vals[j] = vis[vi].vals[j - 1]; // 把 vis[vi].vals[下标 j 减 1]; 写入 vis[vi].vals[j]
        }
        vis[vi].vals[j] = key; // 把 key; 写入 vis[vi].vals[j]
    }
    i = 0; // 把 0; 写入 下标 i
    while (i < node.ncount) : (i += 1) { // 循环，直到不满足「下标 i 小于 节点.ncount) : (下标 i 累加 1」
        if (vis[@intCast(node.neighbors[i].val)].count == -1) { // 若 vis[@intCast(节点.neighbors[下标 i].值)].计数 等于 减 1
            signature(node.neighbors[i], vis); // signature(节点.neighbors[下标 i], vis);
        }
    }
}

pub fn main() !void { // 程序入口：跑内嵌自测用例
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator); // 把 std.堆.ArenaAllocator.init(std.堆.page_allocator) 存入 arena
    defer arena.deinit(); // defer arena.deinit();
    const allocator = arena.allocator(); // 把 arena.allocator() 存入 allocator

    const adj = [_][]const i32{ &.{ 2, 4 }, &.{ 1, 3 }, &.{ 2, 4 }, &.{ 1, 3 } };
    const root = try buildGraph(allocator, &adj); // 把 try buildGraph(allocator, 按位与 邻接表) 存入 根节点
    const cloned = (try cloneGraph(allocator, root)).?; // 把 (try cloneGraph(allocator, 根节点)).? 存入 cloned
    if (cloned == root) return error.NotDeepCopy; // not a deep copy (same object)

    var vis: [MAX_NODES]Sig = [_]Sig{.{}} ** MAX_NODES; // 把 [_]Sig{.{}} 乘 乘 MAX_NODES; 写入 var vis: [MAX_NODES]Sig
    signature(cloned, &vis); // signature(cloned, 按位与 vis);
    const expected = [_][2]i32{ .{ 2, 4 }, .{ 1, 3 }, .{ 2, 4 }, .{ 1, 3 } };
    var k: usize = 1; // 把 1; 写入 var k: usize
    while (k <= 4) : (k += 1) { // 循环，直到不满足「下标 k 不超过 4) : (下标 k 累加 1」
        if (vis[k].count != 2) return error.SignatureMismatch; // 若 vis[下标 k].计数 不等于 2，直接返回 error.SignatureMismatch
        var i: usize = 0; // 把 0; 写入 var i: usize
        while (i < 2) : (i += 1) { // 循环，直到不满足「下标 i 小于 2) : (下标 i 累加 1」
            if (vis[k].vals[i] != expected[k - 1][i]) return error.SignatureMismatch;
        }
    }
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
