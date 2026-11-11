// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/137060905
// LeetCode 451. 根据字符出现频率排序 — Zig 版（方案5）
const std = @import("std"); // 把 @import(「std」) 存入 std
const FC = struct { c: u8, cnt: i32, first: usize }; // 把 struct { 字符: u8, 计数: i32, first: usize } 存入 FC
fn frequencySort(s: []const u8, out: *std.ArrayList(u8)) void { // 定义函数/方法 frequencySort
    var fcs: [256]FC = undefined; // 把 undefined; 写入 var fcs: [256]FC
    var seen = [_]bool{false} ** 256; // 把 [_]bool{false} 乘 乘 256 存入 已见集合
    var n: usize = 0; // 把 0; 写入 var n: usize
    for (s, 0..) |c, i| { // for (字符串, 0..) 按位或 字符, 下标 i 按位或 {
        if (!seen[c]) { // 若 取反 已见集合[字符]
            seen[c] = true; // 把 true; 写入 seen[c]
            fcs[n] = .{ .c = c, .cnt = 0, .first = i }; // 把 { .字符 赋值为 字符, .计数 赋值为 0, .first 赋值为 下标 i }; 写入 fcs[n]
            n += 1; // 元素个数累加 1
        }
        for (0..n) |k| { // 让 下标 k 从 0 走到 元素个数 减一
            if (fcs[k].c == c) {
                fcs[k].cnt += 1;
                break;
            } // 若 fcs[下标 k].字符 等于 字符) { fcs[下标 k].计数 累加 1; break; }
        }
    }
    const S = struct { // 把 struct { 存入 S
        fn lt(_: void, a: FC, b: FC) bool { // 定义函数/方法 lt
            if (a.cnt != b.cnt) return a.cnt > b.cnt; // 若 数组.计数 不等于 b.计数，直接返回 数组.计数 超过 b.计数
            return a.first < b.first; // 返回 数组.first 小于 b.first
        }
    };
    std.sort.pdq(FC, fcs[0..n], {}, S.lt); // std.sort.pdq(FC, fcs[0..元素个数], {}, S.lt);
    for (0..n) |k| { // 让 下标 k 从 0 走到 元素个数 减一
        for (0..@intCast(fcs[k].cnt)) |_| out.append(fcs[k].c) catch unreachable; // 把 fcs[下标 k].字符 追加到列表尾部
    }
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var out = std.ArrayList(u8).init(std.heap.page_allocator); // 把 std.ArrayList(u8).init(std.堆.page_allocator) 存入 out
    defer out.deinit(); // defer out.deinit();
    frequencySort("tree", &out); // frequencySort(「tree」, 按位与 out);
    if (!std.mem.eql(u8, out.items, "eetr")) return error.TestFailed;
    out.clearRetainingCapacity(); // out.clearRetainingCapacity();
    frequencySort("", &out); // frequencySort(「」, 按位与 out);
    if (out.items.len != 0) return error.TestFailed; // 若 out.items.长度 不等于 0，直接返回 error.TestFailed
    out.clearRetainingCapacity(); // out.clearRetainingCapacity();
    frequencySort("cccaaa", &out); // frequencySort(「cccaaa」, 按位与 out);
    if (!std.mem.eql(u8, out.items, "cccaaa")) return error.TestFailed;
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
