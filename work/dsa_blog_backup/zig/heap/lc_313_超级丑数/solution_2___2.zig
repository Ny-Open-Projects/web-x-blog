// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133547933
// LeetCode 313. 超级丑数 — Zig 版（方案2）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn nthSuperUglyNumber(n: usize, primes: []const i64, alloc: std.mem.Allocator) i64 { // 定义函数/方法 nthSuperUglyNumber
    var ugly = alloc.alloc(i64, n) catch unreachable; // 把 alloc.alloc(i64, 元素个数) catch unreachable 存入 ugly
    defer alloc.free(ugly); // defer alloc.free(ugly);
    var idx = alloc.alloc(usize, primes.len) catch unreachable; // 把 alloc.alloc(usize, primes.长度) catch unreachable 存入 idx
    defer alloc.free(idx); // defer alloc.free(idx);
    var val = alloc.alloc(i64, primes.len) catch unreachable; // 把 alloc.alloc(i64, primes.长度) catch unreachable 存入 值
    defer alloc.free(val); // defer alloc.free(值);
    ugly[0] = 1; // 把 1; 写入 ugly[0]
    for (primes, 0..) |p, k| {
        idx[k] = 0;
        val[k] = p;
    } // 把 0; 值[下标 k] 赋值为 节点; } 写入 for (primes, 0..) |p, k| { idx[k]
    var i: usize = 1; // 把 1; 写入 var i: usize
    while (i < n) : (i += 1) { // 循环，直到不满足「下标 i 小于 元素个数) : (下标 i 累加 1」
        var next: i64 = std.math.maxInt(i64); // 把 std.math.maxInt(i64); 写入 var next: i64
        for (val) |v| { // 逐个取出 值 的元素（值）
            if (v < next) next = v; // 若 值 小于 下一个) 下一个 赋值为 值;
        }
        ugly[i] = next; // 把 下一个; 写入 ugly[i]
        for (primes, 0..) |p, k| { // for (primes, 0..) 按位或 节点, 下标 k 按位或 {
            if (val[k] == next) { // 若 值[下标 k] 等于 下一个
                idx[k] += 1; // idx[k]累加 1
                val[k] = ugly[idx[k]] * p; // 把 ugly[idx[下标 k]] 乘 节点; 写入 val[k]
            }
        }
    }
    return ugly[n - 1]; // 返回 ugly[元素个数 减 1]
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator); // 把 std.堆.ArenaAllocator.init(std.堆.page_allocator) 存入 arena
    defer arena.deinit(); // defer arena.deinit();
    const alloc = arena.allocator(); // 把 arena.allocator() 存入 alloc
    if (nthSuperUglyNumber(12, &[_]i64{ 2, 7, 13, 19 }, alloc) != 32) return error.TestFailed;
    if (nthSuperUglyNumber(1, &[_]i64{ 2, 7, 13, 19 }, alloc) != 1) return error.TestFailed;
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
