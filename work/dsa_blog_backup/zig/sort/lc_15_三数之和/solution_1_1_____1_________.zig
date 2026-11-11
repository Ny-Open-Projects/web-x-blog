// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133845474
// LeetCode 15. 三数之和 — Zig 版（方案1）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn threeSum(nums: []const i32, alloc: std.mem.Allocator, out: *std.ArrayList([3]i32)) void { // 定义函数/方法 threeSum
    const arr = alloc.dupe(i32, nums) catch unreachable; // 把 alloc.dupe(i32, 数组) catch unreachable 存入 数组
    std.sort.pdq(i32, arr, {}, std.sort.asc(i32)); // std.sort.pdq(i32, 数组, {}, std.sort.asc(i32));
    const n = arr.len; // 把 数组.长度 存入 元素个数
    for (0..n) |first| { // 让 first 从 0 走到 元素个数 减一
        if (first > 0 and arr[first] == arr[first - 1]) continue; // 若 first 超过 0 and 数组[first] 等于 数组[first 减 1]) continue;
        var third = n - 1; // 把 元素个数 减 1 存入 third
        const target = -arr[first]; // 把 减 数组[first] 存入 目标值
        var second = first + 1; // 把 first 加 1 存入 second
        while (second < n) : (second += 1) { // 循环，直到不满足「second 小于 元素个数) : (second 累加 1」
            if (second > first + 1 and arr[second] == arr[second - 1]) continue;
            while (second < third and arr[second] + arr[third] > target) third -= 1;
            if (second == third) break; // 若 second 等于 third) break;
            if (arr[second] + arr[third] == target) { // 若 数组[second] 加 数组[third] 等于 目标值
                out.append(.{ arr[first], arr[second], arr[third] }) catch unreachable; // 把 { 数组[first], 数组[second], 数组[third] } 追加到列表尾部
            }
        }
    }
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator); // 把 std.堆.ArenaAllocator.init(std.堆.page_allocator) 存入 arena
    defer arena.deinit(); // defer arena.deinit();
    const alloc = arena.allocator(); // 把 arena.allocator() 存入 alloc
    var out = std.ArrayList([3]i32).init(std.heap.page_allocator); // 把 std.ArrayList([3]i32).init(std.堆.page_allocator) 存入 out
    defer out.deinit(); // defer out.deinit();
    threeSum(&[_]i32{ -1, 0, 1, 2, -1, -4 }, alloc, &out);
    if (out.items.len != 2) return error.TestFailed; // 若 out.items.长度 不等于 2，直接返回 error.TestFailed
    if (out.items[0][0] != -1 or out.items[0][1] != -1 or out.items[0][2] != 2) return error.TestFailed;
    if (out.items[1][0] != -1 or out.items[1][1] != 0 or out.items[1][2] != 1) return error.TestFailed;
    out.clearRetainingCapacity(); // out.clearRetainingCapacity();
    threeSum(&[_]i32{ 0, 0, 0 }, alloc, &out); // threeSum( 按位与 [_]i32{ 0, 0, 0 }, alloc, 按位与 out);
    if (out.items.len != 1 or out.items[0][0] != 0) return error.TestFailed;
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
