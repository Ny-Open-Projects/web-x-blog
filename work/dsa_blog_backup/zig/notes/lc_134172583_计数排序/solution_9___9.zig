// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134172583
// 数据结构与算法之排序: 计数排序 — Zig 版（方案9）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn countSort(nums: []i32, alloc: std.mem.Allocator) []i32 { // 定义函数/方法 countSort
    if (nums.len == 0) return nums; // 若 数组.长度 等于 0，直接返回 数组
    var mx = nums[0]; // 把 数组[0] 存入 mx
    var mn = nums[0]; // 把 数组[0] 存入 mn
    for (nums) |v| { // 逐个取出 数组 的元素（值）
        if (v > mx) mx = v; // 若 值 超过 mx) mx 赋值为 值;
        if (v < mn) mn = v; // 若 值 小于 mn) mn 赋值为 值;
    }
    const range: usize = @intCast(mx - mn + 1); // 把 @intCast(mx 减 mn 加 1); 写入 const range: usize
    var count = alloc.alloc(i32, range) catch unreachable; // 把 alloc.alloc(i32, range) catch unreachable 存入 计数
    var output = alloc.alloc(i32, nums.len) catch unreachable; // 把 alloc.alloc(i32, 数组.长度) catch unreachable 存入 输出
    for (0..range) |i| count[i] = 0; // 让 下标 i 从 0 走到 range 减一
    for (nums) |v| count[@intCast(v - mn)] += 1; // 逐个取出 数组 的元素（值）
    for (1..range) |i| count[i] += count[i - 1]; // 逐个取出 1..range 的元素（下标 i）
    var i: usize = nums.len; // 把 数组.长度; 写入 var i: usize
    while (i > 0) { // 循环，直到不满足「下标 i 超过 0」
        i -= 1; // 下标 i累减 1
        const idx: usize = @intCast(nums[i] - mn); // 把 @intCast(数组[下标 i] 减 mn); 写入 const idx: usize
        count[idx] -= 1; // count[idx]累减 1
        output[@intCast(count[idx])] = nums[i]; // 把 数组[下标 i]; 写入 output[@intCast(count[idx])]
    }
    return output; // 返回 输出
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator); // 把 std.堆.ArenaAllocator.init(std.堆.page_allocator) 存入 arena
    defer arena.deinit(); // defer arena.deinit();
    const alloc = arena.allocator(); // 把 arena.allocator() 存入 alloc
    var v1 = [_]i32{ 5, 3, 8, 3, 1 }; // 把 [_]i32{ 5, 3, 8, 3, 1 } 存入 v1
    const got = countSort(&v1, alloc); // 把 countSort( 按位与 v1, alloc) 存入 got
    const want = [_]i32{ 1, 3, 3, 5, 8 }; // 把 [_]i32{ 1, 3, 3, 5, 8 } 存入 want
    for (want, 0..) |w, i| if (got[i] != w) return error.TestFailed;
    std.debug.print("PASS\n", .{});
} // 全部用例通过，输出 PASS
