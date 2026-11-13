// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135096603
// LeetCode 455. 分发饼干 — Zig 版（方案1）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn findContentChildren(g_in: []const i32, s_in: []const i32, alloc: std.mem.Allocator) i32 { // 定义函数/方法 findContentChildren
    const g = alloc.dupe(i32, g_in) catch unreachable; // 把 alloc.dupe(i32, g_in) catch unreachable 存入 g
    const s = alloc.dupe(i32, s_in) catch unreachable; // 把 alloc.dupe(i32, s_in) catch unreachable 存入 字符串
    std.sort.pdq(i32, g, {}, std.sort.asc(i32)); // std.sort.pdq(i32, g, {}, std.sort.asc(i32));
    std.sort.pdq(i32, s, {}, std.sort.asc(i32)); // std.sort.pdq(i32, 字符串, {}, std.sort.asc(i32));
    var child: usize = 0; // 把 0; 写入 var child: usize
    var cookie: usize = 0; // 把 0; 写入 var cookie: usize
    while (child < g.len and cookie < s.len) { // 循环，直到不满足「子节点 小于 g.长度 and cookie 小于 字符串.长度」
        if (s[cookie] >= g[child]) child += 1; // 若 字符串[cookie] 不低于 g[子节点]) 子节点 累加 1;
        cookie += 1; // cookie累加 1
    }
    return @intCast(child); // 返回 @intCast(子节点)
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator); // 把 std.堆.ArenaAllocator.init(std.堆.page_allocator) 存入 arena
    defer arena.deinit(); // defer arena.deinit();
    const alloc = arena.allocator(); // 把 arena.allocator() 存入 alloc
    if (findContentChildren(&[_]i32{ 1, 2, 3 }, &[_]i32{ 1, 1 }, alloc) != 1) return error.TestFailed;
    if (findContentChildren(&[_]i32{ 1, 2 }, &[_]i32{ 1, 2, 3 }, alloc) != 2) return error.TestFailed;
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
