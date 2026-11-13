// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/138290964
// LeetCode 482. 密钥格式化 — Zig 版（方案1）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn licenseKeyFormatting(s: []const u8, k: usize, out: *std.ArrayList(u8)) void { // 定义函数/方法 licenseKeyFormatting
    var cleaned: [8192]u8 = undefined; // 把 undefined; 写入 var cleaned: [8192]u8
    var n: usize = 0; // 把 0; 写入 var n: usize
    for (s) |c| { // 逐个取出 字符串 的元素（字符）
        if (c != '-') { // 若 字符 不等于 ' 减 '
            cleaned[n] = std.ascii.toUpper(c); // 把 std.ascii.toUpper(字符); 写入 cleaned[n]
            n += 1; // 元素个数累加 1
        }
    }
    if (n == 0) return; // 若 元素个数 等于 0) return;
    const first = n % k; // 把 元素个数 对…取模 下标 k 存入 first
    var idx: usize = 0; // 把 0; 写入 var idx: usize
    if (first > 0) { // 若 first 超过 0
        for (0..first) |_| { // 让 _ 从 0 走到 first 减一
            out.append(cleaned[idx]) catch unreachable; // 把 cleaned[idx] 追加到列表尾部
            idx += 1; // idx累加 1
        }
        if (idx < n) out.append('-') catch unreachable; // 若 idx 小于 元素个数) out 追加 ' 减 ') catch unreachable;
    }
    while (idx < n) { // 循环，直到不满足「idx 小于 元素个数」
        for (0..k) |_| { // 让 _ 从 0 走到 下标 k 减一
            out.append(cleaned[idx]) catch unreachable; // 把 cleaned[idx] 追加到列表尾部
            idx += 1; // idx累加 1
        }
        if (idx < n) out.append('-') catch unreachable; // 若 idx 小于 元素个数) out 追加 ' 减 ') catch unreachable;
    }
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var out = std.ArrayList(u8).init(std.heap.page_allocator); // 把 std.ArrayList(u8).init(std.堆.page_allocator) 存入 out
    defer out.deinit(); // defer out.deinit();
    licenseKeyFormatting("5F3Z-2e-9-w", 4, &out); // licenseKeyFormatting(「5F3Z 减 2e 减 9 减 权重」, 4, 按位与 out);
    if (!std.mem.eql(u8, out.items, "5F3Z-2E9W")) return error.TestFailed;
    out.clearRetainingCapacity(); // out.clearRetainingCapacity();
    licenseKeyFormatting("2-5g-3-J", 2, &out); // licenseKeyFormatting(「2 减 5g 减 3 减 J」, 2, 按位与 out);
    if (!std.mem.eql(u8, out.items, "2-5G-3J")) return error.TestFailed;
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
