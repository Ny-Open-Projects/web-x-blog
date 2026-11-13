// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145114689
// LeetCode 27. 移除元素 — Zig 版（方案3）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn removeElement(nums: []i32, val: i32) i32 { // 定义函数/方法 removeElement
    var k: usize = 0; // 把 0; 写入 var k: usize
    for (nums) |v| { // 逐个取出 数组 的元素（值）
        if (v != val) { // 若 值 不等于 值
            nums[k] = v; // 把 值; 写入 nums[k]
            k += 1; // 下标 k累加 1
        }
    }
    return @intCast(k); // 返回 @intCast(下标 k)
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var v1 = [_]i32{ 3, 2, 2, 3 }; // 把 [_]i32{ 3, 2, 2, 3 } 存入 v1
    if (removeElement(&v1, 3) != 2) return error.TestFailed; // 若 removeElement( 按位与 v1, 3) 不等于 2，直接返回 error.TestFailed
    if (v1[0] != 2 or v1[1] != 2) return error.TestFailed; // 若 v1[0] 不等于 2 or v1[1] 不等于 2，直接返回 error.TestFailed
    var v2 = [_]i32{ 0, 1, 2, 2, 3, 0, 4, 2 }; // 把 [_]i32{ 0, 1, 2, 2, 3, 0, 4, 2 } 存入 v2
    if (removeElement(&v2, 2) != 5) return error.TestFailed; // 若 removeElement( 按位与 v2, 2) 不等于 5，直接返回 error.TestFailed
    std.debug.print("PASS\n", .{});
} // 全部用例通过，输出 PASS
