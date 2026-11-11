#!/usr/bin/env python3
# gen_fix_n16.py — 补齐 notes/lc_107490876 分书和八皇后 × 7 语言（7 解法）
# s1/s2: 分书(共享回溯/函数式)  s3: 递归isSafe  s4: 显式栈  s5: 布尔数组  s6: 不可变状态  s7: 位置对列表
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from langlib import emit

REL = "notes/lc_107490876_计算思维之分书和八皇后问题"
BLOG = "来源：https://blog.csdn.net/tyro_java/article/details/107490876"
LIKE = '''const like: number[][] = [
        [0, 0, 1, 1, 0],
        [1, 1, 0, 0, 1],
        [0, 1, 1, 0, 1],
        [0, 0, 0, 1, 0],
        [0, 1, 0, 0, 1],
    ];'''

# ---------------- s1: 分书（共享 assigned + 回溯） ----------------
S1 = {
"rust": '''// @@BLOG@@
// LeetCode 107490876. 分书和八皇后问题 — Rust 版（方案1：分书，共享 assigned + 回溯）
const LIKE: [[i32; 5]; 5] = [
    [0, 0, 1, 1, 0],
    [1, 1, 0, 0, 1],
    [0, 1, 1, 0, 1],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 1],
];

fn allocate_books() -> Vec<Vec<i32>> {
    let mut results: Vec<Vec<i32>> = vec![];
    let mut assigned = vec![-1i32; 5];

    fn try_assign(reader: usize, assigned: &mut Vec<i32>, results: &mut Vec<Vec<i32>>) {
        if reader == 5 {
            results.push(assigned.clone());
            return;
        }
        for book in 0..5usize {
            if LIKE[reader][book] == 1 && assigned[book] == -1 {
                assigned[book] = reader as i32;
                try_assign(reader + 1, assigned, results);
                assigned[book] = -1; // 回溯
            }
        }
    }

    try_assign(0, &mut assigned, &mut results);
    results
}

fn main() {
    let want: Vec<Vec<i32>> = vec![vec![1, 2, 0, 3, 4], vec![1, 4, 0, 3, 2]];
    let res = allocate_books();
    assert_eq!(res.len(), want.len(), "count mismatch");
    for i in 0..want.len() {
        assert_eq!(res[i], want[i], "scheme {} mismatch", i);
    }
    // 附加性质：每人都拿到喜欢的书且书不重复（assigned[book]=reader 语义下天然成立）
    println!("PASS");
}
''',
"lua": '''-- @@BLOG@@
-- LeetCode 107490876. 分书和八皇后问题 — Lua 版（方案1：分书，共享 assigned + 回溯）
local like = {
    {0, 0, 1, 1, 0},
    {1, 1, 0, 0, 1},
    {0, 1, 1, 0, 1},
    {0, 0, 0, 1, 0},
    {0, 1, 0, 0, 1},
}

local function allocate_books()
    local results = {}
    local assigned = {-1, -1, -1, -1, -1}  -- assigned[book] = reader（1 基）

    local function try_assign(reader)
        if reader > 5 then
            local snap = {}
            for i = 1, 5 do snap[i] = assigned[i] - 1 end  -- 转 0 基输出
            results[#results + 1] = snap
            return
        end
        for book = 1, 5 do
            if like[reader][book] == 1 and assigned[book] == -1 then
                assigned[book] = reader
                try_assign(reader + 1)
                assigned[book] = -1 -- 回溯
            end
        end
    end

    try_assign(1)
    return results
end

local want = {{1, 2, 0, 3, 4}, {1, 4, 0, 3, 2}}
local res = allocate_books()
assert(#res == #want, "count mismatch")
for i = 1, #want do
    for j = 1, 5 do
        assert(res[i][j] == want[i][j], "scheme " .. i .. " mismatch")
    end
end
print("PASS")
''',
"c": '''/* @@BLOG@@
 * LeetCode 107490876. 分书和八皇后问题 — C 版（方案1：分书，共享 assigned + 回溯）
 */
#include <stdio.h>
#include <string.h>

static const int LIKE[5][5] = {
    {0, 0, 1, 1, 0},
    {1, 1, 0, 0, 1},
    {0, 1, 1, 0, 1},
    {0, 0, 0, 1, 0},
    {0, 1, 0, 0, 1},
};

static int assigned[5];
static int results[16][5];
static int result_count = 0;

static void try_assign(int reader) {
    if (reader == 5) {
        for (int i = 0; i < 5; i++) results[result_count][i] = assigned[i];
        result_count++;
        return;
    }
    for (int book = 0; book < 5; book++) {
        if (LIKE[reader][book] == 1 && assigned[book] == -1) {
            assigned[book] = reader;
            try_assign(reader + 1);
            assigned[book] = -1; /* 回溯 */
        }
    }
}

int main(void) {
    int want[2][5] = {{1, 2, 0, 3, 4}, {1, 4, 0, 3, 2}};
    for (int i = 0; i < 5; i++) assigned[i] = -1;
    try_assign(0);
    if (result_count != 2) { printf("count mismatch %d\\n", result_count); return 1; }
    for (int i = 0; i < 2; i++)
        for (int j = 0; j < 5; j++)
            if (results[i][j] != want[i][j]) { printf("scheme %d mismatch\\n", i); return 1; }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''// @@BLOG@@
// LeetCode 107490876. 分书和八皇后问题 — C++ 版（方案1：分书，共享 assigned + 回溯）
#include <iostream>
#include <vector>

static const int LIKE[5][5] = {
    {0, 0, 1, 1, 0},
    {1, 1, 0, 0, 1},
    {0, 1, 1, 0, 1},
    {0, 0, 0, 1, 0},
    {0, 1, 0, 0, 1},
};

static std::vector<std::vector<int>> allocate_books() {
    std::vector<std::vector<int>> results;
    std::vector<int> assigned(5, -1);

    std::function<void(int)> try_assign = [&](int reader) {
        if (reader == 5) {
            results.push_back(assigned);
            return;
        }
        for (int book = 0; book < 5; ++book) {
            if (LIKE[reader][book] == 1 && assigned[book] == -1) {
                assigned[book] = reader;
                try_assign(reader + 1);
                assigned[book] = -1; // 回溯
            }
        }
    };

    try_assign(0);
    return results;
}

int main() {
    std::vector<std::vector<int>> want = {{1, 2, 0, 3, 4}, {1, 4, 0, 3, 2}};
    std::vector<std::vector<int>> res = allocate_books();
    if (res != want) { std::cout << "mismatch" << std::endl; return 1; }
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''# @@BLOG@@
# LeetCode 107490876. 分书和八皇后问题 — R 版（方案1：分书，共享 assigned + 回溯）
LIKE <- matrix(c(
  0, 0, 1, 1, 0,
  1, 1, 0, 0, 1,
  0, 1, 1, 0, 1,
  0, 0, 0, 1, 0,
  0, 1, 0, 0, 1
), nrow = 5, byrow = TRUE)

allocate_books <- function() {
  results <- list()
  assigned <- rep(-1L, 5)

  try_assign <- function(reader) {
    if (reader == 5L) {
      results <<- c(results, list(assigned))
      return(invisible(NULL))
    }
    for (book in 0:4) {
      if (LIKE[reader + 1L, book + 1L] == 1 && assigned[book + 1L] == -1L) {
        assigned[book + 1L] <<- reader
        try_assign(reader + 1L)
        assigned[book + 1L] <<- -1L # 回溯
      }
    }
  }

  try_assign(0L)
  results
}

want <- list(c(1L, 2L, 0L, 3L, 4L), c(1L, 4L, 0L, 3L, 2L))
res <- allocate_books()
stopifnot(length(res) == 2L)
for (i in 1:2) {
  stopifnot(identical(as.integer(res[[i]]), as.integer(want[[i]])))
}
cat("PASS\\n")
''',
"zig": '''// @@BLOG@@
// LeetCode 107490876. 分书和八皇后问题 — Zig 版（方案1：分书，共享 assigned + 回溯）
const std = @import("std");

const LIKE = [5][5]i32{
    .{ 0, 0, 1, 1, 0 },
    .{ 1, 1, 0, 0, 1 },
    .{ 0, 1, 1, 0, 1 },
    .{ 0, 0, 0, 1, 0 },
    .{ 0, 1, 0, 0, 1 },
};

var assigned: [5]i32 = undefined;
var results: [16][5]i32 = undefined;
var result_count: usize = 0;

fn tryAssign(reader: usize) void {
    if (reader == 5) {
        results[result_count] = assigned;
        result_count += 1;
        return;
    }
    var book: usize = 0;
    while (book < 5) : (book += 1) {
        if (LIKE[reader][book] == 1 and assigned[book] == -1) {
            assigned[book] = @intCast(reader);
            tryAssign(reader + 1);
            assigned[book] = -1; // 回溯
        }
    }
}

pub fn main() !void {
    const want = [2][5]i32{ .{ 1, 2, 0, 3, 4 }, .{ 1, 4, 0, 3, 2 } };
    assigned = .{ -1, -1, -1, -1, -1 };
    tryAssign(0);
    if (result_count != 2) {
        std.debug.print("count mismatch {d}\\n", .{result_count});
        return error.TestFailed;
    }
    for (want, 0..) |w, i| {
        for (w, 0..) |x, j| {
            if (results[i][j] != x) {
                std.debug.print("scheme {d} mismatch\\n", .{i});
                return error.TestFailed;
            }
        }
    }
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''// @@BLOG@@
// LeetCode 107490876. 分书和八皇后问题 — Dart 版（方案1：分书，共享 assigned + 回溯）
const like = [
  [0, 0, 1, 1, 0],
  [1, 1, 0, 0, 1],
  [0, 1, 1, 0, 1],
  [0, 0, 0, 1, 0],
  [0, 1, 0, 0, 1],
];

List<List<int>> allocateBooks() {
  final results = <List<int>>[];
  final assigned = <int>[-1, -1, -1, -1, -1];

  void tryAssign(int reader) {
    if (reader == 5) {
      results.add(List<int>.from(assigned));
      return;
    }
    for (var book = 0; book < 5; book++) {
      if (like[reader][book] == 1 && assigned[book] == -1) {
        assigned[book] = reader;
        tryAssign(reader + 1);
        assigned[book] = -1; // 回溯
      }
    }
  }

  tryAssign(0);
  return results;
}

void main() {
  final want = <List<int>>[[1, 2, 0, 3, 4], [1, 4, 0, 3, 2]];
  final res = allocateBooks();
  if (res.toString() != want.toString()) {
    throw StateError('mismatch: ' + res.toString());
  }
  print('PASS');
}
''',
}

# ---------------- s2: 分书（函数式不可变） ----------------
S2 = {
"rust": '''// @@BLOG@@
// LeetCode 107490876. 分书和八皇后问题 — Rust 版（方案2：分书，函数式不可变副本）
const LIKE: [[i32; 5]; 5] = [
    [0, 0, 1, 1, 0],
    [1, 1, 0, 0, 1],
    [0, 1, 1, 0, 1],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 1],
];

fn allocate_books_func() -> Vec<Vec<i32>> {
    let mut results: Vec<Vec<i32>> = vec![];

    fn try_assign(reader: usize, assigned: Vec<i32>, results: &mut Vec<Vec<i32>>) {
        if reader == 5 {
            results.push(assigned);
            return;
        }
        for book in 0..5usize {
            if LIKE[reader][book] == 1 && assigned[book] == -1 {
                let mut nxt = assigned.clone();
                nxt[book] = reader as i32;
                try_assign(reader + 1, nxt, results);
            }
        }
    }

    try_assign(0, vec![-1i32; 5], &mut results);
    results
}

fn main() {
    let want: Vec<Vec<i32>> = vec![vec![1, 2, 0, 3, 4], vec![1, 4, 0, 3, 2]];
    let res = allocate_books_func();
    assert_eq!(res, want, "mismatch");
    println!("PASS");
}
''',
"lua": '''-- @@BLOG@@
-- LeetCode 107490876. 分书和八皇后问题 — Lua 版（方案2：分书，函数式不可变副本）
local like = {
    {0, 0, 1, 1, 0},
    {1, 1, 0, 0, 1},
    {0, 1, 1, 0, 1},
    {0, 0, 0, 1, 0},
    {0, 1, 0, 0, 1},
}

local function allocate_books_func()
    local results = {}

    local function try_assign(reader, assigned)
        if reader > 5 then
            local snap = {}
            for i = 1, 5 do snap[i] = assigned[i] - 1 end
            results[#results + 1] = snap
            return
        end
        for book = 1, 5 do
            if like[reader][book] == 1 and assigned[book] == -1 then
                local nxt = {}
                for i = 1, 5 do nxt[i] = assigned[i] end
                nxt[book] = reader
                try_assign(reader + 1, nxt)
            end
        end
    end

    try_assign(1, {-1, -1, -1, -1, -1})
    return results
end

local want = {{1, 2, 0, 3, 4}, {1, 4, 0, 3, 2}}
local res = allocate_books_func()
assert(#res == #want, "count mismatch")
for i = 1, #want do
    for j = 1, 5 do
        assert(res[i][j] == want[i][j], "scheme " .. i .. " mismatch")
    end
end
print("PASS")
''',
"c": '''/* @@BLOG@@
 * LeetCode 107490876. 分书和八皇后问题 — C 版（方案2：分书，函数式不可变副本）
 */
#include <stdio.h>
#include <string.h>

static const int LIKE[5][5] = {
    {0, 0, 1, 1, 0},
    {1, 1, 0, 0, 1},
    {0, 1, 1, 0, 1},
    {0, 0, 0, 1, 0},
    {0, 1, 0, 0, 1},
};

static int results[16][5];
static int result_count = 0;

static void try_assign(int reader, const int assigned[5]) {
    if (reader == 5) {
        memcpy(results[result_count], assigned, sizeof(int) * 5);
        result_count++;
        return;
    }
    for (int book = 0; book < 5; book++) {
        if (LIKE[reader][book] == 1 && assigned[book] == -1) {
            int nxt[5];
            memcpy(nxt, assigned, sizeof(int) * 5);
            nxt[book] = reader;
            try_assign(reader + 1, nxt);
        }
    }
}

int main(void) {
    int want[2][5] = {{1, 2, 0, 3, 4}, {1, 4, 0, 3, 2}};
    int init[5] = {-1, -1, -1, -1, -1};
    try_assign(0, init);
    if (result_count != 2) { printf("count mismatch\\n"); return 1; }
    for (int i = 0; i < 2; i++)
        for (int j = 0; j < 5; j++)
            if (results[i][j] != want[i][j]) { printf("scheme %d mismatch\\n", i); return 1; }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''// @@BLOG@@
// LeetCode 107490876. 分书和八皇后问题 — C++ 版（方案2：分书，函数式不可变副本）
#include <iostream>
#include <vector>

static const int LIKE[5][5] = {
    {0, 0, 1, 1, 0},
    {1, 1, 0, 0, 1},
    {0, 1, 1, 0, 1},
    {0, 0, 0, 1, 0},
    {0, 1, 0, 0, 1},
};

static void try_assign(int reader, std::vector<int> assigned,
                      std::vector<std::vector<int>> &results) {
    if (reader == 5) {
        results.push_back(assigned);
        return;
    }
    for (int book = 0; book < 5; ++book) {
        if (LIKE[reader][book] == 1 && assigned[book] == -1) {
            std::vector<int> nxt = assigned;
            nxt[book] = reader;
            try_assign(reader + 1, nxt, results);
        }
    }
}

int main() {
    std::vector<std::vector<int>> results;
    try_assign(0, std::vector<int>(5, -1), results);
    std::vector<std::vector<int>> want = {{1, 2, 0, 3, 4}, {1, 4, 0, 3, 2}};
    if (results != want) { std::cout << "mismatch" << std::endl; return 1; }
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''# @@BLOG@@
# LeetCode 107490876. 分书和八皇后问题 — R 版（方案2：分书，函数式不可变副本）
LIKE <- matrix(c(
  0, 0, 1, 1, 0,
  1, 1, 0, 0, 1,
  0, 1, 1, 0, 1,
  0, 0, 0, 1, 0,
  0, 1, 0, 0, 1
), nrow = 5, byrow = TRUE)

allocate_books_func <- function() {
  results <- list()

  try_assign <- function(reader, assigned) {
    if (reader == 5L) {
      results <<- c(results, list(assigned))
      return(invisible(NULL))
    }
    for (book in 0:4) {
      if (LIKE[reader + 1L, book + 1L] == 1 && assigned[book + 1L] == -1L) {
        nxt <- assigned
        nxt[book + 1L] <- reader
        try_assign(reader + 1L, nxt)
      }
    }
  }

  try_assign(0L, rep(-1L, 5))
  results
}

want <- list(c(1L, 2L, 0L, 3L, 4L), c(1L, 4L, 0L, 3L, 2L))
res <- allocate_books_func()
stopifnot(length(res) == 2L)
for (i in 1:2) {
  stopifnot(identical(as.integer(res[[i]]), as.integer(want[[i]])))
}
cat("PASS\\n")
''',
"zig": '''// @@BLOG@@
// LeetCode 107490876. 分书和八皇后问题 — Zig 版（方案2：分书，函数式不可变副本）
const std = @import("std");

const LIKE = [5][5]i32{
    .{ 0, 0, 1, 1, 0 },
    .{ 1, 1, 0, 0, 1 },
    .{ 0, 1, 1, 0, 1 },
    .{ 0, 0, 0, 1, 0 },
    .{ 0, 1, 0, 0, 1 },
};

var results: [16][5]i32 = undefined;
var result_count: usize = 0;

fn tryAssign(reader: usize, assigned: [5]i32) void {
    if (reader == 5) {
        results[result_count] = assigned;
        result_count += 1;
        return;
    }
    var book: usize = 0;
    while (book < 5) : (book += 1) {
        if (LIKE[reader][book] == 1 and assigned[book] == -1) {
            var nxt = assigned;
            nxt[book] = @intCast(reader);
            tryAssign(reader + 1, nxt);
        }
    }
}

pub fn main() !void {
    const want = [2][5]i32{ .{ 1, 2, 0, 3, 4 }, .{ 1, 4, 0, 3, 2 } };
    tryAssign(0, .{ -1, -1, -1, -1, -1 });
    if (result_count != 2) return error.TestFailed;
    for (want, 0..) |w, i| {
        for (w, 0..) |x, j| {
            if (results[i][j] != x) return error.TestFailed;
        }
    }
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''// @@BLOG@@
// LeetCode 107490876. 分书和八皇后问题 — Dart 版（方案2：分书，函数式不可变副本）
const like = [
  [0, 0, 1, 1, 0],
  [1, 1, 0, 0, 1],
  [0, 1, 1, 0, 1],
  [0, 0, 0, 1, 0],
  [0, 1, 0, 0, 1],
];

List<List<int>> allocateBooksFunc() {
  final results = <List<int>>[];

  void tryAssign(int reader, List<int> assigned) {
    if (reader == 5) {
      results.add(assigned);
      return;
    }
    for (var book = 0; book < 5; book++) {
      if (like[reader][book] == 1 && assigned[book] == -1) {
        final nxt = List<int>.from(assigned);
        nxt[book] = reader;
        tryAssign(reader + 1, nxt);
      }
    }
  }

  tryAssign(0, <int>[-1, -1, -1, -1, -1]);
  return results;
}

void main() {
  final want = <List<int>>[[1, 2, 0, 3, 4], [1, 4, 0, 3, 2]];
  final res = allocateBooksFunc();
  if (res.toString() != want.toString()) throw StateError('mismatch');
  print('PASS');
}
''',
}

# ---------------- 八皇后通用：生成器按变体产出 ----------------
# cases（1 基行号变体 s3/s4 与 0 基变体 s5/s6/s7 不同）

def queens_cases(one_based, stack_order):
    if stack_order:
        return [(8, 92, [8, 4, 1, 3, 6, 2, 7, 5]), (1, 1, [1]), (2, 0, None), (4, 2, [3, 1, 4, 2])]
    if one_based:
        return [(8, 92, [1, 5, 8, 6, 3, 7, 2, 4]), (1, 1, [1]), (2, 0, None), (4, 2, [2, 4, 1, 3])]
    return [(8, 92, [0, 4, 7, 5, 2, 6, 1, 3]), (1, 1, [0]), (2, 0, None), (4, 2, [1, 3, 0, 2])]

def main_check(lang, cases):
    rows = []
    for n, count, first in cases:
        if first is None:
            rows.append((n, count, None))
        else:
            rows.append((n, count, first))
    return rows

if __name__ == "__main__":
    pass

# ---------------- s3: 递归 isSafe（行号 1..n） ----------------
S3 = {
"rust": '''// @@BLOG@@
// LeetCode 107490876. 分书和八皇后问题 — Rust 版（方案3：八皇后递归 isSafe，行号 1..n）
fn n_queens_safe(n: usize) -> Vec<Vec<i32>> {
    let mut results: Vec<Vec<i32>> = vec![];
    let mut board = vec![0i32; n];

    fn is_safe(board: &[i32], col: usize, row: i32) -> bool {
        for c in 0..col {
            if board[c] == row || (board[c] - row).abs() == (c as i32 - col as i32).abs() {
                return false;
            }
        }
        true
    }

    fn place(col: usize, n: usize, board: &mut Vec<i32>, results: &mut Vec<Vec<i32>>) {
        if col == n {
            results.push(board.clone());
            return;
        }
        for row in 1..=n as i32 {
            if is_safe(board, col, row) {
                board[col] = row;
                place(col + 1, n, board, results);
            }
        }
    }

    place(0, n, &mut board, &mut results);
    results
}

fn main() {
    // (n, 期望解数, 期望首解)
    let cases: Vec<(usize, usize, Option<Vec<i32>>)> = vec![
        (8, 92, Some(vec![1, 5, 8, 6, 3, 7, 2, 4])),
        (1, 1, Some(vec![1])),
        (2, 0, None),
        (4, 2, Some(vec![2, 4, 1, 3])),
    ];
    for (idx, (n, count, first)) in cases.iter().enumerate() {
        let sols = n_queens_safe(*n);
        assert_eq!(sols.len(), *count, "case {} count mismatch", idx);
        if let Some(w) = first {
            assert_eq!(&sols[0], w, "case {} first mismatch", idx);
        }
    }
    println!("PASS");
}
''',
"lua": '''-- @@BLOG@@
-- LeetCode 107490876. 分书和八皇后问题 — Lua 版（方案3：八皇后递归 isSafe，行号 1..n）
local function n_queens_safe(n)
    local results = {}
    local board = {}
    for i = 1, n do board[i] = 0 end

    local function is_safe(col, row)
        for c = 1, col - 1 do
            if board[c] == row or math.abs(board[c] - row) == math.abs(c - col) then
                return false
            end
        end
        return true
    end

    local function place(col)
        if col > n then
            local snap = {}
            for i = 1, n do snap[i] = board[i] end
            results[#results + 1] = snap
            return
        end
        for row = 1, n do
            if is_safe(col, row) then
                board[col] = row
                place(col + 1)
            end
        end
    end

    place(1)
    return results
end

local cases = {
    {8, 92, {1, 5, 8, 6, 3, 7, 2, 4}},
    {1, 1, {1}},
    {2, 0, nil},
    {4, 2, {2, 4, 1, 3}},
}
for idx, c in ipairs(cases) do
    local sols = n_queens_safe(c[1])
    assert(#sols == c[2], "case " .. idx .. " count mismatch: " .. #sols)
    if c[3] then
        for j = 1, #c[3] do
            assert(sols[1][j] == c[3][j], "case " .. idx .. " first mismatch")
        end
    end
end
print("PASS")
''',
"c": '''/* @@BLOG@@
 * LeetCode 107490876. 分书和八皇后问题 — C 版（方案3：八皇后递归 isSafe，行号 1..n）
 */
#include <stdio.h>
#include <stdlib.h>

static int board[8];
static int sols[100][8];
static int sol_count = 0;
static int N;

static int is_safe(int col, int row) {
    for (int c = 0; c < col; c++) {
        if (board[c] == row || abs(board[c] - row) == abs(c - col)) return 0;
    }
    return 1;
}

static void place(int col) {
    if (col == N) {
        for (int i = 0; i < N; i++) sols[sol_count][i] = board[i];
        sol_count++;
        return;
    }
    for (int row = 1; row <= N; row++) {
        if (is_safe(col, row)) {
            board[col] = row;
            place(col + 1);
        }
    }
}

static int n_queens_safe(int n) {
    N = n;
    sol_count = 0;
    place(0);
    return sol_count;
}

int main(void) {
    struct { int n; int count; int has_first; int first[8]; } cases[] = {
        {8, 92, 1, {1, 5, 8, 6, 3, 7, 2, 4}},
        {1, 1, 1, {1}},
        {2, 0, 0, {0}},
        {4, 2, 1, {2, 4, 1, 3}},
    };
    for (int idx = 0; idx < 4; idx++) {
        int count = n_queens_safe(cases[idx].n);
        if (count != cases[idx].count) { printf("case %d count %d\\n", idx, count); return 1; }
        if (cases[idx].has_first) {
            for (int j = 0; j < cases[idx].n; j++) {
                if (sols[0][j] != cases[idx].first[j]) { printf("case %d first\\n", idx); return 1; }
            }
        }
    }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''// @@BLOG@@
// LeetCode 107490876. 分书和八皇后问题 — C++ 版（方案3：八皇后递归 isSafe，行号 1..n）
#include <cmath>
#include <iostream>
#include <vector>

static std::vector<std::vector<int>> n_queens_safe(int n) {
    std::vector<std::vector<int>> results;
    std::vector<int> board(n, 0);

    std::function<bool(int, int)> is_safe = [&](int col, int row) {
        for (int c = 0; c < col; ++c) {
            if (board[c] == row || std::abs(board[c] - row) == std::abs(c - col)) return false;
        }
        return true;
    };

    std::function<void(int)> place = [&](int col) {
        if (col == n) {
            results.push_back(board);
            return;
        }
        for (int row = 1; row <= n; ++row) {
            if (is_safe(col, row)) {
                board[col] = row;
                place(col + 1);
            }
        }
    };

    place(0);
    return results;
}

int main() {
    struct Case { int n; int count; bool has_first; std::vector<int> first; };
    std::vector<Case> cases = {
        {8, 92, true, {1, 5, 8, 6, 3, 7, 2, 4}},
        {1, 1, true, {1}},
        {2, 0, false, {}},
        {4, 2, true, {2, 4, 1, 3}},
    };
    for (size_t idx = 0; idx < cases.size(); ++idx) {
        auto sols = n_queens_safe(cases[idx].n);
        if (static_cast<int>(sols.size()) != cases[idx].count) { std::cout << "case " << idx << " count" << std::endl; return 1; }
        if (cases[idx].has_first && sols[0] != cases[idx].first) { std::cout << "case " << idx << " first" << std::endl; return 1; }
    }
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''# @@BLOG@@
# LeetCode 107490876. 分书和八皇后问题 — R 版（方案3：八皇后递归 isSafe，行号 1..n）
n_queens_safe <- function(n) {
  results <- list()
  board <- rep(0L, n)

  is_safe <- function(col, row) {
    if (col == 1L) return(TRUE)
    for (c in 1:(col - 1L)) {
      if (board[c] == row || abs(board[c] - row) == abs(c - col)) return(FALSE)
    }
    TRUE
  }

  place <- function(col) {
    if (col > n) {
      results <<- c(results, list(board))
      return(invisible(NULL))
    }
    for (row in 1:n) {
      if (is_safe(col, row)) {
        board[col] <<- row
        place(col + 1L)
      }
    }
  }

  place(1L)
  results
}

cases <- list(
  list(8L, 92L, c(1, 5, 8, 6, 3, 7, 2, 4)),
  list(1L, 1L, c(1)),
  list(2L, 0L, NULL),
  list(4L, 2L, c(2, 4, 1, 3))
)
for (idx in seq_along(cases)) {
  sols <- n_queens_safe(cases[[idx]][[1]])
  stopifnot(length(sols) == cases[[idx]][[2]])
  if (!is.null(cases[[idx]][[3]])) {
    stopifnot(identical(as.integer(sols[[1]]), as.integer(cases[[idx]][[3]])))
  }
}
cat("PASS\\n")
''',
"zig": '''// @@BLOG@@
// LeetCode 107490876. 分书和八皇后问题 — Zig 版（方案3：八皇后递归 isSafe，行号 1..n）
const std = @import("std");

var board: [8]i32 = undefined;
var sols: [100][8]i32 = undefined;
var sol_count: usize = 0;
var cur_n: usize = 0;

fn isSafe(col: usize, row: i32) bool {
    var c: usize = 0;
    while (c < col) : (c += 1) {
        const dc: i32 = @as(i32, @intCast(c)) - @as(i32, @intCast(col));
        if (board[c] == row or @abs(board[c] - row) == @abs(dc)) return false;
    }
    return true;
}

fn place(col: usize) void {
    if (col == cur_n) {
        sols[sol_count] = board;
        sol_count += 1;
        return;
    }
    var row: i32 = 1;
    while (row <= @as(i32, @intCast(cur_n))) : (row += 1) {
        if (isSafe(col, row)) {
            board[col] = row;
            place(col + 1);
        }
    }
}

pub fn main() !void {
    const Case = struct { n: usize, count: usize, first: ?[8]i32, flen: usize };
    const cases = [_]Case{
        .{ .n = 8, .count = 92, .first = .{ 1, 5, 8, 6, 3, 7, 2, 4 }, .flen = 8 },
        .{ .n = 1, .count = 1, .first = .{ 1, 0, 0, 0, 0, 0, 0, 0 }, .flen = 1 },
        .{ .n = 2, .count = 0, .first = null, .flen = 0 },
        .{ .n = 4, .count = 2, .first = .{ 2, 4, 1, 3, 0, 0, 0, 0 }, .flen = 4 },
    };
    for (cases, 0..) |c, idx| {
        cur_n = c.n;
        sol_count = 0;
        place(0);
        if (sol_count != c.count) {
            std.debug.print("case {d} count {d}\\n", .{ idx, sol_count });
            return error.TestFailed;
        }
        if (c.first) |f| {
            var j: usize = 0;
            while (j < c.flen) : (j += 1) {
                if (sols[0][j] != f[j]) {
                    std.debug.print("case {d} first\\n", .{idx});
                    return error.TestFailed;
                }
            }
        }
    }
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''// @@BLOG@@
// LeetCode 107490876. 分书和八皇后问题 — Dart 版（方案3：八皇后递归 isSafe，行号 1..n）
List<List<int>> nQueensSafe(int n) {
  final results = <List<int>>[];
  final board = List<int>.filled(n, 0);

  bool isSafe(int col, int row) {
    for (var c = 0; c < col; c++) {
      if (board[c] == row || (board[c] - row).abs() == (c - col).abs()) {
        return false;
      }
    }
    return true;
  }

  void place(int col) {
    if (col == n) {
      results.add(List<int>.from(board));
      return;
    }
    for (var row = 1; row <= n; row++) {
      if (isSafe(col, row)) {
        board[col] = row;
        place(col + 1);
      }
    }
  }

  place(0);
  return results;
}

void main() {
  final cases = <List<dynamic>>[
    [8, 92, [1, 5, 8, 6, 3, 7, 2, 4]],
    [1, 1, [1]],
    [2, 0, null],
    [4, 2, [2, 4, 1, 3]],
  ];
  for (var idx = 0; idx < cases.length; idx++) {
    final c = cases[idx];
    final sols = nQueensSafe(c[0] as int);
    if (sols.length != c[1] as int) throw StateError('case $idx count');
    if (c[2] != null && sols[0].toString() != c[2].toString()) {
      throw StateError('case $idx first');
    }
  }
  print('PASS');
}
''',
}

# ---------------- s4: 显式栈（行号 1..n，LIFO 先探高行号） ----------------
S4 = {
"rust": '''// @@BLOG@@
// LeetCode 107490876. 分书和八皇后问题 — Rust 版（方案4：八皇后显式栈迭代）
fn n_queens_stack(n: usize) -> Vec<Vec<i32>> {
    fn valid(x: i32, a: &[i32]) -> bool {
        let y = a.len() as i32 + 1;
        for i in 1..=a.len() as i32 {
            let prev = a[(i - 1) as usize];
            if x == prev || (y - i).abs() == (x - prev).abs() {
                return false;
            }
        }
        true
    }

    let mut solutions: Vec<Vec<i32>> = vec![];
    let mut stack: Vec<Vec<i32>> = vec![vec![]];
    while let Some(a) = stack.pop() {
        if a.len() == n {
            solutions.push(a);
        } else {
            for i in 1..=n as i32 {
                if valid(i, &a) {
                    let mut b = a.clone();
                    b.push(i);
                    stack.push(b);
                }
            }
        }
    }
    solutions
}

fn main() {
    let cases: Vec<(usize, usize, Option<Vec<i32>>)> = vec![
        (8, 92, Some(vec![8, 4, 1, 3, 6, 2, 7, 5])),
        (1, 1, Some(vec![1])),
        (2, 0, None),
        (4, 2, Some(vec![3, 1, 4, 2])),
    ];
    for (idx, (n, count, first)) in cases.iter().enumerate() {
        let sols = n_queens_stack(*n);
        assert_eq!(sols.len(), *count, "case {} count mismatch", idx);
        if let Some(w) = first {
            assert_eq!(&sols[0], w, "case {} first mismatch", idx);
        }
    }
    println!("PASS");
}
''',
"lua": '''-- @@BLOG@@
-- LeetCode 107490876. 分书和八皇后问题 — Lua 版（方案4：八皇后显式栈迭代）
local function valid(x, a)
    local y = #a + 1
    for i = 1, #a do
        if x == a[i] or math.abs(y - i) == math.abs(x - a[i]) then
            return false
        end
    end
    return true
end

local function n_queens_stack(n)
    local solutions = {}
    local stack = {{}}
    while #stack > 0 do
        local a = table.remove(stack)  -- 弹栈（LIFO）
        if #a == n then
            solutions[#solutions + 1] = a
        else
            for i = 1, n do
                if valid(i, a) then
                    local b = {}
                    for k = 1, #a do b[k] = a[k] end
                    b[#b + 1] = i
                    stack[#stack + 1] = b
                end
            end
        end
    end
    return solutions
end

local cases = {
    {8, 92, {8, 4, 1, 3, 6, 2, 7, 5}},
    {1, 1, {1}},
    {2, 0, nil},
    {4, 2, {3, 1, 4, 2}},
}
for idx, c in ipairs(cases) do
    local sols = n_queens_stack(c[1])
    assert(#sols == c[2], "case " .. idx .. " count mismatch: " .. #sols)
    if c[3] then
        for j = 1, #c[3] do
            assert(sols[1][j] == c[3][j], "case " .. idx .. " first mismatch")
        end
    end
end
print("PASS")
''',
"c": '''/* @@BLOG@@
 * LeetCode 107490876. 分书和八皇后问题 — C 版（方案4：八皇后显式栈迭代）
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define STACK_MAX 8192

static int valid(int x, const int *a, int len) {
    int y = len + 1;
    for (int i = 1; i <= len; i++) {
        if (x == a[i - 1] || abs(y - i) == abs(x - a[i - 1])) return 0;
    }
    return 1;
}

static int run_case(int n, int sols[][8]) {
    static int stack[STACK_MAX][9];
    static int slen[STACK_MAX];
    int top = 0;
    slen[top] = 0;              /* 空盘入栈 */
    top++;
    int sol_count = 0;
    while (top > 0) {
        top--;
        const int *a = stack[top];
        int alen = slen[top];
        if (alen == n) {
            memcpy(sols[sol_count], a, sizeof(int) * n);
            sol_count++;
        } else {
            for (int i = 1; i <= n; i++) {
                if (valid(i, a, alen)) {
                    memcpy(stack[top], a, sizeof(int) * alen);
                    stack[top][alen] = i;
                    slen[top] = alen + 1;
                    top++;
                }
            }
        }
    }
    return sol_count;
}

int main(void) {
    static int sols[100][8];
    struct { int n; int count; int has_first; int first[8]; } cases[] = {
        {8, 92, 1, {8, 4, 1, 3, 6, 2, 7, 5}},
        {1, 1, 1, {1}},
        {2, 0, 0, {0}},
        {4, 2, 1, {3, 1, 4, 2}},
    };
    for (int idx = 0; idx < 4; idx++) {
        int count = run_case(cases[idx].n, sols);
        if (count != cases[idx].count) { printf("case %d count %d\\n", idx, count); return 1; }
        if (cases[idx].has_first) {
            for (int j = 0; j < cases[idx].n; j++) {
                if (sols[0][j] != cases[idx].first[j]) { printf("case %d first\\n", idx); return 1; }
            }
        }
    }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''// @@BLOG@@
// LeetCode 107490876. 分书和八皇后问题 — C++ 版（方案4：八皇后显式栈迭代）
#include <cmath>
#include <iostream>
#include <vector>

static bool valid(int x, const std::vector<int> &a) {
    int y = static_cast<int>(a.size()) + 1;
    for (int i = 1; i <= static_cast<int>(a.size()); ++i) {
        if (x == a[i - 1] || std::abs(y - i) == std::abs(x - a[i - 1])) return false;
    }
    return true;
}

static std::vector<std::vector<int>> n_queens_stack(int n) {
    std::vector<std::vector<int>> solutions;
    std::vector<std::vector<int>> stack{ {} };
    while (!stack.empty()) {
        std::vector<int> a = stack.back();
        stack.pop_back();
        if (static_cast<int>(a.size()) == n) {
            solutions.push_back(a);
        } else {
            for (int i = 1; i <= n; ++i) {
                if (valid(i, a)) {
                    std::vector<int> b = a;
                    b.push_back(i);
                    stack.push_back(b);
                }
            }
        }
    }
    return solutions;
}

int main() {
    struct Case { int n; int count; bool has_first; std::vector<int> first; };
    std::vector<Case> cases = {
        {8, 92, true, {8, 4, 1, 3, 6, 2, 7, 5}},
        {1, 1, true, {1}},
        {2, 0, false, {}},
        {4, 2, true, {3, 1, 4, 2}},
    };
    for (size_t idx = 0; idx < cases.size(); ++idx) {
        auto sols = n_queens_stack(cases[idx].n);
        if (static_cast<int>(sols.size()) != cases[idx].count) { std::cout << "case " << idx << " count" << std::endl; return 1; }
        if (cases[idx].has_first && sols[0] != cases[idx].first) { std::cout << "case " << idx << " first" << std::endl; return 1; }
    }
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''# @@BLOG@@
# LeetCode 107490876. 分书和八皇后问题 — R 版（方案4：八皇后显式栈迭代）
valid_q <- function(x, a) {
  y <- length(a) + 1L
  for (i in seq_along(a)) {
    if (x == a[i] || abs(y - i) == abs(x - a[i])) return(FALSE)
  }
  TRUE
}

n_queens_stack <- function(n) {
  solutions <- list()
  stack <- list(integer(0))
  while (length(stack) > 0L) {
    a <- stack[[length(stack)]]
    stack <- stack[-length(stack)]
    if (length(a) == n) {
      solutions[[length(solutions) + 1L]] <- a
    } else {
      for (i in 1:n) {
        if (valid_q(i, a)) {
          stack[[length(stack) + 1L]] <- c(a, i)
        }
      }
    }
  }
  solutions
}

cases <- list(
  list(8L, 92L, c(8, 4, 1, 3, 6, 2, 7, 5)),
  list(1L, 1L, c(1)),
  list(2L, 0L, NULL),
  list(4L, 2L, c(3, 1, 4, 2))
)
for (idx in seq_along(cases)) {
  sols <- n_queens_stack(cases[[idx]][[1]])
  stopifnot(length(sols) == cases[[idx]][[2]])
  if (!is.null(cases[[idx]][[3]])) {
    stopifnot(identical(as.integer(sols[[1]]), as.integer(cases[[idx]][[3]])))
  }
}
cat("PASS\\n")
''',
"zig": '''// @@BLOG@@
// LeetCode 107490876. 分书和八皇后问题 — Zig 版（方案4：八皇后显式栈迭代）
const std = @import("std");

fn valid(x: i32, a: []const i32) bool {
    const y: i32 = @intCast(a.len + 1);
    for (a, 1..) |prev, i| {
        const ii: i32 = @intCast(i);
        if (x == prev or @abs(y - ii) == @abs(x - prev)) return false;
    }
    return true;
}

fn runCase(n: usize, sols: *[100][8]i32) usize {
    var stack: [8192][9]i32 = undefined;
    var slen: [8192]usize = undefined;
    var top: usize = 0;
    slen[top] = 0;
    top += 1;
    var sol_count: usize = 0;
    while (top > 0) {
        top -= 1;
        const a = stack[top];
        const alen = slen[top];
        if (alen == n) {
            var j: usize = 0;
            while (j < n) : (j += 1) sols[sol_count][j] = a[j];
            sol_count += 1;
        } else {
            var i: usize = 1;
            while (i <= n) : (i += 1) {
                if (valid(@intCast(i), a[0..alen])) {
                    var j: usize = 0;
                    while (j < alen) : (j += 1) stack[top][j] = a[j];
                    stack[top][alen] = @intCast(i);
                    slen[top] = alen + 1;
                    top += 1;
                }
            }
        }
    }
    return sol_count;
}

pub fn main() !void {
    var sols: [100][8]i32 = undefined;
    const Case = struct { n: usize, count: usize, first: ?[8]i32, flen: usize };
    const cases = [_]Case{
        .{ .n = 8, .count = 92, .first = .{ 8, 4, 1, 3, 6, 2, 7, 5 }, .flen = 8 },
        .{ .n = 1, .count = 1, .first = .{ 1, 0, 0, 0, 0, 0, 0, 0 }, .flen = 1 },
        .{ .n = 2, .count = 0, .first = null, .flen = 0 },
        .{ .n = 4, .count = 2, .first = .{ 3, 1, 4, 2, 0, 0, 0, 0 }, .flen = 4 },
    };
    for (cases, 0..) |c, idx| {
        const count = runCase(c.n, &sols);
        if (count != c.count) {
            std.debug.print("case {d} count {d}\\n", .{ idx, count });
            return error.TestFailed;
        }
        if (c.first) |f| {
            var j: usize = 0;
            while (j < c.flen) : (j += 1) {
                if (sols[0][j] != f[j]) return error.TestFailed;
            }
        }
    }
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''// @@BLOG@@
// LeetCode 107490876. 分书和八皇后问题 — Dart 版（方案4：八皇后显式栈迭代）
bool valid(int x, List<int> a) {
  final y = a.length + 1;
  for (var i = 1; i <= a.length; i++) {
    if (x == a[i - 1] || (y - i).abs() == (x - a[i - 1]).abs()) {
      return false;
    }
  }
  return true;
}

List<List<int>> nQueensStack(int n) {
  final solutions = <List<int>>[];
  final stack = <List<int>>[<int>[]];
  while (stack.isNotEmpty) {
    final a = stack.removeLast();
    if (a.length == n) {
      solutions.add(a);
    } else {
      for (var i = 1; i <= n; i++) {
        if (valid(i, a)) {
          final b = List<int>.from(a);
          b.add(i);
          stack.add(b);
        }
      }
    }
  }
  return solutions;
}

void main() {
  final cases = <List<dynamic>>[
    [8, 92, [8, 4, 1, 3, 6, 2, 7, 5]],
    [1, 1, [1]],
    [2, 0, null],
    [4, 2, [3, 1, 4, 2]],
  ];
  for (var idx = 0; idx < cases.length; idx++) {
    final c = cases[idx];
    final sols = nQueensStack(c[0] as int);
    if (sols.length != c[1] as int) throw StateError('case $idx count');
    if (c[2] != null && sols[0].toString() != c[2].toString()) {
      throw StateError('case $idx first');
    }
  }
  print('PASS');
}
''',
}

# ---------------- s5: 布尔数组标记（行号 0..n-1） ----------------
S5 = {
"rust": '''// @@BLOG@@
// LeetCode 107490876. 分书和八皇后问题 — Rust 版（方案5：八皇后布尔数组标记，行号 0..n-1）
fn n_queens_bool(n: usize) -> Vec<Vec<i32>> {
    let mut col_row = vec![0i32; n];
    let mut rows = vec![true; n];
    let mut diag1 = vec![true; 2 * n - 1]; // col - row + OFFSET
    let mut diag2 = vec![true; 2 * n - 1]; // col + row
    let offset = n - 1;
    let mut results: Vec<Vec<i32>> = vec![];

    fn place(
        col: usize,
        n: usize,
        offset: usize,
        col_row: &mut Vec<i32>,
        rows: &mut Vec<bool>,
        diag1: &mut Vec<bool>,
        diag2: &mut Vec<bool>,
        results: &mut Vec<Vec<i32>>,
    ) {
        if col == n {
            results.push(col_row.clone());
            return;
        }
        for row in 0..n {
            let d1 = col - row + offset;
            let d2 = col + row;
            if rows[row] && diag1[d1] && diag2[d2] {
                col_row[col] = row as i32;
                rows[row] = false;
                diag1[d1] = false;
                diag2[d2] = false;
                place(col + 1, n, offset, col_row, rows, diag1, diag2, results);
                rows[row] = true;
                diag1[d1] = true;
                diag2[d2] = true;
            }
        }
    }

    place(0, n, offset, &mut col_row, &mut rows, &mut diag1, &mut diag2, &mut results);
    results
}

fn main() {
    let cases: Vec<(usize, usize, Option<Vec<i32>>)> = vec![
        (8, 92, Some(vec![0, 4, 7, 5, 2, 6, 1, 3])),
        (1, 1, Some(vec![0])),
        (2, 0, None),
        (4, 2, Some(vec![1, 3, 0, 2])),
    ];
    for (idx, (n, count, first)) in cases.iter().enumerate() {
        let sols = n_queens_bool(*n);
        assert_eq!(sols.len(), *count, "case {} count mismatch", idx);
        if let Some(w) = first {
            assert_eq!(&sols[0], w, "case {} first mismatch", idx);
        }
    }
    println!("PASS");
}
''',
"lua": '''-- @@BLOG@@
-- LeetCode 107490876. 分书和八皇后问题 — Lua 版（方案5：八皇后布尔数组标记，行号 0..n-1）
local function n_queens_bool(n)
    local SIZE = n
    local col_row = {}
    local rows, diag1, diag2 = {}, {}, {}
    local OFFSET = SIZE - 1
    for i = 0, SIZE - 1 do col_row[i] = 0 end
    for i = 0, SIZE - 1 do rows[i] = true end
    for i = 0, 2 * SIZE - 2 do
        diag1[i] = true
        diag2[i] = true
    end
    local results = {}

    local function place(col)
        if col == SIZE then
            local snap = {}
            for i = 0, SIZE - 1 do snap[i + 1] = col_row[i] end
            results[#results + 1] = snap
            return
        end
        for row = 0, SIZE - 1 do
            local d1 = col - row + OFFSET
            local d2 = col + row
            if rows[row] and diag1[d1] and diag2[d2] then
                col_row[col] = row
                rows[row] = false
                diag1[d1] = false
                diag2[d2] = false
                place(col + 1)
                rows[row] = true
                diag1[d1] = true
                diag2[d2] = true
            end
        end
    end

    place(0)
    return results
end

local cases = {
    {8, 92, {0, 4, 7, 5, 2, 6, 1, 3}},
    {1, 1, {0}},
    {2, 0, nil},
    {4, 2, {1, 3, 0, 2}},
}
for idx, c in ipairs(cases) do
    local sols = n_queens_bool(c[1])
    assert(#sols == c[2], "case " .. idx .. " count mismatch: " .. #sols)
    if c[3] then
        for j = 1, #c[3] do
            assert(sols[1][j] == c[3][j], "case " .. idx .. " first mismatch")
        end
    end
end
print("PASS")
''',
"c": '''/* @@BLOG@@
 * LeetCode 107490876. 分书和八皇后问题 — C 版（方案5：八皇后布尔数组标记，行号 0..n-1）
 */
#include <stdio.h>
#include <string.h>

static int col_row[8];
static int rows[8];
static int diag1[16];
static int diag2[16];
static int sols[100][8];
static int sol_count = 0;
static int N;
static int OFFSET;

static void place(int col) {
    if (col == N) {
        memcpy(sols[sol_count], col_row, sizeof(int) * N);
        sol_count++;
        return;
    }
    for (int row = 0; row < N; row++) {
        int d1 = col - row + OFFSET;
        int d2 = col + row;
        if (rows[row] && diag1[d1] && diag2[d2]) {
            col_row[col] = row;
            rows[row] = 0;
            diag1[d1] = 0;
            diag2[d2] = 0;
            place(col + 1);
            rows[row] = 1;
            diag1[d1] = 1;
            diag2[d2] = 1;
        }
    }
}

static int n_queens_bool(int n) {
    N = n;
    OFFSET = n - 1;
    memset(rows, 1, sizeof(int) * n);
    memset(diag1, 1, sizeof(int) * (2 * n - 1));
    memset(diag2, 1, sizeof(int) * (2 * n - 1));
    sol_count = 0;
    place(0);
    return sol_count;
}

int main(void) {
    struct { int n; int count; int has_first; int first[8]; } cases[] = {
        {8, 92, 1, {0, 4, 7, 5, 2, 6, 1, 3}},
        {1, 1, 1, {0}},
        {2, 0, 0, {0}},
        {4, 2, 1, {1, 3, 0, 2}},
    };
    for (int idx = 0; idx < 4; idx++) {
        int count = n_queens_bool(cases[idx].n);
        if (count != cases[idx].count) { printf("case %d count %d\\n", idx, count); return 1; }
        if (cases[idx].has_first) {
            for (int j = 0; j < cases[idx].n; j++) {
                if (sols[0][j] != cases[idx].first[j]) { printf("case %d first\\n", idx); return 1; }
            }
        }
    }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''// @@BLOG@@
// LeetCode 107490876. 分书和八皇后问题 — C++ 版（方案5：八皇后布尔数组标记，行号 0..n-1）
#include <iostream>
#include <vector>

static std::vector<std::vector<int>> n_queens_bool(int n) {
    std::vector<int> col_row(n, 0);
    std::vector<bool> rows(n, true);
    std::vector<bool> diag1(2 * n - 1, true);
    std::vector<bool> diag2(2 * n - 1, true);
    int offset = n - 1;
    std::vector<std::vector<int>> results;

    std::function<void(int)> place = [&](int col) {
        if (col == n) {
            results.push_back(col_row);
            return;
        }
        for (int row = 0; row < n; ++row) {
            int d1 = col - row + offset;
            int d2 = col + row;
            if (rows[row] && diag1[d1] && diag2[d2]) {
                col_row[col] = row;
                rows[row] = false;
                diag1[d1] = false;
                diag2[d2] = false;
                place(col + 1);
                rows[row] = true;
                diag1[d1] = true;
                diag2[d2] = true;
            }
        }
    };

    place(0);
    return results;
}

int main() {
    struct Case { int n; int count; bool has_first; std::vector<int> first; };
    std::vector<Case> cases = {
        {8, 92, true, {0, 4, 7, 5, 2, 6, 1, 3}},
        {1, 1, true, {0}},
        {2, 0, false, {}},
        {4, 2, true, {1, 3, 0, 2}},
    };
    for (size_t idx = 0; idx < cases.size(); ++idx) {
        auto sols = n_queens_bool(cases[idx].n);
        if (static_cast<int>(sols.size()) != cases[idx].count) { std::cout << "case " << idx << " count" << std::endl; return 1; }
        if (cases[idx].has_first && sols[0] != cases[idx].first) { std::cout << "case " << idx << " first" << std::endl; return 1; }
    }
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''# @@BLOG@@
# LeetCode 107490876. 分书和八皇后问题 — R 版（方案5：八皇后布尔数组标记，行号 0..n-1）
n_queens_bool <- function(n) {
  SIZE <- n
  OFFSET <- SIZE - 1L
  ctx <- new.env(parent = emptyenv())
  ctx$col_row <- rep(0L, SIZE)
  ctx$rows <- rep(TRUE, SIZE)
  ctx$diag1 <- rep(TRUE, 2L * SIZE - 1L)
  ctx$diag2 <- rep(TRUE, 2L * SIZE - 1L)
  results <- list()

  place <- function(col) {
    if (col == SIZE) {
      results <<- c(results, list(ctx$col_row))
      return(invisible(NULL))
    }
    for (row in 0:(SIZE - 1L)) {
      d1 <- col - row + OFFSET + 1L   # R 1 基
      d2 <- col + row + 1L
      if (ctx$rows[row + 1L] && ctx$diag1[d1] && ctx$diag2[d2]) {
        ctx$col_row[col + 1L] <- row
        ctx$rows[row + 1L] <- FALSE
        ctx$diag1[d1] <- FALSE
        ctx$diag2[d2] <- FALSE
        place(col + 1L)
        ctx$rows[row + 1L] <- TRUE
        ctx$diag1[d1] <- TRUE
        ctx$diag2[d2] <- TRUE
      }
    }
  }

  place(0L)
  results
}

cases <- list(
  list(8L, 92L, c(0, 4, 7, 5, 2, 6, 1, 3)),
  list(1L, 1L, c(0)),
  list(2L, 0L, NULL),
  list(4L, 2L, c(1, 3, 0, 2))
)
for (idx in seq_along(cases)) {
  sols <- n_queens_bool(cases[[idx]][[1]])
  stopifnot(length(sols) == cases[[idx]][[2]])
  if (!is.null(cases[[idx]][[3]])) {
    stopifnot(identical(as.integer(sols[[1]]), as.integer(cases[[idx]][[3]])))
  }
}
cat("PASS\\n")
''',
"zig": '''// @@BLOG@@
// LeetCode 107490876. 分书和八皇后问题 — Zig 版（方案5：八皇后布尔数组标记，行号 0..n-1）
const std = @import("std");

var col_row: [8]i32 = undefined;
var rows: [8]bool = undefined;
var diag1: [16]bool = undefined;
var diag2: [16]bool = undefined;
var sols: [100][8]i32 = undefined;
var sol_count: usize = 0;
var N: usize = 0;
var OFFSET: usize = 0;

fn place(col: usize) void {
    if (col == N) {
        sols[sol_count] = col_row;
        sol_count += 1;
        return;
    }
    var row: usize = 0;
    while (row < N) : (row += 1) {
        const d1: i32 = @as(i32, @intCast(col)) - @as(i32, @intCast(row)) + @as(i32, @intCast(OFFSET));
        const d2: i32 = @as(i32, @intCast(col)) + @as(i32, @intCast(row));
        if (rows[row] and diag1[@intCast(d1)] and diag2[@intCast(d2)]) {
            col_row[col] = @intCast(row);
            rows[row] = false;
            diag1[@intCast(d1)] = false;
            diag2[@intCast(d2)] = false;
            place(col + 1);
            rows[row] = true;
            diag1[@intCast(d1)] = true;
            diag2[@intCast(d2)] = true;
        }
    }
}

fn nQueensBool(n: usize) usize {
    N = n;
    OFFSET = n - 1;
    for (0..n) |i| {
        rows[i] = true;
        col_row[i] = 0;
    }
    for (0..2 * n - 1) |i| {
        diag1[i] = true;
        diag2[i] = true;
    }
    sol_count = 0;
    place(0);
    return sol_count;
}

pub fn main() !void {
    const Case = struct { n: usize, count: usize, first: ?[8]i32, flen: usize };
    const cases = [_]Case{
        .{ .n = 8, .count = 92, .first = .{ 0, 4, 7, 5, 2, 6, 1, 3 }, .flen = 8 },
        .{ .n = 1, .count = 1, .first = .{ 0, 0, 0, 0, 0, 0, 0, 0 }, .flen = 1 },
        .{ .n = 2, .count = 0, .first = null, .flen = 0 },
        .{ .n = 4, .count = 2, .first = .{ 1, 3, 0, 2, 0, 0, 0, 0 }, .flen = 4 },
    };
    for (cases, 0..) |c, idx| {
        const count = nQueensBool(c.n);
        if (count != c.count) {
            std.debug.print("case {d} count {d}\\n", .{ idx, count });
            return error.TestFailed;
        }
        if (c.first) |f| {
            var j: usize = 0;
            while (j < c.flen) : (j += 1) {
                if (sols[0][j] != f[j]) return error.TestFailed;
            }
        }
    }
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''// @@BLOG@@
// LeetCode 107490876. 分书和八皇后问题 — Dart 版（方案5：八皇后布尔数组标记，行号 0..n-1）
List<List<int>> nQueensBool(int n) {
  final colRow = List<int>.filled(n, 0);
  final rows = List<bool>.filled(n, true);
  final diag1 = List<bool>.filled(2 * n - 1, true);
  final diag2 = List<bool>.filled(2 * n - 1, true);
  final offset = n - 1;
  final results = <List<int>>[];

  void place(int col) {
    if (col == n) {
      results.add(List<int>.from(colRow));
      return;
    }
    for (var row = 0; row < n; row++) {
      final d1 = col - row + offset;
      final d2 = col + row;
      if (rows[row] && diag1[d1] && diag2[d2]) {
        colRow[col] = row;
        rows[row] = false;
        diag1[d1] = false;
        diag2[d2] = false;
        place(col + 1);
        rows[row] = true;
        diag1[d1] = true;
        diag2[d2] = true;
      }
    }
  }

  place(0);
  return results;
}

void main() {
  final cases = <List<dynamic>>[
    [8, 92, [0, 4, 7, 5, 2, 6, 1, 3]],
    [1, 1, [0]],
    [2, 0, null],
    [4, 2, [1, 3, 0, 2]],
  ];
  for (var idx = 0; idx < cases.length; idx++) {
    final c = cases[idx];
    final sols = nQueensBool(c[0] as int);
    if (sols.length != c[1] as int) throw StateError('case $idx count');
    if (c[2] != null && sols[0].toString() != c[2].toString()) {
      throw StateError('case $idx first');
    }
  }
  print('PASS');
}
''',
}

# ---------------- s6: 不可变状态函数式（行号 0..n-1） ----------------
S6 = {
"rust": '''// @@BLOG@@
// LeetCode 107490876. 分书和八皇后问题 — Rust 版（方案6：八皇后不可变状态函数式）
fn n_queens_func(n: usize) -> Vec<Vec<i32>> {
    fn place(
        col: usize,
        n: usize,
        col_row: Vec<i32>,
        rows: Vec<bool>,
        diag1: Vec<bool>,
        diag2: Vec<bool>,
        results: &mut Vec<Vec<i32>>,
    ) {
        if col == n {
            results.push(col_row);
            return;
        }
        for row in 0..n {
            let d1 = col + n - 1 - row;
            let d2 = col + row;
            if rows[row] && diag1[d1] && diag2[d2] {
                let mut cr = col_row.clone();
                cr.push(row as i32);
                let mut nr = rows.clone();
                nr[row] = false;
                let mut nd1 = diag1.clone();
                nd1[d1] = false;
                let mut nd2 = diag2.clone();
                nd2[d2] = false;
                place(col + 1, n, cr, nr, nd1, nd2, results);
            }
        }
    }

    let mut results: Vec<Vec<i32>> = vec![];
    place(0, n, vec![], vec![true; n], vec![true; 2 * n - 1], vec![true; 2 * n - 1], &mut results);
    results
}

fn main() {
    let cases: Vec<(usize, usize, Option<Vec<i32>>)> = vec![
        (8, 92, Some(vec![0, 4, 7, 5, 2, 6, 1, 3])),
        (1, 1, Some(vec![0])),
        (2, 0, None),
        (4, 2, Some(vec![1, 3, 0, 2])),
    ];
    for (idx, (n, count, first)) in cases.iter().enumerate() {
        let sols = n_queens_func(*n);
        assert_eq!(sols.len(), *count, "case {} count mismatch", idx);
        if let Some(w) = first {
            assert_eq!(&sols[0], w, "case {} first mismatch", idx);
        }
    }
    println!("PASS");
}
''',
"lua": '''-- @@BLOG@@
-- LeetCode 107490876. 分书和八皇后问题 — Lua 版（方案6：八皇后不可变状态函数式）
local function n_queens_func(n)
    local SIZE = n
    local results = {}

    local function place(col, col_row, rows, diag1, diag2)
        if col == SIZE then
            local snap = {}
            for i = 1, #col_row do snap[i] = col_row[i] end
            results[#results + 1] = snap
            return
        end
        for row = 0, SIZE - 1 do
            local d1 = col - row + (SIZE - 1)
            local d2 = col + row
            if rows[row] and diag1[d1] and diag2[d2] then
                local nr = {}
                for k, v in pairs(rows) do nr[k] = v end
                nr[row] = false
                local nd1 = {}
                for k, v in pairs(diag1) do nd1[k] = v end
                nd1[d1] = false
                local nd2 = {}
                for k, v in pairs(diag2) do nd2[k] = v end
                nd2[d2] = false
                local ncol = {}
                for i = 1, #col_row do ncol[i] = col_row[i] end
                ncol[#ncol + 1] = row
                place(col + 1, ncol, nr, nd1, nd2)
            end
        end
    end

    local rows0, diag0 = {}, {}
    for i = 0, SIZE - 1 do rows0[i] = true end
    for i = 0, 2 * SIZE - 2 do diag0[i] = true end
    place(0, {}, rows0, diag0, {})
    -- diag2 与 diag1 同构，占位用同一初始表
    return results
end

-- 修正：diag2 需独立初始表
local function n_queens_func_fixed(n)
    local SIZE = n
    local results = {}

    local function place(col, col_row, rows, diag1, diag2)
        if col == SIZE then
            local snap = {}
            for i = 1, #col_row do snap[i] = col_row[i] end
            results[#results + 1] = snap
            return
        end
        for row = 0, SIZE - 1 do
            local d1 = col - row + (SIZE - 1)
            local d2 = col + row
            if rows[row] and diag1[d1] and diag2[d2] then
                local function copy(t)
                    local c = {}
                    for k, v in pairs(t) do c[k] = v end
                    return c
                end
                local nr = copy(rows); nr[row] = false
                local nd1 = copy(diag1); nd1[d1] = false
                local nd2 = copy(diag2); nd2[d2] = false
                local ncol = {}
                for i = 1, #col_row do ncol[i] = col_row[i] end
                ncol[#ncol + 1] = row
                place(col + 1, ncol, nr, nd1, nd2)
            end
        end
    end

    local rows0, diag10, diag20 = {}, {}, {}
    for i = 0, SIZE - 1 do rows0[i] = true end
    for i = 0, 2 * SIZE - 2 do
        diag10[i] = true
        diag20[i] = true
    end
    place(0, {}, rows0, diag10, diag20)
    return results
end

local cases = {
    {8, 92, {0, 4, 7, 5, 2, 6, 1, 3}},
    {1, 1, {0}},
    {2, 0, nil},
    {4, 2, {1, 3, 0, 2}},
}
for idx, c in ipairs(cases) do
    local sols = n_queens_func_fixed(c[1])
    assert(#sols == c[2], "case " .. idx .. " count mismatch: " .. #sols)
    if c[3] then
        for j = 1, #c[3] do
            assert(sols[1][j] == c[3][j], "case " .. idx .. " first mismatch")
        end
    end
end
print("PASS")
''',
"c": '''/* @@BLOG@@
 * LeetCode 107490876. 分书和八皇后问题 — C 版（方案6：八皇后不可变状态函数式）
 */
#include <stdio.h>
#include <string.h>

static const int LIKE_UNUSED = 0;

typedef struct {
    int col_row[8];
    int rows[8];
    int diag1[16];
    int diag2[16];
} State;

static int sols[100][8];
static int sol_count = 0;

static void place(int col, int n, State st) {
    if (col == n) {
        memcpy(sols[sol_count], st.col_row, sizeof(int) * n);
        sol_count++;
        return;
    }
    for (int row = 0; row < n; row++) {
        int d1 = col - row + (n - 1);
        int d2 = col + row;
        if (st.rows[row] && st.diag1[d1] && st.diag2[d2]) {
            State ns = st; /* 值拷贝 = 不可变语义 */
            ns.col_row[col] = row;
            ns.rows[row] = 0;
            ns.diag1[d1] = 0;
            ns.diag2[d2] = 0;
            place(col + 1, n, ns);
        }
    }
}

static int n_queens_func(int n) {
    State init;
    memset(&init, 0, sizeof(init));
    memset(init.rows, 1, sizeof(int) * n);
    memset(init.diag1, 1, sizeof(int) * (2 * n - 1));
    memset(init.diag2, 1, sizeof(int) * (2 * n - 1));
    sol_count = 0;
    place(0, n, init);
    return sol_count;
}

int main(void) {
    struct { int n; int count; int has_first; int first[8]; } cases[] = {
        {8, 92, 1, {0, 4, 7, 5, 2, 6, 1, 3}},
        {1, 1, 1, {0}},
        {2, 0, 0, {0}},
        {4, 2, 1, {1, 3, 0, 2}},
    };
    for (int idx = 0; idx < 4; idx++) {
        int count = n_queens_func(cases[idx].n);
        if (count != cases[idx].count) { printf("case %d count %d\\n", idx, count); return 1; }
        if (cases[idx].has_first) {
            for (int j = 0; j < cases[idx].n; j++) {
                if (sols[0][j] != cases[idx].first[j]) { printf("case %d first\\n", idx); return 1; }
            }
        }
    }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''// @@BLOG@@
// LeetCode 107490876. 分书和八皇后问题 — C++ 版（方案6：八皇后不可变状态函数式）
#include <functional>
#include <iostream>
#include <vector>

struct State {
    std::vector<int> col_row;
    std::vector<bool> rows;
    std::vector<bool> diag1;
    std::vector<bool> diag2;
};

static void place(int col, int n, State st, std::vector<std::vector<int>> &results) {
    if (col == n) {
        results.push_back(st.col_row);
        return;
    }
    for (int row = 0; row < n; ++row) {
        int d1 = col - row + (n - 1);
        int d2 = col + row;
        if (st.rows[row] && st.diag1[d1] && st.diag2[d2]) {
            State ns = st; /* 值拷贝 = 不可变语义 */
            ns.col_row.push_back(row);
            ns.rows[row] = false;
            ns.diag1[d1] = false;
            ns.diag2[d2] = false;
            place(col + 1, n, ns, results);
        }
    }
}

static std::vector<std::vector<int>> n_queens_func(int n) {
    State init;
    init.col_row.reserve(n);
    init.rows.assign(n, true);
    init.diag1.assign(2 * n - 1, true);
    init.diag2.assign(2 * n - 1, true);
    std::vector<std::vector<int>> results;
    place(0, n, init, results);
    return results;
}

int main() {
    struct Case { int n; int count; bool has_first; std::vector<int> first; };
    std::vector<Case> cases = {
        {8, 92, true, {0, 4, 7, 5, 2, 6, 1, 3}},
        {1, 1, true, {0}},
        {2, 0, false, {}},
        {4, 2, true, {1, 3, 0, 2}},
    };
    for (size_t idx = 0; idx < cases.size(); ++idx) {
        auto sols = n_queens_func(cases[idx].n);
        if (static_cast<int>(sols.size()) != cases[idx].count) { std::cout << "case " << idx << " count" << std::endl; return 1; }
        if (cases[idx].has_first && sols[0] != cases[idx].first) { std::cout << "case " << idx << " first" << std::endl; return 1; }
    }
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''# @@BLOG@@
# LeetCode 107490876. 分书和八皇后问题 — R 版（方案6：八皇后不可变状态函数式）
n_queens_func <- function(n) {
  SIZE <- n
  results <- list()

  place <- function(col, col_row, rows, diag1, diag2) {
    if (col == SIZE) {
      results <<- c(results, list(col_row))
      return(invisible(NULL))
    }
    for (row in 0:(SIZE - 1L)) {
      d1 <- col - row + SIZE        # R 1 基
      d2 <- col + row + 1L
      if (rows[row + 1L] && diag1[d1] && diag2[d2]) {
        nr <- rows; nr[row + 1L] <- FALSE
        nd1 <- diag1; nd1[d1] <- FALSE
        nd2 <- diag2; nd2[d2] <- FALSE
        place(col + 1L, c(col_row, row), nr, nd1, nd2)
      }
    }
  }

  rows0 <- rep(TRUE, SIZE)
  diag0 <- rep(TRUE, 2L * SIZE - 1L)
  place(0L, integer(0), rows0, diag0, diag0)
  results
}

cases <- list(
  list(8L, 92L, c(0, 4, 7, 5, 2, 6, 1, 3)),
  list(1L, 1L, c(0)),
  list(2L, 0L, NULL),
  list(4L, 2L, c(1, 3, 0, 2))
)
for (idx in seq_along(cases)) {
  sols <- n_queens_func(cases[[idx]][[1]])
  stopifnot(length(sols) == cases[[idx]][[2]])
  if (!is.null(cases[[idx]][[3]])) {
    stopifnot(identical(as.integer(sols[[1]]), as.integer(cases[[idx]][[3]])))
  }
}
cat("PASS\\n")
''',
"zig": '''// @@BLOG@@
// LeetCode 107490876. 分书和八皇后问题 — Zig 版（方案6：八皇后不可变状态函数式）
const std = @import("std");

const State = struct {
    col_row: [8]i32 = [_]i32{0} ** 8,
    col_len: usize = 0,
    rows: [8]bool = [_]bool{true} ** 8,
    diag1: [16]bool = [_]bool{true} ** 16,
    diag2: [16]bool = [_]bool{true} ** 16,
};

var sols: [100][8]i32 = undefined;
var sol_count: usize = 0;

fn place(col: usize, n: usize, st: State) void {
    if (col == n) {
        var j: usize = 0;
        while (j < st.col_len) : (j += 1) sols[sol_count][j] = st.col_row[j];
        sol_count += 1;
        return;
    }
    var row: usize = 0;
    while (row < n) : (row += 1) {
        const d1 = col + n - 1 - row;
        const d2 = col + row;
        if (st.rows[row] and st.diag1[d1] and st.diag2[d2]) {
            // 值拷贝 = 不可变语义
            var ns = st;
            ns.col_row[st.col_len] = @intCast(row);
            ns.col_len = st.col_len + 1;
            ns.rows[row] = false;
            ns.diag1[d1] = false;
            ns.diag2[d2] = false;
            place(col + 1, n, ns);
        }
    }
}

fn nQueensFunc(n: usize) usize {
    sol_count = 0;
    place(0, n, State{});
    return sol_count;
}

pub fn main() !void {
    const Case = struct { n: usize, count: usize, first: ?[8]i32, flen: usize };
    const cases = [_]Case{
        .{ .n = 8, .count = 92, .first = .{ 0, 4, 7, 5, 2, 6, 1, 3 }, .flen = 8 },
        .{ .n = 1, .count = 1, .first = .{ 0, 0, 0, 0, 0, 0, 0, 0 }, .flen = 1 },
        .{ .n = 2, .count = 0, .first = null, .flen = 0 },
        .{ .n = 4, .count = 2, .first = .{ 1, 3, 0, 2, 0, 0, 0, 0 }, .flen = 4 },
    };
    for (cases, 0..) |c, idx| {
        const count = nQueensFunc(c.n);
        if (count != c.count) {
            std.debug.print("case {d} count {d}\\n", .{ idx, count });
            return error.TestFailed;
        }
        if (c.first) |f| {
            var j: usize = 0;
            while (j < c.flen) : (j += 1) {
                if (sols[0][j] != f[j]) return error.TestFailed;
            }
        }
    }
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''// @@BLOG@@
// LeetCode 107490876. 分书和八皇后问题 — Dart 版（方案6：八皇后不可变状态函数式）
List<List<int>> nQueensFunc(int n) {
  final results = <List<int>>[];

  void place(int col, List<int> colRow, List<bool> rows, List<bool> diag1, List<bool> diag2) {
    if (col == n) {
      results.add(colRow);
      return;
    }
    for (var row = 0; row < n; row++) {
      final d1 = col - row + (n - 1);
      final d2 = col + row;
      if (rows[row] && diag1[d1] && diag2[d2]) {
        final nr = List<bool>.from(rows);
        nr[row] = false;
        final nd1 = List<bool>.from(diag1);
        nd1[d1] = false;
        final nd2 = List<bool>.from(diag2);
        nd2[d2] = false;
        place(col + 1, [...colRow, row], nr, nd1, nd2);
      }
    }
  }

  place(0, <int>[], List<bool>.filled(n, true), List<bool>.filled(2 * n - 1, true), List<bool>.filled(2 * n - 1, true));
  return results;
}

void main() {
  final cases = <List<dynamic>>[
    [8, 92, [0, 4, 7, 5, 2, 6, 1, 3]],
    [1, 1, [0]],
    [2, 0, null],
    [4, 2, [1, 3, 0, 2]],
  ];
  for (var idx = 0; idx < cases.length; idx++) {
    final c = cases[idx];
    final sols = nQueensFunc(c[0] as int);
    if (sols.length != c[1] as int) throw StateError('case $idx count');
    if (c[2] != null && sols[0].toString() != c[2].toString()) {
      throw StateError('case $idx first');
    }
  }
  print('PASS');
}
''',
}

# ---------------- s7: 位置对列表（行号 0..n-1） ----------------
S7 = {
"rust": '''// @@BLOG@@
// LeetCode 107490876. 分书和八皇后问题 — Rust 版（方案7：八皇后位置对列表）
fn n_queens_simple(n: usize) -> Vec<Vec<i32>> {
    let mut solutions: Vec<Vec<i32>> = vec![];

    fn safe(positions: &[(i32, i32)], r: i32, c: i32) -> bool {
        for &(rr, cc) in positions {
            if rr == r || (rr - r).abs() == (cc - c).abs() {
                return false;
            }
        }
        true
    }

    fn solve(col: usize, n: usize, positions: &mut Vec<(i32, i32)>, solutions: &mut Vec<Vec<i32>>) {
        if col == n {
            solutions.push(positions.iter().map(|p| p.0).collect());
            return;
        }
        for r in 0..n as i32 {
            if safe(positions, r, col as i32) {
                positions.push((r, col as i32));
                solve(col + 1, n, positions, solutions);
                positions.pop();
            }
        }
    }

    solve(0, n, &mut vec![], &mut solutions);
    solutions
}

fn main() {
    let cases: Vec<(usize, usize, Option<Vec<i32>>)> = vec![
        (8, 92, Some(vec![0, 4, 7, 5, 2, 6, 1, 3])),
        (1, 1, Some(vec![0])),
        (2, 0, None),
        (4, 2, Some(vec![1, 3, 0, 2])),
    ];
    for (idx, (n, count, first)) in cases.iter().enumerate() {
        let sols = n_queens_simple(*n);
        assert_eq!(sols.len(), *count, "case {} count mismatch", idx);
        if let Some(w) = first {
            assert_eq!(&sols[0], w, "case {} first mismatch", idx);
        }
    }
    println!("PASS");
}
''',
"lua": '''-- @@BLOG@@
-- LeetCode 107490876. 分书和八皇后问题 — Lua 版（方案7：八皇后位置对列表）
local function n_queens_simple(n)
    local positions = {}  -- { {row, col}, ... }
    local solutions = {}

    local function safe(r, c)
        for _, p in ipairs(positions) do
            if p[1] == r or math.abs(p[1] - r) == math.abs(p[2] - c) then
                return false
            end
        end
        return true
    end

    local function solve(col)
        if col == n then
            local snap = {}
            for i, p in ipairs(positions) do snap[i] = p[1] end
            solutions[#solutions + 1] = snap
            return
        end
        for r = 0, n - 1 do
            if safe(r, col) then
                positions[#positions + 1] = {r, col}
                solve(col + 1)
                table.remove(positions)
            end
        end
    end

    solve(0)
    return solutions
end

local cases = {
    {8, 92, {0, 4, 7, 5, 2, 6, 1, 3}},
    {1, 1, {0}},
    {2, 0, nil},
    {4, 2, {1, 3, 0, 2}},
}
for idx, c in ipairs(cases) do
    local sols = n_queens_simple(c[1])
    assert(#sols == c[2], "case " .. idx .. " count mismatch: " .. #sols)
    if c[3] then
        for j = 1, #c[3] do
            assert(sols[1][j] == c[3][j], "case " .. idx .. " first mismatch")
        end
    end
end
print("PASS")
''',
"c": '''/* @@BLOG@@
 * LeetCode 107490876. 分书和八皇后问题 — C 版（方案7：八皇后位置对列表）
 */
#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int row, col;
} Pair;

static Pair positions[8];
static int plen = 0;
static int sols[100][8];
static int sol_count = 0;
static int N;

static int safe(int r, int c) {
    for (int i = 0; i < plen; i++) {
        if (positions[i].row == r || abs(positions[i].row - r) == abs(positions[i].col - c)) return 0;
    }
    return 1;
}

static void solve(int col) {
    if (col == N) {
        for (int i = 0; i < N; i++) sols[sol_count][i] = positions[i].row;
        sol_count++;
        return;
    }
    for (int r = 0; r < N; r++) {
        if (safe(r, col)) {
            positions[plen].row = r;
            positions[plen].col = col;
            plen++;
            solve(col + 1);
            plen--;
        }
    }
}

static int n_queens_simple(int n) {
    N = n;
    plen = 0;
    sol_count = 0;
    solve(0);
    return sol_count;
}

int main(void) {
    struct { int n; int count; int has_first; int first[8]; } cases[] = {
        {8, 92, 1, {0, 4, 7, 5, 2, 6, 1, 3}},
        {1, 1, 1, {0}},
        {2, 0, 0, {0}},
        {4, 2, 1, {1, 3, 0, 2}},
    };
    for (int idx = 0; idx < 4; idx++) {
        int count = n_queens_simple(cases[idx].n);
        if (count != cases[idx].count) { printf("case %d count %d\\n", idx, count); return 1; }
        if (cases[idx].has_first) {
            for (int j = 0; j < cases[idx].n; j++) {
                if (sols[0][j] != cases[idx].first[j]) { printf("case %d first\\n", idx); return 1; }
            }
        }
    }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''// @@BLOG@@
// LeetCode 107490876. 分书和八皇后问题 — C++ 版（方案7：八皇后位置对列表）
#include <cmath>
#include <iostream>
#include <vector>

static std::vector<std::vector<int>> n_queens_simple(int n) {
    std::vector<std::pair<int, int>> positions;
    std::vector<std::vector<int>> solutions;

    std::function<bool(int, int)> safe = [&](int r, int c) {
        for (const auto &p : positions) {
            if (p.first == r || std::abs(p.first - r) == std::abs(p.second - c)) return false;
        }
        return true;
    };

    std::function<void(int)> solve = [&](int col) {
        if (col == n) {
            std::vector<int> rows;
            for (const auto &p : positions) rows.push_back(p.first);
            solutions.push_back(rows);
            return;
        }
        for (int r = 0; r < n; ++r) {
            if (safe(r, col)) {
                positions.push_back({r, col});
                solve(col + 1);
                positions.pop_back();
            }
        }
    };

    solve(0);
    return solutions;
}

int main() {
    struct Case { int n; int count; bool has_first; std::vector<int> first; };
    std::vector<Case> cases = {
        {8, 92, true, {0, 4, 7, 5, 2, 6, 1, 3}},
        {1, 1, true, {0}},
        {2, 0, false, {}},
        {4, 2, true, {1, 3, 0, 2}},
    };
    for (size_t idx = 0; idx < cases.size(); ++idx) {
        auto sols = n_queens_simple(cases[idx].n);
        if (static_cast<int>(sols.size()) != cases[idx].count) { std::cout << "case " << idx << " count" << std::endl; return 1; }
        if (cases[idx].has_first && sols[0] != cases[idx].first) { std::cout << "case " << idx << " first" << std::endl; return 1; }
    }
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''# @@BLOG@@
# LeetCode 107490876. 分书和八皇后问题 — R 版（方案7：八皇后位置对列表）
n_queens_simple <- function(n) {
  positions <- list()  # list(c(row, col), ...)
  solutions <- list()

  safe <- function(r, c) {
    for (p in positions) {
      if (p[1] == r || abs(p[1] - r) == abs(p[2] - c)) return(FALSE)
    }
    TRUE
  }

  solve <- function(col) {
    if (col == n) {
      solutions <<- c(solutions, list(vapply(positions, function(p) p[1], integer(1))))
      return(invisible(NULL))
    }
    for (r in 0:(n - 1L)) {
      if (safe(r, col)) {
        positions <<- c(positions, list(c(r, col)))
        solve(col + 1L)
        positions <<- positions[-length(positions)]
      }
    }
  }

  solve(0L)
  solutions
}

cases <- list(
  list(8L, 92L, c(0, 4, 7, 5, 2, 6, 1, 3)),
  list(1L, 1L, c(0)),
  list(2L, 0L, NULL),
  list(4L, 2L, c(1, 3, 0, 2))
)
for (idx in seq_along(cases)) {
  sols <- n_queens_simple(cases[[idx]][[1]])
  stopifnot(length(sols) == cases[[idx]][[2]])
  if (!is.null(cases[[idx]][[3]])) {
    stopifnot(identical(as.integer(sols[[1]]), as.integer(cases[[idx]][[3]])))
  }
}
cat("PASS\\n")
''',
"zig": '''// @@BLOG@@
// LeetCode 107490876. 分书和八皇后问题 — Zig 版（方案7：八皇后位置对列表）
const std = @import("std");

const Pair = struct { row: i32, col: i32 };

var positions: [8]Pair = undefined;
var plen: usize = 0;
var sols: [100][8]i32 = undefined;
var sol_count: usize = 0;
var N: usize = 0;

fn safe(r: i32, c: i32) bool {
    var i: usize = 0;
    while (i < plen) : (i += 1) {
        if (positions[i].row == r or @abs(positions[i].row - r) == @abs(positions[i].col - c)) return false;
    }
    return true;
}

fn solve(col: usize) void {
    if (col == N) {
        var i: usize = 0;
        while (i < N) : (i += 1) sols[sol_count][i] = positions[i].row;
        sol_count += 1;
        return;
    }
    var r: i32 = 0;
    while (r < @as(i32, @intCast(N))) : (r += 1) {
        if (safe(r, @intCast(col))) {
            positions[plen] = .{ .row = r, .col = @intCast(col) };
            plen += 1;
            solve(col + 1);
            plen -= 1;
        }
    }
}

fn nQueensSimple(n: usize) usize {
    N = n;
    plen = 0;
    sol_count = 0;
    solve(0);
    return sol_count;
}

pub fn main() !void {
    const Case = struct { n: usize, count: usize, first: ?[8]i32, flen: usize };
    const cases = [_]Case{
        .{ .n = 8, .count = 92, .first = .{ 0, 4, 7, 5, 2, 6, 1, 3 }, .flen = 8 },
        .{ .n = 1, .count = 1, .first = .{ 0, 0, 0, 0, 0, 0, 0, 0 }, .flen = 1 },
        .{ .n = 2, .count = 0, .first = null, .flen = 0 },
        .{ .n = 4, .count = 2, .first = .{ 1, 3, 0, 2, 0, 0, 0, 0 }, .flen = 4 },
    };
    for (cases, 0..) |c, idx| {
        const count = nQueensSimple(c.n);
        if (count != c.count) {
            std.debug.print("case {d} count {d}\\n", .{ idx, count });
            return error.TestFailed;
        }
        if (c.first) |f| {
            var j: usize = 0;
            while (j < c.flen) : (j += 1) {
                if (sols[0][j] != f[j]) return error.TestFailed;
            }
        }
    }
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''// @@BLOG@@
// LeetCode 107490876. 分书和八皇后问题 — Dart 版（方案7：八皇后位置对列表）
List<List<int>> nQueensSimple(int n) {
  final positions = <List<int>>[]; // [row, col]
  final solutions = <List<int>>[];

  bool safe(int r, int c) {
    for (final p in positions) {
      if (p[0] == r || (p[0] - r).abs() == (p[1] - c).abs()) {
        return false;
      }
    }
    return true;
  }

  void solve(int col) {
    if (col == n) {
      solutions.add(positions.map((p) => p[0]).toList());
      return;
    }
    for (var r = 0; r < n; r++) {
      if (safe(r, col)) {
        positions.add([r, col]);
        solve(col + 1);
        positions.removeLast();
      }
    }
  }

  solve(0);
  return solutions;
}

void main() {
  final cases = <List<dynamic>>[
    [8, 92, [0, 4, 7, 5, 2, 6, 1, 3]],
    [1, 1, [0]],
    [2, 0, null],
    [4, 2, [1, 3, 0, 2]],
  ];
  for (var idx = 0; idx < cases.length; idx++) {
    final c = cases[idx];
    final sols = nQueensSimple(c[0] as int);
    if (sols.length != c[1] as int) throw StateError('case $idx count');
    if (c[2] != null && sols[0].toString() != c[2].toString()) {
      throw StateError('case $idx first');
    }
  }
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
