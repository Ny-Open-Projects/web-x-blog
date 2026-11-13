#!/usr/bin/env python3
# gen_fix_n11.py — 补齐 notes/lc_107868749 matrixsort/PFC/Huffman × 7 语言
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from langlib import emit

REL = "notes/lc_107868749_贪心策略之matrixsorting_pfc_coding_huffmantre"
BLOG = "来源（blog）：https://blog.csdn.net/tyro_java/article/details/107868749"
DESC = "贪心策略之 matrixSort / PFC 编码 / Huffman 树"

T_RUST = '''// @@BLOG@@
// LeetCode 107868749. 贪心策略 — Rust 版（@@DESC@@）
use std::collections::HashMap;

// 每列升序排序后每行升序排序
fn matrix_sort(matrix: &mut Vec<Vec<i32>>) {
    if matrix.is_empty() {
        return;
    }
    let rows = matrix.len();
    let cols = matrix[0].len();
    for c in 0..cols {
        let mut col: Vec<i32> = matrix.iter().map(|r| r[c]).collect();
        col.sort();
        for r in 0..rows {
            matrix[r][c] = col[r];
        }
    }
    for r in 0..rows {
        matrix[r].sort();
    }
}

#[derive(Clone)]
enum Huff {
    Leaf { freq: i64, sym: String },
    Internal { freq: i64, left: Box<Huff>, right: Box<Huff> },
}

impl Huff {
    fn freq(&self) -> i64 {
        match self {
            Huff::Leaf { freq, .. } => *freq,
            Huff::Internal { freq, .. } => *freq,
        }
    }
}

fn build_huffman(freqs: &[(&str, i64)]) -> Huff {
    let mut nodes: Vec<(i64, Huff)> = freqs
        .iter()
        .map(|&(k, v)| (v, Huff::Leaf { freq: v, sym: k.to_string() }))
        .collect();
    nodes.sort_by_key(|n| n.0);
    while nodes.len() > 1 {
        let a = nodes.remove(0);
        let b = nodes.remove(0);
        let merged = (a.0 + b.0, Huff::Internal { freq: a.0 + b.0, left: Box::new(a.1), right: Box::new(b.1) });
        let mut i = 0;
        while i < nodes.len() && nodes[i].0 < merged.0 {
            i += 1;
        }
        nodes.insert(i, merged);
    }
    nodes.remove(0).1
}

fn huffman_codes(freqs: &[(&str, i64)]) -> HashMap<String, String> {
    let root = build_huffman(freqs);
    let mut codes: HashMap<String, String> = HashMap::new();
    fn walk(node: &Huff, prefix: &str, codes: &mut HashMap<String, String>) {
        match node {
            Huff::Leaf { sym, .. } => {
                let code = if prefix.is_empty() { "0".to_string() } else { prefix.to_string() };
                codes.insert(sym.clone(), code);
            }
            Huff::Internal { left, right, .. } => {
                walk(left, &format!("{}0", prefix), codes);
                walk(right, &format!("{}1", prefix), codes);
            }
        }
    }
    walk(&root, "", &mut codes);
    codes
}

fn main() {
    let freqs = [("A", 5i64), ("B", 9), ("C", 12), ("D", 13), ("E", 16), ("F", 45)];

    // case1: matrixSort
    let mut mat = vec![vec![5, 3, 4], vec![1, 6, 2], vec![7, 9, 8]];
    matrix_sort(&mut mat);
    let want_mat = vec![vec![1, 2, 3], vec![4, 5, 6], vec![7, 8, 9]];
    assert_eq!(mat, want_mat, "matrixSort mismatch");

    // case2: WPL
    let codes = huffman_codes(&freqs);
    let mut wpl = 0i64;
    let mut code_list: Vec<String> = vec![];
    for &(k, v) in &freqs {
        let c = codes.get(k).unwrap();
        wpl += v * c.len() as i64;
        code_list.push(c.clone());
    }
    assert_eq!(wpl, 224, "WPL mismatch");

    // case3: 前缀无关
    let mut prefix_free = true;
    for i in 0..code_list.len() {
        for j in 0..code_list.len() {
            if i != j && code_list[j].starts_with(&code_list[i]) {
                prefix_free = false;
            }
        }
    }
    assert!(prefix_free, "codes not prefix-free");

    println!("PASS");
}
'''

T_LUA = '''-- @@BLOG@@
-- LeetCode 107868749. 贪心策略 — Lua 版（@@DESC@@）
local function matrix_sort(matrix)
    local rows, cols = #matrix, #matrix[1]
    for c = 1, cols do
        local col = {}
        for r = 1, rows do col[r] = matrix[r][c] end
        table.sort(col)
        for r = 1, rows do matrix[r][c] = col[r] end
    end
    for r = 1, rows do
        table.sort(matrix[r])
    end
    return matrix
end

-- 节点：{freq=..., sym=...} 叶子 或 {freq=..., left=..., right=...} 内部
local function build_huffman(freqs)
    local nodes = {}
    for sym, f in pairs(freqs) do
        nodes[#nodes + 1] = { freq = f, sym = sym }
    end
    table.sort(nodes, function(a, b) return a.freq < b.freq end)
    while #nodes > 1 do
        local a = table.remove(nodes, 1)
        local b = table.remove(nodes, 1)
        local merged = { freq = a.freq + b.freq, left = a, right = b }
        local i = 1
        while i <= #nodes and nodes[i].freq < merged.freq do i = i + 1 end
        table.insert(nodes, i, merged)
    end
    return nodes[1]
end

local function huffman_codes(freqs)
    local root = build_huffman(freqs)
    local codes = {}
    local function walk(node, prefix)
        if node.sym ~= nil then
            codes[node.sym] = (prefix == "" and "0") or prefix
        else
            walk(node.left, prefix .. "0")
            walk(node.right, prefix .. "1")
        end
    end
    walk(root, "")
    return codes
end

local freqs = { A = 5, B = 9, C = 12, D = 13, E = 16, F = 45 }

-- case1: matrixSort
local mat = {{5, 3, 4}, {1, 6, 2}, {7, 9, 8}}
matrix_sort(mat)
local want_mat = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}
for i = 1, 3 do
    for j = 1, 3 do
        assert(mat[i][j] == want_mat[i][j], "matrixSort mismatch")
    end
end

-- case2: WPL
local codes = huffman_codes(freqs)
local wpl = 0
local code_list = {}
for sym, f in pairs(freqs) do
    local c = codes[sym]
    wpl = wpl + f * #c
    code_list[#code_list + 1] = c
end
assert(wpl == 224, "WPL mismatch: " .. tostring(wpl))

-- case3: 前缀无关
local prefix_free = true
for i = 1, #code_list do
    for j = 1, #code_list do
        if i ~= j and code_list[j]:sub(1, #code_list[i]) == code_list[i] then
            prefix_free = false
        end
    end
end
assert(prefix_free, "codes not prefix-free")

print("PASS")
'''

T_C = '''/* @@BLOG@@
 * LeetCode 107868749. 贪心策略 — C 版（@@DESC@@）
 */
#include <stdio.h>
#include <string.h>

#define MATRIX_SORT_INPLACE(rows, cols, m) \\
    do { \\
        for (int c = 0; c < (cols); c++) { \\
            for (int i = 0; i < (rows) - 1; i++) \\
                for (int j = 0; j < (rows) - 1 - i; j++) \\
                    if (m[j][c] > m[j + 1][c]) { int t = m[j][c]; m[j][c] = m[j + 1][c]; m[j + 1][c] = t; } \\
        } \\
        for (int r = 0; r < (rows); r++) { \\
            for (int i = 0; i < (cols) - 1; i++) \\
                for (int j = 0; j < (cols) - 1 - i; j++) \\
                    if (m[r][j] > m[r][j + 1]) { int t = m[r][j]; m[r][j] = m[r][j + 1]; m[r][j + 1] = t; } \\
        } \\
    } while (0)

/* Huffman 节点：left/right < 0 表示叶子 */
typedef struct {
    long long freq;
    char sym;
    int left, right;
} HNode;

static HNode tree[16];
static int tree_n = 0;

static int build_huffman(const char *syms, const long long *freqs, int n) {
    int order[16];
    for (int i = 0; i < n; i++) {
        tree[i].freq = freqs[i];
        tree[i].sym = syms[i];
        tree[i].left = tree[i].right = -1;
        order[i] = i;
    }
    int count = n;
    tree_n = n;
    while (count > 1) {
        /* 找最小的两个（按 order 中未合并者）——用简单线性选择 */
        int a = -1, b = -1;
        for (int i = 0; i < tree_n; i++) {
            if (tree[i].freq < 0) continue;
            if (a < 0 || tree[i].freq < tree[a].freq) { b = a; a = i; }
            else if (b < 0 || tree[i].freq < tree[b].freq) { b = i; }
        }
        if (b < 0) break;
        /* 合并（同权重时先取先出现的，保持与 JS 版本一致的稳定性不追求完全一致） */
        long long fa = tree[a].freq, fb = tree[b].freq;
        if (fa > fb) { int t = a; a = b; b = t; }
        tree[tree_n].freq = tree[a].freq + tree[b].freq;
        tree[tree_n].sym = 0;
        tree[tree_n].left = a;
        tree[tree_n].right = b;
        tree[a].freq = -1;
        tree[b].freq = -1;
        tree_n++;
        count--;
    }
    /* 根 = 唯一 freq >= 0 的节点 */
    for (int i = 0; i < tree_n; i++)
        if (tree[i].freq >= 0) return i;
    return -1;
}

static char codes[8][8];
static int code_len[8];

static void walk(int node, char *prefix, int depth) {
    if (tree[node].left < 0) {
        if (depth == 0) {
            strcpy(codes[tree[node].sym - 'A'], "0");
            code_len[tree[node].sym - 'A'] = 1;
        } else {
            prefix[depth] = 0;
            strcpy(codes[tree[node].sym - 'A'], prefix);
            code_len[tree[node].sym - 'A'] = depth;
        }
        return;
    }
    prefix[depth] = '0';
    walk(tree[node].left, prefix, depth + 1);
    prefix[depth] = '1';
    walk(tree[node].right, prefix, depth + 1);
}

int main(void) {
    /* case1: matrixSort */
    int mat[3][3] = {{5, 3, 4}, {1, 6, 2}, {7, 9, 8}};
    int want[3][3] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    MATRIX_SORT_INPLACE(3, 3, mat);
    for (int i = 0; i < 3; i++)
        for (int j = 0; j < 3; j++)
            if (mat[i][j] != want[i][j]) { printf("matrixSort mismatch\\n"); return 1; }

    /* case2: WPL（频次 5,9,12,13,16,45 的最优 WPL = 224） */
    const char syms[6] = {'A', 'B', 'C', 'D', 'E', 'F'};
    long long freqs[6] = {5, 9, 12, 13, 16, 45};
    int root = build_huffman(syms, freqs, 6);
    char prefix[16];
    memset(codes, 0, sizeof(codes));
    walk(root, prefix, 0);
    long long wpl = 0;
    for (int i = 0; i < 6; i++) wpl += freqs[i] * code_len[i];
    if (wpl != 224) { printf("WPL mismatch: %lld\\n", wpl); return 1; }

    /* case3: 前缀无关 */
    for (int i = 0; i < 6; i++)
        for (int j = 0; j < 6; j++) {
            if (i == j) continue;
            if (strncmp(codes[j], codes[i], strlen(codes[i])) == 0) {
                printf("not prefix-free\\n");
                return 1;
            }
        }

    printf("PASS\\n");
    return 0;
}
'''

T_CPP = '''// @@BLOG@@
// LeetCode 107868749. 贪心策略 — C++ 版（@@DESC@@）
#include <algorithm>
#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>

static void matrix_sort(std::vector<std::vector<int>> &matrix) {
    if (matrix.empty()) return;
    size_t rows = matrix.size(), cols = matrix[0].size();
    for (size_t c = 0; c < cols; ++c) {
        std::vector<int> col;
        for (size_t r = 0; r < rows; ++r) col.push_back(matrix[r][c]);
        std::sort(col.begin(), col.end());
        for (size_t r = 0; r < rows; ++r) matrix[r][c] = col[r];
    }
    for (size_t r = 0; r < rows; ++r) std::sort(matrix[r].begin(), matrix[r].end());
}

struct Huff {
    long long freq;
    std::string sym;   // 叶子时非空
    Huff *left = nullptr;
    Huff *right = nullptr;
    bool leaf = false;
};

static Huff *build_huffman(const std::vector<std::pair<std::string, long long>> &freqs) {
    std::vector<std::pair<long long, Huff *>> nodes;
    for (const auto &p : freqs) {
        nodes.push_back({p.second, new Huff{p.second, p.first, nullptr, nullptr, true}});
    }
    std::sort(nodes.begin(), nodes.end(),
              [](const auto &a, const auto &b) { return a.first < b.first; });
    while (nodes.size() > 1) {
        Huff *a = nodes.front().second;
        nodes.erase(nodes.begin());
        Huff *b = nodes.front().second;
        nodes.erase(nodes.begin());
        Huff *merged = new Huff{a->freq + b->freq, "", a, b, false};
        size_t i = 0;
        while (i < nodes.size() && nodes[i].first < merged->freq) ++i;
        nodes.insert(nodes.begin() + i, {merged->freq, merged});
    }
    return nodes.front().second;
}

static void walk(Huff *node, const std::string &prefix,
                 std::unordered_map<std::string, std::string> &codes) {
    if (node->leaf) {
        codes[node->sym] = prefix.empty() ? "0" : prefix;
        return;
    }
    walk(node->left, prefix + "0", codes);
    walk(node->right, prefix + "1", codes);
}

int main() {
    std::vector<std::pair<std::string, long long>> freqs = {
        {"A", 5}, {"B", 9}, {"C", 12}, {"D", 13}, {"E", 16}, {"F", 45}};

    // case1: matrixSort
    std::vector<std::vector<int>> mat = {{5, 3, 4}, {1, 6, 2}, {7, 9, 8}};
    matrix_sort(mat);
    std::vector<std::vector<int>> want = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    if (mat != want) { std::cout << "matrixSort mismatch" << std::endl; return 1; }

    // case2: WPL
    auto codes = std::unordered_map<std::string, std::string>{};
    walk(build_huffman(freqs), "", codes);
    long long wpl = 0;
    std::vector<std::string> code_list;
    for (const auto &p : freqs) {
        const std::string &c = codes[p.first];
        wpl += p.second * static_cast<long long>(c.size());
        code_list.push_back(c);
    }
    if (wpl != 224) { std::cout << "WPL mismatch: " << wpl << std::endl; return 1; }

    // case3: 前缀无关
    bool prefix_free = true;
    for (size_t i = 0; i < code_list.size(); ++i)
        for (size_t j = 0; j < code_list.size(); ++j)
            if (i != j && code_list[j].compare(0, code_list[i].size(), code_list[i]) == 0)
                prefix_free = false;
    if (!prefix_free) { std::cout << "not prefix-free" << std::endl; return 1; }

    std::cout << "PASS" << std::endl;
    return 0;
}
'''

T_R = '''# @@BLOG@@
# LeetCode 107868749. 贪心策略 — R 版（@@DESC@@）

matrix_sort <- function(matrix) {
  rows <- nrow(matrix)
  cols <- ncol(matrix)
  for (c in 1:cols) {
    col <- sort(matrix[, c])
    for (r in 1:rows) matrix[r, c] <- col[r]
  }
  for (r in 1:rows) matrix[r, ] <- sort(matrix[r, ])
  matrix
}

# 节点：list(freq=, sym=) 叶子 或 list(freq=, left=, right=) 内部
build_huffman <- function(freqs) {
  nodes <- list()
  for (nm in names(freqs)) {
    nodes[[length(nodes) + 1L]] <- list(freq = freqs[[nm]], sym = nm)
  }
  nodes <- nodes[order(vapply(nodes, function(n) n$freq, numeric(1)))]
  while (length(nodes) > 1L) {
    a <- nodes[[1]]
    b <- nodes[[2]]
    nodes <- nodes[-c(1, 2)]
    merged <- list(freq = a$freq + b$freq, left = a, right = b)
    i <- 1L
    while (i <= length(nodes) && nodes[[i]]$freq < merged$freq) i <- i + 1L
    nodes <- append(nodes, list(merged), after = i - 1L)
  }
  nodes[[1]]
}

huffman_codes <- function(freqs) {
  root <- build_huffman(freqs)
  codes <- list()
  walk <- function(node, prefix) {
    if (!is.null(node$sym)) {
      codes[[node$sym]] <<- if (nchar(prefix) == 0) "0" else prefix
    } else {
      walk(node$left, paste0(prefix, "0"))
      walk(node$right, paste0(prefix, "1"))
    }
  }
  walk(root, "")
  codes
}

freqs <- list(A = 5, B = 9, C = 12, D = 13, E = 16, F = 45)

# case1: matrixSort
mat <- matrix_sort(matrix(c(5, 3, 4, 1, 6, 2, 7, 9, 8), nrow = 3, byrow = TRUE))
want <- matrix(c(1, 2, 3, 4, 5, 6, 7, 8, 9), nrow = 3, byrow = TRUE)
stopifnot(all(mat == want))

# case2: WPL
codes <- huffman_codes(freqs)
wpl <- 0
code_list <- c()
for (nm in names(freqs)) {
  c <- codes[[nm]]
  wpl <- wpl + freqs[[nm]] * nchar(c)
  code_list <- c(code_list, c)
}
stopifnot(wpl == 224)

# case3: 前缀无关
prefix_free <- TRUE
for (i in seq_along(code_list)) {
  for (j in seq_along(code_list)) {
    if (i != j && substr(code_list[j], 1, nchar(code_list[i])) == code_list[i]) {
      prefix_free <- FALSE
    }
  }
}
stopifnot(prefix_free)

cat("PASS\\n")
'''

T_ZIG = '''// @@BLOG@@
// LeetCode 107868749. 贪心策略 — Zig 版（@@DESC@@）
const std = @import("std");

// 每列升序排序后每行升序排序
fn matrixSort(m: *[3][3]i32) void {
    var c: usize = 0;
    while (c < 3) : (c += 1) {
        var i: usize = 0;
        while (i < 2) : (i += 1) {
            var j: usize = 0;
            while (j < 2 - i) : (j += 1) {
                if (m[j][c] > m[j + 1][c]) {
                    const t = m[j][c];
                    m[j][c] = m[j + 1][c];
                    m[j + 1][c] = t;
                }
            }
        }
    }
    var r: usize = 0;
    while (r < 3) : (r += 1) {
        var bi: usize = 0;
        while (bi < 2) : (bi += 1) {
            var bj: usize = 0;
            while (bj < 2 - bi) : (bj += 1) {
                if (m[r][bj] > m[r][bj + 1]) {
                    const t = m[r][bj];
                    m[r][bj] = m[r][bj + 1];
                    m[r][bj + 1] = t;
                }
            }
        }
    }
}

const MAX_NODES = 16;
const HNode = struct {
    freq: i64,
    sym: u8 = 0,
    left: i16 = -1,
    right: i16 = -1,
};

var tree: [MAX_NODES]HNode = undefined;
var tree_n: usize = 0;

fn buildHuffman(syms: []const u8, freqs: []const i64) i16 {
    tree_n = freqs.len;
    for (freqs, 0..) |f, i| {
        tree[i] = .{ .freq = f, .sym = syms[i] };
    }
    var count = freqs.len;
    while (count > 1) {
        var a: i16 = -1;
        var b: i16 = -1;
        var i: usize = 0;
        while (i < tree_n) : (i += 1) {
            if (tree[i].freq < 0) continue;
            if (a < 0 or tree[i].freq < tree[@intCast(a)].freq) {
                b = a;
                a = @intCast(i);
            } else if (b < 0 or tree[i].freq < tree[@intCast(b)].freq) {
                b = @intCast(i);
            }
        }
        if (b < 0) break;
        if (tree[@intCast(a)].freq > tree[@intCast(b)].freq) {
            const t = a;
            a = b;
            b = t;
        }
        tree[tree_n] = .{
            .freq = tree[@intCast(a)].freq + tree[@intCast(b)].freq,
            .left = a,
            .right = b,
        };
        tree[@intCast(a)].freq = -1;
        tree[@intCast(b)].freq = -1;
        tree_n += 1;
        count -= 1;
    }
    var bi: usize = 0;
    while (bi < tree_n) : (bi += 1) {
        if (tree[bi].freq >= 0) return @intCast(bi);
    }
    return -1;
}

var codes: [8][8]u8 = undefined;
var code_len: [8]usize = undefined;

fn walk(node: i16, prefix: []u8, depth: usize) void {
    const n = &tree[@intCast(node)];
    if (n.left < 0) {
        const idx = n.sym - 'A';
        if (depth == 0) {
            codes[idx][0] = '0';
            code_len[idx] = 1;
        } else {
            for (prefix[0..depth], 0..) |ch, k| codes[idx][k] = ch;
            code_len[idx] = depth;
        }
        return;
    }
    prefix[depth] = '0';
    walk(n.left, prefix, depth + 1);
    prefix[depth] = '1';
    walk(n.right, prefix, depth + 1);
}

pub fn main() !void {
    // case1: matrixSort
    var mat = [3][3]i32{ .{ 5, 3, 4 }, .{ 1, 6, 2 }, .{ 7, 9, 8 } };
    const want = [3][3]i32{ .{ 1, 2, 3 }, .{ 4, 5, 6 }, .{ 7, 8, 9 } };
    matrixSort(&mat);
    for (want, 0..) |row, i| {
        for (row, 0..) |x, j| {
            if (mat[i][j] != x) {
                std.debug.print("matrixSort mismatch\\n", .{});
                return error.TestFailed;
            }
        }
    }

    // case2: WPL
    const syms = "ABCDEF";
    const freqs = [_]i64{ 5, 9, 12, 13, 16, 45 };
    const root = buildHuffman(syms, &freqs);
    var prefix: [16]u8 = undefined;
    walk(root, &prefix, 0);
    var wpl: i64 = 0;
    for (freqs, 0..) |f, i| {
        wpl += f * @as(i64, @intCast(code_len[i]));
    }
    if (wpl != 224) {
        std.debug.print("WPL mismatch: {d}\\n", .{wpl});
        return error.TestFailed;
    }

    // case3: 前缀无关
    var ci: usize = 0;
    while (ci < 6) : (ci += 1) {
        var cj: usize = 0;
        while (cj < 6) : (cj += 1) {
            if (ci == cj) continue;
            if (std.mem.eql(u8, codes[cj][0..code_len[ci]], codes[ci][0..code_len[ci]])) {
                std.debug.print("not prefix-free\\n", .{});
                return error.TestFailed;
            }
        }
    }

    std.debug.print("PASS\\n", .{});
}
'''

T_DART = '''// @@BLOG@@
// LeetCode 107868749. 贪心策略 — Dart 版（@@DESC@@）
void matrixSort(List<List<int>> matrix) {
  final rows = matrix.length, cols = matrix[0].length;
  for (var c = 0; c < cols; c++) {
    final col = <int>[for (final r in matrix) r[c]]..sort();
    for (var r = 0; r < rows; r++) {
      matrix[r][c] = col[r];
    }
  }
  for (var r = 0; r < rows; r++) {
    matrix[r].sort();
  }
}

class Huff {
  int freq;
  String? sym;
  Huff? left, right;
  bool get isLeaf => sym != null;
  Huff.leaf(this.freq, this.sym);
  Huff.internal(this.freq, this.left, this.right);
}

Huff buildHuffman(Map<String, int> freqs) {
  var nodes = <Huff>[
    for (final e in freqs.entries) Huff.leaf(e.value, e.key),
  ]..sort((a, b) => a.freq.compareTo(b.freq));
  while (nodes.length > 1) {
    final a = nodes.removeAt(0);
    final b = nodes.removeAt(0);
    final merged = Huff.internal(a.freq + b.freq, a, b);
    var i = 0;
    while (i < nodes.length && nodes[i].freq < merged.freq) {
      i++;
    }
    nodes.insert(i, merged);
  }
  return nodes[0];
}

Map<String, String> huffmanCodes(Map<String, int> freqs) {
  final root = buildHuffman(freqs);
  final codes = <String, String>{};
  void walk(Huff node, String prefix) {
    if (node.isLeaf) {
      codes[node.sym!] = prefix.isEmpty ? '0' : prefix;
    } else {
      walk(node.left!, prefix + '0');
      walk(node.right!, prefix + '1');
    }
  }
  walk(root, '');
  return codes;
}

void main() {
  final freqs = <String, int>{'A': 5, 'B': 9, 'C': 12, 'D': 13, 'E': 16, 'F': 45};

  // case1: matrixSort
  final mat = <List<int>>[[5, 3, 4], [1, 6, 2], [7, 9, 8]];
  matrixSort(mat);
  if (mat.toString() != '[[1, 2, 3], [4, 5, 6], [7, 8, 9]]') {
    throw StateError('matrixSort mismatch');
  }

  // case2: WPL
  final codes = huffmanCodes(freqs);
  var wpl = 0;
  final codeList = <String>[];
  freqs.forEach((sym, f) {
    final c = codes[sym]!;
    wpl += f * c.length;
    codeList.add(c);
  });
  if (wpl != 224) throw StateError('WPL mismatch: $wpl');

  // case3: 前缀无关
  var prefixFree = true;
  for (var i = 0; i < codeList.length; i++) {
    for (var j = 0; j < codeList.length; j++) {
      if (i != j && codeList[j].startsWith(codeList[i])) prefixFree = false;
    }
  }
  if (!prefixFree) throw StateError('not prefix-free');

  print('PASS');
}
'''

GENS = {
    "rust": (T_RUST, ".rs"),
    "lua": (T_LUA, ".lua"),
    "c": (T_C, ".c"),
    "cpp": (T_CPP, ".cpp"),
    "r": (T_R, ".R"),
    "zig": (T_ZIG, ".zig"),
    "dart": (T_DART, ".dart"),
}

def main():
    for lang, (t, ext) in GENS.items():
        out = t.replace("@@BLOG@@", BLOG).replace("@@DESC@@", DESC)
        emit(lang, REL + "/solution_1_主解法" + ext, out)

if __name__ == "__main__":
    main()
