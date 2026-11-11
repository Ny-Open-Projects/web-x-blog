// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135003383
// LeetCode 164. 最大间距 — Zig 版（方案5）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn maximumGap(nums: []const i32, alloc: std.mem.Allocator) i32 { // 定义函数/方法 maximumGap
    const n = nums.len; // 把 数组.长度 存入 元素个数
    if (n < 2) return 0; // 若 元素个数 小于 2，直接返回 0
    var min_val = nums[0]; // 把 数组[0] 存入 min_val
    var max_val = nums[0]; // 把 数组[0] 存入 max_val
    for (nums) |x| { // 逐个取出 数组 的元素（x）
        if (x < min_val) min_val = x; // 若 x 小于 min_val) min_val 赋值为 x;
        if (x > max_val) max_val = x; // 若 x 超过 max_val) max_val 赋值为 x;
    }
    if (min_val == max_val) return 0; // 若 min_val 等于 max_val，直接返回 0
    var d = @divTrunc(max_val - min_val, @as(i32, @intCast(n)) - 1);
    if (d < 1) d = 1; // 若 d 小于 1) d 赋值为 1;
    const bucket_size: usize = @intCast(@divTrunc(max_val - min_val, d) + 1);
    const buckets = alloc.alloc([2]i32, bucket_size) catch unreachable;
    for (buckets) |*b| b.* = .{ -1, -1 }; // 把 { 减 1, 减 1 }; 写入 for (buckets) |*b| b.*
    for (nums) |x| { // 逐个取出 数组 的元素（x）
        const idx: usize = @intCast(@divTrunc(x - min_val, d)); // 把 @intCast(@divTrunc(x 减 min_val, d)); 写入 const idx: usize
        if (buckets[idx][0] == -1) { // 若 buckets[idx][0] 等于 减 1
            buckets[idx] = .{ x, x }; // 把 { x, x }; 写入 buckets[idx]
        } else { // 否则
            if (x < buckets[idx][0]) buckets[idx][0] = x; // 若 x 小于 buckets[idx][0]) buckets[idx][0] 赋值为 x;
            if (x > buckets[idx][1]) buckets[idx][1] = x; // 若 x 超过 buckets[idx][1]) buckets[idx][1] 赋值为 x;
        }
    }
    var ans: i32 = 0; // 把 0; 写入 var ans: i32
    var prev_max: i32 = -1; // 把 减 1; 写入 var prev_max: i32
    for (buckets) |b| { // 逐个取出 buckets 的元素（b）
        if (b[0] == -1) continue; // 若 b[0] 等于 减 1) continue;
        if (prev_max != -1 and b[0] - prev_max > ans) ans = b[0] - prev_max;
        prev_max = b[1]; // 把 b[1]; 写入 prev_max
    }
    return ans; // 返回 答案
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator); // 把 std.堆.ArenaAllocator.init(std.堆.page_allocator) 存入 arena
    defer arena.deinit(); // defer arena.deinit();
    const alloc = arena.allocator(); // 把 arena.allocator() 存入 alloc
    if (maximumGap(&[_]i32{ 1, 2, 3 }, alloc) != 1) return error.TestFailed;
    if (maximumGap(&[_]i32{ 3, 6, 9, 1 }, alloc) != 3) return error.TestFailed;
    if (maximumGap(&[_]i32{10}, alloc) != 0) return error.TestFailed;
    if (maximumGap(&[_]i32{}, alloc) != 0) return error.TestFailed;
    if (maximumGap(&[_]i32{ 1, 10000000 }, alloc) != 9999999) return error.TestFailed;
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
