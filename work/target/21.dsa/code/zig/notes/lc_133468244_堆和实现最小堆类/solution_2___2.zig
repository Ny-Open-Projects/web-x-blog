// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133468244
// 数据结构与算法之堆: 堆和实现最小堆类 — Zig 版（方案2）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn minHeapPopAll(input: []const i32, out: *std.ArrayList(i32)) void { // 定义函数/方法 minHeapPopAll
    var h: [4096]i32 = undefined; // 把 undefined; 写入 var h: [4096]i32
    var hn: usize = 0; // 把 0; 写入 var hn: usize
    for (input) |v| { // 逐个取出 input 的元素（值）
        h[hn] = v; // 把 值; 写入 h[hn]
        var i = hn; // 把 hn 存入 下标 i
        hn += 1; // hn累加 1
        while (i > 0) { // 循环，直到不满足「下标 i 超过 0」
            const p = (i - 1) / 2; // 把 (下标 i 减 1) 除以 2 存入 节点
            if (h[p] <= h[i]) break; // 若 h[节点] 不超过 h[下标 i]) break;
            const t = h[p]; // 把 h[节点] 存入 另一字符串
            h[p] = h[i]; // 把 h[下标 i]; 写入 h[p]
            h[i] = t; // 把 另一字符串; 写入 h[i]
            i = p; // 把 节点; 写入 下标 i
        }
    }
    while (hn > 0) { // 循环，直到不满足「hn 超过 0」
        out.append(h[0]) catch unreachable; // 把 h[0] 追加到列表尾部
        hn -= 1; // hn累减 1
        const last = h[hn]; // 把 h[hn] 存入 last
        if (hn > 0) { // 若 hn 超过 0
            h[0] = last; // 把 last; 写入 h[0]
            var i: usize = 0; // 把 0; 写入 var i: usize
            while (true) { // 循环，直到不满足「true」
                const l = 2 * i + 1; // 把 2 乘 下标 i 加 1 存入 左指针
                const r = 2 * i + 2; // 把 2 乘 下标 i 加 2 存入 右指针
                var m = i; // 把 下标 i 存入 映射表
                if (l < hn and h[l] < h[m]) m = l; // 若 左指针 小于 hn and h[左指针] 小于 h[映射表]) 映射表 赋值为 左指针;
                if (r < hn and h[r] < h[m]) m = r; // 若 右指针 小于 hn and h[右指针] 小于 h[映射表]) 映射表 赋值为 右指针;
                if (m == i) break; // 若 映射表 等于 下标 i) break;
                const t = h[i]; // 把 h[下标 i] 存入 另一字符串
                h[i] = h[m]; // 把 h[映射表]; 写入 h[i]
                h[m] = t; // 把 另一字符串; 写入 h[m]
                i = m; // 把 映射表; 写入 下标 i
            }
        }
    }
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var out = std.ArrayList(i32).init(std.heap.page_allocator); // 把 std.ArrayList(i32).init(std.堆.page_allocator) 存入 out
    defer out.deinit(); // defer out.deinit();
    minHeapPopAll(&[_]i32{ 3, 1, 6, 5, 2, 4 }, &out); // minHeapPopAll( 按位与 [_]i32{ 3, 1, 6, 5, 2, 4 }, 按位与 out);
    for (out.items, 0..) |v, i| if (v != @as(i32, @intCast(i + 1))) return error.TestFailed;
    std.debug.print("PASS\n", .{});
} // 全部用例通过，输出 PASS
