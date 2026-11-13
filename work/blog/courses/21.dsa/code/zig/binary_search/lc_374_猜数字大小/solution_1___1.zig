// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145238093
// LeetCode 374. 猜数字大小 — Zig 版（方案1：递归二分（忠实 TS：左分支 rec(1, mid-1)））
const std = @import("std"); // 把 @import(「std」) 存入 std
var pick: i64 = 6; // 把 6; 写入 var pick: i64
fn guess(num: i64) i32 { // 定义函数/方法 guess
    if (num == pick) return 0; // 若 num 等于 pick，直接返回 0
    return if (num < pick) 1 else -1; // 返回 if (num 小于 pick) 1 else 减 1
}
fn rec(low: i64, high: i64) i64 { // 定义函数/方法 rec
    if (low > high) return -1; // 若 low 超过 high，直接返回 减 1
    const mid = low + @divTrunc(high - low, 2); // 把 low 加 @divTrunc(high 减 low, 2) 存入 中点
    return switch (guess(mid)) { // 定义函数/方法 switch
        0 => mid,
        1 => rec(mid + 1, high),
        else => rec(1, mid - 1),
    };
}
fn guessNumber(n: i64) i64 { // 定义函数/方法 guessNumber
    return rec(1, n); // 返回 rec(1, 元素个数)
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    const cases = [_][2]i64{ .{ 10, 6 }, .{ 1, 1 }, .{ 5, 3 }, .{ 2, 2 } };
    for (cases) |c| { // 逐个取出 cases 的元素（字符）
        pick = c[1]; // 把 字符[1]; 写入 pick
        if (guessNumber(c[0]) != c[1]) { // 若 guessNumber(字符[0]) 不等于 字符[1]
            std.debug.print("FAIL n={d} pick={d}\n", .{ c[0], c[1] }); // 打印输出
            return error.TestFailed; // 返回 error.TestFailed
        }
    }
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
