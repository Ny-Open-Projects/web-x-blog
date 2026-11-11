// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130701795
// LeetCode 43. 字符串相乘 — Zig 版（方案2）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn multiply(num1: []const u8, num2: []const u8, out: *std.ArrayList(u8)) void { // 定义函数/方法 multiply
    if (std.mem.eql(u8, num1, "0") or std.mem.eql(u8, num2, "0")) { // 若 std.mem.eql(u8, num1, 「0」) or std.mem.eql(u8, num2, 「0」
        out.append('0') catch unreachable; // 把 '0' 追加到列表尾部
        return; // return;
    }
    const m = num1.len; // 把 num1.长度 存入 映射表
    const n = num2.len; // 把 num2.长度 存入 元素个数
    var result = [_]i32{0} ** 512; // 把 [_]i32{0} 乘 乘 512 存入 结果
    var i: usize = m; // 把 映射表; 写入 var i: usize
    while (i > 0) { // 循环，直到不满足「下标 i 超过 0」
        i -= 1; // 下标 i累减 1
        var j: usize = n; // 把 元素个数; 写入 var j: usize
        while (j > 0) { // 循环，直到不满足「下标 j 超过 0」
            j -= 1; // 下标 j累减 1
            const mul = @as(i32, num1[i] - '0') * @as(i32, num2[j] - '0');
            const p1 = i + j; // 把 下标 i 加 下标 j 存入 p1
            const p2 = i + j + 1; // 把 下标 i 加 下标 j 加 1 存入 p2
            const total = mul + result[p2]; // 把 mul 加 结果[p2] 存入 总和
            result[p2] = @mod(total, 10); // 把 @mod(总和, 10); 写入 result[p2]
            result[p1] += @divTrunc(total, 10); // result[p1]累加 @divTrunc(总和, 10)
        }
    }
    var started = false; // 把 false 存入 started
    for (result[0 .. m + n]) |d| { // for (结果[0 .. 映射表 加 元素个数]) 按位或 d 按位或 {
        if (d != 0 or started) { // 若 d 不等于 0 or started
            out.append('0' + @as(u8, @intCast(d))) catch unreachable; // 把 '0' 加 @as(u8, @intCast(d 追加到列表尾部
            started = true; // 把 true; 写入 started
        }
    }
    if (out.items.len == 0) out.append('0') catch unreachable; // 若 out.items.长度 等于 0) out 追加 '0') catch unreachable;
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var out = std.ArrayList(u8).init(std.heap.page_allocator); // 把 std.ArrayList(u8).init(std.堆.page_allocator) 存入 out
    defer out.deinit(); // defer out.deinit();
    multiply("2", "3", &out); // multiply(「2」, 「2」, 按位与 out);
    if (!std.mem.eql(u8, out.items, "6")) return error.TestFailed; // 若 取反 std.mem.eql(u8, out.items, 「6」)，直接返回 error.TestFailed
    out.clearRetainingCapacity(); // out.clearRetainingCapacity();
    multiply("123", "456", &out); // multiply(「123」, 「123」, 按位与 out);
    if (!std.mem.eql(u8, out.items, "56088")) return error.TestFailed;
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
