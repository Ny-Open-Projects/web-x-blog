// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133471440
// LeetCode 215. 数组中的第K个最大元素 — Zig 版（方案5）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn findKthLargest(nums: []const i32, k: usize, alloc: std.mem.Allocator) i32 { // 定义函数/方法 findKthLargest
    const a = alloc.dupe(i32, nums) catch unreachable; // 把 alloc.dupe(i32, 数组) catch unreachable 存入 数组
    const S = struct { // 把 struct { 存入 S
        fn lt(_: void, x: i32, y: i32) bool {
            return x > y;
        } // 定义函数/方法 lt
    };
    std.sort.pdq(i32, a, {}, S.lt); // std.sort.pdq(i32, 数组, {}, S.lt);
    return a[k - 1]; // 返回 数组[下标 k 减 1]
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator); // 把 std.堆.ArenaAllocator.init(std.堆.page_allocator) 存入 arena
    defer arena.deinit(); // defer arena.deinit();
    if (findKthLargest(&[_]i32{ 3, 2, 1, 5, 6, 4 }, 2, arena.allocator()) != 5) return error.TestFailed;
    if (findKthLargest(&[_]i32{ 3, 2, 3, 1, 2, 4, 5, 5, 6 }, 4, arena.allocator()) != 4) return error.TestFailed;
    if (findKthLargest(&[_]i32{1}, 1, arena.allocator()) != 1) return error.TestFailed;
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
