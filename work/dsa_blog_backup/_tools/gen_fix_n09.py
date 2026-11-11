#!/usr/bin/env python3
# gen_fix_n09.py — 补齐 notes/lc_108013114 贪心策略 Kruskal MST（并查集）× 7 语言
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from langlib import emit

REL = "notes/lc_108013114_贪心策略之bst&bbst_hashtable+dictionary+map_p"
BLOG = "来源（blog）：https://blog.csdn.net/tyro_java/article/details/108013114"
DESC = "贪心策略之 BST/BBST/哈希表：Kruskal 最小生成树（并查集 + 排序）"

T_RUST = '''// @@BLOG@@
// LeetCode 108013114. @@TITLE@@ — Rust 版（@@DESC@@）
use std::collections::HashMap;

fn kruskal_mst(edges: &[(i32, i32, i32)]) -> i32 {
    let mut sorted = edges.to_vec();
    sorted.sort_by_key(|e| e.2);
    let mut parent: HashMap<i32, i32> = HashMap::new();

    fn find(parent: &mut HashMap<i32, i32>, x: i32) -> i32 {
        parent.entry(x).or_insert(x);
        let mut x = x;
        while parent[&x] != x {
            let px = parent[&x];
            let ppx = parent[&px];
            parent.insert(x, ppx);
            x = ppx;
        }
        x
    }

    let mut total = 0;
    for &(u, v, w) in &sorted {
        let ru = find(&mut parent, u);
        let rv = find(&mut parent, v);
        if ru != rv {
            parent.insert(ru, rv);
            total += w;
        }
    }
    total
}

fn main() {
    let cases: Vec<(Vec<(i32, i32, i32)>, i32)> = vec![
        (vec![(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)], 19),
        (vec![(0, 1, 1), (1, 2, 2), (2, 3, 3), (3, 4, 4)], 10),
        (vec![(0, 1, 2), (1, 2, 3)], 5),
        (vec![], 0),
    ];
    for (idx, (edges, want)) in cases.iter().enumerate() {
        let got = kruskal_mst(edges);
        assert_eq!(got, *want, "case {} failed", idx);
    }
    println!("PASS");
}
'''

T_LUA = '''-- @@BLOG@@
-- LeetCode 108013114. @@TITLE@@ — Lua 版（@@DESC@@）
local function kruskal_mst(edges)
    local sorted = {}
    for i, e in ipairs(edges) do sorted[i] = e end
    table.sort(sorted, function(a, b) return a[3] < b[3] end)
    local parent = {}

    local function find(x)
        if parent[x] == nil then parent[x] = x end
        while parent[x] ~= x do
            parent[x] = parent[parent[x]]
            x = parent[x]
        end
        return x
    end

    local total = 0
    for _, e in ipairs(sorted) do
        local u, v, w = e[1], e[2], e[3]
        local ru, rv = find(u), find(v)
        if ru ~= rv then
            parent[ru] = rv
            total = total + w
        end
    end
    return total
end

local cases = {
    {{{0, 1, 10}, {0, 2, 6}, {0, 3, 5}, {1, 3, 15}, {2, 3, 4}}, 19},
    {{{0, 1, 1}, {1, 2, 2}, {2, 3, 3}, {3, 4, 4}}, 10},
    {{{0, 1, 2}, {1, 2, 3}}, 5},
    {{}, 0},
}
for idx, c in ipairs(cases) do
    local got = kruskal_mst(c[1])
    assert(got == c[2], string.format("case %d failed: got %d want %d", idx, got, c[2]))
end
print("PASS")
'''

T_C = '''/* @@BLOG@@
 * LeetCode 108013114. @@TITLE@@ — C 版（@@DESC@@）
 */
#include <stdio.h>

#define MAX_NODES 100

static int parent[MAX_NODES + 1];

static int find(int x) {
    if (parent[x] == -1) parent[x] = x;
    while (parent[x] != x) {
        parent[x] = parent[parent[x]];
        x = parent[x];
    }
    return x;
}

static int kruskal_mst(const int edges[][3], int n) {
    /* 按权重的简单选择排序（保持稳定足够） */
    int idx[64];
    for (int i = 0; i < n; i++) idx[i] = i;
    for (int i = 0; i < n - 1; i++)
        for (int j = 0; j < n - 1 - i; j++)
            if (edges[idx[j]][2] > edges[idx[j + 1]][2]) {
                int t = idx[j]; idx[j] = idx[j + 1]; idx[j + 1] = t;
            }
    for (int i = 0; i <= MAX_NODES; i++) parent[i] = -1;
    int total = 0;
    for (int i = 0; i < n; i++) {
        int u = edges[idx[i]][0], v = edges[idx[i]][1], w = edges[idx[i]][2];
        int ru = find(u), rv = find(v);
        if (ru != rv) {
            parent[ru] = rv;
            total += w;
        }
    }
    return total;
}

int main(void) {
    int e0[5][3] = {{0, 1, 10}, {0, 2, 6}, {0, 3, 5}, {1, 3, 15}, {2, 3, 4}};
    int e1[4][3] = {{0, 1, 1}, {1, 2, 2}, {2, 3, 3}, {3, 4, 4}};
    int e2[2][3] = {{0, 1, 2}, {1, 2, 3}};
    int ws[4] = {19, 10, 5, 0};
    int ns[4] = {5, 4, 2, 0};
    const int (*es[4])[3] = {e0, e1, e2, NULL};
    for (int i = 0; i < 4; i++) {
        int got = kruskal_mst(es[i], ns[i]);
        if (got != ws[i]) { printf("case %d failed: got %d want %d\\n", i, got, ws[i]); return 1; }
    }
    printf("PASS\\n");
    return 0;
}
'''

T_CPP = '''// @@BLOG@@
// LeetCode 108013114. @@TITLE@@ — C++ 版（@@DESC@@）
#include <algorithm>
#include <iostream>
#include <unordered_map>
#include <vector>

static std::unordered_map<int, int> parent;

static int find(int x) {
    if (parent.find(x) == parent.end()) parent[x] = x;
    while (parent[x] != x) {
        parent[x] = parent[parent[x]];
        x = parent[x];
    }
    return x;
}

static int kruskal_mst(std::vector<std::vector<int>> edges) {
    std::sort(edges.begin(), edges.end(),
              [](const std::vector<int> &a, const std::vector<int> &b) { return a[2] < b[2]; });
    parent.clear();
    int total = 0;
    for (const auto &e : edges) {
        int u = e[0], v = e[1], w = e[2];
        int ru = find(u), rv = find(v);
        if (ru != rv) {
            parent[ru] = rv;
            total += w;
        }
    }
    return total;
}

int main() {
    std::vector<std::pair<std::vector<std::vector<int>>, int>> cases = {
        {{{0, 1, 10}, {0, 2, 6}, {0, 3, 5}, {1, 3, 15}, {2, 3, 4}}, 19},
        {{{0, 1, 1}, {1, 2, 2}, {2, 3, 3}, {3, 4, 4}}, 10},
        {{{0, 1, 2}, {1, 2, 3}}, 5},
        {{}, 0},
    };
    for (size_t idx = 0; idx < cases.size(); ++idx) {
        int got = kruskal_mst(cases[idx].first);
        if (got != cases[idx].second) {
            std::cout << "case " << idx << " failed: got " << got << " want " << cases[idx].second << std::endl;
            return 1;
        }
    }
    std::cout << "PASS" << std::endl;
    return 0;
}
'''

T_R = '''# @@BLOG@@
# LeetCode 108013114. @@TITLE@@ — R 版（@@DESC@@）

kruskal_mst <- function(edges) {
  # edges: 3 列矩阵 [u, v, w]
  if (nrow(edges) == 0) return(0L)
  ord <- order(edges[, 3])
  parent <- new.env(parent = emptyenv())

  find <- function(x) {
    if (is.null(parent[[as.character(x)]])) parent[[as.character(x)]] <- x
    while (parent[[as.character(x)]] != x) {
      parent[[as.character(x)]] <- parent[[as.character(parent[[as.character(x)]])]]
      x <- parent[[as.character(x)]]
    }
    x
  }

  total <- 0L
  for (i in ord) {
    u <- edges[i, 1]; v <- edges[i, 2]; w <- edges[i, 3]
    ru <- find(u); rv <- find(v)
    if (ru != rv) {
      parent[[as.character(ru)]] <- rv
      total <- total + w
    }
  }
  total
}

cases <- list(
  list(matrix(c(0,1,10, 0,2,6, 0,3,5, 1,3,15, 2,3,4), ncol = 3, byrow = TRUE), 19L),
  list(matrix(c(0,1,1, 1,2,2, 2,3,3, 3,4,4), ncol = 3, byrow = TRUE), 10L),
  list(matrix(c(0,1,2, 1,2,3), ncol = 3, byrow = TRUE), 5L),
  list(matrix(integer(0), ncol = 3), 0L)
)
for (idx in seq_along(cases)) {
  got <- kruskal_mst(cases[[idx]][[1]])
  stopifnot(got == cases[[idx]][[2]])
}
cat("PASS\\n")
'''

T_ZIG = '''// @@BLOG@@
// LeetCode 108013114. @@TITLE@@ — Zig 版（@@DESC@@）
const std = @import("std");

const Edge = struct { u: i32, v: i32, w: i32 };

var parent: [101]i32 = undefined;

fn find(x: i32) i32 {
    var xi = x;
    if (parent[@intCast(xi)] == -1) parent[@intCast(xi)] = xi;
    while (parent[@intCast(xi)] != xi) {
        const px = parent[@intCast(xi)];
        parent[@intCast(xi)] = parent[@intCast(px)];
        xi = parent[@intCast(xi)];
    }
    return xi;
}

fn kruskalMst(edges: []const Edge) i32 {
    for (0..parent.len) |i| parent[i] = -1;
    // 拷贝并按权重排序
    var buf: [64]Edge = undefined;
    const n = edges.len;
    for (edges, 0..) |e, i| buf[i] = e;
    var i: usize = 0;
    while (i + 1 < n) : (i += 1) {
        var j: usize = 0;
        while (j + 1 < n - i) : (j += 1) {
            if (buf[j].w > buf[j + 1].w) {
                const t = buf[j];
                buf[j] = buf[j + 1];
                buf[j + 1] = t;
            }
        }
    }
    var total: i32 = 0;
    for (buf[0..n]) |e| {
        const ru = find(e.u);
        const rv = find(e.v);
        if (ru != rv) {
            parent[@intCast(ru)] = rv;
            total += e.w;
        }
    }
    return total;
}

pub fn main() !void {
    const e0 = [_]Edge{ .{ .u = 0, .v = 1, .w = 10 }, .{ .u = 0, .v = 2, .w = 6 }, .{ .u = 0, .v = 3, .w = 5 }, .{ .u = 1, .v = 3, .w = 15 }, .{ .u = 2, .v = 3, .w = 4 } };
    const e1 = [_]Edge{ .{ .u = 0, .v = 1, .w = 1 }, .{ .u = 1, .v = 2, .w = 2 }, .{ .u = 2, .v = 3, .w = 3 }, .{ .u = 3, .v = 4, .w = 4 } };
    const e2 = [_]Edge{ .{ .u = 0, .v = 1, .w = 2 }, .{ .u = 1, .v = 2, .w = 3 } };
    const empty = [_]Edge{};
    const Case = struct { edges: []const Edge, want: i32 };
    const cases = [_]Case{
        .{ .edges = &e0, .want = 19 },
        .{ .edges = &e1, .want = 10 },
        .{ .edges = &e2, .want = 5 },
        .{ .edges = &empty, .want = 0 },
    };
    for (cases, 0..) |c, idx| {
        const got = kruskalMst(c.edges);
        if (got != c.want) {
            std.debug.print("case {d} failed: got {d} want {d}\\n", .{ idx, got, c.want });
            return error.TestFailed;
        }
    }
    std.debug.print("PASS\\n", .{});
}
'''

T_DART = '''// @@BLOG@@
// LeetCode 108013114. @@TITLE@@ — Dart 版（@@DESC@@）
final parent = <int, int>{};

int find(int x) {
  parent.putIfAbsent(x, () => x);
  while (parent[x] != x) {
    parent[x] = parent[parent[x]]!;
    x = parent[x]!;
  }
  return x!;
}

int kruskalMst(List<List<int>> edges) {
  final sorted = List<List<int>>.from(edges)..sort((a, b) => a[2].compareTo(b[2]));
  parent.clear();
  var total = 0;
  for (final e in sorted) {
    final ru = find(e[0]);
    final rv = find(e[1]);
    if (ru != rv) {
      parent[ru] = rv;
      total += e[2];
    }
  }
  return total;
}

void main() {
  final cases = <List<List<int>>, int>{
    [[0, 1, 10], [0, 2, 6], [0, 3, 5], [1, 3, 15], [2, 3, 4]]: 19,
    [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 4, 4]]: 10,
    [[0, 1, 2], [1, 2, 3]]: 5,
    <List<int>>[]: 0,
  };
  var idx = 0;
  cases.forEach((edges, want) {
    final got = kruskalMst(edges);
    if (got != want) throw StateError('case $idx failed: got $got want $want');
    idx++;
  });
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
        out = t.replace("@@BLOG@@", BLOG).replace("@@TITLE@@", "贪心策略之BST&BBST_hashtable+dictionary+map").replace("@@DESC@@", DESC)
        emit(lang, REL + "/solution_1___1" + ext, out)

if __name__ == "__main__":
    main()
