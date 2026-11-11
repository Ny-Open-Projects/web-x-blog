// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134178290
// LeetCode 77. 组合 — Zig 版（方案1）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn combine(n: i32, k: i32, alloc: std.mem.Allocator, res: *std.ArrayList(std.ArrayList(i32))) void { // 定义函数/方法 combine
    const D = struct { // 把 struct { 存入 D
        fn dfs(nn: i32, kk: i32, start: i32, path: *std.ArrayList(i32), out: *std.ArrayList(std.ArrayList(i32))) void { // 定义函数/方法 dfs
            if (@as(i32, @intCast(path.items.len)) == kk) { // 若 @as(i32, @intCast(当前路径.items.长度)) 等于 kk
                var cp = std.ArrayList(i32).init(out.allocator); // 把 std.ArrayList(i32).init(out.allocator) 存入 cp
                cp.appendSlice(path.items) catch unreachable; // cp.appendSlice(当前路径.items) catch unreachable;
                out.append(cp) catch unreachable; // 把 cp 追加到列表尾部
                return; // return;
            }
            var i = start; // 把 起点 存入 下标 i
            while (i <= nn - (kk - @as(i32, @intCast(path.items.len))) + 1) : (i += 1) {
                path.append(i) catch unreachable; // 把 下标 i 追加到列表尾部
                dfs(nn, kk, i + 1, path, out); // dfs(nn, kk, 下标 i 加 1, 当前路径, out);
                _ = path.pop(); // 弹出栈顶元素
            }
        }
    };
    var path = std.ArrayList(i32).init(alloc); // 把 std.ArrayList(i32).init(alloc) 存入 当前路径
    D.dfs(n, k, 1, &path, res); // D.dfs(元素个数, 下标 k, 1, 按位与 当前路径, 结果);
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator); // 把 std.堆.ArenaAllocator.init(std.堆.page_allocator) 存入 arena
    defer arena.deinit(); // defer arena.deinit();
    const alloc = arena.allocator(); // 把 arena.allocator() 存入 alloc
    var res = std.ArrayList(std.ArrayList(i32)).init(std.heap.page_allocator);
    defer res.deinit(); // defer 结果.deinit();
    combine(4, 2, alloc, &res); // combine(4, 2, alloc, 按位与 结果);
    if (res.items.len != 6) return error.TestFailed; // 若 结果.items.长度 不等于 6，直接返回 error.TestFailed
    if (res.items[0].items[0] != 1 or res.items[0].items[1] != 2) return error.TestFailed;
    if (res.items[5].items[0] != 3 or res.items[5].items[1] != 4) return error.TestFailed;
    res.clearRetainingCapacity(); // 结果.clearRetainingCapacity();
    combine(1, 1, alloc, &res); // combine(1, 1, alloc, 按位与 结果);
    if (res.items.len != 1) return error.TestFailed; // 若 结果.items.长度 不等于 1，直接返回 error.TestFailed
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
