// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/110240695
// LeetCode 110240695. 分治策略之 greatest slice — Zig 版（方案B：增量扫描）
const std = @import("std"); // 把 @import(「std」) 存入 std

fn maxSubArrayIc(arr: []const i32) i64 { // 定义函数/方法 maxSubArrayIc
    if (arr.len == 0) return 0; // 若 数组.长度 等于 0，直接返回 0
    var gs: i64 = arr[0]; // 把 数组[0]; 写入 var gs: i64
    for (0..arr.len) |i| { // 逐个取出 0..数组.长度 的元素（下标 i）
        var s: i64 = 0; // 把 0; 写入 var s: i64
        for (i..arr.len) |j| { // 逐个取出 下标 i..数组.长度 的元素（下标 j）
            s += arr[j]; // 字符串累加 数组[下标 j]
            if (gs < s) gs = s; // 若 gs 小于 字符串) gs 赋值为 字符串;
        }
    }
    return gs; // 返回 gs
}

pub fn main() !void { // 程序入口：跑内嵌自测用例
    const a0 = [_]i32{ -2, 1, -3, 4, -1, 2, 1 }; // 把 [_]i32{ 减 2, 1, 减 3, 4, 减 1, 2, 1 } 存入 a0
    const a1 = [_]i32{ -1, -2, -3 }; // 把 [_]i32{ 减 1, 减 2, 减 3 } 存入 a1
    if (maxSubArrayIc(&a0) != 6) return error.TestFailed; // 若 maxSubArrayIc( 按位与 a0) 不等于 6，直接返回 error.TestFailed
    if (maxSubArrayIc(&a1) != -1) return error.TestFailed; // 若 maxSubArrayIc( 按位与 a1) 不等于 减 1，直接返回 error.TestFailed
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
