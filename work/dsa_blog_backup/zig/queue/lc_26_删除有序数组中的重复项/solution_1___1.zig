// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145114454
// LeetCode 26. 删除有序数组中的重复项 — Zig 版
const std = @import("std"); // 把 @import(「std」) 存入 std

// 方案1：k 指针 —— 相邻比较，不同元素逐个写入前 k 个位置
fn removeDuplicates(nums: []i32) usize { // 定义函数/方法 removeDuplicates
    if (nums.len == 0) return 0; // 若 数组.长度 等于 0，直接返回 0
    var k: usize = 1; // 把 1; 写入 var k: usize
    var i: usize = 1; // 把 1; 写入 var i: usize
    while (i < nums.len) : (i += 1) { // 循环，直到不满足「下标 i 小于 数组.长度) : (下标 i 累加 1」
        if (nums[i] != nums[i - 1]) { // 若 数组[下标 i] 不等于 数组[下标 i 减 1]
            nums[k] = nums[i]; // 把 数组[下标 i]; 写入 nums[k]
            k += 1; // 下标 k累加 1
        }
    }
    return k; // 返回 下标 k
}

fn eqArr(a: []const i32, b: []const i32) bool { // 定义函数/方法 eqArr
    if (a.len != b.len) return false; // 若 数组.长度 不等于 b.长度，直接返回 false
    for (a, b) |x, y| { // for (数组, b) 按位或 x, y 按位或 {
        if (x != y) return false; // 若 x 不等于 y，直接返回 false
    }
    return true; // 返回 true
}

pub fn main() !void { // 程序入口：跑内嵌自测用例
    // 与 TS 事实源内嵌用例一致
    const c1 = [_]i32{ 1, 1, 2 }; // 把 [_]i32{ 1, 1, 2 } 存入 c1
    const c2 = [_]i32{ 1, 2, 3 }; // 把 [_]i32{ 1, 2, 3 } 存入 c2
    const c3 = [_]i32{}; // 把 [_]i32{} 存入 c3
    const p1 = [_]i32{ 1, 2 }; // 把 [_]i32{ 1, 2 } 存入 p1
    const p2 = [_]i32{ 1, 2, 3 }; // 把 [_]i32{ 1, 2, 3 } 存入 p2
    const p3 = [_]i32{}; // 把 [_]i32{} 存入 p3

    const Case = struct { in: []const i32, k: usize, pre: []const i32 };
    const cases = [_]Case{ // 把 [_]Case{ 存入 cases
        .{ .in = &c1, .k = 2, .pre = &p1 },
        .{ .in = &c2, .k = 3, .pre = &p2 },
        .{ .in = &c3, .k = 0, .pre = &p3 },
    };
    for (cases, 0..) |c, idx| { // for (cases, 0..) 按位或 字符, idx 按位或 {
        var buf: [8]i32 = undefined; // 把 undefined; 写入 var buf: [8]i32
        @memcpy(buf[0..c.in.len], c.in); // @memcpy(buf[0..字符.in.长度], 字符.in);
        const got = removeDuplicates(buf[0..c.in.len]); // 把 removeDuplicates(buf[0..字符.in.长度]) 存入 got
        if (got != c.k or !eqArr(buf[0..got], c.pre)) { // 若 got 不等于 字符.下标 k or 取反 eqArr(buf[0..got], 字符.前缀和
            std.debug.print("FAIL case {d}: k={d}\n", .{ idx, got }); // 打印输出
            return error.TestFailed; // 返回 error.TestFailed
        }
    }
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
