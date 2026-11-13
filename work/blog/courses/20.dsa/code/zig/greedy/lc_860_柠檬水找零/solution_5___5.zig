// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135167617
// LeetCode 860. 柠檬水找零 — Zig 版（方案5）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn lemonadeChange(bills: []const i32) bool { // 定义函数/方法 lemonadeChange
    var f5: i32 = 0; // 把 0; 写入 var f5: i32
    var f10: i32 = 0; // 把 0; 写入 var f10: i32
    for (bills) |b| { // 逐个取出 bills 的元素（b）
        if (b == 5) { // 若 b 等于 5
            f5 += 1; // f5累加 1
        } else if (b == 10) { // 否则，若 b 等于 10
            f10 += 1; // f10累加 1
            f5 -= 1; // f5累减 1
        } else { // 否则
            if (f10 > 0) { // 若 f10 超过 0
                f10 -= 1; // f10累减 1
                f5 -= 1; // f5累减 1
            } else { // 否则
                f5 -= 3; // f5累减 3
            }
        }
        if (f5 < 0) return false; // 若 f5 小于 0，直接返回 false
    }
    return true; // 返回 true
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    if (!lemonadeChange(&[_]i32{ 5, 5, 5, 10, 20 })) return error.TestFailed;
    if (lemonadeChange(&[_]i32{ 5, 5, 10, 10, 20 })) return error.TestFailed;
    if (!lemonadeChange(&[_]i32{ 5, 5, 5, 5, 20 })) return error.TestFailed;
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
