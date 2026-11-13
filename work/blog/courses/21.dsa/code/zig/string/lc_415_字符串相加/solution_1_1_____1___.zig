// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130736023
// LeetCode 415. 字符串相加 — Zig 版（方案1）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn addStrings(a: []const u8, b: []const u8, out: *std.ArrayList(u8)) void { // 定义函数/方法 addStrings
    var i: isize = @as(isize, @intCast(a.len)) - 1; // 把 @as(isize, @intCast(数组.长度)) 减 1; 写入 var i: isize
    var j: isize = @as(isize, @intCast(b.len)) - 1; // 把 @as(isize, @intCast(b.长度)) 减 1; 写入 var j: isize
    var carry: u8 = 0; // 把 0; 写入 var carry: u8
    while (i >= 0 or j >= 0 or carry > 0) { // 循环，直到不满足「下标 i 不低于 0 or 下标 j 不低于 0 or carry 超过 0」
        var total: u16 = carry; // 把 carry; 写入 var total: u16
        if (i >= 0) {
            total += a[@intCast(i)] - '0';
            i -= 1;
        } // 若 下标 i 不低于 0) { 总和 累加 数组[@intCast(下标 i)] 减 '0'; 下标 i 累减 1; }
        if (j >= 0) {
            total += b[@intCast(j)] - '0';
            j -= 1;
        } // 若 下标 j 不低于 0) { 总和 累加 b[@intCast(下标 j)] 减 '0'; 下标 j 累减 1; }
        out.append('0' + @as(u8, @intCast(total % 10))) catch unreachable; // 把 '0' 加 @as(u8, @intCast(总和 对…取模 10 追加到列表尾部
        carry = @intCast(total / 10); // 把 @intCast(总和 除以 10); 写入 carry
    }
    if (out.items.len == 0) out.append('0') catch unreachable; // 若 out.items.长度 等于 0) out 追加 '0') catch unreachable;
    std.mem.reverse(u8, out.items); // 反转
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var out = std.ArrayList(u8).init(std.heap.page_allocator); // 把 std.ArrayList(u8).init(std.堆.page_allocator) 存入 out
    defer out.deinit(); // defer out.deinit();
    addStrings("11", "123", &out); // addStrings(「11」, 「11」, 按位与 out);
    if (!std.mem.eql(u8, out.items, "134")) return error.TestFailed; // 若 取反 std.mem.eql(u8, out.items, 「134」)，直接返回 error.TestFailed
    out.clearRetainingCapacity(); // out.clearRetainingCapacity();
    addStrings("456", "77", &out); // addStrings(「456」, 「456」, 按位与 out);
    if (!std.mem.eql(u8, out.items, "533")) return error.TestFailed; // 若 取反 std.mem.eql(u8, out.items, 「533」)，直接返回 error.TestFailed
    out.clearRetainingCapacity(); // out.clearRetainingCapacity();
    addStrings("0", "0", &out); // addStrings(「0」, 「0」, 按位与 out);
    if (!std.mem.eql(u8, out.items, "0")) return error.TestFailed; // 若 取反 std.mem.eql(u8, out.items, 「0」)，直接返回 error.TestFailed
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
