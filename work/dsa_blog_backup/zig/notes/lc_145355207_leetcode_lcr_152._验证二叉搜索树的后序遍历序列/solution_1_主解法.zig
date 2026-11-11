// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145355207
// LeetCode LCR 152. 验证二叉搜索树的后序遍历序列 — Zig 版（方案1）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn checkSeq(seq: []const i32, lo: usize, hi: usize) bool { // 定义判定函数 checkSeq
    if (hi <= lo + 1) return true; // 若 右边界 不超过 左边界 加 1，直接返回 true
    const root = seq[hi]; // 把 seq[右边界] 存入 根节点
    var i = lo; // 把 左边界 存入 下标 i
    while (i < hi and seq[i] < root) i += 1; // 循环，直到不满足「下标 i 小于 右边界 and seq[下标 i] 小于 根节点) 下标 i 累加 1;」
    var j = i; // 把 下标 i 存入 下标 j
    while (j < hi) : (j += 1) { // 循环，直到不满足「下标 j 小于 右边界) : (下标 j 累加 1」
        if (seq[j] < root) return false; // 若 seq[下标 j] 小于 根节点，直接返回 false
    }
    return checkSeq(seq, lo, i - 1) and checkSeq(seq, i, hi - 1);
}
fn verifyPostorder(postorder: []const i32) bool { // 定义函数/方法 verifyPostorder
    if (postorder.len == 0) return true; // 若 postorder.长度 等于 0，直接返回 true
    return checkSeq(postorder, 0, postorder.len - 1); // 返回 checkSeq(postorder, 0, postorder.长度 减 1)
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    if (verifyPostorder(&[_]i32{ 1, 6, 3, 2, 5 })) return error.TestFailed;
    if (!verifyPostorder(&[_]i32{ 1, 3, 2, 4, 5 })) return error.TestFailed;
    if (!verifyPostorder(&[_]i32{ 4, 6, 5, 9, 8, 7 })) return error.TestFailed;
    if (!verifyPostorder(&[_]i32{ 1, 2, 3 })) return error.TestFailed;
    std.debug.print("PASS\n", .{});
} // 全部用例通过，输出 PASS
