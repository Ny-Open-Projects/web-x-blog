// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135256754
// LeetCode 76. 最小覆盖子串 — Zig 版（方案2）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn minWindow(s: []const u8, t: []const u8, out: *std.ArrayList(u8)) void { // 定义函数/方法 minWindow
    out.clearRetainingCapacity(); // out.clearRetainingCapacity();
    if (s.len == 0 or t.len == 0) return; // 若 字符串.长度 等于 0 or 另一字符串.长度 等于 0) return;
    var target = [_]i32{0} ** 256; // 把 [_]i32{0} 乘 乘 256 存入 目标值
    var window = [_]i32{0} ** 256; // 把 [_]i32{0} 乘 乘 256 存入 window
    for (t) |c| target[c] += 1; // 逐个取出 另一字符串 的元素（字符）
    var required: i32 = 0; // 把 0; 写入 var required: i32
    for (target) |v| { // 逐个取出 目标值 的元素（值）
        if (v > 0) required += 1; // 若 值 超过 0) required 累加 1;
    }
    var left: usize = 0; // 把 0; 写入 var left: usize
    var formed: i32 = 0; // 把 0; 写入 var formed: i32
    var min_len: usize = std.math.maxInt(usize); // 把 std.math.maxInt(usize); 写入 var min_len: usize
    var min_left: usize = 0; // 把 0; 写入 var min_left: usize
    for (s, 0..) |c, right| { // for (字符串, 0..) 按位或 字符, 右边界 按位或 {
        window[c] += 1; // window[c]累加 1
        if (target[c] > 0 and window[c] == target[c]) formed += 1; // 若 目标值[字符] 超过 0 and window[字符] 等于 目标值[字符]) formed 累加 1;
        while (formed == required) { // 循环，直到不满足「formed 等于 required」
            if (right - left + 1 < min_len) {
                min_len = right - left + 1;
                min_left = left;
            }
            const lc = s[left]; // 把 字符串[左边界] 存入 lc
            window[lc] -= 1; // window[lc]累减 1
            if (target[lc] > 0 and window[lc] < target[lc]) formed -= 1; // 若 目标值[lc] 超过 0 and window[lc] 小于 目标值[lc]) formed 累减 1;
            left += 1; // 左边界累加 1
        }
    }
    if (min_len != std.math.maxInt(usize)) { // 若 min_len 不等于 std.math.maxInt(usize
        out.appendSlice(s[min_left .. min_left + min_len]) catch unreachable;
    }
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var out = std.ArrayList(u8).init(std.heap.page_allocator); // 把 std.ArrayList(u8).init(std.堆.page_allocator) 存入 out
    defer out.deinit(); // defer out.deinit();
    minWindow("ADOBECODEBANC", "ABC", &out); // minWindow(「ADOBECODEBANC」, 「ADOBECODEBANC」, 按位与 out);
    if (!std.mem.eql(u8, out.items, "BANC")) return error.TestFailed;
    minWindow("a", "a", &out); // minWindow(「数组」, 「数组」, 按位与 out);
    if (!std.mem.eql(u8, out.items, "a")) return error.TestFailed; // 若 取反 std.mem.eql(u8, out.items, 「数组」)，直接返回 error.TestFailed
    minWindow("a", "aa", &out); // minWindow(「数组」, 「数组」, 按位与 out);
    if (out.items.len != 0) return error.TestFailed; // 若 out.items.长度 不等于 0，直接返回 error.TestFailed
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
