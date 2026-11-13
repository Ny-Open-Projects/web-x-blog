// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107836586
// LeetCode 107836586. Big-O 记号 — Zig 版（Big-O 记号：按最高次非零系数给出多项式复杂度分类）
const std = @import("std"); // 把 @import(「std」) 存入 std

// coeffs[i] 为 n^i 的系数，返回最高次非零项对应的复杂度记号
fn classify(buf: []u8, coeffs: []const i64) ![]u8 { // 定义函数/方法 classify
    var deg: usize = coeffs.len; // 把 coeffs.长度; 写入 var deg: usize
    while (deg > 0) { // 循环，直到不满足「deg 超过 0」
        deg -= 1; // deg累减 1
        if (coeffs[deg] != 0) { // 若 coeffs[deg] 不等于 0
            if (deg > 1) { // 若 deg 超过 1
                return std.fmt.bufPrint(buf, "O(n^{d})", .{deg}); // 返回 std.fmt.bufPrint(buf, 「O(元素个数 按位异或 {d})」, .{deg})
            } else if (deg == 1) { // 否则，若 deg 等于 1
                return std.fmt.bufPrint(buf, "O(n)", .{}); // 返回 std.fmt.bufPrint(buf, 「O(元素个数)」, .{})
            } else { // 否则
                return std.fmt.bufPrint(buf, "O(1)", .{}); // 返回 std.fmt.bufPrint(buf, 「O(1)」, .{})
            }
        }
    }
    return std.fmt.bufPrint(buf, "O(1)", .{}); // 返回 std.fmt.bufPrint(buf, 「O(1)」, .{})
}

pub fn main() !void { // 程序入口：跑内嵌自测用例
    var buf: [32]u8 = undefined; // 把 undefined; 写入 var buf: [32]u8
    const Case = struct { coeffs: []const i64, want: []const u8 }; // 把 struct { coeffs: []const i64, want: []const u8 } 存入 Case
    const cases = [_]Case{ // 把 [_]Case{ 存入 cases
        .{ .coeffs = &[_]i64{ 1, 0, 0, 0 }, .want = "O(1)" },
        .{ .coeffs = &[_]i64{ 0, 0, 0, 35 }, .want = "O(n^3)" },
        .{ .coeffs = &[_]i64{ 0, 0, 1, 0 }, .want = "O(n^2)" },
        .{ .coeffs = &[_]i64{ 0, 1, 0, 0 }, .want = "O(n)" },
    };
    for (cases, 0..) |c, idx| { // for (cases, 0..) 按位或 字符, idx 按位或 {
        const got = try classify(&buf, c.coeffs); // 把 try classify( 按位与 buf, 字符.coeffs) 存入 got
        if (!std.mem.eql(u8, got, c.want)) { // 若 取反 std.mem.eql(u8, got, 字符.want
            std.debug.print("case {d} failed: got {s} want {s}\n", .{ idx, got, c.want }); // 打印输出
            return error.TestFailed; // 返回 error.TestFailed
        }
    }
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
