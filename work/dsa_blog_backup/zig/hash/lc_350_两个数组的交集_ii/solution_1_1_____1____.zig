// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145568435
// LeetCode 350. 两个数组的交集 II — Zig 版（方案1）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn intersect(a: []const i32, b: []const i32, alloc: std.mem.Allocator, out: *std.ArrayList(i32)) void { // 定义函数/方法 intersect
    var mp = std.AutoHashMap(i32, i32).init(alloc); // 把 std.AutoHashMap(i32, i32).init(alloc) 存入 mp
    defer mp.deinit(); // defer mp.deinit();
    for (a) |v| { // 逐个取出 数组 的元素（值）
        const cur = mp.get(v) orelse 0; // 把 mp 查找 值) orelse 0 存入 当前值
        mp.put(v, cur + 1) catch unreachable; // mp.put(值, 当前值 加 1) catch unreachable;
    }
    for (b) |v| { // 逐个取出 b 的元素（值）
        if (mp.get(v)) |c| { // 若 mp 查找 值)) 按位或 字符 按位或
            if (c > 0) { // 若 字符 超过 0
                out.append(v) catch unreachable; // 把 值 追加到列表尾部
                mp.put(v, c - 1) catch unreachable; // mp.put(值, 字符 减 1) catch unreachable;
            }
        }
    }
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator); // 把 std.堆.ArenaAllocator.init(std.堆.page_allocator) 存入 arena
    defer arena.deinit(); // defer arena.deinit();
    const alloc = arena.allocator(); // 把 arena.allocator() 存入 alloc
    var out = std.ArrayList(i32).init(std.heap.page_allocator); // 把 std.ArrayList(i32).init(std.堆.page_allocator) 存入 out
    defer out.deinit(); // defer out.deinit();
    intersect(&[_]i32{ 1, 2, 2, 1 }, &[_]i32{ 2, 2 }, alloc, &out);
    if (out.items.len != 2 or out.items[0] != 2 or out.items[1] != 2) return error.TestFailed;
    out.clearRetainingCapacity(); // out.clearRetainingCapacity();
    intersect(&[_]i32{ 4, 9, 5 }, &[_]i32{ 9, 4, 9, 8, 4 }, alloc, &out);
    if (out.items.len != 2 or out.items[0] != 9 or out.items[1] != 4) return error.TestFailed;
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
