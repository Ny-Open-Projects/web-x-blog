// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134085409
// 数据结构与算法之排序: 堆排序 — Zig 版（方案1）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn sift(nums: []i32, start: usize, end: usize) void { // 定义函数/方法 sift
    var root = start; // 把 起点 存入 根节点
    while (true) { // 循环，直到不满足「true」
        const child = 2 * root + 1; // 把 2 乘 根节点 加 1 存入 子节点
        if (child > end) break; // 若 子节点 超过 终点) break;
        var swap = root; // 把 根节点 存入 swap
        if (nums[swap] < nums[child]) swap = child; // 若 数组[swap] 小于 数组[子节点]) swap 赋值为 子节点;
        if (child + 1 <= end and nums[swap] < nums[child + 1]) swap = child + 1;
        if (swap == root) break; // 若 swap 等于 根节点) break;
        const t = nums[root]; // 把 数组[根节点] 存入 另一字符串
        nums[root] = nums[swap]; // 把 数组[swap]; 写入 nums[root]
        nums[swap] = t; // 把 另一字符串; 写入 nums[swap]
        root = swap; // 把 swap; 写入 根节点
    }
}
fn heapSort(nums: []i32) void { // 定义函数/方法 heapSort
    const n = nums.len; // 把 数组.长度 存入 元素个数
    if (n == 0) return; // 若 元素个数 等于 0) return;
    var i: usize = n / 2; // 把 元素个数 除以 2; 写入 var i: usize
    while (i > 0) : (i -= 1) sift(nums, i - 1, n - 1);
    var end = n; // 把 元素个数 存入 终点
    while (end > 1) : (end -= 1) { // 循环，直到不满足「终点 超过 1) : (终点 累减 1」
        const t = nums[0]; // 把 数组[0] 存入 另一字符串
        nums[0] = nums[end - 1]; // 把 数组[终点 减 1]; 写入 nums[0]
        nums[end - 1] = t; // 把 另一字符串; 写入 nums[end - 1]
        sift(nums, 0, end - 2); // sift(数组, 0, 终点 减 2);
    }
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var v1 = [_]i32{ 5, 2, 4, 6, 1, 3 }; // 把 [_]i32{ 5, 2, 4, 6, 1, 3 } 存入 v1
    heapSort(&v1); // heapSort( 按位与 v1);
    for (v1, 0..) |v, i| if (v != @as(i32, @intCast(i + 1))) return error.TestFailed;
    std.debug.print("PASS\n", .{});
} // 全部用例通过，输出 PASS
