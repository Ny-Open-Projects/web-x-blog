// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133471440
// LeetCode 215. 数组中的第K个最大元素 — Zig 版（方案3）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn findKthLargest(nums: []const i32, k: usize) i32 { // 定义函数/方法 findKthLargest
    var a: [4096]i32 = undefined; // 把 undefined; 写入 var a: [4096]i32
    @memcpy(a[0..nums.len], nums); // @memcpy(数组[0..数组.长度], 数组);
    const n = nums.len; // 把 数组.长度 存入 元素个数
    var i: isize = @intCast(n - 1); // 把 @intCast(元素个数 减 1); 写入 var i: isize
    const bound: isize = @as(isize, @intCast(n)) - 1 - @as(isize, @intCast(k));
    while (i > bound) : (i -= 1) { // 循环，直到不满足「下标 i 超过 bound) : (下标 i 累减 1」
        var j: usize = 0; // 把 0; 写入 var j: usize
        while (@as(isize, @intCast(j)) < i) : (j += 1) { // 循环，直到不满足「@as(isize, @intCast(下标 j)) 小于 下标 i) : (下标 j 累加 1」
            if (a[j] > a[j + 1]) {
                const t = a[j];
                a[j] = a[j + 1];
                a[j + 1] = t;
            }
        }
    }
    return a[n - k]; // 返回 数组[元素个数 减 下标 k]
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    if (findKthLargest(&[_]i32{ 3, 2, 1, 5, 6, 4 }, 2) != 5) return error.TestFailed;
    if (findKthLargest(&[_]i32{ 3, 2, 3, 1, 2, 4, 5, 5, 6 }, 4) != 4) return error.TestFailed;
    if (findKthLargest(&[_]i32{1}, 1) != 1) return error.TestFailed;
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
