#!/usr/bin/env python3
# gen_bs.py — 生成 binary_search 剩余 3 题（lc_35/lc_374/lc_69）× 7 语言
# 模板用占位符 __SRC__/__TITLE__/__BODY__，避免 f-string 与语言花括号冲突
import os
DSA = "/Users/Wang/Code/github/web-x-blog/work/blog/courses/21.dsa"
LANGS = {"rust": "rs", "lua": "lua", "c": "c", "cpp": "cpp", "r": "R", "zig": "zig", "dart": "dart"}
B35, B374, B69 = "145233077", "145238093", "145299731"

# ================= lc_35 =================
T35 = {}
T35["rust"] = '''// 来源（blog）：__SRC__
// LeetCode 35. 搜索插入位置 — Rust 版（方案1：二分查找）
fn search_insert(nums: &[i32], target: i32) -> usize {
    let (mut left, mut right) = (0usize, nums.len());
    while left < right {
        let mid = left + (right - left) / 2;
        if nums[mid] < target { left = mid + 1; } else { right = mid; }
    }
    left
}
fn main() {
    let a1 = [1, 2, 3];
    let a2 = [1, 3, 5, 6];
    let cases = [
        (&a1[..], 1, 0usize), (&a2[..], 5, 2), (&a2[..], 2, 1),
        (&a2[..], 7, 4), (&a2[..], 0, 0),
    ];
    for (nums, t, want) in cases {
        assert_eq!(search_insert(nums, t), want);
    }
    println!("PASS");
}
'''
T35["lua"] = '''-- 来源（blog）：__SRC__
-- LeetCode 35. 搜索插入位置 — Lua 版（方案1：二分查找）
local function search_insert(nums, target)
    local left, right = 1, #nums + 1
    while left < right do
        local mid = math.floor((left + right) / 2)
        if nums[mid] < target then left = mid + 1 else right = mid end
    end
    return left - 1
end
local cases = {
    {{1, 2, 3}, 1, 0}, {{1, 3, 5, 6}, 5, 2}, {{1, 3, 5, 6}, 2, 1},
    {{1, 3, 5, 6}, 7, 4}, {{1, 3, 5, 6}, 0, 0},
}
for _, c in ipairs(cases) do
    assert(search_insert(c[1], c[2]) == c[3], "case failed")
end
print("PASS")
'''
T35["c"] = '''/* 来源（blog）：__SRC__
 * LeetCode 35. 搜索插入位置 — C 版（方案1：二分查找） */
#include <stdio.h>
int search_insert(const int *nums, int n, int target) {
    int left = 0, right = n;
    while (left < right) {
        int mid = left + (right - left) / 2;
        if (nums[mid] < target) left = mid + 1; else right = mid;
    }
    return left;
}
int main(void) {
    int a1[] = {1, 2, 3}, a[] = {1, 3, 5, 6};
    struct { const int *nums; int n; int t; int want; } cs[] = {
        {a1, 3, 1, 0}, {a, 4, 5, 2}, {a, 4, 2, 1}, {a, 4, 7, 4}, {a, 4, 0, 0},
    };
    for (int i = 0; i < 5; i++)
        if (search_insert(cs[i].nums, cs[i].n, cs[i].t) != cs[i].want) { printf("FAIL %d\\n", i); return 1; }
    printf("PASS\\n");
    return 0;
}
'''
T35["cpp"] = '''// 来源（blog）：__SRC__
// LeetCode 35. 搜索插入位置 — C++ 版（方案1：二分查找）
#include <cassert>
#include <iostream>
#include <vector>
int searchInsert(const std::vector<int> &nums, int target) {
    int left = 0, right = static_cast<int>(nums.size());
    while (left < right) {
        int mid = left + (right - left) / 2;
        if (nums[mid] < target) left = mid + 1; else right = mid;
    }
    return left;
}
int main() {
    assert(searchInsert({1, 2, 3}, 1) == 0);
    assert(searchInsert({1, 3, 5, 6}, 5) == 2);
    assert(searchInsert({1, 3, 5, 6}, 2) == 1);
    assert(searchInsert({1, 3, 5, 6}, 7) == 4);
    assert(searchInsert({1, 3, 5, 6}, 0) == 0);
    std::cout << "PASS" << std::endl;
}
'''
T35["r"] = '''# 来源（blog）：__SRC__
# LeetCode 35. 搜索插入位置 — R 版（方案1：二分查找）
search_insert <- function(nums, target) {
  left <- 1L; right <- length(nums) + 1L
  while (left < right) {
    mid <- left + (right - left) %/% 2L
    if (nums[mid] < target) left <- mid + 1L else right <- mid
  }
  left - 1L
}
stopifnot(search_insert(c(1L, 2L, 3L), 1L) == 0L)
stopifnot(search_insert(c(1L, 3L, 5L, 6L), 5L) == 2L)
stopifnot(search_insert(c(1L, 3L, 5L, 6L), 2L) == 1L)
stopifnot(search_insert(c(1L, 3L, 5L, 6L), 7L) == 4L)
stopifnot(search_insert(c(1L, 3L, 5L, 6L), 0L) == 0L)
cat("PASS\\n")
'''
T35["zig"] = '''// 来源（blog）：__SRC__
// LeetCode 35. 搜索插入位置 — Zig 版（方案1：二分查找）
const std = @import("std");
fn searchInsert(nums: []const i32, target: i32) usize {
    var left: usize = 0;
    var right: usize = nums.len;
    while (left < right) {
        const mid = left + (right - left) / 2;
        if (nums[mid] < target) left = mid + 1 else right = mid;
    }
    return left;
}
pub fn main() !void {
    const a1 = [_]i32{ 1, 2, 3 };
    const a2 = [_]i32{ 1, 3, 5, 6 };
    const Case = struct { nums: []const i32, t: i32, want: usize };
    const cases = [_]Case{
        .{ .nums = &a1, .t = 1, .want = 0 },
        .{ .nums = &a2, .t = 5, .want = 2 },
        .{ .nums = &a2, .t = 2, .want = 1 },
        .{ .nums = &a2, .t = 7, .want = 4 },
        .{ .nums = &a2, .t = 0, .want = 0 },
    };
    for (cases, 0..) |c, i| {
        if (searchInsert(c.nums, c.t) != c.want) {
            std.debug.print("FAIL case {d}\\n", .{i});
            return error.TestFailed;
        }
    }
    std.debug.print("PASS\\n", .{});
}
'''
T35["dart"] = '''// 来源（blog）：__SRC__
// LeetCode 35. 搜索插入位置 — Dart 版（方案1：二分查找）
int searchInsert(List<int> nums, int target) {
  var left = 0, right = nums.length;
  while (left < right) {
    final mid = left + (right - left) ~/ 2;
    if (nums[mid] < target) {
      left = mid + 1;
    } else {
      right = mid;
    }
  }
  return left;
}
void main() {
  final r = <bool>[
    searchInsert([1, 2, 3], 1) == 0,
    searchInsert([1, 3, 5, 6], 5) == 2,
    searchInsert([1, 3, 5, 6], 2) == 1,
    searchInsert([1, 3, 5, 6], 7) == 4,
    searchInsert([1, 3, 5, 6], 0) == 0,
  ];
  if (r.any((e) => !e)) throw StateError('case failed');
  print('PASS');
}
'''

# ================= lc_374（sol1 递归 / 其余迭代） =================
def build_374(lang, rec, plan):
    src = f"https://blog.csdn.net/tyro_java/article/details/{B374}"
    title = plan + ("：递归二分（忠实 TS：左分支 rec(1, mid-1)）" if rec else "：迭代二分")
    H = {}
    H["rust"] = ('''static mut PICK: i64 = 6;
fn guess(num: i64) -> i32 {
    unsafe { if num == PICK { 0 } else if num < PICK { 1 } else { -1 } }
}
fn guess_number(n: i64) -> i64 {
__BODY__
}
fn main() {
    let cases: [(i64, i64); 4] = [(10, 6), (1, 1), (5, 3), (2, 2)];
    for (n, pick) in cases {
        unsafe { PICK = pick; }
        assert_eq!(guess_number(n), pick, "n={} pick={}", n, pick);
    }
    println!("PASS");
}
''', '''    fn rec(low: i64, high: i64) -> i64 {
        if low > high { return -1; }
        let mid = (low + high) / 2;
        match guess(mid) {
            0 => mid,
            1 => rec(mid + 1, high),
            _ => rec(1, mid - 1),
        }
    }
    rec(1, n)''', '''    let (mut low, mut high) = (1i64, n);
    while low <= high {
        let mid = (low + high) / 2;
        match guess(mid) {
            0 => return mid,
            1 => low = mid + 1,
            _ => high = mid - 1,
        }
    }
    -1''')
    H["lua"] = ('''local pick = 6
local function guess(num)
    if num == pick then return 0 end
    if num < pick then return 1 end
    return -1
end
local function guess_number(n)
__BODY__
end
local cases = {{10, 6}, {1, 1}, {5, 3}, {2, 2}}
for _, c in ipairs(cases) do
    pick = c[2]
    assert(guess_number(c[1]) == c[2], "n=" .. c[1] .. " pick=" .. c[2])
end
print("PASS")
''', '''    local function rec(low, high)
        if low > high then return -1 end
        local mid = math.floor((low + high) / 2)
        local res = guess(mid)
        if res == 0 then return mid end
        if res == 1 then return rec(mid + 1, high) end
        return rec(1, mid - 1)
    end
    return rec(1, n)''', '''    local low, high = 1, n
    while low <= high do
        local mid = math.floor((low + high) / 2)
        local res = guess(mid)
        if res == 0 then return mid end
        if res == 1 then low = mid + 1 else high = mid - 1 end
    end
    return -1''')
    H["c"] = ('''/* 来源（blog）：__SRC__
 * LeetCode 374. 猜数字大小 — C 版（__TITLE__） */
#include <stdio.h>
static long pick_v = 6;
static int guess(long num) {
    if (num == pick_v) return 0;
    return num < pick_v ? 1 : -1;
}
__BODY__
int main(void) {
    long cs[4][2] = { {10, 6}, {1, 1}, {5, 3}, {2, 2} };
    for (int i = 0; i < 4; i++) {
        pick_v = cs[i][1];
        if (guess_number(cs[i][0]) != cs[i][1]) { printf("FAIL %d\\n", i); return 1; }
    }
    printf("PASS\\n");
    return 0;
}
''', '''static long rec(long low, long high) {
    if (low > high) return -1;
    long mid = low + (high - low) / 2;
    int res = guess(mid);
    if (res == 0) return mid;
    if (res == 1) return rec(mid + 1, high);
    return rec(1, mid - 1);
}
static long guess_number(long n) { return rec(1, n); }''', '''static long guess_number(long n) {
    long low = 1, high = n;
    while (low <= high) {
        long mid = low + (high - low) / 2;
        int res = guess(mid);
        if (res == 0) return mid;
        if (res == 1) low = mid + 1; else high = mid - 1;
    }
    return -1;
}''')
    H["cpp"] = ('''// 来源（blog）：__SRC__
// LeetCode 374. 猜数字大小 — C++ 版（__TITLE__）
#include <cassert>
#include <iostream>
static long pick_v = 6;
static int guess(long num) {
    if (num == pick_v) return 0;
    return num < pick_v ? 1 : -1;
}
__BODY__
int main() {
    long cs[4][2] = {{10, 6}, {1, 1}, {5, 3}, {2, 2}};
    for (auto &c : cs) {
        pick_v = c[1];
        assert(guessNumber(c[0]) == c[1]);
    }
    std::cout << "PASS" << std::endl;
}
''', '''static long rec(long low, long high) {
    if (low > high) return -1;
    long mid = low + (high - low) / 2;
    int res = guess(mid);
    if (res == 0) return mid;
    if (res == 1) return rec(mid + 1, high);
    return rec(1, mid - 1);
}
static long guessNumber(long n) { return rec(1, n); }''', '''static long guessNumber(long n) {
    long low = 1, high = n;
    while (low <= high) {
        long mid = low + (high - low) / 2;
        int res = guess(mid);
        if (res == 0) return mid;
        if (res == 1) low = mid + 1; else high = mid - 1;
    }
    return -1;
}''')
    H["r"] = ('''# 来源（blog）：__SRC__
# LeetCode 374. 猜数字大小 — R 版（__TITLE__）
pick_v <- 6L
guess <- function(num) if (num == pick_v) 0L else if (num < pick_v) 1L else -1L
guess_number <- function(n) {
__BODY__
}
cs <- matrix(c(10L, 6L, 1L, 1L, 5L, 3L, 2L, 2L), ncol = 2L, byrow = TRUE)
for (i in seq_len(nrow(cs))) {
  pick_v <<- cs[i, 2L]
  stopifnot(guess_number(cs[i, 1L]) == cs[i, 2L])
}
cat("PASS\\n")
''', '''  rec <- function(low, high) {
    if (low > high) return(-1L)
    mid <- low + (high - low) %/% 2L
    res <- guess(mid)
    if (res == 0L) return(mid)
    if (res == 1L) return(rec(mid + 1L, high))
    rec(1L, mid - 1L)
  }
  rec(1L, n)''', '''  low <- 1L; high <- n
  while (low <= high) {
    mid <- low + (high - low) %/% 2L
    res <- guess(mid)
    if (res == 0L) return(mid)
    if (res == 1L) low <- mid + 1L else high <- mid - 1L
  }
  -1L''')
    H["zig"] = ('''// 来源（blog）：__SRC__
// LeetCode 374. 猜数字大小 — Zig 版（__TITLE__）
const std = @import("std");
var pick: i64 = 6;
fn guess(num: i64) i32 {
    if (num == pick) return 0;
    return if (num < pick) 1 else -1;
}
fn rec(low: i64, high: i64) i64 {
    if (low > high) return -1;
    const mid = low + @divTrunc(high - low, 2);
    return switch (guess(mid)) {
        0 => mid,
        1 => rec(mid + 1, high),
        else => rec(1, mid - 1),
    };
}
fn guessNumber(n: i64) i64 {
__BODY__
}
pub fn main() !void {
    const cases = [_][2]i64{ .{ 10, 6 }, .{ 1, 1 }, .{ 5, 3 }, .{ 2, 2 } };
    for (cases) |c| {
        pick = c[1];
        if (guessNumber(c[0]) != c[1]) {
            std.debug.print("FAIL n={d} pick={d}\\n", .{ c[0], c[1] });
            return error.TestFailed;
        }
    }
    std.debug.print("PASS\\n", .{});
}
''', '''    rec(1, n)''', '''    var low: i64 = 1;
    var high: i64 = n;
    while (low <= high) {
        const mid = low + @divTrunc(high - low, 2);
        switch (guess(mid)) {
            0 => return mid,
            1 => { low = mid + 1; },
            else => { high = mid - 1; },
        }
    }
    return -1;''')
    H["dart"] = ('''// 来源（blog）：__SRC__
// LeetCode 374. 猜数字大小 — Dart 版（__TITLE__）
var pick = 6;
int guess(int num) {
  if (num == pick) return 0;
  return num < pick ? 1 : -1;
}
__BODY__
void main() {
  final cases = [
    [10, 6],
    [1, 1],
    [5, 3],
    [2, 2],
  ];
  for (final c in cases) {
    pick = c[1];
    if (guessNumber(c[0]) != c[1]) throw StateError('n=${c[0]} pick=${c[1]}');
  }
  print('PASS');
}
''', '''int rec(int low, int high) {
  if (low > high) return -1;
  final mid = low + (high - low) ~/ 2;
  final res = guess(mid);
  if (res == 0) return mid;
  if (res == 1) return rec(mid + 1, high);
  return rec(1, mid - 1);
}
int guessNumber(int n) => rec(1, n);''', '''int guessNumber(int n) {
  var low = 1, high = n;
  while (low <= high) {
    final mid = low + (high - low) ~/ 2;
    final res = guess(mid);
    if (res == 0) return mid;
    if (res == 1) { low = mid + 1; } else { high = mid - 1; }
  }
  return -1;
}''')
    frame, rec_body, iter_body = H[lang]
    body = rec_body if rec else iter_body
    out = frame.replace("__BODY__", body).replace("__SRC__", src).replace("__TITLE__", title)
    if lang in ("rust", "lua"):
        head = {"rust": f"// 来源（blog）：{src}\n// LeetCode 374. 猜数字大小 — Rust 版（{title}）\n",
                "lua": f"-- 来源（blog）：{src}\n-- LeetCode 374. 猜数字大小 — Lua 版（{title}）\n"}[lang]
        out = head + out
    return out

# ================= lc_69（4 种算法） =================
def build_69(lang, kind, plan):
    src = f"https://blog.csdn.net/tyro_java/article/details/{B69}"
    names = {"bs_exact": plan + "：二分（精确区间判断）", "bs_ans": plan + "：二分（保留 ans）",
             "newton": plan + "：牛顿迭代", "bs_hi": plan + "：二分（返回 hi）"}
    title = names[kind]
    B = {}
    B["rust"] = {
      "bs_exact": '''    if x < 2 { return x; }
    let (mut lo, mut hi) = (1i64, x / 2);
    while lo <= hi {
        let m = lo + (hi - lo) / 2;
        if m * m <= x && x < (m + 1) * (m + 1) { return m; }
        else if m * m > x { hi = m - 1; } else { lo = m + 1; }
    }
    lo''',
      "bs_ans": '''    let (mut lo, mut hi, mut ans) = (0i64, x, 0i64);
    while lo <= hi {
        let m = lo + (hi - lo) / 2;
        if m * m <= x { ans = m; lo = m + 1; } else { hi = m - 1; }
    }
    ans''',
      "newton": '''    if x < 2 { return x; }
    let mut r = x;
    while r * r > x {
        r = (r + x / r) / 2;
    }
    r''',
      "bs_hi": '''    let (mut lo, mut hi) = (1i64, x);
    while lo <= hi {
        let m = lo + (hi - lo) / 2;
        if m * m == x { return m; }
        else if m * m < x { lo = m + 1; } else { hi = m - 1; }
    }
    hi'''}
    B["lua"] = {
      "bs_exact": '''    if x < 2 then return x end
    local lo, hi = 1, x // 2
    while lo <= hi do
        local m = lo + (hi - lo) // 2
        if m * m <= x and x < (m + 1) * (m + 1) then return m
        elseif m * m > x then hi = m - 1 else lo = m + 1 end
    end
    return lo''',
      "bs_ans": '''    local lo, hi, ans = 0, x, 0
    while lo <= hi do
        local m = lo + (hi - lo) // 2
        if m * m <= x then ans = m; lo = m + 1 else hi = m - 1 end
    end
    return ans''',
      "newton": '''    if x < 2 then return x end
    local r = x
    while r * r > x do
        r = (r + x // r) // 2
    end
    return r''',
      "bs_hi": '''    local lo, hi = 1, x
    while lo <= hi do
        local m = lo + (hi - lo) // 2
        if m * m == x then return m
        elseif m * m < x then lo = m + 1 else hi = m - 1 end
    end
    return hi'''}
    B["c"] = {
      "bs_exact": '''    if (x < 2) return x;
    long lo = 1, hi = x / 2;
    while (lo <= hi) {
        long m = lo + (hi - lo) / 2;
        if (m * m <= x && x < (m + 1) * (m + 1)) return m;
        else if (m * m > x) hi = m - 1; else lo = m + 1;
    }
    return lo;''',
      "bs_ans": '''    long lo = 0, hi = x, ans = 0;
    while (lo <= hi) {
        long m = lo + (hi - lo) / 2;
        if (m * m <= x) { ans = m; lo = m + 1; } else hi = m - 1;
    }
    return ans;''',
      "newton": '''    if (x < 2) return x;
    long r = x;
    while (r * r > x) r = (r + x / r) / 2;
    return r;''',
      "bs_hi": '''    long lo = 1, hi = x;
    while (lo <= hi) {
        long m = lo + (hi - lo) / 2;
        if (m * m == x) return m;
        else if (m * m < x) lo = m + 1; else hi = m - 1;
    }
    return hi;'''}
    B["cpp"] = {
      "bs_exact": '''    if (x < 2) return x;
    int64_t lo = 1, hi = x / 2;
    while (lo <= hi) {
        int64_t m = lo + (hi - lo) / 2;
        if (m * m <= x && x < (m + 1) * (m + 1)) return m;
        else if (m * m > x) hi = m - 1; else lo = m + 1;
    }
    return lo;''',
      "bs_ans": '''    int64_t lo = 0, hi = x, ans = 0;
    while (lo <= hi) {
        int64_t m = lo + (hi - lo) / 2;
        if (m * m <= x) { ans = m; lo = m + 1; } else hi = m - 1;
    }
    return ans;''',
      "newton": '''    if (x < 2) return x;
    int64_t r = x;
    while (r * r > x) r = (r + x / r) / 2;
    return r;''',
      "bs_hi": '''    int64_t lo = 1, hi = x;
    while (lo <= hi) {
        int64_t m = lo + (hi - lo) / 2;
        if (m * m == x) return m;
        else if (m * m < x) lo = m + 1; else hi = m - 1;
    }
    return hi;'''}
    B["r"] = {
      "bs_exact": '''  if (x < 2L) return(x)
  lo <- 1L; hi <- x %/% 2L
  while (lo <= hi) {
    m <- lo + (hi - lo) %/% 2L
    if (m * m <= x && x < (m + 1L) * (m + 1L)) return(m)
    else if (m * m > x) hi <- m - 1L else lo <- m + 1L
  }
  lo''',
      "bs_ans": '''  lo <- 0L; hi <- x; ans <- 0L
  while (lo <= hi) {
    m <- lo + (hi - lo) %/% 2L
    if (m * m <= x) { ans <- m; lo <- m + 1L } else hi <- m - 1L
  }
  ans''',
      "newton": '''  if (x < 2L) return(x)
  r <- x
  while (r * r > x) r <- (r + x %/% r) %/% 2L
  r''',
      "bs_hi": '''  lo <- 1L; hi <- x
  while (lo <= hi) {
    m <- lo + (hi - lo) %/% 2L
    if (m * m == x) return(m)
    else if (m * m < x) lo <- m + 1L else hi <- m - 1L
  }
  hi'''}
    B["zig"] = {
      "bs_exact": '''    if (x < 2) return x;
    var lo: i64 = 1;
    var hi: i64 = @divTrunc(x, 2);
    while (lo <= hi) {
        const m = lo + @divTrunc(hi - lo, 2);
        if (m * m <= x and x < (m + 1) * (m + 1)) return m;
        if (m * m > x) { hi = m - 1; } else { lo = m + 1; }
    }
    return lo;''',
      "bs_ans": '''    var lo: i64 = 0;
    var hi: i64 = x;
    var ans: i64 = 0;
    while (lo <= hi) {
        const m = lo + @divTrunc(hi - lo, 2);
        if (m * m <= x) { ans = m; lo = m + 1; } else { hi = m - 1; }
    }
    return ans;''',
      "newton": '''    if (x < 2) return x;
    var r: i64 = x;
    while (r * r > x) {
        r = @divTrunc(r + @divTrunc(x, r), 2);
    }
    return r;''',
      "bs_hi": '''    var lo: i64 = 1;
    var hi: i64 = x;
    while (lo <= hi) {
        const m = lo + @divTrunc(hi - lo, 2);
        if (m * m == x) return m;
        if (m * m < x) { lo = m + 1; } else { hi = m - 1; }
    }
    return hi;'''}
    B["dart"] = {
      "bs_exact": '''  if (x < 2) return x;
  var lo = 1, hi = x ~/ 2;
  while (lo <= hi) {
    final m = lo + (hi - lo) ~/ 2;
    if (m * m <= x && x < (m + 1) * (m + 1)) return m;
    if (m * m > x) { hi = m - 1; } else { lo = m + 1; }
  }
  return lo;''',
      "bs_ans": '''  var lo = 0, hi = x, ans = 0;
  while (lo <= hi) {
    final m = lo + (hi - lo) ~/ 2;
    if (m * m <= x) { ans = m; lo = m + 1; } else { hi = m - 1; }
  }
  return ans;''',
      "newton": '''  if (x < 2) return x;
  var r = x;
  while (r * r > x) {
    r = (r + x ~/ r) ~/ 2;
  }
  return r;''',
      "bs_hi": '''  var lo = 1, hi = x;
  while (lo <= hi) {
    final m = lo + (hi - lo) ~/ 2;
    if (m * m == x) return m;
    if (m * m < x) { lo = m + 1; } else { hi = m - 1; }
  }
  return hi;'''}

    cm = {"rust": ("fn my_sqrt(x: i64) -> i64 {\n__BODY__\n}\nfn main() {\n    let cases: [(i64, i64); 4] = [(4, 2), (8, 2), (16, 4), (2147395599, 46339)];\n    for (x, want) in cases {\n        assert_eq!(my_sqrt(x), want, \"x={}\", x);\n    }\n    println!(\"PASS\");\n}\n", "// 来源（blog）：__SRC__\n// LeetCode 69. x 的平方根 — Rust 版（__TITLE__）\n"),
          "lua": ("local function my_sqrt(x)\n__BODY__\nend\nlocal cases = {{4, 2}, {8, 2}, {16, 4}, {2147395599, 46339}}\nfor _, c in ipairs(cases) do\n    assert(my_sqrt(c[1]) == c[2], \"x=\" .. c[1])\nend\nprint(\"PASS\")\n", "-- 来源（blog）：__SRC__\n-- LeetCode 69. x 的平方根 — Lua 版（__TITLE__）\n"),
          "c": ("static long my_sqrt(long x) {\n__BODY__\n}\nint main(void) {\n    long cs[4][2] = { {4, 2}, {8, 2}, {16, 4}, {2147395599, 46339} };\n    for (int i = 0; i < 4; i++)\n        if (my_sqrt(cs[i][0]) != cs[i][1]) { printf(\"FAIL %d\\\\n\", i); return 1; }\n    printf(\"PASS\\\\n\");\n    return 0;\n}\n", "/* 来源（blog）：__SRC__\n * LeetCode 69. x 的平方根 — C 版（__TITLE__） */\n#include <stdio.h>\n"),
          "cpp": ("static int64_t mySqrt(int64_t x) {\n__BODY__\n}\nint main() {\n    int64_t cs[4][2] = {{4, 2}, {8, 2}, {16, 4}, {2147395599LL, 46339}};\n    for (auto &c : cs) assert(mySqrt(c[0]) == c[1]);\n    std::cout << \"PASS\" << std::endl;\n}\n", "// 来源（blog）：__SRC__\n// LeetCode 69. x 的平方根 — C++ 版（__TITLE__）\n#include <cassert>\n#include <cstdint>\n#include <iostream>\n"),
          "r": ("my_sqrt <- function(x) {\n__BODY__\n}\ncs <- matrix(c(4L, 2L, 8L, 2L, 16L, 4L, 2147395599L, 46339L), ncol = 2L, byrow = TRUE)\nfor (i in seq_len(nrow(cs))) stopifnot(my_sqrt(cs[i, 1L]) == cs[i, 2L])\ncat(\"PASS\\\\n\")\n", "# 来源（blog）：__SRC__\n# LeetCode 69. x 的平方根 — R 版（__TITLE__）\n"),
          "zig": ("fn mySqrt(x: i64) i64 {\n__BODY__\n}\npub fn main() !void {\n    const cases = [_][2]i64{ .{ 4, 2 }, .{ 8, 2 }, .{ 16, 4 }, .{ 2147395599, 46339 } };\n    for (cases, 0..) |c, i| {\n        if (mySqrt(c[0]) != c[1]) {\n            std.debug.print(\"FAIL case {d}\\\\n\", .{i});\n            return error.TestFailed;\n        }\n    }\n    std.debug.print(\"PASS\\\\n\", .{});\n}\n", "// 来源（blog）：__SRC__\n// LeetCode 69. x 的平方根 — Zig 版（__TITLE__）\nconst std = @import(\"std\");\n"),
          "dart": ("int mySqrt(int x) {\n__BODY__\n}\nvoid main() {\n  final cases = <List<int>>[\n    [4, 2],\n    [8, 2],\n    [16, 4],\n    [2147395599, 46339],\n  ];\n  for (final c in cases) {\n    if (mySqrt(c[0]) != c[1]) throw StateError('x=${c[0]}');\n  }\n  print('PASS');\n}\n", "// 来源（blog）：__SRC__\n// LeetCode 69. x 的平方根 — Dart 版（__TITLE__）\n")}
    frame, head = cm[lang]
    return head.replace("__SRC__", src).replace("__TITLE__", title) + frame.replace("__BODY__", B[lang][kind])

# ---- 写文件 ----
PLANS374 = ["方案1", "方案2", "方案3", "方案4", "方案5", "方案6"]
SOLS374 = ["solution_1___1", "solution_2___2", "solution_3___3", "solution_4___4", "solution_5___5", "solution_6___6"]
SOLS69 = [("solution_1_1_____1________", "1 ) 方案1", "bs_exact"), ("solution_2_2_____2_____", "2 ) 方案2", "bs_ans"),
          ("solution_3_3_____3_________", "3 ) 方案3", "newton"), ("solution_4_4____4__________", "4 ) 方案4", "bs_hi")]
count = 0
for lang, ext in LANGS.items():
    d = f"{DSA}/code/{lang}/binary_search"
    os.makedirs(f"{d}/lc_35_搜索插入位置", exist_ok=True)
    open(f"{d}/lc_35_搜索插入位置/solution_1_1_____1_____.{ext}", "w").write(
        T35[lang].replace("__SRC__", f"https://blog.csdn.net/tyro_java/article/details/{B35}"))
    count += 1
    os.makedirs(f"{d}/lc_374_猜数字大小", exist_ok=True)
    for sol, plan in zip(SOLS374, PLANS374):
        open(f"{d}/lc_374_猜数字大小/{sol}.{ext}", "w").write(build_374(lang, sol.endswith("1___1"), plan))
        count += 1
    os.makedirs(f"{d}/lc_69_x_的平方根", exist_ok=True)
    for sol, plan, kind in SOLS69:
        open(f"{d}/lc_69_x_的平方根/{sol}.{ext}", "w").write(build_69(lang, kind, plan))
        count += 1
print(f"wrote {count} files")
