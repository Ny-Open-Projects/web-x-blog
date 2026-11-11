// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133772625
// LeetCode 131. 分割回文串 — Zig 版（方案1）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn isPal(s: []const u8) bool { // 定义判定函数 isPal
    if (s.len == 0) return true; // 若 字符串.长度 等于 0，直接返回 true
    var i: usize = 0; // 把 0; 写入 var i: usize
    var j: usize = s.len - 1; // 把 字符串.长度 减 1; 写入 var j: usize
    while (i < j) : ({ // 循环，直到不满足「下标 i 小于 下标 j) : (」
        i += 1; // 下标 i累加 1
        j -= 1; // 下标 j累减 1
    }) { // }) {
        if (s[i] != s[j]) return false; // 若 字符串[下标 i] 不等于 字符串[下标 j]，直接返回 false
    }
    return true; // 返回 true
}
fn partition(s: []const u8, alloc: std.mem.Allocator, res: *std.ArrayList(std.ArrayList([]const u8))) void { // 定义函数/方法 partition
    const D = struct { // 把 struct { 存入 D
        fn dfs(str: []const u8, start: usize, path: *std.ArrayList([]const u8), out: *std.ArrayList(std.ArrayList([]const u8)), a: std.mem.Allocator) void { // 定义函数/方法 dfs
            if (start == str.len) { // 若 起点 等于 str.长度
                var cp = std.ArrayList([]const u8).init(out.allocator); // 把 std.ArrayList([]const u8).init(out.allocator) 存入 cp
                cp.appendSlice(path.items) catch unreachable; // cp.appendSlice(当前路径.items) catch unreachable;
                out.append(cp) catch unreachable; // 把 cp 追加到列表尾部
                return; // return;
            }
            var e = start + 1; // 把 起点 加 1 存入 e
            while (e <= str.len) : (e += 1) { // 循环，直到不满足「e 不超过 str.长度) : (e 累加 1」
                const sub = str[start..e]; // 把 str[起点..e] 存入 sub
                if (isPal(sub)) { // 若 isPal(sub
                    path.append(a.dupe(u8, sub) catch unreachable) catch unreachable; // 把 数组.dupe(u8, sub 追加到列表尾部
                    dfs(str, e, path, out, a); // dfs(str, e, 当前路径, out, 数组);
                    _ = path.pop(); // 弹出栈顶元素
                }
            }
        }
    };
    var path = std.ArrayList([]const u8).init(alloc); // 把 std.ArrayList([]const u8).init(alloc) 存入 当前路径
    D.dfs(s, 0, &path, res, alloc); // D.dfs(字符串, 0, 按位与 当前路径, 结果, alloc);
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator); // 把 std.堆.ArenaAllocator.init(std.堆.page_allocator) 存入 arena
    defer arena.deinit(); // defer arena.deinit();
    const alloc = arena.allocator(); // 把 arena.allocator() 存入 alloc
    var res = std.ArrayList(std.ArrayList([]const u8)).init(std.heap.page_allocator);
    defer res.deinit(); // defer 结果.deinit();
    partition("aab", alloc, &res); // partition(「aab」, alloc, 按位与 结果);
    if (res.items.len != 2) return error.TestFailed; // 若 结果.items.长度 不等于 2，直接返回 error.TestFailed
    if (res.items[0].items.len != 3 or !std.mem.eql(u8, res.items[0].items[0], "a")) return error.TestFailed;
    if (res.items[1].items.len != 2 or !std.mem.eql(u8, res.items[1].items[0], "aa")) return error.TestFailed;
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
