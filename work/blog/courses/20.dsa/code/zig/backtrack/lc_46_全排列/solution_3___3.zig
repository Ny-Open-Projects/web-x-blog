// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133767953
// LeetCode 46. 全排列 — Zig 版（方案3）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn permute(nums: []const i32, alloc: std.mem.Allocator, res: *std.ArrayList(std.ArrayList(i32))) void { // 定义函数/方法 permute
    const D = struct { // 把 struct { 存入 D
        fn dfs(ns: []const i32, used: []bool, path: *std.ArrayList(i32), out: *std.ArrayList(std.ArrayList(i32))) void { // 定义函数/方法 dfs
            if (path.items.len == ns.len) { // 若 当前路径.items.长度 等于 ns.长度
                var cp = std.ArrayList(i32).init(out.allocator); // 把 std.ArrayList(i32).init(out.allocator) 存入 cp
                cp.appendSlice(path.items) catch unreachable; // cp.appendSlice(当前路径.items) catch unreachable;
                out.append(cp) catch unreachable; // 把 cp 追加到列表尾部
                return; // return;
            }
            for (ns, 0..) |v, i| { // for (ns, 0..) 按位或 值, 下标 i 按位或 {
                if (used[i]) continue; // 若 已用标记[下标 i]) continue;
                used[i] = true; // 把 true; 写入 used[i]
                path.append(v) catch unreachable; // 把 值 追加到列表尾部
                dfs(ns, used, path, out); // dfs(ns, 已用标记, 当前路径, out);
                _ = path.pop(); // 弹出栈顶元素
                used[i] = false; // 把 false; 写入 used[i]
            }
        }
    };
    const used = alloc.alloc(bool, nums.len) catch unreachable; // 把 alloc.alloc(bool, 数组.长度) catch unreachable 存入 已用标记
    @memset(used, false); // @memset(已用标记, false);
    var path = std.ArrayList(i32).init(alloc); // 把 std.ArrayList(i32).init(alloc) 存入 当前路径
    D.dfs(nums, used, &path, res); // D.dfs(数组, 已用标记, 按位与 当前路径, 结果);
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator); // 把 std.堆.ArenaAllocator.init(std.堆.page_allocator) 存入 arena
    defer arena.deinit(); // defer arena.deinit();
    const alloc = arena.allocator(); // 把 arena.allocator() 存入 alloc
    var res = std.ArrayList(std.ArrayList(i32)).init(std.heap.page_allocator);
    defer res.deinit(); // defer 结果.deinit();
    permute(&[_]i32{ 1, 2, 3 }, alloc, &res); // permute( 按位与 [_]i32{ 1, 2, 3 }, alloc, 按位与 结果);
    if (res.items.len != 6) return error.TestFailed; // 若 结果.items.长度 不等于 6，直接返回 error.TestFailed
    const w1 = [_]i32{ 1, 2, 3 }; // 把 [_]i32{ 1, 2, 3 } 存入 w1
    const w2 = [_]i32{ 1, 3, 2 }; // 把 [_]i32{ 1, 3, 2 } 存入 w2
    const w6 = [_]i32{ 3, 2, 1 }; // 把 [_]i32{ 3, 2, 1 } 存入 w6
    for (w1, 0..) |w, i| if (res.items[0].items[i] != w) return error.TestFailed;
    for (w2, 0..) |w, i| if (res.items[1].items[i] != w) return error.TestFailed;
    for (w6, 0..) |w, i| if (res.items[5].items[i] != w) return error.TestFailed;
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
