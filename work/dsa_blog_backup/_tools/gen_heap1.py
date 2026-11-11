#!/usr/bin/env python3
# gen_heap1.py — heap 第一批：lc_208/lc_313/lc_502/lc_451 × 7语言
import sys, os; sys.path.insert(0, "/Users/Wang/Code/webfault-ai/dsa/_tools")
from langlib import emit, head_comment, EXT

B = {"208": "135533027", "313": "133547933", "502": "136847926", "451": "137060905"}
LANGNAME = {"rust": "Rust", "lua": "Lua", "c": "C", "cpp": "C++", "r": "R", "zig": "Zig", "dart": "Dart"}

A208 = {
"rust": '''use std::collections::HashMap;
struct TrieNode { children: HashMap<char, Box<TrieNode>>, is_end: bool }
impl TrieNode { fn new() -> Self { TrieNode { children: HashMap::new(), is_end: false } } }
struct Trie { root: TrieNode }
impl Trie {
    fn new() -> Self { Trie { root: TrieNode::new() } }
    fn insert(&mut self, word: &str) {
        let mut node = &mut self.root;
        for ch in word.chars() {
            node = node.children.entry(ch).or_insert_with(|| Box::new(TrieNode::new())).as_mut();
        }
        node.is_end = true;
    }
    fn search(&self, word: &str) -> bool {
        let mut node = &self.root;
        for ch in word.chars() {
            match node.children.get(&ch) { Some(n) => node = n, None => return false }
        }
        node.is_end
    }
    fn starts_with(&self, prefix: &str) -> bool {
        let mut node = &self.root;
        for ch in prefix.chars() {
            match node.children.get(&ch) { Some(n) => node = n, None => return false }
        }
        true
    }
}
fn main() {
    let mut t = Trie::new();
    t.insert("apple");
    assert!(t.search("apple"));
    assert!(!t.search("app"));
    assert!(t.starts_with("app"));
    assert!(!t.search("appl"));
    println!("PASS");
}
''',
"lua": '''local TrieNode = {}
TrieNode.__index = TrieNode
function TrieNode.new() return setmetatable({children = {}, is_end = false}, TrieNode) end
local Trie = {}
Trie.__index = Trie
function Trie.new() return setmetatable({root = TrieNode.new()}, Trie) end
function Trie:insert(word)
    local node = self.root
    for i = 1, #word do
        local ch = word:sub(i, i)
        if not node.children[ch] then node.children[ch] = TrieNode.new() end
        node = node.children[ch]
    end
    node.is_end = true
end
function Trie:search(word)
    local node = self.root
    for i = 1, #word do
        local ch = word:sub(i, i)
        if not node.children[ch] then return false end
        node = node.children[ch]
    end
    return node.is_end
end
function Trie:startsWith(prefix)
    local node = self.root
    for i = 1, #prefix do
        local ch = prefix:sub(i, i)
        if not node.children[ch] then return false end
        node = node.children[ch]
    end
    return true
end
local t = Trie.new()
t:insert("apple")
assert(t:search("apple") == true)
assert(t:search("app") == false)
assert(t:startsWith("app") == true)
assert(t:search("appl") == false)
print("PASS")
''',
"c": '''#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef struct TrieNode { struct TrieNode *children[26]; int is_end; } TrieNode;
static TrieNode *tn_new() { return calloc(1, sizeof(TrieNode)); }
static void tn_free(TrieNode *n) {
    if (!n) return;
    for (int i = 0; i < 26; i++) tn_free(n->children[i]);
    free(n);
}
static void trie_insert(TrieNode *root, const char *word) {
    TrieNode *node = root;
    for (const char *p = word; *p; p++) {
        int idx = *p - 'a';
        if (!node->children[idx]) node->children[idx] = tn_new();
        node = node->children[idx];
    }
    node->is_end = 1;
}
static TrieNode *trie_walk(TrieNode *root, const char *s) {
    TrieNode *node = root;
    for (const char *p = s; *p; p++) {
        int idx = *p - 'a';
        if (idx < 0 || idx >= 26) return NULL;
        if (!node->children[idx]) return NULL;
        node = node->children[idx];
    }
    return node;
}
static int trie_search(TrieNode *root, const char *word) {
    TrieNode *n = trie_walk(root, word);
    return n && n->is_end;
}
static int trie_starts(TrieNode *root, const char *prefix) { return trie_walk(root, prefix) != NULL; }
int main(void) {
    TrieNode *t = tn_new();
    trie_insert(t, "apple");
    if (!trie_search(t, "apple")) { printf("FAIL 1\\n"); return 1; }
    if (trie_search(t, "app")) { printf("FAIL 2\\n"); return 1; }
    if (!trie_starts(t, "app")) { printf("FAIL 3\\n"); return 1; }
    if (trie_search(t, "appl")) { printf("FAIL 4\\n"); return 1; }
    tn_free(t);
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''#include <cassert>
#include <iostream>
#include <memory>
#include <unordered_map>
struct TrieNode {
    std::unordered_map<char, std::unique_ptr<TrieNode>> children;
    bool isEnd = false;
};
struct Trie {
    std::unique_ptr<TrieNode> root = std::make_unique<TrieNode>();
    void insert(const std::string &word) {
        TrieNode *node = root.get();
        for (char ch : word) {
            auto &child = node->children[ch];
            if (!child) child = std::make_unique<TrieNode>();
            node = child.get();
        }
        node->isEnd = true;
    }
    bool search(const std::string &word) const {
        const TrieNode *node = root.get();
        for (char ch : word) {
            auto it = node->children.find(ch);
            if (it == node->children.end()) return false;
            node = it->second.get();
        }
        return node->isEnd;
    }
    bool startsWith(const std::string &prefix) const {
        const TrieNode *node = root.get();
        for (char ch : prefix) {
            auto it = node->children.find(ch);
            if (it == node->children.end()) return false;
            node = it->second.get();
        }
        return true;
    }
};
int main() {
    Trie t;
    t.insert("apple");
    assert(t.search("apple"));
    assert(!t.search("app"));
    assert(t.startsWith("app"));
    assert(!t.search("appl"));
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''TrieNode <- function() {
  e <- new.env(parent = emptyenv())
  e$children <- new.env(parent = emptyenv())
  e$is_end <- FALSE
  e
}
Trie <- function() { e <- new.env(parent = emptyenv()); e$root <- TrieNode(); e }
trie_insert <- function(t, word) {
  node <- t$root
  chars <- strsplit(word, "")[[1]]
  for (ch in chars) {
    if (is.null(node$children[[ch]])) node$children[[ch]] <- TrieNode()
    node <- node$children[[ch]]
  }
  node$is_end <- TRUE
}
trie_walk <- function(t, s) {
  node <- t$root
  chars <- strsplit(s, "")[[1]]
  for (ch in chars) {
    if (is.null(node$children[[ch]])) return(NULL)
    node <- node$children[[ch]]
  }
  node
}
trie_search <- function(t, word) { n <- trie_walk(t, word); !is.null(n) && n$is_end }
trie_starts <- function(t, prefix) !is.null(trie_walk(t, prefix))
t <- Trie()
trie_insert(t, "apple")
stopifnot(trie_search(t, "apple"), !trie_search(t, "app"), trie_starts(t, "app"), !trie_search(t, "appl"))
cat("PASS\\n")
''',
"zig": '''const std = @import("std");
const TrieNode = struct { children: [26]?*TrieNode, is_end: bool };
fn tnNew(alloc: std.mem.Allocator) *TrieNode {
    const n = alloc.create(TrieNode) catch unreachable;
    n.* = .{ .children = [_]?*TrieNode{null} ** 26, .is_end = false };
    return n;
}
const Trie = struct {
    root: *TrieNode,
    fn init(alloc: std.mem.Allocator) Trie { return .{ .root = tnNew(alloc) }; }
    fn insert(self: *Trie, word: []const u8, alloc: std.mem.Allocator) void {
        var node = self.root;
        for (word) |ch| {
            const idx = ch - 'a';
            if (node.children[idx] == null) node.children[idx] = tnNew(alloc);
            node = node.children[idx].?;
        }
        node.is_end = true;
    }
    fn walk(self: *Trie, s: []const u8) ?*TrieNode {
        var node = self.root;
        for (s) |ch| {
            if (ch < 'a' or ch > 'z') return null;
            const idx = ch - 'a';
            if (node.children[idx] == null) return null;
            node = node.children[idx].?;
        }
        return node;
    }
    fn search(self: *Trie, word: []const u8) bool {
        const n = self.walk(word) orelse return false;
        return n.is_end;
    }
    fn startsWith(self: *Trie, prefix: []const u8) bool {
        return self.walk(prefix) != null;
    }
};
pub fn main() !void {
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();
    const alloc = arena.allocator();
    var t = Trie.init(alloc);
    t.insert("apple", alloc);
    if (!t.search("apple")) return error.TestFailed;
    if (t.search("app")) return error.TestFailed;
    if (!t.startsWith("app")) return error.TestFailed;
    if (t.search("appl")) return error.TestFailed;
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''class TrieNode {
  final Map<String, TrieNode> children = {};
  bool isEnd = false;
}
class Trie {
  final TrieNode root = TrieNode();
  void insert(String word) {
    var node = root;
    for (final ch in word.split('')) {
      node.children[ch] ??= TrieNode();
      node = node.children[ch]!;
    }
    node.isEnd = true;
  }
  TrieNode? _walk(String s) {
    var node = root;
    for (final ch in s.split('')) {
      final next = node.children[ch];
      if (next == null) return null;
      node = next;
    }
    return node;
  }
  bool search(String word) {
    final n = _walk(word);
    return n != null && n.isEnd;
  }
  bool startsWith(String prefix) => _walk(prefix) != null;
}
void main() {
  final t = Trie();
  t.insert('apple');
  if (!t.search('apple')) throw StateError('c1');
  if (t.search('app')) throw StateError('c2');
  if (!t.startsWith('app')) throw StateError('c3');
  if (t.search('appl')) throw StateError('c4');
  print('PASS');
}
''',
}

A313 = {
"rust": '''fn nth_super_ugly_number(n: usize, primes: &[i64]) -> i64 {
    let mut ugly = vec![1i64; n];
    let mut idx = vec![0usize; primes.len()];
    let mut val: Vec<i64> = primes.to_vec();
    for i in 1..n {
        let mut next = i64::MAX;
        for k in 0..primes.len() { if val[k] < next { next = val[k]; } }
        ugly[i] = next;
        for k in 0..primes.len() {
            if val[k] == next {
                idx[k] += 1;
                val[k] = ugly[idx[k]] * primes[k];
            }
        }
    }
    ugly[n - 1]
}
fn main() {
    assert_eq!(nth_super_ugly_number(12, &[2, 7, 13, 19]), 32);
    assert_eq!(nth_super_ugly_number(1, &[2, 7, 13, 19]), 1);
    println!("PASS");
}
''',
"lua": '''local function nth_super_ugly_number(n, primes)
    local ugly = {}
    ugly[1] = 1
    local idx, val = {}, {}
    for k = 1, #primes do idx[k] = 1; val[k] = primes[k] end
    for i = 2, n do
        local next = math.huge
        for k = 1, #primes do if val[k] < next then next = val[k] end end
        ugly[i] = next
        for k = 1, #primes do
            if val[k] == next then
                idx[k] = idx[k] + 1
                val[k] = ugly[idx[k]] * primes[k]
            end
        end
    end
    return ugly[n]
end
assert(nth_super_ugly_number(12, {2, 7, 13, 19}) == 32)
assert(nth_super_ugly_number(1, {2, 7, 13, 19}) == 1)
print("PASS")
''',
"c": '''#include <stdio.h>
static long nth_super_ugly_number(int n, const long *primes, int np) {
    long ugly[1024];
    int idx[64];
    long val[64];
    ugly[0] = 1;
    for (int k = 0; k < np; k++) { idx[k] = 0; val[k] = primes[k]; }
    for (int i = 1; i < n; i++) {
        long next = ~0UL >> 1;
        for (int k = 0; k < np; k++) if (val[k] < next) next = val[k];
        ugly[i] = next;
        for (int k = 0; k < np; k++) {
            if (val[k] == next) { idx[k]++; val[k] = ugly[idx[k]] * primes[k]; }
        }
    }
    return ugly[n - 1];
}
int main(void) {
    long p[] = {2, 7, 13, 19};
    if (nth_super_ugly_number(12, p, 4) != 32) { printf("FAIL 1\\n"); return 1; }
    if (nth_super_ugly_number(1, p, 4) != 1) { printf("FAIL 2\\n"); return 1; }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''#include <cassert>
#include <cstdint>
#include <iostream>
#include <vector>
static int64_t nthSuperUglyNumber(int n, const std::vector<int64_t> &primes) {
    std::vector<int64_t> ugly(n, 1);
    std::vector<size_t> idx(primes.size(), 0);
    std::vector<int64_t> val(primes);
    for (int i = 1; i < n; ++i) {
        int64_t next = INT64_MAX;
        for (size_t k = 0; k < primes.size(); ++k) next = std::min(next, val[k]);
        ugly[i] = next;
        for (size_t k = 0; k < primes.size(); ++k) {
            if (val[k] == next) {
                ++idx[k];
                val[k] = ugly[idx[k]] * primes[k];
            }
        }
    }
    return ugly[n - 1];
}
int main() {
    assert(nthSuperUglyNumber(12, {2, 7, 13, 19}) == 32);
    assert(nthSuperUglyNumber(1, {2, 7, 13, 19}) == 1);
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''nth_super_ugly_number <- function(n, primes) {
  ugly <- rep(1, n)
  idx <- rep(1L, length(primes))
  val <- primes
  if (n >= 2) for (i in 2:n) {
    next_v <- min(val)
    ugly[i] <- next_v
    for (k in seq_along(primes)) {
      if (val[k] == next_v) {
        idx[k] <- idx[k] + 1L
        val[k] <- ugly[idx[k]] * primes[k]
      }
    }
  }
  ugly[n]
}
stopifnot(nth_super_ugly_number(12, c(2, 7, 13, 19)) == 32)
stopifnot(nth_super_ugly_number(1, c(2, 7, 13, 19)) == 1)
cat("PASS\\n")
''',
"zig": '''const std = @import("std");
fn nthSuperUglyNumber(n: usize, primes: []const i64, alloc: std.mem.Allocator) i64 {
    var ugly = alloc.alloc(i64, n) catch unreachable;
    defer alloc.free(ugly);
    var idx = alloc.alloc(usize, primes.len) catch unreachable;
    defer alloc.free(idx);
    var val = alloc.alloc(i64, primes.len) catch unreachable;
    defer alloc.free(val);
    ugly[0] = 1;
    for (primes, 0..) |p, k| { idx[k] = 0; val[k] = p; }
    var i: usize = 1;
    while (i < n) : (i += 1) {
        var next: i64 = std.math.maxInt(i64);
        for (val) |v| {
            if (v < next) next = v;
        }
        ugly[i] = next;
        for (primes, 0..) |p, k| {
            if (val[k] == next) {
                idx[k] += 1;
                val[k] = ugly[idx[k]] * p;
            }
        }
    }
    return ugly[n - 1];
}
pub fn main() !void {
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();
    const alloc = arena.allocator();
    if (nthSuperUglyNumber(12, &[_]i64{ 2, 7, 13, 19 }, alloc) != 32) return error.TestFailed;
    if (nthSuperUglyNumber(1, &[_]i64{ 2, 7, 13, 19 }, alloc) != 1) return error.TestFailed;
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''int nthSuperUglyNumber(int n, List<int> primes) {
  final ugly = List<int>.filled(n, 1);
  final idx = List<int>.filled(primes.length, 0);
  final val = List<int>.from(primes);
  for (var i = 1; i < n; i++) {
    var next = 0x7fffffffffffffff;
    for (final v in val) {
      if (v < next) next = v;
    }
    ugly[i] = next;
    for (var k = 0; k < primes.length; k++) {
      if (val[k] == next) {
        idx[k]++;
        val[k] = ugly[idx[k]] * primes[k];
      }
    }
  }
  return ugly[n - 1];
}
void main() {
  if (nthSuperUglyNumber(12, [2, 7, 13, 19]) != 32) throw StateError('c1');
  if (nthSuperUglyNumber(1, [2, 7, 13, 19]) != 1) throw StateError('c2');
  print('PASS');
}
''',
}

A502 = {
"rust": '''fn find_maximized_capital(mut k: i32, mut w: i64, profits: &[i64], capital: &[i64]) -> i64 {
    let n = profits.len();
    let mut projects: Vec<(i64, i64)> = (0..n).map(|i| (capital[i], profits[i])).collect();
    projects.sort();
    let mut i = 0usize;
    while k > 0 {
        // 选可用项目中利润最大者（等价于最大堆）
        let mut best: i64 = -1;
        let mut best_j: i64 = -1;
        for j in 0..n as i64 {
            if projects[j as usize].0 <= w && projects[j as usize].1 > best {
                best = projects[j as usize].1;
                best_j = j;
            }
        }
        if best_j < 0 { break; }
        w += best;
        projects[best_j as usize].0 = i64::MAX; // 标记已用
        k -= 1;
    }
    w
}
fn main() {
    assert_eq!(find_maximized_capital(2, 0, &[1, 2, 3], &[0, 1, 1]), 4);
    assert_eq!(find_maximized_capital(3, 0, &[1, 2, 3], &[0, 1, 2]), 6);
    assert_eq!(find_maximized_capital(1, 0, &[1, 2], &[1, 2]), 0);
    assert_eq!(find_maximized_capital(2, 1, &[1, 2, 3], &[1, 1, 2]), 6);
    println!("PASS");
}
''',
"lua": '''local function find_maximized_capital(k, w, profits, capital)
    local n = #profits
    local used = {}
    for _ = 1, k do
        local best, best_j = -1, -1
        for j = 1, n do
            if not used[j] and capital[j] <= w and profits[j] > best then
                best = profits[j]
                best_j = j
            end
        end
        if best_j < 0 then break end
        w = w + best
        used[best_j] = true
    end
    return w
end
assert(find_maximized_capital(2, 0, {1, 2, 3}, {0, 1, 1}) == 4)
assert(find_maximized_capital(3, 0, {1, 2, 3}, {0, 1, 2}) == 6)
assert(find_maximized_capital(1, 0, {1, 2}, {1, 2}) == 0)
assert(find_maximized_capital(2, 1, {1, 2, 3}, {1, 1, 2}) == 6)
print("PASS")
''',
"c": '''#include <stdio.h>
static long find_maximized_capital(int k, long w, const long *profits, const long *capital, int n) {
    int used[64] = {0};
    for (int t = 0; t < k; t++) {
        long best = -1;
        int best_j = -1;
        for (int j = 0; j < n; j++) {
            if (!used[j] && capital[j] <= w && profits[j] > best) { best = profits[j]; best_j = j; }
        }
        if (best_j < 0) break;
        w += best;
        used[best_j] = 1;
    }
    return w;
}
int main(void) {
    if (find_maximized_capital(2, 0, (long[]){1,2,3}, (long[]){0,1,1}, 3) != 4) { printf("FAIL 1\\n"); return 1; }
    if (find_maximized_capital(3, 0, (long[]){1,2,3}, (long[]){0,1,2}, 3) != 6) { printf("FAIL 2\\n"); return 1; }
    if (find_maximized_capital(1, 0, (long[]){1,2}, (long[]){1,2}, 2) != 0) { printf("FAIL 3\\n"); return 1; }
    if (find_maximized_capital(2, 1, (long[]){1,2,3}, (long[]){1,1,2}, 3) != 6) { printf("FAIL 4\\n"); return 1; }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''#include <cassert>
#include <iostream>
#include <vector>
static long long findMaximizedCapital(int k, long long w, const std::vector<long long> &profits, const std::vector<long long> &capital) {
    int n = static_cast<int>(profits.size());
    std::vector<bool> used(n, false);
    for (int t = 0; t < k; ++t) {
        long long best = -1;
        int best_j = -1;
        for (int j = 0; j < n; ++j) {
            if (!used[j] && capital[j] <= w && profits[j] > best) { best = profits[j]; best_j = j; }
        }
        if (best_j < 0) break;
        w += best;
        used[best_j] = true;
    }
    return w;
}
int main() {
    assert(findMaximizedCapital(2, 0, {1, 2, 3}, {0, 1, 1}) == 4);
    assert(findMaximizedCapital(3, 0, {1, 2, 3}, {0, 1, 2}) == 6);
    assert(findMaximizedCapital(1, 0, {1, 2}, {1, 2}) == 0);
    assert(findMaximizedCapital(2, 1, {1, 2, 3}, {1, 1, 2}) == 6);
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''find_maximized_capital <- function(k, w, profits, capital) {
  n <- length(profits)
  used <- rep(FALSE, n)
  for (t in seq_len(k)) {
    best <- -1; best_j <- -1
    for (j in seq_len(n)) {
      if (!used[j] && capital[j] <= w && profits[j] > best) { best <- profits[j]; best_j <- j }
    }
    if (best_j < 0) break
    w <- w + best
    used[best_j] <- TRUE
  }
  w
}
stopifnot(find_maximized_capital(2, 0, c(1, 2, 3), c(0, 1, 1)) == 4)
stopifnot(find_maximized_capital(3, 0, c(1, 2, 3), c(0, 1, 2)) == 6)
stopifnot(find_maximized_capital(1, 0, c(1, 2), c(1, 2)) == 0)
stopifnot(find_maximized_capital(2, 1, c(1, 2, 3), c(1, 1, 2)) == 6)
cat("PASS\\n")
''',
"zig": '''const std = @import("std");
fn findMaximizedCapital(k: i32, w0: i64, profits: []const i64, capital: []const i64) i64 {
    var w = w0;
    var used = [_]bool{false} ** 64;
    var t: i32 = 0;
    while (t < k) : (t += 1) {
        var best: i64 = -1;
        var best_j: i64 = -1;
        for (profits, 0..) |p, j| {
            if (!used[j] and capital[j] <= w and p > best) { best = p; best_j = @intCast(j); }
        }
        if (best_j < 0) break;
        w += best;
        used[@intCast(best_j)] = true;
    }
    return w;
}
pub fn main() !void {
    if (findMaximizedCapital(2, 0, &[_]i64{ 1, 2, 3 }, &[_]i64{ 0, 1, 1 }) != 4) return error.TestFailed;
    if (findMaximizedCapital(3, 0, &[_]i64{ 1, 2, 3 }, &[_]i64{ 0, 1, 2 }) != 6) return error.TestFailed;
    if (findMaximizedCapital(1, 0, &[_]i64{ 1, 2 }, &[_]i64{ 1, 2 }) != 0) return error.TestFailed;
    if (findMaximizedCapital(2, 1, &[_]i64{ 1, 2, 3 }, &[_]i64{ 1, 1, 2 }) != 6) return error.TestFailed;
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''int findMaximizedCapital(int k, int w, List<int> profits, List<int> capital) {
  final n = profits.length;
  final used = List<bool>.filled(n, false);
  for (var t = 0; t < k; t++) {
    var best = -1;
    var bestJ = -1;
    for (var j = 0; j < n; j++) {
      if (!used[j] && capital[j] <= w && profits[j] > best) {
        best = profits[j];
        bestJ = j;
      }
    }
    if (bestJ < 0) break;
    w += best;
    used[bestJ] = true;
  }
  return w;
}
void main() {
  if (findMaximizedCapital(2, 0, [1, 2, 3], [0, 1, 1]) != 4) throw StateError('c1');
  if (findMaximizedCapital(3, 0, [1, 2, 3], [0, 1, 2]) != 6) throw StateError('c2');
  if (findMaximizedCapital(1, 0, [1, 2], [1, 2]) != 0) throw StateError('c3');
  if (findMaximizedCapital(2, 1, [1, 2, 3], [1, 1, 2]) != 6) throw StateError('c4');
  print('PASS');
}
''',
}

A451 = {
"rust": '''use std::collections::HashMap;
fn frequency_sort(s: &str) -> String {
    let mut counts: HashMap<char, i64> = HashMap::new();
    let mut first_idx: HashMap<char, usize> = HashMap::new();
    for (i, c) in s.chars().enumerate() {
        *counts.entry(c).or_insert(0) += 1;
        first_idx.entry(c).or_insert(i);
    }
    let mut items: Vec<(char, i64, usize)> = counts.iter().map(|(&c, &n)| (c, n, first_idx[&c])).collect();
    items.sort_by(|a, b| b.1.cmp(&a.1).then(a.2.cmp(&b.2)));
    items.iter().map(|&(c, n, _)| std::iter::repeat(c).take(n as usize).collect::<String>()).collect()
}
fn main() {
    assert_eq!(frequency_sort("tree"), "eetr");
    assert_eq!(frequency_sort(""), "");
    assert_eq!(frequency_sort("cccaaa"), "cccaaa");
    println!("PASS");
}
''',
"lua": '''local function frequency_sort(s)
    local counts, first = {}, {}
    for i = 1, #s do
        local c = s:sub(i, i)
        if counts[c] == nil then counts[c] = 0; first[c] = i end
        counts[c] = counts[c] + 1
    end
    local order = {}
    for c in pairs(counts) do order[#order + 1] = c end
    table.sort(order, function(a, b)
        if counts[a] ~= counts[b] then return counts[a] > counts[b] end
        return first[a] < first[b]
    end)
    local out = {}
    for _, c in ipairs(order) do
        out[#out + 1] = string.rep(c, counts[c])
    end
    return table.concat(out)
end
assert(frequency_sort("tree") == "eetr")
assert(frequency_sort("") == "")
assert(frequency_sort("cccaaa") == "cccaaa")
print("PASS")
''',
"c": '''#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef struct { char c; int cnt; int first; } FC;
static int cmp_fc(const void *a, const void *b) {
    const FC *x = a, *y = b;
    if (x->cnt != y->cnt) return y->cnt - x->cnt;
    return x->first - y->first;
}
static void frequency_sort(const char *s, char out[]) {
    FC fcs[256];
    int n = 0;
    int seen[256] = {0};
    for (const char *p = s; *p; p++) {
        unsigned char c = (unsigned char)*p;
        if (!seen[c]) { seen[c] = 1; fcs[n].c = c; fcs[n].cnt = 0; fcs[n].first = (int)(p - s); n++; }
        fcs[0].cnt += 0; // noop
        for (int k = 0; k < n; k++) if (fcs[k].c == c) { fcs[k].cnt++; break; }
    }
    qsort(fcs, n, sizeof(FC), cmp_fc);
    int pos = 0;
    for (int k = 0; k < n; k++)
        for (int j = 0; j < fcs[k].cnt; j++) out[pos++] = fcs[k].c;
    out[pos] = '\\0';
}
int main(void) {
    char out[4096];
    frequency_sort("tree", out);
    if (strcmp(out, "eetr") != 0) { printf("FAIL 1 %s\\n", out); return 1; }
    frequency_sort("", out);
    if (strcmp(out, "") != 0) { printf("FAIL 2\\n"); return 1; }
    frequency_sort("cccaaa", out);
    if (strcmp(out, "cccaaa") != 0) { printf("FAIL 3 %s\\n", out); return 1; }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''#include <algorithm>
#include <cassert>
#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>
static std::string frequencySort(const std::string &s) {
    std::unordered_map<char, long long> counts;
    std::unordered_map<char, size_t> firstIdx;
    for (size_t i = 0; i < s.size(); ++i) {
        ++counts[s[i]];
        firstIdx.emplace(s[i], i);
    }
    std::vector<std::pair<char, std::pair<long long, size_t>>> items;
    for (auto &[c, n] : counts) items.emplace_back(c, std::make_pair(n, firstIdx[c]));
    std::sort(items.begin(), items.end(), [](auto &a, auto &b) {
        if (a.second.first != b.second.first) return a.second.first > b.second.first;
        return a.second.second < b.second.second;
    });
    std::string res;
    for (auto &[c, p] : items) res.append(static_cast<size_t>(p.first), c);
    return res;
}
int main() {
    assert(frequencySort("tree") == "eetr");
    assert(frequencySort("") == "");
    assert(frequencySort("cccaaa") == "cccaaa");
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''frequency_sort <- function(s) {
  chars <- strsplit(s, "")[[1]]
  if (length(chars) == 0L) return("")
  counts <- table(chars)
  first_idx <- sapply(names(counts), function(c) match(c, chars))
  ord <- order(-as.integer(counts), first_idx)
  paste(vapply(ord, function(i) {
    strrep(names(counts)[i], counts[[i]])
  }, ""), collapse = "")
}
stopifnot(frequency_sort("tree") == "eetr")
stopifnot(frequency_sort("") == "")
stopifnot(frequency_sort("cccaaa") == "cccaaa")
cat("PASS\\n")
''',
"zig": '''const std = @import("std");
const FC = struct { c: u8, cnt: i32, first: usize };
fn frequencySort(s: []const u8, out: *std.ArrayList(u8)) void {
    var fcs: [256]FC = undefined;
    var seen = [_]bool{false} ** 256;
    var n: usize = 0;
    for (s, 0..) |c, i| {
        if (!seen[c]) {
            seen[c] = true;
            fcs[n] = .{ .c = c, .cnt = 0, .first = i };
            n += 1;
        }
        for (0..n) |k| {
            if (fcs[k].c == c) { fcs[k].cnt += 1; break; }
        }
    }
    const S = struct {
        fn lt(_: void, a: FC, b: FC) bool {
            if (a.cnt != b.cnt) return a.cnt > b.cnt;
            return a.first < b.first;
        }
    };
    std.sort.pdq(FC, fcs[0..n], {}, S.lt);
    for (0..n) |k| {
        for (0..@intCast(fcs[k].cnt)) |_| out.append(fcs[k].c) catch unreachable;
    }
}
pub fn main() !void {
    var out = std.ArrayList(u8).init(std.heap.page_allocator);
    defer out.deinit();
    frequencySort("tree", &out);
    if (!std.mem.eql(u8, out.items, "eetr")) return error.TestFailed;
    out.clearRetainingCapacity();
    frequencySort("", &out);
    if (out.items.len != 0) return error.TestFailed;
    out.clearRetainingCapacity();
    frequencySort("cccaaa", &out);
    if (!std.mem.eql(u8, out.items, "cccaaa")) return error.TestFailed;
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''String frequencySort(String s) {
  if (s.isEmpty) return '';
  final counts = <String, int>{};
  final firstIdx = <String, int>{};
  for (var i = 0; i < s.length; i++) {
    final c = s[i];
    counts[c] = (counts[c] ?? 0) + 1;
    firstIdx.putIfAbsent(c, () => i);
  }
  final keys = counts.keys.toList()
    ..sort((a, b) {
      if (counts[a] != counts[b]) return counts[b]!.compareTo(counts[a]!);
      return firstIdx[a]!.compareTo(firstIdx[b]!);
    });
  final sb = StringBuffer();
  for (final c in keys) {
    sb.write(c * counts[c]!);
  }
  return sb.toString();
}
void main() {
  if (frequencySort('tree') != 'eetr') throw StateError('c1');
  if (frequencySort('') != '') throw StateError('c2');
  if (frequencySort('cccaaa') != 'cccaaa') throw StateError('c3');
  print('PASS');
}
''',
}

PROBS = [
    ("lc_208_实现_trie_(前缀树)", A208, "LeetCode 208. 实现 Trie (前缀树)"),
    ("lc_313_超级丑数", A313, "LeetCode 313. 超级丑数"),
    ("lc_502_ipo", A502, "LeetCode 502. IPO"),
    ("lc_451_根据字符出现频率排序", A451, "LeetCode 451. 根据字符出现频率排序"),
]
count = 0
for prob, algo, title in PROBS:
    bid = B[prob.split("_")[1]]
    ts_dir = f"/Users/Wang/Code/webfault-ai/dsa/ts/heap/{prob}"
    sols = sorted(f[:-3] for f in os.listdir(ts_dir) if f.startswith("solution_") and f.endswith(".ts"))
    for lang in EXT:
        ext = EXT[lang]
        for sol in sols:
            n = sol.replace("solution_", "").split("_")[0]
            head = head_comment(lang, bid, f"{title} — {LANGNAME[lang]} 版（方案{n}）")
            emit(lang, f"heap/{prob}/{sol}.{ext}", head + "\n" + algo[lang])
            count += 1
print(f"emitted {count} files")
