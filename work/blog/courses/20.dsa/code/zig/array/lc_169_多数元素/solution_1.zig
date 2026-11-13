// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133531071
// LeetCode 169. 多数元素 — Zig 版（方案1）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn majorityElement(nums: []const i32, alloc: std.mem.Allocator) i32 { // 定义函数/方法 majorityElement
    var counts = std.AutoHashMap(i32, i32).init(alloc); // 把 std.AutoHashMap(i32, i32).init(alloc) 存入 counts
    var best = nums[0]; // 把 数组[0] 存入 当前最优
    var bn: i32 = 0; // 把 0; 写入 var bn: i32
    for (nums) |v| { // 逐个取出 数组 的元素（值）
        const c = (counts.get(v) orelse 0) + 1; // 把 (counts 查找 值) orelse 0) 加 1 存入 字符
        counts.put(v, c) catch unreachable; // counts.put(值, 字符) catch unreachable;
        if (c > bn) {
            bn = c;
            best = v;
        } // 若 字符 超过 bn) { bn 赋值为 字符; 当前最优 赋值为 值; }
    }
    return best; // 返回 当前最优
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator); // 把 std.堆.ArenaAllocator.init(std.堆.page_allocator) 存入 arena
    defer arena.deinit(); // defer arena.deinit();
    if (majorityElement(&[_]i32{ 3, 2, 3 }, arena.allocator()) != 3) return error.TestFailed;
    if (majorityElement(&[_]i32{ 2, 2, 1, 1, 1, 2, 2 }, arena.allocator()) != 2) return error.TestFailed;
    std.debug.print("PASS\n", .{});
} // 全部用例通过，输出 PASS
