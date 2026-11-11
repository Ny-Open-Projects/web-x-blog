#!/usr/bin/env python3
# gen_notes3.py — notes 第三批：结构化笔记题（顺序查找/栈排序/LRU/最小堆/最大堆/BFS/DFS/顺序查找等）× 7语言
import sys, os; sys.path.insert(0, "/Users/Wang/Code/webfault-ai/dsa/_tools")
from langlib import emit, head_comment, EXT

LANGNAME = {"rust": "Rust", "lua": "Lua", "c": "C", "cpp": "C++", "r": "R", "zig": "Zig", "dart": "Dart"}

SEQSEARCH = {
"rust":'''fn seq_search(arr: &[i32], key: i32) -> i32 {
    for (i, &v) in arr.iter().enumerate() {
        if v == key { return i as i32; }
    }
    -1
}
fn main() {
    assert_eq!(seq_search(&[1,2,3], 1), 0);
    assert_eq!(seq_search(&[1,2,3], 2), 1);
    assert_eq!(seq_search(&[1,2,3], 3), 2);
    assert_eq!(seq_search(&[1,2,3], 4), -1);
    println!("PASS"); }''',
"lua":'''local function seq_search(arr, key)
    for i, v in ipairs(arr) do
        if v == key then return i - 1 end
    end
    return -1
end
assert(seq_search({1,2,3}, 1) == 0)
assert(seq_search({1,2,3}, 2) == 1)
assert(seq_search({1,2,3}, 3) == 2)
assert(seq_search({1,2,3}, 4) == -1)
print("PASS")''',
"c":'''#include <stdio.h>
static int seq_search(const int *arr, int n, int key) {
    for (int i = 0; i < n; i++) if (arr[i] == key) return i;
    return -1;
}
int main(void) {
    int a[] = {1,2,3};
    if (seq_search(a, 3, 1) != 0) { printf("FAIL 1\\n"); return 1; }
    if (seq_search(a, 3, 2) != 1) { printf("FAIL 2\\n"); return 1; }
    if (seq_search(a, 3, 4) != -1) { printf("FAIL 3\\n"); return 1; }
    printf("PASS\\n"); return 0; }''',
"cpp":'''#include <cassert>
#include <iostream>
#include <vector>
static int seqSearch(const std::vector<int> &arr, int key) {
    for (size_t i = 0; i < arr.size(); ++i) if (arr[i] == key) return static_cast<int>(i);
    return -1;
}
int main() {
    assert(seqSearch({1,2,3}, 1) == 0);
    assert(seqSearch({1,2,3}, 2) == 1);
    assert(seqSearch({1,2,3}, 4) == -1);
    std::cout << "PASS" << std::endl; }''',
"r":'''seq_search <- function(arr, key) {
  w <- which(arr == key)
  if (length(w) == 0) -1L else as.integer(w[1] - 1L)
}
stopifnot(seq_search(c(1, 2, 3), 1) == 0)
stopifnot(seq_search(c(1, 2, 3), 2) == 1)
stopifnot(seq_search(c(1, 2, 3), 4) == -1)
cat("PASS\\n")''',
"zig":'''const std = @import("std");
fn seqSearch(arr: []const i32, key: i32) i32 {
    for (arr, 0..) |v, i| {
        if (v == key) return @intCast(i);
    }
    return -1;
}
pub fn main() !void {
    const a = [_]i32{ 1, 2, 3 };
    if (seqSearch(&a, 1) != 0) return error.TestFailed;
    if (seqSearch(&a, 2) != 1) return error.TestFailed;
    if (seqSearch(&a, 4) != -1) return error.TestFailed;
    std.debug.print("PASS\\n", .{}); }''',
"dart":'''int seqSearch(List<int> arr, int key) {
  for (var i = 0; i < arr.length; i++) {
    if (arr[i] == key) return i;
  }
  return -1;
}
void main() {
  if (seqSearch([1, 2, 3], 1) != 0) throw StateError('c1');
  if (seqSearch([1, 2, 3], 2) != 1) throw StateError('c2');
  if (seqSearch([1, 2, 3], 4) != -1) throw StateError('c3');
  print('PASS'); }''',
}

STKSORT = {
"rust":'''fn stack_sort(input: &[i32]) -> Vec<i32> {
    let mut st: Vec<i32> = Vec::new();
    for &v in input { st.push(v); }
    let mut out = Vec::new();
    while let Some(v) = st.pop() { out.push(v); }
    out
}
fn main() {
    assert_eq!(stack_sort(&[3,1,5,2,4]), vec![4,2,5,1,3]);
    println!("PASS"); }''',
"lua":'''local function stack_sort(input)
    local st = {}
    for _, v in ipairs(input) do st[#st + 1] = v end
    local out = {}
    while #st > 0 do out[#out + 1] = table.remove(st) end
    return out
end
assert(table.concat(stack_sort({3,1,5,2,4}), ",") == "4,2,5,1,3")
print("PASS")''',
"c":'''#include <stdio.h>
static void stack_sort(const int *in, int n, int out[]) {
    int st[4096];
    int top = 0;
    for (int i = 0; i < n; i++) st[top++] = in[i];
    for (int i = 0; i < n; i++) out[i] = st[--top];
}
int main(void) {
    int out[64];
    stack_sort((int[]){3,1,5,2,4}, 5, out);
    int w[] = {4,2,5,1,3};
    for (int i = 0; i < 5; i++) if (out[i] != w[i]) { printf("FAIL\\n"); return 1; }
    printf("PASS\\n"); return 0; }''',
"cpp":'''#include <cassert>
#include <iostream>
#include <vector>
static std::vector<int> stackSort(const std::vector<int> &input) {
    std::vector<int> st;
    for (int v : input) st.push_back(v);
    std::vector<int> out;
    while (!st.empty()) { out.push_back(st.back()); st.pop_back(); }
    return out;
}
int main() {
    assert((stackSort({3,1,5,2,4}) == std::vector<int>{4,2,5,1,3}));
    std::cout << "PASS" << std::endl; }''',
"r":'''stack_sort <- function(input) as.integer(rev(input))
stopifnot(identical(stack_sort(c(3, 1, 5, 2, 4)), c(4L, 2L, 5L, 1L, 3L)))
cat("PASS\\n")''',
"zig":'''const std = @import("std");
fn stackSort(input: []const i32, out: []i32) void {
    var st: [4096]i32 = undefined;
    var top: usize = 0;
    for (input) |v| {
        st[top] = v;
        top += 1;
    }
    for (0..input.len) |i| {
        top -= 1;
        out[i] = st[top];
    }
}
pub fn main() !void {
    var out: [8]i32 = undefined;
    stackSort(&[_]i32{ 3, 1, 5, 2, 4 }, &out);
    const want = [_]i32{ 4, 2, 5, 1, 3 };
    for (want, 0..) |w, i| if (out[i] != w) return error.TestFailed;
    std.debug.print("PASS\\n", .{}); }''',
"dart":'''List<int> stackSort(List<int> input) {
  final st = <int>[];
  for (final v in input) { st.add(v); }
  final out = <int>[];
  while (st.isNotEmpty) { out.add(st.removeLast()); }
  return out;
}
void main() { if (stackSort([3,1,5,2,4]).toString() != '[4, 2, 5, 1, 3]') throw StateError('c1'); print('PASS'); }''',
}

MINHEAP = {
"rust":'''fn min_heap_pop_all(input: &[i32]) -> Vec<i32> {
    let mut h: Vec<i32> = Vec::new();
    for &v in input {
        h.push(v);
        let mut i = h.len() - 1;
        while i > 0 {
            let p = (i - 1) / 2;
            if h[p] <= h[i] { break; }
            h.swap(p, i);
            i = p;
        }
    }
    let mut out = Vec::new();
    while !h.is_empty() {
        out.push(h[0]);
        let last = h.pop().unwrap();
        if !h.is_empty() {
            h[0] = last;
            let mut i = 0usize;
            loop {
                let (l, r) = (2 * i + 1, 2 * i + 2);
                let mut m = i;
                if l < h.len() && h[l] < h[m] { m = l; }
                if r < h.len() && h[r] < h[m] { m = r; }
                if m == i { break; }
                h.swap(i, m);
                i = m;
            }
        }
    }
    out
}
fn main() {
    assert_eq!(min_heap_pop_all(&[3,1,6,5,2,4]), vec![1,2,3,4,5,6]);
    println!("PASS"); }''',
"lua":'''local function min_heap_pop_all(input)
    local h = {}
    local function up(i)
        while i > 1 do
            local p = i // 2
            if h[p] <= h[i] then break end
            h[p], h[i] = h[i], h[p]
            i = p
        end
    end
    local function down(i)
        local n = #h
        while true do
            local l, r, m = 2 * i, 2 * i + 1, i
            if l <= n and h[l] < h[m] then m = l end
            if r <= n and h[r] < h[m] then m = r end
            if m == i then break end
            h[i], h[m] = h[m], h[i]
            i = m
        end
    end
    for _, v in ipairs(input) do
        h[#h + 1] = v
        up(#h)
    end
    local out = {}
    while #h > 0 do
        out[#out + 1] = h[1]
        local last = table.remove(h)
        if #h > 0 then
            h[1] = last
            down(1)
        end
    end
    return out
end
assert(table.concat(min_heap_pop_all({3,1,6,5,2,4}), ",") == "1,2,3,4,5,6")
print("PASS")''',
"c":'''#include <stdio.h>
static void up(int *h, int i) {
    while (i > 0) {
        int p = (i - 1) / 2;
        if (h[p] <= h[i]) break;
        int t = h[p]; h[p] = h[i]; h[i] = t;
        i = p;
    }
}
static void down(int *h, int n, int i) {
    while (1) {
        int l = 2 * i + 1, r = 2 * i + 2, m = i;
        if (l < n && h[l] < h[m]) m = l;
        if (r < n && h[r] < h[m]) m = r;
        if (m == i) break;
        int t = h[i]; h[i] = h[m]; h[m] = t;
        i = m;
    }
}
static void min_heap_pop_all(const int *in, int n, int out[]) {
    int h[4096];
    int hn = 0;
    for (int i = 0; i < n; i++) { h[hn++] = in[i]; up(h, hn - 1); }
    int on = 0;
    while (hn > 0) {
        out[on++] = h[0];
        int last = h[--hn];
        if (hn > 0) { h[0] = last; down(h, hn, 0); }
    }
}
int main(void) {
    int out[64];
    min_heap_pop_all((int[]){3,1,6,5,2,4}, 6, out);
    for (int i = 0; i < 6; i++) if (out[i] != i + 1) { printf("FAIL\\n"); return 1; }
    printf("PASS\\n"); return 0; }''',
"cpp":'''#include <cassert>
#include <iostream>
#include <vector>
static std::vector<int> minHeapPopAll(const std::vector<int> &input) {
    std::vector<int> h;
    auto up = [&](size_t i) {
        while (i > 0) {
            size_t p = (i - 1) / 2;
            if (h[p] <= h[i]) break;
            std::swap(h[p], h[i]);
            i = p;
        }
    };
    auto down = [&](size_t i) {
        size_t n = h.size();
        while (true) {
            size_t l = 2 * i + 1, r = 2 * i + 2, m = i;
            if (l < n && h[l] < h[m]) m = l;
            if (r < n && h[r] < h[m]) m = r;
            if (m == i) break;
            std::swap(h[i], h[m]);
            i = m;
        }
    };
    for (int v : input) {
        h.push_back(v);
        up(h.size() - 1);
    }
    std::vector<int> out;
    while (!h.empty()) {
        out.push_back(h[0]);
        int last = h.back();
        h.pop_back();
        if (!h.empty()) { h[0] = last; down(0); }
    }
    return out;
}
int main() {
    assert((minHeapPopAll({3,1,6,5,2,4}) == std::vector<int>{1,2,3,4,5,6}));
    std::cout << "PASS" << std::endl; }''',
"r":'''min_heap_pop_all <- function(input) sort(as.integer(input))
stopifnot(identical(min_heap_pop_all(c(3, 1, 6, 5, 2, 4)), 1:6))
cat("PASS\\n")''',
"zig":'''const std = @import("std");
fn minHeapPopAll(input: []const i32, out: *std.ArrayList(i32)) void {
    var h: [4096]i32 = undefined;
    var hn: usize = 0;
    for (input) |v| {
        h[hn] = v;
        var i = hn;
        hn += 1;
        while (i > 0) {
            const p = (i - 1) / 2;
            if (h[p] <= h[i]) break;
            const t = h[p];
            h[p] = h[i];
            h[i] = t;
            i = p;
        }
    }
    while (hn > 0) {
        out.append(h[0]) catch unreachable;
        hn -= 1;
        const last = h[hn];
        if (hn > 0) {
            h[0] = last;
            var i: usize = 0;
            while (true) {
                const l = 2 * i + 1;
                const r = 2 * i + 2;
                var m = i;
                if (l < hn and h[l] < h[m]) m = l;
                if (r < hn and h[r] < h[m]) m = r;
                if (m == i) break;
                const t = h[i];
                h[i] = h[m];
                h[m] = t;
                i = m;
            }
        }
    }
}
pub fn main() !void {
    var out = std.ArrayList(i32).init(std.heap.page_allocator);
    defer out.deinit();
    minHeapPopAll(&[_]i32{ 3, 1, 6, 5, 2, 4 }, &out);
    for (out.items, 0..) |v, i| if (v != @as(i32, @intCast(i + 1))) return error.TestFailed;
    std.debug.print("PASS\\n", .{}); }''',
"dart":'''List<int> minHeapPopAll(List<int> input) {
  final h = <int>[];
  void up(int i) {
    while (i > 0) {
      final p = (i - 1) ~/ 2;
      if (h[p] <= h[i]) break;
      final t = h[p];
      h[p] = h[i];
      h[i] = t;
      i = p;
    }
  }
  void down(int i) {
    final n = h.length;
    while (true) {
      final l = 2 * i + 1, r = 2 * i + 2;
      var m = i;
      if (l < n && h[l] < h[m]) m = l;
      if (r < n && h[r] < h[m]) m = r;
      if (m == i) break;
      final t = h[i];
      h[i] = h[m];
      h[m] = t;
      i = m;
    }
  }
  for (final v in input) {
    h.add(v);
    up(h.length - 1);
  }
  final out = <int>[];
  while (h.isNotEmpty) {
    out.add(h[0]);
    final last = h.removeLast();
    if (h.isNotEmpty) { h[0] = last; down(0); }
  }
  return out;
}
void main() { if (minHeapPopAll([3,1,6,5,2,4]).toString() != '[1, 2, 3, 4, 5, 6]') throw StateError('c1'); print('PASS'); }''',
}

MAXHEAP = {
"rust":'''fn max_heap_pop_all(input: &[i32]) -> Vec<i32> {
    let mut h: Vec<i32> = Vec::new();
    for &v in input {
        h.push(v);
        let mut i = h.len() - 1;
        while i > 0 {
            let p = (i - 1) / 2;
            if h[p] >= h[i] { break; }
            h.swap(p, i);
            i = p;
        }
    }
    let mut out = Vec::new();
    while !h.is_empty() {
        out.push(h[0]);
        let last = h.pop().unwrap();
        if !h.is_empty() {
            h[0] = last;
            let mut i = 0usize;
            loop {
                let (l, r) = (2 * i + 1, 2 * i + 2);
                let mut m = i;
                if l < h.len() && h[l] > h[m] { m = l; }
                if r < h.len() && h[r] > h[m] { m = r; }
                if m == i { break; }
                h.swap(i, m);
                i = m;
            }
        }
    }
    out
}
fn main() {
    assert_eq!(max_heap_pop_all(&[3,1,6,5,2,4]), vec![6,5,4,3,2,1]);
    println!("PASS"); }''',
"lua":'''local function max_heap_pop_all(input)
    local h = {}
    local function up(i)
        while i > 1 do
            local p = i // 2
            if h[p] >= h[i] then break end
            h[p], h[i] = h[i], h[p]
            i = p
        end
    end
    local function down(i)
        local n = #h
        while true do
            local l, r, m = 2 * i, 2 * i + 1, i
            if l <= n and h[l] > h[m] then m = l end
            if r <= n and h[r] > h[m] then m = r end
            if m == i then break end
            h[i], h[m] = h[m], h[i]
            i = m
        end
    end
    for _, v in ipairs(input) do
        h[#h + 1] = v
        up(#h)
    end
    local out = {}
    while #h > 0 do
        out[#out + 1] = h[1]
        local last = table.remove(h)
        if #h > 0 then
            h[1] = last
            down(1)
        end
    end
    return out
end
assert(table.concat(max_heap_pop_all({3,1,6,5,2,4}), ",") == "6,5,4,3,2,1")
print("PASS")''',
"c":'''#include <stdio.h>
static void up_max(int *h, int i) {
    while (i > 0) {
        int p = (i - 1) / 2;
        if (h[p] >= h[i]) break;
        int t = h[p]; h[p] = h[i]; h[i] = t;
        i = p;
    }
}
static void down_max(int *h, int n, int i) {
    while (1) {
        int l = 2 * i + 1, r = 2 * i + 2, m = i;
        if (l < n && h[l] > h[m]) m = l;
        if (r < n && h[r] > h[m]) m = r;
        if (m == i) break;
        int t = h[i]; h[i] = h[m]; h[m] = t;
        i = m;
    }
}
static void max_heap_pop_all(const int *in, int n, int out[]) {
    int h[4096];
    int hn = 0;
    for (int i = 0; i < n; i++) { h[hn++] = in[i]; up_max(h, hn - 1); }
    int on = 0;
    while (hn > 0) {
        out[on++] = h[0];
        int last = h[--hn];
        if (hn > 0) { h[0] = last; down_max(h, hn, 0); }
    }
}
int main(void) {
    int out[64];
    max_heap_pop_all((int[]){3,1,6,5,2,4}, 6, out);
    for (int i = 0; i < 6; i++) if (out[i] != 6 - i) { printf("FAIL\\n"); return 1; }
    printf("PASS\\n"); return 0; }''',
"cpp":'''#include <cassert>
#include <iostream>
#include <vector>
static std::vector<int> maxHeapPopAll(const std::vector<int> &input) {
    std::vector<int> h;
    auto up = [&](size_t i) {
        while (i > 0) {
            size_t p = (i - 1) / 2;
            if (h[p] >= h[i]) break;
            std::swap(h[p], h[i]);
            i = p;
        }
    };
    auto down = [&](size_t i) {
        size_t n = h.size();
        while (true) {
            size_t l = 2 * i + 1, r = 2 * i + 2, m = i;
            if (l < n && h[l] > h[m]) m = l;
            if (r < n && h[r] > h[m]) m = r;
            if (m == i) break;
            std::swap(h[i], h[m]);
            i = m;
        }
    };
    for (int v : input) {
        h.push_back(v);
        up(h.size() - 1);
    }
    std::vector<int> out;
    while (!h.empty()) {
        out.push_back(h[0]);
        int last = h.back();
        h.pop_back();
        if (!h.empty()) { h[0] = last; down(0); }
    }
    return out;
}
int main() {
    assert((maxHeapPopAll({3,1,6,5,2,4}) == std::vector<int>{6,5,4,3,2,1}));
    std::cout << "PASS" << std::endl; }''',
"r":'''max_heap_pop_all <- function(input) sort(as.integer(input), decreasing = TRUE)
stopifnot(identical(max_heap_pop_all(c(3, 1, 6, 5, 2, 4)), c(6L, 5L, 4L, 3L, 2L, 1L)))
cat("PASS\\n")''',
"zig":'''const std = @import("std");
fn maxHeapPopAll(input: []const i32, out: *std.ArrayList(i32)) void {
    var h: [4096]i32 = undefined;
    var hn: usize = 0;
    for (input) |v| {
        h[hn] = v;
        var i = hn;
        hn += 1;
        while (i > 0) {
            const p = (i - 1) / 2;
            if (h[p] >= h[i]) break;
            const t = h[p];
            h[p] = h[i];
            h[i] = t;
            i = p;
        }
    }
    while (hn > 0) {
        out.append(h[0]) catch unreachable;
        hn -= 1;
        const last = h[hn];
        if (hn > 0) {
            h[0] = last;
            var i: usize = 0;
            while (true) {
                const l = 2 * i + 1;
                const r = 2 * i + 2;
                var m = i;
                if (l < hn and h[l] > h[m]) m = l;
                if (r < hn and h[r] > h[m]) m = r;
                if (m == i) break;
                const t = h[i];
                h[i] = h[m];
                h[m] = t;
                i = m;
            }
        }
    }
}
pub fn main() !void {
    var out = std.ArrayList(i32).init(std.heap.page_allocator);
    defer out.deinit();
    maxHeapPopAll(&[_]i32{ 3, 1, 6, 5, 2, 4 }, &out);
    for (out.items, 0..) |v, i| if (v != @as(i32, @intCast(6 - i))) return error.TestFailed;
    std.debug.print("PASS\\n", .{}); }''',
"dart":'''List<int> maxHeapPopAll(List<int> input) {
  final h = <int>[];
  void up(int i) {
    while (i > 0) {
      final p = (i - 1) ~/ 2;
      if (h[p] >= h[i]) break;
      final t = h[p];
      h[p] = h[i];
      h[i] = t;
      i = p;
    }
  }
  void down(int i) {
    final n = h.length;
    while (true) {
      final l = 2 * i + 1, r = 2 * i + 2;
      var m = i;
      if (l < n && h[l] > h[m]) m = l;
      if (r < n && h[r] > h[m]) m = r;
      if (m == i) break;
      final t = h[i];
      h[i] = h[m];
      h[m] = t;
      i = m;
    }
  }
  for (final v in input) {
    h.add(v);
    up(h.length - 1);
  }
  final out = <int>[];
  while (h.isNotEmpty) {
    out.add(h[0]);
    final last = h.removeLast();
    if (h.isNotEmpty) { h[0] = last; down(0); }
  }
  return out;
}
void main() { if (maxHeapPopAll([3,1,6,5,2,4]).toString() != '[6, 5, 4, 3, 2, 1]') throw StateError('c1'); print('PASS'); }''',
}

BFS = {
"rust":'''fn bfs_order(graph: &[Vec<i32>], start: usize) -> Vec<i32> {
    let n = graph.len();
    let mut visited = vec![false; n];
    let mut order = Vec::new();
    let mut queue = std::collections::VecDeque::new();
    visited[start] = true;
    queue.push_back(start);
    while let Some(c) = queue.pop_front() {
        order.push(c as i32);
        for &nx in &graph[c] {
            if !visited[nx as usize] {
                visited[nx as usize] = true;
                queue.push_back(nx as usize);
            }
        }
    }
    order
}
fn main() {
    // 6节点图: 0-1,0-2,1-3,1-4,2-5
    let g = vec![vec![1,2],vec![3,4],vec![5],vec![],vec![],vec![]];
    assert_eq!(bfs_order(&g, 0), vec![0,1,2,3,4,5]);
    println!("PASS"); }''',
"lua":'''local function bfs_order(graph, start)
    local n = #graph
    local visited = {}
    local order = {}
    local queue = {start}
    local head = 1
    visited[start + 1] = true
    while head <= #queue do
        local c = queue[head]
        head = head + 1
        order[#order + 1] = c
        for _, nx in ipairs(graph[c + 1] or {}) do
            if not visited[nx + 1] then
                visited[nx + 1] = true
                queue[#queue + 1] = nx
            end
        end
    end
    return order
end
local g = {{1,2},{3,4},{5},{},{},{}}
assert(table.concat(bfs_order(g, 0), ",") == "0,1,2,3,4,5")
print("PASS")''',
"c":'''#include <stdio.h>
static void bfs_order(const int graph[][8], const int gsize[], int n, int start, int out[]) {
    int visited[64] = {0};
    int queue[64];
    int head = 0, tail = 0, on = 0;
    visited[start] = 1;
    queue[tail++] = start;
    while (head < tail) {
        int c = queue[head++];
        out[on++] = c;
        for (int i = 0; i < gsize[c]; i++) {
            int nx = graph[c][i];
            if (!visited[nx]) {
                visited[nx] = 1;
                queue[tail++] = nx;
            }
        }
    }
}
int main(void) {
    int graph[6][8] = {{1,2},{3,4},{5},{},{},{}};
    int gsize[6] = {2,2,1,0,0,0};
    int out[64];
    bfs_order(graph, gsize, 6, 0, out);
    for (int i = 0; i < 6; i++) if (out[i] != i) { printf("FAIL\\n"); return 1; }
    printf("PASS\\n"); return 0; }''',
"cpp":'''#include <cassert>
#include <iostream>
#include <queue>
#include <vector>
static std::vector<int> bfsOrder(const std::vector<std::vector<int>> &graph, int start) {
    size_t n = graph.size();
    std::vector<bool> visited(n, false);
    std::vector<int> order;
    std::queue<int> q;
    visited[start] = true;
    q.push(start);
    while (!q.empty()) {
        int c = q.front();
        q.pop();
        order.push_back(c);
        for (int nx : graph[c]) {
            if (!visited[nx]) {
                visited[nx] = true;
                q.push(nx);
            }
        }
    }
    return order;
}
int main() {
    std::vector<std::vector<int>> g = {{1,2},{3,4},{5},{},{},{}};
    assert((bfsOrder(g, 0) == std::vector<int>{0,1,2,3,4,5}));
    std::cout << "PASS" << std::endl; }''',
"r":'''bfs_order <- function(graph, start) {
  n <- length(graph)
  visited <- rep(FALSE, 100L)  # 预分配足够大
  order_ <- integer(0)
  queue <- start + 1L
  head <- 1L
  visited[start + 1L] <- TRUE
  while (head <= length(queue)) {
    c <- queue[head]
    head <- head + 1L
    order_ <- c(order_, c - 1L)
    nb <- if (c <= length(graph) && !is.null(graph[[c]])) graph[[c]] else integer(0)
    if (length(nb) > 0) {
      for (nx in nb) {
        if (!visited[nx]) {
          visited[nx] <- TRUE
          queue <- c(queue, nx)
        }
      }
    }
  }
  order_
}
g <- list(c(2, 3), c(4, 5), c(6), NULL, NULL, NULL)
stopifnot(identical(as.integer(bfs_order(g, 0)), 0:5))
cat("PASS\\n")''',
"zig":'''const std = @import("std");
fn bfsOrder(graph: []const []const i32, start: usize, out: *std.ArrayList(i32)) void {
    const n = graph.len;
    var visited: [64]bool = undefined;
    for (0..n) |i| visited[i] = false;
    var queue: [64]usize = undefined;
    var head: usize = 0;
    var tail: usize = 0;
    visited[start] = true;
    queue[tail] = start;
    tail += 1;
    while (head < tail) {
        const c = queue[head];
        head += 1;
        out.append(@intCast(c)) catch unreachable;
        for (graph[c]) |nx| {
            const u: usize = @intCast(nx);
            if (!visited[u]) {
                visited[u] = true;
                queue[tail] = u;
                tail += 1;
            }
        }
    }
}
pub fn main() !void {
    var out = std.ArrayList(i32).init(std.heap.page_allocator);
    defer out.deinit();
    const g0 = [_]i32{ 1, 2 };
    const g1 = [_]i32{ 3, 4 };
    const g2 = [_]i32{5};
    const g3 = [_]i32{};
    const g4 = [_]i32{};
    const g5 = [_]i32{};
    const g = [_][]const i32{ &g0, &g1, &g2, &g3, &g4, &g5 };
    bfsOrder(&g, 0, &out);
    for (out.items, 0..) |v, i| if (v != @as(i32, @intCast(i))) return error.TestFailed;
    std.debug.print("PASS\\n", .{}); }''',
"dart":'''List<int> bfsOrder(List<List<int>> graph, int start) {
  final n = graph.length;
  final visited = List<bool>.filled(n, false);
  final order = <int>[];
  final queue = <int>[start];
  var head = 0;
  visited[start] = true;
  while (head < queue.length) {
    final c = queue[head++];
    order.add(c);
    for (final nx in graph[c]) {
      if (!visited[nx]) {
        visited[nx] = true;
        queue.add(nx);
      }
    }
  }
  return order;
}
void main() {
  final g = <List<int>>[
    <int>[1, 2],
    <int>[3, 4],
    <int>[5],
    <int>[],
    <int>[],
    <int>[]
  ];
  if (bfsOrder(g, 0).toString() != '[0, 1, 2, 3, 4, 5]') throw StateError('c1');
  print('PASS'); }''',
}

PROBS = [
    ("lc_134217002_顺序查找", SEQSEARCH, "134217002", "数据结构与算法之查找: 顺序查找"),
    ("lc_105893757_栈排序分析", STKSORT, "105893757", "栈排序分析"),
    ("lc_133468244_堆和实现最小堆类", MINHEAP, "133468244", "数据结构与算法之堆: 堆和实现最小堆类"),
    ("lc_133530983_实现最大堆类的两种方式及实现堆排序", MAXHEAP, "133530983", "数据结构与算法之堆: 实现最大堆类及堆排序"),
    ("lc_113548046_图搜索之bfs详解", BFS, "113548046", "图搜索之BFS详解"),
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
