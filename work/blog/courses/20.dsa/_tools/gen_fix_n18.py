#!/usr/bin/env python3
# gen_fix_n18.py — 补齐 notes/lc_104107934 滑动验证码识别 × 7 语言（7 解法）
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from langlib import emit

REL = "notes/lc_104107934_python笔记_滑动验证码的识别算法"
BLOG = "来源（blog）：https://blog.csdn.net/tyro_java/article/details/104107934"

# ---------- s1: 前向差分边缘 + 匹配 ----------
S1 = {
"rust": '''// @@BLOG@@
// LeetCode 104107934. 滑动验证码识别 — Rust 版（方案1：前向差分边缘 + 匹配）
fn detect_edges(image: &[i32]) -> Vec<bool> {
    let mut edges = vec![false; image.len()];
    for i in 1..image.len() {
        edges[i] = (image[i] - image[i - 1]).abs() > 50;
    }
    edges
}

fn recognize_captcha(bg: &[i32], puzzle: &[i32]) -> usize {
    let bg_edges = detect_edges(bg);
    let puzzle_edges = detect_edges(puzzle);
    let mut best_x = 0usize;
    let mut best_score: i64 = -1;
    for x in 0..=bg.len() - puzzle.len() {
        let mut score = 0i64;
        for y in 0..puzzle.len() {
            if bg_edges[x + y] && puzzle_edges[y] {
                score += 1;
            }
        }
        if score > best_score {
            best_score = score;
            best_x = x;
        }
    }
    best_x
}

fn main() {
    let bg = [10, 10, 10, 10, 200, 200, 200, 200];
    let puzzle = [10, 200, 200, 200];
    assert_eq!(recognize_captcha(&bg, &puzzle), 3, "gap");
    println!("PASS");
}
''',
"lua": '''-- @@BLOG@@
-- LeetCode 104107934. 滑动验证码识别 — Lua 版（方案1：前向差分边缘 + 匹配）
local function detect_edges(image)
    local edges = {}
    for i = 1, #image do edges[i] = false end
    for i = 2, #image do
        edges[i] = math.abs(image[i] - image[i - 1]) > 50
    end
    return edges
end

local function recognize_captcha(bg, puzzle)
    local bg_edges = detect_edges(bg)
    local puzzle_edges = detect_edges(puzzle)
    local best_x, best_score = 1, -1
    for x = 1, #bg - #puzzle + 1 do
        local score = 0
        for y = 1, #puzzle do
            if bg_edges[x + y - 1] and puzzle_edges[y] then score = score + 1 end
        end
        if score > best_score then
            best_score = score
            best_x = x
        end
    end
    return best_x - 1  -- 0 基结果
end

local bg = {10, 10, 10, 10, 200, 200, 200, 200}
local puzzle = {10, 200, 200, 200}
assert(recognize_captcha(bg, puzzle) == 3, "gap")
print("PASS")
''',
"c": '''/* @@BLOG@@
 * LeetCode 104107934. 滑动验证码识别 — C 版（方案1：前向差分边缘 + 匹配）
 */
#include <stdio.h>
#include <stdlib.h>

static void detect_edges(const int *image, int n, int *edges) {
    for (int i = 0; i < n; i++) edges[i] = 0;
    for (int i = 1; i < n; i++) edges[i] = abs(image[i] - image[i - 1]) > 50;
}

static int recognize_captcha(const int *bg, int bn, const int *puzzle, int pn) {
    int bg_edges[64], puzzle_edges[64];
    detect_edges(bg, bn, bg_edges);
    detect_edges(puzzle, pn, puzzle_edges);
    int best_x = 0;
    long best_score = -1;
    for (int x = 0; x <= bn - pn; x++) {
        long score = 0;
        for (int y = 0; y < pn; y++)
            if (bg_edges[x + y] && puzzle_edges[y]) score++;
        if (score > best_score) { best_score = score; best_x = x; }
    }
    return best_x;
}

int main(void) {
    int bg[8] = {10, 10, 10, 10, 200, 200, 200, 200};
    int puzzle[4] = {10, 200, 200, 200};
    if (recognize_captcha(bg, 8, puzzle, 4) != 3) { printf("gap failed\\n"); return 1; }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''// @@BLOG@@
// LeetCode 104107934. 滑动验证码识别 — C++ 版（方案1：前向差分边缘 + 匹配）
#include <cmath>
#include <iostream>
#include <vector>

static std::vector<bool> detect_edges(const std::vector<int> &image) {
    std::vector<bool> edges(image.size(), false);
    for (size_t i = 1; i < image.size(); ++i) {
        edges[i] = std::abs(image[i] - image[i - 1]) > 50;
    }
    return edges;
}

static int recognize_captcha(const std::vector<int> &bg, const std::vector<int> &puzzle) {
    auto bg_edges = detect_edges(bg);
    auto puzzle_edges = detect_edges(puzzle);
    int best_x = 0;
    long long best_score = -1;
    for (size_t x = 0; x + puzzle.size() <= bg.size(); ++x) {
        long long score = 0;
        for (size_t y = 0; y < puzzle.size(); ++y) {
            if (bg_edges[x + y] && puzzle_edges[y]) ++score;
        }
        if (score > best_score) { best_score = score; best_x = static_cast<int>(x); }
    }
    return best_x;
}

int main() {
    std::vector<int> bg = {10, 10, 10, 10, 200, 200, 200, 200};
    std::vector<int> puzzle = {10, 200, 200, 200};
    if (recognize_captcha(bg, puzzle) != 3) { std::cout << "gap failed" << std::endl; return 1; }
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''# @@BLOG@@
# LeetCode 104107934. 滑动验证码识别 — R 版（方案1：前向差分边缘 + 匹配）
detect_edges <- function(image) {
  edges <- rep(FALSE, length(image))
  for (i in 2:length(image)) {
    edges[i] <- abs(image[i] - image[i - 1L]) > 50
  }
  edges
}

recognize_captcha <- function(bg, puzzle) {
  bg_edges <- detect_edges(bg)
  puzzle_edges <- detect_edges(puzzle)
  best_x <- 1L
  best_score <- -1L
  for (x in 1:(length(bg) - length(puzzle) + 1L)) {
    score <- 0L
    for (y in 1:length(puzzle)) {
      if (bg_edges[x + y - 1L] && puzzle_edges[y]) score <- score + 1L
    }
    if (score > best_score) {
      best_score <- score
      best_x <- x
    }
  }
  as.integer(best_x - 1L)  # 0 基结果
}

bg <- c(10, 10, 10, 10, 200, 200, 200, 200)
puzzle <- c(10, 200, 200, 200)
stopifnot(recognize_captcha(bg, puzzle) == 3L)
cat("PASS\\n")
''',
"zig": '''// @@BLOG@@
// LeetCode 104107934. 滑动验证码识别 — Zig 版（方案1：前向差分边缘 + 匹配）
const std = @import("std");

fn detectEdges(image: []const i32, edges: []bool) void {
    for (edges) |*e| e.* = false;
    var i: usize = 1;
    while (i < image.len) : (i += 1) {
        edges[i] = @abs(image[i] - image[i - 1]) > 50;
    }
}

fn recognizeCaptcha(bg: []const i32, puzzle: []const i32) usize {
    var bg_edges: [64]bool = undefined;
    var puzzle_edges: [64]bool = undefined;
    detectEdges(bg, &bg_edges);
    detectEdges(puzzle, &puzzle_edges);
    var best_x: usize = 0;
    var best_score: i64 = -1;
    var x: usize = 0;
    while (x + puzzle.len <= bg.len) : (x += 1) {
        var score: i64 = 0;
        for (0..puzzle.len) |y| {
            if (bg_edges[x + y] and puzzle_edges[y]) score += 1;
        }
        if (score > best_score) {
            best_score = score;
            best_x = x;
        }
    }
    return best_x;
}

pub fn main() !void {
    const bg = [_]i32{ 10, 10, 10, 10, 200, 200, 200, 200 };
    const puzzle = [_]i32{ 10, 200, 200, 200 };
    if (recognizeCaptcha(&bg, &puzzle) != 3) return error.TestFailed;
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''// @@BLOG@@
// LeetCode 104107934. 滑动验证码识别 — Dart 版（方案1：前向差分边缘 + 匹配）
List<bool> detectEdges(List<int> image) {
  final edges = List<bool>.filled(image.length, false);
  for (var i = 1; i < image.length; i++) {
    edges[i] = (image[i] - image[i - 1]).abs() > 50;
  }
  return edges;
}

int recognizeCaptcha(List<int> bg, List<int> puzzle) {
  final bgEdges = detectEdges(bg);
  final puzzleEdges = detectEdges(puzzle);
  var bestX = 0;
  var bestScore = -1;
  for (var x = 0; x <= bg.length - puzzle.length; x++) {
    var score = 0;
    for (var y = 0; y < puzzle.length; y++) {
      if (bgEdges[x + y] && puzzleEdges[y]) score++;
    }
    if (score > bestScore) {
      bestScore = score;
      bestX = x;
    }
  }
  return bestX;
}

void main() {
  const bg = <int>[10, 10, 10, 10, 200, 200, 200, 200];
  const puzzle = <int>[10, 200, 200, 200];
  if (recognizeCaptcha(bg, puzzle) != 3) throw StateError('gap failed');
  print('PASS');
}
''',
}

# ---------- s2: Sobel 中心差分 ----------
S2 = {
"rust": '''// @@BLOG@@
// LeetCode 104107934. 滑动验证码识别 — Rust 版（方案2：Sobel 中心差分边缘 + 匹配）
fn detect_edges_sobel(image: &[i32]) -> Vec<bool> {
    let n = image.len();
    let mut edges = vec![false; n];
    if n < 2 {
        return edges;
    }
    edges[0] = (image[1] - image[0]).abs() > 50;
    for i in 1..n - 1 {
        edges[i] = (image[i + 1] - image[i - 1]).abs() > 50;
    }
    edges[n - 1] = (image[n - 1] - image[n - 2]).abs() > 50;
    edges
}

fn recognize_captcha(bg: &[i32], puzzle: &[i32]) -> usize {
    let bg_edges = detect_edges_sobel(bg);
    let puzzle_edges = detect_edges_sobel(puzzle);
    let mut best_x = 0usize;
    let mut best_score: i64 = -1;
    for x in 0..=bg.len() - puzzle.len() {
        let mut score = 0i64;
        for y in 0..puzzle.len() {
            if bg_edges[x + y] && puzzle_edges[y] {
                score += 1;
            }
        }
        if score > best_score {
            best_score = score;
            best_x = x;
        }
    }
    best_x
}

fn main() {
    let bg = [10, 10, 10, 10, 200, 200, 200, 200];
    let puzzle = [10, 200, 200, 200];
    assert_eq!(recognize_captcha(&bg, &puzzle), 3, "gap");
    println!("PASS");
}
''',
"lua": '''-- @@BLOG@@
-- LeetCode 104107934. 滑动验证码识别 — Lua 版（方案2：Sobel 中心差分边缘 + 匹配）
local function detect_edges_sobel(image)
    local n = #image
    local edges = {}
    for i = 1, n do edges[i] = false end
    if n < 2 then return edges end
    edges[1] = math.abs(image[2] - image[1]) > 50
    for i = 2, n - 1 do
        edges[i] = math.abs(image[i + 1] - image[i - 1]) > 50
    end
    edges[n] = math.abs(image[n] - image[n - 1]) > 50
    return edges
end

local function recognize_captcha(bg, puzzle)
    local bg_edges = detect_edges_sobel(bg)
    local puzzle_edges = detect_edges_sobel(puzzle)
    local best_x, best_score = 1, -1
    for x = 1, #bg - #puzzle + 1 do
        local score = 0
        for y = 1, #puzzle do
            if bg_edges[x + y - 1] and puzzle_edges[y] then score = score + 1 end
        end
        if score > best_score then
            best_score = score
            best_x = x
        end
    end
    return best_x - 1
end

local bg = {10, 10, 10, 10, 200, 200, 200, 200}
local puzzle = {10, 200, 200, 200}
assert(recognize_captcha(bg, puzzle) == 3, "gap")
print("PASS")
''',
"c": '''/* @@BLOG@@
 * LeetCode 104107934. 滑动验证码识别 — C 版（方案2：Sobel 中心差分边缘 + 匹配）
 */
#include <stdio.h>
#include <stdlib.h>

static void detect_edges_sobel(const int *image, int n, int *edges) {
    for (int i = 0; i < n; i++) edges[i] = 0;
    if (n < 2) return;
    edges[0] = abs(image[1] - image[0]) > 50;
    for (int i = 1; i < n - 1; i++) edges[i] = abs(image[i + 1] - image[i - 1]) > 50;
    edges[n - 1] = abs(image[n - 1] - image[n - 2]) > 50;
}

static int recognize_captcha(const int *bg, int bn, const int *puzzle, int pn) {
    int bg_edges[64], puzzle_edges[64];
    detect_edges_sobel(bg, bn, bg_edges);
    detect_edges_sobel(puzzle, pn, puzzle_edges);
    int best_x = 0;
    long best_score = -1;
    for (int x = 0; x <= bn - pn; x++) {
        long score = 0;
        for (int y = 0; y < pn; y++)
            if (bg_edges[x + y] && puzzle_edges[y]) score++;
        if (score > best_score) { best_score = score; best_x = x; }
    }
    return best_x;
}

int main(void) {
    int bg[8] = {10, 10, 10, 10, 200, 200, 200, 200};
    int puzzle[4] = {10, 200, 200, 200};
    if (recognize_captcha(bg, 8, puzzle, 4) != 3) { printf("gap failed\\n"); return 1; }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''// @@BLOG@@
// LeetCode 104107934. 滑动验证码识别 — C++ 版（方案2：Sobel 中心差分边缘 + 匹配）
#include <cmath>
#include <iostream>
#include <vector>

static std::vector<bool> detect_edges_sobel(const std::vector<int> &image) {
    int n = static_cast<int>(image.size());
    std::vector<bool> edges(n, false);
    if (n < 2) return edges;
    edges[0] = std::abs(image[1] - image[0]) > 50;
    for (int i = 1; i < n - 1; ++i) {
        edges[i] = std::abs(image[i + 1] - image[i - 1]) > 50;
    }
    edges[n - 1] = std::abs(image[n - 1] - image[n - 2]) > 50;
    return edges;
}

static int recognize_captcha(const std::vector<int> &bg, const std::vector<int> &puzzle) {
    auto bg_edges = detect_edges_sobel(bg);
    auto puzzle_edges = detect_edges_sobel(puzzle);
    int best_x = 0;
    long long best_score = -1;
    for (size_t x = 0; x + puzzle.size() <= bg.size(); ++x) {
        long long score = 0;
        for (size_t y = 0; y < puzzle.size(); ++y) {
            if (bg_edges[x + y] && puzzle_edges[y]) ++score;
        }
        if (score > best_score) { best_score = score; best_x = static_cast<int>(x); }
    }
    return best_x;
}

int main() {
    std::vector<int> bg = {10, 10, 10, 10, 200, 200, 200, 200};
    std::vector<int> puzzle = {10, 200, 200, 200};
    if (recognize_captcha(bg, puzzle) != 3) { std::cout << "gap failed" << std::endl; return 1; }
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''# @@BLOG@@
# LeetCode 104107934. 滑动验证码识别 — R 版（方案2：Sobel 中心差分边缘 + 匹配）
detect_edges_sobel <- function(image) {
  n <- length(image)
  edges <- rep(FALSE, n)
  if (n < 2L) return(edges)
  edges[1] <- abs(image[2] - image[1]) > 50
  for (i in 2:(n - 1L)) {
    edges[i] <- abs(image[i + 1L] - image[i - 1L]) > 50
  }
  edges[n] <- abs(image[n] - image[n - 1L]) > 50
  edges
}

recognize_captcha <- function(bg, puzzle) {
  bg_edges <- detect_edges_sobel(bg)
  puzzle_edges <- detect_edges_sobel(puzzle)
  best_x <- 1L
  best_score <- -1L
  for (x in 1:(length(bg) - length(puzzle) + 1L)) {
    score <- 0L
    for (y in 1:length(puzzle)) {
      if (bg_edges[x + y - 1L] && puzzle_edges[y]) score <- score + 1L
    }
    if (score > best_score) {
      best_score <- score
      best_x <- x
    }
  }
  as.integer(best_x - 1L)
}

bg <- c(10, 10, 10, 10, 200, 200, 200, 200)
puzzle <- c(10, 200, 200, 200)
stopifnot(recognize_captcha(bg, puzzle) == 3L)
cat("PASS\\n")
''',
"zig": '''// @@BLOG@@
// LeetCode 104107934. 滑动验证码识别 — Zig 版（方案2：Sobel 中心差分边缘 + 匹配）
const std = @import("std");

fn detectEdgesSobel(image: []const i32, edges: []bool) void {
    const n = image.len;
    for (edges) |*e| e.* = false;
    if (n < 2) return;
    edges[0] = @abs(image[1] - image[0]) > 50;
    var i: usize = 1;
    while (i < n - 1) : (i += 1) {
        edges[i] = @abs(image[i + 1] - image[i - 1]) > 50;
    }
    edges[n - 1] = @abs(image[n - 1] - image[n - 2]) > 50;
}

fn recognizeCaptcha(bg: []const i32, puzzle: []const i32) usize {
    var bg_edges: [64]bool = undefined;
    var puzzle_edges: [64]bool = undefined;
    detectEdgesSobel(bg, &bg_edges);
    detectEdgesSobel(puzzle, &puzzle_edges);
    var best_x: usize = 0;
    var best_score: i64 = -1;
    var x: usize = 0;
    while (x + puzzle.len <= bg.len) : (x += 1) {
        var score: i64 = 0;
        for (0..puzzle.len) |y| {
            if (bg_edges[x + y] and puzzle_edges[y]) score += 1;
        }
        if (score > best_score) {
            best_score = score;
            best_x = x;
        }
    }
    return best_x;
}

pub fn main() !void {
    const bg = [_]i32{ 10, 10, 10, 10, 200, 200, 200, 200 };
    const puzzle = [_]i32{ 10, 200, 200, 200 };
    if (recognizeCaptcha(&bg, &puzzle) != 3) return error.TestFailed;
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''// @@BLOG@@
// LeetCode 104107934. 滑动验证码识别 — Dart 版（方案2：Sobel 中心差分边缘 + 匹配）
List<bool> detectEdgesSobel(List<int> image) {
  final n = image.length;
  final edges = List<bool>.filled(n, false);
  if (n < 2) return edges;
  edges[0] = (image[1] - image[0]).abs() > 50;
  for (var i = 1; i < n - 1; i++) {
    edges[i] = (image[i + 1] - image[i - 1]).abs() > 50;
  }
  edges[n - 1] = (image[n - 1] - image[n - 2]).abs() > 50;
  return edges;
}

int recognizeCaptcha(List<int> bg, List<int> puzzle) {
  final bgEdges = detectEdgesSobel(bg);
  final puzzleEdges = detectEdgesSobel(puzzle);
  var bestX = 0;
  var bestScore = -1;
  for (var x = 0; x <= bg.length - puzzle.length; x++) {
    var score = 0;
    for (var y = 0; y < puzzle.length; y++) {
      if (bgEdges[x + y] && puzzleEdges[y]) score++;
    }
    if (score > bestScore) {
      bestScore = score;
      bestX = x;
    }
  }
  return bestX;
}

void main() {
  const bg = <int>[10, 10, 10, 10, 200, 200, 200, 200];
  const puzzle = <int>[10, 200, 200, 200];
  if (recognizeCaptcha(bg, puzzle) != 3) throw StateError('gap failed');
  print('PASS');
}
''',
}

# ---------- s3: NCC 归一化互相关 ----------
S3 = {
"rust": '''// @@BLOG@@
// LeetCode 104107934. 滑动验证码识别 — Rust 版（方案3：NCC 归一化互相关）
fn ncc_match(bg: &[i32], puzzle: &[i32]) -> usize {
    let mut best_x = 0usize;
    let mut best_score = f64::NEG_INFINITY;
    let n = puzzle.len();
    for x in 0..=bg.len() - n {
        let window = &bg[x..x + n];
        let bw: f64 = window.iter().map(|&v| v as f64).sum::<f64>() / n as f64;
        let pw: f64 = puzzle.iter().map(|&v| v as f64).sum::<f64>() / n as f64;
        let (mut num, mut db, mut dp) = (0.0, 0.0, 0.0);
        for i in 0..n {
            let a = window[i] as f64 - bw;
            let b = puzzle[i] as f64 - pw;
            num += a * b;
            db += a * a;
            dp += b * b;
        }
        let denom = db.sqrt() * dp.sqrt();
        let score = if denom != 0.0 { num / denom } else { 0.0 };
        if score > best_score {
            best_score = score;
            best_x = x;
        }
    }
    best_x
}

fn main() {
    let bg = [10, 10, 10, 10, 200, 200, 200, 200];
    let puzzle = [10, 200, 200, 200];
    assert_eq!(ncc_match(&bg, &puzzle), 3, "gap");
    println!("PASS");
}
''',
"lua": '''-- @@BLOG@@
-- LeetCode 104107934. 滑动验证码识别 — Lua 版（方案3：NCC 归一化互相关）
local function ncc_match(bg, puzzle)
    local best_x, best_score = 1, -math.huge
    local n = #puzzle
    for x = 1, #bg - n + 1 do
        local bw, pw = 0, 0
        for i = 0, n - 1 do
            bw = bw + bg[x + i]
            pw = pw + puzzle[i + 1]
        end
        bw = bw / n
        pw = pw / n
        local num, db, dp = 0, 0, 0
        for i = 0, n - 1 do
            local a = bg[x + i] - bw
            local b = puzzle[i + 1] - pw
            num = num + a * b
            db = db + a * a
            dp = dp + b * b
        end
        local denom = math.sqrt(db) * math.sqrt(dp)
        local score = (denom ~= 0) and (num / denom) or 0
        if score > best_score then
            best_score = score
            best_x = x
        end
    end
    return best_x - 1
end

local bg = {10, 10, 10, 10, 200, 200, 200, 200}
local puzzle = {10, 200, 200, 200}
assert(ncc_match(bg, puzzle) == 3, "gap")
print("PASS")
''',
"c": '''/* @@BLOG@@
 * LeetCode 104107934. 滑动验证码识别 — C 版（方案3：NCC 归一化互相关）
 */
#include <math.h>
#include <stdio.h>

static int ncc_match(const int *bg, int bn, const int *puzzle, int pn) {
    int best_x = 0;
    double best_score = -1.0 / 0.0;
    for (int x = 0; x <= bn - pn; x++) {
        double bw = 0, pw = 0;
        for (int i = 0; i < pn; i++) {
            bw += bg[x + i];
            pw += puzzle[i];
        }
        bw /= pn;
        pw /= pn;
        double num = 0, db = 0, dp = 0;
        for (int i = 0; i < pn; i++) {
            double a = bg[x + i] - bw;
            double b = puzzle[i] - pw;
            num += a * b;
            db += a * a;
            dp += b * b;
        }
        double denom = sqrt(db) * sqrt(dp);
        double score = (denom != 0.0) ? (num / denom) : 0.0;
        if (score > best_score) { best_score = score; best_x = x; }
    }
    return best_x;
}

int main(void) {
    int bg[8] = {10, 10, 10, 10, 200, 200, 200, 200};
    int puzzle[4] = {10, 200, 200, 200};
    if (ncc_match(bg, 8, puzzle, 4) != 3) { printf("gap failed\\n"); return 1; }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''// @@BLOG@@
// LeetCode 104107934. 滑动验证码识别 — C++ 版（方案3：NCC 归一化互相关）
#include <cmath>
#include <iostream>
#include <vector>

static int ncc_match(const std::vector<int> &bg, const std::vector<int> &puzzle) {
    int best_x = 0;
    double best_score = -1.0 / 0.0;
    int n = static_cast<int>(puzzle.size());
    for (int x = 0; x + n <= static_cast<int>(bg.size()); ++x) {
        double bw = 0, pw = 0;
        for (int i = 0; i < n; ++i) {
            bw += bg[x + i];
            pw += puzzle[i];
        }
        bw /= n;
        pw /= n;
        double num = 0, db = 0, dp = 0;
        for (int i = 0; i < n; ++i) {
            double a = bg[x + i] - bw;
            double b = puzzle[i] - pw;
            num += a * b;
            db += a * a;
            dp += b * b;
        }
        double denom = std::sqrt(db) * std::sqrt(dp);
        double score = (denom != 0.0) ? (num / denom) : 0.0;
        if (score > best_score) { best_score = score; best_x = x; }
    }
    return best_x;
}

int main() {
    std::vector<int> bg = {10, 10, 10, 10, 200, 200, 200, 200};
    std::vector<int> puzzle = {10, 200, 200, 200};
    if (ncc_match(bg, puzzle) != 3) { std::cout << "gap failed" << std::endl; return 1; }
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''# @@BLOG@@
# LeetCode 104107934. 滑动验证码识别 — R 版（方案3：NCC 归一化互相关）
ncc_match <- function(bg, puzzle) {
  best_x <- 1L
  best_score <- -Inf
  n <- length(puzzle)
  for (x in 1:(length(bg) - n + 1L)) {
    window <- bg[x:(x + n - 1L)]
    bw <- mean(window)
    pw <- mean(puzzle)
    num <- 0; db <- 0; dp <- 0
    for (i in 1:n) {
      a <- window[i] - bw
      b <- puzzle[i] - pw
      num <- num + a * b
      db <- db + a * a
      dp <- dp + b * b
    }
    denom <- sqrt(db) * sqrt(dp)
    score <- if (denom != 0) num / denom else 0
    if (score > best_score) {
      best_score <- score
      best_x <- x
    }
  }
  as.integer(best_x - 1L)
}

bg <- c(10, 10, 10, 10, 200, 200, 200, 200)
puzzle <- c(10, 200, 200, 200)
stopifnot(ncc_match(bg, puzzle) == 3L)
cat("PASS\\n")
''',
"zig": '''// @@BLOG@@
// LeetCode 104107934. 滑动验证码识别 — Zig 版（方案3：NCC 归一化互相关）
const std = @import("std");

fn nccMatch(bg: []const i32, puzzle: []const i32) usize {
    var best_x: usize = 0;
    var best_score = -std.math.inf(f64);
    const n = puzzle.len;
    var x: usize = 0;
    while (x + n <= bg.len) : (x += 1) {
        var bw: f64 = 0;
        var pw: f64 = 0;
        for (0..n) |i| {
            bw += @as(f64, @floatFromInt(bg[x + i]));
            pw += @as(f64, @floatFromInt(puzzle[i]));
        }
        bw /= @floatFromInt(n);
        pw /= @floatFromInt(n);
        var num: f64 = 0;
        var db: f64 = 0;
        var dp: f64 = 0;
        for (0..n) |i| {
            const a = @as(f64, @floatFromInt(bg[x + i])) - bw;
            const b = @as(f64, @floatFromInt(puzzle[i])) - pw;
            num += a * b;
            db += a * a;
            dp += b * b;
        }
        const denom = @sqrt(db) * @sqrt(dp);
        const score = if (denom != 0.0) num / denom else 0.0;
        if (score > best_score) {
            best_score = score;
            best_x = x;
        }
    }
    return best_x;
}

pub fn main() !void {
    const bg = [_]i32{ 10, 10, 10, 10, 200, 200, 200, 200 };
    const puzzle = [_]i32{ 10, 200, 200, 200 };
    if (nccMatch(&bg, &puzzle) != 3) return error.TestFailed;
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''// @@BLOG@@
// LeetCode 104107934. 滑动验证码识别 — Dart 版（方案3：NCC 归一化互相关）
import 'dart:math' as math;

int nccMatch(List<int> bg, List<int> puzzle) {
  var bestX = 0;
  var bestScore = -double.infinity;
  final n = puzzle.length;
  for (var x = 0; x + n <= bg.length; x++) {
    var bw = 0.0, pw = 0.0;
    for (var i = 0; i < n; i++) {
      bw += bg[x + i];
      pw += puzzle[i];
    }
    bw /= n;
    pw /= n;
    var num = 0.0, db = 0.0, dp = 0.0;
    for (var i = 0; i < n; i++) {
      final a = bg[x + i] - bw;
      final b = puzzle[i] - pw;
      num += a * b;
      db += a * a;
      dp += b * b;
    }
    final denom = math.sqrt(db) * math.sqrt(dp);
    final score = denom != 0.0 ? num / denom : 0.0;
    if (score > bestScore) {
      bestScore = score;
      bestX = x;
    }
  }
  return bestX;
}

void main() {
  const bg = <int>[10, 10, 10, 10, 200, 200, 200, 200];
  const puzzle = <int>[10, 200, 200, 200];
  if (nccMatch(bg, puzzle) != 3) throw StateError('gap failed');
  print('PASS');
}
''',
}

# ---------- s4: SAD 绝对差和 ----------
S4 = {
"rust": '''// @@BLOG@@
// LeetCode 104107934. 滑动验证码识别 — Rust 版（方案4：SAD 绝对差和最佳窗口）
fn best_match_window(bg: &[i32], puzzle: &[i32]) -> (usize, i64) {
    let mut best_x = 0usize;
    let mut best_score = i64::MAX;
    let n = puzzle.len();
    for x in 0..=bg.len() - n {
        let mut score = 0i64;
        for y in 0..n {
            score += (bg[x + y] - puzzle[y]).abs() as i64;
        }
        if score < best_score {
            best_score = score;
            best_x = x;
        }
    }
    (best_x, best_score)
}

fn main() {
    let bg = [10, 10, 10, 10, 200, 200, 200, 200];
    let puzzle = [10, 200, 200, 200];
    assert_eq!(best_match_window(&bg, &puzzle), (3, 0), "gap");
    println!("PASS");
}
''',
"lua": '''-- @@BLOG@@
-- LeetCode 104107934. 滑动验证码识别 — Lua 版（方案4：SAD 绝对差和最佳窗口）
local function best_match_window(bg, puzzle)
    local best_x, best_score = 1, math.huge
    local n = #puzzle
    for x = 1, #bg - n + 1 do
        local score = 0
        for y = 0, n - 1 do
            score = score + math.abs(bg[x + y] - puzzle[y + 1])
        end
        if score < best_score then
            best_score = score
            best_x = x
        end
    end
    return best_x - 1, best_score
end

local bg = {10, 10, 10, 10, 200, 200, 200, 200}
local puzzle = {10, 200, 200, 200}
local bx, bs = best_match_window(bg, puzzle)
assert(bx == 3 and bs == 0, "gap failed")
print("PASS")
''',
"c": '''/* @@BLOG@@
 * LeetCode 104107934. 滑动验证码识别 — C 版（方案4：SAD 绝对差和最佳窗口）
 */
#include <stdio.h>
#include <stdlib.h>

static void best_match_window(const int *bg, int bn, const int *puzzle, int pn, int *out_x, long *out_score) {
    int best_x = 0;
    long best_score = 1L << 60;
    for (int x = 0; x <= bn - pn; x++) {
        long score = 0;
        for (int y = 0; y < pn; y++) score += labs(bg[x + y] - puzzle[y]);
        if (score < best_score) { best_score = score; best_x = x; }
    }
    *out_x = best_x;
    *out_score = best_score;
}

int main(void) {
    int bg[8] = {10, 10, 10, 10, 200, 200, 200, 200};
    int puzzle[4] = {10, 200, 200, 200};
    int bx;
    long bs;
    best_match_window(bg, 8, puzzle, 4, &bx, &bs);
    if (bx != 3 || bs != 0) { printf("gap failed\\n"); return 1; }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''// @@BLOG@@
// LeetCode 104107934. 滑动验证码识别 — C++ 版（方案4：SAD 绝对差和最佳窗口）
#include <cmath>
#include <iostream>
#include <vector>

static std::pair<int, long long> best_match_window(const std::vector<int> &bg, const std::vector<int> &puzzle) {
    int best_x = 0;
    long long best_score = 1LL << 60;
    int n = static_cast<int>(puzzle.size());
    for (int x = 0; x + n <= static_cast<int>(bg.size()); ++x) {
        long long score = 0;
        for (int y = 0; y < n; ++y) score += std::abs(bg[x + y] - puzzle[y]);
        if (score < best_score) { best_score = score; best_x = x; }
    }
    return {best_x, best_score};
}

int main() {
    std::vector<int> bg = {10, 10, 10, 10, 200, 200, 200, 200};
    std::vector<int> puzzle = {10, 200, 200, 200};
    auto [bx, bs] = best_match_window(bg, puzzle);
    if (bx != 3 || bs != 0) { std::cout << "gap failed" << std::endl; return 1; }
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''# @@BLOG@@
# LeetCode 104107934. 滑动验证码识别 — R 版（方案4：SAD 绝对差和最佳窗口）
best_match_window <- function(bg, puzzle) {
  best_x <- 1L
  best_score <- Inf
  n <- length(puzzle)
  for (x in 1:(length(bg) - n + 1L)) {
    score <- 0
    for (y in 0:(n - 1L)) {
      score <- score + abs(bg[x + y] - puzzle[y + 1L])
    }
    if (score < best_score) {
      best_score <- score
      best_x <- x
    }
  }
  c(as.integer(best_x - 1L), as.integer(best_score))
}

bg <- c(10, 10, 10, 10, 200, 200, 200, 200)
puzzle <- c(10, 200, 200, 200)
got <- best_match_window(bg, puzzle)
stopifnot(got[1] == 3L && got[2] == 0L)
cat("PASS\\n")
''',
"zig": '''// @@BLOG@@
// LeetCode 104107934. 滑动验证码识别 — Zig 版（方案4：SAD 绝对差和最佳窗口）
const std = @import("std");

fn bestMatchWindow(bg: []const i32, puzzle: []const i32) struct { x: usize, score: i64 } {
    var best_x: usize = 0;
    var best_score: i64 = std.math.maxInt(i64);
    const n = puzzle.len;
    var x: usize = 0;
    while (x + n <= bg.len) : (x += 1) {
        var score: i64 = 0;
        for (0..n) |y| {
            score += @abs(bg[x + y] - puzzle[y]);
        }
        if (score < best_score) {
            best_score = score;
            best_x = x;
        }
    }
    return .{ .x = best_x, .score = best_score };
}

pub fn main() !void {
    const bg = [_]i32{ 10, 10, 10, 10, 200, 200, 200, 200 };
    const puzzle = [_]i32{ 10, 200, 200, 200 };
    const r = bestMatchWindow(&bg, &puzzle);
    if (r.x != 3 or r.score != 0) return error.TestFailed;
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''// @@BLOG@@
// LeetCode 104107934. 滑动验证码识别 — Dart 版（方案4：SAD 绝对差和最佳窗口）
List<int> bestMatchWindow(List<int> bg, List<int> puzzle) {
  var bestX = 0;
  var bestScore = 1 << 60;
  final n = puzzle.length;
  for (var x = 0; x + n <= bg.length; x++) {
    var score = 0;
    for (var y = 0; y < n; y++) {
      score += (bg[x + y] - puzzle[y]).abs();
    }
    if (score < bestScore) {
      bestScore = score;
      bestX = x;
    }
  }
  return [bestX, bestScore];
}

void main() {
  const bg = <int>[10, 10, 10, 10, 200, 200, 200, 200];
  const puzzle = <int>[10, 200, 200, 200];
  final got = bestMatchWindow(bg, puzzle);
  if (got[0] != 3 || got[1] != 0) throw StateError('gap failed');
  print('PASS');
}
''',
}

# ---------- s5: findGap（边缘响应曲线） ----------
S5 = {
"rust": '''// @@BLOG@@
// LeetCode 104107934. 滑动验证码识别 — Rust 版（方案5：边缘匹配 findGap 响应曲线）
fn detect_edges(image: &[i32]) -> Vec<bool> {
    let mut edges = vec![false; image.len()];
    for i in 1..image.len() {
        edges[i] = (image[i] - image[i - 1]).abs() > 50;
    }
    edges
}

fn find_gap(bg: &[i32], puzzle: &[i32]) -> (usize, Vec<i64>) {
    let bg_edges = detect_edges(bg);
    let puzzle_edges = detect_edges(puzzle);
    let mut responses: Vec<i64> = vec![];
    for x in 0..=bg.len() - puzzle.len() {
        let mut score = 0i64;
        for y in 0..puzzle.len() {
            if bg_edges[x + y] && puzzle_edges[y] {
                score += 1;
            }
        }
        responses.push(score);
    }
    let mut best_x = 0usize;
    for i in 1..responses.len() {
        if responses[i] > responses[best_x] {
            best_x = i;
        }
    }
    (best_x, responses)
}

fn main() {
    let bg = [10, 10, 10, 10, 200, 200, 200, 200];
    let puzzle = [10, 200, 200, 200];
    let (best_x, responses) = find_gap(&bg, &puzzle);
    assert_eq!(best_x, 3, "gap");
    assert_eq!(responses, vec![0, 0, 0, 1, 0], "responses");
    println!("PASS");
}
''',
"lua": '''-- @@BLOG@@
-- LeetCode 104107934. 滑动验证码识别 — Lua 版（方案5：边缘匹配 findGap 响应曲线）
local function detect_edges(image)
    local edges = {}
    for i = 1, #image do edges[i] = false end
    for i = 2, #image do
        edges[i] = math.abs(image[i] - image[i - 1]) > 50
    end
    return edges
end

local function find_gap(bg, puzzle)
    local bg_edges = detect_edges(bg)
    local puzzle_edges = detect_edges(puzzle)
    local responses = {}
    for x = 1, #bg - #puzzle + 1 do
        local score = 0
        for y = 1, #puzzle do
            if bg_edges[x + y - 1] and puzzle_edges[y] then score = score + 1 end
        end
        responses[#responses + 1] = score
    end
    local best_x = 1
    for i = 2, #responses do
        if responses[i] > responses[best_x] then best_x = i end
    end
    return best_x - 1, responses
end

local bg = {10, 10, 10, 10, 200, 200, 200, 200}
local puzzle = {10, 200, 200, 200}
local bx, resp = find_gap(bg, puzzle)
assert(bx == 3, "gap")
local want_resp = {0, 0, 0, 1, 0}
for i = 1, 5 do assert(resp[i] == want_resp[i], "responses") end
print("PASS")
''',
"c": '''/* @@BLOG@@
 * LeetCode 104107934. 滑动验证码识别 — C 版（方案5：边缘匹配 findGap 响应曲线）
 */
#include <stdio.h>
#include <stdlib.h>

static void detect_edges(const int *image, int n, int *edges) {
    for (int i = 0; i < n; i++) edges[i] = 0;
    for (int i = 1; i < n; i++) edges[i] = abs(image[i] - image[i - 1]) > 50;
}

static int find_gap(const int *bg, int bn, const int *puzzle, int pn, long *responses, int *resp_len) {
    int bg_edges[64], puzzle_edges[64];
    detect_edges(bg, bn, bg_edges);
    detect_edges(puzzle, pn, puzzle_edges);
    int len = 0;
    for (int x = 0; x <= bn - pn; x++) {
        long score = 0;
        for (int y = 0; y < pn; y++)
            if (bg_edges[x + y] && puzzle_edges[y]) score++;
        responses[len++] = score;
    }
    int best_x = 0;
    for (int i = 1; i < len; i++)
        if (responses[i] > responses[best_x]) best_x = i;
    *resp_len = len;
    return best_x;
}

int main(void) {
    int bg[8] = {10, 10, 10, 10, 200, 200, 200, 200};
    int puzzle[4] = {10, 200, 200, 200};
    long responses[64];
    int resp_len;
    int bx = find_gap(bg, 8, puzzle, 4, responses, &resp_len);
    if (bx != 3) { printf("gap failed\\n"); return 1; }
    long want[5] = {0, 0, 0, 1, 0};
    for (int i = 0; i < 5; i++)
        if (responses[i] != want[i]) { printf("responses failed\\n"); return 1; }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''// @@BLOG@@
// LeetCode 104107934. 滑动验证码识别 — C++ 版（方案5：边缘匹配 findGap 响应曲线）
#include <cmath>
#include <iostream>
#include <vector>

static std::vector<bool> detect_edges(const std::vector<int> &image) {
    std::vector<bool> edges(image.size(), false);
    for (size_t i = 1; i < image.size(); ++i) {
        edges[i] = std::abs(image[i] - image[i - 1]) > 50;
    }
    return edges;
}

static std::pair<int, std::vector<long long>> find_gap(const std::vector<int> &bg, const std::vector<int> &puzzle) {
    auto bg_edges = detect_edges(bg);
    auto puzzle_edges = detect_edges(puzzle);
    std::vector<long long> responses;
    for (size_t x = 0; x + puzzle.size() <= bg.size(); ++x) {
        long long score = 0;
        for (size_t y = 0; y < puzzle.size(); ++y) {
            if (bg_edges[x + y] && puzzle_edges[y]) ++score;
        }
        responses.push_back(score);
    }
    int best_x = 0;
    for (size_t i = 1; i < responses.size(); ++i) {
        if (responses[i] > responses[best_x]) best_x = static_cast<int>(i);
    }
    return {best_x, responses};
}

int main() {
    std::vector<int> bg = {10, 10, 10, 10, 200, 200, 200, 200};
    std::vector<int> puzzle = {10, 200, 200, 200};
    auto [bx, resp] = find_gap(bg, puzzle);
    if (bx != 3) { std::cout << "gap failed" << std::endl; return 1; }
    if (resp != std::vector<long long>({0, 0, 0, 1, 0})) { std::cout << "responses failed" << std::endl; return 1; }
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''# @@BLOG@@
# LeetCode 104107934. 滑动验证码识别 — R 版（方案5：边缘匹配 findGap 响应曲线）
detect_edges <- function(image) {
  edges <- rep(FALSE, length(image))
  for (i in 2:length(image)) {
    edges[i] <- abs(image[i] - image[i - 1L]) > 50
  }
  edges
}

find_gap <- function(bg, puzzle) {
  bg_edges <- detect_edges(bg)
  puzzle_edges <- detect_edges(puzzle)
  responses <- c()
  for (x in 1:(length(bg) - length(puzzle) + 1L)) {
    score <- 0L
    for (y in 1:length(puzzle)) {
      if (bg_edges[x + y - 1L] && puzzle_edges[y]) score <- score + 1L
    }
    responses <- c(responses, score)
  }
  best_x <- 1L
  for (i in 2:length(responses)) {
    if (responses[i] > responses[best_x]) best_x <- i
  }
  list(as.integer(best_x - 1L), as.integer(responses))
}

bg <- c(10, 10, 10, 10, 200, 200, 200, 200)
puzzle <- c(10, 200, 200, 200)
got <- find_gap(bg, puzzle)
stopifnot(got[[1]] == 3L)
stopifnot(identical(got[[2]], as.integer(c(0, 0, 0, 1, 0))))
cat("PASS\\n")
''',
"zig": '''// @@BLOG@@
// LeetCode 104107934. 滑动验证码识别 — Zig 版（方案5：边缘匹配 findGap 响应曲线）
const std = @import("std");

fn detectEdges(image: []const i32, edges: []bool) void {
    for (edges) |*e| e.* = false;
    var i: usize = 1;
    while (i < image.len) : (i += 1) {
        edges[i] = @abs(image[i] - image[i - 1]) > 50;
    }
}

fn findGap(bg: []const i32, puzzle: []const i32, responses: []i64) usize {
    var bg_edges: [64]bool = undefined;
    var puzzle_edges: [64]bool = undefined;
    detectEdges(bg, &bg_edges);
    detectEdges(puzzle, &puzzle_edges);
    var len: usize = 0;
    var x: usize = 0;
    while (x + puzzle.len <= bg.len) : (x += 1) {
        var score: i64 = 0;
        for (0..puzzle.len) |y| {
            if (bg_edges[x + y] and puzzle_edges[y]) score += 1;
        }
        responses[len] = score;
        len += 1;
    }
    var best_x: usize = 0;
    for (1..len) |i| {
        if (responses[i] > responses[best_x]) best_x = i;
    }
    return best_x;
}

pub fn main() !void {
    const bg = [_]i32{ 10, 10, 10, 10, 200, 200, 200, 200 };
    const puzzle = [_]i32{ 10, 200, 200, 200 };
    var responses: [64]i64 = undefined;
    const bx = findGap(&bg, &puzzle, &responses);
    if (bx != 3) return error.TestFailed;
    const want = [_]i64{ 0, 0, 0, 1, 0 };
    for (want, 0..) |w, i| {
        if (responses[i] != w) return error.TestFailed;
    }
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''// @@BLOG@@
// LeetCode 104107934. 滑动验证码识别 — Dart 版（方案5：边缘匹配 findGap 响应曲线）
List<bool> detectEdges(List<int> image) {
  final edges = List<bool>.filled(image.length, false);
  for (var i = 1; i < image.length; i++) {
    edges[i] = (image[i] - image[i - 1]).abs() > 50;
  }
  return edges;
}

List<dynamic> findGap(List<int> bg, List<int> puzzle) {
  final bgEdges = detectEdges(bg);
  final puzzleEdges = detectEdges(puzzle);
  final responses = <int>[];
  for (var x = 0; x <= bg.length - puzzle.length; x++) {
    var score = 0;
    for (var y = 0; y < puzzle.length; y++) {
      if (bgEdges[x + y] && puzzleEdges[y]) score++;
    }
    responses.add(score);
  }
  var bestX = 0;
  for (var i = 1; i < responses.length; i++) {
    if (responses[i] > responses[bestX]) bestX = i;
  }
  return [bestX, responses];
}

void main() {
  const bg = <int>[10, 10, 10, 10, 200, 200, 200, 200];
  const puzzle = <int>[10, 200, 200, 200];
  final got = findGap(bg, puzzle);
  if (got[0] != 3) throw StateError('gap failed');
  if (got[1].toString() != '[0, 0, 0, 1, 0]') throw StateError('responses failed');
  print('PASS');
}
''',
}

# ---------- s6: 合成数据 ----------
S6 = {
"rust": '''// @@BLOG@@
// LeetCode 104107934. 滑动验证码识别 — Rust 版（方案6：合成滑块数据 buildSynthetic）
fn build_synthetic(bg_len: usize, gap_start: usize, puzzle_len: usize) -> (Vec<i32>, Vec<i32>) {
    let mut bg = vec![10i32; bg_len];
    for i in gap_start..std::cmp::min(gap_start + puzzle_len, bg_len) {
        bg[i] = 200;
    }
    let puzzle = bg[gap_start..std::cmp::min(gap_start + puzzle_len, bg_len)].to_vec();
    (bg, puzzle)
}

fn main() {
    let (bg, puzzle) = build_synthetic(8, 3, 4);
    assert_eq!(bg, vec![10, 10, 10, 200, 200, 200, 200, 10], "bg");
    assert_eq!(puzzle, vec![200, 200, 200, 200], "puzzle");
    assert_eq!(puzzle.len(), 4, "puzzle length");
    assert_eq!(bg.len(), 8, "bg length");
    println!("PASS");
}
''',
"lua": '''-- @@BLOG@@
-- LeetCode 104107934. 滑动验证码识别 — Lua 版（方案6：合成滑块数据 buildSynthetic）
local function build_synthetic(bg_len, gap_start, puzzle_len)
    local bg = {}
    for i = 1, bg_len do bg[i] = 10 end
    for i = gap_start + 1, math.min(gap_start + puzzle_len, bg_len) do
        bg[i] = 200
    end
    local puzzle = {}
    for i = 1, puzzle_len do
        puzzle[i] = bg[gap_start + i]
    end
    return bg, puzzle
end

local bg, puzzle = build_synthetic(8, 3, 4)
local want_bg = {10, 10, 10, 200, 200, 200, 200, 10}
for i = 1, 8 do assert(bg[i] == want_bg[i], "bg") end
local want_pz = {200, 200, 200, 200}
for i = 1, 4 do assert(puzzle[i] == want_pz[i], "puzzle") end
assert(#puzzle == 4, "puzzle length")
assert(#bg == 8, "bg length")
print("PASS")
''',
"c": '''/* @@BLOG@@
 * LeetCode 104107934. 滑动验证码识别 — C 版（方案6：合成滑块数据 buildSynthetic）
 */
#include <stdio.h>

static void build_synthetic(int bg_len, int gap_start, int puzzle_len, int *bg, int *puzzle) {
    for (int i = 0; i < bg_len; i++) bg[i] = 10;
    for (int i = gap_start; i < gap_start + puzzle_len && i < bg_len; i++) bg[i] = 200;
    for (int i = 0; i < puzzle_len; i++) puzzle[i] = bg[gap_start + i];
}

int main(void) {
    int bg[8], puzzle[4];
    build_synthetic(8, 3, 4, bg, puzzle);
    int want_bg[8] = {10, 10, 10, 200, 200, 200, 200, 10};
    int want_pz[4] = {200, 200, 200, 200};
    for (int i = 0; i < 8; i++)
        if (bg[i] != want_bg[i]) { printf("bg failed\\n"); return 1; }
    for (int i = 0; i < 4; i++)
        if (puzzle[i] != want_pz[i]) { printf("puzzle failed\\n"); return 1; }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''// @@BLOG@@
// LeetCode 104107934. 滑动验证码识别 — C++ 版（方案6：合成滑块数据 buildSynthetic）
#include <algorithm>
#include <iostream>
#include <vector>

static std::pair<std::vector<int>, std::vector<int>> build_synthetic(int bg_len, int gap_start, int puzzle_len) {
    std::vector<int> bg(bg_len, 10);
    for (int i = gap_start; i < std::min(gap_start + puzzle_len, bg_len); ++i) bg[i] = 200;
    std::vector<int> puzzle(bg.begin() + gap_start, bg.begin() + std::min(gap_start + puzzle_len, bg_len));
    return {bg, puzzle};
}

int main() {
    auto [bg, puzzle] = build_synthetic(8, 3, 4);
    if (bg != std::vector<int>({10, 10, 10, 200, 200, 200, 200, 10})) { std::cout << "bg failed" << std::endl; return 1; }
    if (puzzle != std::vector<int>({200, 200, 200, 200})) { std::cout << "puzzle failed" << std::endl; return 1; }
    if (puzzle.size() != 4 || bg.size() != 8) { std::cout << "lens failed" << std::endl; return 1; }
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''# @@BLOG@@
# LeetCode 104107934. 滑动验证码识别 — R 版（方案6：合成滑块数据 buildSynthetic）
build_synthetic <- function(bg_len, gap_start, puzzle_len) {
  bg <- rep(10L, bg_len)
  for (i in (gap_start + 1L):min(gap_start + puzzle_len, bg_len)) {
    bg[i] <- 200L
  }
  puzzle <- bg[(gap_start + 1L):(gap_start + puzzle_len)]
  list(bg, puzzle)
}

got <- build_synthetic(8L, 3L, 4L)
stopifnot(identical(as.integer(got[[1]]), as.integer(c(10, 10, 10, 200, 200, 200, 200, 10))))
stopifnot(identical(as.integer(got[[2]]), as.integer(c(200, 200, 200, 200))))
stopifnot(length(got[[2]]) == 4L)
stopifnot(length(got[[1]]) == 8L)
cat("PASS\\n")
''',
"zig": '''// @@BLOG@@
// LeetCode 104107934. 滑动验证码识别 — Zig 版（方案6：合成滑块数据 buildSynthetic）
const std = @import("std");

fn buildSynthetic(bg: []i32, puzzle: []i32, gap_start: usize, puzzle_len: usize) void {
    for (bg) |*v| v.* = 10;
    var i = gap_start;
    while (i < @min(gap_start + puzzle_len, bg.len)) : (i += 1) {
        bg[i] = 200;
    }
    for (0..puzzle_len) |k| {
        puzzle[k] = bg[gap_start + k];
    }
}

pub fn main() !void {
    var bg: [8]i32 = undefined;
    var puzzle: [4]i32 = undefined;
    buildSynthetic(&bg, &puzzle, 3, 4);
    const want_bg = [_]i32{ 10, 10, 10, 200, 200, 200, 200, 10 };
    const want_pz = [_]i32{ 200, 200, 200, 200 };
    for (want_bg, 0..) |w, i| {
        if (bg[i] != w) return error.TestFailed;
    }
    for (want_pz, 0..) |w, i| {
        if (puzzle[i] != w) return error.TestFailed;
    }
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''// @@BLOG@@
// LeetCode 104107934. 滑动验证码识别 — Dart 版（方案6：合成滑块数据 buildSynthetic）
List<List<int>> buildSynthetic(int bgLen, int gapStart, int puzzleLen) {
  final bg = List<int>.filled(bgLen, 10);
  for (var i = gapStart; i < (gapStart + puzzleLen).clamp(0, bgLen); i++) {
    bg[i] = 200;
  }
  final puzzle = bg.sublist(gapStart, (gapStart + puzzleLen).clamp(0, bgLen));
  return [bg, puzzle];
}

void main() {
  final got = buildSynthetic(8, 3, 4);
  if (got[0].toString() != '[10, 10, 10, 200, 200, 200, 200, 10]') throw StateError('bg failed');
  if (got[1].toString() != '[200, 200, 200, 200]') throw StateError('puzzle failed');
  if (got[1].length != 4 || got[0].length != 8) throw StateError('lens failed');
  print('PASS');
}
''',
}

# ---------- s7: 全流程（合成 + 识别） ----------
S7 = {
"rust": '''// @@BLOG@@
// LeetCode 104107934. 滑动验证码识别 — Rust 版（方案7：合成数据 + 识别全流程）
fn detect_edges(image: &[i32]) -> Vec<bool> {
    let mut edges = vec![false; image.len()];
    for i in 1..image.len() {
        edges[i] = (image[i] - image[i - 1]).abs() > 50;
    }
    edges
}

fn recognize_captcha(bg: &[i32], puzzle: &[i32]) -> usize {
    let bg_edges = detect_edges(bg);
    let puzzle_edges = detect_edges(puzzle);
    let mut best_x = 0usize;
    let mut best_score: i64 = -1;
    for x in 0..=bg.len() - puzzle.len() {
        let mut score = 0i64;
        for y in 0..puzzle.len() {
            if bg_edges[x + y] && puzzle_edges[y] {
                score += 1;
            }
        }
        if score > best_score {
            best_score = score;
            best_x = x;
        }
    }
    best_x
}

fn build_synthetic(bg_len: usize, gap_start: usize, puzzle_len: usize) -> (Vec<i32>, Vec<i32>) {
    let mut bg = vec![10i32; bg_len];
    for i in gap_start..std::cmp::min(gap_start + puzzle_len, bg_len) {
        bg[i] = 200;
    }
    let puzzle = bg[gap_start..std::cmp::min(gap_start + puzzle_len, bg_len)].to_vec();
    (bg, puzzle)
}

fn main() {
    let (bg, puzzle) = build_synthetic(8, 3, 4);
    // 与 TS 原文件一致：合成数据下 puzzle 边缘全平，识别结果为 0
    assert_eq!(recognize_captcha(&bg, &puzzle), 0, "synthetic");
    println!("PASS");
}
''',
"lua": '''-- @@BLOG@@
-- LeetCode 104107934. 滑动验证码识别 — Lua 版（方案7：合成数据 + 识别全流程）
local function detect_edges(image)
    local edges = {}
    for i = 1, #image do edges[i] = false end
    for i = 2, #image do
        edges[i] = math.abs(image[i] - image[i - 1]) > 50
    end
    return edges
end

local function recognize_captcha(bg, puzzle)
    local bg_edges = detect_edges(bg)
    local puzzle_edges = detect_edges(puzzle)
    local best_x, best_score = 1, -1
    for x = 1, #bg - #puzzle + 1 do
        local score = 0
        for y = 1, #puzzle do
            if bg_edges[x + y - 1] and puzzle_edges[y] then score = score + 1 end
        end
        if score > best_score then
            best_score = score
            best_x = x
        end
    end
    return best_x - 1
end

local function build_synthetic(bg_len, gap_start, puzzle_len)
    local bg = {}
    for i = 1, bg_len do bg[i] = 10 end
    for i = gap_start + 1, math.min(gap_start + puzzle_len, bg_len) do
        bg[i] = 200
    end
    local puzzle = {}
    for i = 1, puzzle_len do
        puzzle[i] = bg[gap_start + i]
    end
    return bg, puzzle
end

local bg, puzzle = build_synthetic(8, 3, 4)
-- 与 TS 原文件一致：合成数据下 puzzle 边缘全平，识别结果为 0
assert(recognize_captcha(bg, puzzle) == 0, "synthetic")
print("PASS")
''',
"c": '''/* @@BLOG@@
 * LeetCode 104107934. 滑动验证码识别 — C 版（方案7：合成数据 + 识别全流程）
 */
#include <stdio.h>
#include <stdlib.h>

static void detect_edges(const int *image, int n, int *edges) {
    for (int i = 0; i < n; i++) edges[i] = 0;
    for (int i = 1; i < n; i++) edges[i] = abs(image[i] - image[i - 1]) > 50;
}

static int recognize_captcha(const int *bg, int bn, const int *puzzle, int pn) {
    int bg_edges[64], puzzle_edges[64];
    detect_edges(bg, bn, bg_edges);
    detect_edges(puzzle, pn, puzzle_edges);
    int best_x = 0;
    long best_score = -1;
    for (int x = 0; x <= bn - pn; x++) {
        long score = 0;
        for (int y = 0; y < pn; y++)
            if (bg_edges[x + y] && puzzle_edges[y]) score++;
        if (score > best_score) { best_score = score; best_x = x; }
    }
    return best_x;
}

static void build_synthetic(int bg_len, int gap_start, int puzzle_len, int *bg, int *puzzle) {
    for (int i = 0; i < bg_len; i++) bg[i] = 10;
    for (int i = gap_start; i < gap_start + puzzle_len && i < bg_len; i++) bg[i] = 200;
    for (int i = 0; i < puzzle_len; i++) puzzle[i] = bg[gap_start + i];
}

int main(void) {
    int bg[8], puzzle[4];
    build_synthetic(8, 3, 4, bg, puzzle);
    /* 与 TS 原文件一致：合成数据下 puzzle 边缘全平，识别结果为 0 */
    if (recognize_captcha(bg, 8, puzzle, 4) != 0) { printf("synthetic failed\\n"); return 1; }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''// @@BLOG@@
// LeetCode 104107934. 滑动验证码识别 — C++ 版（方案7：合成数据 + 识别全流程）
#include <algorithm>
#include <cmath>
#include <iostream>
#include <vector>

static std::vector<bool> detect_edges(const std::vector<int> &image) {
    std::vector<bool> edges(image.size(), false);
    for (size_t i = 1; i < image.size(); ++i) {
        edges[i] = std::abs(image[i] - image[i - 1]) > 50;
    }
    return edges;
}

static int recognize_captcha(const std::vector<int> &bg, const std::vector<int> &puzzle) {
    auto bg_edges = detect_edges(bg);
    auto puzzle_edges = detect_edges(puzzle);
    int best_x = 0;
    long long best_score = -1;
    for (size_t x = 0; x + puzzle.size() <= bg.size(); ++x) {
        long long score = 0;
        for (size_t y = 0; y < puzzle.size(); ++y) {
            if (bg_edges[x + y] && puzzle_edges[y]) ++score;
        }
        if (score > best_score) { best_score = score; best_x = static_cast<int>(x); }
    }
    return best_x;
}

static std::pair<std::vector<int>, std::vector<int>> build_synthetic(int bg_len, int gap_start, int puzzle_len) {
    std::vector<int> bg(bg_len, 10);
    for (int i = gap_start; i < std::min(gap_start + puzzle_len, bg_len); ++i) bg[i] = 200;
    std::vector<int> puzzle(bg.begin() + gap_start, bg.begin() + std::min(gap_start + puzzle_len, bg_len));
    return {bg, puzzle};
}

int main() {
    auto [bg, puzzle] = build_synthetic(8, 3, 4);
    // 与 TS 原文件一致：合成数据下 puzzle 边缘全平，识别结果为 0
    if (recognize_captcha(bg, puzzle) != 0) { std::cout << "synthetic failed" << std::endl; return 1; }
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''# @@BLOG@@
# LeetCode 104107934. 滑动验证码识别 — R 版（方案7：合成数据 + 识别全流程）
detect_edges <- function(image) {
  edges <- rep(FALSE, length(image))
  for (i in 2:length(image)) {
    edges[i] <- abs(image[i] - image[i - 1L]) > 50
  }
  edges
}

recognize_captcha <- function(bg, puzzle) {
  bg_edges <- detect_edges(bg)
  puzzle_edges <- detect_edges(puzzle)
  best_x <- 1L
  best_score <- -1L
  for (x in 1:(length(bg) - length(puzzle) + 1L)) {
    score <- 0L
    for (y in 1:length(puzzle)) {
      if (bg_edges[x + y - 1L] && puzzle_edges[y]) score <- score + 1L
    }
    if (score > best_score) {
      best_score <- score
      best_x <- x
    }
  }
  as.integer(best_x - 1L)
}

build_synthetic <- function(bg_len, gap_start, puzzle_len) {
  bg <- rep(10L, bg_len)
  for (i in (gap_start + 1L):min(gap_start + puzzle_len, bg_len)) {
    bg[i] <- 200L
  }
  puzzle <- bg[(gap_start + 1L):(gap_start + puzzle_len)]
  list(bg, puzzle)
}

got <- build_synthetic(8L, 3L, 4L)
# 与 TS 原文件一致：合成数据下 puzzle 边缘全平，识别结果为 0
stopifnot(recognize_captcha(got[[1]], got[[2]]) == 0L)
cat("PASS\\n")
''',
"zig": '''// @@BLOG@@
// LeetCode 104107934. 滑动验证码识别 — Zig 版（方案7：合成数据 + 识别全流程）
const std = @import("std");

fn detectEdges(image: []const i32, edges: []bool) void {
    for (edges) |*e| e.* = false;
    var i: usize = 1;
    while (i < image.len) : (i += 1) {
        edges[i] = @abs(image[i] - image[i - 1]) > 50;
    }
}

fn recognizeCaptcha(bg: []const i32, puzzle: []const i32) usize {
    var bg_edges: [64]bool = undefined;
    var puzzle_edges: [64]bool = undefined;
    detectEdges(bg, &bg_edges);
    detectEdges(puzzle, &puzzle_edges);
    var best_x: usize = 0;
    var best_score: i64 = -1;
    var x: usize = 0;
    while (x + puzzle.len <= bg.len) : (x += 1) {
        var score: i64 = 0;
        for (0..puzzle.len) |y| {
            if (bg_edges[x + y] and puzzle_edges[y]) score += 1;
        }
        if (score > best_score) {
            best_score = score;
            best_x = x;
        }
    }
    return best_x;
}

pub fn main() !void {
    // 合成数据：build_synthetic(8,3,4) → bg[3..6] = 200
    const bg = [_]i32{ 10, 10, 10, 200, 200, 200, 200, 10 };
    const puzzle = [_]i32{ 200, 200, 200, 200 };
    // 与 TS 原文件一致：合成数据下 puzzle 边缘全平，识别结果为 0
    if (recognizeCaptcha(&bg, &puzzle) != 0) return error.TestFailed;
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''// @@BLOG@@
// LeetCode 104107934. 滑动验证码识别 — Dart 版（方案7：合成数据 + 识别全流程）
List<bool> detectEdges(List<int> image) {
  final edges = List<bool>.filled(image.length, false);
  for (var i = 1; i < image.length; i++) {
    edges[i] = (image[i] - image[i - 1]).abs() > 50;
  }
  return edges;
}

int recognizeCaptcha(List<int> bg, List<int> puzzle) {
  final bgEdges = detectEdges(bg);
  final puzzleEdges = detectEdges(puzzle);
  var bestX = 0;
  var bestScore = -1;
  for (var x = 0; x <= bg.length - puzzle.length; x++) {
    var score = 0;
    for (var y = 0; y < puzzle.length; y++) {
      if (bgEdges[x + y] && puzzleEdges[y]) score++;
    }
    if (score > bestScore) {
      bestScore = score;
      bestX = x;
    }
  }
  return bestX;
}

List<List<int>> buildSynthetic(int bgLen, int gapStart, int puzzleLen) {
  final bg = List<int>.filled(bgLen, 10);
  for (var i = gapStart; i < (gapStart + puzzleLen).clamp(0, bgLen); i++) {
    bg[i] = 200;
  }
  final puzzle = bg.sublist(gapStart, (gapStart + puzzleLen).clamp(0, bgLen));
  return [bg, puzzle];
}

void main() {
  final got = buildSynthetic(8, 3, 4);
  // 与 TS 原文件一致：合成数据下 puzzle 边缘全平，识别结果为 0
  if (recognizeCaptcha(got[0], got[1]) != 0) throw StateError('synthetic failed');
  print('PASS');
}
''',
}

EXTS = {"rust": ".rs", "lua": ".lua", "c": ".c", "cpp": ".cpp", "r": ".R", "zig": ".zig", "dart": ".dart"}

def main():
    blocks = {1: S1, 2: S2, 3: S3, 4: S4, 5: S5, 6: S6, 7: S7}
    for sol, block in blocks.items():
        for lang, t in block.items():
            emit(lang, REL + "/solution_%d___%d%s" % (sol, sol, EXTS[lang]), t.replace("@@BLOG@@", BLOG))

if __name__ == "__main__":
    main()
