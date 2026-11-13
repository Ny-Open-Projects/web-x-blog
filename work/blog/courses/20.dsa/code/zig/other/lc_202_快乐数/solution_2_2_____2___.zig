// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135124945
// LeetCode 202. 快乐数 — Zig 版（方案2）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn bitSquareSum(n0: i64) i64 { // 定义函数/方法 bitSquareSum
    var s: i64 = 0; // 把 0; 写入 var s: i64
    var n = n0; // 把 n0 存入 元素个数
    while (n > 0) : (n = @divTrunc(n, 10)) { // 循环，直到不满足「元素个数 超过 0) : (元素个数 赋值为 @divTrunc(元素个数, 10」
        const d = @mod(n, 10); // 把 @mod(元素个数, 10) 存入 d
        s += d * d; // 字符串累加 d 乘 d
    }
    return s; // 返回 字符串
}
fn isHappy(n0: i64) bool { // 定义判定函数 isHappy
    var seen_buf: [1024]i64 = undefined; // 把 undefined; 写入 var seen_buf: [1024]i64
    var cnt: usize = 0; // 把 0; 写入 var cnt: usize
    var n = n0; // 把 n0 存入 元素个数
    while (n != 1) { // 循环，直到不满足「元素个数 不等于 1」
        for (seen_buf[0..cnt]) |v| if (v == n) return false;
        if (cnt < seen_buf.len) {
            seen_buf[cnt] = n;
            cnt += 1;
        } // 若 计数 小于 seen_buf.长度) { seen_buf[计数] 赋值为 元素个数; 计数 累加 1; }
        n = bitSquareSum(n); // 把 bitSquareSum(元素个数); 写入 元素个数
    }
    return true; // 返回 true
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    if (bitSquareSum(1) != 1) return error.TestFailed; // 若 bitSquareSum(1) 不等于 1，直接返回 error.TestFailed
    if (bitSquareSum(19) != 82) return error.TestFailed; // 若 bitSquareSum(19) 不等于 82，直接返回 error.TestFailed
    if (bitSquareSum(82) != 68) return error.TestFailed; // 若 bitSquareSum(82) 不等于 68，直接返回 error.TestFailed
    if (!isHappy(19) or !isHappy(1) or isHappy(2)) return error.TestFailed;
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
