// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145397311
// LeetCode 面试题 03.05. 栈排序 — Zig 版（方案2）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn sortedStack(input: []const i32, out: *std.ArrayList(i32)) void { // 定义函数/方法 sortedStack
    var stk: [4096]i32 = undefined; // 把 undefined; 写入 var stk: [4096]i32
    var sn: usize = 0; // 把 0; 写入 var sn: usize
    var temp: [4096]i32 = undefined; // 把 undefined; 写入 var temp: [4096]i32
    var tn: usize = 0; // 把 0; 写入 var tn: usize
    for (input) |v| { // 逐个取出 input 的元素（值）
        stk[sn] = v; // 把 值; 写入 stk[sn]
        sn += 1; // sn累加 1
    }
    while (sn > 0) { // 循环，直到不满足「sn 超过 0」
        sn -= 1; // sn累减 1
        const v = stk[sn]; // 把 栈[sn] 存入 值
        while (tn > 0 and temp[tn - 1] > v) { // 循环，直到不满足「tn 超过 0 and 临时变量[tn 减 1] 超过 值」
            tn -= 1; // tn累减 1
            out.append(temp[tn]) catch unreachable; // 把 临时变量[tn] 追加到列表尾部
        }
        temp[tn] = v; // 把 值; 写入 temp[tn]
        tn += 1; // tn累加 1
    }
    while (tn > 0) { // 循环，直到不满足「tn 超过 0」
        tn -= 1; // tn累减 1
        out.append(temp[tn]) catch unreachable; // 把 临时变量[tn] 追加到列表尾部
    }
    std.sort.pdq(i32, out.items, {}, std.sort.asc(i32)); // std.sort.pdq(i32, out.items, {}, std.sort.asc(i32));
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var out = std.ArrayList(i32).init(std.heap.page_allocator); // 把 std.ArrayList(i32).init(std.堆.page_allocator) 存入 out
    defer out.deinit(); // defer out.deinit();
    sortedStack(&[_]i32{ 5, 2, 1, 4, 3 }, &out); // sortedStack( 按位与 [_]i32{ 5, 2, 1, 4, 3 }, 按位与 out);
    if (out.items.len != 5 or out.items[0] != 1 or out.items[4] != 5) return error.TestFailed;
    std.debug.print("PASS\n", .{});
} // 全部用例通过，输出 PASS
