// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134191965
// 数据结构与算法之排序: 基数排序 — Zig 版（方案4）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn radixSort(nums: []i32, alloc: std.mem.Allocator) []i32 { // 定义函数/方法 radixSort
    if (nums.len == 0) return nums; // 若 数组.长度 等于 0，直接返回 数组
    var mn = nums[0]; // 把 数组[0] 存入 mn
    var mx = nums[0]; // 把 数组[0] 存入 mx
    for (nums) |v| { // 逐个取出 数组 的元素（值）
        if (v < mn) mn = v; // 若 值 小于 mn) mn 赋值为 值;
        if (v > mx) mx = v; // 若 值 超过 mx) mx 赋值为 值;
    }
    const offset: i64 = if (mn < 0) -mn else 0; // 把 if (mn 小于 0) 减 mn else 0; 写入 const offset: i64
    var adj = alloc.alloc(i64, nums.len) catch unreachable; // 把 alloc.alloc(i64, 数组.长度) catch unreachable 存入 邻接表
    var max_adj: i64 = 0; // 把 0; 写入 var max_adj: i64
    for (nums, 0..) |v, i| { // for (数组, 0..) 按位或 值, 下标 i 按位或 {
        adj[i] = @as(i64, v) + offset; // 把 @as(i64, 值) 加 offset; 写入 adj[i]
        if (adj[i] > max_adj) max_adj = adj[i]; // 若 邻接表[下标 i] 超过 max_adj) max_adj 赋值为 邻接表[下标 i];
    }
    var radix: i64 = 1; // 把 1; 写入 var radix: i64
    var tmp = alloc.alloc(i64, nums.len) catch unreachable; // 把 alloc.alloc(i64, 数组.长度) catch unreachable 存入 临时变量
    while (max_adj >= radix) { // 循环，直到不满足「max_adj 不低于 radix」
        var bucket = [_]i64{0} ** 10; // 把 [_]i64{0} 乘 乘 10 存入 bucket
        for (adj) |x| bucket[@intCast(@mod(@divTrunc(x, radix), 10))] += 1; // 逐个取出 邻接表 的元素（x）
        for (1..10) |i| bucket[i] += bucket[i - 1]; // 逐个取出 1..10 的元素（下标 i）
        var i: usize = nums.len; // 把 数组.长度; 写入 var i: usize
        while (i > 0) { // 循环，直到不满足「下标 i 超过 0」
            i -= 1; // 下标 i累减 1
            const d: usize = @intCast(@mod(@divTrunc(adj[i], radix), 10));
            bucket[d] -= 1; // bucket[d]累减 1
            tmp[@intCast(bucket[d])] = adj[i]; // 把 邻接表[下标 i]; 写入 tmp[@intCast(bucket[d])]
        }
        for (0..nums.len) |k| adj[k] = tmp[k]; // 逐个取出 0..数组.长度 的元素（下标 k）
        radix *= 10; // 把 10; 写入 radix *
    }
    const out = alloc.alloc(i32, nums.len) catch unreachable; // 把 alloc.alloc(i32, 数组.长度) catch unreachable 存入 out
    for (adj, 0..) |x, i| out[i] = @intCast(x - offset); // 把 @intCast(x 减 offset); 写入 for (adj, 0..) |x, i| out[i]
    return out; // 返回 out
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator); // 把 std.堆.ArenaAllocator.init(std.堆.page_allocator) 存入 arena
    defer arena.deinit(); // defer arena.deinit();
    var v1 = [_]i32{ 5, 4, 3, 2, 1 }; // 把 [_]i32{ 5, 4, 3, 2, 1 } 存入 v1
    const got = radixSort(&v1, arena.allocator()); // 把 radixSort( 按位与 v1, arena.allocator()) 存入 got
    for (got, 0..) |g, i| if (g != @as(i32, @intCast(i + 1))) return error.TestFailed;
    std.debug.print("PASS\n", .{});
} // 全部用例通过，输出 PASS
