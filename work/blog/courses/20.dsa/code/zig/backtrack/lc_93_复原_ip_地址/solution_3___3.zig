// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/138771574
// LeetCode 93. 复原IP地址 — Zig 版（方案3）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn validSeg(s: []const u8) bool { // 定义函数/方法 validSeg
    if (s.len == 0 or s.len > 3) return false; // 若 字符串.长度 等于 0 or 字符串.长度 超过 3，直接返回 false
    if (s.len > 1 and s[0] == '0') return false; // 若 字符串.长度 超过 1 and 字符串[0] 等于 '0'，直接返回 false
    var v: i32 = 0; // 把 0; 写入 var v: i32
    for (s) |c| v = v * 10 + @as(i32, c - '0'); // 逐个取出 字符串 的元素（字符）
    return v <= 255; // 返回 值 不超过 255
}
fn restoreIpAddresses(s: []const u8, out: *std.ArrayList([]const u8), alloc: std.mem.Allocator) void { // 定义函数/方法 restoreIpAddresses
    const n = s.len; // 把 字符串.长度 存入 元素个数
    if (n < 4 or n > 12) return; // 若 元素个数 小于 4 or 元素个数 超过 12) return;
    var a: usize = 1; // 把 1; 写入 var a: usize
    while (a <= 3) : (a += 1) { // 循环，直到不满足「数组 不超过 3) : (数组 累加 1」
        var b: usize = 1; // 把 1; 写入 var b: usize
        while (b <= 3) : (b += 1) { // 循环，直到不满足「b 不超过 3) : (b 累加 1」
            var c: usize = 1; // 把 1; 写入 var c: usize
            while (c <= 3) : (c += 1) { // 循环，直到不满足「字符 不超过 3) : (字符 累加 1」
                if (a + b + c >= n) continue; // 若 数组 加 b 加 字符 不低于 元素个数) continue;
                const d = n - a - b - c; // 把 元素个数 减 数组 减 b 减 字符 存入 d
                if (d > 3) continue; // 若 d 超过 3) continue;
                const s1 = s[0..a]; // 把 字符串[0..数组] 存入 s1
                const s2 = s[a .. a + b]; // 把 字符串[数组 .. 数组 加 b] 存入 s2
                const s3 = s[a + b .. a + b + c]; // 把 字符串[数组 加 b .. 数组 加 b 加 字符] 存入 s3
                const s4 = s[a + b + c ..]; // 把 字符串[数组 加 b 加 字符 ..] 存入 s4
                if (validSeg(s1) and validSeg(s2) and validSeg(s3) and validSeg(s4)) {
                    var buf = std.ArrayList(u8).init(alloc); // 把 std.ArrayList(u8).init(alloc) 存入 buf
                    buf.appendSlice(s1) catch unreachable; // buf.appendSlice(s1) catch unreachable;
                    buf.append('.') catch unreachable; // 把 '.' 追加到列表尾部
                    buf.appendSlice(s2) catch unreachable; // buf.appendSlice(s2) catch unreachable;
                    buf.append('.') catch unreachable; // 把 '.' 追加到列表尾部
                    buf.appendSlice(s3) catch unreachable; // buf.appendSlice(s3) catch unreachable;
                    buf.append('.') catch unreachable; // 把 '.' 追加到列表尾部
                    buf.appendSlice(s4) catch unreachable; // buf.appendSlice(s4) catch unreachable;
                    out.append(buf.toOwnedSlice() catch unreachable) catch unreachable; // 把 buf.toOwnedSlice( 追加到列表尾部
                }
            }
        }
    }
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator); // 把 std.堆.ArenaAllocator.init(std.堆.page_allocator) 存入 arena
    defer arena.deinit(); // defer arena.deinit();
    const alloc = arena.allocator(); // 把 arena.allocator() 存入 alloc
    var out = std.ArrayList([]const u8).init(std.heap.page_allocator);
    defer out.deinit(); // defer out.deinit();
    restoreIpAddresses("25525511135", &out, alloc); // restoreIpAddresses(「25525511135」, 按位与 out, alloc);
    if (out.items.len != 2) return error.TestFailed; // 若 out.items.长度 不等于 2，直接返回 error.TestFailed
    if (!std.mem.eql(u8, out.items[0], "255.255.11.135")) return error.TestFailed;
    if (!std.mem.eql(u8, out.items[1], "255.255.111.35")) return error.TestFailed;
    out.clearRetainingCapacity(); // out.clearRetainingCapacity();
    restoreIpAddresses("0000", &out, alloc); // restoreIpAddresses(「0000」, 按位与 out, alloc);
    if (out.items.len != 1 or !std.mem.eql(u8, out.items[0], "0.0.0.0")) return error.TestFailed;
    out.clearRetainingCapacity(); // out.clearRetainingCapacity();
    restoreIpAddresses("abc", &out, alloc); // restoreIpAddresses(「abc」, 按位与 out, alloc);
    if (out.items.len != 0) return error.TestFailed; // 若 out.items.长度 不等于 0，直接返回 error.TestFailed
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
