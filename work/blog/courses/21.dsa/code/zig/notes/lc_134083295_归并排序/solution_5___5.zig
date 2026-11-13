// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134083295
// 数据结构与算法之排序: 归并排序 — Zig 版（方案5）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn mergeSort(nums: []i32, tmp: []i32, lo: usize, hi: usize) void { // 定义函数/方法 mergeSort
    if (lo >= hi) return; // 若 左边界 不低于 右边界) return;
    const mid = (lo + hi) / 2; // 把 (左边界 加 右边界) 除以 2 存入 中点
    mergeSort(nums, tmp, lo, mid); // mergeSort(数组, 临时变量, 左边界, 中点);
    mergeSort(nums, tmp, mid + 1, hi); // mergeSort(数组, 临时变量, 中点 加 1, 右边界);
    var i = lo; // 把 左边界 存入 下标 i
    var j = mid + 1; // 把 中点 加 1 存入 下标 j
    var k: usize = 0; // 把 0; 写入 var k: usize
    while (i <= mid and j <= hi) { // 循环，直到不满足「下标 i 不超过 中点 and 下标 j 不超过 右边界」
        if (nums[i] <= nums[j]) { // 若 数组[下标 i] 不超过 数组[下标 j]
            tmp[k] = nums[i]; // 把 数组[下标 i]; 写入 tmp[k]
            i += 1; // 下标 i累加 1
        } else { // 否则
            tmp[k] = nums[j]; // 把 数组[下标 j]; 写入 tmp[k]
            j += 1; // 下标 j累加 1
        }
        k += 1; // 下标 k累加 1
    }
    while (i <= mid) { // 循环，直到不满足「下标 i 不超过 中点」
        tmp[k] = nums[i]; // 把 数组[下标 i]; 写入 tmp[k]
        i += 1; // 下标 i累加 1
        k += 1; // 下标 k累加 1
    }
    while (j <= hi) { // 循环，直到不满足「下标 j 不超过 右边界」
        tmp[k] = nums[j]; // 把 数组[下标 j]; 写入 tmp[k]
        j += 1; // 下标 j累加 1
        k += 1; // 下标 k累加 1
    }
    for (0..k) |x| nums[lo + x] = tmp[x]; // 让 x 从 0 走到 下标 k 减一
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var v1 = [_]i32{ 5, 4, 3, 2, 1 }; // 把 [_]i32{ 5, 4, 3, 2, 1 } 存入 v1
    var tmp: [8]i32 = undefined; // 把 undefined; 写入 var tmp: [8]i32
    mergeSort(&v1, &tmp, 0, 4); // mergeSort( 按位与 v1, 按位与 临时变量, 0, 4);
    if (v1[0] != 1 or v1[4] != 5) return error.TestFailed; // 若 v1[0] 不等于 1 or v1[4] 不等于 5，直接返回 error.TestFailed
    std.debug.print("PASS\n", .{});
} // 全部用例通过，输出 PASS
