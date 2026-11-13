// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/113877588
// 动态规划之Fibonacci — Zig 版（方案2）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn fibMemo(n: i32) i64 { // 定义函数/方法 fibMemo
    var memo: [64]i64 = undefined; // 把 undefined; 写入 var memo: [64]i64
    for (0..64) |i| memo[i] = -1; // 让 下标 i 从 0 走到 64 减一
    const D = struct { // 把 struct { 存入 D
        fn go(k: i32, m: []i64) i64 { // 定义函数/方法 go
            if (k <= 1) return k; // 若 下标 k 不超过 1，直接返回 下标 k
            if (m[@intCast(k)] != -1) return m[@intCast(k)]; // 若 映射表[@intCast(下标 k)] 不等于 减 1，直接返回 映射表[@intCast(下标 k)]
            m[@intCast(k)] = go(k - 1, m) + go(k - 2, m); // 把 go(下标 k 减 1, 映射表) 加 go(下标 k 减 2, 映射表); 写入 m[@intCast(k)]
            return m[@intCast(k)]; // 返回 映射表[@intCast(下标 k)]
        }
    };
    return D.go(n, &memo); // 返回 D.go(元素个数, 按位与 记忆化表)
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    if (fibMemo(10) != 55 or fibMemo(20) != 6765 or fibMemo(0) != 0) return error.TestFailed;
    std.debug.print("PASS\n", .{});
} // 全部用例通过，输出 PASS
