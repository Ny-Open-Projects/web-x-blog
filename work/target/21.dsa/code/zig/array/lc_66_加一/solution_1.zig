// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134707891
// LeetCode 66. 加一 — Zig 版（方案1）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn plusOne(digits: []const i32, out: []i32) usize { // 定义函数/方法 plusOne
    var v: [4096]i32 = undefined; // 把 undefined; 写入 var v: [4096]i32
    @memcpy(v[0..digits.len], digits); // @memcpy(值[0..digits.长度], digits);
    var i: usize = digits.len; // 把 digits.长度; 写入 var i: usize
    while (i > 0) { // 循环，直到不满足「下标 i 超过 0」
        i -= 1; // 下标 i累减 1
        if (v[i] < 9) { // 若 值[下标 i] 小于 9
            v[i] += 1; // v[i]累加 1
            @memcpy(out[0..digits.len], v[0..digits.len]); // @memcpy(out[0..digits.长度], 值[0..digits.长度]);
            return digits.len; // 返回 digits.长度
        }
        v[i] = 0; // 把 0; 写入 v[i]
    }
    out[0] = 1; // 把 1; 写入 out[0]
    @memcpy(out[1 .. digits.len + 1], v[0..digits.len]); // @memcpy(out[1 .. digits.长度 加 1], 值[0..digits.长度]);
    return digits.len + 1; // 返回 digits.长度 加 1
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var out: [4097]i32 = undefined; // 把 undefined; 写入 var out: [4097]i32
    var n = plusOne(&[_]i32{ 1, 2, 3 }, &out); // 把 plusOne( 按位与 [_]i32{ 1, 2, 3 }, 按位与 out) 存入 元素个数
    if (n != 3 or out[2] != 4) return error.TestFailed; // 若 元素个数 不等于 3 or out[2] 不等于 4，直接返回 error.TestFailed
    n = plusOne(&[_]i32{ 4, 3, 2, 1 }, &out); // 把 plusOne( 按位与 [_]i32{ 4, 3, 2, 1 }, 按位与 out); 写入 元素个数
    if (n != 4 or out[3] != 2) return error.TestFailed; // 若 元素个数 不等于 4 or out[3] 不等于 2，直接返回 error.TestFailed
    n = plusOne(&[_]i32{9}, &out); // 把 plusOne( 按位与 [_]i32{9}, 按位与 out); 写入 元素个数
    if (n != 2 or out[0] != 1 or out[1] != 0) return error.TestFailed;
    std.debug.print("PASS\n", .{});
} // 全部用例通过，输出 PASS
