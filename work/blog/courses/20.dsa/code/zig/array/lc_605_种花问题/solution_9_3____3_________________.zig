// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134638462
// LeetCode 605. 种花问题 — Zig 版（方案9）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn canPlaceFlowers(bed: []const i32, n: i32) bool { // 定义函数/方法 canPlaceFlowers
    var v: [4096]i32 = undefined; // 把 undefined; 写入 var v: [4096]i32
    @memcpy(v[0..bed.len], bed); // @memcpy(值[0..bed.长度], bed);
    var count: i32 = 0; // 把 0; 写入 var count: i32
    for (0..bed.len) |i| { // 逐个取出 0..bed.长度 的元素（下标 i）
        const leftOk = i == 0 or v[i - 1] == 0; // 把 下标 i 等于 0 or 值[下标 i 减 1] 等于 0 存入 leftOk
        const rightOk = i == bed.len - 1 or v[i + 1] == 0; // 把 下标 i 等于 bed.长度 减 1 or 值[下标 i 加 1] 等于 0 存入 rightOk
        if (v[i] == 0 and leftOk and rightOk) { // 若 值[下标 i] 等于 0 and leftOk and rightOk
            v[i] = 1; // 把 1; 写入 v[i]
            count += 1; // 计数累加 1
        }
    }
    return count >= n; // 返回 计数 不低于 元素个数
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    if (!canPlaceFlowers(&[_]i32{ 1, 0, 0, 0, 1 }, 1)) return error.TestFailed;
    if (canPlaceFlowers(&[_]i32{ 1, 0, 0, 0, 1 }, 2)) return error.TestFailed;
    if (!canPlaceFlowers(&[_]i32{ 0, 0, 1, 0, 0 }, 1)) return error.TestFailed;
    std.debug.print("PASS\n", .{});
} // 全部用例通过，输出 PASS
