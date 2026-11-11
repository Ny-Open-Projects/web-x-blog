// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107849059
// Gnome Sort（侏儒排序）+ Bubble Sort（冒泡排序）+ 贪心找零 对比
const std = @import("std"); // 把 @import(「std」) 存入 std

fn gnomeSort(a: []i32) void { // 定义函数/方法 gnomeSort
    var i: usize = 0; // 把 0; 写入 var i: usize
    while (i < a.len) { // 循环，直到不满足「下标 i 小于 数组.长度」
        if (i == 0 or a[i] >= a[i - 1]) { // 若 下标 i 等于 0 or 数组[下标 i] 不低于 数组[下标 i 减 1]
            i += 1; // 下标 i累加 1
        } else { // 否则
            const t = a[i - 1]; // 把 数组[下标 i 减 1] 存入 另一字符串
            a[i - 1] = a[i]; // 把 数组[下标 i]; 写入 a[i - 1]
            a[i] = t; // 把 另一字符串; 写入 a[i]
            i -= 1; // 下标 i累减 1
        }
    }
}

fn bubbleSort(a: []i32) void { // 定义函数/方法 bubbleSort
    var swapped = true; // 把 true 存入 swapped
    while (swapped) { // 循环，直到不满足「swapped」
        swapped = false; // 把 false; 写入 swapped
        var i: usize = 0; // 把 0; 写入 var i: usize
        while (i + 1 < a.len) : (i += 1) { // 循环，直到不满足「下标 i 加 1 小于 数组.长度) : (下标 i 累加 1」
            if (a[i] > a[i + 1]) { // 若 数组[下标 i] 超过 数组[下标 i 加 1]
                const t = a[i]; // 把 数组[下标 i] 存入 另一字符串
                a[i] = a[i + 1]; // 把 数组[下标 i 加 1]; 写入 a[i]
                a[i + 1] = t; // 把 另一字符串; 写入 a[i + 1]
                swapped = true; // 把 true; 写入 swapped
            }
        }
    }
}

fn coinChange(coins: []const i32, amount: i32) i32 { // 定义函数/方法 coinChange
    var cs: [64]i32 = undefined; // 把 undefined; 写入 var cs: [64]i32
    var n: usize = 0; // 把 0; 写入 var n: usize
    for (coins) |c| { // 逐个取出 硬币面额 的元素（字符）
        cs[n] = c; // 把 字符; 写入 cs[n]
        n += 1; // 元素个数累加 1
    }
    // 降序冒泡
    var i: usize = 0; // 把 0; 写入 var i: usize
    while (i + 1 < n) : (i += 1) { // 循环，直到不满足「下标 i 加 1 小于 元素个数) : (下标 i 累加 1」
        var j: usize = 0; // 把 0; 写入 var j: usize
        while (j + 1 < n - i) : (j += 1) { // 循环，直到不满足「下标 j 加 1 小于 元素个数 减 下标 i) : (下标 j 累加 1」
            if (cs[j] < cs[j + 1]) { // 若 cs[下标 j] 小于 cs[下标 j 加 1]
                const t = cs[j]; // 把 cs[下标 j] 存入 另一字符串
                cs[j] = cs[j + 1]; // 把 cs[下标 j 加 1]; 写入 cs[j]
                cs[j + 1] = t; // 把 另一字符串; 写入 cs[j + 1]
            }
        }
    }
    var remaining = amount; // 把 目标金额 存入 remaining
    var count: i32 = 0; // 把 0; 写入 var count: i32
    for (cs[0..n]) |coin| { // for (cs[0..元素个数]) 按位或 coin 按位或 {
        while (remaining >= coin) { // 循环，直到不满足「remaining 不低于 coin」
            remaining -= coin; // remaining累减 coin
            count += 1; // 计数累加 1
        }
    }
    if (remaining == 0) return count; // 若 remaining 等于 0，直接返回 计数
    return -1; // 返回 减 1
}

pub fn main() !void { // 程序入口：跑内嵌自测用例
    var gpa = std.heap.GeneralPurposeAllocator(.{}){}; // 把 std.堆.GeneralPurposeAllocator(.{}){} 存入 gpa
    defer _ = gpa.deinit(); // 把 gpa.deinit(); 写入 defer _
    const allocator = gpa.allocator(); // 把 gpa.allocator() 存入 allocator

    var g = [_]i32{ 3, 2, 1 }; // 把 [_]i32{ 3, 2, 1 } 存入 g
    gnomeSort(&g); // gnomeSort( 按位与 g);
    const want = [_]i32{ 1, 2, 3 }; // 把 [_]i32{ 1, 2, 3 } 存入 want
    if (!std.mem.eql(i32, &g, &want)) return error.TestFailed; // 若 取反 std.mem.eql(i32, 按位与 g, 按位与 want)，直接返回 error.TestFailed

    var b = [_]i32{ 3, 2, 1 }; // 把 [_]i32{ 3, 2, 1 } 存入 b
    bubbleSort(&b); // bubbleSort( 按位与 b);
    if (!std.mem.eql(i32, &b, &want)) return error.TestFailed; // 若 取反 std.mem.eql(i32, 按位与 b, 按位与 want)，直接返回 error.TestFailed

    const coins = [_]i32{ 1, 5, 10, 25 }; // 把 [_]i32{ 1, 5, 10, 25 } 存入 硬币面额
    if (coinChange(&coins, 63) != 6) return error.TestFailed; // 若 coinChange( 按位与 硬币面额, 63) 不等于 6，直接返回 error.TestFailed

    _ = allocator; // 把 allocator; 写入 _
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
