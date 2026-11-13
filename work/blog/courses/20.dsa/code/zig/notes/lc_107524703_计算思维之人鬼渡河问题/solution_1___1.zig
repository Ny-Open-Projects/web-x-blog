// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107524703
// LeetCode 107524703. 人鬼渡河问题 — Zig 版（方案1：安全判定谓词）
const std = @import("std"); // 把 @import(「std」) 存入 std

fn isSafe(r: i32, g: i32) bool { // 定义判定函数 isSafe
    return 0 <= r and r <= 3 and 0 <= g and g <= 3 and (r == 0 or r == 3 or r == g);
}

pub fn main() !void { // 程序入口：跑内嵌自测用例
    const Case = struct { r: i32, g: i32, want: bool }; // 把 struct { 右指针: i32, g: i32, want: bool } 存入 Case
    const cases = [_]Case{ // 把 [_]Case{ 存入 cases
        .{ .r = 3, .g = 3, .want = true },
        .{ .r = 3, .g = 1, .want = true },
        .{ .r = 2, .g = 2, .want = true },
        .{ .r = 1, .g = 3, .want = false },
        .{ .r = 0, .g = 0, .want = true },
    };
    for (cases) |c| { // 逐个取出 cases 的元素（字符）
        if (isSafe(c.r, c.g) != c.want) { // 若 isSafe(字符.右指针, 字符.g) 不等于 字符.want
            std.debug.print("isSafe({d},{d}) failed\n", .{ c.r, c.g }); // 打印输出
            return error.TestFailed; // 返回 error.TestFailed
        }
    }
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
