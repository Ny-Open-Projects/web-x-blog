// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133471440
// LeetCode 215. 数组中的第K个最大元素 — Zig 版（方案7）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn quickselect(a: []i32, l: usize, r: usize, k: usize) void { // 定义函数/方法 quickselect
    if (l >= r) return; // 若 左指针 不低于 右指针) return;
    var i = l; // 把 左指针 存入 下标 i
    var j = r; // 把 右指针 存入 下标 j
    const pivot = a[(l + r) / 2]; // 把 数组[(左指针 加 右指针) 除以 2] 存入 pivot
    while (i <= j) { // 循环，直到不满足「下标 i 不超过 下标 j」
        while (a[i] > pivot) i += 1; // 循环，直到不满足「数组[下标 i] 超过 pivot) 下标 i 累加 1;」
        while (a[j] < pivot) j -= 1; // 循环，直到不满足「数组[下标 j] 小于 pivot) 下标 j 累减 1;」
        if (i <= j) { // 若 下标 i 不超过 下标 j
            const t = a[i];
            a[i] = a[j];
            a[j] = t;
            i += 1; // 下标 i累加 1
            if (j == 0) break; // 若 下标 j 等于 0) break;
            j -= 1; // 下标 j累减 1
        }
    }
    if (k <= j + 1) { // 若 下标 k 不超过 下标 j 加 1
        if (l < j) quickselect(a, l, j, k); // 若 左指针 小于 下标 j) quickselect(数组, 左指针, 下标 j, 下标 k);
        return; // return;
    }
    if (k >= i + 1 and i < r) quickselect(a, i, r, k);
}
fn findKthLargest(nums: []const i32, k: usize) i32 { // 定义函数/方法 findKthLargest
    var a: [4096]i32 = undefined; // 把 undefined; 写入 var a: [4096]i32
    @memcpy(a[0..nums.len], nums); // @memcpy(数组[0..数组.长度], 数组);
    quickselect(a[0..nums.len], 0, nums.len - 1, k); // quickselect(数组[0..数组.长度], 0, 数组.长度 减 1, 下标 k);
    return a[k - 1]; // 返回 数组[下标 k 减 1]
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    if (findKthLargest(&[_]i32{ 3, 2, 1, 5, 6, 4 }, 2) != 5) return error.TestFailed;
    if (findKthLargest(&[_]i32{ 3, 2, 3, 1, 2, 4, 5, 5, 6 }, 4) != 4) return error.TestFailed;
    if (findKthLargest(&[_]i32{1}, 1) != 1) return error.TestFailed;
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
