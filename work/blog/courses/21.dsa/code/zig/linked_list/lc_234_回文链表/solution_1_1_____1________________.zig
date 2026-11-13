// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133812752
// LeetCode 234. 回文链表 — Zig 版（方案1）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn isPalindromeList(v: []const i32) bool { // 定义判定函数 isPalindromeList
    if (v.len == 0) return true; // 若 值.长度 等于 0，直接返回 true
    var i: usize = 0; // 把 0; 写入 var i: usize
    var j: usize = v.len - 1; // 把 值.长度 减 1; 写入 var j: usize
    while (i < j) { // 循环，直到不满足「下标 i 小于 下标 j」
        if (v[i] != v[j]) return false; // 若 值[下标 i] 不等于 值[下标 j]，直接返回 false
        i += 1; // 下标 i累加 1
        j -= 1; // 下标 j累减 1
    }
    return true; // 返回 true
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    if (!isPalindromeList(&[_]i32{})) return error.TestFailed; // 若 取反 isPalindromeList( 按位与 [_]i32{})，直接返回 error.TestFailed
    if (!isPalindromeList(&[_]i32{ 1, 2, 2, 1 })) return error.TestFailed;
    if (isPalindromeList(&[_]i32{ 1, 2 })) return error.TestFailed;
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
