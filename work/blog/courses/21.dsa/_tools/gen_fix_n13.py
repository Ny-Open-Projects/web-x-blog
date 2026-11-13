#!/usr/bin/env python3
# gen_fix_n13.py — 补齐 notes/lc_107431726 最大红矩形分析 × 7 语言（5 解法）
# 最大全 '.' 矩形：s1/s2 暴力+卡片法，s3/s4/s5 单调栈
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from langlib import emit

REL = "notes/lc_107431726_最大红矩形分析"
BLOG = "来源（blog）：https://blog.csdn.net/tyro_java/article/details/107431726"

# ---------- A: 暴力 + 卡片法（s1/s2） ----------
A = {
"rust": '''// @@BLOG@@
// LeetCode 107431726. 最大红矩形分析 — Rust 版（方案A：逐行高度 + 暴力区间 / 卡片扩展）
fn get_result(n: usize, m: usize, matrix: &[&str]) -> i64 {
    let bytes: Vec<&[u8]> = matrix.iter().map(|s| s.as_bytes()).collect();
    let mut ans = 0i64;
    let mut height = vec![0i64; m + 2];
    for k in 0..n {
        for i in 1..=m {
            if bytes[k][i - 1] == b'.' {
                height[i] += 1;
            } else {
                height[i] = 0;
            }
        }
        for a in 1..=m {
            let mut min_h = 50000i64;
            for c in a..=m {
                if height[c] < min_h {
                    min_h = height[c];
                }
            }
            let area = (m - a + 1) as i64 * min_h;
            if area > ans {
                ans = area;
            }
        }
    }
    ans
}

fn get_result_card(n: usize, m: usize, matrix: &[&str]) -> i64 {
    let bytes: Vec<&[u8]> = matrix.iter().map(|s| s.as_bytes()).collect();
    let mut ans = 0i64;
    let mut height = vec![0i64; m + 2];
    for k in 0..n {
        for i in 1..=m {
            if bytes[k][i - 1] == b'.' {
                height[i] += 1;
            } else {
                height[i] = 0;
            }
        }
        for a in 1..=m {
            let cur_h = height[a];
            let mut lo = a as i64 - 1;
            while lo >= 1 && height[lo as usize] >= cur_h {
                lo -= 1;
            }
            let mut hi = a + 1;
            while hi <= m && height[hi] >= cur_h {
                hi += 1;
            }
            let area = (hi - lo as usize - 1) as i64 * cur_h;
            if area > ans {
                ans = area;
            }
        }
    }
    ans
}

fn main() {
    let matrix = [".....", "XXXXX", ".X...", "....."];
    assert_eq!(get_result(4, 5, &matrix), 6, "brute");
    assert_eq!(get_result_card(4, 5, &matrix), 6, "card");
    println!("PASS");
}
''',
"lua": '''-- @@BLOG@@
-- LeetCode 107431726. 最大红矩形分析 — Lua 版（方案A：逐行高度 + 暴力区间 / 卡片扩展）
local function get_result(n, m, matrix)
    local ans = 0
    local height = {}
    for i = 1, m + 2 do height[i] = 0 end
    for k = 1, n do
        for i = 1, m do
            if matrix[k]:sub(i, i) == "." then height[i] = height[i] + 1 else height[i] = 0 end
        end
        for a = 1, m do
            local min_h = 50000
            for c = a, m do
                if height[c] < min_h then min_h = height[c] end
            end
            local area = (m - a + 1) * min_h
            if area > ans then ans = area end
        end
    end
    return ans
end

local function get_result_card(n, m, matrix)
    local ans = 0
    local height = {}
    for i = 1, m + 2 do height[i] = 0 end
    for k = 1, n do
        for i = 1, m do
            if matrix[k]:sub(i, i) == "." then height[i] = height[i] + 1 else height[i] = 0 end
        end
        for a = 1, m do
            local cur_h = height[a]
            local lo = a - 1
            while lo >= 1 and height[lo] >= cur_h do lo = lo - 1 end
            local hi = a + 1
            while hi <= m and height[hi] >= cur_h do hi = hi + 1 end
            local area = (hi - lo - 1) * cur_h
            if area > ans then ans = area end
        end
    end
    return ans
end

local matrix = {".....", "XXXXX", ".X...", "....."}
assert(get_result(4, 5, matrix) == 6, "brute")
assert(get_result_card(4, 5, matrix) == 6, "card")
print("PASS")
''',
"c": '''/* @@BLOG@@
 * LeetCode 107431726. 最大红矩形分析 — C 版（方案A：逐行高度 + 暴力区间 / 卡片扩展）
 */
#include <stdio.h>

static long long get_result(int n, int m, const char *matrix[]) {
    long long ans = 0;
    long long height[64] = {0};
    for (int k = 0; k < n; k++) {
        for (int i = 1; i <= m; i++) {
            if (matrix[k][i - 1] == '.') height[i]++; else height[i] = 0;
        }
        for (int a = 1; a <= m; a++) {
            long long min_h = 50000;
            for (int c = a; c <= m; c++) if (height[c] < min_h) min_h = height[c];
            long long area = (long long)(m - a + 1) * min_h;
            if (area > ans) ans = area;
        }
    }
    return ans;
}

static long long get_result_card(int n, int m, const char *matrix[]) {
    long long ans = 0;
    long long height[64] = {0};
    for (int k = 0; k < n; k++) {
        for (int i = 1; i <= m; i++) {
            if (matrix[k][i - 1] == '.') height[i]++; else height[i] = 0;
        }
        for (int a = 1; a <= m; a++) {
            long long cur_h = height[a];
            long long lo = a - 1;
            while (lo >= 1 && height[lo] >= cur_h) lo--;
            long long hi = a + 1;
            while (hi <= m && height[hi] >= cur_h) hi++;
            long long area = (hi - lo - 1) * cur_h;
            if (area > ans) ans = area;
        }
    }
    return ans;
}

int main(void) {
    const char *matrix[] = {".....", "XXXXX", ".X...", "....."};
    if (get_result(4, 5, matrix) != 6) { printf("brute failed\\n"); return 1; }
    if (get_result_card(4, 5, matrix) != 6) { printf("card failed\\n"); return 1; }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''// @@BLOG@@
// LeetCode 107431726. 最大红矩形分析 — C++ 版（方案A：逐行高度 + 暴力区间 / 卡片扩展）
#include <iostream>
#include <string>
#include <vector>

static long long get_result(int n, int m, const std::vector<std::string> &matrix) {
    long long ans = 0;
    std::vector<long long> height(m + 2, 0);
    for (int k = 0; k < n; ++k) {
        for (int i = 1; i <= m; ++i) {
            if (matrix[k][i - 1] == '.') ++height[i]; else height[i] = 0;
        }
        for (int a = 1; a <= m; ++a) {
            long long min_h = 50000;
            for (int c = a; c <= m; ++c) if (height[c] < min_h) min_h = height[c];
            long long area = static_cast<long long>(m - a + 1) * min_h;
            if (area > ans) ans = area;
        }
    }
    return ans;
}

static long long get_result_card(int n, int m, const std::vector<std::string> &matrix) {
    long long ans = 0;
    std::vector<long long> height(m + 2, 0);
    for (int k = 0; k < n; ++k) {
        for (int i = 1; i <= m; ++i) {
            if (matrix[k][i - 1] == '.') ++height[i]; else height[i] = 0;
        }
        for (int a = 1; a <= m; ++a) {
            long long cur_h = height[a];
            long long lo = a - 1;
            while (lo >= 1 && height[lo] >= cur_h) --lo;
            long long hi = a + 1;
            while (hi <= m && height[hi] >= cur_h) ++hi;
            long long area = (hi - lo - 1) * cur_h;
            if (area > ans) ans = area;
        }
    }
    return ans;
}

int main() {
    std::vector<std::string> matrix = {".....", "XXXXX", ".X...", "....."};
    if (get_result(4, 5, matrix) != 6) { std::cout << "brute failed" << std::endl; return 1; }
    if (get_result_card(4, 5, matrix) != 6) { std::cout << "card failed" << std::endl; return 1; }
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''# @@BLOG@@
# LeetCode 107431726. 最大红矩形分析 — R 版（方案A：逐行高度 + 暴力区间 / 卡片扩展）
get_result <- function(n, m, matrix) {
  ans <- 0
  height <- rep(0L, m + 2L)
  for (k in 1:n) {
    for (i in 1:m) {
      if (substr(matrix[k], i, i) == ".") height[i] <- height[i] + 1L else height[i] <- 0L
    }
    for (a in 1:m) {
      min_h <- 50000L
      for (c in a:m) if (height[c] < min_h) min_h <- height[c]
      area <- (m - a + 1L) * min_h
      if (area > ans) ans <- area
    }
  }
  ans
}

get_result_card <- function(n, m, matrix) {
  ans <- 0
  height <- rep(0L, m + 2L)
  for (k in 1:n) {
    for (i in 1:m) {
      if (substr(matrix[k], i, i) == ".") height[i] <- height[i] + 1L else height[i] <- 0L
    }
    for (a in 1:m) {
      cur_h <- height[a]
      lo <- a - 1L
      while (lo >= 1L && height[lo] >= cur_h) lo <- lo - 1L
      hi <- a + 1L
      while (hi <= m && height[hi] >= cur_h) hi <- hi + 1L
      area <- (hi - lo - 1L) * cur_h
      if (area > ans) ans <- area
    }
  }
  ans
}

matrix <- c(".....", "XXXXX", ".X...", ".....")
stopifnot(get_result(4L, 5L, matrix) == 6L)
stopifnot(get_result_card(4L, 5L, matrix) == 6L)
cat("PASS\\n")
''',
"zig": '''// @@BLOG@@
// LeetCode 107431726. 最大红矩形分析 — Zig 版（方案A：逐行高度 + 暴力区间 / 卡片扩展）
const std = @import("std");

fn getResult(n: usize, m: usize, matrix: []const []const u8) i64 {
    var ans: i64 = 0;
    var height: [66]i64 = undefined;
    for (&height) |*h| h.* = 0;
    for (0..n) |k| {
        var i: usize = 1;
        while (i <= m) : (i += 1) {
            if (matrix[k][i - 1] == '.') {
                height[i] += 1;
            } else {
                height[i] = 0;
            }
        }
        var a: usize = 1;
        while (a <= m) : (a += 1) {
            var min_h: i64 = 50000;
            var c = a;
            while (c <= m) : (c += 1) {
                if (height[c] < min_h) min_h = height[c];
            }
            const area = @as(i64, @intCast(m - a + 1)) * min_h;
            if (area > ans) ans = area;
        }
    }
    return ans;
}

fn getResultCard(n: usize, m: usize, matrix: []const []const u8) i64 {
    var ans: i64 = 0;
    var height: [66]i64 = undefined;
    for (&height) |*h| h.* = 0;
    for (0..n) |k| {
        var i: usize = 1;
        while (i <= m) : (i += 1) {
            if (matrix[k][i - 1] == '.') {
                height[i] += 1;
            } else {
                height[i] = 0;
            }
        }
        var a: usize = 1;
        while (a <= m) : (a += 1) {
            const cur_h = height[a];
            var lo: i64 = @as(i64, @intCast(a)) - 1;
            while (lo >= 1 and height[@intCast(lo)] >= cur_h) lo -= 1;
            var hi: usize = a + 1;
            while (hi <= m and height[hi] >= cur_h) hi += 1;
            const area = @as(i64, @intCast(hi - @as(usize, @intCast(lo)) - 1)) * cur_h;
            if (area > ans) ans = area;
        }
    }
    return ans;
}

pub fn main() !void {
    const matrix = [_][]const u8{ ".....", "XXXXX", ".X...", "....." };
    if (getResult(4, 5, &matrix) != 6) return error.TestFailed;
    if (getResultCard(4, 5, &matrix) != 6) return error.TestFailed;
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''// @@BLOG@@
// LeetCode 107431726. 最大红矩形分析 — Dart 版（方案A：逐行高度 + 暴力区间 / 卡片扩展）
int getResult(int n, int m, List<String> matrix) {
  var ans = 0;
  final height = List<int>.filled(m + 2, 0);
  for (var k = 0; k < n; k++) {
    for (var i = 1; i <= m; i++) {
      if (matrix[k][i - 1] == '.') {
        height[i] += 1;
      } else {
        height[i] = 0;
      }
    }
    for (var a = 1; a <= m; a++) {
      var minH = 50000;
      for (var c = a; c <= m; c++) {
        if (height[c] < minH) minH = height[c];
      }
      final area = (m - a + 1) * minH;
      if (area > ans) ans = area;
    }
  }
  return ans;
}

int getResultCard(int n, int m, List<String> matrix) {
  var ans = 0;
  final height = List<int>.filled(m + 2, 0);
  for (var k = 0; k < n; k++) {
    for (var i = 1; i <= m; i++) {
      if (matrix[k][i - 1] == '.') {
        height[i] += 1;
      } else {
        height[i] = 0;
      }
    }
    for (var a = 1; a <= m; a++) {
      final curH = height[a];
      var lo = a - 1;
      while (lo >= 1 && height[lo] >= curH) {
        lo--;
      }
      var hi = a + 1;
      while (hi <= m && height[hi] >= curH) {
        hi++;
      }
      final area = (hi - lo - 1) * curH;
      if (area > ans) ans = area;
    }
  }
  return ans;
}

void main() {
  const matrix = <String>['.....', 'XXXXX', '.X...', '.....'];
  if (getResult(4, 5, matrix) != 6) throw StateError('brute failed');
  if (getResultCard(4, 5, matrix) != 6) throw StateError('card failed');
  print('PASS');
}
''',
}

# ---------- B: 单调栈（s3/s4/s5 变体） ----------
def mono_block(tag, extra_case):
    extra = ""
    main_body = {
"rust": '''fn main() {
    let matrix = [".....", "XXXXX", ".X...", "....."];
    assert_eq!(max_red_rectangle(&matrix), 6, "mono");%(EXTRA)s
    println!("PASS");
}
''',
"lua": '''local matrix = {".....", "XXXXX", ".X...", "....."}
assert(max_red_rectangle(matrix) == 6, "mono")%(EXTRA)s
print("PASS")
''',
"c": '''int main(void) {
    const char *matrix[] = {".....", "XXXXX", ".X...", "....."};
    if (max_red_rectangle(matrix, 4) != 6) { printf("mono failed\\n"); return 1; }%(EXTRA)s
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''int main() {
    std::vector<std::string> matrix = {".....", "XXXXX", ".X...", "....."};
    if (max_red_rectangle(matrix) != 6) { std::cout << "mono failed" << std::endl; return 1; }%(EXTRA)s
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''matrix <- c(".....", "XXXXX", ".X...", ".....")
stopifnot(max_red_rectangle(matrix) == 6L)%(EXTRA)s
cat("PASS\\n")
''',
"zig": '''pub fn main() !void {
    const matrix = [_][]const u8{ ".....", "XXXXX", ".X...", "....." };
    if (maxRedRectangle(&matrix) != 6) return error.TestFailed;%(EXTRA)s
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''void main() {
  const matrix = <String>['.....', 'XXXXX', '.X...', '.....'];
  if (maxRedRectangle(matrix) != 6) throw StateError('mono failed');%(EXTRA)s
  print('PASS');
}
''',
    }
    extra = {lang: "" for lang in ("rust", "lua", "c", "cpp", "r", "zig", "dart")}
    if extra_case:
        extra = {
"rust": '''
    assert_eq!(max_red_rectangle(&["...", "...", "..."]), 9, "all dots");''',
"lua": '''
assert(max_red_rectangle({"...", "...", "..."}) == 9, "all dots")''',
"c": '''
    const char *m2[] = {"...", "...", "..."};
    if (max_red_rectangle(m2, 3) != 9) { printf("all dots failed\\n"); return 1; }''',
"cpp": '''
    if (max_red_rectangle({"...", "...", "..."}) != 9) { std::cout << "all dots failed" << std::endl; return 1; }''',
"r": '''
stopifnot(max_red_rectangle(c("...", "...", "...")) == 9L)''',
"zig": '''
    const m2 = [_][]const u8{ "...", "...", "..." };
    if (maxRedRectangle(&m2) != 9) return error.TestFailed;''',
"dart": '''
  if (maxRedRectangle(<String>['...', '...', '...']) != 9) throw StateError('all dots failed');''',
        }
    core = {
"rust": '''// @@BLOG@@
// LeetCode 107431726. 最大红矩形分析 — Rust 版（@@TAG@@：逐行高度 + 单调栈）
fn max_red_rectangle(matrix: &[&str]) -> i64 {
    let n = matrix.len();
    let m = matrix[0].len();
    let mut ans = 0i64;
    let mut height = vec![0i64; m + 2];
    for k in 0..n {
        let row = matrix[k].as_bytes();
        for i in 1..=m {
            if row[i - 1] == b'.' {
                height[i] += 1;
            } else {
                height[i] = 0;
            }
        }
        let mut stack: Vec<usize> = vec![0];
        for i in 1..=m + 1 {
            while height[*stack.last().unwrap()] > height[i] {
                let top = stack.pop().unwrap();
                let now_h = height[top];
                let width = i - stack.last().unwrap() - 1;
                let area = now_h * width as i64;
                if area > ans {
                    ans = area;
                }
            }
            stack.push(i);
        }
    }
    ans
}
''',
"lua": '''-- @@BLOG@@
-- LeetCode 107431726. 最大红矩形分析 — Lua 版（@@TAG@@：逐行高度 + 单调栈）
local function max_red_rectangle(matrix)
    local n, m = #matrix, #matrix[1]
    local ans = 0
    local height = {}
    height[0] = 0  -- 哨兵
    for i = 1, m + 2 do height[i] = 0 end
    for k = 1, n do
        for i = 1, m do
            if matrix[k]:sub(i, i) == "." then height[i] = height[i] + 1 else height[i] = 0 end
        end
        local stack = {0}
        for i = 1, m + 1 do
            while height[stack[#stack]] > height[i] do
                local top = table.remove(stack)
                local now_h = height[top]
                local width = i - stack[#stack] - 1
                local area = now_h * width
                if area > ans then ans = area end
            end
            stack[#stack + 1] = i
        end
    end
    return ans
end
''',
"c": '''/* @@BLOG@@
 * LeetCode 107431726. 最大红矩形分析 — C 版（@@TAG@@：逐行高度 + 单调栈）
 */
#include <stdio.h>

static long long max_red_rectangle(const char *matrix[], int n) {
    int m = 0;
    while (matrix[0][m]) m++;
    long long ans = 0;
    long long height[64] = {0};
    int stack[66];
    for (int k = 0; k < n; k++) {
        for (int i = 1; i <= m; i++) {
            if (matrix[k][i - 1] == '.') height[i]++; else height[i] = 0;
        }
        int top = 0;
        stack[top++] = 0;
        for (int i = 1; i <= m + 1; i++) {
            long long hi = (i <= m) ? height[i] : 0;
            while (height[stack[top - 1]] > hi) {
                long long now_h = height[stack[--top]];
                long long width = i - stack[top - 1] - 1;
                long long area = now_h * width;
                if (area > ans) ans = area;
            }
            stack[top++] = i;
        }
    }
    return ans;
}
''',
"cpp": '''// @@BLOG@@
// LeetCode 107431726. 最大红矩形分析 — C++ 版（@@TAG@@：逐行高度 + 单调栈）
#include <iostream>
#include <string>
#include <vector>

static long long max_red_rectangle(const std::vector<std::string> &matrix) {
    size_t n = matrix.size();
    size_t m = matrix[0].size();
    long long ans = 0;
    std::vector<long long> height(m + 2, 0);
    for (size_t k = 0; k < n; ++k) {
        for (size_t i = 1; i <= m; ++i) {
            if (matrix[k][i - 1] == '.') ++height[i]; else height[i] = 0;
        }
        std::vector<size_t> stack{0};
        for (size_t i = 1; i <= m + 1; ++i) {
            long long hi = (i <= m) ? height[i] : 0;
            while (height[stack.back()] > hi) {
                long long now_h = height[stack.back()];
                stack.pop_back();
                long long width = static_cast<long long>(i - stack.back() - 1);
                long long area = now_h * width;
                if (area > ans) ans = area;
            }
            stack.push_back(i);
        }
    }
    return ans;
}
''',
"r": '''# @@BLOG@@
# LeetCode 107431726. 最大红矩形分析 — R 版（@@TAG@@：逐行高度 + 单调栈）
max_red_rectangle <- function(matrix) {
  n <- length(matrix)
  m <- nchar(matrix[1])
  ans <- 0L
  height <- rep(0L, m + 2L)
  for (k in 1:n) {
    for (i in 1:m) {
      if (substr(matrix[k], i, i) == ".") height[i] <- height[i] + 1L else height[i] <- 0L
    }
    stack <- c(0L)
    h_at <- function(i) if (i == 0L) 0L else height[i]
    for (i in 1:(m + 1L)) {
      hi <- if (i <= m) height[i] else 0L
      while (h_at(stack[length(stack)]) > hi) {
        now_h <- h_at(stack[length(stack)])
        stack <- stack[-length(stack)]
        width <- i - stack[length(stack)] - 1L
        area <- now_h * width
        if (area > ans) ans <- area
      }
      stack <- c(stack, i)
    }
  }
  ans
}
''',
"zig": '''// @@BLOG@@
// LeetCode 107431726. 最大红矩形分析 — Zig 版（@@TAG@@：逐行高度 + 单调栈）
const std = @import("std");

fn maxRedRectangle(matrix: []const []const u8) i64 {
    const n = matrix.len;
    const m = matrix[0].len;
    var ans: i64 = 0;
    var height: [66]i64 = undefined;
    for (&height) |*h| h.* = 0;
    var stack: [66]usize = undefined;
    for (0..n) |k| {
        var i: usize = 1;
        while (i <= m) : (i += 1) {
            if (matrix[k][i - 1] == '.') {
                height[i] += 1;
            } else {
                height[i] = 0;
            }
        }
        var top: usize = 0;
        stack[top] = 0;
        top += 1;
        var idx: usize = 1;
        while (idx <= m + 1) : (idx += 1) {
            const hi: i64 = if (idx <= m) height[idx] else 0;
            while (height[stack[top - 1]] > hi) {
                top -= 1;
                const now_h = height[stack[top]];
                const width = idx - stack[top - 1] - 1;
                const area = now_h * @as(i64, @intCast(width));
                if (area > ans) ans = area;
            }
            stack[top] = idx;
            top += 1;
        }
    }
    return ans;
}
''',
"dart": '''// @@BLOG@@
// LeetCode 107431726. 最大红矩形分析 — Dart 版（@@TAG@@：逐行高度 + 单调栈）
int maxRedRectangle(List<String> matrix) {
  final n = matrix.length;
  final m = matrix[0].length;
  var ans = 0;
  final height = List<int>.filled(m + 2, 0);
  for (var k = 0; k < n; k++) {
    for (var i = 1; i <= m; i++) {
      if (matrix[k][i - 1] == '.') {
        height[i] += 1;
      } else {
        height[i] = 0;
      }
    }
    final stack = <int>[0];
    for (var i = 1; i <= m + 1; i++) {
      final hi = i <= m ? height[i] : 0;
      while (height[stack.last] > hi) {
        final nowH = height[stack.removeLast()];
        final width = i - stack.last - 1;
        final area = nowH * width;
        if (area > ans) ans = area;
      }
      stack.add(i);
    }
  }
  return ans;
}
''',
    }
    return core, main_body, extra

EXTS = {"rust": ".rs", "lua": ".lua", "c": ".c", "cpp": ".cpp", "r": ".R", "zig": ".zig", "dart": ".dart"}

def build_sol(tag, extra_case):
    core, main_body, extra = mono_block(tag, extra_case)
    out = {}
    for lang in EXTS:
        out[lang] = core[lang].replace("@@BLOG@@", BLOG).replace("@@TAG@@", tag) + "\n" + main_body[lang].replace("%(EXTRA)s", extra[lang])
    return out

def main():
    sols = {
        1: build_sol("方案A", False),
        2: build_sol("方案B", False),
        3: build_sol("方案C", False),
        4: build_sol("方案D", False),
        5: build_sol("方案E", True),
    }
    # s1/s2 的 TS 源码相同（暴力+卡片法），A 块单独处理
    for lang, t in A.items():
        out = t.replace("@@BLOG@@", BLOG)
        emit(lang, REL + "/solution_1___1" + EXTS[lang], out)
        emit(lang, REL + "/solution_2___2" + EXTS[lang], out)
    for sol in (3, 4, 5):
        for lang, t in sols[sol].items():
            emit(lang, REL + "/solution_%d___%d%s" % (sol, sol, EXTS[lang]), t)

if __name__ == "__main__":
    main()
