// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145078849
// LeetCode 341. 扁平化嵌套列表迭代器 — Zig 版（方案1）
const std = @import("std"); // 把 @import(「std」) 存入 std
const NI = union(enum) { // 把 union(enum) { 存入 NI
    int: i32,
    list: []const NI,
};
fn flatten(items: []const NI, out: *std.ArrayList(i32)) void { // 定义函数/方法 flatten
    for (items) |it| { // 逐个取出 items 的元素（it）
        switch (it) { // switch (it) {
            .int => |v| out.append(v) catch unreachable,
            .list => |l| flatten(l, out),
        }
    }
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator); // 把 std.堆.ArenaAllocator.init(std.堆.page_allocator) 存入 arena
    defer arena.deinit(); // defer arena.deinit();
    const alloc = arena.allocator(); // 把 arena.allocator() 存入 alloc
    const inner = try alloc.alloc(NI, 2); // 把 try alloc.alloc(NI, 2) 存入 inner
    inner[0] = .{ .int = 3 }; // 把 { .int 赋值为 3 }; 写入 inner[0]
    inner[1] = .{ .int = 4 }; // 把 { .int 赋值为 4 }; 写入 inner[1]
    const top = try alloc.alloc(NI, 3); // 把 try alloc.alloc(NI, 3) 存入 top
    top[0] = .{ .int = 1 }; // 把 { .int 赋值为 1 }; 写入 top[0]
    top[1] = .{ .int = 2 }; // 把 { .int 赋值为 2 }; 写入 top[1]
    top[2] = .{ .list = inner }; // 把 { .列表 赋值为 inner }; 写入 top[2]
    var out = std.ArrayList(i32).init(std.heap.page_allocator); // 把 std.ArrayList(i32).init(std.堆.page_allocator) 存入 out
    defer out.deinit(); // defer out.deinit();
    flatten(top, &out); // flatten(top, 按位与 out);
    if (out.items.len != 4 or out.items[0] != 1 or out.items[3] != 4) return error.TestFailed;
    std.debug.print("PASS\n", .{});
} // 全部用例通过，输出 PASS
