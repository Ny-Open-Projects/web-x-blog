// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130846022
// LeetCode 151. 反转字符串中的单词 — Zig 版（方案3）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn reverseWords(s: []const u8, out: *std.ArrayList(u8)) void { // 定义函数/方法 reverseWords
    var words: [8192][]const u8 = undefined; // 把 undefined; 写入 var words: [8192][]const u8
    var wn: usize = 0; // 把 0; 写入 var wn: usize
    var it = std.mem.tokenizeAny(u8, s, " \t"); // 把 std.mem.tokenizeAny(u8, 字符串, 「 」) 存入 it
    while (it.next()) |w| { // 循环，直到不满足「it.下一个()) 按位或 权重 按位或」
        words[wn] = w; // 把 权重; 写入 words[wn]
        wn += 1; // wn累加 1
    }
    var first = true; // 把 true 存入 first
    var i: usize = wn; // 把 wn; 写入 var i: usize
    while (i > 0) { // 循环，直到不满足「下标 i 超过 0」
        i -= 1; // 下标 i累减 1
        if (!first) out.append(' ') catch unreachable; // 若 取反 first) out 追加 ' ') catch unreachable;
        first = false; // 把 false; 写入 first
        out.appendSlice(words[i]) catch unreachable; // out.appendSlice(单词列表[下标 i]) catch unreachable;
    }
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var out = std.ArrayList(u8).init(std.heap.page_allocator); // 把 std.ArrayList(u8).init(std.堆.page_allocator) 存入 out
    defer out.deinit(); // defer out.deinit();
    reverseWords("the sky is blue", &out); // reverseWords(「the sky is blue」, 按位与 out);
    if (!std.mem.eql(u8, out.items, "blue is sky the")) return error.TestFailed;
    out.clearRetainingCapacity(); // out.clearRetainingCapacity();
    reverseWords("  hello world  ", &out); // reverseWords(「 hello world 」, 按位与 out);
    if (!std.mem.eql(u8, out.items, "world hello")) return error.TestFailed;
    out.clearRetainingCapacity(); // out.clearRetainingCapacity();
    reverseWords("a good   example", &out); // reverseWords(「数组 good example」, 按位与 out);
    if (!std.mem.eql(u8, out.items, "example good a")) return error.TestFailed;
    std.debug.print("PASS\n", .{});
} // 全部用例通过，输出 PASS
