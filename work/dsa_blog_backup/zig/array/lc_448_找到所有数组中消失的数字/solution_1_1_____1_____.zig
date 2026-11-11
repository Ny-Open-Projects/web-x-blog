// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134378688
// LeetCode 448. 找到所有数组中消失的数字 — Zig 版（方案1）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn findDisappeared(nums: []const i32, out: *std.ArrayList(i32)) void { // 定义函数/方法 findDisappeared
    var v: [4096]i32 = undefined; // 把 undefined; 写入 var v: [4096]i32
    @memcpy(v[0..nums.len], nums); // @memcpy(值[0..数组.长度], 数组);
    for (0..nums.len) |i| { // 逐个取出 0..数组.长度 的元素（下标 i）
        const idx: usize = @intCast(if (v[i] < 0) -v[i] - 1 else v[i] - 1);
        if (v[idx] > 0) v[idx] = -v[idx]; // 若 值[idx] 超过 0) 值[idx] 赋值为 减 值[idx];
    }
    for (0..nums.len) |i| { // 逐个取出 0..数组.长度 的元素（下标 i）
        if (v[i] > 0) out.append(@intCast(i + 1)) catch unreachable;
    }
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var out = std.ArrayList(i32).init(std.heap.page_allocator); // 把 std.ArrayList(i32).init(std.堆.page_allocator) 存入 out
    defer out.deinit(); // defer out.deinit();
    findDisappeared(&[_]i32{ 4, 3, 2, 7, 8, 2, 3, 1 }, &out);
    if (out.items.len != 2 or out.items[0] != 5 or out.items[1] != 6) return error.TestFailed;
    out.clearRetainingCapacity(); // out.clearRetainingCapacity();
    findDisappeared(&[_]i32{ 1, 1 }, &out); // findDisappeared( 按位与 [_]i32{ 1, 1 }, 按位与 out);
    if (out.items.len != 1 or out.items[0] != 2) return error.TestFailed;
    std.debug.print("PASS\n", .{});
} // 全部用例通过，输出 PASS
