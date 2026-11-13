#!/usr/bin/env python3
# gen_fix_n12.py — 补齐 notes/lc_116567013 PM 模式匹配 × 7 语言（4 解法）
# s1: BF v1（主串指针回退）  s2: BF v2（双循环对齐）  s3: KMP（next 表）  s4: buildNext 单测
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from langlib import emit

REL = "notes/lc_116567013_pm"
BLOG = "https://blog.csdn.net/tyro_java/article/details/116567013"
DESC = "PM 模式匹配"

# ---------- s1: BF v1 ----------
S1 = {
"rust": '''// 来源（blog）：@@BLOG@@
// LeetCode 116567013. PM — Rust 版（方案1：Brute-Force 主串指针回退）
fn match_v1(p: &[u8], t: &[u8]) -> i64 {
    let n = t.len();
    let m = p.len();
    let mut i = 0usize;
    let mut j = 0usize;
    while j < m && i < n {
        if t[i] == p[j] {
            i += 1;
            j += 1;
        } else {
            i -= j - 1; // 主串回退到本次对齐的下一位置
            j = 0;
        }
    }
    if j == m {
        (i - j) as i64
    } else {
        -1
    }
}

fn main() {
    let t = b"now is the time for all good people to come";
    let cases: Vec<(&str, i64)> = vec![
        ("people", 29),
        ("good", 24),
        ("xyz", -1),
        ("a", -1), // 边界：空文本
        ("is", 4),
    ];
    for (idx, (p, want)) in cases.iter().enumerate() {
        let text: &[u8] = if *want == -1 && *p == "a" { b"" } else { t };
        let got = match_v1(p.as_bytes(), text);
        assert_eq!(got, *want, "case {} failed: match_v1({})", idx, p);
    }
    println!("PASS");
}
''',
"lua": '''-- 来源（blog）：@@BLOG@@
-- LeetCode 116567013. PM — Lua 版（方案1：Brute-Force 主串指针回退）
local function match_v1(p, t)
    local n, m = #t, #p
    local i, j = 1, 1  -- 1 基
    while j <= m and i <= n do
        if t:sub(i, i) == p:sub(j, j) then
            i, j = i + 1, j + 1
        else
            i = i - j + 2  -- 主串回退到本次对齐的下一位置（1 基）
            j = 1
        end
    end
    if j > m then return i - j end
    return -1
end

local T = "now is the time for all good people to come"
local cases = {
    {"people", T, 29},
    {"good", T, 24},
    {"xyz", T, -1},
    {"a", "", -1},   -- 边界：空文本
    {"is", T, 4},
}
for idx, c in ipairs(cases) do
    local got = match_v1(c[1], c[2])
    assert(got == c[3], string.format("case %d failed: match_v1(%s)=%d want %d", idx, c[1], got, c[3]))
end
print("PASS")
''',
"c": '''/* 来源（blog）：@@BLOG@@
 * LeetCode 116567013. PM — C 版（方案1：Brute-Force 主串指针回退）
 */
#include <stdio.h>
#include <string.h>

static long match_v1(const char *p, const char *t) {
    long n = strlen(t), m = strlen(p);
    long i = 0, j = 0;
    while (j < m && i < n) {
        if (t[i] == p[j]) {
            i++; j++;
        } else {
            i -= j - 1; /* 主串回退到本次对齐的下一位置 */
            j = 0;
        }
    }
    return j == m ? i - j : -1;
}

int main(void) {
    const char *T = "now is the time for all good people to come";
    struct { const char *p; const char *t; long want; } cases[] = {
        {"people", T, 29},
        {"good", T, 24},
        {"xyz", T, -1},
        {"a", "", -1},   /* 边界：空文本 */
        {"is", T, 4},
    };
    for (int idx = 0; idx < 5; idx++) {
        long got = match_v1(cases[idx].p, cases[idx].t);
        if (got != cases[idx].want) {
            printf("case %d failed: match_v1(%s)=%ld want %ld\\n", idx, cases[idx].p, got, cases[idx].want);
            return 1;
        }
    }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''// 来源（blog）：@@BLOG@@
// LeetCode 116567013. PM — C++ 版（方案1：Brute-Force 主串指针回退）
#include <iostream>
#include <string>

static long long match_v1(const std::string &p, const std::string &t) {
    long long n = t.size(), m = p.size();
    long long i = 0, j = 0;
    while (j < m && i < n) {
        if (t[i] == p[j]) {
            ++i; ++j;
        } else {
            i -= j - 1; // 主串回退到本次对齐的下一位置
            j = 0;
        }
    }
    return j == m ? i - j : -1;
}

int main() {
    std::string T = "now is the time for all good people to come";
    struct Case { std::string p, t; long long want; };
    Case cases[] = {
        {"people", T, 29},
        {"good", T, 24},
        {"xyz", T, -1},
        {"a", "", -1},   // 边界：空文本
        {"is", T, 4},
    };
    for (int idx = 0; idx < 5; ++idx) {
        long long got = match_v1(cases[idx].p, cases[idx].t);
        if (got != cases[idx].want) {
            std::cout << "case " << idx << " failed" << std::endl;
            return 1;
        }
    }
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''# 来源（blog）：@@BLOG@@
# LeetCode 116567013. PM — R 版（方案1：Brute-Force 主串指针回退）
match_v1 <- function(p, t) {
  n <- nchar(t); m <- nchar(p)
  i <- 1L; j <- 1L
  while (j <= m && i <= n) {
    if (substr(t, i, i) == substr(p, j, j)) {
      i <- i + 1L; j <- j + 1L
    } else {
      i <- i - j + 2L  # 主串回退（1 基）
      j <- 1L
    }
  }
  if (j > m) return(i - j)
  -1L
}

T <- "now is the time for all good people to come"
cases <- list(
  list("people", T, 29L),
  list("good", T, 24L),
  list("xyz", T, -1L),
  list("a", "", -1L),
  list("is", T, 4L)
)
for (idx in seq_along(cases)) {
  got <- match_v1(cases[[idx]][[1]], cases[[idx]][[2]])
  stopifnot(got == cases[[idx]][[3]])
}
cat("PASS\\n")
''',
"zig": '''// 来源（blog）：@@BLOG@@
// LeetCode 116567013. PM — Zig 版（方案1：Brute-Force 主串指针回退）
const std = @import("std");

fn matchV1(p: []const u8, t: []const u8) i64 {
    const n = t.len;
    const m = p.len;
    var i: usize = 0;
    var j: usize = 0;
    while (j < m and i < n) {
        if (t[i] == p[j]) {
            i += 1;
            j += 1;
        } else {
            i = i + 1 - j; // 主串回退到本次对齐的下一位置
            j = 0;
        }
    }
    if (j == m) return @intCast(i - j);
    return -1;
}

pub fn main() !void {
    const T = "now is the time for all good people to come";
    const Case = struct { p: []const u8, t: []const u8, want: i64 };
    const cases = [_]Case{
        .{ .p = "people", .t = T, .want = 29 },
        .{ .p = "good", .t = T, .want = 24 },
        .{ .p = "xyz", .t = T, .want = -1 },
        .{ .p = "a", .t = "", .want = -1 },
        .{ .p = "is", .t = T, .want = 4 },
    };
    for (cases, 0..) |c, idx| {
        const got = matchV1(c.p, c.t);
        if (got != c.want) {
            std.debug.print("case {d} failed: matchV1({s})={d} want {d}\\n", .{ idx, c.p, got, c.want });
            return error.TestFailed;
        }
    }
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''// 来源（blog）：@@BLOG@@
// LeetCode 116567013. PM — Dart 版（方案1：Brute-Force 主串指针回退）
int matchV1(String p, String t) {
  final n = t.length, m = p.length;
  var i = 0, j = 0;
  while (j < m && i < n) {
    if (t[i] == p[j]) {
      i++; j++;
    } else {
      i -= j - 1; // 主串回退到本次对齐的下一位置
      j = 0;
    }
  }
  return j == m ? i - j : -1;
}

void main() {
  const T = 'now is the time for all good people to come';
  final cases = <List<dynamic>>[
    ['people', T, 29],
    ['good', T, 24],
    ['xyz', T, -1],
    ['a', '', -1],
    ['is', T, 4],
  ];
  for (var idx = 0; idx < cases.length; idx++) {
    final c = cases[idx];
    final got = matchV1(c[0] as String, c[1] as String);
    if (got != c[2] as int) throw StateError('case $idx failed: matchV1(${c[0]})=$got want ${c[2]}');
  }
  print('PASS');
}
''',
}

# ---------- s2: BF v2（双循环对齐） ----------
def bf_v2(tag):
    return {
"rust": '''// 来源（blog）：@@BLOG@@
// LeetCode 116567013. PM — Rust 版（方案2：Brute-Force 双循环对齐）
fn match_v2(p: &[u8], t: &[u8]) -> i64 {
    let n = t.len();
    let m = p.len();
    if m == 0 || n < m {
        return -1;
    }
    let mut i = 0usize;
    while i <= n - m {
        let mut j = 0usize;
        while j < m && t[i + j] == p[j] {
            j += 1;
        }
        if j == m {
            return i as i64;
        }
        i += 1;
    }
    -1
}

fn main() {
    let t = b"now is the time for all good people to come";
    let cases: Vec<(&str, i64)> = vec![
        ("people", 29),
        ("time", 11),
        ("all", 20),
        ("xyz", -1),
        ("a", -1),
        ("is", 4),
    ];
    for (idx, (p, want)) in cases.iter().enumerate() {
        let text: &[u8] = if *p == "a" && *want == -1 { b"" } else { t };
        let got = match_v2(p.as_bytes(), text);
        assert_eq!(got, *want, "case {} failed: match_v2({})", idx, p);
    }
    println!("PASS");
}
''',
"lua": '''-- 来源（blog）：@@BLOG@@
-- LeetCode 116567013. PM — Lua 版（方案2：Brute-Force 双循环对齐）
local function match_v2(p, t)
    local n, m = #t, #p
    for i = 1, n - m + 1 do
        local j = 1
        while j <= m and t:sub(i + j - 1, i + j - 1) == p:sub(j, j) do
            j = j + 1
        end
        if j > m then return i - 1 end
    end
    return -1
end

local T = "now is the time for all good people to come"
local cases = {
    {"people", T, 29},
    {"time", T, 11},
    {"all", T, 20},
    {"xyz", T, -1},
    {"a", "", -1},
    {"is", T, 4},
}
for idx, c in ipairs(cases) do
    local got = match_v2(c[1], c[2])
    assert(got == c[3], string.format("case %d failed: match_v2(%s)=%d want %d", idx, c[1], got, c[3]))
end
print("PASS")
''',
"c": '''/* 来源（blog）：@@BLOG@@
 * LeetCode 116567013. PM — C 版（方案2：Brute-Force 双循环对齐）
 */
#include <stdio.h>
#include <string.h>

static long match_v2(const char *p, const char *t) {
    long n = strlen(t), m = strlen(p);
    if (m == 0 || n < m) return -1;
    for (long i = 0; i <= n - m; i++) {
        long j = 0;
        while (j < m && t[i + j] == p[j]) j++;
        if (j == m) return i;
    }
    return -1;
}

int main(void) {
    const char *T = "now is the time for all good people to come";
    struct { const char *p; const char *t; long want; } cases[] = {
        {"people", T, 29}, {"time", T, 11}, {"all", T, 20},
        {"xyz", T, -1}, {"a", "", -1}, {"is", T, 4},
    };
    for (int idx = 0; idx < 6; idx++) {
        long got = match_v2(cases[idx].p, cases[idx].t);
        if (got != cases[idx].want) { printf("case %d failed\\n", idx); return 1; }
    }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''// 来源（blog）：@@BLOG@@
// LeetCode 116567013. PM — C++ 版（方案2：Brute-Force 双循环对齐）
#include <iostream>
#include <string>

static long long match_v2(const std::string &p, const std::string &t) {
    long long n = t.size(), m = p.size();
    if (m == 0 || n < m) return -1;
    for (long long i = 0; i <= n - m; ++i) {
        long long j = 0;
        while (j < m && t[i + j] == p[j]) ++j;
        if (j == m) return i;
    }
    return -1;
}

int main() {
    std::string T = "now is the time for all good people to come";
    struct Case { std::string p, t; long long want; };
    Case cases[] = {
        {"people", T, 29}, {"time", T, 11}, {"all", T, 20},
        {"xyz", T, -1}, {"a", "", -1}, {"is", T, 4},
    };
    for (int idx = 0; idx < 6; ++idx) {
        if (match_v2(cases[idx].p, cases[idx].t) != cases[idx].want) {
            std::cout << "case " << idx << " failed" << std::endl;
            return 1;
        }
    }
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''# 来源（blog）：@@BLOG@@
# LeetCode 116567013. PM — R 版（方案2：Brute-Force 双循环对齐）
match_v2 <- function(p, t) {
  n <- nchar(t); m <- nchar(p)
  if (m == 0L || n < m) return(-1L)
  for (i in 1:(n - m + 1L)) {
    j <- 1L
    while (j <= m && substr(t, i + j - 1L, i + j - 1L) == substr(p, j, j)) {
      j <- j + 1L
    }
    if (j > m) return(i - 1L)
  }
  -1L
}

T <- "now is the time for all good people to come"
cases <- list(
  list("people", T, 29L), list("time", T, 11L), list("all", T, 20L),
  list("xyz", T, -1L), list("a", "", -1L), list("is", T, 4L)
)
for (idx in seq_along(cases)) {
  got <- match_v2(cases[[idx]][[1]], cases[[idx]][[2]])
  stopifnot(got == cases[[idx]][[3]])
}
cat("PASS\\n")
''',
"zig": '''// 来源（blog）：@@BLOG@@
// LeetCode 116567013. PM — Zig 版（方案2：Brute-Force 双循环对齐）
const std = @import("std");

fn matchV2(p: []const u8, t: []const u8) i64 {
    const n = t.len;
    const m = p.len;
    if (m == 0 or n < m) return -1;
    var i: usize = 0;
    while (i <= n - m) : (i += 1) {
        var j: usize = 0;
        while (j < m and t[i + j] == p[j]) : (j += 1) {}
        if (j == m) return @intCast(i);
    }
    return -1;
}

pub fn main() !void {
    const T = "now is the time for all good people to come";
    const Case = struct { p: []const u8, t: []const u8, want: i64 };
    const cases = [_]Case{
        .{ .p = "people", .t = T, .want = 29 },
        .{ .p = "time", .t = T, .want = 11 },
        .{ .p = "all", .t = T, .want = 20 },
        .{ .p = "xyz", .t = T, .want = -1 },
        .{ .p = "a", .t = "", .want = -1 },
        .{ .p = "is", .t = T, .want = 4 },
    };
    for (cases, 0..) |c, idx| {
        const got = matchV2(c.p, c.t);
        if (got != c.want) {
            std.debug.print("case {d} failed\\n", .{idx});
            return error.TestFailed;
        }
    }
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''// 来源（blog）：@@BLOG@@
// LeetCode 116567013. PM — Dart 版（方案2：Brute-Force 双循环对齐）
int matchV2(String p, String t) {
  final n = t.length, m = p.length;
  if (m == 0 || n < m) return -1;
  for (var i = 0; i <= n - m; i++) {
    var j = 0;
    while (j < m && t[i + j] == p[j]) {
      j++;
    }
    if (j == m) return i;
  }
  return -1;
}

void main() {
  const T = 'now is the time for all good people to come';
  final cases = <List<dynamic>>[
    ['people', T, 29], ['time', T, 11], ['all', T, 20],
    ['xyz', T, -1], ['a', '', -1], ['is', T, 4],
  ];
  for (var idx = 0; idx < cases.length; idx++) {
    final c = cases[idx];
    if (matchV2(c[0] as String, c[1] as String) != c[2] as int) {
      throw StateError('case $idx failed');
    }
  }
  print('PASS');
}
''',
    }

# ---------- s3: KMP ----------
S3 = {
"rust": '''// 来源（blog）：@@BLOG@@
// LeetCode 116567013. PM — Rust 版（方案3：KMP，next 表失配大步跳跃）
fn build_next(p: &[u8]) -> Vec<i64> {
    let m = p.len();
    let mut n = vec![-1i64; m];
    let mut j: i64 = 0;
    let mut t: i64 = -1;
    while (j as usize) < m.saturating_sub(1) {
        if t < 0 || p[j as usize] == p[t as usize] {
            j += 1;
            t += 1;
            n[j as usize] = t;
        } else {
            t = n[t as usize];
        }
    }
    n
}

fn kmp_match(p: &[u8], t: &[u8]) -> i64 {
    let next = build_next(p);
    let n = t.len();
    let m = p.len();
    let mut i: i64 = 0;
    let mut j: i64 = 0;
    while j < m as i64 && i < n as i64 {
        if j < 0 || t[i as usize] == p[j as usize] {
            i += 1;
            j += 1;
        } else {
            j = next[j as usize];
        }
    }
    if j as usize == m {
        i - j
    } else {
        -1
    }
}

fn eq_arr(a: &[i64], b: &[i64]) -> bool {
    a == b
}

fn main() {
    let t = b"now is the time for all good people to come";
    let normal: Vec<(&str, i64)> = vec![("people", 29), ("all", 20), ("no", 0), ("xyz", -1), ("a", -1)];
    for (idx, (p, want)) in normal.iter().enumerate() {
        let text: &[u8] = if *p == "a" && *want == -1 { b"" } else { t };
        let got = kmp_match(p.as_bytes(), text);
        assert_eq!(got, *want, "case {} failed: kmp_match({})", idx, p);
    }
    // 重叠前缀：'aaaa' in 'aaaaa' -> 0
    assert_eq!(kmp_match(b"aaaa", b"aaaaa"), 0, "overlap case failed");
    // 回退复用：'aaab' in 'aaabaaa' -> 0
    assert_eq!(kmp_match(b"aaab", b"aaabaaa"), 0, "reuse case failed");
    // next 表
    assert!(eq_arr(&build_next(b"ababaca"), &[-1, 0, 0, 1, 2, 3, 0]), "next ababaca failed");
    assert!(eq_arr(&build_next(b"aaaa"), &[-1, 0, 1, 2]), "next aaaa failed");
    assert!(eq_arr(&build_next(b"abcd"), &[-1, 0, 0, 0]), "next abcd failed");
    println!("PASS");
}
''',
"lua": '''-- 来源（blog）：@@BLOG@@
-- LeetCode 116567013. PM — Lua 版（方案3：KMP，next 表失配大步跳跃）
local function build_next(p)
    local m = #p
    local N = {}
    for i = 1, m do N[i] = -1 end
    local J, T = 0, -1  -- 0 基逻辑游标（存储仍按 1 基下标）
    while J < m - 1 do
        if T < 0 or p:sub(J + 1, J + 1) == p:sub(T + 1, T + 1) then
            J = J + 1
            T = T + 1
            N[J + 1] = T
        else
            T = N[T + 1]
        end
    end
    return N
end

local function kmp_match(p, t)
    local N = build_next(p)
    local n, m = #t, #p
    local i, j = 1, 1
    local at = function(s, k) return s:sub(k, k) end
    while j <= m and i <= n do
        if j < 1 or at(t, i) == at(p, j) then
            i = i + 1
            j = j + 1
        else
            j = N[j] + 1  -- N 存 0 基，转 1 基
        end
    end
    if j > m then return i - j end
    return -1
end

local function eq_arr(a, b)
    if #a ~= #b then return false end
    for i = 1, #a do if a[i] ~= b[i] then return false end end
    return true
end

local T = "now is the time for all good people to come"
local cases = {
    {"people", T, 29}, {"all", T, 20}, {"no", T, 0}, {"xyz", T, -1}, {"a", "", -1},
}
for idx, c in ipairs(cases) do
    local got = kmp_match(c[1], c[2])
    assert(got == c[3], "case " .. idx .. " failed")
end
-- 特殊边界
assert(kmp_match("aaaa", "aaaaa") == 0, "overlap failed")
assert(kmp_match("aaab", "aaabaaa") == 0, "reuse failed")
-- next 表
assert(eq_arr(build_next("ababaca"), {-1, 0, 0, 1, 2, 3, 0}), "next ababaca failed")
assert(eq_arr(build_next("aaaa"), {-1, 0, 1, 2}), "next aaaa failed")
assert(eq_arr(build_next("abcd"), {-1, 0, 0, 0}), "next abcd failed")
print("PASS")
''',
"c": '''/* 来源（blog）：@@BLOG@@
 * LeetCode 116567013. PM — C 版（方案3：KMP，next 表失配大步跳跃）
 */
#include <stdio.h>
#include <string.h>

static long long N[64];

static void build_next(const char *p) {
    long long m = strlen(p);
    for (long long i = 0; i < m; i++) N[i] = -1;
    long long j = 0, t = -1;
    while (j < m - 1) {
        if (t < 0 || p[j] == p[t]) {
            j++; t++;
            N[j] = t;
        } else {
            t = N[t];
        }
    }
}

static long long kmp_match(const char *p, const char *t) {
    build_next(p);
    long long n = strlen(t), m = strlen(p);
    long long i = 0, j = 0;
    while (j < m && i < n) {
        if (j < 0 || t[i] == p[j]) {
            i++; j++;
        } else {
            j = N[j];
        }
    }
    return j == m ? i - j : -1;
}

static int eq_arr(const long long *a, const long long *b, int n) {
    for (int i = 0; i < n; i++) if (a[i] != b[i]) return 0;
    return 1;
}

int main(void) {
    const char *T = "now is the time for all good people to come";
    struct { const char *p; const char *t; long long want; } cases[] = {
        {"people", T, 29}, {"all", T, 20}, {"no", T, 0}, {"xyz", T, -1}, {"a", "", -1},
    };
    for (int idx = 0; idx < 5; idx++) {
        if (kmp_match(cases[idx].p, cases[idx].t) != cases[idx].want) {
            printf("case %d failed\\n", idx);
            return 1;
        }
    }
    if (kmp_match("aaaa", "aaaaa") != 0) { printf("overlap failed\\n"); return 1; }
    if (kmp_match("aaab", "aaabaaa") != 0) { printf("reuse failed\\n"); return 1; }

    long long w1[7] = {-1, 0, 0, 1, 2, 3, 0};
    build_next("ababaca");
    if (!eq_arr(N, w1, 7)) { printf("next ababaca failed\\n"); return 1; }
    long long w2[4] = {-1, 0, 1, 2};
    build_next("aaaa");
    if (!eq_arr(N, w2, 4)) { printf("next aaaa failed\\n"); return 1; }
    long long w3[4] = {-1, 0, 0, 0};
    build_next("abcd");
    if (!eq_arr(N, w3, 4)) { printf("next abcd failed\\n"); return 1; }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''// 来源（blog）：@@BLOG@@
// LeetCode 116567013. PM — C++ 版（方案3：KMP，next 表失配大步跳跃）
#include <iostream>
#include <string>
#include <vector>

static std::vector<long long> build_next(const std::string &p) {
    long long m = static_cast<long long>(p.size());
    std::vector<long long> N(m, -1);
    long long j = 0, t = -1;
    while (j < m - 1) {
        if (t < 0 || p[j] == p[t]) {
            ++j; ++t;
            N[j] = t;
        } else {
            t = N[t];
        }
    }
    return N;
}

static long long kmp_match(const std::string &p, const std::string &t) {
    std::vector<long long> N = build_next(p);
    long long n = t.size(), m = p.size();
    long long i = 0, j = 0;
    while (j < m && i < n) {
        if (j < 0 || t[i] == p[j]) {
            ++i; ++j;
        } else {
            j = N[j];
        }
    }
    return j == m ? i - j : -1;
}

int main() {
    std::string T = "now is the time for all good people to come";
    struct Case { std::string p, t; long long want; };
    Case cases[] = {
        {"people", T, 29}, {"all", T, 20}, {"no", T, 0}, {"xyz", T, -1}, {"a", "", -1},
    };
    for (int idx = 0; idx < 5; ++idx) {
        if (kmp_match(cases[idx].p, cases[idx].t) != cases[idx].want) {
            std::cout << "case " << idx << " failed" << std::endl;
            return 1;
        }
    }
    if (kmp_match("aaaa", "aaaaa") != 0) { std::cout << "overlap failed" << std::endl; return 1; }
    if (kmp_match("aaab", "aaabaaa") != 0) { std::cout << "reuse failed" << std::endl; return 1; }

    auto check_next = [](const std::string &p, const std::vector<long long> &want) {
        return build_next(p) == want;
    };
    if (!check_next("ababaca", {-1, 0, 0, 1, 2, 3, 0})) { std::cout << "next ababaca failed" << std::endl; return 1; }
    if (!check_next("aaaa", {-1, 0, 1, 2})) { std::cout << "next aaaa failed" << std::endl; return 1; }
    if (!check_next("abcd", {-1, 0, 0, 0})) { std::cout << "next abcd failed" << std::endl; return 1; }
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''# 来源（blog）：@@BLOG@@
# LeetCode 116567013. PM — R 版（方案3：KMP，next 表失配大步跳跃）
build_next <- function(p) {
  m <- nchar(p)
  N <- rep(-1L, m)
  J <- 0L; T <- -1L  # 0 基逻辑游标（存储按 1 基下标）
  pc <- function(k) substr(p, k, k)
  while (J < m - 1L) {
    if (T < 0L || pc(J + 1L) == pc(T + 1L)) {
      J <- J + 1L; T <- T + 1L
      N[J + 1L] <- T
    } else {
      T <- N[T + 1L]
    }
  }
  as.integer(N)
}

kmp_match <- function(p, t) {
  N <- build_next(p)
  n <- nchar(t); m <- nchar(p)
  i <- 1L; j <- 1L
  at <- function(s, k) substr(s, k, k)
  while (j <= m && i <= n) {
    if (j < 1L || at(t, i) == at(p, j)) {
      i <- i + 1L; j <- j + 1L
    } else {
      j <- N[j] + 1L  # 0 基转 1 基
    }
  }
  if (j > m) return(as.integer(i - j))
  -1L
}

eq_arr <- function(a, b) identical(as.integer(a), as.integer(b))

T <- "now is the time for all good people to come"
cases <- list(
  list("people", T, 29L), list("all", T, 20L), list("no", T, 0L),
  list("xyz", T, -1L), list("a", "", -1L)
)
for (idx in seq_along(cases)) {
  stopifnot(kmp_match(cases[[idx]][[1]], cases[[idx]][[2]]) == cases[[idx]][[3]])
}
stopifnot(kmp_match("aaaa", "aaaaa") == 0L)
stopifnot(kmp_match("aaab", "aaabaaa") == 0L)
stopifnot(eq_arr(build_next("ababaca"), c(-1, 0, 0, 1, 2, 3, 0)))
stopifnot(eq_arr(build_next("aaaa"), c(-1, 0, 1, 2)))
stopifnot(eq_arr(build_next("abcd"), c(-1, 0, 0, 0)))
cat("PASS\\n")
''',
"zig": '''// 来源（blog）：@@BLOG@@
// LeetCode 116567013. PM — Zig 版（方案3：KMP，next 表失配大步跳跃）
const std = @import("std");

fn buildNext(p: []const u8, out: []i64) void {
    const m = p.len;
    for (out[0..m]) |*x| x.* = -1;
    var j: i64 = 0;
    var t: i64 = -1;
    while (j < @as(i64, @intCast(m)) - 1) {
        if (t < 0 or p[@intCast(j)] == p[@intCast(t)]) {
            j += 1;
            t += 1;
            out[@intCast(j)] = t;
        } else {
            t = out[@intCast(t)];
        }
    }
}

fn kmpMatch(p: []const u8, t: []const u8, next_buf: []i64) i64 {
    buildNext(p, next_buf);
    const n = t.len;
    const m = p.len;
    var i: i64 = 0;
    var j: i64 = 0;
    while (j < @as(i64, @intCast(m)) and i < @as(i64, @intCast(n))) {
        if (j < 0 or t[@intCast(i)] == p[@intCast(j)]) {
            i += 1;
            j += 1;
        } else {
            j = next_buf[@intCast(j)];
        }
    }
    if (j == @as(i64, @intCast(m))) return i - j;
    return -1;
}

pub fn main() !void {
    var next_buf: [64]i64 = undefined;
    const T = "now is the time for all good people to come";
    const Case = struct { p: []const u8, t: []const u8, want: i64 };
    const cases = [_]Case{
        .{ .p = "people", .t = T, .want = 29 },
        .{ .p = "all", .t = T, .want = 20 },
        .{ .p = "no", .t = T, .want = 0 },
        .{ .p = "xyz", .t = T, .want = -1 },
        .{ .p = "a", .t = "", .want = -1 },
    };
    for (cases, 0..) |c, idx| {
        if (kmpMatch(c.p, c.t, &next_buf) != c.want) {
            std.debug.print("case {d} failed\\n", .{idx});
            return error.TestFailed;
        }
    }
    if (kmpMatch("aaaa", "aaaaa", &next_buf) != 0) return error.TestFailed;
    if (kmpMatch("aaab", "aaabaaa", &next_buf) != 0) return error.TestFailed;

    buildNext("ababaca", &next_buf);
    const w1 = [_]i64{ -1, 0, 0, 1, 2, 3, 0 };
    if (!std.mem.eql(i64, next_buf[0..7], &w1)) return error.TestFailed;
    buildNext("aaaa", &next_buf);
    const w2 = [_]i64{ -1, 0, 1, 2 };
    if (!std.mem.eql(i64, next_buf[0..4], &w2)) return error.TestFailed;
    buildNext("abcd", &next_buf);
    const w3 = [_]i64{ -1, 0, 0, 0 };
    if (!std.mem.eql(i64, next_buf[0..4], &w3)) return error.TestFailed;
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''// 来源（blog）：@@BLOG@@
// LeetCode 116567013. PM — Dart 版（方案3：KMP，next 表失配大步跳跃）
List<int> buildNext(String p) {
  final m = p.length;
  final N = List<int>.filled(m, -1);
  var j = 0, t = -1;
  while (j < m - 1) {
    if (t < 0 || p[j] == p[t]) {
      j++; t++;
      N[j] = t;
    } else {
      t = N[t];
    }
  }
  return N;
}

int kmpMatch(String p, String t) {
  final N = buildNext(p);
  final n = t.length, m = p.length;
  var i = 0, j = 0;
  while (j < m && i < n) {
    if (j < 0 || t[i] == p[j]) {
      i++; j++;
    } else {
      j = N[j];
    }
  }
  return j == m ? i - j : -1;
}

bool eqArr(List<int> a, List<int> b) {
  if (a.length != b.length) return false;
  for (var i = 0; i < a.length; i++) {
    if (a[i] != b[i]) return false;
  }
  return true;
}

void main() {
  const T = 'now is the time for all good people to come';
  final cases = <List<dynamic>>[
    ['people', T, 29], ['all', T, 20], ['no', T, 0], ['xyz', T, -1], ['a', '', -1],
  ];
  for (var idx = 0; idx < cases.length; idx++) {
    final c = cases[idx];
    if (kmpMatch(c[0] as String, c[1] as String) != c[2] as int) {
      throw StateError('case $idx failed');
    }
  }
  if (kmpMatch('aaaa', 'aaaaa') != 0) throw StateError('overlap failed');
  if (kmpMatch('aaab', 'aaabaaa') != 0) throw StateError('reuse failed');
  if (!eqArr(buildNext('ababaca'), [-1, 0, 0, 1, 2, 3, 0])) throw StateError('next ababaca failed');
  if (!eqArr(buildNext('aaaa'), [-1, 0, 1, 2])) throw StateError('next aaaa failed');
  if (!eqArr(buildNext('abcd'), [-1, 0, 0, 0])) throw StateError('next abcd failed');
  print('PASS');
}
''',
}

# ---------- s4: buildNext 单测 ----------
S4 = {
"rust": '''// 来源（blog）：@@BLOG@@
// LeetCode 116567013. PM — Rust 版（方案4：buildNext 单测）
fn build_next(p: &[u8]) -> Vec<i64> {
    let m = p.len();
    let mut n = vec![-1i64; m];
    let mut j: i64 = 0;
    let mut t: i64 = -1;
    while (j as usize) < m.saturating_sub(1) {
        if t < 0 || p[j as usize] == p[t as usize] {
            j += 1;
            t += 1;
            n[j as usize] = t;
        } else {
            t = n[t as usize];
        }
    }
    n
}

fn main() {
    assert_eq!(build_next(b"ababaca"), vec![-1, 0, 0, 1, 2, 3, 0], "ababaca");
    assert_eq!(build_next(b"aaaa"), vec![-1, 0, 1, 2], "aaaa");
    assert_eq!(build_next(b"abcabc"), vec![-1, 0, 0, 0, 1, 2], "abcabc");
    assert_eq!(build_next(b"abcd"), vec![-1, 0, 0, 0], "abcd");
    assert_eq!(build_next(b"a"), vec![-1], "a");
    println!("PASS");
}
''',
"lua": '''-- 来源（blog）：@@BLOG@@
-- LeetCode 116567013. PM — Lua 版（方案4：buildNext 单测）
local function build_next(p)
    local m = #p
    local N = {}
    for i = 1, m do N[i] = -1 end
    local J, T = 0, -1  -- 0 基逻辑游标（存储按 1 基下标）
    while J < m - 1 do
        if T < 0 or p:sub(J + 1, J + 1) == p:sub(T + 1, T + 1) then
            J = J + 1
            T = T + 1
            N[J + 1] = T
        else
            T = N[T + 1]
        end
    end
    return N
end

local function eq_arr(a, b)
    if #a ~= #b then return false end
    for i = 1, #a do if a[i] ~= b[i] then return false end end
    return true
end

assert(eq_arr(build_next("ababaca"), {-1, 0, 0, 1, 2, 3, 0}), "ababaca failed")
assert(eq_arr(build_next("aaaa"), {-1, 0, 1, 2}), "aaaa failed")
assert(eq_arr(build_next("abcabc"), {-1, 0, 0, 0, 1, 2}), "abcabc failed")
assert(eq_arr(build_next("abcd"), {-1, 0, 0, 0}), "abcd failed")
assert(eq_arr(build_next("a"), {-1}), "a failed")
print("PASS")
''',
"c": '''/* 来源（blog）：@@BLOG@@
 * LeetCode 116567013. PM — C 版（方案4：buildNext 单测）
 */
#include <stdio.h>
#include <string.h>

static long long N[64];

static void build_next(const char *p) {
    long long m = strlen(p);
    for (long long i = 0; i < m; i++) N[i] = -1;
    long long j = 0, t = -1;
    while (j < m - 1) {
        if (t < 0 || p[j] == p[t]) {
            j++; t++;
            N[j] = t;
        } else {
            t = N[t];
        }
    }
}

static int eq_arr(const long long *a, const long long *b, int n) {
    for (int i = 0; i < n; i++) if (a[i] != b[i]) return 0;
    return 1;
}

int main(void) {
    long long w1[7] = {-1, 0, 0, 1, 2, 3, 0};
    build_next("ababaca");
    if (!eq_arr(N, w1, 7)) { printf("ababaca failed\\n"); return 1; }
    long long w2[4] = {-1, 0, 1, 2};
    build_next("aaaa");
    if (!eq_arr(N, w2, 4)) { printf("aaaa failed\\n"); return 1; }
    long long w5[6] = {-1, 0, 0, 0, 1, 2};
    build_next("abcabc");
    if (!eq_arr(N, w5, 6)) { printf("abcabc failed\\n"); return 1; }
    long long w3[4] = {-1, 0, 0, 0};
    build_next("abcd");
    if (!eq_arr(N, w3, 4)) { printf("abcd failed\\n"); return 1; }
    long long w4[1] = {-1};
    build_next("a");
    if (!eq_arr(N, w4, 1)) { printf("a failed\\n"); return 1; }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''// 来源（blog）：@@BLOG@@
// LeetCode 116567013. PM — C++ 版（方案4：buildNext 单测）
#include <iostream>
#include <string>
#include <vector>

static std::vector<long long> build_next(const std::string &p) {
    long long m = static_cast<long long>(p.size());
    std::vector<long long> N(m, -1);
    long long j = 0, t = -1;
    while (j < m - 1) {
        if (t < 0 || p[j] == p[t]) {
            ++j; ++t;
            N[j] = t;
        } else {
            t = N[t];
        }
    }
    return N;
}

int main() {
    if (build_next("ababaca") != std::vector<long long>({-1, 0, 0, 1, 2, 3, 0})) { std::cout << "ababaca failed" << std::endl; return 1; }
    if (build_next("aaaa") != std::vector<long long>({-1, 0, 1, 2})) { std::cout << "aaaa failed" << std::endl; return 1; }
    if (build_next("abcabc") != std::vector<long long>({-1, 0, 0, 0, 1, 2})) { std::cout << "abcabc failed" << std::endl; return 1; }
    if (build_next("abcd") != std::vector<long long>({-1, 0, 0, 0})) { std::cout << "abcd failed" << std::endl; return 1; }
    if (build_next("a") != std::vector<long long>({-1})) { std::cout << "a failed" << std::endl; return 1; }
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''# 来源（blog）：@@BLOG@@
# LeetCode 116567013. PM — R 版（方案4：buildNext 单测）
build_next <- function(p) {
  m <- nchar(p)
  N <- rep(-1L, m)
  J <- 0L; T <- -1L  # 0 基逻辑游标（存储按 1 基下标）
  pc <- function(k) substr(p, k, k)
  while (J < m - 1L) {
    if (T < 0L || pc(J + 1L) == pc(T + 1L)) {
      J <- J + 1L; T <- T + 1L
      N[J + 1L] <- T
    } else {
      T <- N[T + 1L]
    }
  }
  as.integer(N)
}

eq_arr <- function(a, b) identical(as.integer(a), as.integer(b))

stopifnot(eq_arr(build_next("ababaca"), c(-1, 0, 0, 1, 2, 3, 0)))
stopifnot(eq_arr(build_next("aaaa"), c(-1, 0, 1, 2)))
stopifnot(eq_arr(build_next("abcabc"), c(-1, 0, 0, 0, 1, 2)))
stopifnot(eq_arr(build_next("abcd"), c(-1, 0, 0, 0)))
stopifnot(eq_arr(build_next("a"), c(-1)))
cat("PASS\\n")
''',
"zig": '''// 来源（blog）：@@BLOG@@
// LeetCode 116567013. PM — Zig 版（方案4：buildNext 单测）
const std = @import("std");

fn buildNext(p: []const u8, out: []i64) void {
    const m = p.len;
    for (out[0..m]) |*x| x.* = -1;
    var j: i64 = 0;
    var t: i64 = -1;
    while (j < @as(i64, @intCast(m)) - 1) {
        if (t < 0 or p[@intCast(j)] == p[@intCast(t)]) {
            j += 1;
            t += 1;
            out[@intCast(j)] = t;
        } else {
            t = out[@intCast(t)];
        }
    }
}

pub fn main() !void {
    var buf: [64]i64 = undefined;
    buildNext("ababaca", &buf);
    const w1 = [_]i64{ -1, 0, 0, 1, 2, 3, 0 };
    if (!std.mem.eql(i64, buf[0..7], &w1)) return error.TestFailed;
    buildNext("aaaa", &buf);
    const w2 = [_]i64{ -1, 0, 1, 2 };
    if (!std.mem.eql(i64, buf[0..4], &w2)) return error.TestFailed;
    buildNext("abcabc", &buf);
    const w5 = [_]i64{ -1, 0, 0, 0, 1, 2 };
    if (!std.mem.eql(i64, buf[0..6], &w5)) return error.TestFailed;
    buildNext("abcd", &buf);
    const w3 = [_]i64{ -1, 0, 0, 0 };
    if (!std.mem.eql(i64, buf[0..4], &w3)) return error.TestFailed;
    buildNext("a", &buf);
    const w4 = [_]i64{-1};
    if (!std.mem.eql(i64, buf[0..1], &w4)) return error.TestFailed;
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''// 来源（blog）：@@BLOG@@
// LeetCode 116567013. PM — Dart 版（方案4：buildNext 单测）
List<int> buildNext(String p) {
  final m = p.length;
  final N = List<int>.filled(m, -1);
  var j = 0, t = -1;
  while (j < m - 1) {
    if (t < 0 || p[j] == p[t]) {
      j++; t++;
      N[j] = t;
    } else {
      t = N[t];
    }
  }
  return N;
}

bool eqArr(List<int> a, List<int> b) {
  if (a.length != b.length) return false;
  for (var i = 0; i < a.length; i++) {
    if (a[i] != b[i]) return false;
  }
  return true;
}

void main() {
  if (!eqArr(buildNext('ababaca'), [-1, 0, 0, 1, 2, 3, 0])) throw StateError('ababaca failed');
  if (!eqArr(buildNext('aaaa'), [-1, 0, 1, 2])) throw StateError('aaaa failed');
  if (!eqArr(buildNext('abcabc'), [-1, 0, 0, 0, 1, 2])) throw StateError('abcabc failed');
  if (!eqArr(buildNext('abcd'), [-1, 0, 0, 0])) throw StateError('abcd failed');
  if (!eqArr(buildNext('a'), [-1])) throw StateError('a failed');
  print('PASS');
}
''',
}

EXTS = {"rust": ".rs", "lua": ".lua", "c": ".c", "cpp": ".cpp", "r": ".R", "zig": ".zig", "dart": ".dart"}

def main():
    s2 = bf_v2("")
    for sol, block in ((1, S1), (2, s2), (3, S3), (4, S4)):
        for lang, t in block.items():
            out = t.replace("@@BLOG@@", BLOG)
            emit(lang, REL + "/solution_%d___%d%s" % (sol, sol, EXTS[lang]), out)

if __name__ == "__main__":
    main()
