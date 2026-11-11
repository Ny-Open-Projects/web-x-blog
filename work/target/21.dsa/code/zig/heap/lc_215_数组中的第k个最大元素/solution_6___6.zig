// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133471440
// LeetCode 215. 数组中的第K个最大元素 — Zig 版（方案6）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn findKthLargest(nums: []const i32, k: usize, alloc: std.mem.Allocator) i32 { // 定义函数/方法 findKthLargest
    // 最大堆（手写 up/down）
    var h = std.ArrayList(i32).init(alloc); // 把 std.ArrayList(i32).init(alloc) 存入 h
    defer h.deinit(); // defer h.deinit();
    for (nums) |v| { // 逐个取出 数组 的元素（值）
        h.append(v) catch unreachable; // 把 值 追加到列表尾部
        var i = h.items.len - 1; // 把 h.items.长度 减 1 存入 下标 i
        while (i > 0) { // 循环，直到不满足「下标 i 超过 0」
            const p = (i - 1) / 2; // 把 (下标 i 减 1) 除以 2 存入 节点
            if (h.items[i] <= h.items[p]) break; // 若 h.items[下标 i] 不超过 h.items[节点]) break;
            const t = h.items[i];
            h.items[i] = h.items[p];
            h.items[p] = t;
            i = p; // 把 节点; 写入 下标 i
        }
    }
    var t: usize = 0; // 把 0; 写入 var t: usize
    while (t + 1 < k) : (t += 1) { // 循环，直到不满足「另一字符串 加 1 小于 下标 k) : (另一字符串 累加 1」
        const last = h.pop().?; // 把 h 弹出 ).? 存入 last
        if (h.items.len > 0) { // 若 h.items.长度 超过 0
            h.items[0] = last; // 把 last; 写入 h.items[0]
            var i: usize = 0; // 把 0; 写入 var i: usize
            while (true) { // 循环，直到不满足「true」
                const l = 2 * i + 1; // 把 2 乘 下标 i 加 1 存入 左指针
                const r = 2 * i + 2; // 把 2 乘 下标 i 加 2 存入 右指针
                var m = i; // 把 下标 i 存入 映射表
                if (l < h.items.len and h.items[l] > h.items[m]) m = l;
                if (r < h.items.len and h.items[r] > h.items[m]) m = r;
                if (m == i) break; // 若 映射表 等于 下标 i) break;
                const tmp = h.items[i];
                h.items[i] = h.items[m];
                h.items[m] = tmp;
                i = m; // 把 映射表; 写入 下标 i
            }
        }
    }
    return h.items[0]; // 返回 h.items[0]
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator); // 把 std.堆.ArenaAllocator.init(std.堆.page_allocator) 存入 arena
    defer arena.deinit(); // defer arena.deinit();
    if (findKthLargest(&[_]i32{ 3, 2, 1, 5, 6, 4 }, 2, arena.allocator()) != 5) return error.TestFailed;
    if (findKthLargest(&[_]i32{ 3, 2, 3, 1, 2, 4, 5, 5, 6 }, 4, arena.allocator()) != 4) return error.TestFailed;
    if (findKthLargest(&[_]i32{1}, 1, arena.allocator()) != 1) return error.TestFailed;
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
