// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/136838836
// LeetCode 791. 自定义字符串排序 — Zig 版（方案2）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn customSortString(order: []const u8, s: []const u8, out: *std.ArrayList(u8)) void { // 定义函数/方法 customSortString
    var count = [_]usize{0} ** 26; // 把 [_]usize{0} 乘 乘 26 存入 计数
    for (s) |c| count[c - 'a'] += 1; // 逐个取出 字符串 的元素（字符）
    for (order) |c| { // 逐个取出 order 的元素（字符）
        const idx = c - 'a'; // 把 字符 减 '数组' 存入 idx
        for (0..count[idx]) |_| out.append(c) catch unreachable; // 把 字符 追加到列表尾部
        count[idx] = 0; // 把 0; 写入 count[idx]
    }
    for (count, 0..) |cnt, i| { // for (计数, 0..) 按位或 计数, 下标 i 按位或 {
        for (0..cnt) |_| out.append('a' + @as(u8, @intCast(i))) catch unreachable; // 让 _ 从 0 走到 计数 减一
    }
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var out = std.ArrayList(u8).init(std.heap.page_allocator); // 把 std.ArrayList(u8).init(std.堆.page_allocator) 存入 out
    defer out.deinit(); // defer out.deinit();
    customSortString("cba", "abcd", &out); // customSortString(「cba」, 「cba」, 按位与 out);
    if (!std.mem.eql(u8, out.items, "cbad")) return error.TestFailed;
    out.clearRetainingCapacity(); // out.clearRetainingCapacity();
    customSortString("bcafg", "abcd", &out); // customSortString(「bcafg」, 「bcafg」, 按位与 out);
    if (!std.mem.eql(u8, out.items, "bcad")) return error.TestFailed;
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
