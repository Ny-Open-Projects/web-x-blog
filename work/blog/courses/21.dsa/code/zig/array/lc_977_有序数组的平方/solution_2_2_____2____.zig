// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134982348
// LeetCode 977. 有序数组的平方 — Zig 版（方案2）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn sortedSquares(nums: []const i32, out: []i32) void { // 定义函数/方法 sortedSquares
    const n = nums.len; // 把 数组.长度 存入 元素个数
    var l: usize = 0; // 把 0; 写入 var l: usize
    var r: usize = n - 1; // 把 元素个数 减 1; 写入 var r: usize
    var idx: usize = n - 1; // 把 元素个数 减 1; 写入 var idx: usize
    while (l <= r) { // 循环，直到不满足「左指针 不超过 右指针」
        const a: i64 = @intCast(if (nums[l] < 0) -nums[l] else nums[l]);
        const b: i64 = @intCast(if (nums[r] < 0) -nums[r] else nums[r]);
        if (a > b) { // 若 数组 超过 b
            out[idx] = @intCast(a * a); // 把 @intCast(数组 乘 数组); 写入 out[idx]
            l += 1; // 左指针累加 1
        } else { // 否则
            out[idx] = @intCast(b * b); // 把 @intCast(b 乘 b); 写入 out[idx]
            if (r == 0) break; // 若 右指针 等于 0) break;
            r -= 1; // 右指针累减 1
        }
        if (idx == 0) break; // 若 idx 等于 0) break;
        idx -= 1; // idx累减 1
    }
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var out: [4096]i32 = undefined; // 把 undefined; 写入 var out: [4096]i32
    sortedSquares(&[_]i32{ -4, -1, 0, 3, 10 }, &out); // sortedSquares( 按位与 [_]i32{ 减 4, 减 1, 0, 3, 10 }, 按位与 out);
    if (out[0] != 0 or out[4] != 100) return error.TestFailed; // 若 out[0] 不等于 0 or out[4] 不等于 100，直接返回 error.TestFailed
    sortedSquares(&[_]i32{ -7, -3, 2, 3, 11 }, &out); // sortedSquares( 按位与 [_]i32{ 减 7, 减 3, 2, 3, 11 }, 按位与 out);
    if (out[0] != 4 or out[4] != 121) return error.TestFailed; // 若 out[0] 不等于 4 or out[4] 不等于 121，直接返回 error.TestFailed
    sortedSquares(&[_]i32{ 1, 2, 3 }, &out); // sortedSquares( 按位与 [_]i32{ 1, 2, 3 }, 按位与 out);
    if (out[0] != 1 or out[2] != 9) return error.TestFailed; // 若 out[0] 不等于 1 or out[2] 不等于 9，直接返回 error.TestFailed
    std.debug.print("PASS\n", .{});
} // 全部用例通过，输出 PASS
