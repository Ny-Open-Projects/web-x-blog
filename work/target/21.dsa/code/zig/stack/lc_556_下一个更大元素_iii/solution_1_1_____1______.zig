// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145397820
// LeetCode 556. 下一个更大元素 III — Zig 版（方案1）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn nextGreaterElement(n: i32) i32 { // 定义函数/方法 nextGreaterElement
    var d: [16]i32 = undefined; // 把 undefined; 写入 var d: [16]i32
    var m: usize = 0; // 把 0; 写入 var m: usize
    var x: i64 = n; // 把 元素个数; 写入 var x: i64
    while (x > 0) { // 循环，直到不满足「x 超过 0」
        d[m] = @intCast(@mod(x, 10)); // 把 @intCast(@mod(x, 10)); 写入 d[m]
        m += 1; // 映射表累加 1
        x = @divTrunc(x, 10); // 把 @divTrunc(x, 10); 写入 x
    }
    var i: usize = 0; // 把 0; 写入 var i: usize
    var j: usize = m - 1; // 把 映射表 减 1; 写入 var j: usize
    while (i < j) : ({ // 循环，直到不满足「下标 i 小于 下标 j) : (」
        i += 1; // 下标 i累加 1
        j -= 1; // 下标 j累减 1
    }) { // }) {
        const t = d[i]; // 把 d[下标 i] 存入 另一字符串
        d[i] = d[j]; // 把 d[下标 j]; 写入 d[i]
        d[j] = t; // 把 另一字符串; 写入 d[j]
    }
    if (m < 2) return -1; // 若 映射表 小于 2，直接返回 减 1
    var ii: isize = @as(isize, @intCast(m)) - 2; // 把 @as(isize, @intCast(映射表)) 减 2; 写入 var ii: isize
    while (ii >= 0 and d[@intCast(ii)] >= d[@intCast(ii + 1)]) ii -= 1;
    if (ii < 0) return -1; // 若 ii 小于 0，直接返回 减 1
    const iu: usize = @intCast(ii); // 把 @intCast(ii); 写入 const iu: usize
    var jj: usize = m - 1; // 把 映射表 减 1; 写入 var jj: usize
    while (d[jj] <= d[iu]) jj -= 1; // 循环，直到不满足「d[jj] 不超过 d[iu]) jj 累减 1;」
    const t = d[iu]; // 把 d[iu] 存入 另一字符串
    d[iu] = d[jj]; // 把 d[jj]; 写入 d[iu]
    d[jj] = t; // 把 另一字符串; 写入 d[jj]
    var l = iu + 1; // 把 iu 加 1 存入 左指针
    var r = m - 1; // 把 映射表 减 1 存入 右指针
    while (l < r) : ({ // 循环，直到不满足「左指针 小于 右指针) : (」
        l += 1; // 左指针累加 1
        r -= 1; // 右指针累减 1
    }) { // }) {
        const t2 = d[l]; // 把 d[左指针] 存入 t2
        d[l] = d[r]; // 把 d[右指针]; 写入 d[l]
        d[r] = t2; // 把 t2; 写入 d[r]
    }
    var res: i64 = 0; // 把 0; 写入 var res: i64
    for (0..m) |k| res = res * 10 + d[k]; // 让 下标 k 从 0 走到 映射表 减一
    return if (res > 2147483647) -1 else @intCast(res); // 返回 if (结果 超过 2147483647) 减 1 else @intCast(结果)
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    if (nextGreaterElement(12) != 21) return error.TestFailed; // 若 nextGreaterElement(12) 不等于 21，直接返回 error.TestFailed
    if (nextGreaterElement(21) != -1) return error.TestFailed; // 若 nextGreaterElement(21) 不等于 减 1，直接返回 error.TestFailed
    if (nextGreaterElement(1) != -1) return error.TestFailed; // 若 nextGreaterElement(1) 不等于 减 1，直接返回 error.TestFailed
    std.debug.print("PASS\n", .{});
} // 全部用例通过，输出 PASS
