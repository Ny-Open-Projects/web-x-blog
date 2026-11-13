// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133493400
// LeetCode 347. 前K个高频元素 — Zig 版（方案4）
const std = @import("std"); // 把 @import(「std」) 存入 std
const VC = struct { v: i32, c: i64 }; // 把 struct { 值: i32, 字符: i64 } 存入 VC
fn topKFrequent(nums: []const i32, k: usize, alloc: std.mem.Allocator, out: *std.ArrayList(i32)) void { // 定义函数/方法 topKFrequent
    var vcs = std.ArrayList(VC).init(alloc); // 把 std.ArrayList(VC).init(alloc) 存入 vcs
    for (nums) |v| { // 逐个取出 数组 的元素（值）
        var found = false; // 把 false 存入 found
        for (vcs.items) |*vc| { // for (vcs.items) 按位或 乘 vc 按位或 {
            if (vc.v == v) {
                vc.c += 1;
                found = true;
                break;
            } // 若 vc.值 等于 值) { vc.字符 累加 1; found 赋值为 true; break; }
        }
        if (!found) vcs.append(.{ .v = v, .c = 1 }) catch unreachable;
    }
    const S = struct { // 把 struct { 存入 S
        fn lt(_: void, a: VC, b: VC) bool { // 定义函数/方法 lt
            if (a.c != b.c) return a.c > b.c; // 若 数组.字符 不等于 b.字符，直接返回 数组.字符 超过 b.字符
            return a.v < b.v; // 返回 数组.值 小于 b.值
        }
    };
    std.sort.pdq(VC, vcs.items, {}, S.lt); // std.sort.pdq(VC, vcs.items, {}, S.lt);
    for (vcs.items[0..@min(k, vcs.items.len)]) |vc| out.append(vc.v) catch unreachable; // 把 vc.值 追加到列表尾部
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator); // 把 std.堆.ArenaAllocator.init(std.堆.page_allocator) 存入 arena
    defer arena.deinit(); // defer arena.deinit();
    const alloc = arena.allocator(); // 把 arena.allocator() 存入 alloc
    var out = std.ArrayList(i32).init(std.heap.page_allocator); // 把 std.ArrayList(i32).init(std.堆.page_allocator) 存入 out
    defer out.deinit(); // defer out.deinit();
    topKFrequent(&[_]i32{ 1, 1, 1, 2, 2, 3 }, 2, alloc, &out);
    if (out.items.len != 2) return error.TestFailed; // 若 out.items.长度 不等于 2，直接返回 error.TestFailed
    std.sort.pdq(i32, out.items, {}, std.sort.asc(i32)); // std.sort.pdq(i32, out.items, {}, std.sort.asc(i32));
    if (out.items[0] != 1 or out.items[1] != 2) return error.TestFailed;
    out.clearRetainingCapacity(); // out.clearRetainingCapacity();
    topKFrequent(&[_]i32{1}, 1, alloc, &out); // topKFrequent( 按位与 [_]i32{1}, 1, alloc, 按位与 out);
    if (out.items.len != 1 or out.items[0] != 1) return error.TestFailed;
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
