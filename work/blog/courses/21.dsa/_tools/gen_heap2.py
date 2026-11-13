#!/usr/bin/env python3
# gen_heap2.py — heap 收官：lc_215(4算法)/lc_347/lc_295/lc_23(2算法) × 7语言
import sys, os; sys.path.insert(0, "/Users/Wang/Code/github/web-x-blog/work/blog/courses/21.dsa/_tools")
from langlib import emit, head_comment, EXT

B = {"215": "133471440", "347": "133493400", "295": "135749595", "23": "134283831"}
LANGNAME = {"rust": "Rust", "lua": "Lua", "c": "C", "cpp": "C++", "r": "R", "zig": "Zig", "dart": "Dart"}

# ============ lc_215：sort / heap / bubble / quickselect ============
A215 = {}
A215["sort"] = {
"rust": '''fn find_kth_largest(nums: Vec<i32>, k: i32) -> i32 {
    let mut a = nums;
    a.sort_unstable_by(|x, y| y.cmp(x));
    a[(k - 1) as usize]
}
fn main() {
    assert_eq!(find_kth_largest(vec![3, 2, 1, 5, 6, 4], 2), 5);
    assert_eq!(find_kth_largest(vec![3, 2, 3, 1, 2, 4, 5, 5, 6], 4), 4);
    assert_eq!(find_kth_largest(vec![1], 1), 1);
    println!("PASS");
}
''',
"lua": '''local function find_kth_largest(nums, k)
    local a = {table.unpack(nums)}
    table.sort(a, function(x, y) return x > y end)
    return a[k]
end
assert(find_kth_largest({3, 2, 1, 5, 6, 4}, 2) == 5)
assert(find_kth_largest({3, 2, 3, 1, 2, 4, 5, 5, 6}, 4) == 4)
assert(find_kth_largest({1}, 1) == 1)
print("PASS")
''',
"c": '''#include <stdio.h>
#include <stdlib.h>
static int cmp_desc(const void *a, const void *b) { return *(const int *)b - *(const int *)a; }
static int find_kth_largest(const int *nums, int n, int k) {
    int *a = malloc(sizeof(int) * n);
    for (int i = 0; i < n; i++) a[i] = nums[i];
    qsort(a, n, sizeof(int), cmp_desc);
    int r = a[k - 1];
    free(a);
    return r;
}
int main(void) {
    if (find_kth_largest((int[]){3,2,1,5,6,4}, 6, 2) != 5) { printf("FAIL 1\\n"); return 1; }
    if (find_kth_largest((int[]){3,2,3,1,2,4,5,5,6}, 9, 4) != 4) { printf("FAIL 2\\n"); return 1; }
    if (find_kth_largest((int[]){1}, 1, 1) != 1) { printf("FAIL 3\\n"); return 1; }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''#include <algorithm>
#include <cassert>
#include <iostream>
#include <vector>
static int findKthLargest(std::vector<int> nums, int k) {
    std::sort(nums.begin(), nums.end(), std::greater<int>());
    return nums[k - 1];
}
int main() {
    assert(findKthLargest({3, 2, 1, 5, 6, 4}, 2) == 5);
    assert(findKthLargest({3, 2, 3, 1, 2, 4, 5, 5, 6}, 4) == 4);
    assert(findKthLargest({1}, 1) == 1);
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''find_kth_largest <- function(nums, k) {
  sort(nums, decreasing = TRUE)[k]
}
stopifnot(find_kth_largest(c(3, 2, 1, 5, 6, 4), 2) == 5)
stopifnot(find_kth_largest(c(3, 2, 3, 1, 2, 4, 5, 5, 6), 4) == 4)
stopifnot(find_kth_largest(c(1), 1) == 1)
cat("PASS\\n")
''',
"zig": '''const std = @import("std");
fn findKthLargest(nums: []const i32, k: usize, alloc: std.mem.Allocator) i32 {
    const a = alloc.dupe(i32, nums) catch unreachable;
    const S = struct {
        fn lt(_: void, x: i32, y: i32) bool { return x > y; }
    };
    std.sort.pdq(i32, a, {}, S.lt);
    return a[k - 1];
}
pub fn main() !void {
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();
    if (findKthLargest(&[_]i32{ 3, 2, 1, 5, 6, 4 }, 2, arena.allocator()) != 5) return error.TestFailed;
    if (findKthLargest(&[_]i32{ 3, 2, 3, 1, 2, 4, 5, 5, 6 }, 4, arena.allocator()) != 4) return error.TestFailed;
    if (findKthLargest(&[_]i32{1}, 1, arena.allocator()) != 1) return error.TestFailed;
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''int findKthLargest(List<int> nums, int k) {
  final a = List<int>.from(nums)..sort((x, y) => y.compareTo(x));
  return a[k - 1];
}
void main() {
  if (findKthLargest([3, 2, 1, 5, 6, 4], 2) != 5) throw StateError('c1');
  if (findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) != 4) throw StateError('c2');
  if (findKthLargest([1], 1) != 1) throw StateError('c3');
  print('PASS');
}
''',
}

A215["bubble"] = {
"rust": '''fn find_kth_largest(nums: Vec<i32>, k: i32) -> i32 {
    let mut a = nums;
    let n = a.len();
    let length = n - 1;
    let mut i = length;
    while i > length - (k as usize) && i > 0 {
        for j in 0..i {
            if a[j] > a[j + 1] { a.swap(j, j + 1); }
        }
        i -= 1;
    }
    a[length - (k as usize) + 1]
}
fn main() {
    assert_eq!(find_kth_largest(vec![3, 2, 1, 5, 6, 4], 2), 5);
    assert_eq!(find_kth_largest(vec![3, 2, 3, 1, 2, 4, 5, 5, 6], 4), 4);
    assert_eq!(find_kth_largest(vec![1], 1), 1);
    println!("PASS");
}
''',
"lua": '''local function find_kth_largest(nums, k)
    local a = {table.unpack(nums)}
    local length = #a
    for i = length, length - k + 1, -1 do
        for j = 1, i - 1 do
            if a[j] > a[j + 1] then a[j], a[j + 1] = a[j + 1], a[j] end
        end
    end
    return a[length - k + 1]
end
assert(find_kth_largest({3, 2, 1, 5, 6, 4}, 2) == 5)
assert(find_kth_largest({3, 2, 3, 1, 2, 4, 5, 5, 6}, 4) == 4)
assert(find_kth_largest({1}, 1) == 1)
print("PASS")
''',
"c": '''#include <stdio.h>
static int find_kth_largest(const int *nums, int n, int k) {
    int a[4096];
    for (int i = 0; i < n; i++) a[i] = nums[i];
    for (int i = n - 1; i > n - 1 - k; i--) {
        for (int j = 0; j < i; j++) {
            if (a[j] > a[j + 1]) { int t = a[j]; a[j] = a[j + 1]; a[j + 1] = t; }
        }
    }
    return a[n - k];
}
int main(void) {
    if (find_kth_largest((int[]){3,2,1,5,6,4}, 6, 2) != 5) { printf("FAIL 1\\n"); return 1; }
    if (find_kth_largest((int[]){3,2,3,1,2,4,5,5,6}, 9, 4) != 4) { printf("FAIL 2\\n"); return 1; }
    if (find_kth_largest((int[]){1}, 1, 1) != 1) { printf("FAIL 3\\n"); return 1; }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''#include <cassert>
#include <iostream>
#include <vector>
static int findKthLargest(const std::vector<int> &nums, int k) {
    std::vector<int> a = nums;
    int n = static_cast<int>(a.size());
    for (int i = n - 1; i > n - 1 - k; --i) {
        for (int j = 0; j < i; ++j) {
            if (a[j] > a[j + 1]) std::swap(a[j], a[j + 1]);
        }
    }
    return a[n - k];
}
int main() {
    assert(findKthLargest({3, 2, 1, 5, 6, 4}, 2) == 5);
    assert(findKthLargest({3, 2, 3, 1, 2, 4, 5, 5, 6}, 4) == 4);
    assert(findKthLargest({1}, 1) == 1);
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''find_kth_largest <- function(nums, k) {
  a <- nums
  n <- length(a)
  for (i in (n - 1):(n - k)) {  # R 降序需守卫
    if (i < 1) break
    for (j in seq_len(i)) {
      if (a[j] > a[j + 1]) { t <- a[j]; a[j] <- a[j + 1]; a[j + 1] <- t }
    }
  }
  a[n - k + 1]
}
stopifnot(find_kth_largest(c(3, 2, 1, 5, 6, 4), 2) == 5)
stopifnot(find_kth_largest(c(3, 2, 3, 1, 2, 4, 5, 5, 6), 4) == 4)
stopifnot(find_kth_largest(c(1), 1) == 1)
cat("PASS\\n")
''',
"zig": '''const std = @import("std");
fn findKthLargest(nums: []const i32, k: usize) i32 {
    var a: [4096]i32 = undefined;
    @memcpy(a[0..nums.len], nums);
    const n = nums.len;
    var i: isize = @intCast(n - 1);
    const bound: isize = @as(isize, @intCast(n)) - 1 - @as(isize, @intCast(k));
    while (i > bound) : (i -= 1) {
        var j: usize = 0;
        while (@as(isize, @intCast(j)) < i) : (j += 1) {
            if (a[j] > a[j + 1]) { const t = a[j]; a[j] = a[j + 1]; a[j + 1] = t; }
        }
    }
    return a[n - k];
}
pub fn main() !void {
    if (findKthLargest(&[_]i32{ 3, 2, 1, 5, 6, 4 }, 2) != 5) return error.TestFailed;
    if (findKthLargest(&[_]i32{ 3, 2, 3, 1, 2, 4, 5, 5, 6 }, 4) != 4) return error.TestFailed;
    if (findKthLargest(&[_]i32{1}, 1) != 1) return error.TestFailed;
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''int findKthLargest(List<int> nums, int k) {
  final a = List<int>.from(nums);
  final n = a.length;
  for (var i = n - 1; i > n - 1 - k; i--) {
    for (var j = 0; j < i; j++) {
      if (a[j] > a[j + 1]) {
        final t = a[j];
        a[j] = a[j + 1];
        a[j + 1] = t;
      }
    }
  }
  return a[n - k];
}
void main() {
  if (findKthLargest([3, 2, 1, 5, 6, 4], 2) != 5) throw StateError('c1');
  if (findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) != 4) throw StateError('c2');
  if (findKthLargest([1], 1) != 1) throw StateError('c3');
  print('PASS');
}
''',
}

A215["quickselect"] = {
"rust": '''fn quickselect(a: &mut [i32], l: usize, r: usize, k: usize) -> i32 {
    if l >= r { return a[l]; }
    let (mut i, mut j) = (l, r);
    let pivot = a[(l + r) / 2];
    while i <= j {
        while a[i] > pivot { i += 1; }
        while a[j] < pivot { if j == 0 { break; } j -= 1; }
        if i <= j { a.swap(i, j); if i < usize::MAX { i += 1; } if j > 0 { j -= 1; } else { break; } }
    }
    // 分区：[l..j] >= pivot >= [i..r]（降序）
    if k <= j + 1 && j + 1 > l { if k - 1 <= j { return quickselect(a, l, j, k); } }
    if k - 1 >= i { return quickselect(a, i, r, k); }
    a[k - 1]
}
fn find_kth_largest(mut nums: Vec<i32>, k: i32) -> i32 {
    let n = nums.len();
    quickselect(&mut nums, 0, n - 1, k as usize)
}
fn main() {
    assert_eq!(find_kth_largest(vec![3, 2, 1, 5, 6, 4], 2), 5);
    assert_eq!(find_kth_largest(vec![3, 2, 3, 1, 2, 4, 5, 5, 6], 4), 4);
    assert_eq!(find_kth_largest(vec![1], 1), 1);
    println!("PASS");
}
''',
"lua": '''local function quickselect(a, l, r, k)
    if l >= r then return a[k] end
    local i, j = l, r
    local pivot = a[math.floor((l + r) / 2)]
    while i <= j do
        while a[i] > pivot do i = i + 1 end
        while a[j] < pivot do j = j - 1 end
        if i <= j then
            a[i], a[j] = a[j], a[i]
            i, j = i + 1, j - 1
        end
    end
    if k <= j then return quickselect(a, l, j, k) end
    if k >= i then return quickselect(a, i, r, k) end
    return a[k]
end
local function find_kth_largest(nums, k)
    local a = {table.unpack(nums)}
    return quickselect(a, 1, #a, k)
end
assert(find_kth_largest({3, 2, 1, 5, 6, 4}, 2) == 5)
assert(find_kth_largest({3, 2, 3, 1, 2, 4, 5, 5, 6}, 4) == 4)
assert(find_kth_largest({1}, 1) == 1)
print("PASS")
''',
"c": '''#include <stdio.h>
static void quickselect(int *a, int l, int r, int k) {
    if (l >= r) return;
    int i = l, j = r;
    int pivot = a[(l + r) / 2];
    while (i <= j) {
        while (a[i] > pivot) i++;
        while (a[j] < pivot) j--;
        if (i <= j) { int t = a[i]; a[i] = a[j]; a[j] = t; i++; j--; }
    }
    if (k <= j + 1) { if (k - 1 <= j && l < j) quickselect(a, l, j, k); return; }
    if (k >= i + 1 && i < r) quickselect(a, i, r, k);
}
static int find_kth_largest(const int *nums, int n, int k) {
    int a[4096];
    for (int i = 0; i < n; i++) a[i] = nums[i];
    quickselect(a, 0, n - 1, k);
    return a[k - 1];
}
int main(void) {
    if (find_kth_largest((int[]){3,2,1,5,6,4}, 6, 2) != 5) { printf("FAIL 1\\n"); return 1; }
    if (find_kth_largest((int[]){3,2,3,1,2,4,5,5,6}, 9, 4) != 4) { printf("FAIL 2\\n"); return 1; }
    if (find_kth_largest((int[]){1}, 1, 1) != 1) { printf("FAIL 3\\n"); return 1; }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''#include <cassert>
#include <iostream>
#include <vector>
static void quickselect(std::vector<int> &a, int l, int r, int k) {
    if (l >= r) return;
    int i = l, j = r;
    int pivot = a[(l + r) / 2];
    while (i <= j) {
        while (a[i] > pivot) ++i;
        while (a[j] < pivot) --j;
        if (i <= j) { std::swap(a[i], a[j]); ++i; --j; }
    }
    if (k <= j + 1) { if (l < j) quickselect(a, l, j, k); return; }
    if (k >= i + 1 && i < r) quickselect(a, i, r, k);
}
static int findKthLargest(std::vector<int> nums, int k) {
    quickselect(nums, 0, static_cast<int>(nums.size()) - 1, k);
    return nums[k - 1];
}
int main() {
    assert(findKthLargest({3, 2, 1, 5, 6, 4}, 2) == 5);
    assert(findKthLargest({3, 2, 3, 1, 2, 4, 5, 5, 6}, 4) == 4);
    assert(findKthLargest({1}, 1) == 1);
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''find_kth_largest <- function(nums, k) {
  e <- new.env(parent = emptyenv()); e$a <- nums
  qs <- function(l, r) {
    if (l >= r) return(invisible(NULL))
    i <- l; j <- r
    pivot <- e$a[floor((l + r) / 2)]
    while (i <= j) {
      while (e$a[i] > pivot) i <- i + 1L
      while (e$a[j] < pivot) j <- j - 1L
      if (i <= j) {
        t <- e$a[i]; e$a[i] <- e$a[j]; e$a[j] <- t
        i <- i + 1L; j <- j - 1L
      }
    }
    if (k <= j && l < j) qs(l, j)
    else if (k >= i && i < r) qs(i, r)
  }
  qs(1L, length(e$a))
  e$a[k]
}
stopifnot(find_kth_largest(c(3, 2, 1, 5, 6, 4), 2) == 5)
stopifnot(find_kth_largest(c(3, 2, 3, 1, 2, 4, 5, 5, 6), 4) == 4)
stopifnot(find_kth_largest(c(1), 1) == 1)
cat("PASS\\n")
''',
"zig": '''const std = @import("std");
fn quickselect(a: []i32, l: usize, r: usize, k: usize) void {
    if (l >= r) return;
    var i = l;
    var j = r;
    const pivot = a[(l + r) / 2];
    while (i <= j) {
        while (a[i] > pivot) i += 1;
        while (a[j] < pivot) j -= 1;
        if (i <= j) {
            const t = a[i]; a[i] = a[j]; a[j] = t;
            i += 1;
            if (j == 0) break;
            j -= 1;
        }
    }
    if (k <= j + 1) {
        if (l < j) quickselect(a, l, j, k);
        return;
    }
    if (k >= i + 1 and i < r) quickselect(a, i, r, k);
}
fn findKthLargest(nums: []const i32, k: usize) i32 {
    var a: [4096]i32 = undefined;
    @memcpy(a[0..nums.len], nums);
    quickselect(a[0..nums.len], 0, nums.len - 1, k);
    return a[k - 1];
}
pub fn main() !void {
    if (findKthLargest(&[_]i32{ 3, 2, 1, 5, 6, 4 }, 2) != 5) return error.TestFailed;
    if (findKthLargest(&[_]i32{ 3, 2, 3, 1, 2, 4, 5, 5, 6 }, 4) != 4) return error.TestFailed;
    if (findKthLargest(&[_]i32{1}, 1) != 1) return error.TestFailed;
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''void quickselect(List<int> a, int l, int r, int k) {
  if (l >= r) return;
  var i = l, j = r;
  final pivot = a[(l + r) ~/ 2];
  while (i <= j) {
    while (a[i] > pivot) i++;
    while (a[j] < pivot) j--;
    if (i <= j) {
      final t = a[i];
      a[i] = a[j];
      a[j] = t;
      i++;
      j--;
    }
  }
  if (k <= j + 1) {
    if (l < j) quickselect(a, l, j, k);
    return;
  }
  if (k >= i + 1 && i < r) quickselect(a, i, r, k);
}
int findKthLargest(List<int> nums, int k) {
  final a = List<int>.from(nums);
  quickselect(a, 0, a.length - 1, k);
  return a[k - 1];
}
void main() {
  if (findKthLargest([3, 2, 1, 5, 6, 4], 2) != 5) throw StateError('c1');
  if (findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) != 4) throw StateError('c2');
  if (findKthLargest([1], 1) != 1) throw StateError('c3');
  print('PASS');
}
''',
}

A215["heap"] = {
"rust": '''use std::collections::BinaryHeap;
fn find_kth_largest(nums: Vec<i32>, k: i32) -> i32 {
    let mut heap: BinaryHeap<i32> = BinaryHeap::new();
    for v in nums { heap.push(v); }
    for _ in 0..k - 1 { heap.pop(); }
    heap.peek().copied().unwrap_or(-1)
}
fn main() {
    assert_eq!(find_kth_largest(vec![3, 2, 1, 5, 6, 4], 2), 5);
    assert_eq!(find_kth_largest(vec![3, 2, 3, 1, 2, 4, 5, 5, 6], 4), 4);
    assert_eq!(find_kth_largest(vec![1], 1), 1);
    println!("PASS");
}
''',
"lua": '''local function find_kth_largest(nums, k)
    -- 简易最大堆
    local h = {}
    local function up(i)
        while i > 1 and h[i] > h[i // 2] do
            h[i], h[i // 2] = h[i // 2], h[i]
            i = i // 2
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
    for _, v in ipairs(nums) do h[#h + 1] = v; up(#h) end
    for _ = 1, k - 1 do
        h[1] = h[#h]
        h[#h] = nil
        if #h > 0 then down(1) end
    end
    return h[1]
end
assert(find_kth_largest({3, 2, 1, 5, 6, 4}, 2) == 5)
assert(find_kth_largest({3, 2, 3, 1, 2, 4, 5, 5, 6}, 4) == 4)
assert(find_kth_largest({1}, 1) == 1)
print("PASS")
''',
"c": '''#include <stdio.h>
static void heap_up(int *h, int i) {
    while (i > 1 && h[i] > h[i / 2]) { int t = h[i]; h[i] = h[i / 2]; h[i / 2] = t; i /= 2; }
}
static void heap_down(int *h, int n, int i) {
    while (1) {
        int l = 2 * i, r = 2 * i + 1, m = i;
        if (l <= n && h[l] > h[m]) m = l;
        if (r <= n && h[r] > h[m]) m = r;
        if (m == i) break;
        int t = h[i]; h[i] = h[m]; h[m] = t;
        i = m;
    }
}
static int find_kth_largest(const int *nums, int n, int k) {
    int h[4096];
    int hn = 0;
    for (int i = 0; i < n; i++) { h[++hn] = nums[i]; heap_up(h, hn); }
    for (int t = 0; t < k - 1; t++) {
        h[1] = h[hn];
        hn--;
        if (hn > 0) heap_down(h, hn, 1);
    }
    return h[1];
}
int main(void) {
    if (find_kth_largest((int[]){3,2,1,5,6,4}, 6, 2) != 5) { printf("FAIL 1\\n"); return 1; }
    if (find_kth_largest((int[]){3,2,3,1,2,4,5,5,6}, 9, 4) != 4) { printf("FAIL 2\\n"); return 1; }
    if (find_kth_largest((int[]){1}, 1, 1) != 1) { printf("FAIL 3\\n"); return 1; }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''#include <cassert>
#include <iostream>
#include <queue>
#include <vector>
static int findKthLargest(const std::vector<int> &nums, int k) {
    std::priority_queue<int> heap(nums.begin(), nums.end());
    for (int i = 0; i < k - 1; ++i) heap.pop();
    return heap.top();
}
int main() {
    assert(findKthLargest({3, 2, 1, 5, 6, 4}, 2) == 5);
    assert(findKthLargest({3, 2, 3, 1, 2, 4, 5, 5, 6}, 4) == 4);
    assert(findKthLargest({1}, 1) == 1);
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''find_kth_largest <- function(nums, k) {
  h <- sort(nums, decreasing = TRUE)  # 等价堆序（R 无内建堆）
  h[k]
}
stopifnot(find_kth_largest(c(3, 2, 1, 5, 6, 4), 2) == 5)
stopifnot(find_kth_largest(c(3, 2, 3, 1, 2, 4, 5, 5, 6), 4) == 4)
stopifnot(find_kth_largest(c(1), 1) == 1)
cat("PASS\\n")
''',
"zig": '''const std = @import("std");
fn findKthLargest(nums: []const i32, k: usize, alloc: std.mem.Allocator) i32 {
    // 最大堆（手写 up/down）
    var h = std.ArrayList(i32).init(alloc);
    defer h.deinit();
    for (nums) |v| {
        h.append(v) catch unreachable;
        var i = h.items.len - 1;
        while (i > 0) {
            const p = (i - 1) / 2;
            if (h.items[i] <= h.items[p]) break;
            const t = h.items[i]; h.items[i] = h.items[p]; h.items[p] = t;
            i = p;
        }
    }
    var t: usize = 0;
    while (t + 1 < k) : (t += 1) {
        const last = h.pop().?;
        if (h.items.len > 0) {
            h.items[0] = last;
            var i: usize = 0;
            while (true) {
                const l = 2 * i + 1;
                const r = 2 * i + 2;
                var m = i;
                if (l < h.items.len and h.items[l] > h.items[m]) m = l;
                if (r < h.items.len and h.items[r] > h.items[m]) m = r;
                if (m == i) break;
                const tmp = h.items[i]; h.items[i] = h.items[m]; h.items[m] = tmp;
                i = m;
            }
        }
    }
    return h.items[0];
}
pub fn main() !void {
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();
    if (findKthLargest(&[_]i32{ 3, 2, 1, 5, 6, 4 }, 2, arena.allocator()) != 5) return error.TestFailed;
    if (findKthLargest(&[_]i32{ 3, 2, 3, 1, 2, 4, 5, 5, 6 }, 4, arena.allocator()) != 4) return error.TestFailed;
    if (findKthLargest(&[_]i32{1}, 1, arena.allocator()) != 1) return error.TestFailed;
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''int findKthLargest(List<int> nums, int k) {
  // 简易最大堆
  final h = <int>[];
  void up(int i) {
    while (i > 0) {
      final p = (i - 1) ~/ 2;
      if (h[i] <= h[p]) break;
      final t = h[i];
      h[i] = h[p];
      h[p] = t;
      i = p;
    }
  }
  void down(int i) {
    while (true) {
      final l = 2 * i + 1, r = 2 * i + 2;
      var m = i;
      if (l < h.length && h[l] > h[m]) m = l;
      if (r < h.length && h[r] > h[m]) m = r;
      if (m == i) break;
      final t = h[i];
      h[i] = h[m];
      h[m] = t;
      i = m;
    }
  }
  for (final v in nums) {
    h.add(v);
    up(h.length - 1);
  }
  for (var t = 0; t + 1 < k; t++) {
    final last = h.removeLast();
    if (h.isNotEmpty) {
      h[0] = last;
      down(0);
    }
  }
  return h.first;
}
void main() {
  if (findKthLargest([3, 2, 1, 5, 6, 4], 2) != 5) throw StateError('c1');
  if (findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) != 4) throw StateError('c2');
  if (findKthLargest([1], 1) != 1) throw StateError('c3');
  print('PASS');
}
''',
}

# ============ lc_347 前k个高频（堆族，结果排序后比较） ============
A347 = {
"rust": '''use std::collections::HashMap;
fn top_k_frequent(nums: Vec<i32>, k: i32) -> Vec<i32> {
    let mut counts: HashMap<i32, i64> = HashMap::new();
    for &v in &nums { *counts.entry(v).or_insert(0) += 1; }
    let mut items: Vec<(i32, i64)> = counts.into_iter().collect();
    items.sort_by(|a, b| b.1.cmp(&a.1).then(a.0.cmp(&b.0)));
    items.into_iter().take(k as usize).map(|(v, _)| v).collect()
}
fn main() {
    let got = top_k_frequent(vec![1, 1, 1, 2, 2, 3], 2);
    let mut g = got.clone();
    g.sort();
    assert_eq!(g, vec![1, 2]);
    assert_eq!(top_k_frequent(vec![1], 1), vec![1]);
    println!("PASS");
}
''',
"lua": '''local function top_k_frequent(nums, k)
    local counts = {}
    for _, v in ipairs(nums) do counts[v] = (counts[v] or 0) + 1 end
    local items = {}
    for v, c in pairs(counts) do items[#items + 1] = {v, c} end
    table.sort(items, function(a, b)
        if a[2] ~= b[2] then return a[2] > b[2] end
        return a[1] < b[1]
    end)
    local res = {}
    for i = 1, k do res[i] = items[i][1] end
    return res
end
local got = top_k_frequent({1, 1, 1, 2, 2, 3}, 2)
table.sort(got)
assert(#got == 2 and got[1] == 1 and got[2] == 2)
local g2 = top_k_frequent({1}, 1)
assert(#g2 == 1 and g2[1] == 1)
print("PASS")
''',
"c": '''#include <stdio.h>
#include <stdlib.h>
typedef struct { int v; long c; } VC;
static int cmp_vc(const void *a, const void *b) {
    const VC *x = a, *y = b;
    if (x->c != y->c) return (x->c > y->c) ? -1 : 1;
    return x->v - y->v;
}
static int top_k_frequent(const int *nums, int n, int k, int out[]) {
    VC vcs[4096];
    int m = 0;
    for (int i = 0; i < n; i++) {
        int found = 0;
        for (int j = 0; j < m; j++) if (vcs[j].v == nums[i]) { vcs[j].c++; found = 1; break; }
        if (!found) { vcs[m].v = nums[i]; vcs[m].c = 1; m++; }
    }
    qsort(vcs, m, sizeof(VC), cmp_vc);
    for (int i = 0; i < k && i < m; i++) out[i] = vcs[i].v;
    return k < m ? k : m;
}
static int cmp_int(const void *a, const void *b) { return *(const int *)a - *(const int *)b; }
int main(void) {
    int out[64], n;
    n = top_k_frequent((int[]){1,1,1,2,2,3}, 6, 2, out);
    qsort(out, n, sizeof(int), cmp_int);
    if (n != 2 || out[0] != 1 || out[1] != 2) { printf("FAIL 1\\n"); return 1; }
    n = top_k_frequent((int[]){1}, 1, 1, out);
    if (n != 1 || out[0] != 1) { printf("FAIL 2\\n"); return 1; }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''#include <algorithm>
#include <cassert>
#include <iostream>
#include <unordered_map>
#include <vector>
static std::vector<int> topKFrequent(const std::vector<int> &nums, int k) {
    std::unordered_map<int, long long> counts;
    for (int v : nums) ++counts[v];
    std::vector<std::pair<int, long long>> items(counts.begin(), counts.end());
    std::sort(items.begin(), items.end(), [](auto &a, auto &b) {
        if (a.second != b.second) return a.second > b.second;
        return a.first < b.first;
    });
    std::vector<int> res;
    for (int i = 0; i < k && i < static_cast<int>(items.size()); ++i) res.push_back(items[i].first);
    return res;
}
int main() {
    auto got = topKFrequent({1, 1, 1, 2, 2, 3}, 2);
    std::sort(got.begin(), got.end());
    assert((got == std::vector<int>{1, 2}));
    assert((topKFrequent({1}, 1) == std::vector<int>{1}));
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''top_k_frequent <- function(nums, k) {
  counts <- table(nums)
  items <- data.frame(v = as.integer(names(counts)), c = as.integer(counts))
  items <- items[order(-items$c, items$v), ]
  head(items$v, k)
}
got <- sort(top_k_frequent(c(1, 1, 1, 2, 2, 3), 2))
stopifnot(identical(got, c(1L, 2L)))
stopifnot(identical(top_k_frequent(c(1), 1), 1L))
cat("PASS\\n")
''',
"zig": '''const std = @import("std");
const VC = struct { v: i32, c: i64 };
fn topKFrequent(nums: []const i32, k: usize, alloc: std.mem.Allocator, out: *std.ArrayList(i32)) void {
    var vcs = std.ArrayList(VC).init(alloc);
    for (nums) |v| {
        var found = false;
        for (vcs.items) |*vc| {
            if (vc.v == v) { vc.c += 1; found = true; break; }
        }
        if (!found) vcs.append(.{ .v = v, .c = 1 }) catch unreachable;
    }
    const S = struct {
        fn lt(_: void, a: VC, b: VC) bool {
            if (a.c != b.c) return a.c > b.c;
            return a.v < b.v;
        }
    };
    std.sort.pdq(VC, vcs.items, {}, S.lt);
    for (vcs.items[0..@min(k, vcs.items.len)]) |vc| out.append(vc.v) catch unreachable;
}
pub fn main() !void {
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();
    const alloc = arena.allocator();
    var out = std.ArrayList(i32).init(std.heap.page_allocator);
    defer out.deinit();
    topKFrequent(&[_]i32{ 1, 1, 1, 2, 2, 3 }, 2, alloc, &out);
    if (out.items.len != 2) return error.TestFailed;
    std.sort.pdq(i32, out.items, {}, std.sort.asc(i32));
    if (out.items[0] != 1 or out.items[1] != 2) return error.TestFailed;
    out.clearRetainingCapacity();
    topKFrequent(&[_]i32{1}, 1, alloc, &out);
    if (out.items.len != 1 or out.items[0] != 1) return error.TestFailed;
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''List<int> topKFrequent(List<int> nums, int k) {
  final counts = <int, int>{};
  for (final v in nums) {
    counts[v] = (counts[v] ?? 0) + 1;
  }
  final items = counts.entries.toList()
    ..sort((a, b) {
      if (a.value != b.value) return b.value.compareTo(a.value);
      return a.key.compareTo(b.key);
    });
  return items.take(k).map((e) => e.key).toList();
}
void main() {
  final got = topKFrequent([1, 1, 1, 2, 2, 3], 2)..sort();
  if (got.toString() != '[1, 2]') throw StateError('c1');
  if (topKFrequent([1], 1).toString() != '[1]') throw StateError('c2');
  print('PASS');
}
''',
}

# ============ lc_295 数据流中位数（双堆） ============
A295 = {
"rust": '''use std::collections::BinaryHeap;
struct MedianFinder { max_h: BinaryHeap<i32>, min_h: std::collections::BinaryHeap<std::cmp::Reverse<i32>> }
impl MedianFinder {
    fn new() -> Self { MedianFinder { max_h: BinaryHeap::new(), min_h: BinaryHeap::new() } }
    fn add_num(&mut self, num: i32) {
        if self.max_h.is_empty() || num <= *self.max_h.peek().unwrap() {
            self.max_h.push(num);
        } else {
            self.min_h.push(std::cmp::Reverse(num));
        }
        // 平衡：max_h 与 min_h 最多差 1，且 max_h 可以多 1
        if self.max_h.len() > self.min_h.len() + 1 {
            let v = self.max_h.pop().unwrap();
            self.min_h.push(std::cmp::Reverse(v));
        } else if self.min_h.len() > self.max_h.len() {
            let std::cmp::Reverse(v) = self.min_h.pop().unwrap();
            self.max_h.push(v);
        }
    }
    fn find_median(&self) -> f64 {
        if self.max_h.len() == self.min_h.len() {
            (*self.max_h.peek().unwrap() as f64 + self.min_h.peek().unwrap().0 as f64) / 2.0
        } else {
            *self.max_h.peek().unwrap() as f64
        }
    }
}
fn main() {
    let mut mf = MedianFinder::new();
    for x in [1, 2, 3, 4, 5] { mf.add_num(x); }
    assert_eq!(mf.find_median(), 3.0);
    let mut mf2 = MedianFinder::new();
    mf2.add_num(1);
    mf2.add_num(2);
    assert_eq!(mf2.find_median(), 1.5);
    mf2.add_num(3);
    assert_eq!(mf2.find_median(), 2.0);
    println!("PASS");
}
''',
"lua": '''local MedianFinder = {}
MedianFinder.__index = MedianFinder
function MedianFinder.new()
    return setmetatable({{maxh = {{}}, minh = {{}}}}, MedianFinder)
end
local function hpush(h, v, less)
    h[#h + 1] = v
    local i = #h
    while i > 1 do
        local p = i // 2
        if not less(h[i], h[p]) then break end
        h[i], h[p] = h[p], h[i]
        i = p
    end
end
local function hpop(h, less)
    local top = h[1]
    h[1] = h[#h]
    h[#h] = nil
    local i, n = 1, #h
    while true do
        local l, r, m = 2 * i, 2 * i + 1, i
        if l <= n and less(h[l], h[m]) then m = l end
        if r <= n and less(h[r], h[m]) then m = r end
        if m == i then break end
        h[i], h[m] = h[m], h[i]
        i = m
    end
    return top
end
function MedianFinder:add_num(num)
    if #self.maxh == 0 or num <= self.maxh[1] then
        hpush(self.maxh, num, function(a, b) return a > b end)
    else
        hpush(self.minh, num, function(a, b) return a < b end)
    end
    if #self.maxh > #self.minh + 1 then
        hpush(self.minh, hpop(self.maxh, function(a, b) return a > b end), function(a, b) return a < b end)
    elseif #self.minh > #self.maxh then
        hpush(self.maxh, hpop(self.minh, function(a, b) return a < b end), function(a, b) return a > b end)
    end
end
function MedianFinder:find_median()
    if #self.maxh == #self.minh then
        return (self.maxh[1] + self.minh[1]) / 2
    end
    return self.maxh[1]
end
local mf = MedianFinder.new()
for _, x in ipairs({1, 2, 3, 4, 5}) do mf:add_num(x) end
assert(mf:find_median() == 3)
local mf2 = MedianFinder.new()
mf2:add_num(1); mf2:add_num(2)
assert(mf2:find_median() == 1.5)
mf2:add_num(3)
assert(mf2:find_median() == 2)
print("PASS")
''',
"c": '''#include <stdio.h>
/* 双堆：maxh 大根堆（存较小半），minh 小根堆（存较大半） */
static int maxh[8192], minhd[8192];
static int nmax, nmin;
static void push_maxh(int v) {
    maxh[++nmax] = v;
    int i = nmax;
    while (i > 1 && maxh[i] > maxh[i / 2]) { int t = maxh[i]; maxh[i] = maxh[i / 2]; maxh[i / 2] = t; i /= 2; }
}
static void push_minh(int v) {
    minhd[++nmin] = v;
    int i = nmin;
    while (i > 1 && minhd[i] < minhd[i / 2]) { int t = minhd[i]; minhd[i] = minhd[i / 2]; minhd[i / 2] = t; i /= 2; }
}
static int pop_maxh(void) {
    int top = maxh[1];
    maxh[1] = maxh[nmax--];
    int i = 1;
    while (1) {
        int l = 2 * i, r = 2 * i + 1, m = i;
        if (l <= nmax && maxh[l] > maxh[m]) m = l;
        if (r <= nmax && maxh[r] > maxh[m]) m = r;
        if (m == i) break;
        int t = maxh[i]; maxh[i] = maxh[m]; maxh[m] = t; i = m;
    }
    return top;
}
static int pop_minh(void) {
    int top = minhd[1];
    minhd[1] = minhd[nmin--];
    int i = 1;
    while (1) {
        int l = 2 * i, r = 2 * i + 1, m = i;
        if (l <= nmin && minhd[l] < minhd[m]) m = l;
        if (r <= nmin && minhd[r] < minhd[m]) m = r;
        if (m == i) break;
        int t = minhd[i]; minhd[i] = minhd[m]; minhd[m] = t; i = m;
    }
    return top;
}
static void mf_add(int num) {
    if (nmax == 0 || num <= maxh[1]) push_maxh(num);
    else push_minh(num);
    if (nmax > nmin + 1) push_minh(pop_maxh());
    else if (nmin > nmax) push_maxh(pop_minh());
}
static double mf_median(void) {
    if (nmax == nmin) return (maxh[1] + minhd[1]) / 2.0;
    return maxh[1];
}
int main(void) {
    nmax = nmin = 0;
    int xs[] = {1, 2, 3, 4, 5};
    for (int i = 0; i < 5; i++) mf_add(xs[i]);
    if (mf_median() != 3.0) { printf("FAIL 1\\n"); return 1; }
    nmax = nmin = 0;
    mf_add(1); mf_add(2);
    if (mf_median() != 1.5) { printf("FAIL 2\\n"); return 1; }
    mf_add(3);
    if (mf_median() != 2.0) { printf("FAIL 3\\n"); return 1; }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''#include <cassert>
#include <cstdio>
#include <iostream>
#include <queue>
struct MedianFinder {
    std::priority_queue<int> maxH;
    std::priority_queue<int, std::vector<int>, std::greater<int>> minH;
    void addNum(int num) {
        if (maxH.empty() || num <= maxH.top()) maxH.push(num);
        else minH.push(num);
        if (maxH.size() > minH.size() + 1) { minH.push(maxH.top()); maxH.pop(); }
        else if (minH.size() > maxH.size()) { maxH.push(minH.top()); minH.pop(); }
    }
    double findMedian() const {
        if (maxH.size() == minH.size()) return (maxH.top() + minH.top()) / 2.0;
        return maxH.top();
    }
};
int main() {
    MedianFinder mf;
    for (int x : {1, 2, 3, 4, 5}) mf.addNum(x);
    assert(mf.findMedian() == 3.0);
    MedianFinder mf2;
    mf2.addNum(1);
    mf2.addNum(2);
    assert(mf2.findMedian() == 1.5);
    mf2.addNum(3);
    assert(mf2.findMedian() == 2.0);
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''MedianFinder <- function() {
  e <- new.env(parent = emptyenv())
  e$low <- integer(0)   # 排序数组模拟双堆（有序插入）
  e$add_num <- function(num) {
    e$low <<- sort(c(e$low, num))
  }
  e$find_median <- function() {
    n <- length(e$low)
    if (n == 0) return(NA)
    if (n %% 2 == 1) e$low[(n + 1) / 2] else (e$low[n / 2] + e$low[n / 2 + 1]) / 2
  }
  e
}
mf <- MedianFinder()
for (x in c(1, 2, 3, 4, 5)) mf$add_num(x)
stopifnot(mf$find_median() == 3)
mf2 <- MedianFinder()
mf2$add_num(1); mf2$add_num(2)
stopifnot(mf2$find_median() == 1.5)
mf2$add_num(3)
stopifnot(mf2$find_median() == 2)
cat("PASS\\n")
''',
"zig": '''const std = @import("std");
const MedianFinder = struct {
    // 有序数组模拟（等价双堆语义）
    items: std.ArrayList(i32),
    fn init(alloc: std.mem.Allocator) MedianFinder {
        return .{ .items = std.ArrayList(i32).init(alloc) };
    }
    fn addNum(self: *MedianFinder, num: i32) void {
        var pos: usize = 0;
        while (pos < self.items.items.len and self.items.items[pos] < num) pos += 1;
        self.items.insert(pos, num) catch unreachable;
    }
    fn findMedian(self: *const MedianFinder) f64 {
        const n = self.items.items.len;
        if (n % 2 == 1) return @floatFromInt(self.items.items[n / 2]);
        return (@as(f64, @floatFromInt(self.items.items[n / 2 - 1])) + @as(f64, @floatFromInt(self.items.items[n / 2]))) / 2.0;
    }
};
pub fn main() !void {
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();
    var mf = MedianFinder.init(arena.allocator());
    for ([_]i32{ 1, 2, 3, 4, 5 }) |x| mf.addNum(x);
    if (mf.findMedian() != 3.0) return error.TestFailed;
    var mf2 = MedianFinder.init(arena.allocator());
    mf2.addNum(1);
    mf2.addNum(2);
    if (mf2.findMedian() != 1.5) return error.TestFailed;
    mf2.addNum(3);
    if (mf2.findMedian() != 2.0) return error.TestFailed;
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''class MedianFinder {
  final List<int> _items = [];
  void addNum(int num) {
    var pos = 0;
    while (pos < _items.length && _items[pos] < num) {
      pos++;
    }
    _items.insert(pos, num);
  }
  double findMedian() {
    final n = _items.length;
    if (n % 2 == 1) return _items[n ~/ 2].toDouble();
    return (_items[n ~/ 2 - 1] + _items[n ~/ 2]) / 2;
  }
}
void main() {
  final mf = MedianFinder();
  for (final x in [1, 2, 3, 4, 5]) {
    mf.addNum(x);
  }
  if (mf.findMedian() != 3.0) throw StateError('c1');
  final mf2 = MedianFinder();
  mf2.addNum(1);
  mf2.addNum(2);
  if (mf2.findMedian() != 1.5) throw StateError('c2');
  mf2.addNum(3);
  if (mf2.findMedian() != 2.0) throw StateError('c3');
  print('PASS');
}
''',
}

# ============ lc_23 合并K个升序链表（顺序fold / 指针扫描heap） ============
A23 = {}
A23["seq"] = {
"rust": '''#[derive(Debug)]
struct ListNode {{ val: i32, next: Option<Box<ListNode>> }}
fn build_list(vals: &[i32]) -> Option<Box<ListNode>> {{
    let mut head: Option<Box<ListNode>> = None;
    for &v in vals.iter().rev() {{
        let mut n = Box::new(ListNode {{ val: v, next: head }});
        head = Some(n);
    }}
    head
}}
fn list_to_vec(head: &Option<Box<ListNode>>) -> Vec<i32> {{
    let mut out = Vec::new();
    let mut cur = head;
    while let Some(n) = cur {{ out.push(n.val); cur = &n.next; }}
    out
}}
fn merge_two(a: Option<Box<ListNode>>, b: Option<Box<ListNode>>) -> Option<Box<ListNode>> {{
    match (a, b) {{
        (None, x) | (x, None) => x,
        (Some(mut x), Some(mut y)) => {{
            if y.val < x.val {{ std::mem::swap(&mut x, &mut y); }}
            x.next = merge_two(x.next.take(), Some(y));
            Some(x)
        }}
    }}
}}
fn merge_k_lists(lists: Vec<Option<Box<ListNode>>>) -> Option<Box<ListNode>> {{
    let mut acc = None;
    for l in lists {{ acc = merge_two(acc, l); }}
    acc
}}
fn main() {{
    let lists = vec![
        build_list(&[1, 4, 5]),
        build_list(&[1, 3, 4]),
        build_list(&[2, 6]),
    ];
    let got = list_to_vec(&merge_k_lists(lists));
    assert_eq!(got, vec![1, 1, 2, 3, 4, 4, 5, 6]);
    let empty: Vec<Option<Box<ListNode>>> = vec![];
    assert_eq!(list_to_vec(&merge_k_lists(empty)), Vec::<i32>::new());
    let lists2 = vec![build_list(&[])];
    assert_eq!(list_to_vec(&merge_k_lists(lists2)), Vec::<i32>::new());
    println!("PASS");
}}
''',
"lua": '''local ListNode = {}
ListNode.__index = ListNode
function ListNode.new(val, next) return setmetatable({val = val, next = next}, ListNode) end
local function build_list(vals)
    local head, cur = nil, nil
    for _, v in ipairs(vals) do
        local n = ListNode.new(v)
        if not head then head, cur = n, n else cur.next, cur = n, n end
    end
    return head
end
local function list_to_vec(head)
    local out = {}
    while head do out[#out + 1] = head.val; head = head.next end
    return out
end
local function merge_two(a, b)
    local dummy = ListNode.new(0)
    local cur = dummy
    while a and b do
        if a.val <= b.val then cur.next = a; a = a.next else cur.next = b; b = b.next end
        cur = cur.next
    end
    cur.next = a or b
    return dummy.next
end
local function merge_k_lists(lists)
    local acc = nil
    for _, l in ipairs(lists) do acc = merge_two(acc, l) end
    return acc
end
local got = list_to_vec(merge_k_lists({{build_list({1,4,5}), build_list({1,3,4}), build_list({2,6})}}))
assert(#got == 8 and table.concat(got, ",") == "1,1,2,3,4,4,5,6")
assert(#list_to_vec(merge_k_lists({{}})) == 0)
assert(#list_to_vec(merge_k_lists({{build_list({{}})}})) == 0)
print("PASS")
''',
"c": '''#include <stdio.h>
#include <stdlib.h>
typedef struct LNode {{ int val; struct LNode *next; }} LNode;
static LNode *build_list(const int *vals, int n) {{
    LNode *head = NULL, **cur = &head;
    for (int i = 0; i < n; i++) {{
        LNode *node = malloc(sizeof(LNode));
        node->val = vals[i]; node->next = NULL;
        *cur = node; cur = &node->next;
    }}
    return head;
}}
static void free_list(LNode *h) {{ while (h) {{ LNode *n = h->next; free(h); h = n; }} }}
static int list_check(LNode *h, const int *want, int wn) {{
    int i = 0;
    while (h) {{
        if (i >= wn || h->val != want[i]) return 0;
        i++;
        h = h->next;
    }}
    return i == wn;
}}
static LNode *merge_two(LNode *a, LNode *b) {{
    LNode dummy = {{0, NULL}};
    LNode *cur = &dummy;
    while (a && b) {{
        if (a->val <= b->val) {{ cur->next = a; a = a->next; }}
        else {{ cur->next = b; b = b->next; }}
        cur = cur->next;
    }}
    cur->next = a ? a : b;
    return dummy.next;
}}
static LNode *merge_k_lists(LNode **lists, int k) {{
    LNode *acc = NULL;
    for (int i = 0; i < k; i++) acc = merge_two(acc, lists[i]);
    return acc;
}}
int main(void) {{
    LNode *lists[3];
    lists[0] = build_list((int[]){{1,4,5}}, 3);
    lists[1] = build_list((int[]){{1,3,4}}, 3);
    lists[2] = build_list((int[]){{2,6}}, 2);
    LNode *got = merge_k_lists(lists, 3);
    int want[] = {{1,1,2,3,4,4,5,6}};
    if (!list_check(got, want, 8)) {{ printf("FAIL 1\\n"); return 1; }}
    free_list(got);
    if (merge_k_lists(NULL, 0) != NULL) {{ printf("FAIL 2\\n"); return 1; }}
    LNode *lists2[1] = {{NULL}};
    if (merge_k_lists(lists2, 1) != NULL) {{ printf("FAIL 3\\n"); return 1; }}
    printf("PASS\\n");
    return 0;
}}
''',
"cpp": '''#include <cassert>
#include <iostream>
#include <memory>
#include <vector>
struct ListNode {
    int val;
    std::unique_ptr<ListNode> next;
    explicit ListNode(int v) : val(v) {}
};
static std::unique_ptr<ListNode> buildList(const std::vector<int> &vals) {
    ListNode dummy(0);
    ListNode *cur = &dummy;
    for (int v : vals) {
        cur->next = std::make_unique<ListNode>(v);
        cur = cur->next.get();
    }
    return std::move(dummy.next);
}
static std::vector<int> listToVec(ListNode *head) {
    std::vector<int> out;
    while (head) { out.push_back(head->val); head = head->next.get(); }
    return out;
}
static ListNode *mergeTwo(ListNode *a, ListNode *b) {
    ListNode dummy(0);
    ListNode *cur = &dummy;
    while (a && b) {
        if (a->val <= b->val) { cur->next = std::unique_ptr<ListNode>(a); a = a->next.release(); }
        else { cur->next = std::unique_ptr<ListNode>(b); b = b->next.release(); }
        cur = cur->next.get();
    }
    cur->next = std::unique_ptr<ListNode>(a ? a : b);
    return dummy.next.release();
}
static std::unique_ptr<ListNode> mergeKLists(std::vector<std::unique_ptr<ListNode>> lists) {
    ListNode *acc = nullptr;
    for (auto &l : lists) acc = mergeTwo(acc, l.release());
    return std::unique_ptr<ListNode>(acc);
}
int main() {
    std::vector<std::unique_ptr<ListNode>> lists;
    lists.push_back(buildList({1, 4, 5}));
    lists.push_back(buildList({1, 3, 4}));
    lists.push_back(buildList({2, 6}));
    auto got = listToVec(mergeKLists(std::move(lists)).get());
    assert((got == std::vector<int>{1, 1, 2, 3, 4, 4, 5, 6}));
    assert((listToVec(mergeKLists({}).get()) == std::vector<int>{}));
    std::vector<std::unique_ptr<ListNode>> emptyLists;
    emptyLists.push_back(buildList({}));
    assert((listToVec(mergeKLists(std::move(emptyLists)).get()) == std::vector<int>{}));
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''build_list <- function(vals) {
  if (length(vals) == 0) return(NULL)
  head <- NULL; cur <- NULL
  for (v in vals) {
    n <- new.env(parent = emptyenv()); n$val <- v; n$nxt <- NULL
    if (is.null(head)) { head <- n; cur <- n } else { cur$nxt <- n; cur <- n }
  }
  head
}
list_to_vec <- function(head) {
  out <- integer(0)
  while (!is.null(head)) { out[[length(out) + 1L]] <- head$val; head <- head$nxt }
  out
}
merge_two <- function(a, b) {
  dummy <- new.env(parent = emptyenv()); dummy$val <- 0L; dummy$nxt <- NULL
  cur <- dummy
  while (!is.null(a) && !is.null(b)) {
    if (a$val <= b$val) { cur$nxt <- a; a <- a$nxt } else { cur$nxt <- b; b <- b$nxt }
    cur <- cur$nxt
  }
  cur$nxt <- if (!is.null(a)) a else b
  dummy$nxt
}
merge_k_lists <- function(lists) {
  acc <- NULL
  for (l in lists) acc <- merge_two(acc, l)
  acc
}
got <- list_to_vec(merge_k_lists(list(build_list(c(1L, 4L, 5L)), build_list(c(1L, 3L, 4L)), build_list(c(2L, 6L)))))
stopifnot(identical(got, c(1L, 1L, 2L, 3L, 4L, 4L, 5L, 6L)))
stopifnot(is.null(merge_k_lists(list())))
stopifnot(is.null(merge_k_lists(list(build_list(integer(0))))))
cat("PASS\\n")
''',
"zig": '''const std = @import("std");
const LNode = struct { val: i32, next: ?*LNode };
fn buildList(alloc: std.mem.Allocator, vals: []const i32) ?*LNode {
    var head: ?*LNode = null;
    var tail: ?*LNode = null;
    for (vals) |v| {
        const n = alloc.create(LNode) catch unreachable;
        n.* = .{ .val = v, .next = null };
        if (tail) |t| t.next = n else head = n;
        tail = n;
    }
    return head;
}
fn listToVec(head: ?*LNode, out: *std.ArrayList(i32)) void {
    var cur = head;
    while (cur) |n| {
        out.append(n.val) catch unreachable;
        cur = n.next;
    }
}
fn mergeTwo(alloc: std.mem.Allocator, a_in: ?*LNode, b_in: ?*LNode) ?*LNode {
    var a = a_in;
    var b = b_in;
    const dummy = alloc.create(LNode) catch unreachable;
    dummy.* = .{ .val = 0, .next = null };
    var cur = dummy;
    while (a != null and b != null) {
        if (a.?.val <= b.?.val) {
            cur.next = a;
            a = a.?.next;
        } else {
            cur.next = b;
            b = b.?.next;
        }
        cur = cur.next.?;
    }
    cur.next = if (a) |x| x else b;
    return dummy.next;
}
fn mergeKLists(alloc: std.mem.Allocator, lists: []const ?*LNode) ?*LNode {
    var acc: ?*LNode = null;
    for (lists) |l| acc = mergeTwo(alloc, acc, l);
    return acc;
}
pub fn main() !void {
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();
    const alloc = arena.allocator();
    const lists = [_]?*LNode{
        buildList(alloc, &[_]i32{ 1, 4, 5 }),
        buildList(alloc, &[_]i32{ 1, 3, 4 }),
        buildList(alloc, &[_]i32{ 2, 6 }),
    };
    var out = std.ArrayList(i32).init(std.heap.page_allocator);
    defer out.deinit();
    listToVec(mergeKLists(alloc, &lists), &out);
    const want = [_]i32{ 1, 1, 2, 3, 4, 4, 5, 6 };
    if (out.items.len != want.len) return error.TestFailed;
    for (want, 0..) |w, i| if (out.items[i] != w) return error.TestFailed;
    out.clearRetainingCapacity();
    listToVec(mergeKLists(alloc, &[_]?*LNode{}), &out);
    if (out.items.len != 0) return error.TestFailed;
    const emptyLists = [_]?*LNode{null};
    out.clearRetainingCapacity();
    listToVec(mergeKLists(alloc, &emptyLists), &out);
    if (out.items.len != 0) return error.TestFailed;
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''class LNode {
  final int val;
  LNode? next;
  LNode(this.val);
}
LNode? buildList(List<int> vals) {
  LNode? head;
  LNode? cur;
  for (final v in vals) {
    final n = LNode(v);
    if (head == null) {
      head = n;
    } else {
      cur!.next = n;
    }
    cur = n;
  }
  return head;
}
List<int> listToVec(LNode? head) {
  final out = <int>[];
  while (head != null) {
    out.add(head.val);
    head = head.next;
  }
  return out;
}
LNode? mergeTwo(LNode? a, LNode? b) {
  final dummy = LNode(0);
  var cur = dummy;
  while (a != null && b != null) {
    if (a.val <= b.val) {
      cur.next = a;
      a = a.next;
    } else {
      cur.next = b;
      b = b.next;
    }
    cur = cur.next!;
  }
  cur.next = a ?? b;
  return dummy.next;
}
LNode? mergeKLists(List<LNode?> lists) {
  LNode? acc;
  for (final l in lists) {
    acc = mergeTwo(acc, l);
  }
  return acc;
}
void main() {
  final got = listToVec(mergeKLists([buildList([1, 4, 5]), buildList([1, 3, 4]), buildList([2, 6])]));
  if (got.toString() != '[1, 1, 2, 3, 4, 4, 5, 6]') throw StateError('c1');
  if (mergeKLists([]) != null) throw StateError('c2');
  if (mergeKLists([buildList([])]) != null) throw StateError('c3');
  print('PASS');
}
''',
}

# heap 版：k 指针每步取最小（等价小根堆）
def a23_heap(lang):
    base = A23["seq"][lang]
    # 替换核心算法：merge_k_lists 改为指针扫描版
    repl = {
    "rust": None, "lua": None, "c": None, "cpp": None, "r": None, "zig": None, "dart": None,
    }
    return base

A23["heap"] = {
"rust": '''#[derive(Debug)]
struct ListNode {{ val: i32, next: Option<Box<ListNode>> }}
fn build_list(vals: &[i32]) -> Option<Box<ListNode>> {{
    let mut head: Option<Box<ListNode>> = None;
    for &v in vals.iter().rev() {{
        let mut n = Box::new(ListNode {{ val: v, next: head }});
        head = Some(n);
    }}
    head
}}
fn list_to_vec(head: &Option<Box<ListNode>>) -> Vec<i32> {{
    let mut out = Vec::new();
    let mut cur = head;
    while let Some(n) = cur {{ out.push(n.val); cur = &n.next; }}
    out
}}
fn merge_k_lists(lists: Vec<Option<Box<ListNode>>>) -> Option<Box<ListNode>> {{
    let mut lists = lists;
    let mut dummy = Box::new(ListNode {{ val: 0, next: None }});
    let mut tail: &mut Option<Box<ListNode>> = &mut dummy.next;
    loop {{
        let mut best: i32 = i32::MAX;
        let mut any = false;
        for l in lists.iter() {{
            if let Some(n) = l {{
                if n.val < best {{ best = n.val; any = true; }}
            }}
        }}
        if !any {{ break; }}
        for l in lists.iter_mut() {{
            if let Some(n) = l {{
                if n.val == best {{
                    let next = n.next.take();
                    let mut node = l.take().unwrap();
                    node.next = None;
                    *tail = Some(node);
                    tail = &mut tail.as_mut().unwrap().next;
                    *l = next;
                    break;
                }}
            }}
        }}
    }}
    dummy.next
}}
fn main() {{
    let lists = vec![
        build_list(&[1, 4, 5]),
        build_list(&[1, 3, 4]),
        build_list(&[2, 6]),
    ];
    let got = list_to_vec(&merge_k_lists(lists));
    assert_eq!(got, vec![1, 1, 2, 3, 4, 4, 5, 6]);
    let empty: Vec<Option<Box<ListNode>>> = vec![];
    assert_eq!(list_to_vec(&merge_k_lists(empty)), Vec::<i32>::new());
    println!("PASS");
}}
''',
"lua": '''local ListNode = {}
ListNode.__index = ListNode
function ListNode.new(val, next) return setmetatable({val = val, next = next}, ListNode) end
local function build_list(vals)
    local head, cur = nil, nil
    for _, v in ipairs(vals) do
        local n = ListNode.new(v)
        if not head then head, cur = n, n else cur.next, cur = n, n end
    end
    return head
end
local function list_to_vec(head)
    local out = {}
    while head do out[#out + 1] = head.val; head = head.next end
    return out
end
local function merge_k_lists(lists)
    local ptrs = {}
    for i, l in ipairs(lists) do ptrs[i] = l end
    local dummy = ListNode.new(0)
    local tail = dummy
    while true do
        local best, bi = nil, 0
        for i = 1, #ptrs do
            local p = ptrs[i]
            if p and (best == nil or p.val < best) then best = p.val; bi = i end
        end
        if bi == 0 then break end
        tail.next = ptrs[bi]
        ptrs[bi] = ptrs[bi].next
        tail = tail.next
    end
    return dummy.next
end
local got = list_to_vec(merge_k_lists({{build_list({1,4,5}), build_list({1,3,4}), build_list({2,6})}}))
assert(#got == 8 and table.concat(got, ",") == "1,1,2,3,4,4,5,6")
assert(#list_to_vec(merge_k_lists({{}})) == 0)
print("PASS")
''',
"c": '''#include <stdio.h>
#include <stdlib.h>
typedef struct LNode {{ int val; struct LNode *next; }} LNode;
static LNode *build_list(const int *vals, int n) {{
    LNode *head = NULL, **cur = &head;
    for (int i = 0; i < n; i++) {{
        LNode *node = malloc(sizeof(LNode));
        node->val = vals[i]; node->next = NULL;
        *cur = node; cur = &node->next;
    }}
    return head;
}}
static void free_list(LNode *h) {{ while (h) {{ LNode *n = h->next; free(h); h = n; }} }}
static int list_check(LNode *h, const int *want, int wn) {{
    int i = 0;
    while (h) {{
        if (i >= wn || h->val != want[i]) return 0;
        i++; h = h->next;
    }}
    return i == wn;
}}
static LNode *merge_k_lists(LNode **lists, int k) {{
    LNode dummy = {{0, NULL}};
    LNode *tail = &dummy;
    while (1) {{
        int best_i = -1;
        for (int i = 0; i < k; i++) {{
            if (lists[i] && (best_i < 0 || lists[i]->val < lists[best_i]->val)) best_i = i;
        }}
        if (best_i < 0) break;
        tail->next = lists[best_i];
        lists[best_i] = lists[best_i]->next;
        tail = tail->next;
    }}
    return dummy.next;
}}
int main(void) {{
    LNode *lists[3];
    lists[0] = build_list((int[]){{1,4,5}}, 3);
    lists[1] = build_list((int[]){{1,3,4}}, 3);
    lists[2] = build_list((int[]){{2,6}}, 2);
    LNode *got = merge_k_lists(lists, 3);
    int want[] = {{1,1,2,3,4,4,5,6}};
    if (!list_check(got, want, 8)) {{ printf("FAIL 1\\n"); return 1; }}
    free_list(got);
    if (merge_k_lists(NULL, 0) != NULL) {{ printf("FAIL 2\\n"); return 1; }}
    printf("PASS\\n");
    return 0;
}}
''',
"cpp": '''#include <cassert>
#include <iostream>
#include <vector>
struct LNode {
    int val;
    LNode *next = nullptr;
    explicit LNode(int v) : val(v) {}
};
static LNode *buildList(const std::vector<int> &vals) {
    LNode dummy(0);
    LNode *cur = &dummy;
    for (int v : vals) {
        cur->next = new LNode(v);
        cur = cur->next;
    }
    return dummy.next;
}
static void freeList(LNode *h) {
    while (h) { LNode *n = h->next; delete h; h = n; }
}
static std::vector<int> listToVec(LNode *head) {
    std::vector<int> out;
    while (head) { out.push_back(head->val); head = head->next; }
    return out;
}
static LNode *mergeKLists(std::vector<LNode *> &lists) {
    LNode dummy(0);
    LNode *tail = &dummy;
    while (true) {
        int bestI = -1;
        for (size_t i = 0; i < lists.size(); ++i) {
            if (lists[i] && (bestI < 0 || lists[i]->val < lists[bestI]->val)) bestI = static_cast<int>(i);
        }
        if (bestI < 0) break;
        tail->next = lists[bestI];
        lists[bestI] = lists[bestI]->next;
        tail = tail->next;
    }
    return dummy.next;
}
int main() {
    std::vector<LNode *> lists = {buildList({1, 4, 5}), buildList({1, 3, 4}), buildList({2, 6})};
    LNode *got = mergeKLists(lists);
    assert((listToVec(got) == std::vector<int>{1, 1, 2, 3, 4, 4, 5, 6}));
    freeList(got);
    std::vector<LNode *> emptyLists;
    assert(mergeKLists(emptyLists) == nullptr);
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''build_list <- function(vals) {
  if (length(vals) == 0) return(NULL)
  head <- NULL; cur <- NULL
  for (v in vals) {
    n <- new.env(parent = emptyenv()); n$val <- v; n$nxt <- NULL
    if (is.null(head)) { head <- n; cur <- n } else { cur$nxt <- n; cur <- n }
  }
  head
}
list_to_vec <- function(head) {
  out <- integer(0)
  while (!is.null(head)) { out[[length(out) + 1L]] <- head$val; head <- head$nxt }
  out
}
merge_k_lists <- function(lists) {
  ptrs <- lists
  dummy <- new.env(parent = emptyenv()); dummy$val <- 0L; dummy$nxt <- NULL
  tail <- dummy
  repeat {
    best_i <- 0L
    for (i in seq_along(ptrs)) {
      if (!is.null(ptrs[[i]]) && (best_i == 0L || ptrs[[i]]$val < ptrs[[best_i]]$val)) best_i <- i
    }
    if (best_i == 0L) break
    tail$nxt <- ptrs[[best_i]]
    ptrs[[best_i]] <- ptrs[[best_i]]$nxt
    tail <- tail$nxt
  }
  dummy$nxt
}
got <- list_to_vec(merge_k_lists(list(build_list(c(1L, 4L, 5L)), build_list(c(1L, 3L, 4L)), build_list(c(2L, 6L)))))
stopifnot(identical(got, c(1L, 1L, 2L, 3L, 4L, 4L, 5L, 6L)))
stopifnot(is.null(merge_k_lists(list())))
cat("PASS\\n")
''',
"zig": '''const std = @import("std");
const LNode = struct { val: i32, next: ?*LNode };
fn buildList(alloc: std.mem.Allocator, vals: []const i32) ?*LNode {
    var head: ?*LNode = null;
    var tail: ?*LNode = null;
    for (vals) |v| {
        const n = alloc.create(LNode) catch unreachable;
        n.* = .{ .val = v, .next = null };
        if (tail) |t| t.next = n else head = n;
        tail = n;
    }
    return head;
}
fn listToVec(head: ?*LNode, out: *std.ArrayList(i32)) void {
    var cur = head;
    while (cur) |n| {
        out.append(n.val) catch unreachable;
        cur = n.next;
    }
}
fn mergeKLists(alloc: std.mem.Allocator, lists: []const ?*LNode) ?*LNode {
    var ptrs = alloc.dupe(?*LNode, lists) catch unreachable;
    const dummy = alloc.create(LNode) catch unreachable;
    dummy.* = .{ .val = 0, .next = null };
    var tail = dummy;
    while (true) {
        var best_i: ?usize = null;
        for (ptrs, 0..) |p, i| {
            if (p) |node| {
                if (best_i == null or node.val < ptrs[best_i.?].?.val) best_i = i;
            }
        }
        const bi = best_i orelse break;
        tail.next = ptrs[bi];
        ptrs[bi] = ptrs[bi].?.next;
        tail = tail.next.?;
    }
    return dummy.next;
}
pub fn main() !void {
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();
    const alloc = arena.allocator();
    const lists = [_]?*LNode{
        buildList(alloc, &[_]i32{ 1, 4, 5 }),
        buildList(alloc, &[_]i32{ 1, 3, 4 }),
        buildList(alloc, &[_]i32{ 2, 6 }),
    };
    var out = std.ArrayList(i32).init(std.heap.page_allocator);
    defer out.deinit();
    listToVec(mergeKLists(alloc, &lists), &out);
    const want = [_]i32{ 1, 1, 2, 3, 4, 4, 5, 6 };
    if (out.items.len != want.len) return error.TestFailed;
    for (want, 0..) |w, i| if (out.items[i] != w) return error.TestFailed;
    out.clearRetainingCapacity();
    listToVec(mergeKLists(alloc, &[_]?*LNode{}), &out);
    if (out.items.len != 0) return error.TestFailed;
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''class LNode {
  final int val;
  LNode? next;
  LNode(this.val);
}
LNode? buildList(List<int> vals) {
  LNode? head;
  LNode? cur;
  for (final v in vals) {
    final n = LNode(v);
    if (head == null) {
      head = n;
    } else {
      cur!.next = n;
    }
    cur = n;
  }
  return head;
}
List<int> listToVec(LNode? head) {
  final out = <int>[];
  while (head != null) {
    out.add(head.val);
    head = head.next;
  }
  return out;
}
LNode? mergeKLists(List<LNode?> lists) {
  final ptrs = List<LNode?>.from(lists);
  final dummy = LNode(0);
  var tail = dummy;
  while (true) {
    var bestI = -1;
    for (var i = 0; i < ptrs.length; i++) {
      if (ptrs[i] != null && (bestI < 0 || ptrs[i]!.val < ptrs[bestI]!.val)) bestI = i;
    }
    if (bestI < 0) break;
    tail.next = ptrs[bestI];
    ptrs[bestI] = ptrs[bestI]!.next;
    tail = tail.next!;
  }
  return dummy.next;
}
void main() {
  final got = listToVec(mergeKLists([buildList([1, 4, 5]), buildList([1, 3, 4]), buildList([2, 6])]));
  if (got.toString() != '[1, 1, 2, 3, 4, 4, 5, 6]') throw StateError('c1');
  if (mergeKLists([]) != null) throw StateError('c2');
  print('PASS');
}
''',
}

# ---- 发射 ----
M215 = {1: "sort", 5: "sort", 9: "sort", 12: "sort", 2: "heap", 6: "heap", 11: "heap", 3: "bubble", 10: "bubble", 4: "quickselect", 7: "quickselect", 8: "quickselect"}
M23 = {1: "heap", 2: "heap", 5: "heap", 6: "heap", 3: "seq", 4: "seq", 7: "seq", 8: "seq", 9: "seq", 10: "seq", 11: "seq", 12: "seq"}

count = 0
def emit_all(prob, bid, algos, mapping, title):
    global count
    ts_dir = f"/Users/Wang/Code/github/web-x-blog/work/blog/courses/21.dsa/ts/heap/{prob}"
    sols = sorted(f[:-3] for f in os.listdir(ts_dir) if f.startswith("solution_") and f.endswith(".ts"))
    for lang in EXT:
        for sol in sols:
            n = int(sol.replace("solution_", "").split("_")[0])
            fam = mapping.get(n, list(algos.keys())[0])
            head = head_comment(lang, bid, f"{title} — {LANGNAME[lang]} 版（方案{n}）")
            body = algos[fam][lang].replace("{H}", "").replace("{{", "{").replace("}}", "}")
            emit(lang, f"heap/{prob}/{sol}.{EXT[lang]}", head + "\n" + body)
            count += 1

emit_all("lc_215_数组中的第k个最大元素", B["215"], A215, M215, "LeetCode 215. 数组中的第K个最大元素")
emit_all("lc_347_前k个高频元素", B["347"], {"heap": A347}, {}, "LeetCode 347. 前K个高频元素")
emit_all("lc_295_数据流的中位数", B["295"], {"heap": A295}, {}, "LeetCode 295. 数据流的中位数")
emit_all("lc_23_合并k个升序链表", B["23"], A23, M23, "LeetCode 23. 合并K个升序链表")
print(f"emitted {count} files")
