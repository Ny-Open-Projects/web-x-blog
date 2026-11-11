// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134577890
// LeetCode 179. 最大数 — Zig 版（方案2）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn largestNumber(nums: []const i32, alloc: std.mem.Allocator, out: *std.ArrayList(u8)) void { // 定义函数/方法 largestNumber
    var strs = std.ArrayList([]const u8).init(alloc); // 把 std.ArrayList([]const u8).init(alloc) 存入 strs
    for (nums) |v| { // 逐个取出 数组 的元素（值）
        var buf: [16]u8 = undefined; // 把 undefined; 写入 var buf: [16]u8
        const s = std.fmt.bufPrint(&buf, "{d}", .{v}) catch unreachable;
        strs.append(alloc.dupe(u8, s) catch unreachable) catch unreachable; // 把 alloc.dupe(u8, 字符串 追加到列表尾部
    }
    const S = struct { // 把 struct { 存入 S
        fn lt(_: void, a: []const u8, b: []const u8) bool { // 定义函数/方法 lt
            var ab: [64]u8 = undefined; // 把 undefined; 写入 var ab: [64]u8
            var ba: [64]u8 = undefined; // 把 undefined; 写入 var ba: [64]u8
            const ablen = std.fmt.bufPrint(&ab, "{s}{s}", .{ a, b }) catch unreachable;
            const balen = std.fmt.bufPrint(&ba, "{s}{s}", .{ b, a }) catch unreachable;
            return std.mem.order(u8, ablen, balen) == .gt; // 返回 std.mem.order(u8, ablen, balen) 等于 .gt
        }
    };
    std.sort.pdq([]const u8, strs.items, {}, S.lt); // std.sort.pdq([]const u8, strs.items, {}, S.lt);
    if (strs.items.len > 0 and std.mem.eql(u8, strs.items[0], "0")) { // 若 strs.items.长度 超过 0 and std.mem.eql(u8, strs.items[0], 「0」
        out.appendSlice("0") catch unreachable; // out.appendSlice(「0」) catch unreachable;
        return; // return;
    }
    for (strs.items) |s| out.appendSlice(s) catch unreachable; // 逐个取出 strs.items 的元素（字符串）
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator); // 把 std.堆.ArenaAllocator.init(std.堆.page_allocator) 存入 arena
    defer arena.deinit(); // defer arena.deinit();
    const alloc = arena.allocator(); // 把 arena.allocator() 存入 alloc
    var out = std.ArrayList(u8).init(std.heap.page_allocator); // 把 std.ArrayList(u8).init(std.堆.page_allocator) 存入 out
    defer out.deinit(); // defer out.deinit();
    largestNumber(&[_]i32{ 10, 2 }, alloc, &out); // largestNumber( 按位与 [_]i32{ 10, 2 }, alloc, 按位与 out);
    if (!std.mem.eql(u8, out.items, "210")) return error.TestFailed; // 若 取反 std.mem.eql(u8, out.items, 「210」)，直接返回 error.TestFailed
    out.clearRetainingCapacity(); // out.clearRetainingCapacity();
    largestNumber(&[_]i32{ 3, 30, 34, 5, 9 }, alloc, &out);
    if (!std.mem.eql(u8, out.items, "9534330")) return error.TestFailed;
    out.clearRetainingCapacity(); // out.clearRetainingCapacity();
    largestNumber(&[_]i32{ 0, 0 }, alloc, &out); // largestNumber( 按位与 [_]i32{ 0, 0 }, alloc, 按位与 out);
    if (!std.mem.eql(u8, out.items, "0")) return error.TestFailed; // 若 取反 std.mem.eql(u8, out.items, 「0」)，直接返回 error.TestFailed
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
