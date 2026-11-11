// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134368624
// LeetCode 71. 简化路径 — Zig 版（方案1）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn simplifyPath(path: []const u8, out: *std.ArrayList(u8)) void { // 定义函数/方法 simplifyPath
    var parts: [1024][]const u8 = undefined; // 把 undefined; 写入 var parts: [1024][]const u8
    var pn: usize = 0; // 把 0; 写入 var pn: usize
    var it = std.mem.splitScalar(u8, path, '/'); // 把 std.mem.splitScalar(u8, 当前路径, ' 除以 ') 存入 it
    while (it.next()) |part| { // 循环，直到不满足「it.下一个()) 按位或 part 按位或」
        if (part.len == 0 or std.mem.eql(u8, part, ".")) continue; // 若 part.长度 等于 0 or std.mem.eql(u8, part, 「.」)) continue;
        if (std.mem.eql(u8, part, "..")) { // 若 std.mem.eql(u8, part, 「..」
            if (pn > 0) pn -= 1; // 若 pn 超过 0) pn 累减 1;
        } else { // 否则
            parts[pn] = part; // 把 part; 写入 parts[pn]
            pn += 1; // pn累加 1
        }
    }
    if (pn == 0) { // 若 pn 等于 0
        out.append('/') catch unreachable; // 把 ' 除以 ' 追加到列表尾部
        return; // return;
    }
    for (0..pn) |i| { // 让 下标 i 从 0 走到 pn 减一
        out.append('/') catch unreachable; // 把 ' 除以 ' 追加到列表尾部
        out.appendSlice(parts[i]) catch unreachable; // out.appendSlice(parts[下标 i]) catch unreachable;
    }
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var out = std.ArrayList(u8).init(std.heap.page_allocator); // 把 std.ArrayList(u8).init(std.堆.page_allocator) 存入 out
    defer out.deinit(); // defer out.deinit();
    simplifyPath("/home/", &out); // simplifyPath(「 除以 home 除以 」, 按位与 out);
    if (!std.mem.eql(u8, out.items, "/home")) return error.TestFailed;
    out.clearRetainingCapacity(); // out.clearRetainingCapacity();
    simplifyPath("/../", &out); // simplifyPath(「 除以 .. 除以 」, 按位与 out);
    if (!std.mem.eql(u8, out.items, "/")) return error.TestFailed;
    out.clearRetainingCapacity(); // out.clearRetainingCapacity();
    simplifyPath("/home//foo/", &out); // simplifyPath(" 除以 home
    if (!std.mem.eql(u8, out.items, "/home/foo")) return error.TestFailed;
    out.clearRetainingCapacity(); // out.clearRetainingCapacity();
    simplifyPath("/a/./b/../../c/", &out);
    if (!std.mem.eql(u8, out.items, "/c")) return error.TestFailed;
    std.debug.print("PASS\n", .{});
} // 全部用例通过，输出 PASS
