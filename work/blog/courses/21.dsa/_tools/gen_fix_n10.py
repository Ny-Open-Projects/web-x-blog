#!/usr/bin/env python3
# gen_fix_n10.py — 补齐 notes/lc_107579658 转换视角提炼共性 × 7 语言
# solveUnified：统一"分书问题"(queen=false, 5人) 与 八皇后(queen=true) 的回溯框架
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from langlib import emit

REL = "notes/lc_107579658_抽象思维之转换视角_提炼共性"
BLOG = "来源（blog）：https://blog.csdn.net/tyro_java/article/details/107579658"
DESC = "抽象思维之转换视角：统一分书问题与八皇后的回溯框架"

LIKE = "[[0,0,1,1,0],[1,1,0,0,1],[0,1,1,0,1],[0,0,0,1,0],[0,1,0,0,1]]"

T_RUST = '''// @@BLOG@@
// LeetCode 107579658. 转换视角，提炼共性 — Rust 版（@@DESC@@）
// queen=false: 分书问题（5人，like 偏好矩阵）; queen=true: 八皇后

fn solve_unified(queen: bool) -> Vec<Vec<i32>> {
    let size = if queen { 8usize } else { 5usize };
    let like: [[i32; 5]; 5] = [0,0,1,1,0], 0], [1,1,0,0,1], [0,1,1,0,1], [0,0,0,1,0], [0,1,0,0,1]];
    let mut q = vec![-1i32; size];
    let mut rows = vec![true; size];
    let mut diag1 = vec![true; 2 * size - 1];
    let mut diag2 = vec![true; 2 * size - 1];
    let mut results: Vec<Vec<i32>> = vec![];

    let mut place = |col: usize, q: &mut Vec<i32>, results: &mut Vec<Vec<i32>>| -> () {};

    // 用显式递归函数实现（闭包可变借用冲突，改为内层 fn + 上下文结构）
    struct Ctx {
        queen: bool,
        size: usize,
        q: Vec<i32>,
        rows: Vec<bool>,
        diag1: Vec<bool>,
        diag2: Vec<bool>,
        results: Vec<Vec<i32>>,
    }

    fn is_valid(ctx: &Ctx, row: usize, col: usize) -> bool {
        if ctx.queen {
            true
        } else {
            LIKE_C[row][col] == 1
        }
    }

    impl Ctx {
        fn is_safe(&self, row: usize, col: usize) -> bool {
            if self.queen {
                self.rows[row]
                    && self.diag1[col + self.size - 1 - row]
                    && self.diag2[col + row]
            } else {
                self.rows[row]
            }
        }
        fn place(&mut self, col: usize) {
            if col == self.size {
                self.results.push(self.q.clone());
                return;
            }
            for row in 0..self.size {
                if !is_valid(self, row, col) {
                    continue;
                }
                if !self.is_safe(row, col) {
                    continue;
                }
                self.q[col] = row as i32;
                self.rows[row] = false;
                if self.queen {
                    let d1 = col + self.size - 1 - row;
                    let d2 = col + row;
                    self.diag1[d1] = false;
                    self.diag2[d2] = false;
                }
                self.place(col + 1);
                self.rows[row] = true;
                if self.queen {
                    let d1 = col + self.size - 1 - row;
                    let d2 = col + row;
                    self.diag1[d1] = true;
                    self.diag2[d2] = true;
                }
            }
        }
    }

    const LIKE_C: [[i32; 5]; 5] = [
        [0, 0, 1, 1, 0],
        [1, 1, 0, 0, 1],
        [0, 1, 1, 0, 1],
        [0, 0, 0, 1, 0],
        [0, 1, 0, 0, 1],
    ];

    let mut ctx = Ctx { queen, size, q, rows, diag1, diag2, results };
    ctx.place(0);
    ctx.results
}

fn main() {
    let want: Vec<Vec<i32>> = vec![vec![1, 2, 0, 3, 4], vec![1, 4, 0, 3, 2]];
    let got = solve_unified(false);
    assert_eq!(got, want, "solve_unified(false) mismatch");
    println!("PASS");
}
'''

# 上面 Rust 草稿有语法残渣，直接重写：
T_RUST = '''// @@BLOG@@
// LeetCode 107579658. 转换视角，提炼共性 — Rust 版（@@DESC@@）
// queen=false: 分书问题（5人，like 偏好矩阵）; queen=true: 八皇后

const LIKE: [[i32; 5]; 5] = [
    [0, 0, 1, 1, 0],
    [1, 1, 0, 0, 1],
    [0, 1, 1, 0, 1],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 1],
];

struct Ctx {
    queen: bool,
    size: usize,
    q: Vec<i32>,
    rows: Vec<bool>,
    diag1: Vec<bool>,
    diag2: Vec<bool>,
    results: Vec<Vec<i32>>,
}

impl Ctx {
    fn is_valid(&self, row: usize, col: usize) -> bool {
        if self.queen {
            true
        } else {
            LIKE[row][col] == 1
        }
    }

    fn is_safe(&self, row: usize, col: usize) -> bool {
        if self.queen {
            self.rows[row] && self.diag1[col + self.size - 1 - row] && self.diag2[col + row]
        } else {
            self.rows[row]
        }
    }

    fn place(&mut self, col: usize) {
        if col == self.size {
            self.results.push(self.q.clone());
            return;
        }
        for row in 0..self.size {
            if !self.is_valid(row, col) {
                continue;
            }
            if !self.is_safe(row, col) {
                continue;
            }
            self.q[col] = row as i32;
            self.rows[row] = false;
            if self.queen {
                let d1 = col + self.size - 1 - row;
                let d2 = col + row;
                self.diag1[d1] = false;
                self.diag2[d2] = false;
            }
            self.place(col + 1);
            self.rows[row] = true;
            if self.queen {
                let d1 = col + self.size - 1 - row;
                let d2 = col + row;
                self.diag1[d1] = true;
                self.diag2[d2] = true;
            }
        }
    }
}

fn solve_unified(queen: bool) -> Vec<Vec<i32>> {
    let size = if queen { 8usize } else { 5usize };
    let mut ctx = Ctx {
        queen,
        size,
        q: vec![-1i32; size],
        rows: vec![true; size],
        diag1: vec![true; 2 * size - 1],
        diag2: vec![true; 2 * size - 1],
        results: vec![],
    };
    ctx.place(0);
    ctx.results
}

fn main() {
    let want: Vec<Vec<i32>> = vec![vec![1, 2, 0, 3, 4], vec![1, 4, 0, 3, 2]];
    let got = solve_unified(false);
    assert_eq!(got, want, "solve_unified(false) mismatch");
    println!("PASS");
}
'''

T_LUA = '''-- @@BLOG@@
-- LeetCode 107579658. 转换视角，提炼共性 — Lua 版（@@DESC@@）
-- queen=false: 分书问题（5人，like 偏好矩阵）; queen=true: 八皇后
local function solve_unified(queen)
    local SIZE = queen and 8 or 5
    local like = {
        {0, 0, 1, 1, 0},
        {1, 1, 0, 0, 1},
        {0, 1, 1, 0, 1},
        {0, 0, 0, 1, 0},
        {0, 1, 0, 0, 1},
    }
    local Q = {}
    for i = 1, SIZE do Q[i] = -1 end
    local rows = {}
    for i = 1, SIZE do rows[i] = true end
    local diag1, diag2 = {}, {}
    for i = 1, 2 * SIZE - 1 do
        diag1[i] = true
        diag2[i] = true
    end
    local results = {}

    local function is_valid(row, col)
        if queen then return true end
        return like[row][col] == 1
    end

    local function is_safe(row, col)
        if queen then
            return rows[row] and diag1[col - row + SIZE - 1] and diag2[col + row - 1]
        end
        return rows[row]
    end

    local function place(col)
        if col > SIZE then
            local snap = {}
            for i = 1, SIZE do snap[i] = Q[i] end
            results[#results + 1] = snap
            return
        end
        for row = 1, SIZE do
            if is_valid(row, col) and is_safe(row, col) then
                Q[col] = row - 1  -- 0 基行号
                rows[row] = false
                local d1, d2 = col - (row - 1) + SIZE - 1, (col - 1) + (row - 1) + 1
                if queen then
                    diag1[d1] = false
                    diag2[d2] = false
                end
                place(col + 1)
                rows[row] = true
                if queen then
                    diag1[d1] = true
                    diag2[d2] = true
                end
            end
        end
    end

    place(1)
    return results
end

local want = {{1, 2, 0, 3, 4}, {1, 4, 0, 3, 2}}
local got = solve_unified(false)
assert(#got == #want, "results length mismatch")
for i = 1, #want do
    for j = 1, 5 do
        assert(got[i][j] == want[i][j], string.format("results[%d][%d] mismatch", i, j))
    end
end
print("PASS")
'''

T_C = '''/* @@BLOG@@
 * LeetCode 107579658. 转换视角，提炼共性 — C 版（@@DESC@@）
 * queen=false: 分书问题（5人，like 偏好矩阵）; queen=true: 八皇后
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

#define MAX_SIZE 8
static int queen_flag;
static int SIZE;
static int Q[MAX_SIZE];
static int rows[MAX_SIZE];
static int diag1[2 * MAX_SIZE];
static int diag2[2 * MAX_SIZE];
static int results[64][MAX_SIZE];
static int result_count;

static int is_valid(int row, int col) {
    if (queen_flag) return 1;
    return LIKE[row][col] == 1;
}

static int is_safe(int row, int col) {
    if (queen_flag) return rows[row] && diag1[col - row + SIZE - 1] && diag2[col + row];
    return rows[row];
}

static void place(int col) {
    if (col == SIZE) {
        memcpy(results[result_count], Q, sizeof(int) * SIZE);
        result_count++;
        return;
    }
    for (int row = 0; row < SIZE; row++) {
        if (!is_valid(row, col)) continue;
        if (!is_safe(row, col)) continue;
        Q[col] = row;
        rows[row] = 0;
        if (queen_flag) {
            diag1[col - row + SIZE - 1] = 0;
            diag2[col + row] = 0;
        }
        place(col + 1);
        rows[row] = 1;
        if (queen_flag) {
            diag1[col - row + SIZE - 1] = 1;
            diag2[col + row] = 1;
        }
    }
}

int main(void) {
    int want[2][5] = {{1, 2, 0, 3, 4}, {1, 4, 0, 3, 2}};

    queen_flag = 0;
    SIZE = 5;
    memset(rows, 1, sizeof(rows));
    memset(diag1, 1, sizeof(diag1));
    memset(diag2, 1, sizeof(diag2));
    result_count = 0;
    place(0);

    if (result_count != 2) { printf("FAIL count %d\\n", result_count); return 1; }
    for (int i = 0; i < 2; i++)
        for (int j = 0; j < 5; j++)
            if (results[i][j] != want[i][j]) {
                printf("FAIL results[%d][%d]\\n", i, j);
                return 1;
            }
    printf("PASS\\n");
    return 0;
}
'''

T_CPP = '''// @@BLOG@@
// LeetCode 107579658. 转换视角，提炼共性 — C++ 版（@@DESC@@）
// queen=false: 分书问题（5人，like 偏好矩阵）; queen=true: 八皇后
#include <iostream>
#include <vector>

class Unified {
public:
    explicit Unified(bool queen) : queen_(queen), size_(queen ? 8 : 5) {
        q_.assign(size_, -1);
        rows_.assign(size_, true);
        diag1_.assign(2 * size_ - 1, true);
        diag2_.assign(2 * size_ - 1, true);
    }

    std::vector<std::vector<int>> solve() {
        place(0);
        return results_;
    }

private:
    static const std::vector<std::vector<int>> LIKE;

    bool is_valid(int row, int col) const {
        if (queen_) return true;
        return LIKE[row][col] == 1;
    }

    bool is_safe(int row, int col) const {
        if (queen_) return rows_[row] && diag1_[col - row + size_ - 1] && diag2_[col + row];
        return rows_[row];
    }

    void place(int col) {
        if (col == static_cast<int>(size_)) {
            results_.push_back(q_);
            return;
        }
        for (int row = 0; row < static_cast<int>(size_); ++row) {
            if (!is_valid(row, col)) continue;
            if (!is_safe(row, col)) continue;
            q_[col] = row;
            rows_[row] = false;
            if (queen_) {
                diag1_[col - row + size_ - 1] = false;
                diag2_[col + row] = false;
            }
            place(col + 1);
            rows_[row] = true;
            if (queen_) {
                diag1_[col - row + size_ - 1] = true;
                diag2_[col + row] = true;
            }
        }
    }

    bool queen_;
    size_t size_;
    std::vector<int> q_;
    std::vector<bool> rows_;
    std::vector<bool> diag1_, diag2_;
    std::vector<std::vector<int>> results_;
};

const std::vector<std::vector<int>> Unified::LIKE = {
    {0, 0, 1, 1, 0},
    {1, 1, 0, 0, 1},
    {0, 1, 1, 0, 1},
    {0, 0, 0, 1, 0},
    {0, 1, 0, 0, 1},
};

int main() {
    std::vector<std::vector<int>> want = {{1, 2, 0, 3, 4}, {1, 4, 0, 3, 2}};
    Unified solver(false);
    std::vector<std::vector<int>> got = solver.solve();
    if (got != want) { std::cout << "FAIL mismatch" << std::endl; return 1; }
    std::cout << "PASS" << std::endl;
    return 0;
}
'''

T_R = '''# @@BLOG@@
# LeetCode 107579658. 转换视角，提炼共性 — R 版（@@DESC@@）
# queen=FALSE: 分书问题（5人，like 偏好矩阵）; queen=TRUE: 八皇后

LIKE <- matrix(c(
  0, 0, 1, 1, 0,
  1, 1, 0, 0, 1,
  0, 1, 1, 0, 1,
  0, 0, 0, 1, 0,
  0, 1, 0, 0, 1
), nrow = 5, byrow = TRUE)

solve_unified <- function(queen) {
  SIZE <- if (queen) 8L else 5L
  ctx <- new.env(parent = emptyenv())
  ctx$Q <- rep(-1L, SIZE)
  ctx$rows <- rep(TRUE, SIZE)
  ctx$diag1 <- rep(TRUE, 2L * SIZE - 1L)
  ctx$diag2 <- rep(TRUE, 2L * SIZE - 1L)
  results <- list()

  is_valid <- function(row, col) {
    if (queen) return(TRUE)
    LIKE[row + 1L, col + 1L] == 1
  }

  is_safe <- function(row, col) {
    if (queen) {
      ctx$rows[row + 1L] && ctx$diag1[col - row + SIZE] && ctx$diag2[col + row + 1L]
    } else {
      ctx$rows[row + 1L]
    }
  }

  place <- function(col) {
    if (col == SIZE) {
      results <<- c(results, list(ctx$Q))
      return(invisible(NULL))
    }
    for (row in 0:(SIZE - 1L)) {
      if (!is_valid(row, col)) next
      if (!is_safe(row, col)) next
      ctx$Q[col + 1L] <- row
      ctx$rows[row + 1L] <- FALSE
      if (queen) {
        ctx$diag1[col - row + SIZE] <- FALSE
        ctx$diag2[col + row + 1L] <- FALSE
      }
      place(col + 1L)
      ctx$rows[row + 1L] <- TRUE
      if (queen) {
        ctx$diag1[col - row + SIZE] <- TRUE
        ctx$diag2[col + row + 1L] <- TRUE
      }
    }
  }

  place(0L)
  results
}

want <- list(c(1L, 2L, 0L, 3L, 4L), c(1L, 4L, 0L, 3L, 2L))
got <- solve_unified(FALSE)
stopifnot(length(got) == 2L)
for (i in 1:2) {
  stopifnot(identical(as.integer(got[[i]]), as.integer(want[[i]])))
}
cat("PASS\\n")
'''

T_ZIG = '''// @@BLOG@@
// LeetCode 107579658. 转换视角，提炼共性 — Zig 版（@@DESC@@）
// queen=false: 分书问题（5人，like 偏好矩阵）; queen=true: 八皇后
const std = @import("std");

const LIKE = [5][5]i32{
    .{ 0, 0, 1, 1, 0 },
    .{ 1, 1, 0, 0, 1 },
    .{ 0, 1, 1, 0, 1 },
    .{ 0, 0, 0, 1, 0 },
    .{ 0, 1, 0, 0, 1 },
};

const Ctx = struct {
    queen: bool,
    size: usize,
    q: [8]i32,
    rows: [8]bool,
    diag1: [16]bool,
    diag2: [16]bool,
    results: [64][8]i32 = undefined,
    result_count: usize = 0,

    fn isValid(self: *const Ctx, row: usize, col: usize) bool {
        if (self.queen) return true;
        return LIKE[row][col] == 1;
    }

    fn isSafe(self: *const Ctx, row: usize, col: usize) bool {
        if (self.queen) {
            return self.rows[row] and self.diag1[col + self.size - 1 - row] and self.diag2[col + row];
        }
        return self.rows[row];
    }

    fn place(self: *Ctx, col: usize) void {
        if (col == self.size) {
            self.results[self.result_count] = self.q;
            self.result_count += 1;
            return;
        }
        var row: usize = 0;
        while (row < self.size) : (row += 1) {
            if (!self.isValid(row, col)) continue;
            if (!self.isSafe(row, col)) continue;
            self.q[col] = @intCast(row);
            self.rows[row] = false;
            if (self.queen) {
                self.diag1[col + self.size - 1 - row] = false;
                self.diag2[col + row] = false;
            }
            self.place(col + 1);
            self.rows[row] = true;
            if (self.queen) {
                self.diag1[col + self.size - 1 - row] = true;
                self.diag2[col + row] = true;
            }
        }
    }
};

fn solveUnified(queen: bool) Ctx {
    const size: usize = if (queen) 8 else 5;
    var ctx = Ctx{
        .queen = queen,
        .size = size,
        .q = [_]i32{-1} ** 8,
        .rows = [_]bool{true} ** 8,
        .diag1 = [_]bool{true} ** 16,
        .diag2 = [_]bool{true} ** 16,
    };
    ctx.place(0);
    return ctx;
}

pub fn main() !void {
    const want = [2][5]i32{ .{ 1, 2, 0, 3, 4 }, .{ 1, 4, 0, 3, 2 } };
    const ctx = solveUnified(false);
    if (ctx.result_count != 2) {
        std.debug.print("FAIL count {d}\\n", .{ctx.result_count});
        return error.TestFailed;
    }
    for (want, 0..) |w, i| {
        for (w, 0..) |x, j| {
            if (ctx.results[i][j] != x) {
                std.debug.print("FAIL results[{d}][{d}]\\n", .{ i, j });
                return error.TestFailed;
            }
        }
    }
    std.debug.print("PASS\\n", .{});
}
'''

T_DART = '''// @@BLOG@@
// LeetCode 107579658. 转换视角，提炼共性 — Dart 版（@@DESC@@）
// queen=false: 分书问题（5人，like 偏好矩阵）; queen=true: 八皇后
const LIKE = [
  [0, 0, 1, 1, 0],
  [1, 1, 0, 0, 1],
  [0, 1, 1, 0, 1],
  [0, 0, 0, 1, 0],
  [0, 1, 0, 0, 1],
];

List<List<int>> solveUnified(bool queen) {
  final size = queen ? 8 : 5;
  final q = List<int>.filled(size, -1);
  final rows = List<bool>.filled(size, true);
  final diag1 = List<bool>.filled(2 * size - 1, true);
  final diag2 = List<bool>.filled(2 * size - 1, true);
  final results = <List<int>>[];

  bool isValid(int row, int col) {
    if (queen) return true;
    return LIKE[row][col] == 1;
  }

  bool isSafe(int row, int col) {
    if (queen) return rows[row] && diag1[col + size - 1 - row] && diag2[col + row];
    return rows[row];
  }

  void place(int col) {
    if (col == size) {
      results.add(List<int>.from(q));
      return;
    }
    for (var row = 0; row < size; row++) {
      if (!isValid(row, col)) continue;
      if (!isSafe(row, col)) continue;
      q[col] = row;
      rows[row] = false;
      if (queen) {
        diag1[col + size - 1 - row] = false;
        diag2[col + row] = false;
      }
      place(col + 1);
      rows[row] = true;
      if (queen) {
        diag1[col + size - 1 - row] = true;
        diag2[col + row] = true;
      }
    }
  }

  place(0);
  return results;
}

void main() {
  final want = <List<int>>[
    [1, 2, 0, 3, 4],
    [1, 4, 0, 3, 2],
  ];
  final got = solveUnified(false);
  if (got.toString() != want.toString()) {
    throw StateError('solveUnified(false) mismatch: ' + got.toString());
  }
  print('PASS');
}
'''

GENS = {
    "rust": (T_RUST, ".rs"),
    "lua": (T_LUA, ".lua"),
    "c": (T_C, ".c"),
    "cpp": (T_CPP, ".cpp"),
    "r": (T_R, ".R"),
    "zig": (T_ZIG, ".zig"),
    "dart": (T_DART, ".dart"),
}

def main():
    for lang, (t, ext) in GENS.items():
        out = t.replace("@@BLOG@@", BLOG).replace("@@DESC@@", DESC)
        emit(lang, REL + "/solution_1___1" + ext, out)

if __name__ == "__main__":
    main()
