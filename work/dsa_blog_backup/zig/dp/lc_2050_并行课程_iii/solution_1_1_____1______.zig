// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134859971
// LeetCode 2050. 并行课程III — Zig 版（方案1）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn minimumTime(n: usize, relations: []const [2]i32, time: []const i32) i32 { // 定义函数/方法 minimumTime
    var next_buf: [64][64]i32 = undefined; // 把 undefined; 写入 var next_buf: [64][64]i32
    var nnext: [64]usize = undefined; // 把 undefined; 写入 var nnext: [64]usize
    var indeg: [64]i32 = undefined; // 把 undefined; 写入 var indeg: [64]i32
    for (0..n + 1) |i| { // for (0..元素个数 加 1) 按位或 下标 i 按位或 {
        nnext[i] = 0; // 把 0; 写入 nnext[i]
        indeg[i] = 0; // 把 0; 写入 indeg[i]
    }
    for (relations) |r| { // 逐个取出 relations 的元素（右指针）
        const u: usize = @intCast(r[0]); // 把 @intCast(右指针[0]); 写入 const u: usize
        const v: usize = @intCast(r[1]); // 把 @intCast(右指针[1]); 写入 const v: usize
        next_buf[u][nnext[u]] = r[1]; // 把 右指针[1]; 写入 next_buf[u][nnext[u]]
        nnext[u] += 1; // nnext[u]累加 1
        indeg[v] += 1; // indeg[v]累加 1
    }
    var finish: [64]i32 = undefined; // 把 undefined; 写入 var finish: [64]i32
    for (0..n + 1) |i| finish[i] = 0; // 把 0; 写入 for (0..n + 1) |i| finish[i]
    var queue: [64]i32 = undefined; // 把 undefined; 写入 var queue: [64]i32
    var qn: usize = 0; // 把 0; 写入 var qn: usize
    for (1..n + 1) |c| { // for (1..元素个数 加 1) 按位或 字符 按位或 {
        if (indeg[c] == 0) { // 若 indeg[字符] 等于 0
            queue[qn] = @intCast(c); // 把 @intCast(字符); 写入 queue[qn]
            qn += 1; // qn累加 1
        }
    }
    var total: i32 = 0; // 把 0; 写入 var total: i32
    while (qn > 0) { // 循环，直到不满足「qn 超过 0」
        var nq: [64]i32 = undefined; // 把 undefined; 写入 var nq: [64]i32
        var nqn: usize = 0; // 把 0; 写入 var nqn: usize
        for (0..qn) |i| { // 让 下标 i 从 0 走到 qn 减一
            const c: usize = @intCast(queue[i]); // 把 @intCast(队列[下标 i]); 写入 const c: usize
            finish[c] += time[c - 1]; // finish[c]累加 time[字符 减 1]
            if (finish[c] > total) total = finish[c]; // 若 finish[字符] 超过 总和) 总和 赋值为 finish[字符];
            for (0..nnext[c]) |k| { // for (0..nnext[字符]) 按位或 下标 k 按位或 {
                const nx: usize = @intCast(next_buf[c][k]); // 把 @intCast(next_buf[字符][下标 k]); 写入 const nx: usize
                if (finish[nx] < finish[c]) finish[nx] = finish[c]; // 若 finish[nx] 小于 finish[字符]) finish[nx] 赋值为 finish[字符];
                indeg[nx] -= 1; // indeg[nx]累减 1
                if (indeg[nx] == 0) { // 若 indeg[nx] 等于 0
                    nq[nqn] = next_buf[c][k]; // 把 next_buf[字符][下标 k]; 写入 nq[nqn]
                    nqn += 1; // nqn累加 1
                }
            }
        }
        for (0..nqn) |i| queue[i] = nq[i]; // 让 下标 i 从 0 走到 nqn 减一
        qn = nqn; // 把 nqn; 写入 qn
    }
    return total; // 返回 总和
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    const r1 = [_][2]i32{ .{ 1, 3 }, .{ 2, 3 } }; // 把 [_][2]i32{ .{ 1, 3 }, .{ 2, 3 } } 存入 r1
    if (minimumTime(3, &r1, &[_]i32{ 3, 2, 5 }) != 8) return error.TestFailed;
    const r2 = [_][2]i32{ .{ 1, 2 }, .{ 2, 3 }, .{ 3, 4 }, .{ 4, 5 } };
    if (minimumTime(5, &r2, &[_]i32{ 1, 2, 3, 4, 5 }) != 15) return error.TestFailed;
    const empty_rel = [_][2]i32{}; // 把 [_][2]i32{} 存入 empty_rel
    if (minimumTime(1, &empty_rel, &[_]i32{5}) != 5) return error.TestFailed;
    std.debug.print("PASS\n", .{});
} // 全部用例通过，输出 PASS
