#!/usr/bin/env python3
# gen_fix_n14.py — 补齐 notes/lc_110240695 分治策略 greatest_slice × 7 语言（5 解法）
# s1/s5: 暴力  s2: 增量  s3/s4: 分治(best/prefix/suffix/total)
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from langlib import emit

REL = "notes/lc_110240695_分治策略之greatest_slice_2-way_merge_counting"
BLOG = "来源（blog）：https://blog.csdn.net/tyro_java/article/details/110240695"

# ---------- A: 暴力（s1/s5） ----------
A = {
"rust": '''// @@BLOG@@
// LeetCode 110240695. 分治策略之 greatest slice — Rust 版（方案A：暴力枚举所有子段）
fn max_sub_array_bf(arr: &[i32]) -> i64 {
    let mut best = i64::MIN;
    for i in 0..arr.len() {
        let mut s = 0i64;
        for j in i..arr.len() {
            s += arr[j] as i64;
            if s > best {
                best = s;
            }
        }
    }
    best
}

fn main() {
    let cases: Vec<(Vec<i32>, i64)> = vec![
        (vec![-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
        (vec![1], 1),
        (vec![-1, -2, -3], -1),
        (vec![5, 4, -1, 7, 8], 23),
    ];
    for (idx, (arr, want)) in cases.iter().enumerate() {
        assert_eq!(max_sub_array_bf(arr), *want, "case {} failed", idx);
    }
    println!("PASS");
}
''',
"lua": '''-- @@BLOG@@
-- LeetCode 110240695. 分治策略之 greatest slice — Lua 版（方案A：暴力枚举所有子段）
local function max_sub_array_bf(arr)
    local best = -math.huge
    for i = 1, #arr do
        local s = 0
        for j = i, #arr do
            s = s + arr[j]
            if s > best then best = s end
        end
    end
    return best
end

local cases = {
    {{-2, 1, -3, 4, -1, 2, 1, -5, 4}, 6},
    {{1}, 1},
    {{-1, -2, -3}, -1},
    {{5, 4, -1, 7, 8}, 23},
}
for idx, c in ipairs(cases) do
    assert(max_sub_array_bf(c[1]) == c[2], "case " .. idx .. " failed")
end
print("PASS")
''',
"c": '''/* @@BLOG@@
 * LeetCode 110240695. 分治策略之 greatest slice — C 版（方案A：暴力枚举所有子段）
 */
#include <stdio.h>

static long long max_sub_array_bf(const int *arr, int n) {
    long long best = 0;
    int first = 1;
    for (int i = 0; i < n; i++) {
        long long s = 0;
        for (int j = i; j < n; j++) {
            s += arr[j];
            if (first || s > best) { best = s; first = 0; }
        }
    }
    return best;
}

int main(void) {
    int a0[9] = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
    int a1[1] = {1};
    int a2[3] = {-1, -2, -3};
    int a3[5] = {5, 4, -1, 7, 8};
    if (max_sub_array_bf(a0, 9) != 6) { printf("case 0 failed\\n"); return 1; }
    if (max_sub_array_bf(a1, 1) != 1) { printf("case 1 failed\\n"); return 1; }
    if (max_sub_array_bf(a2, 3) != -1) { printf("case 2 failed\\n"); return 1; }
    if (max_sub_array_bf(a3, 5) != 23) { printf("case 3 failed\\n"); return 1; }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''// @@BLOG@@
// LeetCode 110240695. 分治策略之 greatest slice — C++ 版（方案A：暴力枚举所有子段）
#include <iostream>
#include <vector>

static long long max_sub_array_bf(const std::vector<int> &arr) {
    long long best = 0;
    bool first = true;
    for (size_t i = 0; i < arr.size(); ++i) {
        long long s = 0;
        for (size_t j = i; j < arr.size(); ++j) {
            s += arr[j];
            if (first || s > best) { best = s; first = false; }
        }
    }
    return best;
}

int main() {
    std::vector<std::pair<std::vector<int>, long long>> cases = {
        {{-2, 1, -3, 4, -1, 2, 1, -5, 4}, 6},
        {{1}, 1},
        {{-1, -2, -3}, -1},
        {{5, 4, -1, 7, 8}, 23},
    };
    for (size_t idx = 0; idx < cases.size(); ++idx) {
        if (max_sub_array_bf(cases[idx].first) != cases[idx].second) {
            std::cout << "case " << idx << " failed" << std::endl;
            return 1;
        }
    }
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''# @@BLOG@@
# LeetCode 110240695. 分治策略之 greatest slice — R 版（方案A：暴力枚举所有子段）
max_sub_array_bf <- function(arr) {
  n <- length(arr)
  best <- NULL
  for (i in 1:n) {
    s <- 0L
    for (j in i:n) {
      s <- s + arr[j]
      if (is.null(best) || s > best) best <- s
    }
  }
  as.integer(best)
}

cases <- list(
  list(c(-2L, 1L, -3L, 4L, -1L, 2L, 1L, -5L, 4L), 6L),
  list(c(1L), 1L),
  list(c(-1L, -2L, -3L), -1L),
  list(c(5L, 4L, -1L, 7L, 8L), 23L)
)
for (idx in seq_along(cases)) {
  stopifnot(max_sub_array_bf(cases[[idx]][[1]]) == cases[[idx]][[2]])
}
cat("PASS\\n")
''',
"zig": '''// @@BLOG@@
// LeetCode 110240695. 分治策略之 greatest slice — Zig 版（方案A：暴力枚举所有子段）
const std = @import("std");

fn maxSubArrayBf(arr: []const i32) i64 {
    var best: i64 = std.math.minInt(i64);
    for (0..arr.len) |i| {
        var s: i64 = 0;
        for (i..arr.len) |j| {
            s += arr[j];
            if (s > best) best = s;
        }
    }
    return best;
}

pub fn main() !void {
    const a0 = [_]i32{ -2, 1, -3, 4, -1, 2, 1, -5, 4 };
    const a1 = [_]i32{1};
    const a2 = [_]i32{ -1, -2, -3 };
    const a3 = [_]i32{ 5, 4, -1, 7, 8 };
    const Case = struct { arr: []const i32, want: i64 };
    const cases = [_]Case{
        .{ .arr = &a0, .want = 6 },
        .{ .arr = &a1, .want = 1 },
        .{ .arr = &a2, .want = -1 },
        .{ .arr = &a3, .want = 23 },
    };
    for (cases, 0..) |c, idx| {
        if (maxSubArrayBf(c.arr) != c.want) {
            std.debug.print("case {d} failed\\n", .{idx});
            return error.TestFailed;
        }
    }
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''// @@BLOG@@
// LeetCode 110240695. 分治策略之 greatest slice — Dart 版（方案A：暴力枚举所有子段）
int maxSubArrayBf(List<int> arr) {
  var best = 0;
  var first = true;
  for (var i = 0; i < arr.length; i++) {
    var s = 0;
    for (var j = i; j < arr.length; j++) {
      s += arr[j];
      if (first || s > best) {
        best = s;
        first = false;
      }
    }
  }
  return best;
}

void main() {
  final cases = <List<int>, int>{
    [-2, 1, -3, 4, -1, 2, 1, -5, 4]: 6,
    [1]: 1,
    [-1, -2, -3]: -1,
    [5, 4, -1, 7, 8]: 23,
  };
  var idx = 0;
  cases.forEach((arr, want) {
    if (maxSubArrayBf(arr) != want) throw StateError('case $idx failed');
    idx++;
  });
  print('PASS');
}
''',
}

# ---------- B: 增量（s2） ----------
B = {
"rust": '''// @@BLOG@@
// LeetCode 110240695. 分治策略之 greatest slice — Rust 版（方案B：增量扫描）
fn max_sub_array_ic(arr: &[i32]) -> i64 {
    let n = arr.len();
    if n == 0 {
        return 0;
    }
    let mut gs = arr[0] as i64;
    for i in 0..n {
        let mut s = 0i64;
        for j in i..n {
            s += arr[j] as i64;
            if gs < s {
                gs = s;
            }
        }
    }
    gs
}

fn main() {
    assert_eq!(max_sub_array_ic(&[-2, 1, -3, 4, -1, 2, 1]), 6, "ms1");
    assert_eq!(max_sub_array_ic(&[-1, -2, -3]), -1, "ms2");
    println!("PASS");
}
''',
"lua": '''-- @@BLOG@@
-- LeetCode 110240695. 分治策略之 greatest slice — Lua 版（方案B：增量扫描）
local function max_sub_array_ic(arr)
    local n = #arr
    if n == 0 then return 0 end
    local gs = arr[1]
    for i = 1, n do
        local s = 0
        for j = i, n do
            s = s + arr[j]
            if gs < s then gs = s end
        end
    end
    return gs
end

assert(max_sub_array_ic({-2, 1, -3, 4, -1, 2, 1}) == 6, "ms1")
assert(max_sub_array_ic({-1, -2, -3}) == -1, "ms2")
print("PASS")
''',
"c": '''/* @@BLOG@@
 * LeetCode 110240695. 分治策略之 greatest slice — C 版（方案B：增量扫描）
 */
#include <stdio.h>

static long long max_sub_array_ic(const int *arr, int n) {
    if (n == 0) return 0;
    long long gs = arr[0];
    for (int i = 0; i < n; i++) {
        long long s = 0;
        for (int j = i; j < n; j++) {
            s += arr[j];
            if (gs < s) gs = s;
        }
    }
    return gs;
}

int main(void) {
    int a0[7] = {-2, 1, -3, 4, -1, 2, 1};
    int a1[3] = {-1, -2, -3};
    if (max_sub_array_ic(a0, 7) != 6) { printf("ms1 failed\\n"); return 1; }
    if (max_sub_array_ic(a1, 3) != -1) { printf("ms2 failed\\n"); return 1; }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''// @@BLOG@@
// LeetCode 110240695. 分治策略之 greatest slice — C++ 版（方案B：增量扫描）
#include <iostream>
#include <vector>

static long long max_sub_array_ic(const std::vector<int> &arr) {
    if (arr.empty()) return 0;
    long long gs = arr[0];
    for (size_t i = 0; i < arr.size(); ++i) {
        long long s = 0;
        for (size_t j = i; j < arr.size(); ++j) {
            s += arr[j];
            if (gs < s) gs = s;
        }
    }
    return gs;
}

int main() {
    if (max_sub_array_ic({-2, 1, -3, 4, -1, 2, 1}) != 6) { std::cout << "ms1 failed" << std::endl; return 1; }
    if (max_sub_array_ic({-1, -2, -3}) != -1) { std::cout << "ms2 failed" << std::endl; return 1; }
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''# @@BLOG@@
# LeetCode 110240695. 分治策略之 greatest slice — R 版（方案B：增量扫描）
max_sub_array_ic <- function(arr) {
  n <- length(arr)
  if (n == 0L) return(0L)
  gs <- arr[1]
  for (i in 1:n) {
    s <- 0L
    for (j in i:n) {
      s <- s + arr[j]
      if (gs < s) gs <- s
    }
  }
  as.integer(gs)
}

stopifnot(max_sub_array_ic(c(-2L, 1L, -3L, 4L, -1L, 2L, 1L)) == 6L)
stopifnot(max_sub_array_ic(c(-1L, -2L, -3L)) == -1L)
cat("PASS\\n")
''',
"zig": '''// @@BLOG@@
// LeetCode 110240695. 分治策略之 greatest slice — Zig 版（方案B：增量扫描）
const std = @import("std");

fn maxSubArrayIc(arr: []const i32) i64 {
    if (arr.len == 0) return 0;
    var gs: i64 = arr[0];
    for (0..arr.len) |i| {
        var s: i64 = 0;
        for (i..arr.len) |j| {
            s += arr[j];
            if (gs < s) gs = s;
        }
    }
    return gs;
}

pub fn main() !void {
    const a0 = [_]i32{ -2, 1, -3, 4, -1, 2, 1 };
    const a1 = [_]i32{ -1, -2, -3 };
    if (maxSubArrayIc(&a0) != 6) return error.TestFailed;
    if (maxSubArrayIc(&a1) != -1) return error.TestFailed;
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''// @@BLOG@@
// LeetCode 110240695. 分治策略之 greatest slice — Dart 版（方案B：增量扫描）
int maxSubArrayIc(List<int> arr) {
  if (arr.isEmpty) return 0;
  var gs = arr[0];
  for (var i = 0; i < arr.length; i++) {
    var s = 0;
    for (var j = i; j < arr.length; j++) {
      s += arr[j];
      if (gs < s) gs = s;
    }
  }
  return gs;
}

void main() {
  if (maxSubArrayIc([-2, 1, -3, 4, -1, 2, 1]) != 6) throw StateError('ms1 failed');
  if (maxSubArrayIc([-1, -2, -3]) != -1) throw StateError('ms2 failed');
  print('PASS');
}
''',
}

# ---------- C: 分治（s3/s4） ----------
C = {
"rust": '''// @@BLOG@@
// LeetCode 110240695. 分治策略之 greatest slice — Rust 版（方案C：分治 best/prefix/suffix/total）
fn max_sub_array_dc(arr: &[i32]) -> i64 {
    fn helper(arr: &[i32], lo: usize, hi: usize) -> (i64, i64, i64, i64) {
        // (best, prefix, suffix, total)
        if hi - lo == 1 {
            let v = arr[lo] as i64;
            return (v, v, v, v);
        }
        let mi = (lo + hi) / 2;
        let (l_best, l_pre, l_suf, l_sum) = helper(arr, lo, mi);
        let (r_best, r_pre, r_suf, r_sum) = helper(arr, mi, hi);
        let crossing = l_suf + r_pre;
        let best = l_best.max(r_best).max(crossing);
        let prefix = l_pre.max(l_sum + r_pre);
        let suffix = r_suf.max(r_sum + l_suf);
        let total = l_sum + r_sum;
        (best, prefix, suffix, total)
    }
    if arr.is_empty() {
        return 0;
    }
    helper(arr, 0, arr.len()).0
}

fn main() {
    assert_eq!(max_sub_array_dc(&[-2, 1, -3, 4, -1, 2, 1]), 6, "ms1");
    assert_eq!(max_sub_array_dc(&[1, 2, 3]), 6, "ms2");
    println!("PASS");
}
''',
"lua": '''-- @@BLOG@@
-- LeetCode 110240695. 分治策略之 greatest slice — Lua 版（方案C：分治 best/prefix/suffix/total）
local function max_sub_array_dc(arr)
    local n = #arr
    if n == 0 then return 0 end

    local helper
    helper = function(lo, hi)
        if hi - lo == 1 then
            local v = arr[lo + 1]  -- lo 为 0 基
            return v, v, v, v
        end
        local mi = math.floor((lo + hi) / 2)
        local l_best, l_pre, l_suf, l_sum = helper(lo, mi)
        local r_best, r_pre, r_suf, r_sum = helper(mi, hi)
        local crossing = l_suf + r_pre
        local best = math.max(l_best, r_best, crossing)
        local prefix = math.max(l_pre, l_sum + r_pre)
        local suffix = math.max(r_suf, r_sum + l_suf)
        local total = l_sum + r_sum
        return best, prefix, suffix, total
    end

    return helper(0, n)
end

assert(max_sub_array_dc({-2, 1, -3, 4, -1, 2, 1}) == 6, "ms1")
assert(max_sub_array_dc({1, 2, 3}) == 6, "ms2")
print("PASS")
''',
"c": '''/* @@BLOG@@
 * LeetCode 110240695. 分治策略之 greatest slice — C 版（方案C：分治 best/prefix/suffix/total）
 */
#include <stdio.h>

typedef struct {
    long long best, prefix, suffix, total;
} Quad;

static Quad helper(const int *arr, int lo, int hi) {
    Quad q;
    if (hi - lo == 1) {
        q.best = q.prefix = q.suffix = q.total = arr[lo];
        return q;
    }
    int mi = (lo + hi) / 2;
    Quad l = helper(arr, lo, mi);
    Quad r = helper(arr, mi, hi);
    long long crossing = l.suffix + r.prefix;
    q.best = l.best > r.best ? l.best : r.best;
    if (crossing > q.best) q.best = crossing;
    q.prefix = l.prefix > l.total + r.prefix ? l.prefix : l.total + r.prefix;
    q.suffix = r.suffix > r.total + l.suffix ? r.suffix : r.total + l.suffix;
    q.total = l.total + r.total;
    return q;
}

static long long max_sub_array_dc(const int *arr, int n) {
    if (n == 0) return 0;
    return helper(arr, 0, n).best;
}

int main(void) {
    int a0[7] = {-2, 1, -3, 4, -1, 2, 1};
    int a1[3] = {1, 2, 3};
    if (max_sub_array_dc(a0, 7) != 6) { printf("ms1 failed\\n"); return 1; }
    if (max_sub_array_dc(a1, 3) != 6) { printf("ms2 failed\\n"); return 1; }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''// @@BLOG@@
// LeetCode 110240695. 分治策略之 greatest slice — C++ 版（方案C：分治 best/prefix/suffix/total）
#include <algorithm>
#include <iostream>
#include <vector>

struct Quad {
    long long best, prefix, suffix, total;
};

static Quad helper(const std::vector<int> &arr, int lo, int hi) {
    if (hi - lo == 1) {
        long long v = arr[lo];
        return {v, v, v, v};
    }
    int mi = (lo + hi) / 2;
    Quad l = helper(arr, lo, mi);
    Quad r = helper(arr, mi, hi);
    long long crossing = l.suffix + r.prefix;
    Quad q;
    q.best = std::max({l.best, r.best, crossing});
    q.prefix = std::max(l.prefix, l.total + r.prefix);
    q.suffix = std::max(r.suffix, r.total + l.suffix);
    q.total = l.total + r.total;
    return q;
}

static long long max_sub_array_dc(const std::vector<int> &arr) {
    if (arr.empty()) return 0;
    return helper(arr, 0, static_cast<int>(arr.size())).best;
}

int main() {
    if (max_sub_array_dc({-2, 1, -3, 4, -1, 2, 1}) != 6) { std::cout << "ms1 failed" << std::endl; return 1; }
    if (max_sub_array_dc({1, 2, 3}) != 6) { std::cout << "ms2 failed" << std::endl; return 1; }
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''# @@BLOG@@
# LeetCode 110240695. 分治策略之 greatest slice — R 版（方案C：分治 best/prefix/suffix/total）
max_sub_array_dc <- function(arr) {
  n <- length(arr)
  if (n == 0L) return(0L)

  helper <- function(lo, hi) {
    if (hi - lo == 1L) {
      v <- as.integer(arr[lo + 1L])  # lo 为 0 基
      return(c(v, v, v, v))
    }
    mi <- as.integer((lo + hi) %/% 2L)
    l <- helper(lo, mi)
    r <- helper(mi, hi)
    crossing <- l[3] + r[2]
    best <- max(l[1], r[1], crossing)
    prefix <- max(l[2], l[4] + r[2])
    suffix <- max(r[3], r[4] + l[3])
    total <- l[4] + r[4]
    c(best, prefix, suffix, total)
  }

  helper(0L, n)[1]
}

stopifnot(max_sub_array_dc(c(-2L, 1L, -3L, 4L, -1L, 2L, 1L)) == 6L)
stopifnot(max_sub_array_dc(c(1L, 2L, 3L)) == 6L)
cat("PASS\\n")
''',
"zig": '''// @@BLOG@@
// LeetCode 110240695. 分治策略之 greatest slice — Zig 版（方案C：分治 best/prefix/suffix/total）
const std = @import("std");

const Quad = struct { best: i64, prefix: i64, suffix: i64, total: i64 };

fn helper(arr: []const i32, lo: usize, hi: usize) Quad {
    if (hi - lo == 1) {
        const v: i64 = arr[lo];
        return .{ .best = v, .prefix = v, .suffix = v, .total = v };
    }
    const mi = (lo + hi) / 2;
    const l = helper(arr, lo, mi);
    const r = helper(arr, mi, hi);
    const crossing = l.suffix + r.prefix;
    return .{
        .best = @max(l.best, @max(r.best, crossing)),
        .prefix = @max(l.prefix, l.total + r.prefix),
        .suffix = @max(r.suffix, r.total + l.suffix),
        .total = l.total + r.total,
    };
}

fn maxSubArrayDc(arr: []const i32) i64 {
    if (arr.len == 0) return 0;
    return helper(arr, 0, arr.len).best;
}

pub fn main() !void {
    const a0 = [_]i32{ -2, 1, -3, 4, -1, 2, 1 };
    const a1 = [_]i32{ 1, 2, 3 };
    if (maxSubArrayDc(&a0) != 6) return error.TestFailed;
    if (maxSubArrayDc(&a1) != 6) return error.TestFailed;
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''// @@BLOG@@
// LeetCode 110240695. 分治策略之 greatest slice — Dart 版（方案C：分治 best/prefix/suffix/total）
List<int> helper(List<int> arr, int lo, int hi) {
  if (hi - lo == 1) {
    final v = arr[lo];
    return [v, v, v, v];
  }
  final mi = (lo + hi) ~/ 2;
  final l = helper(arr, lo, mi);
  final r = helper(arr, mi, hi);
  final crossing = l[2] + r[1];
  final best = [l[0], r[0], crossing].reduce((a, b) => a > b ? a : b);
  final prefix = l[1] > l[3] + r[1] ? l[1] : l[3] + r[1];
  final suffix = r[2] > r[3] + l[2] ? r[2] : r[3] + l[2];
  return [best, prefix, suffix, l[3] + r[3]];
}

int maxSubArrayDc(List<int> arr) {
  if (arr.isEmpty) return 0;
  return helper(arr, 0, arr.length)[0];
}

void main() {
  if (maxSubArrayDc([-2, 1, -3, 4, -1, 2, 1]) != 6) throw StateError('ms1 failed');
  if (maxSubArrayDc([1, 2, 3]) != 6) throw StateError('ms2 failed');
  print('PASS');
}
''',
}

EXTS = {"rust": ".rs", "lua": ".lua", "c": ".c", "cpp": ".cpp", "r": ".R", "zig": ".zig", "dart": ".dart"}

def main():
    for sol, block in ((1, A), (5, A), (2, B), (3, C), (4, C)):
        for lang, t in block.items():
            emit(lang, REL + "/solution_%d___%d%s" % (sol, sol, EXTS[lang]), t.replace("@@BLOG@@", BLOG))

if __name__ == "__main__":
    main()
