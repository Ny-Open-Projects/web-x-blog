// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/110240695
// LeetCode 110240695. 分治策略之 greatest slice — Zig 版（方案C：分治 best/prefix/suffix/total）
const std = @import("std"); // 把 @import(「std」) 存入 std

const Quad = struct { best: i64, prefix: i64, suffix: i64, total: i64 };

fn helper(arr: []const i32, lo: usize, hi: usize) Quad { // 定义函数/方法 helper
    if (hi - lo == 1) { // 若 右边界 减 左边界 等于 1
        const v: i64 = arr[lo]; // 把 数组[左边界]; 写入 const v: i64
        return .{ .best = v, .prefix = v, .suffix = v, .total = v }; // 返回 { .当前最优 赋值为 值, .prefix 赋值为 值, .suffix 赋值为 值, .总和 赋值为 值 }
    }
    const mi = (lo + hi) / 2; // 把 (左边界 加 右边界) 除以 2 存入 mi
    const l = helper(arr, lo, mi); // 把 helper(数组, 左边界, mi) 存入 左指针
    const r = helper(arr, mi, hi); // 把 helper(数组, mi, 右边界) 存入 右指针
    const crossing = l.suffix + r.prefix; // 把 左指针.suffix 加 右指针.prefix 存入 crossing
    return .{ // 返回 {
        .best = @max(l.best, @max(r.best, crossing)),
        .prefix = @max(l.prefix, l.total + r.prefix),
        .suffix = @max(r.suffix, r.total + l.suffix),
        .total = l.total + r.total,
    };
}

fn maxSubArrayDc(arr: []const i32) i64 { // 定义函数/方法 maxSubArrayDc
    if (arr.len == 0) return 0; // 若 数组.长度 等于 0，直接返回 0
    return helper(arr, 0, arr.len).best; // 返回 helper(数组, 0, 数组.长度).当前最优
}

pub fn main() !void { // 程序入口：跑内嵌自测用例
    const a0 = [_]i32{ -2, 1, -3, 4, -1, 2, 1 }; // 把 [_]i32{ 减 2, 1, 减 3, 4, 减 1, 2, 1 } 存入 a0
    const a1 = [_]i32{ 1, 2, 3 }; // 把 [_]i32{ 1, 2, 3 } 存入 a1
    if (maxSubArrayDc(&a0) != 6) return error.TestFailed; // 若 maxSubArrayDc( 按位与 a0) 不等于 6，直接返回 error.TestFailed
    if (maxSubArrayDc(&a1) != 6) return error.TestFailed; // 若 maxSubArrayDc( 按位与 a1) 不等于 6，直接返回 error.TestFailed
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
