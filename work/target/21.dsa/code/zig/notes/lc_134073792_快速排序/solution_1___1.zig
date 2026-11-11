// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134073792
// 数据结构与算法之排序: 快速排序 — Zig 版（方案1）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn quickSortPart(nums: []i32, lo: isize, hi: isize) void { // 定义函数/方法 quickSortPart
    if (lo >= hi) return; // 若 左边界 不低于 右边界) return;
    const pivot = nums[@intCast(@divTrunc(lo + hi, 2))]; // 把 数组[@intCast(@divTrunc(左边界 加 右边界, 2))] 存入 pivot
    var i = lo; // 把 左边界 存入 下标 i
    var j = hi; // 把 右边界 存入 下标 j
    while (i <= j) { // 循环，直到不满足「下标 i 不超过 下标 j」
        while (nums[@intCast(i)] < pivot) i += 1; // 循环，直到不满足「数组[@intCast(下标 i)] 小于 pivot) 下标 i 累加 1;」
        while (nums[@intCast(j)] > pivot) j -= 1; // 循环，直到不满足「数组[@intCast(下标 j)] 超过 pivot) 下标 j 累减 1;」
        if (i <= j) { // 若 下标 i 不超过 下标 j
            const t = nums[@intCast(i)]; // 把 数组[@intCast(下标 i)] 存入 另一字符串
            nums[@intCast(i)] = nums[@intCast(j)]; // 把 数组[@intCast(下标 j)]; 写入 nums[@intCast(i)]
            nums[@intCast(j)] = t; // 把 另一字符串; 写入 nums[@intCast(j)]
            i += 1; // 下标 i累加 1
            j -= 1; // 下标 j累减 1
        }
    }
    quickSortPart(nums, lo, j); // quickSortPart(数组, 左边界, 下标 j);
    quickSortPart(nums, i, hi); // quickSortPart(数组, 下标 i, 右边界);
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var v1 = [_]i32{ 5, 4, 3, 2, 1 }; // 把 [_]i32{ 5, 4, 3, 2, 1 } 存入 v1
    quickSortPart(&v1, 0, 4); // quickSortPart( 按位与 v1, 0, 4);
    if (v1[0] != 1 or v1[4] != 5) return error.TestFailed; // 若 v1[0] 不等于 1 or v1[4] 不等于 5，直接返回 error.TestFailed
    var v2 = [_]i32{ 3, 1, 4, 1, 5 }; // 把 [_]i32{ 3, 1, 4, 1, 5 } 存入 v2
    quickSortPart(&v2, 0, 4); // quickSortPart( 按位与 v2, 0, 4);
    if (v2[0] != 1 or v2[1] != 1 or v2[4] != 5) return error.TestFailed;
    std.debug.print("PASS\n", .{});
} // 全部用例通过，输出 PASS
