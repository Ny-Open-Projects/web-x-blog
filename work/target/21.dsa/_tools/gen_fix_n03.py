#!/usr/bin/env python3
# gen_fix_n03.py — 补齐 notes/lc_108673483 减治策略（二分/快速选择/多数元素）× 7 语言
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from langlib import emit

REL = "notes/lc_108673483_减治策略之heap_binarysearch_selectionsort_hea"
BLOG = "来源（blog）：https://blog.csdn.net/tyro_java/article/details/108673483"

# ---------- 方案1：二分查找 ----------
T_RUST1 = '''// @@BLOG@@
// LeetCode 108673483. 减治策略之 heap/binarysearch/selectionsort — Rust 版（方案1：二分查找）
fn binary_search(arr: &[i32], target: i32) -> i32 {
    let mut left: i64 = 0;
    let mut right = arr.len() as i64 - 1;
    while left <= right {
        let mid = ((left + right) / 2) as usize;
        if arr[mid] == target {
            return mid as i32;
        }
        if arr[mid] < target {
            left = mid as i64 + 1;
        } else {
            right = mid as i64 - 1;
        }
    }
    -1
}

fn main() {
    let cases: Vec<(Vec<i32>, i32, i32)> = vec![
        (vec![1, 3, 5, 7, 9], 5, 2),
        (vec![1, 3, 5, 7, 9], 4, -1),
        (vec![], 5, -1),
        (vec![1, 3, 5, 7, 9], 1, 0),
    ];
    for (idx, (a, t, want)) in cases.iter().enumerate() {
        let got = binary_search(a, *t);
        assert_eq!(got, *want, "case {} failed", idx);
    }
    println!("PASS");
}
'''

T_LUA1 = '''-- @@BLOG@@
-- LeetCode 108673483. 减治策略 — Lua 版（方案1：二分查找）
local function binary_search(arr, target)
    local left, right = 1, #arr
    while left <= right do
        local mid = math.floor((left + right) / 2)
        if arr[mid] == target then return mid - 1 end
        if arr[mid] < target then left = mid + 1 else right = mid - 1 end
    end
    return -1
end

local cases = {
    {{1, 3, 5, 7, 9}, 5, 2},
    {{1, 3, 5, 7, 9}, 4, -1},
    {{}, 5, -1},
    {{1, 3, 5, 7, 9}, 1, 0},
}
for idx, c in ipairs(cases) do
    local got = binary_search(c[1], c[2])
    assert(got == c[3], string.format("case %d failed: got %d want %d", idx, got, c[3]))
end
print("PASS")
'''

T_C1 = '''/* @@BLOG@@
 * LeetCode 108673483. 减治策略 — C 版（方案1：二分查找）
 */
#include <stdio.h>

static int binary_search(const int *arr, int n, int target) {
    int left = 0, right = n - 1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (arr[mid] == target) return mid;
        if (arr[mid] < target) left = mid + 1;
        else right = mid - 1;
    }
    return -1;
}

int main(void) {
    int a[5] = {1, 3, 5, 7, 9};
    if (binary_search(a, 5, 5) != 2) { printf("case 0 failed\\n"); return 1; }
    if (binary_search(a, 5, 4) != -1) { printf("case 1 failed\\n"); return 1; }
    if (binary_search(a, 0, 5) != -1) { printf("case 2 failed\\n"); return 1; }
    if (binary_search(a, 5, 1) != 0) { printf("case 3 failed\\n"); return 1; }
    printf("PASS\\n");
    return 0;
}
'''

T_CPP1 = '''// @@BLOG@@
// LeetCode 108673483. 减治策略 — C++ 版（方案1：二分查找）
#include <iostream>
#include <vector>

static int binary_search(const std::vector<int> &arr, int target) {
    int left = 0, right = static_cast<int>(arr.size()) - 1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (arr[mid] == target) return mid;
        if (arr[mid] < target) left = mid + 1;
        else right = mid - 1;
    }
    return -1;
}

int main() {
    std::vector<std::vector<int>> as = {
        {1, 3, 5, 7, 9}, {1, 3, 5, 7, 9}, {}, {1, 3, 5, 7, 9},
    };
    int ts[4] = {5, 4, 5, 1};
    int ws[4] = {2, -1, -1, 0};
    for (int i = 0; i < 4; ++i) {
        int got = binary_search(as[i], ts[i]);
        if (got != ws[i]) { std::cout << "case " << i << " failed" << std::endl; return 1; }
    }
    std::cout << "PASS" << std::endl;
    return 0;
}
'''

T_R1 = '''# @@BLOG@@
# LeetCode 108673483. 减治策略 — R 版（方案1：二分查找）
binary_search <- function(arr, target) {
  left <- 1L
  right <- length(arr)
  while (left <= right) {
    mid <- as.integer((left + right) %/% 2)
    if (arr[mid] == target) return(as.integer(mid - 1L))
    if (arr[mid] < target) left <- mid + 1L else right <- mid - 1L
  }
  -1L
}

cases <- list(
  list(c(1L, 3L, 5L, 7L, 9L), 5L, 2L),
  list(c(1L, 3L, 5L, 7L, 9L), 4L, -1L),
  list(c(), 5L, -1L),
  list(c(1L, 3L, 5L, 7L, 9L), 1L, 0L)
)
for (idx in seq_along(cases)) {
  got <- binary_search(cases[[idx]][[1]], cases[[idx]][[2]])
  stopifnot(got == cases[[idx]][[3]])
}
cat("PASS\\n")
'''

T_ZIG1 = '''// @@BLOG@@
// LeetCode 108673483. 减治策略 — Zig 版（方案1：二分查找）
const std = @import("std");

fn binarySearch(arr: []const i32, target: i32) i32 {
    var left: usize = 0;
    var right: usize = arr.len;
    while (left < right) {
        const mid = left + (right - left) / 2;
        if (arr[mid] == target) return @intCast(mid);
        if (arr[mid] < target) left = mid + 1 else right = mid;
    }
    return -1;
}

pub fn main() !void {
    const a = [_]i32{ 1, 3, 5, 7, 9 };
    const empty = [_]i32{};
    const Case = struct { arr: []const i32, t: i32, want: i32 };
    const cases = [_]Case{
        .{ .arr = &a, .t = 5, .want = 2 },
        .{ .arr = &a, .t = 4, .want = -1 },
        .{ .arr = &empty, .t = 5, .want = -1 },
        .{ .arr = &a, .t = 1, .want = 0 },
    };
    for (cases, 0..) |c, idx| {
        const got = binarySearch(c.arr, c.t);
        if (got != c.want) {
            std.debug.print("case {d} failed: got {d} want {d}\\n", .{ idx, got, c.want });
            return error.TestFailed;
        }
    }
    std.debug.print("PASS\\n", .{});
}
'''

T_DART1 = '''// @@BLOG@@
// LeetCode 108673483. 减治策略 — Dart 版（方案1：二分查找）
int binarySearch(List<int> arr, int target) {
  var left = 0, right = arr.length - 1;
  while (left <= right) {
    final mid = left + (right - left) ~/ 2;
    if (arr[mid] == target) return mid;
    if (arr[mid] < target) {
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }
  return -1;
}

void main() {
  final cases = <List<int>, List<int>>{
    // arr -> [target, want]
  };
  final arrs = <List<int>>[
    [1, 3, 5, 7, 9],
    [1, 3, 5, 7, 9],
    <int>[],
    [1, 3, 5, 7, 9],
  ];
  final ts = <int>[5, 4, 5, 1];
  final ws = <int>[2, -1, -1, 0];
  for (var i = 0; i < 4; i++) {
    final got = binarySearch(arrs[i], ts[i]);
    if (got != ws[i]) throw StateError('case $i failed: got $got want ${ws[i]}');
  }
  print('PASS');
}
'''

# ---------- 方案2：快速选择 ----------
T_RUST2 = '''// @@BLOG@@
// LeetCode 108673483. 减治策略 — Rust 版（方案2：快速选择求第 k 小）
fn select(a: &mut Vec<i32>, lo: usize, hi: usize, k: usize) -> i32 {
    if lo == hi {
        return a[lo];
    }
    let pivot = a[hi];
    let mut i = lo;
    for j in lo..hi {
        if a[j] <= pivot {
            a.swap(i, j);
            i += 1;
        }
    }
    a.swap(i, hi);
    if i == k {
        a[i]
    } else if i > k {
        select(a, lo, i - 1, k)
    } else {
        select(a, i + 1, hi, k)
    }
}

fn quick_select(arr: &[i32], k: usize) -> i32 {
    let mut a = arr.to_vec();
    let n = a.len();
    select(&mut a, 0, n - 1, k)
}

fn main() {
    let base = vec![3, 1, 4, 1, 5, 9, 2, 6];
    let cases: Vec<(usize, i32)> = vec![(2, 2), (3, 3), (0, 1), (7, 9)];
    for (idx, (k, want)) in cases.iter().enumerate() {
        let got = quick_select(&base, *k);
        assert_eq!(got, *want, "case {} failed", idx);
    }
    println!("PASS");
}
'''

T_LUA2 = '''-- @@BLOG@@
-- LeetCode 108673483. 减治策略 — Lua 版（方案2：快速选择求第 k 小，k 从 0 起）
local function select_k(a, lo, hi, k)
    if lo == hi then return a[lo] end
    local pivot = a[hi]
    local i = lo
    for j = lo, hi - 1 do
        if a[j] <= pivot then
            a[i], a[j] = a[j], a[i]
            i = i + 1
        end
    end
    a[i], a[hi] = a[hi], a[i]
    if i == k then return a[i] end
    if i > k then return select_k(a, lo, i - 1, k) end
    return select_k(a, i + 1, hi, k)
end

local function quick_select(arr, k)
    local a = {}
    for i, v in ipairs(arr) do a[i] = v end
    return select_k(a, 1, #a, k + 1)  -- 内部 1 基
end

local base = {3, 1, 4, 1, 5, 9, 2, 6}
local cases = {{2, 2}, {3, 3}, {0, 1}, {7, 9}}
for idx, c in ipairs(cases) do
    local got = quick_select(base, c[1])
    assert(got == c[2], string.format("case %d failed: got %d want %d", idx, got, c[2]))
end
print("PASS")
'''

T_C2 = '''/* @@BLOG@@
 * LeetCode 108673483. 减治策略 — C 版（方案2：快速选择求第 k 小，k 从 0 起）
 */
#include <stdio.h>

static int select_k(int *a, int lo, int hi, int k) {
    if (lo == hi) return a[lo];
    int pivot = a[hi];
    int i = lo;
    for (int j = lo; j < hi; j++) {
        if (a[j] <= pivot) {
            int t = a[i]; a[i] = a[j]; a[j] = t;
            i++;
        }
    }
    int t = a[i]; a[i] = a[hi]; a[hi] = t;
    if (i == k) return a[i];
    if (i > k) return select_k(a, lo, i - 1, k);
    return select_k(a, i + 1, hi, k);
}

int main(void) {
    int base[8] = {3, 1, 4, 1, 5, 9, 2, 6};
    int ks[4] = {2, 3, 0, 7};
    int ws[4] = {2, 3, 1, 9};
    for (int idx = 0; idx < 4; idx++) {
        int a[8];
        for (int i = 0; i < 8; i++) a[i] = base[i];
        int got = select_k(a, 0, 7, ks[idx]);
        if (got != ws[idx]) { printf("case %d failed\\n", idx); return 1; }
    }
    printf("PASS\\n");
    return 0;
}
'''

T_CPP2 = '''// @@BLOG@@
// LeetCode 108673483. 减治策略 — C++ 版（方案2：快速选择求第 k 小）
#include <iostream>
#include <vector>

static int select_k(std::vector<int> &a, int lo, int hi, int k) {
    if (lo == hi) return a[lo];
    int pivot = a[hi];
    int i = lo;
    for (int j = lo; j < hi; ++j) {
        if (a[j] <= pivot) {
            std::swap(a[i], a[j]);
            ++i;
        }
    }
    std::swap(a[i], a[hi]);
    if (i == k) return a[i];
    if (i > k) return select_k(a, lo, i - 1, k);
    return select_k(a, i + 1, hi, k);
}

int main() {
    std::vector<int> base{3, 1, 4, 1, 5, 9, 2, 6};
    int ks[4] = {2, 3, 0, 7};
    int ws[4] = {2, 3, 1, 9};
    for (int idx = 0; idx < 4; ++idx) {
        std::vector<int> a = base;
        int got = select_k(a, 0, static_cast<int>(a.size()) - 1, ks[idx]);
        if (got != ws[idx]) { std::cout << "case " << idx << " failed" << std::endl; return 1; }
    }
    std::cout << "PASS" << std::endl;
    return 0;
}
'''

T_R2 = '''# @@BLOG@@
# LeetCode 108673483. 减治策略 — R 版（方案2：快速选择求第 k 小，k 从 0 起）
select_k <- function(a, lo, hi, k) {
  if (lo == hi) return(a[[lo]])
  pivot <- a[[hi]]
  i <- lo
  for (j in lo:(hi - 1L)) {
    if (a[[j]] <= pivot) {
      tmp <- a[[i]]
      a[[i]] <- a[[j]]
      a[[j]] <- tmp
      i <- i + 1L
    }
  }
  tmp <- a[[i]]
  a[[i]] <- a[[hi]]
  a[[hi]] <- tmp
  # R 列表按引用不可变，用环境回传
  if (i == k) return(a[[i]])
  if (i > k) return(select_k_rec(a, lo, i - 1L, k))
  select_k_rec(a, i + 1L, hi, k)
}

# R 值语义：递归用环境包装保存数组
select_k_rec <- function(a, lo, hi, k) select_k(a, lo, hi, k)

quick_select <- function(arr, k) {
  e <- new.env(parent = emptyenv())
  e$a <- as.list(arr)
  get_k <- function(lo, hi, k) {
    if (lo == hi) return(e$a[[lo]])
    pivot <- e$a[[hi]]
    i <- lo
    for (j in lo:(hi - 1L)) {
      if (e$a[[j]] <= pivot) {
        tmp <- e$a[[i]]
        e$a[[i]] <- e$a[[j]]
        e$a[[j]] <- tmp
        i <- i + 1L
      }
    }
    tmp <- e$a[[i]]
    e$a[[i]] <- e$a[[hi]]
    e$a[[hi]] <- tmp
    if (i == k) return(e$a[[i]])
    if (i > k) return(get_k(lo, i - 1L, k))
    get_k(i + 1L, hi, k)
  }
  get_k(1L, length(e$a), k + 1L)
}

base <- c(3L, 1L, 4L, 1L, 5L, 9L, 2L, 6L)
cases <- list(list(2L, 2L), list(3L, 3L), list(0L, 1L), list(7L, 9L))
for (idx in seq_along(cases)) {
  got <- quick_select(base, cases[[idx]][[1]])
  stopifnot(got == cases[[idx]][[2]])
}
cat("PASS\\n")
'''

T_ZIG2 = '''// @@BLOG@@
// LeetCode 108673483. 减治策略 — Zig 版（方案2：快速选择求第 k 小）
const std = @import("std");

fn selectK(a: []i32, lo: usize, hi: usize, k: usize) i32 {
    if (lo == hi) return a[lo];
    const pivot = a[hi];
    var i = lo;
    var j = lo;
    while (j < hi) : (j += 1) {
        if (a[j] <= pivot) {
            const t = a[i];
            a[i] = a[j];
            a[j] = t;
            i += 1;
        }
    }
    const t = a[i];
    a[i] = a[hi];
    a[hi] = t;
    if (i == k) return a[i];
    if (i > k) return selectK(a, lo, i - 1, k);
    return selectK(a, i + 1, hi, k);
}

pub fn main() !void {
    var gpa = std.heap.GeneralPurposeAllocator(.{}){};
    defer _ = gpa.deinit();
    const allocator = gpa.allocator();

    const base = [_]i32{ 3, 1, 4, 1, 5, 9, 2, 6 };
    const Case = struct { k: usize, want: i32 };
    const cases = [_]Case{
        .{ .k = 2, .want = 2 },
        .{ .k = 3, .want = 3 },
        .{ .k = 0, .want = 1 },
        .{ .k = 7, .want = 9 },
    };
    for (cases, 0..) |c, idx| {
        const a = try allocator.dupe(i32, &base);
        defer allocator.free(a);
        const got = selectK(a, 0, a.len - 1, c.k);
        if (got != c.want) {
            std.debug.print("case {d} failed: got {d} want {d}\\n", .{ idx, got, c.want });
            return error.TestFailed;
        }
    }
    std.debug.print("PASS\\n", .{});
}
'''

T_DART2 = '''// @@BLOG@@
// LeetCode 108673483. 减治策略 — Dart 版（方案2：快速选择求第 k 小）
int selectK(List<int> a, int lo, int hi, int k) {
  if (lo == hi) return a[lo];
  final pivot = a[hi];
  var i = lo;
  for (var j = lo; j < hi; j++) {
    if (a[j] <= pivot) {
      final t = a[i];
      a[i] = a[j];
      a[j] = t;
      i++;
    }
  }
  final t = a[i];
  a[i] = a[hi];
  a[hi] = t;
  if (i == k) return a[i];
  if (i > k) return selectK(a, lo, i - 1, k);
  return selectK(a, i + 1, hi, k);
}

int quickSelect(List<int> arr, int k) {
  final a = List<int>.from(arr);
  return selectK(a, 0, a.length - 1, k);
}

void main() {
  final base = <int>[3, 1, 4, 1, 5, 9, 2, 6];
  final ks = <int>[2, 3, 0, 7];
  final ws = <int>[2, 3, 1, 9];
  for (var idx = 0; idx < 4; idx++) {
    final got = quickSelect(base, ks[idx]);
    if (got != ws[idx]) throw StateError('case $idx failed: got $got want ${ws[idx]}');
  }
  print('PASS');
}
'''

# ---------- 方案3：多数元素（Boyer-Moore 投票） ----------
T_RUST3 = '''// @@BLOG@@
// LeetCode 108673483. 减治策略 — Rust 版（方案3：Boyer-Moore 摩尔投票求多数元素）
fn majority_element(arr: &[i32]) -> i32 {
    let mut candidate: Option<i32> = None;
    let mut count = 0;
    for &num in arr {
        if count == 0 {
            candidate = Some(num);
        }
        if Some(num) == candidate {
            count += 1;
        } else {
            count -= 1;
        }
    }
    let cand = candidate.unwrap();
    let mut cnt = 0;
    for &num in arr {
        if num == cand {
            cnt += 1;
        }
    }
    if cnt > arr.len() as i32 / 2 {
        return cand;
    }
    -1
}

fn main() {
    let cases: Vec<(Vec<i32>, i32)> = vec![
        (vec![2, 2, 1, 1, 1, 1, 1], 1),
        (vec![1, 2, 3], -1),
        (vec![3, 3, 4], 3),
    ];
    for (idx, (a, want)) in cases.iter().enumerate() {
        let got = majority_element(a);
        assert_eq!(got, *want, "case {} failed", idx);
    }
    println!("PASS");
}
'''

T_LUA3 = '''-- @@BLOG@@
-- LeetCode 108673483. 减治策略 — Lua 版（方案3：Boyer-Moore 摩尔投票求多数元素）
local function majority_element(arr)
    local candidate = nil
    local count = 0
    for _, num in ipairs(arr) do
        if count == 0 then candidate = num end
        if num == candidate then count = count + 1 else count = count - 1 end
    end
    local cnt = 0
    for _, num in ipairs(arr) do
        if num == candidate then cnt = cnt + 1 end
    end
    if cnt > math.floor(#arr / 2) then return candidate end
    return -1
end

local cases = {
    {{2, 2, 1, 1, 1, 1, 1}, 1},
    {{1, 2, 3}, -1},
    {{3, 3, 4}, 3},
}
for idx, c in ipairs(cases) do
    local got = majority_element(c[1])
    assert(got == c[2], string.format("case %d failed: got %d want %d", idx, got, c[2]))
end
print("PASS")
'''

T_C3 = '''/* @@BLOG@@
 * LeetCode 108673483. 减治策略 — C 版（方案3：Boyer-Moore 摩尔投票求多数元素）
 */
#include <stdio.h>

static int majority_element(const int *arr, int n) {
    int candidate = 0;
    int count = 0;
    for (int i = 0; i < n; i++) {
        if (count == 0) candidate = arr[i];
        if (arr[i] == candidate) count++;
        else count--;
    }
    int cnt = 0;
    for (int i = 0; i < n; i++) if (arr[i] == candidate) cnt++;
    if (cnt > n / 2) return candidate;
    return -1;
}

int main(void) {
    int a0[7] = {2, 2, 1, 1, 1, 1, 1};
    int a1[3] = {1, 2, 3};
    int a2[3] = {3, 3, 4};
    if (majority_element(a0, 7) != 1) { printf("case 0 failed\\n"); return 1; }
    if (majority_element(a1, 3) != -1) { printf("case 1 failed\\n"); return 1; }
    if (majority_element(a2, 3) != 3) { printf("case 2 failed\\n"); return 1; }
    printf("PASS\\n");
    return 0;
}
'''

T_CPP3 = '''// @@BLOG@@
// LeetCode 108673483. 减治策略 — C++ 版（方案3：Boyer-Moore 摩尔投票求多数元素）
#include <iostream>
#include <vector>

static int majority_element(const std::vector<int> &arr) {
    int candidate = 0;
    int count = 0;
    for (int num : arr) {
        if (count == 0) candidate = num;
        if (num == candidate) ++count;
        else --count;
    }
    int cnt = 0;
    for (int num : arr) if (num == candidate) ++cnt;
    if (cnt > static_cast<int>(arr.size()) / 2) return candidate;
    return -1;
}

int main() {
    std::vector<std::vector<int>> as = {
        {2, 2, 1, 1, 1, 1, 1},
        {1, 2, 3},
        {3, 3, 4},
    };
    int ws[3] = {1, -1, 3};
    for (int i = 0; i < 3; ++i) {
        int got = majority_element(as[i]);
        if (got != ws[i]) { std::cout << "case " << i << " failed" << std::endl; return 1; }
    }
    std::cout << "PASS" << std::endl;
    return 0;
}
'''

T_R3 = '''# @@BLOG@@
# LeetCode 108673483. 减治策略 — R 版（方案3：Boyer-Moore 摩尔投票求多数元素）
majority_element <- function(arr) {
  candidate <- NULL
  count <- 0L
  for (num in arr) {
    if (count == 0L) candidate <- num
    if (num == candidate) count <- count + 1L else count <- count - 1L
  }
  cnt <- sum(arr == candidate)
  if (cnt > length(arr) %/% 2L) return(as.integer(candidate))
  -1L
}

cases <- list(
  list(c(2L, 2L, 1L, 1L, 1L, 1L, 1L), 1L),
  list(c(1L, 2L, 3L), -1L),
  list(c(3L, 3L, 4L), 3L)
)
for (idx in seq_along(cases)) {
  got <- majority_element(cases[[idx]][[1]])
  stopifnot(got == cases[[idx]][[2]])
}
cat("PASS\\n")
'''

T_ZIG3 = '''// @@BLOG@@
// LeetCode 108673483. 减治策略 — Zig 版（方案3：Boyer-Moore 摩尔投票求多数元素）
const std = @import("std");

fn majorityElement(arr: []const i32) i32 {
    var candidate: i32 = 0;
    var count: i32 = 0;
    for (arr) |num| {
        if (count == 0) {
            candidate = num;
        }
        if (num == candidate) {
            count += 1;
        } else {
            count -= 1;
        }
    }
    var cnt: i32 = 0;
    for (arr) |num| {
        if (num == candidate) cnt += 1;
    }
    if (cnt > @divTrunc(@as(i32, @intCast(arr.len)), 2)) return candidate;
    return -1;
}

pub fn main() !void {
    const Case = struct { arr: []const i32, want: i32 };
    const cases = [_]Case{
        .{ .arr = &[_]i32{ 2, 2, 1, 1, 1, 1, 1 }, .want = 1 },
        .{ .arr = &[_]i32{ 1, 2, 3 }, .want = -1 },
        .{ .arr = &[_]i32{ 3, 3, 4 }, .want = 3 },
    };
    for (cases, 0..) |c, idx| {
        const got = majorityElement(c.arr);
        if (got != c.want) {
            std.debug.print("case {d} failed: got {d} want {d}\\n", .{ idx, got, c.want });
            return error.TestFailed;
        }
    }
    std.debug.print("PASS\\n", .{});
}
'''

T_DART3 = '''// @@BLOG@@
// LeetCode 108673483. 减治策略 — Dart 版（方案3：Boyer-Moore 摩尔投票求多数元素）
int majorityElement(List<int> arr) {
  int? candidate;
  var count = 0;
  for (final num in arr) {
    if (count == 0) candidate = num;
    if (num == candidate) {
      count++;
    } else {
      count--;
    }
  }
  var cnt = 0;
  for (final num in arr) {
    if (num == candidate) cnt++;
  }
  if (cnt > arr.length ~/ 2) return candidate!;
  return -1;
}

void main() {
  final cases = <List<int>, int>{
    [2, 2, 1, 1, 1, 1, 1]: 1,
    [1, 2, 3]: -1,
    [3, 3, 4]: 3,
  };
  var idx = 0;
  cases.forEach((arr, want) {
    final got = majorityElement(arr);
    if (got != want) throw StateError('case $idx failed: got $got want $want');
    idx++;
  });
  print('PASS');
}
'''

SOLS = {
    1: {"rust": T_RUST1, "lua": T_LUA1, "c": T_C1, "cpp": T_CPP1, "r": T_R1, "zig": T_ZIG1, "dart": T_DART1},
    2: {"rust": T_RUST2, "lua": T_LUA2, "c": T_C2, "cpp": T_CPP2, "r": T_R2, "zig": T_ZIG2, "dart": T_DART2},
    3: {"rust": T_RUST3, "lua": T_LUA3, "c": T_C3, "cpp": T_CPP3, "r": T_R3, "zig": T_ZIG3, "dart": T_DART3},
}
EXT = {"rust": ".rs", "lua": ".lua", "c": ".c", "cpp": ".cpp", "r": ".R", "zig": ".zig", "dart": ".dart"}

def main():
    for sol, langs in SOLS.items():
        for lang, t in langs.items():
            out = t.replace("@@BLOG@@", BLOG)
            emit(lang, REL + "/solution_%d___%d%s" % (sol, sol, EXT[lang]), out)

if __name__ == "__main__":
    main()
