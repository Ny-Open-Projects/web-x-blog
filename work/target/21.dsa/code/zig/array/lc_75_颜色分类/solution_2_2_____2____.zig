// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134773756
// LeetCode 75. 颜色分类 — Zig 版（方案2）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn sortColors(nums: []i32) void { // 定义函数/方法 sortColors
    var p0: usize = 0; // 把 0; 写入 var p0: usize
    var cur: usize = 0; // 把 0; 写入 var cur: usize
    var p2: usize = nums.len - 1; // 把 数组.长度 减 1; 写入 var p2: usize
    while (cur <= p2) { // 循环，直到不满足「当前值 不超过 p2」
        if (nums[cur] == 0) { // 若 数组[当前值] 等于 0
            const t = nums[p0]; // 把 数组[p0] 存入 另一字符串
            nums[p0] = nums[cur]; // 把 数组[当前值]; 写入 nums[p0]
            nums[cur] = t; // 把 另一字符串; 写入 nums[cur]
            p0 += 1; // p0累加 1
            cur += 1; // 当前值累加 1
        } else if (nums[cur] == 2) { // 否则，若 数组[当前值] 等于 2
            const t = nums[cur]; // 把 数组[当前值] 存入 另一字符串
            nums[cur] = nums[p2]; // 把 数组[p2]; 写入 nums[cur]
            nums[p2] = t; // 把 另一字符串; 写入 nums[p2]
            if (p2 == 0) break; // 若 p2 等于 0) break;
            p2 -= 1; // p2累减 1
        } else cur += 1; // 否则
    }
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var v1 = [_]i32{ 2, 0, 2, 1, 1, 0 }; // 把 [_]i32{ 2, 0, 2, 1, 1, 0 } 存入 v1
    sortColors(&v1); // sortColors( 按位与 v1);
    if (v1[0] != 0 or v1[2] != 1 or v1[5] != 2) return error.TestFailed;
    var v2 = [_]i32{ 2, 0, 1 }; // 把 [_]i32{ 2, 0, 1 } 存入 v2
    sortColors(&v2); // sortColors( 按位与 v2);
    if (v2[0] != 0 or v2[2] != 2) return error.TestFailed; // 若 v2[0] 不等于 0 or v2[2] 不等于 2，直接返回 error.TestFailed
    std.debug.print("PASS\n", .{});
} // 全部用例通过，输出 PASS
