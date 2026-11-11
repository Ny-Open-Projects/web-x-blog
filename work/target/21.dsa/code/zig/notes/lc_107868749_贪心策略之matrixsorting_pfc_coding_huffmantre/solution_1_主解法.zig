// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107868749
// LeetCode 107868749. 贪心策略 — Zig 版（贪心策略之 matrixSort / PFC 编码 / Huffman 树）
const std = @import("std"); // 把 @import(「std」) 存入 std

// 每列升序排序后每行升序排序
fn matrixSort(m: *[3][3]i32) void { // 定义函数/方法 matrixSort
    var c: usize = 0; // 把 0; 写入 var c: usize
    while (c < 3) : (c += 1) { // 循环，直到不满足「字符 小于 3) : (字符 累加 1」
        var i: usize = 0; // 把 0; 写入 var i: usize
        while (i < 2) : (i += 1) { // 循环，直到不满足「下标 i 小于 2) : (下标 i 累加 1」
            var j: usize = 0; // 把 0; 写入 var j: usize
            while (j < 2 - i) : (j += 1) { // 循环，直到不满足「下标 j 小于 2 减 下标 i) : (下标 j 累加 1」
                if (m[j][c] > m[j + 1][c]) { // 若 映射表[下标 j][字符] 超过 映射表[下标 j 加 1][字符]
                    const t = m[j][c]; // 把 映射表[下标 j][字符] 存入 另一字符串
                    m[j][c] = m[j + 1][c]; // 把 映射表[下标 j 加 1][字符]; 写入 m[j][c]
                    m[j + 1][c] = t; // 把 另一字符串; 写入 m[j + 1][c]
                }
            }
        }
    }
    var r: usize = 0; // 把 0; 写入 var r: usize
    while (r < 3) : (r += 1) { // 循环，直到不满足「右指针 小于 3) : (右指针 累加 1」
        var bi: usize = 0; // 把 0; 写入 var bi: usize
        while (bi < 2) : (bi += 1) { // 循环，直到不满足「bi 小于 2) : (bi 累加 1」
            var bj: usize = 0; // 把 0; 写入 var bj: usize
            while (bj < 2 - bi) : (bj += 1) { // 循环，直到不满足「bj 小于 2 减 bi) : (bj 累加 1」
                if (m[r][bj] > m[r][bj + 1]) { // 若 映射表[右指针][bj] 超过 映射表[右指针][bj 加 1]
                    const t = m[r][bj]; // 把 映射表[右指针][bj] 存入 另一字符串
                    m[r][bj] = m[r][bj + 1]; // 把 映射表[右指针][bj 加 1]; 写入 m[r][bj]
                    m[r][bj + 1] = t; // 把 另一字符串; 写入 m[r][bj + 1]
                }
            }
        }
    }
}

const MAX_NODES = 16; // 把 16 存入 MAX_NODES
const HNode = struct { // 把 struct { 存入 HNode
    freq: i64,
    sym: u8 = 0,
    left: i16 = -1,
    right: i16 = -1,
};

var tree: [MAX_NODES]HNode = undefined; // 把 undefined; 写入 var tree: [MAX_NODES]HNode
var tree_n: usize = 0; // 把 0; 写入 var tree_n: usize

fn buildHuffman(syms: []const u8, freqs: []const i64) i16 { // 定义函数/方法 buildHuffman
    tree_n = freqs.len; // 把 freqs.长度; 写入 tree_n
    for (freqs, 0..) |f, i| { // for (freqs, 0..) 按位或 f, 下标 i 按位或 {
        tree[i] = .{ .freq = f, .sym = syms[i] }; // 把 { .频次表 赋值为 f, .sym 赋值为 syms[下标 i] }; 写入 tree[i]
    }
    var count = freqs.len; // 把 freqs.长度 存入 计数
    while (count > 1) { // 循环，直到不满足「计数 超过 1」
        var a: i16 = -1; // 把 减 1; 写入 var a: i16
        var b: i16 = -1; // 把 减 1; 写入 var b: i16
        var i: usize = 0; // 把 0; 写入 var i: usize
        while (i < tree_n) : (i += 1) { // 循环，直到不满足「下标 i 小于 tree_n) : (下标 i 累加 1」
            if (tree[i].freq < 0) continue; // 若 tree[下标 i].频次表 小于 0) continue;
            if (a < 0 or tree[i].freq < tree[@intCast(a)].freq) { // 若 数组 小于 0 or tree[下标 i].频次表 小于 tree[@intCast(数组)].频次表
                b = a; // 把 数组; 写入 b
                a = @intCast(i); // 把 @intCast(下标 i); 写入 数组
            } else if (b < 0 or tree[i].freq < tree[@intCast(b)].freq) { // 否则，若 b 小于 0 or tree[下标 i].频次表 小于 tree[@intCast(b)].频次表
                b = @intCast(i); // 把 @intCast(下标 i); 写入 b
            }
        }
        if (b < 0) break; // 若 b 小于 0) break;
        if (tree[@intCast(a)].freq > tree[@intCast(b)].freq) { // 若 tree[@intCast(数组)].频次表 超过 tree[@intCast(b)].频次表
            const t = a; // 把 数组 存入 另一字符串
            a = b; // 把 b; 写入 数组
            b = t; // 把 另一字符串; 写入 b
        }
        tree[tree_n] = .{ // 把 { 写入 tree[tree_n]
            .freq = tree[@intCast(a)].freq + tree[@intCast(b)].freq,
            .left = a,
            .right = b,
        };
        tree[@intCast(a)].freq = -1; // 把 减 1; 写入 频次表
        tree[@intCast(b)].freq = -1; // 把 减 1; 写入 频次表
        tree_n += 1; // tree_n累加 1
        count -= 1; // 计数累减 1
    }
    var bi: usize = 0; // 把 0; 写入 var bi: usize
    while (bi < tree_n) : (bi += 1) { // 循环，直到不满足「bi 小于 tree_n) : (bi 累加 1」
        if (tree[bi].freq >= 0) return @intCast(bi); // 若 tree[bi].频次表 不低于 0，直接返回 @intCast(bi)
    }
    return -1; // 返回 减 1
}

var codes: [8][8]u8 = undefined; // 把 undefined; 写入 var codes: [8][8]u8
var code_len: [8]usize = undefined; // 把 undefined; 写入 var code_len: [8]usize

fn walk(node: i16, prefix: []u8, depth: usize) void { // 定义函数/方法 walk
    const n = &tree[@intCast(node)]; // 把 按位与 tree[@intCast(节点)] 存入 元素个数
    if (n.left < 0) { // 若 元素个数.左边界 小于 0
        const idx = n.sym - 'A'; // 把 元素个数.sym 减 'A' 存入 idx
        if (depth == 0) { // 若 深度 等于 0
            codes[idx][0] = '0'; // 把 '0'; 写入 codes[idx][0]
            code_len[idx] = 1; // 把 1; 写入 code_len[idx]
        } else { // 否则
            for (prefix[0..depth], 0..) |ch, k| codes[idx][k] = ch; // 把 字符; 写入 for (prefix[0..depth], 0..) |ch, k| codes[idx][k]
            code_len[idx] = depth; // 把 深度; 写入 code_len[idx]
        }
        return; // return;
    }
    prefix[depth] = '0'; // 把 '0'; 写入 prefix[depth]
    walk(n.left, prefix, depth + 1); // walk(元素个数.左边界, prefix, 深度 加 1);
    prefix[depth] = '1'; // 把 '1'; 写入 prefix[depth]
    walk(n.right, prefix, depth + 1); // walk(元素个数.右边界, prefix, 深度 加 1);
}

pub fn main() !void { // 程序入口：跑内嵌自测用例
    // case1: matrixSort
    var mat = [3][3]i32{ .{ 5, 3, 4 }, .{ 1, 6, 2 }, .{ 7, 9, 8 } };
    const want = [3][3]i32{ .{ 1, 2, 3 }, .{ 4, 5, 6 }, .{ 7, 8, 9 } };
    matrixSort(&mat); // matrixSort( 按位与 mat);
    for (want, 0..) |row, i| { // for (want, 0..) 按位或 row, 下标 i 按位或 {
        for (row, 0..) |x, j| { // for (row, 0..) 按位或 x, 下标 j 按位或 {
            if (mat[i][j] != x) { // 若 mat[下标 i][下标 j] 不等于 x
                std.debug.print("matrixSort mismatch\n", .{}); // 打印输出
                return error.TestFailed; // 返回 error.TestFailed
            }
        }
    }

    // case2: WPL
    const syms = "ABCDEF"; // 把 「ABCDEF」 存入 syms
    const freqs = [_]i64{ 5, 9, 12, 13, 16, 45 }; // 把 [_]i64{ 5, 9, 12, 13, 16, 45 } 存入 freqs
    const root = buildHuffman(syms, &freqs); // 把 buildHuffman(syms, 按位与 freqs) 存入 根节点
    var prefix: [16]u8 = undefined; // 把 undefined; 写入 var prefix: [16]u8
    walk(root, &prefix, 0); // walk(根节点, 按位与 prefix, 0);
    var wpl: i64 = 0; // 把 0; 写入 var wpl: i64
    for (freqs, 0..) |f, i| { // for (freqs, 0..) 按位或 f, 下标 i 按位或 {
        wpl += f * @as(i64, @intCast(code_len[i])); // wpl累加 f 乘 @as(i64, @intCast(code_len[下标 i]))
    }
    if (wpl != 224) { // 若 wpl 不等于 224
        std.debug.print("WPL mismatch: {d}\n", .{wpl}); // 打印输出
        return error.TestFailed; // 返回 error.TestFailed
    }

    // case3: 前缀无关
    var ci: usize = 0; // 把 0; 写入 var ci: usize
    while (ci < 6) : (ci += 1) { // 循环，直到不满足「ci 小于 6) : (ci 累加 1」
        var cj: usize = 0; // 把 0; 写入 var cj: usize
        while (cj < 6) : (cj += 1) { // 循环，直到不满足「cj 小于 6) : (cj 累加 1」
            if (ci == cj) continue; // 若 ci 等于 cj) continue;
            if (std.mem.eql(u8, codes[cj][0..code_len[ci]], codes[ci][0..code_len[ci]])) {
                std.debug.print("not prefix-free\n", .{}); // 打印输出
                return error.TestFailed; // 返回 error.TestFailed
            }
        }
    }

    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
