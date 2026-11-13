// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130734875
// LeetCode 682. 棒球比赛 — Zig 版（方案2）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn calPoints(ops: []const []const u8) i32 { // 定义函数/方法 calPoints
    var st: [4096]i32 = undefined; // 把 undefined; 写入 var st: [4096]i32
    var top: usize = 0; // 把 0; 写入 var top: usize
    for (ops) |op| { // 逐个取出 ops 的元素（op）
        if (std.mem.eql(u8, op, "+")) { // 若 std.mem.eql(u8, op, 「 加 」
            st[top] = st[top - 1] + st[top - 2]; // 把 st[top 减 1] 加 st[top 减 2]; 写入 st[top]
            top += 1; // top累加 1
        } else if (std.mem.eql(u8, op, "D")) { // 否则，若 std.mem.eql(u8, op, 「D」
            st[top] = st[top - 1] * 2; // 把 st[top 减 1] 乘 2; 写入 st[top]
            top += 1; // top累加 1
        } else if (std.mem.eql(u8, op, "C")) { // 否则，若 std.mem.eql(u8, op, 「C」
            top -= 1; // top累减 1
        } else { // 否则
            st[top] = std.fmt.parseInt(i32, op, 10) catch unreachable; // 把 std.fmt.转整数(i32, op, 10) catch unreachable; 写入 st[top]
            top += 1; // top累加 1
        }
    }
    var sum: i32 = 0; // 把 0; 写入 var sum: i32
    for (0..top) |i| sum += st[i]; // 让 下标 i 从 0 走到 top 减一
    return sum; // 返回 累计和
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    if (calPoints(&[_][]const u8{ "5", "2", "C", "D", "+" }) != 30) return error.TestFailed;
    if (calPoints(&[_][]const u8{ "5", "-2", "4", "C", "D", "9", "+", "+" }) != 27) return error.TestFailed;
    if (calPoints(&[_][]const u8{ "1", "C" }) != 0) return error.TestFailed;
    std.debug.print("PASS\n", .{});
} // 全部用例通过，输出 PASS
