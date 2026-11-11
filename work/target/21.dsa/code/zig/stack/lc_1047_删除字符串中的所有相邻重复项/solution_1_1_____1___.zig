// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145295630
// LeetCode 1047. 删除字符串中的所有相邻重复项 — Zig 版（方案1）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn removeDuplicates(s: []const u8, out: *std.ArrayList(u8)) void { // 定义函数/方法 removeDuplicates
    var st: [8192]u8 = undefined; // 把 undefined; 写入 var st: [8192]u8
    var top: usize = 0; // 把 0; 写入 var top: usize
    for (s) |c| { // 逐个取出 字符串 的元素（字符）
        if (top > 0 and st[top - 1] == c) top -= 1 else { // 若 top 超过 0 and st[top 减 1] 等于 字符) top 累减 1 else
            st[top] = c; // 把 字符; 写入 st[top]
            top += 1; // top累加 1
        }
    }
    out.appendSlice(st[0..top]) catch unreachable; // out.appendSlice(st[0..top]) catch unreachable;
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var out = std.ArrayList(u8).init(std.heap.page_allocator); // 把 std.ArrayList(u8).init(std.堆.page_allocator) 存入 out
    defer out.deinit(); // defer out.deinit();
    removeDuplicates("abbaca", &out); // removeDuplicates(「abbaca」, 按位与 out);
    if (!std.mem.eql(u8, out.items, "ca")) return error.TestFailed; // 若 取反 std.mem.eql(u8, out.items, 「ca」)，直接返回 error.TestFailed
    out.clearRetainingCapacity(); // out.clearRetainingCapacity();
    removeDuplicates("azxxzy", &out); // removeDuplicates(「azxxzy」, 按位与 out);
    if (!std.mem.eql(u8, out.items, "ay")) return error.TestFailed; // 若 取反 std.mem.eql(u8, out.items, 「ay」)，直接返回 error.TestFailed
    out.clearRetainingCapacity(); // out.clearRetainingCapacity();
    removeDuplicates("", &out); // removeDuplicates(「」, 按位与 out);
    if (out.items.len != 0) return error.TestFailed; // 若 out.items.长度 不等于 0，直接返回 error.TestFailed
    std.debug.print("PASS\n", .{});
} // 全部用例通过，输出 PASS
