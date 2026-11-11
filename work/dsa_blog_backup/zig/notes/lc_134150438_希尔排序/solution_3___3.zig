// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134150438
// 数据结构与算法之排序: 希尔排序 — Zig 版（方案3）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn shellSort(nums: []i32) void { // 定义函数/方法 shellSort
    const n = nums.len; // 把 数组.长度 存入 元素个数
    var gap = n / 2; // 把 元素个数 除以 2 存入 gap
    while (gap > 0) : (gap /= 2) { // 循环，直到不满足「gap 超过 0) : (gap 除以 2」
        for (gap..n) |i| { // 逐个取出 gap..元素个数 的元素（下标 i）
            const key = nums[i]; // 把 数组[下标 i] 存入 key
            var j = i; // 把 下标 i 存入 下标 j
            while (j >= gap and nums[j - gap] > key) { // 循环，直到不满足「下标 j 不低于 gap and 数组[下标 j 减 gap] 超过 key」
                nums[j] = nums[j - gap]; // 把 数组[下标 j 减 gap]; 写入 nums[j]
                j -= gap; // 下标 j累减 gap
            }
            nums[j] = key; // 把 key; 写入 nums[j]
        }
    }
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var v1 = [_]i32{ 5, 2, 4, 6, 1, 3 }; // 把 [_]i32{ 5, 2, 4, 6, 1, 3 } 存入 v1
    shellSort(&v1); // shellSort( 按位与 v1);
    for (v1, 0..) |v, i| if (v != @as(i32, @intCast(i + 1))) return error.TestFailed;
    std.debug.print("PASS\n", .{});
} // 全部用例通过，输出 PASS
