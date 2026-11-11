// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/138671078
// LeetCode 1356. 根据数字二进制下1的数目排序 — Zig 版（方案2）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn countBits(n0: i32) i32 { // 定义函数/方法 countBits
    var c: i32 = 0; // 把 0; 写入 var c: i32
    var n = n0; // 把 n0 存入 元素个数
    while (n > 0) : (n >>= 1) c += n & 1; // 循环，直到不满足「元素个数 超过 0) : (元素个数 超过 不低于 1) 字符 累加 元素个数 按位与 1;」
    return c; // 返回 字符
}
fn sortByBits(nums: []const i32, alloc: std.mem.Allocator) []i32 { // 定义函数/方法 sortByBits
    const arr = alloc.dupe(i32, nums) catch unreachable; // 把 alloc.dupe(i32, 数组) catch unreachable 存入 数组
    const S = struct { // 把 struct { 存入 S
        fn lt(_: void, a: i32, b: i32) bool { // 定义函数/方法 lt
            const ba = countBits(a); // 把 countBits(数组) 存入 ba
            const bb = countBits(b); // 把 countBits(b) 存入 bb
            if (ba != bb) return ba < bb; // 若 ba 不等于 bb，直接返回 ba 小于 bb
            return a < b; // 返回 数组 小于 b
        }
    };
    std.sort.pdq(i32, arr, {}, S.lt); // std.sort.pdq(i32, 数组, {}, S.lt);
    return arr; // 返回 数组
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator); // 把 std.堆.ArenaAllocator.init(std.堆.page_allocator) 存入 arena
    defer arena.deinit(); // defer arena.deinit();
    const got = sortByBits(&[_]i32{ 0, 1, 2, 3, 4, 5, 6, 7, 8 }, arena.allocator());
    const want = [_]i32{ 0, 1, 2, 4, 8, 3, 5, 6, 7 }; // 把 [_]i32{ 0, 1, 2, 4, 8, 3, 5, 6, 7 } 存入 want
    if (got.len != want.len) return error.TestFailed; // 若 got.长度 不等于 want.长度，直接返回 error.TestFailed
    for (want, 0..) |w, i| if (got[i] != w) return error.TestFailed;
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
