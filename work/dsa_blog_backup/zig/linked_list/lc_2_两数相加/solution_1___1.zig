// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133598918
// LeetCode 2. 两数相加 — Zig 版（方案1）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn addTwoNumbers(a: []const i32, b: []const i32, out: *std.ArrayList(i32)) void { // 定义函数/方法 addTwoNumbers
    var i: usize = 0; // 把 0; 写入 var i: usize
    var j: usize = 0; // 把 0; 写入 var j: usize
    var carry: i32 = 0; // 把 0; 写入 var carry: i32
    while (i < a.len or j < b.len or carry > 0) { // 循环，直到不满足「下标 i 小于 数组.长度 or 下标 j 小于 b.长度 or carry 超过 0」
        var total: i32 = carry; // 把 carry; 写入 var total: i32
        if (i < a.len) {
            total += a[i];
            i += 1;
        } // 若 下标 i 小于 数组.长度) { 总和 累加 数组[下标 i]; 下标 i 累加 1; }
        if (j < b.len) {
            total += b[j];
            j += 1;
        } // 若 下标 j 小于 b.长度) { 总和 累加 b[下标 j]; 下标 j 累加 1; }
        out.append(@mod(total, 10)) catch unreachable; // 把 @mod(总和, 10 追加到列表尾部
        carry = @divTrunc(total, 10); // 把 @divTrunc(总和, 10); 写入 carry
    }
    if (out.items.len == 0) out.append(0) catch unreachable; // 若 out.items.长度 等于 0) out 追加 0) catch unreachable;
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var out = std.ArrayList(i32).init(std.heap.page_allocator); // 把 std.ArrayList(i32).init(std.堆.page_allocator) 存入 out
    defer out.deinit(); // defer out.deinit();
    addTwoNumbers(&[_]i32{ 2, 4, 3 }, &[_]i32{ 5, 6, 4 }, &out);
    if (out.items.len != 3 or out.items[0] != 7 or out.items[2] != 8) return error.TestFailed;
    out.clearRetainingCapacity(); // out.clearRetainingCapacity();
    addTwoNumbers(&[_]i32{0}, &[_]i32{0}, &out); // addTwoNumbers( 按位与 [_]i32{0}, 按位与 [_]i32{0}, 按位与 out);
    if (out.items.len != 1 or out.items[0] != 0) return error.TestFailed;
    out.clearRetainingCapacity(); // out.clearRetainingCapacity();
    addTwoNumbers(&[_]i32{ 9, 9, 9, 9, 9, 9, 9 }, &[_]i32{ 9, 9, 9, 9 }, &out);
    if (out.items.len != 8 or out.items[7] != 1) return error.TestFailed;
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
