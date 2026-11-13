// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/105893757
// 栈排序分析 — Zig 版（方案4）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn stackSort(input: []const i32, out: []i32) void { // 定义函数/方法 stackSort
    var st: [4096]i32 = undefined; // 把 undefined; 写入 var st: [4096]i32
    var top: usize = 0; // 把 0; 写入 var top: usize
    for (input) |v| { // 逐个取出 input 的元素（值）
        st[top] = v; // 把 值; 写入 st[top]
        top += 1; // top累加 1
    }
    for (0..input.len) |i| { // 逐个取出 0..input.长度 的元素（下标 i）
        top -= 1; // top累减 1
        out[i] = st[top]; // 把 st[top]; 写入 out[i]
    }
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var out: [8]i32 = undefined; // 把 undefined; 写入 var out: [8]i32
    stackSort(&[_]i32{ 3, 1, 5, 2, 4 }, &out); // stackSort( 按位与 [_]i32{ 3, 1, 5, 2, 4 }, 按位与 out);
    const want = [_]i32{ 4, 2, 5, 1, 3 }; // 把 [_]i32{ 4, 2, 5, 1, 3 } 存入 want
    for (want, 0..) |w, i| if (out[i] != w) return error.TestFailed;
    std.debug.print("PASS\n", .{});
} // 全部用例通过，输出 PASS
