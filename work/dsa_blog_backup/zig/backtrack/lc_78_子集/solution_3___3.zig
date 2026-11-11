// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134109616
// LeetCode 78. 子集 — Zig 版（方案3）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn subsets(nums: []const i32, alloc: std.mem.Allocator, res: *std.ArrayList(std.ArrayList(i32))) void { // 定义函数/方法 subsets
    const D = struct { // 把 struct { 存入 D
        fn dfs(ns: []const i32, start: usize, path: *std.ArrayList(i32), out: *std.ArrayList(std.ArrayList(i32))) void { // 定义函数/方法 dfs
            var cp = std.ArrayList(i32).init(out.allocator); // 把 std.ArrayList(i32).init(out.allocator) 存入 cp
            cp.appendSlice(path.items) catch unreachable; // cp.appendSlice(当前路径.items) catch unreachable;
            out.append(cp) catch unreachable; // 把 cp 追加到列表尾部
            for (start..ns.len) |i| { // 逐个取出 起点..ns.长度 的元素（下标 i）
                path.append(ns[i]) catch unreachable; // 把 ns[下标 i] 追加到列表尾部
                dfs(ns, i + 1, path, out); // dfs(ns, 下标 i 加 1, 当前路径, out);
                _ = path.pop(); // 弹出栈顶元素
            }
        }
    };
    var path = std.ArrayList(i32).init(alloc); // 把 std.ArrayList(i32).init(alloc) 存入 当前路径
    D.dfs(nums, 0, &path, res); // D.dfs(数组, 0, 按位与 当前路径, 结果);
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator); // 把 std.堆.ArenaAllocator.init(std.堆.page_allocator) 存入 arena
    defer arena.deinit(); // defer arena.deinit();
    const alloc = arena.allocator(); // 把 arena.allocator() 存入 alloc
    var res = std.ArrayList(std.ArrayList(i32)).init(std.heap.page_allocator);
    defer res.deinit(); // defer 结果.deinit();
    subsets(&[_]i32{ 1, 2, 3 }, alloc, &res); // subsets( 按位与 [_]i32{ 1, 2, 3 }, alloc, 按位与 结果);
    if (res.items.len != 8) return error.TestFailed; // 若 结果.items.长度 不等于 8，直接返回 error.TestFailed
    res.clearRetainingCapacity(); // 结果.clearRetainingCapacity();
    subsets(&[_]i32{0}, alloc, &res); // subsets( 按位与 [_]i32{0}, alloc, 按位与 结果);
    if (res.items.len != 2) return error.TestFailed; // 若 结果.items.长度 不等于 2，直接返回 error.TestFailed
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
