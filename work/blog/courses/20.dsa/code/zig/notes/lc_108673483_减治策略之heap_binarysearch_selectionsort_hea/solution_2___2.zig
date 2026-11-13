// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/108673483
// LeetCode 108673483. 减治策略 — Zig 版（方案2：快速选择求第 k 小）
const std = @import("std"); // 把 @import(「std」) 存入 std

fn selectK(a: []i32, lo: usize, hi: usize, k: usize) i32 { // 定义函数/方法 selectK
    if (lo == hi) return a[lo]; // 若 左边界 等于 右边界，直接返回 数组[左边界]
    const pivot = a[hi]; // 把 数组[右边界] 存入 pivot
    var i = lo; // 把 左边界 存入 下标 i
    var j = lo; // 把 左边界 存入 下标 j
    while (j < hi) : (j += 1) { // 循环，直到不满足「下标 j 小于 右边界) : (下标 j 累加 1」
        if (a[j] <= pivot) { // 若 数组[下标 j] 不超过 pivot
            const t = a[i]; // 把 数组[下标 i] 存入 另一字符串
            a[i] = a[j]; // 把 数组[下标 j]; 写入 a[i]
            a[j] = t; // 把 另一字符串; 写入 a[j]
            i += 1; // 下标 i累加 1
        }
    }
    const t = a[i]; // 把 数组[下标 i] 存入 另一字符串
    a[i] = a[hi]; // 把 数组[右边界]; 写入 a[i]
    a[hi] = t; // 把 另一字符串; 写入 a[hi]
    if (i == k) return a[i]; // 若 下标 i 等于 下标 k，直接返回 数组[下标 i]
    if (i > k) return selectK(a, lo, i - 1, k); // 若 下标 i 超过 下标 k，直接返回 selectK(数组, 左边界, 下标 i 减 1, 下标 k)
    return selectK(a, i + 1, hi, k); // 返回 selectK(数组, 下标 i 加 1, 右边界, 下标 k)
}

pub fn main() !void { // 程序入口：跑内嵌自测用例
    var gpa = std.heap.GeneralPurposeAllocator(.{}){}; // 把 std.堆.GeneralPurposeAllocator(.{}){} 存入 gpa
    defer _ = gpa.deinit(); // 把 gpa.deinit(); 写入 defer _
    const allocator = gpa.allocator(); // 把 gpa.allocator() 存入 allocator

    const base = [_]i32{ 3, 1, 4, 1, 5, 9, 2, 6 }; // 把 [_]i32{ 3, 1, 4, 1, 5, 9, 2, 6 } 存入 base
    const Case = struct { k: usize, want: i32 }; // 把 struct { 下标 k: usize, want: i32 } 存入 Case
    const cases = [_]Case{ // 把 [_]Case{ 存入 cases
        .{ .k = 2, .want = 2 },
        .{ .k = 3, .want = 3 },
        .{ .k = 0, .want = 1 },
        .{ .k = 7, .want = 9 },
    };
    for (cases, 0..) |c, idx| { // for (cases, 0..) 按位或 字符, idx 按位或 {
        const a = try allocator.dupe(i32, &base); // 把 try allocator.dupe(i32, 按位与 base) 存入 数组
        defer allocator.free(a); // defer allocator.free(数组);
        const got = selectK(a, 0, a.len - 1, c.k); // 把 selectK(数组, 0, 数组.长度 减 1, 字符.下标 k) 存入 got
        if (got != c.want) { // 若 got 不等于 字符.want
            std.debug.print("case {d} failed: got {d} want {d}\n", .{ idx, got, c.want }); // 打印输出
            return error.TestFailed; // 返回 error.TestFailed
        }
    }
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
