// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145565975
// LeetCode 557. 反转字符串中的单词III — Zig 版（方案7）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn reverseWords(s: []const u8, out: *std.ArrayList(u8)) void { // 定义函数/方法 reverseWords
    var it = std.mem.tokenizeScalar(u8, s, ' '); // 把 std.mem.tokenizeScalar(u8, 字符串, ' ') 存入 it
    var first = true; // 把 true 存入 first
    while (it.next()) |w| { // 循环，直到不满足「it.下一个()) 按位或 权重 按位或」
        if (!first) out.append(' ') catch unreachable; // 若 取反 first) out 追加 ' ') catch unreachable;
        first = false; // 把 false; 写入 first
        var i: usize = w.len; // 把 权重.长度; 写入 var i: usize
        while (i > 0) { // 循环，直到不满足「下标 i 超过 0」
            i -= 1; // 下标 i累减 1
            out.append(w[i]) catch unreachable; // 把 权重[下标 i] 追加到列表尾部
        }
    }
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var out = std.ArrayList(u8).init(std.heap.page_allocator); // 把 std.ArrayList(u8).init(std.堆.page_allocator) 存入 out
    defer out.deinit(); // defer out.deinit();
    reverseWords("Let's take LeetCode contest", &out);
    if (!std.mem.eql(u8, out.items, "s'teL ekat edoCteeL tsetnoc")) return error.TestFailed;
    out.clearRetainingCapacity(); // out.clearRetainingCapacity();
    reverseWords("God Ding", &out); // reverseWords(「God Ding」, 按位与 out);
    if (!std.mem.eql(u8, out.items, "doG gniD")) return error.TestFailed;
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
