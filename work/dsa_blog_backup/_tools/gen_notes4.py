#!/usr/bin/env python3
# gen_notes4.py — notes 第四批：LC真题笔记 + DFS + DFS图遍历 + LCS + dijkstra + LRU笔记 × 7语言
import sys, os; sys.path.insert(0, "/Users/Wang/Code/webfault-ai/dsa/_tools")
from langlib import emit, head_comment, EXT

LANGNAME = {"rust": "Rust", "lua": "Lua", "c": "C", "cpp": "C++", "r": "R", "zig": "Zig", "dart": "Dart"}

POSTORDER = {
"rust":'''fn verify_postorder(postorder: &[i32]) -> bool {
    fn check(seq: &[i32]) -> bool {
        if seq.len() <= 2 { return true; }
        let root = seq[seq.len() - 1];
        let mut i = 0usize;
        while i < seq.len() - 1 && seq[i] < root { i += 1; }
        for &v in &seq[i..seq.len() - 1] {
            if v < root { return false; }
        }
        check(&seq[..i]) && check(&seq[i..seq.len() - 1])
    }
    check(postorder)
}
fn main() {
    assert!(!verify_postorder(&[1,6,3,2,5]));
    assert!(verify_postorder(&[1,3,2,4,5]));
    assert!(verify_postorder(&[4,6,5,9,8,7]));
    assert!(verify_postorder(&[1,2,3]));
    println!("PASS"); }''',
"lua":'''local function verify_postorder(postorder)
    local function check(seq, lo, hi)
        if hi - lo <= 1 then return true end
        local root = seq[hi]
        local i = lo
        while i < hi and seq[i] < root do i = i + 1 end
        for j = i, hi - 1 do
            if seq[j] < root then return false end
        end
        return check(seq, lo, i - 1) and check(seq, i, hi - 1)
    end
    return check(postorder, 1, #postorder)
end
assert(verify_postorder({1,6,3,2,5}) == false)
assert(verify_postorder({1,3,2,4,5}) == true)
assert(verify_postorder({4,6,5,9,8,7}) == true)
assert(verify_postorder({1,2,3}) == true)
print("PASS")''',
"c":'''#include <stdio.h>
static int check(const int *seq, int lo, int hi) {
    if (hi - lo <= 1) return 1;
    int root = seq[hi];
    int i = lo;
    while (i < hi && seq[i] < root) i++;
    for (int j = i; j < hi; j++) {
        if (seq[j] < root) return 0;
    }
    return check(seq, lo, i - 1) && check(seq, i, hi - 1);
}
static int verify_postorder(const int *seq, int n) { return check(seq, 0, n - 1); }
int main(void) {
    if (verify_postorder((int[]){1,6,3,2,5}, 5)) { printf("FAIL 1\\n"); return 1; }
    if (!verify_postorder((int[]){1,3,2,4,5}, 5)) { printf("FAIL 2\\n"); return 1; }
    if (!verify_postorder((int[]){4,6,5,9,8,7}, 6)) { printf("FAIL 3\\n"); return 1; }
    if (!verify_postorder((int[]){1,2,3}, 3)) { printf("FAIL 4\\n"); return 1; }
    printf("PASS\\n"); return 0; }''',
"cpp":'''#include <cassert>
#include <iostream>
#include <vector>
static bool check(const std::vector<int> &seq, int lo, int hi) {
    if (hi - lo <= 1) return true;
    int root = seq[hi];
    int i = lo;
    while (i < hi && seq[i] < root) ++i;
    for (int j = i; j < hi; ++j) {
        if (seq[j] < root) return false;
    }
    return check(seq, lo, i - 1) && check(seq, i, hi - 1);
}
static bool verifyPostorder(const std::vector<int> &postorder) {
    return check(postorder, 0, static_cast<int>(postorder.size()) - 1);
}
int main() {
    assert(!verifyPostorder({1,6,3,2,5}));
    assert(verifyPostorder({1,3,2,4,5}));
    assert(verifyPostorder({4,6,5,9,8,7}));
    assert(verifyPostorder({1,2,3}));
    std::cout << "PASS" << std::endl; }''',
"r":'''verify_postorder <- function(postorder) {
  check <- function(lo, hi) {
    if (hi - lo <= 1L) return(TRUE)
    root <- postorder[hi]
    i <- lo
    while (i < hi && postorder[i] < root) i <- i + 1L
    if (i <= hi - 1L) {
      for (j in i:(hi - 1L)) {
        if (postorder[j] < root) return(FALSE)
      }
    }
    check(lo, i - 1L) && check(i, hi - 1L)
  }
  check(1L, length(postorder))
}
stopifnot(!verify_postorder(c(1, 6, 3, 2, 5)))
stopifnot(verify_postorder(c(1, 3, 2, 4, 5)))
stopifnot(verify_postorder(c(4, 6, 5, 9, 8, 7)))
stopifnot(verify_postorder(c(1, 2, 3)))
cat("PASS\\n")''',
"zig":'''const std = @import("std");
fn checkSeq(seq: []const i32, lo: usize, hi: usize) bool {
    if (hi <= lo + 1) return true;
    const root = seq[hi];
    var i = lo;
    while (i < hi and seq[i] < root) i += 1;
    var j = i;
    while (j < hi) : (j += 1) {
        if (seq[j] < root) return false;
    }
    return checkSeq(seq, lo, i - 1) and checkSeq(seq, i, hi - 1);
}
fn verifyPostorder(postorder: []const i32) bool {
    if (postorder.len == 0) return true;
    return checkSeq(postorder, 0, postorder.len - 1);
}
pub fn main() !void {
    if (verifyPostorder(&[_]i32{ 1, 6, 3, 2, 5 })) return error.TestFailed;
    if (!verifyPostorder(&[_]i32{ 1, 3, 2, 4, 5 })) return error.TestFailed;
    if (!verifyPostorder(&[_]i32{ 4, 6, 5, 9, 8, 7 })) return error.TestFailed;
    if (!verifyPostorder(&[_]i32{ 1, 2, 3 })) return error.TestFailed;
    std.debug.print("PASS\\n", .{}); }''',
"dart":'''bool verifyPostorder(List<int> postorder) {
  bool check(int lo, int hi) {
    if (hi - lo <= 1) return true;
    final root = postorder[hi];
    var i = lo;
    while (i < hi && postorder[i] < root) { i++; }
    for (var j = i; j < hi; j++) {
      if (postorder[j] < root) return false;
    }
    return check(lo, i - 1) && check(i, hi - 1);
  }
  return check(0, postorder.length - 1);
}
void main() {
  if (verifyPostorder([1, 6, 3, 2, 5])) throw StateError('c1');
  if (!verifyPostorder([1, 3, 2, 4, 5])) throw StateError('c2');
  if (!verifyPostorder([4, 6, 5, 9, 8, 7])) throw StateError('c3');
  if (!verifyPostorder([1, 2, 3])) throw StateError('c4');
  print('PASS'); }''',
}

DFS = {
"rust":'''fn dfs_traverse(graph: &[Vec<i32>], start: usize) -> (Vec<i32>, Vec<i32>) {
    let n = graph.len();
    let mut visited = vec![false; n];
    let mut d = vec![-1i32; n];
    let mut p = vec![-1i32; n];
    let mut order = Vec::new();
    fn go(c: usize, depth: i32, parent: i32, graph: &[Vec<i32>], visited: &mut Vec<bool>,
          d: &mut Vec<i32>, p: &mut Vec<i32>, order: &mut Vec<i32>) {
        visited[c] = true;
        d[c] = depth;
        p[c] = parent;
        order.push(c as i32);
        for &nx in &graph[c] {
            let u = nx as usize;
            if !visited[u] { go(u, depth + 1, c as i32, graph, visited, d, p, order); }
        }
    }
    go(start, 0, -1, graph, &mut visited, &mut d, &mut p, &mut order);
    (order, d)
}
fn main() {
    // 8节点图: 0-1,0-2,1-3,1-6,2-4,2-5,5-7 (期望 d=[1,2,3,0,0,6,7])
    let g = vec![vec![1,2],vec![3,6],vec![4,5],vec![],vec![],vec![7],vec![],vec![]];
    let (order, d) = dfs_traverse(&g, 0);
    assert_eq!(d, vec![0,1,1,2,2,2,2,3]);
    assert_eq!(order.len(), 8);
    println!("PASS"); }''',
"lua":'''local function dfs_traverse(graph, start)
    local n = #graph
    local visited = {}
    local d, p = {}, {}
    local order = {}
    local function go(c, depth, parent)
        visited[c + 1] = true
        d[c + 1] = depth
        p[c + 1] = parent
        order[#order + 1] = c
        for _, nx in ipairs(graph[c + 1] or {}) do
            if not visited[nx + 1] then go(nx, depth + 1, c) end
        end
    end
    go(start, 0, -1)
    return order, d
end
local g = {{1,2},{3,6},{4,5},{},{},{7},{},{}}
local order, d = dfs_traverse(g, 0)
assert(#order == 8)
assert(d[1] == 0 and d[2] == 1 and d[4] == 2 and d[8] == 3)
print("PASS")''',
"c":'''#include <stdio.h>
static int visited_g[64], d_g[64], p_g[64], order_g[64], on_g;
static const int (*graph_g)[8];
static const int *gsize_g;
static void go(int c, int depth, int parent) {
    visited_g[c] = 1;
    d_g[c] = depth;
    p_g[c] = parent;
    order_g[on_g++] = c;
    for (int i = 0; i < gsize_g[c]; i++) {
        int nx = graph_g[c][i];
        if (!visited_g[nx]) go(nx, depth + 1, c);
    }
}
int main(void) {
    static const int graph[8][8] = {{1,2},{3,6},{4,5},{},{},{7},{},{}};
    static const int gsize[8] = {2,2,2,0,0,1,0,0};
    graph_g = graph;
    gsize_g = gsize;
    go(0, 0, -1);
    int want_d[] = {0,1,1,2,2,2,2,3};
    for (int i = 0; i < 8; i++) if (d_g[i] != want_d[i]) { printf("FAIL d %d\\n", i); return 1; }
    if (on_g != 8) { printf("FAIL order\\n"); return 1; }
    printf("PASS\\n"); return 0; }''',
"cpp":'''#include <cassert>
#include <iostream>
#include <vector>
static void dfsGo(size_t c, int depth, int parent,
                  const std::vector<std::vector<int>> &graph,
                  std::vector<bool> &visited, std::vector<int> &d,
                  std::vector<int> &p, std::vector<int> &order) {
    visited[c] = true;
    d[c] = depth;
    p[c] = parent;
    order.push_back(static_cast<int>(c));
    for (int nx : graph[c]) {
        size_t u = static_cast<size_t>(nx);
        if (!visited[u]) dfsGo(u, depth + 1, static_cast<int>(c), graph, visited, d, p, order);
    }
}
int main() {
    std::vector<std::vector<int>> g = {{1,2},{3,6},{4,5},{},{},{7},{},{}};
    size_t n = g.size();
    std::vector<bool> visited(n, false);
    std::vector<int> d(n, -1), p(n, -1), order;
    dfsGo(0, 0, -1, g, visited, d, p, order);
    std::vector<int> wantD = {0,1,1,2,2,2,2,3};
    assert(d == wantD);
    assert(order.size() == 8);
    std::cout << "PASS" << std::endl; }''',
"r":'''dfs_traverse <- function(graph, start) {
  n <- length(graph)
  visited <- rep(FALSE, n)
  d <- rep(-1L, n)
  p <- rep(-1L, n)
  order_ <- integer(0)
  go <- function(c, depth, parent) {
    visited[c + 1L] <<- TRUE
    d[c + 1L] <<- depth
    p[c + 1L] <<- parent
    order_ <<- c(order_, c)
    nb <- if (!is.null(graph[[c + 1L]])) graph[[c + 1L]] else integer(0)
    if (length(nb) > 0) {
      for (nx in nb) {
        if (!visited[nx + 1L]) go(nx, depth + 1L, c)
      }
    }
  }
  go(start, 0L, -1L)
  list(order = order_, d = d)
}
g <- list(c(1, 2), c(3, 6), c(4, 5), NULL, NULL, c(7), NULL, NULL)
res <- dfs_traverse(g, 0)
stopifnot(identical(as.integer(res$d), c(0L, 1L, 1L, 2L, 2L, 2L, 2L, 3L)))
stopifnot(length(res$order) == 8)
cat("PASS\\n")''',
"zig":'''const std = @import("std");
const Ctx = struct {
    visited: [64]bool,
    d: [64]i32,
    p: [64]i32,
    order: std.ArrayList(i32),
    graph: []const []const i32,
};
fn dfsGo(ctx: *Ctx, c: usize, depth: i32, parent: i32) void {
    ctx.visited[c] = true;
    ctx.d[c] = depth;
    ctx.p[c] = parent;
    ctx.order.append(@intCast(c)) catch unreachable;
    for (ctx.graph[c]) |nx| {
        const u: usize = @intCast(nx);
        if (!ctx.visited[u]) dfsGo(ctx, u, depth + 1, @intCast(c));
    }
}
pub fn main() !void {
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();
    const g0 = [_]i32{ 1, 2 };
    const g1 = [_]i32{ 3, 6 };
    const g2 = [_]i32{ 4, 5 };
    const g3 = [_]i32{};
    const g4 = [_]i32{};
    const g5 = [_]i32{7};
    const g6 = [_]i32{};
    const g7 = [_]i32{};
    const g = [_][]const i32{ &g0, &g1, &g2, &g3, &g4, &g5, &g6, &g7 };
    var ctx = Ctx{ .visited = undefined, .d = undefined, .p = undefined, .order = std.ArrayList(i32).init(std.heap.page_allocator), .graph = &g };
    for (0..8) |i| {
        ctx.visited[i] = false;
        ctx.d[i] = -1;
        ctx.p[i] = -1;
    }
    defer ctx.order.deinit();
    dfsGo(&ctx, 0, 0, -1);
    const wantD = [_]i32{ 0, 1, 1, 2, 2, 2, 2, 3 };
    for (wantD, 0..) |w, i| if (ctx.d[i] != w) return error.TestFailed;
    if (ctx.order.items.len != 8) return error.TestFailed;
    std.debug.print("PASS\\n", .{}); }''',
"dart":'''List<List<int>> dfsTraverse(List<List<int>> graph, int start) {
  final n = graph.length;
  final visited = List<bool>.filled(n, false);
  final d = List<int>.filled(n, -1);
  final p = List<int>.filled(n, -1);
  final order = <int>[];
  void go(int c, int depth, int parent) {
    visited[c] = true;
    d[c] = depth;
    p[c] = parent;
    order.add(c);
    for (final nx in graph[c]) {
      if (!visited[nx]) go(nx, depth + 1, c);
    }
  }
  go(start, 0, -1);
  return [order, d];
}
void main() {
  final g = <List<int>>[
    <int>[1, 2],
    <int>[3, 6],
    <int>[4, 5],
    <int>[],
    <int>[],
    <int>[7],
    <int>[],
    <int>[]
  ];
  final res = dfsTraverse(g, 0);
  if (res[1].toString() != '[0, 1, 1, 2, 2, 2, 2, 3]') throw StateError('d');
  if (res[0].length != 8) throw StateError('order');
  print('PASS'); }''',
}

LCSDP = {
"rust":'''fn lcs_length(s1: &str, s2: &str) -> i32 {
    let a: Vec<char> = s1.chars().collect();
    let b: Vec<char> = s2.chars().collect();
    let (m, n) = (a.len(), b.len());
    let mut dp = vec![0i32; n + 1];
    for i in 1..=m {
        let mut prev_diag = 0;
        for j in 1..=n {
            let tmp = dp[j];
            dp[j] = if a[i - 1] == b[j - 1] { prev_diag + 1 } else { dp[j].max(dp[j - 1]) };
            prev_diag = tmp;
        }
    }
    dp[n]
}
fn main() {
    assert_eq!(lcs_length("ABCBDAB", "BDCABA"), 4);
    assert_eq!(lcs_length("abc", "abc"), 3);
    assert_eq!(lcs_length("abc", "def"), 0);
    println!("PASS"); }''',
"lua":'''local function lcs_length(s1, s2)
    local m, n = #s1, #s2
    local dp = {}
    for j = 0, n do dp[j] = 0 end
    for i = 1, m do
        local prev_diag = 0
        for j = 1, n do
            local tmp = dp[j]
            if s1:sub(i, i) == s2:sub(j, j) then dp[j] = prev_diag + 1
            else dp[j] = math.max(dp[j], dp[j - 1]) end
            prev_diag = tmp
        end
    end
    return dp[n]
end
assert(lcs_length("ABCBDAB", "BDCABA") == 4)
assert(lcs_length("abc", "abc") == 3)
assert(lcs_length("abc", "def") == 0)
print("PASS")''',
"c":'''#include <stdio.h>
#include <string.h>
static int lcs_length(const char *s1, const char *s2) {
    int m = (int)strlen(s1), n = (int)strlen(s2);
    int dp[1001] = {0};
    for (int i = 1; i <= m; i++) {
        int prev_diag = 0;
        for (int j = 1; j <= n; j++) {
            int tmp = dp[j];
            dp[j] = s1[i - 1] == s2[j - 1] ? prev_diag + 1 : (dp[j] > dp[j - 1] ? dp[j] : dp[j - 1]);
            prev_diag = tmp;
        }
    }
    return dp[n];
}
int main(void) {
    if (lcs_length("ABCBDAB", "BDCABA") != 4) { printf("FAIL 1\\n"); return 1; }
    if (lcs_length("abc", "abc") != 3) { printf("FAIL 2\\n"); return 1; }
    printf("PASS\\n"); return 0; }''',
"cpp":'''#include <algorithm>
#include <cassert>
#include <iostream>
#include <string>
#include <vector>
static int lcsLength(const std::string &s1, const std::string &s2) {
    int m = static_cast<int>(s1.size()), n = static_cast<int>(s2.size());
    std::vector<int> dp(n + 1, 0);
    for (int i = 1; i <= m; ++i) {
        int prevDiag = 0;
        for (int j = 1; j <= n; ++j) {
            int tmp = dp[j];
            dp[j] = (s1[i - 1] == s2[j - 1]) ? prevDiag + 1 : std::max(dp[j], dp[j - 1]);
            prevDiag = tmp;
        }
    }
    return dp[n];
}
int main() {
    assert(lcsLength("ABCBDAB", "BDCABA") == 4);
    assert(lcsLength("abc", "abc") == 3);
    assert(lcsLength("abc", "def") == 0);
    std::cout << "PASS" << std::endl; }''',
"r":'''lcs_length <- function(s1, s2) {
  chars1 <- strsplit(s1, "")[[1]]
  chars2 <- strsplit(s2, "")[[1]]
  m <- length(chars1); n <- length(chars2)
  dp <- rep(0L, n + 1)
  for (i in 1:m) {
    prev_diag <- 0L
    for (j in 1:n) {
      tmp <- dp[j + 1]
      dp[j + 1] <- if (chars1[i] == chars2[j]) prev_diag + 1L else max(dp[j + 1], dp[j])
      prev_diag <- tmp
    }
  }
  dp[n + 1]
}
stopifnot(lcs_length("ABCBDAB", "BDCABA") == 4)
stopifnot(lcs_length("abc", "abc") == 3)
stopifnot(lcs_length("abc", "def") == 0)
cat("PASS\\n")''',
"zig":'''const std = @import("std");
fn lcsLength(s1: []const u8, s2: []const u8) i32 {
    const m = s1.len;
    const n = s2.len;
    var dp: [1001]i32 = undefined;
    for (0..n + 1) |j| dp[j] = 0;
    for (1..m + 1) |i| {
        var prev_diag: i32 = 0;
        for (1..n + 1) |j| {
            const tmp = dp[j];
            dp[j] = if (s1[i - 1] == s2[j - 1]) prev_diag + 1 else @max(dp[j], dp[j - 1]);
            prev_diag = tmp;
        }
    }
    return dp[n];
}
pub fn main() !void {
    if (lcsLength("ABCBDAB", "BDCABA") != 4) return error.TestFailed;
    if (lcsLength("abc", "abc") != 3) return error.TestFailed;
    if (lcsLength("abc", "def") != 0) return error.TestFailed;
    std.debug.print("PASS\\n", .{}); }''',
"dart":'''int lcsLength(String s1, String s2) {
  final m = s1.length, n = s2.length;
  final dp = List<int>.filled(n + 1, 0);
  for (var i = 1; i <= m; i++) {
    var prevDiag = 0;
    for (var j = 1; j <= n; j++) {
      final tmp = dp[j];
      dp[j] = s1[i - 1] == s2[j - 1] ? prevDiag + 1 : (dp[j] > dp[j - 1] ? dp[j] : dp[j - 1]);
      prevDiag = tmp;
    }
  }
  return dp[n];
}
void main() {
  if (lcsLength('ABCBDAB', 'BDCABA') != 4) throw StateError('c1');
  if (lcsLength('abc', 'abc') != 3) throw StateError('c2');
  if (lcsLength('abc', 'def') != 0) throw StateError('c3');
  print('PASS'); }''',
}

LRUNOTE = {
"rust":'''struct NoteLru { cap: usize, keys: std::collections::VecDeque<i32>, vals: std::collections::HashMap<i32, i32> }
impl NoteLru {
    fn new(cap: usize) -> Self { NoteLru { cap, keys: Default::default(), vals: Default::default() } }
    fn get(&mut self, k: i32) -> i32 {
        if let Some(&v) = self.vals.get(&k) {
            self.keys.retain(|&x| x != k);
            self.keys.push_back(k);
            v
        } else { -1 }
    }
    fn put(&mut self, k: i32, v: i32) {
        if self.vals.contains_key(&k) {
            self.keys.retain(|&x| x != k);
        } else if self.keys.len() == self.cap {
            let old = self.keys.pop_front().unwrap();
            self.vals.remove(&old);
        }
        self.keys.push_back(k);
        self.vals.insert(k, v);
    }
}
fn main() {
    // TS 笔记语义: cap=2, put(1,1), put(2,2), get(1)=1, put(3,3)逐出1, get(1)=-1, get(3)=3
    let mut c = NoteLru::new(2);
    c.put(1, 1);
    c.put(2, 2);
    assert_eq!(c.get(1), 1);
    c.put(3, 3);
    assert_eq!(c.get(1), -1);
    assert_eq!(c.get(3), 3);
    println!("PASS"); }''',
"lua":'''local NoteLru = {}
NoteLru.__index = NoteLru
function NoteLru.new(cap) return setmetatable({cap = cap, keys = {}, vals = {}}, NoteLru) end
function NoteLru:get(k)
    if self.vals[k] ~= nil then
        for i, key in ipairs(self.keys) do
            if key == k then table.remove(self.keys, i) break end
        end
        self.keys[#self.keys + 1] = k
        return self.vals[k]
    end
    return -1
end
function NoteLru:put(k, v)
    if self.vals[k] ~= nil then
        for i, key in ipairs(self.keys) do
            if key == k then table.remove(self.keys, i) break end
        end
    elseif #self.keys == self.cap then
        local old = table.remove(self.keys, 1)
        self.vals[old] = nil
    end
    self.keys[#self.keys + 1] = k
    self.vals[k] = v
end
local c = NoteLru.new(2)
c:put(1, 1); c:put(2, 2)
assert(c:get(1) == 1)
c:put(3, 3)
assert(c:get(1) == -1)
assert(c:get(3) == 3)
print("PASS")''',
"c":'''#include <stdio.h>
typedef struct { int cap, n; int keys[256]; int vals[256]; } NoteLru;
static void nl_init(NoteLru *c, int cap) { c->cap = cap; c->n = 0; }
static int nl_find(NoteLru *c, int k) { for (int i = 0; i < c->n; i++) if (c->keys[i] == k) return i; return -1; }
static void nl_remove_idx(NoteLru *c, int idx) {
    for (int i = idx; i + 1 < c->n; i++) { c->keys[i] = c->keys[i + 1]; c->vals[i] = c->vals[i + 1]; }
    c->n--;
}
static int nl_get(NoteLru *c, int k) {
    int i = nl_find(c, k);
    if (i < 0) return -1;
    int v = c->vals[i];
    int kv = c->keys[i];
    nl_remove_idx(c, i);
    c->keys[c->n] = kv; c->vals[c->n] = v; c->n++;
    return v;
}
static void nl_put(NoteLru *c, int k, int v) {
    int i = nl_find(c, k);
    if (i >= 0) {
        nl_remove_idx(c, i);
    } else if (c->n == c->cap) {
        nl_remove_idx(c, 0);
    }
    c->keys[c->n] = k; c->vals[c->n] = v; c->n++;
}
int main(void) {
    NoteLru c;
    nl_init(&c, 2);
    nl_put(&c, 1, 1);
    nl_put(&c, 2, 2);
    if (nl_get(&c, 1) != 1) { printf("FAIL 1\\n"); return 1; }
    nl_put(&c, 3, 3);
    if (nl_get(&c, 1) != -1) { printf("FAIL 2\\n"); return 1; }
    if (nl_get(&c, 3) != 3) { printf("FAIL 3\\n"); return 1; }
    printf("PASS\\n"); return 0; }''',
"cpp":'''#include <cassert>
#include <iostream>
#include <list>
#include <unordered_map>
struct NoteLru {
    int cap;
    std::list<std::pair<int, int>> items;
    std::unordered_map<int, std::list<std::pair<int, int>>::iterator> pos;
    explicit NoteLru(int capacity) : cap(capacity) {}
    int get(int key) {
        auto it = pos.find(key);
        if (it == pos.end()) return -1;
        items.splice(items.begin(), items, it->second);
        return it->second->second;
    }
    void put(int key, int value) {
        auto it = pos.find(key);
        if (it != pos.end()) {
            it->second->second = value;
            items.splice(items.begin(), items, it->second);
            return;
        }
        if (static_cast<int>(items.size()) == cap) {
            pos.erase(items.back().first);
            items.pop_back();
        }
        items.emplace_front(key, value);
        pos[key] = items.begin();
    }
};
int main() {
    NoteLru c(2);
    c.put(1, 1);
    c.put(2, 2);
    assert(c.get(1) == 1);
    c.put(3, 3);
    assert(c.get(1) == -1);
    assert(c.get(3) == 3);
    std::cout << "PASS" << std::endl; }''',
"r":'''NoteLruNote <- function(cap) {
  e <- new.env(parent = emptyenv())
  e$cap <- cap; e$keys <- integer(0); e$vals <- list()
  e$get <- function(k) {
    w <- match(k, e$keys)
    if (is.na(w)) return(-1L)
    e$keys <- c(e$keys[-w], e$keys[w])
    e$vals[[as.character(k)]]
  }
  e$put <- function(k, v) {
    w <- match(k, e$keys)
    if (!is.na(w)) {
      e$keys <- e$keys[-w]
    } else if (length(e$keys) == e$cap) {
      old <- e$keys[1]
      e$keys <- e$keys[-1]
      e$vals[[as.character(old)]] <- NULL
    }
    e$keys <- c(e$keys, k)
    e$vals[[as.character(k)]] <- v
  }
  e
}
c1 <- NoteLruNote(2)
c1$put(1, 1); c1$put(2, 2)
stopifnot(c1$get(1) == 1)
c1$put(3, 3)
stopifnot(c1$get(1) == -1, c1$get(3) == 3)
cat("PASS\\n")''',
"zig":'''const std = @import("std");
const NoteLru = struct {
    cap: usize,
    keys: [256]i32,
    vals: [256]i32,
    n: usize,
    fn init(cap: usize) NoteLru {
        return .{ .cap = cap, .keys = undefined, .vals = undefined, .n = 0 };
    }
    fn find(self: *NoteLru, k: i32) ?usize {
        for (0..self.n) |i| if (self.keys[i] == k) return i;
        return null;
    }
    fn removeIdx(self: *NoteLru, idx: usize) void {
        var i = idx;
        while (i + 1 < self.n) : (i += 1) {
            self.keys[i] = self.keys[i + 1];
            self.vals[i] = self.vals[i + 1];
        }
        self.n -= 1;
    }
    fn get(self: *NoteLru, k: i32) i32 {
        const i = self.find(k) orelse return -1;
        const v = self.vals[i];
        const kv = self.keys[i];
        self.removeIdx(i);
        self.keys[self.n] = kv;
        self.vals[self.n] = v;
        self.n += 1;
        return v;
    }
    fn put(self: *NoteLru, k: i32, v: i32) void {
        if (self.find(k)) |i| self.removeIdx(i) else if (self.n == self.cap) self.removeIdx(0);
        self.keys[self.n] = k;
        self.vals[self.n] = v;
        self.n += 1;
    }
};
pub fn main() !void {
    var c = NoteLru.init(2);
    c.put(1, 1);
    c.put(2, 2);
    if (c.get(1) != 1) return error.TestFailed;
    c.put(3, 3);
    if (c.get(1) != -1) return error.TestFailed;
    if (c.get(3) != 3) return error.TestFailed;
    std.debug.print("PASS\\n", .{}); }''',
"dart":'''class NoteLru {
  final int cap;
  final List<int> keys = [];
  final Map<int, int> vals = {};
  NoteLru(this.cap);
  int get(int k) {
    if (vals.containsKey(k)) {
      keys.remove(k);
      keys.add(k);
      return vals[k]!;
    }
    return -1;
  }
  void put(int k, int v) {
    if (vals.containsKey(k)) {
      keys.remove(k);
    } else if (keys.length == cap) {
      vals.remove(keys.removeAt(0));
    }
    keys.add(k);
    vals[k] = v;
  }
}
void main() {
  final c = NoteLru(2);
  c.put(1, 1);
  c.put(2, 2);
  if (c.get(1) != 1) throw StateError('c1');
  c.put(3, 3);
  if (c.get(1) != -1) throw StateError('c2');
  if (c.get(3) != 3) throw StateError('c3');
  print('PASS'); }''',
}

FIBNOTE = {
"rust":'''fn fib_memo(n: i32) -> i64 {
    // 动态规划笔记: fibonacci 带记忆化 vs 递归
    let mut memo = std::collections::HashMap::new();
    fn go(n: i32, memo: &mut std::collections::HashMap<i32, i64>) -> i64 {
        if n <= 1 { return n as i64; }
        if let Some(&v) = memo.get(&n) { return v; }
        let v = go(n - 1, memo) + go(n - 2, memo);
        memo.insert(n, v);
        v
    }
    go(n, &mut memo)
}
fn main() {
    assert_eq!(fib_memo(10), 55);
    assert_eq!(fib_memo(20), 6765);
    assert_eq!(fib_memo(0), 0);
    println!("PASS"); }''',
"lua":'''local function fib_memo(n)
    local memo = {}
    local function go(k)
        if k <= 1 then return k end
        if memo[k] then return memo[k] end
        memo[k] = go(k - 1) + go(k - 2)
        return memo[k]
    end
    return go(n)
end
assert(fib_memo(10) == 55)
assert(fib_memo(20) == 6765)
assert(fib_memo(0) == 0)
print("PASS")''',
"c":'''#include <stdio.h>
static long memo_g[64];
static long go(int n) {
    if (n <= 1) return n;
    if (memo_g[n]) return memo_g[n];
    memo_g[n] = go(n - 1) + go(n - 2);
    return memo_g[n];
}
static long fib_memo(int n) {
    for (int i = 0; i < 64; i++) memo_g[i] = 0;
    return go(n);
}
int main(void) {
    if (fib_memo(10) != 55 || fib_memo(20) != 6765 || fib_memo(0) != 0) { printf("FAIL\\n"); return 1; }
    printf("PASS\\n"); return 0; }''',
"cpp":'''#include <cassert>
#include <iostream>
#include <unordered_map>
static long long fibMemo(int n) {
    std::unordered_map<int, long long> memo;
    std::function<long long(int)> go = [&](int k) -> long long {
        if (k <= 1) return k;
        if (memo.count(k)) return memo[k];
        return memo[k] = go(k - 1) + go(k - 2);
    };
    return go(n);
}
int main() { assert(fibMemo(10) == 55); assert(fibMemo(20) == 6765); assert(fibMemo(0) == 0); std::cout << "PASS" << std::endl; }''',
"r":'''fib_memo <- function(n) {
  memo <- new.env(parent = emptyenv())
  go <- function(k) {
    if (k <= 1) return(k)
    key <- as.character(k)
    if (!is.null(memo[[key]])) return(memo[[key]])
    memo[[key]] <<- go(k - 1L) + go(k - 2L)
    memo[[key]]
  }
  go(n)
}
stopifnot(fib_memo(10) == 55, fib_memo(20) == 6765, fib_memo(0) == 0)
cat("PASS\\n")''',
"zig":'''const std = @import("std");
fn fibMemo(n: i32) i64 {
    var memo: [64]i64 = undefined;
    for (0..64) |i| memo[i] = -1;
    const D = struct {
        fn go(k: i32, m: []i64) i64 {
            if (k <= 1) return k;
            if (m[@intCast(k)] != -1) return m[@intCast(k)];
            m[@intCast(k)] = go(k - 1, m) + go(k - 2, m);
            return m[@intCast(k)];
        }
    };
    return D.go(n, &memo);
}
pub fn main() !void {
    if (fibMemo(10) != 55 or fibMemo(20) != 6765 or fibMemo(0) != 0) return error.TestFailed;
    std.debug.print("PASS\\n", .{}); }''',
"dart":'''int fibMemo(int n) {
  final memo = <int, int>{};
  int go(int k) {
    if (k <= 1) return k;
    if (memo.containsKey(k)) return memo[k]!;
    memo[k] = go(k - 1) + go(k - 2);
    return memo[k]!;
  }
  return go(n);
}
void main() { if (fibMemo(10) != 55 || fibMemo(20) != 6765 || fibMemo(0) != 0) throw StateError('x'); print('PASS'); }''',
}

DIJKSTRA = {
"rust":'''fn dijkstra_shortest(graph: &[Vec<(usize, i32)>], start: usize) -> Vec<i32> {
    let n = graph.len();
    let mut dist = vec![i32::MAX; n];
    dist[start] = 0;
    let mut visited = vec![false; n];
    loop {
        let mut u = usize::MAX;
        for i in 0..n {
            if !visited[i] && (u == usize::MAX || dist[i] < dist[u]) { u = i; }
        }
        if u == usize::MAX || dist[u] == i32::MAX { break; }
        visited[u] = true;
        for &(v, w) in &graph[u] {
            if dist[u] + w < dist[v] { dist[v] = dist[u] + w; }
        }
    }
    dist
}
fn main() {
    // 5节点: 0->1(10), 0->2(3), 1->2(1), 2->1(4), 1->3(2), 2->3(8), 3->4(7)
    let g = vec![vec![(1,10),(2,3)],vec![(2,1),(3,2)],vec![(1,4),(3,8)],vec![(4,7)],vec![]];
    let d = dijkstra_shortest(&g, 0);
    assert_eq!(d[0], 0);
    assert_eq!(d[1], 7);   // 0->2->1 = 3+4
    assert_eq!(d[2], 3);
    assert_eq!(d[3], 9);   // 0->2->1->3 = 3+4+2
    assert_eq!(d[4], 16);
    println!("PASS"); }''',
"lua":'''local function dijkstra_shortest(graph, start)
    local n = #graph
    local dist, visited = {}, {}
    for i = 1, n do dist[i] = math.huge; visited[i] = false end
    dist[start + 1] = 0
    while true do
        local u = nil
        for i = 1, n do
            if not visited[i] and (u == nil or dist[i] < dist[u]) then u = i end
        end
        if u == nil or dist[u] == math.huge then break end
        visited[u] = true
        for _, e in ipairs(graph[u] or {}) do
            local v, w = e[1] + 1, e[2]
            if dist[u] + w < dist[v] then dist[v] = dist[u] + w end
        end
    end
    local out = {}
    for i = 1, n do out[i] = dist[i] end
    return out
end
local g = {{{1,10},{2,3}},{{2,1},{3,2}},{{1,4},{3,8}},{{4,7}},{}}
local d = dijkstra_shortest(g, 0)
assert(d[1] == 0 and d[2] == 7 and d[3] == 3 and d[4] == 9 and d[5] == 16)
print("PASS")''',
"c":'''#include <stdio.h>
static void dijkstra_shortest(const int edges[][3], const int esizes[], int n, int start, int out[]) {
    int dist[64], visited[64] = {0};
    for (int i = 0; i < n; i++) dist[i] = 0x3f3f3f3f;
    dist[start] = 0;
    while (1) {
        int u = -1;
        for (int i = 0; i < n; i++) {
            if (!visited[i] && (u < 0 || dist[i] < dist[u])) u = i;
        }
        if (u < 0 || dist[u] == 0x3f3f3f3f) break;
        visited[u] = 1;
        for (int i = 0; i < esizes[u]; i++) {
            int v = edges[u][i * 2], w = edges[u][i * 2 + 1];
            if (dist[u] + w < dist[v]) dist[v] = dist[u] + w;
        }
    }
    for (int i = 0; i < n; i++) out[i] = dist[i];
}
int main(void) {
    /* 5节点: 0->1(10),0->2(3),1->2(1),1->3(2),2->1(4),2->3(8),3->4(7) */
    static const int edges[5][6] = {{1,10,2,3}, {2,1,3,2}, {1,4,3,8}, {4,7}, {}};
    static const int esizes[5] = {2,2,2,1,0};
    int out[64];
    dijkstra_shortest(edges, esizes, 5, 0, out);
    int want[] = {0,7,3,9,16};
    for (int i = 0; i < 5; i++) if (out[i] != want[i]) { printf("FAIL %d\\n", i); return 1; }
    printf("PASS\\n"); return 0; }''',
"cpp":'''#include <cassert>
#include <iostream>
#include <vector>
static std::vector<int> dijkstraShortest(const std::vector<std::vector<std::pair<int, int>>> &graph, int start) {
    size_t n = graph.size();
    std::vector<int> dist(n, 0x3f3f3f3f);
    std::vector<bool> visited(n, false);
    dist[start] = 0;
    while (true) {
        int u = -1;
        for (size_t i = 0; i < n; ++i) {
            if (!visited[i] && (u < 0 || dist[i] < dist[u])) u = static_cast<int>(i);
        }
        if (u < 0 || dist[u] == 0x3f3f3f3f) break;
        visited[u] = true;
        for (auto &[v, w] : graph[u]) {
            if (dist[u] + w < dist[v]) dist[v] = dist[u] + w;
        }
    }
    return dist;
}
int main() {
    std::vector<std::vector<std::pair<int, int>>> g = {
        {{1,10},{2,3}}, {{2,1},{3,2}}, {{1,4},{3,8}}, {{4,7}}, {}
    };
    auto d = dijkstraShortest(g, 0);
    assert(d[0] == 0 && d[1] == 7 && d[2] == 3 && d[3] == 9 && d[4] == 16);
    std::cout << "PASS" << std::endl; }''',
"r":'''dijkstra_shortest <- function(edges_list, start) {
  n <- length(edges_list)
  dist <- rep(.Machine$integer.max, n)
  visited <- rep(FALSE, n)
  dist[start + 1L] <- 0L
  repeat {
    u <- NA
    for (i in 1:n) {
      if (!visited[i] && (is.na(u) || dist[i] < dist[u])) u <- i
    }
    if (is.na(u) || dist[u] == .Machine$integer.max) break
    visited[u] <- TRUE
    nb <- if (!is.null(edges_list[[u]])) edges_list[[u]] else list()
    if (length(nb) > 0) {
      for (e in nb) {
        v <- e[1] + 1L
        w <- e[2]
        nd <- as.numeric(dist[u]) + w
        if (nd < dist[v] && nd < .Machine$integer.max) dist[v] <- as.integer(nd)
      }
    }
  }
  dist
}
g <- list(list(c(1L, 10L), c(2L, 3L)), list(c(2L, 1L), c(3L, 2L)), list(c(1L, 4L), c(3L, 8L)), list(c(4L, 7L)), list())
d <- dijkstra_shortest(g, 0)
stopifnot(d[1] == 0, d[2] == 7, d[3] == 3, d[4] == 9, d[5] == 16)
cat("PASS\\n")''',
"zig":'''const std = @import("std");
const INF: i32 = 0x3f3f3f3f;
fn dijkstraShortest(graph: []const []const [2]i32, start: usize) [8]i32 {
    const n = graph.len;
    var dist: [8]i32 = undefined;
    var visited: [8]bool = undefined;
    for (0..n) |i| {
        dist[i] = INF;
        visited[i] = false;
    }
    dist[start] = 0;
    while (true) {
        var u: usize = std.math.maxInt(usize);
        for (0..n) |i| {
            if (!visited[i] and (u == std.math.maxInt(usize) or dist[i] < dist[u])) u = i;
        }
        if (u == std.math.maxInt(usize) or dist[u] == INF) break;
        visited[u] = true;
        for (graph[u]) |e| {
            const v: usize = @intCast(e[0]);
            if (dist[u] + e[1] < dist[v]) dist[v] = dist[u] + e[1];
        }
    }
    return dist;
}
pub fn main() !void {
    const g0 = [_][2]i32{ .{ 1, 10 }, .{ 2, 3 } };
    const g1 = [_][2]i32{ .{ 2, 1 }, .{ 3, 2 } };
    const g2 = [_][2]i32{ .{ 1, 4 }, .{ 3, 8 } };
    const g3 = [_][2]i32{.{ 4, 7 }};
    const g4 = [_][2]i32{};
    const g = [_][]const [2]i32{ &g0, &g1, &g2, &g3, &g4 };
    const d = dijkstraShortest(&g, 0);
    if (d[0] != 0 or d[1] != 7 or d[2] != 3 or d[3] != 9 or d[4] != 16) return error.TestFailed;
    std.debug.print("PASS\\n", .{}); }''',
"dart":'''List<int> dijkstraShortest(List<List<List<int>>> graph, int start) {
  final n = graph.length;
  final dist = List<int>.filled(n, 0x3f3f3f3f);
  final visited = List<bool>.filled(n, false);
  dist[start] = 0;
  while (true) {
    int u = -1;
    for (var i = 0; i < n; i++) {
      if (!visited[i] && (u < 0 || dist[i] < dist[u])) u = i;
    }
    if (u < 0 || dist[u] == 0x3f3f3f3f) break;
    visited[u] = true;
    for (final e in graph[u]) {
      final v = e[0], w = e[1];
      if (dist[u] + w < dist[v]) dist[v] = dist[u] + w;
    }
  }
  return dist;
}
void main() {
  final g = <List<List<int>>>[
    [[1, 10], [2, 3]],
    [[2, 1], [3, 2]],
    [[1, 4], [3, 8]],
    [[4, 7]],
    []
  ];
  final d = dijkstraShortest(g, 0);
  if (d[0] != 0 || d[1] != 7 || d[2] != 3 || d[3] != 9 || d[4] != 16) throw StateError('x');
  print('PASS'); }''',
}

PROBS = [
    ("lc_145355207_leetcode_lcr_152._验证二叉搜索树的后序遍历序列", POSTORDER, "145355207", "LeetCode LCR 152. 验证二叉搜索树的后序遍历序列"),
    ("lc_113764246_图搜索之dfs详解", DFS, "113764246", "图搜索之DFS详解"),
    ("lc_113951689_动态规划之lcs_0", LCSDP, "113951689", "动态规划之LCS"),
    ("lc_134097112_实现_lru_缓存算法功能", LRUNOTE, "134097112", "实现LRU缓存算法功能"),
    ("lc_113877588_动态规划之fibonacci_power_spu_lmp", FIBNOTE, "113877588", "动态规划之Fibonacci"),
    ("lc_108717090_减治策略之详解dijkstra算法", DIJKSTRA, "108717090", "减治策略之详解Dijkstra算法"),
]
count = 0
for pdir, algo, bid, title in PROBS:
    ts_dir = f"/Users/Wang/Code/webfault-ai/dsa/ts/notes/{pdir}"
    sols = sorted(f[:-3] for f in os.listdir(ts_dir) if f.startswith("solution_") and f.endswith(".ts"))
    for lang in LANGNAME:
        ext = EXT[lang]
        for sol in sols:
            n = sol.replace("solution_", "").split("_")[0]
            head = head_comment(lang, bid, f"{title} — {LANGNAME[lang]} 版（方案{n}）")
            emit(lang, f"notes/{pdir}/{sol}.{ext}", head + "\n" + algo[lang])
            count += 1
print(f"emitted {count} files")
