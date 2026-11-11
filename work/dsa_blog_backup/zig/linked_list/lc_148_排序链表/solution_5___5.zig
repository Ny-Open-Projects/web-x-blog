// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133904873
// LeetCode 148. 排序链表 — Zig 版（方案5）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn sortList(vals: []const i32, out: []i32) void { // 定义函数/方法 sortList
    @memcpy(out[0..vals.len], vals); // @memcpy(out[0..vals.长度], vals);
    std.sort.pdq(i32, out[0..vals.len], {}, std.sort.asc(i32)); // std.sort.pdq(i32, out[0..vals.长度], {}, std.sort.asc(i32));
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var buf: [8]i32 = undefined; // 把 undefined; 写入 var buf: [8]i32
    sortList(&[_]i32{ 4, 2, 1, 3 }, &buf); // sortList( 按位与 [_]i32{ 4, 2, 1, 3 }, 按位与 buf);
    if (buf[0] != 1 or buf[3] != 4) return error.TestFailed; // 若 buf[0] 不等于 1 or buf[3] 不等于 4，直接返回 error.TestFailed
    sortList(&[_]i32{ -1, 5, 3, 4, 0 }, &buf); // sortList( 按位与 [_]i32{ 减 1, 5, 3, 4, 0 }, 按位与 buf);
    if (buf[0] != -1 or buf[4] != 5) return error.TestFailed; // 若 buf[0] 不等于 减 1 or buf[4] 不等于 5，直接返回 error.TestFailed
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
