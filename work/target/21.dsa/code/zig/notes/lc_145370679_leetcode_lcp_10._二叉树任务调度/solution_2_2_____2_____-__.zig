// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145370679
// LeetCode LCP 10. 二叉树任务调度 — Zig 版（方案2：深度优先-优化）
const std = @import("std"); // 把 @import(「std」) 存入 std

// 二叉树节点：val 为自身执行时间（f64 承载均摊的 0.5）
const TreeNode = struct {
    val: f64,
    left: ?*TreeNode = null,
    right: ?*TreeNode = null,
};

fn new_node(alloc: std.mem.Allocator, val: f64) !*TreeNode { // 新建节点
    const n = try alloc.create(TreeNode);
    n.* = .{ .val = val };
    return n;
}

// 层序数组建树，NAN 表示空节点（任务耗时恒为正，用 NAN 做哨兵安全）
fn build_tree(alloc: std.mem.Allocator, vals: []const f64) !?*TreeNode {
    if (vals.len == 0) return null;
    const root = try new_node(alloc, vals[0]);
    var queue = std.ArrayList(*TreeNode).init(alloc); // 队列里只放非空节点
    defer queue.deinit();
    try queue.append(root);
    var head: usize = 0;
    var i: usize = 1;
    while (head < queue.items.len and i < vals.len) {
        const node = queue.items[head]; // 出队一个父节点
        head += 1;
        if (i < vals.len and !std.math.isNan(vals[i])) { // 左孩子
            const child = try new_node(alloc, vals[i]);
            node.left = child;
            try queue.append(child);
        }
        i += 1;
        if (i < vals.len and !std.math.isNan(vals[i])) { // 右孩子
            const child = try new_node(alloc, vals[i]);
            node.right = child;
            try queue.append(child);
        }
        i += 1;
    }
    return root;
}

// dfs 的返回结构：sum 子树总耗时，exec 子树最小完成时间
const Dfs = struct { sum: f64, exec: f64 };

fn dfs(root: ?*TreeNode) Dfs {
    const node = root orelse return .{ .sum = 0.0, .exec = 0.0 }; // 空子树
    const left = dfs(node.left); // 左子树的总耗时与最小完成时间
    const right = dfs(node.right); // 右子树的总耗时与最小完成时间
    // 当前任务自身必须独占串行跑完；孩子任务两条机器可穿插：
    // 下界取「较慢的一侧」与「两侧工作量均分到两台机器」的较大者
    const parallel = (left.sum + right.sum) / 2.0; // 两台机器均摊左右子树总工作量（浮点）
    const exec = node.val + @max(@max(left.exec, right.exec), parallel);
    return .{ .sum = left.sum + right.sum + node.val, .exec = exec };
}

fn minimal_execution_time(root: ?*TreeNode) f64 { // 答案 = 整棵树的最小完成时间
    return dfs(root).exec;
}

pub fn main() !void { // 程序入口：跑内嵌自测用例（三个官方用例）
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();
    const alloc = arena.allocator();
    const nan = std.math.nan(f64);
    const Case = struct { vals: []const f64, want: f64 };
    const cases = [_]Case{
        .{ .vals = &[_]f64{ 47, 74, 31 }, .want = 121.0 },
        .{ .vals = &[_]f64{ 15, 21, nan, 24, nan, 27, 26 }, .want = 87.0 },
        .{ .vals = &[_]f64{ 1, 3, 2, nan, nan, 4, 4 }, .want = 7.5 },
    };
    for (cases) |case| {
        const root = try build_tree(alloc, case.vals);
        const got = minimal_execution_time(root);
        const diff = got - case.want;
        if (diff > 1e-6 or diff < -1e-6) { // 浮点比较用 1e-6 容差
            std.debug.print("FAIL got {d} want {d}\n", .{ got, case.want }); // 失败打印 FAIL
            std.process.exit(1); // 非零退出
        }
    }
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
