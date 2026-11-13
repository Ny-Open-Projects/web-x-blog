// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145565975
// LeetCode 922. 按奇偶排序数组II — Zig 版（方案9）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn sortArrayByParityII(nums: []const i32, alloc: std.mem.Allocator) []i32 { // 定义函数/方法 sortArrayByParityII
    const sorted = alloc.dupe(i32, nums) catch unreachable; // 把 alloc.dupe(i32, 数组) catch unreachable 存入 sorted
    std.sort.pdq(i32, sorted, {}, std.sort.asc(i32)); // std.sort.pdq(i32, sorted, {}, std.sort.asc(i32));
    const res = alloc.alloc(i32, sorted.len) catch unreachable; // 把 alloc.alloc(i32, sorted.长度) catch unreachable 存入 结果
    var odd: usize = 1; // 把 1; 写入 var odd: usize
    var even: usize = 0; // 把 0; 写入 var even: usize
    for (sorted) |item| { // 逐个取出 sorted 的元素（item）
        if (@mod(item, 2) != 0) { // 若 @mod(item, 2) 不等于 0
            res[odd] = item; // 把 item; 写入 res[odd]
            odd += 2; // odd累加 2
        } else { // 否则
            res[even] = item; // 把 item; 写入 res[even]
            even += 2; // even累加 2
        }
    }
    return res; // 返回 结果
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator); // 把 std.堆.ArenaAllocator.init(std.堆.page_allocator) 存入 arena
    defer arena.deinit(); // defer arena.deinit();
    const got = sortArrayByParityII(&[_]i32{ 4, 2, 5, 7 }, arena.allocator());
    const want = [_]i32{ 2, 5, 4, 7 }; // 把 [_]i32{ 2, 5, 4, 7 } 存入 want
    if (got.len != want.len) return error.TestFailed; // 若 got.长度 不等于 want.长度，直接返回 error.TestFailed
    for (want, 0..) |w, i| if (got[i] != w) return error.TestFailed;
    const got2 = sortArrayByParityII(&[_]i32{ 2, 3 }, arena.allocator());
    if (got2[0] != 2 or got2[1] != 3) return error.TestFailed; // 若 got2[0] 不等于 2 or got2[1] 不等于 3，直接返回 error.TestFailed
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
