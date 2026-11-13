// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133596542
// LeetCode 17. 电话号码的字母组合 — Zig 版（方案6）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn letterCombinations(digits: []const u8, alloc: std.mem.Allocator, res: *std.ArrayList([]const u8)) void { // 定义函数/方法 letterCombinations
    if (digits.len == 0) return; // 若 digits.长度 等于 0) return;
    const map = [_][]const u8{ "", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz" };
    res.append("") catch unreachable; // 把 「」 追加到列表尾部
    for (digits) |c| { // 逐个取出 digits 的元素（字符）
        const letters = map[c - '0']; // 把 映射表[字符 减 '0'] 存入 letters
        var next = std.ArrayList([]const u8).init(alloc); // 把 std.ArrayList([]const u8).init(alloc) 存入 下一个
        for (res.items) |prefix| { // 逐个取出 结果.items 的元素（prefix）
            for (letters) |lc| { // 逐个取出 letters 的元素（lc）
                var buf = std.ArrayList(u8).init(alloc); // 把 std.ArrayList(u8).init(alloc) 存入 buf
                buf.appendSlice(prefix) catch unreachable; // buf.appendSlice(prefix) catch unreachable;
                buf.append(lc) catch unreachable; // 把 lc 追加到列表尾部
                next.append(buf.toOwnedSlice() catch unreachable) catch unreachable; // 把 buf.toOwnedSlice( 追加到列表尾部
            }
        }
        res.* = next; // 把 下一个; 写入 res.*
    }
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator); // 把 std.堆.ArenaAllocator.init(std.堆.page_allocator) 存入 arena
    defer arena.deinit(); // defer arena.deinit();
    const alloc = arena.allocator(); // 把 arena.allocator() 存入 alloc
    var res = std.ArrayList([]const u8).init(std.heap.page_allocator); // 把 std.ArrayList([]const u8).init(std.堆.page_allocator) 存入 结果
    defer res.deinit(); // defer 结果.deinit();
    letterCombinations("23", alloc, &res); // letterCombinations(「23」, alloc, 按位与 结果);
    if (res.items.len != 9) return error.TestFailed; // 若 结果.items.长度 不等于 9，直接返回 error.TestFailed
    if (!std.mem.eql(u8, res.items[0], "ad") or !std.mem.eql(u8, res.items[8], "cf")) return error.TestFailed;
    res.clearRetainingCapacity(); // 结果.clearRetainingCapacity();
    letterCombinations("", alloc, &res); // letterCombinations(「」, alloc, 按位与 结果);
    if (res.items.len != 0) return error.TestFailed; // 若 结果.items.长度 不等于 0，直接返回 error.TestFailed
    res.clearRetainingCapacity(); // 结果.clearRetainingCapacity();
    letterCombinations("2", alloc, &res); // letterCombinations(「2」, alloc, 按位与 结果);
    if (res.items.len != 3) return error.TestFailed; // 若 结果.items.长度 不等于 3，直接返回 error.TestFailed
    std.debug.print("PASS\n", .{});
} // 全部用例通过，输出 PASS
