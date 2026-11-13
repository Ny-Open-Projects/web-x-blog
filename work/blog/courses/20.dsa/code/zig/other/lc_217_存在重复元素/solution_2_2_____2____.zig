// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135038527
// LeetCode 217. 存在重复元素 — Zig 版（方案2）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn containsDuplicate(nums: []const i32, alloc: std.mem.Allocator) bool { // 定义函数/方法 containsDuplicate
    var set = std.AutoHashMap(i32, void).init(alloc); // 把 std.AutoHashMap(i32, void).init(alloc) 存入 set
    defer set.deinit(); // defer set.deinit();
    for (nums) |v| { // 逐个取出 数组 的元素（值）
        if (set.contains(v)) return true; // 若 set 是否包含 值)，直接返回 true
        set.put(v, {}) catch unreachable; // set.put(值, {}) catch unreachable;
    }
    return false; // 返回 false
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator); // 把 std.堆.ArenaAllocator.init(std.堆.page_allocator) 存入 arena
    defer arena.deinit(); // defer arena.deinit();
    if (!containsDuplicate(&[_]i32{ 1, 2, 3, 1 }, arena.allocator())) return error.TestFailed;
    if (containsDuplicate(&[_]i32{ 1, 2, 3, 4 }, arena.allocator())) return error.TestFailed;
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
