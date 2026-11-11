// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133865307
// LeetCode 39. 组合总和 — Zig 版（方案1）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn combinationSum(cands: []const i32, target: i32, alloc: std.mem.Allocator, res: *std.ArrayList(std.ArrayList(i32))) void { // 定义函数/方法 combinationSum
    const D = struct { // 把 struct { 存入 D
        fn dfs(cs: []const i32, start: usize, remaining: i32, path: *std.ArrayList(i32), out: *std.ArrayList(std.ArrayList(i32))) void { // 定义函数/方法 dfs
            if (remaining == 0) { // 若 remaining 等于 0
                var cp = std.ArrayList(i32).init(out.allocator); // 把 std.ArrayList(i32).init(out.allocator) 存入 cp
                cp.appendSlice(path.items) catch unreachable; // cp.appendSlice(当前路径.items) catch unreachable;
                out.append(cp) catch unreachable; // 把 cp 追加到列表尾部
                return; // return;
            }
            if (remaining < 0) return; // 若 remaining 小于 0) return;
            for (start..cs.len) |i| { // 逐个取出 起点..cs.长度 的元素（下标 i）
                path.append(cs[i]) catch unreachable; // 把 cs[下标 i] 追加到列表尾部
                dfs(cs, i, remaining - cs[i], path, out); // dfs(cs, 下标 i, remaining 减 cs[下标 i], 当前路径, out);
                _ = path.pop(); // 弹出栈顶元素
            }
        }
    };
    var path = std.ArrayList(i32).init(alloc); // 把 std.ArrayList(i32).init(alloc) 存入 当前路径
    D.dfs(cands, 0, target, &path, res); // D.dfs(cands, 0, 目标值, 按位与 当前路径, 结果);
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator); // 把 std.堆.ArenaAllocator.init(std.堆.page_allocator) 存入 arena
    defer arena.deinit(); // defer arena.deinit();
    const alloc = arena.allocator(); // 把 arena.allocator() 存入 alloc
    var res = std.ArrayList(std.ArrayList(i32)).init(std.heap.page_allocator);
    defer res.deinit(); // defer 结果.deinit();
    combinationSum(&[_]i32{ 2, 3, 6, 7 }, 7, alloc, &res); // combinationSum( 按位与 [_]i32{ 2, 3, 6, 7 }, 7, alloc, 按位与 结果);
    if (res.items.len != 2) return error.TestFailed; // 若 结果.items.长度 不等于 2，直接返回 error.TestFailed
    if (res.items[0].items.len != 3 or res.items[0].items[0] != 2 or res.items[0].items[2] != 3) return error.TestFailed;
    if (res.items[1].items.len != 1 or res.items[1].items[0] != 7) return error.TestFailed;
    res.clearRetainingCapacity(); // 结果.clearRetainingCapacity();
    combinationSum(&[_]i32{ 2, 3, 5 }, 8, alloc, &res); // combinationSum( 按位与 [_]i32{ 2, 3, 5 }, 8, alloc, 按位与 结果);
    if (res.items.len != 3) return error.TestFailed; // 若 结果.items.长度 不等于 3，直接返回 error.TestFailed
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
