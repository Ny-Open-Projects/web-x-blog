// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133894317
// LeetCode 18. 四数之和 — Zig 版（方案2）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn fourSum(nums: []const i32, target: i32, alloc: std.mem.Allocator, out: *std.ArrayList([4]i32)) void { // 定义函数/方法 fourSum
    const arr = alloc.dupe(i32, nums) catch unreachable; // 把 alloc.dupe(i32, 数组) catch unreachable 存入 数组
    std.sort.pdq(i32, arr, {}, std.sort.asc(i32)); // std.sort.pdq(i32, 数组, {}, std.sort.asc(i32));
    const n = arr.len; // 把 数组.长度 存入 元素个数
    for (0..n) |i| { // 让 下标 i 从 0 走到 元素个数 减一
        if (i > 0 and arr[i] == arr[i - 1]) continue; // 若 下标 i 超过 0 and 数组[下标 i] 等于 数组[下标 i 减 1]) continue;
        for (i + 1..n) |j| { // for (下标 i 加 1..元素个数) 按位或 下标 j 按位或 {
            if (j > i + 1 and arr[j] == arr[j - 1]) continue; // 若 下标 j 超过 下标 i 加 1 and 数组[下标 j] 等于 数组[下标 j 减 1]) continue;
            var left = j + 1; // 把 下标 j 加 1 存入 左边界
            var right = n - 1; // 把 元素个数 减 1 存入 右边界
            while (left < right) { // 循环，直到不满足「左边界 小于 右边界」
                const s = @as(i64, arr[i]) + arr[j] + arr[left] + arr[right]; // 把 @as(i64, 数组[下标 i]) 加 数组[下标 j] 加 数组[左边界] 加 数组[右边界] 存入 字符串
                if (s == target) { // 若 字符串 等于 目标值
                    out.append(.{ arr[i], arr[j], arr[left], arr[right] }) catch unreachable; // 把 { 数组[下标 i], 数组[下标 j], 数组[左边界], 数组[右边界] } 追加到列表尾部
                    left += 1; // 左边界累加 1
                    right -= 1; // 右边界累减 1
                    while (left < right and arr[left] == arr[left - 1]) left += 1; // 循环，直到不满足「左边界 小于 右边界 and 数组[左边界] 等于 数组[左边界 减 1]) 左边界 累加 1;」
                    while (left < right and arr[right] == arr[right + 1]) right -= 1; // 循环，直到不满足「左边界 小于 右边界 and 数组[右边界] 等于 数组[右边界 加 1]) 右边界 累减 1;」
                } else if (s < target) left += 1 // 否则，若 字符串 小于 目标值) 左边界 累加 1
                else right -= 1; // 否则
            }
        }
    }
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator); // 把 std.堆.ArenaAllocator.init(std.堆.page_allocator) 存入 arena
    defer arena.deinit(); // defer arena.deinit();
    var out = std.ArrayList([4]i32).init(std.heap.page_allocator); // 把 std.ArrayList([4]i32).init(std.堆.page_allocator) 存入 out
    defer out.deinit(); // defer out.deinit();
    fourSum(&[_]i32{ 1, 0, -1, 0, -2, 2 }, 0, arena.allocator(), &out);
    if (out.items.len != 3) return error.TestFailed; // 若 out.items.长度 不等于 3，直接返回 error.TestFailed
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
