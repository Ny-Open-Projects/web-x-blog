#!/usr/bin/env python3
# gen_fix_n19.py — 补齐 notes/lc_107737496 代码重构_隔离变化 × 7 语言（13 解法）
# s1-3 螺旋矩阵(递归)  s4 方向模拟  s5/s6 Matrix 封装  s7 分派表  s8 Filler+hasNext
# s9 规则串状态机  s10 9x9 全螺旋  s11 Rule 循环  s12 Location/Rule/Filler  s13 正则匹配
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from langlib import emit

REL = "notes/lc_107737496_抽象思维之代码重构_隔离变化"
BLOG = "来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496"

SPIRAL6_WANT = [" 1 20 19 18 17 16", " 2 21 32 31 30 15", " 3 22 33 36 29 14",
                " 4 23 34 35 28 13", " 5 24 25 26 27 12", " 6  7  8  9 10 11"]
MATRIX9_WANT = [" 1 32 31 30 29 28 27 26 25", " 2 33 56 55 54 53 52 51 24",
                " 3 34 57 72 71 70 69 50 23", " 4 35 58 73 80 79 68 49 22",
                " 5 36 59 74 81 78 67 48 21", " 6 37 60 75 76 77 66 47 20",
                " 7 38 61 62 63 64 65 46 19", " 8 39 40 41 42 43 44 45 18",
                " 9 10 11 12 13 14 15 16 17"]

# ---------------- A: s1/s2/s3 递归螺旋矩阵（同一实现，三种排版） ----------------
A = {
"rust": '''// @@BLOG@@
// LeetCode 107737496. 代码重构_隔离变化 — Rust 版（方案@@N@@：螺旋矩阵递归填充）
struct Matrix {
    n: usize,
    m: Vec<Vec<i32>>,
}

impl Matrix {
    fn new(size: usize) -> Self {
        Matrix { n: size, m: vec![vec![0i32; size]; size] }
    }

    fn fill(&mut self, mut num: i32, begin: usize, size: usize) {
        if size == 0 {
            return;
        }
        if size == 1 {
            self.m[begin][begin] = num;
            return;
        }
        for j in 0..size - 1 {
            self.m[begin + j][begin] = num;
            num += 1;
        }
        for j in 0..size - 1 {
            self.m[begin + size - 1][begin + j] = num;
            num += 1;
        }
        let mut j = size - 1;
        while j > 0 {
            self.m[begin + j][begin + size - 1] = num;
            num += 1;
            j -= 1;
        }
        let mut j = size - 1;
        while j > 0 {
            self.m[begin][begin + j] = num;
            num += 1;
            j -= 1;
        }
        self.fill(num, begin + 1, size - 2);
    }
}

fn fmt_row(row: &[i32]) -> String {
    row.iter().map(|x| format!("{:2}", x)).collect::<Vec<_>>().join(" ")
}

fn main() {
    let mut m = Matrix::new(6);
    m.fill(1, 0, 6);
    let rows: Vec<String> = m.m.iter().map(|r| fmt_row(r)).collect();
    let want = [
        " 1 20 19 18 17 16",
        " 2 21 32 31 30 15",
        " 3 22 33 36 29 14",
        " 4 23 34 35 28 13",
        " 5 24 25 26 27 12",
        " 6  7  8  9 10 11",
    ];
    for i in 0..6 {
        assert_eq!(rows[i], want[i], "spiral6 row {}", i);
    }
    println!("PASS");
}
''',
"lua": '''-- @@BLOG@@
-- LeetCode 107737496. 代码重构_隔离变化 — Lua 版（方案@@N@@：螺旋矩阵递归填充）
local Matrix = {}
Matrix.__index = Matrix
function Matrix.new(size)
    local m = setmetatable({ N = size, M = {} }, Matrix)
    for i = 1, size do
        m.M[i] = {}
        for j = 1, size do m.M[i][j] = 0 end
    end
    return m
end
function Matrix:fill(num, begin_, size)
    if size == 0 then return end
    if size == 1 then
        self.M[begin_ + 1][begin_ + 1] = num
        return
    end
    for j = 0, size - 2 do
        self.M[begin_ + j + 1][begin_ + 1] = num
        num = num + 1
    end
    for j = 0, size - 2 do
        self.M[begin_ + size][begin_ + j + 1] = num
        num = num + 1
    end
    for j = size - 1, 1, -1 do
        self.M[begin_ + j + 1][begin_ + size] = num
        num = num + 1
    end
    for j = size - 1, 1, -1 do
        self.M[begin_ + 1][begin_ + j + 1] = num
        num = num + 1
    end
    self:fill(num, begin_ + 1, size - 2)
end

local function fmt_row(row)
    local parts = {}
    for i, x in ipairs(row) do
        parts[i] = string.format("%2d", x)
    end
    return table.concat(parts, " ")
end

local m = Matrix.new(6)
m:fill(1, 0, 6)
local rows = {}
for i = 1, 6 do rows[i] = fmt_row(m.M[i]) end
local want = {
    " 1 20 19 18 17 16",
    " 2 21 32 31 30 15",
    " 3 22 33 36 29 14",
    " 4 23 34 35 28 13",
    " 5 24 25 26 27 12",
    " 6  7  8  9 10 11",
}
for i = 1, 6 do
    assert(rows[i] == want[i], "spiral6 row " .. i)
end
print("PASS")
''',
"c": '''/* @@BLOG@@
 * LeetCode 107737496. 代码重构_隔离变化 — C 版（方案@@N@@：螺旋矩阵递归填充）
 */
#include <stdio.h>
#include <string.h>

static int M[6][6];

static void fill_spiral(int num, int begin, int size) {
    if (size == 0) return;
    if (size == 1) { M[begin][begin] = num; return; }
    for (int j = 0; j < size - 1; j++) { M[begin + j][begin] = num; num++; }
    for (int j = 0; j < size - 1; j++) { M[begin + size - 1][begin + j] = num; num++; }
    for (int j = size - 1; j > 0; j--) { M[begin + j][begin + size - 1] = num; num++; }
    for (int j = size - 1; j > 0; j--) { M[begin][begin + j] = num; num++; }
    fill_spiral(num, begin + 1, size - 2);
}

static void fmt_row(const int *row, int n, char *out) {
    out[0] = 0;
    char cell[8];
    for (int i = 0; i < n; i++) {
        snprintf(cell, sizeof(cell), "%2d", row[i]);
        if (i) strcat(out, " ");
        strcat(out, cell);
    }
}

int main(void) {
    fill_spiral(1, 0, 6);
    const char *want[6] = {
        " 1 20 19 18 17 16",
        " 2 21 32 31 30 15",
        " 3 22 33 36 29 14",
        " 4 23 34 35 28 13",
        " 5 24 25 26 27 12",
        " 6  7  8  9 10 11",
    };
    for (int i = 0; i < 6; i++) {
        char got[64];
        fmt_row(M[i], 6, got);
        if (strcmp(got, want[i]) != 0) {
            printf("spiral6 row %d failed: got [%s] want [%s]\\n", i, got, want[i]);
            return 1;
        }
    }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''// @@BLOG@@
// LeetCode 107737496. 代码重构_隔离变化 — C++ 版（方案@@N@@：螺旋矩阵递归填充）
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

class Matrix {
public:
    explicit Matrix(int size) : n_(size), m_(size, std::vector<int>(size, 0)) {}

    void fill(int num, int begin, int size) {
        if (size == 0) return;
        if (size == 1) { m_[begin][begin] = num; return; }
        for (int j = 0; j < size - 1; ++j) { m_[begin + j][begin] = num++; }
        for (int j = 0; j < size - 1; ++j) { m_[begin + size - 1][begin + j] = num++; }
        for (int j = size - 1; j > 0; --j) { m_[begin + j][begin + size - 1] = num++; }
        for (int j = size - 1; j > 0; --j) { m_[begin][begin + j] = num++; }
        fill(num, begin + 1, size - 2);
    }

    const std::vector<std::vector<int>> &rows() const { return m_; }

private:
    int n_;
    std::vector<std::vector<int>> m_;
};

static std::string fmt_row(const std::vector<int> &row) {
    std::ostringstream oss;
    for (size_t i = 0; i < row.size(); ++i) {
        if (i) oss << " ";
        oss.width(2);
        oss << row[i];
    }
    return oss.str();
}

int main() {
    Matrix m(6);
    m.fill(1, 0, 6);
    const char *want[6] = {
        " 1 20 19 18 17 16",
        " 2 21 32 31 30 15",
        " 3 22 33 36 29 14",
        " 4 23 34 35 28 13",
        " 5 24 25 26 27 12",
        " 6  7  8  9 10 11",
    };
    for (int i = 0; i < 6; ++i) {
        std::string got = fmt_row(m.rows()[i]);
        if (got != want[i]) { std::cout << "spiral6 row " << i << " failed" << std::endl; return 1; }
    }
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''# @@BLOG@@
# LeetCode 107737496. 代码重构_隔离变化 — R 版（方案@@N@@：螺旋矩阵递归填充）
M <- matrix(0L, nrow = 6L, ncol = 6L)

fill_spiral <- function(num, begin, size) {
  if (size == 0L) return(invisible(num))
  if (size == 1L) {
    M[begin + 1L, begin + 1L] <<- num
    return(invisible(num))
  }
  for (j in 0:(size - 2L)) {
    M[begin + j + 1L, begin + 1L] <<- num
    num <- num + 1L
  }
  for (j in 0:(size - 2L)) {
    M[begin + size, begin + j + 1L] <<- num
    num <- num + 1L
  }
  for (j in (size - 1L):1L) {
    M[begin + j + 1L, begin + size] <<- num
    num <- num + 1L
  }
  for (j in (size - 1L):1L) {
    M[begin + 1L, begin + j + 1L] <<- num
    num <- num + 1L
  }
  fill_spiral(num, begin + 1L, size - 2L)
  invisible(NULL)
}

fmt_row <- function(row) paste(sprintf("%2d", row), collapse = " ")

fill_spiral(1L, 0L, 6L)
want <- c(
  " 1 20 19 18 17 16",
  " 2 21 32 31 30 15",
  " 3 22 33 36 29 14",
  " 4 23 34 35 28 13",
  " 5 24 25 26 27 12",
  " 6  7  8  9 10 11"
)
for (i in 1:6) {
  got <- fmt_row(M[i, ])
  stopifnot(identical(got, want[i]))
}
cat("PASS\\n")
''',
"zig": '''// @@BLOG@@
// LeetCode 107737496. 代码重构_隔离变化 — Zig 版（方案@@N@@：螺旋矩阵递归填充）
const std = @import("std");

var M: [6][6]i32 = undefined;

fn fillSpiral(num0: i32, begin: usize, size: usize) void {
    var num = num0;
    if (size == 0) return;
    if (size == 1) {
        M[begin][begin] = num;
        return;
    }
    var j: usize = 0;
    while (j < size - 1) : (j += 1) {
        M[begin + j][begin] = num;
        num += 1;
    }
    j = 0;
    while (j < size - 1) : (j += 1) {
        M[begin + size - 1][begin + j] = num;
        num += 1;
    }
    j = size - 1;
    while (j > 0) {
        M[begin + j][begin + size - 1] = num;
        num += 1;
        j -= 1;
    }
    j = size - 1;
    while (j > 0) {
        M[begin][begin + j] = num;
        num += 1;
        j -= 1;
    }
    fillSpiral(num, begin + 1, size - 2);
}

fn fmtRow(buf: []u8, row: []const i32) ![]u8 {
    var n: usize = 0;
    for (row, 0..) |x, i| {
        if (i != 0) {
            buf[n] = ' ';
            n += 1;
        }
        var cell_buf: [16]u8 = undefined;
        const cell = try std.fmt.bufPrint(&cell_buf, "{d}", .{x});
        if (cell.len < 2) {
            buf[n] = ' ';
            n += 1;
        }
        for (cell) |ch| {
            buf[n] = ch;
            n += 1;
        }
    }
    return buf[0..n];
}

pub fn main() !void {
    fillSpiral(1, 0, 6);
    const want = [6][]const u8{
        " 1 20 19 18 17 16",
        " 2 21 32 31 30 15",
        " 3 22 33 36 29 14",
        " 4 23 34 35 28 13",
        " 5 24 25 26 27 12",
        " 6  7  8  9 10 11",
    };
    var buf: [64]u8 = undefined;
    for (want, 0..) |w, i| {
        const got = try fmtRow(&buf, &M[i]);
        if (!std.mem.eql(u8, got, w)) {
            std.debug.print("spiral6 row {d} failed\\n", .{i});
            return error.TestFailed;
        }
    }
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''// @@BLOG@@
// LeetCode 107737496. 代码重构_隔离变化 — Dart 版（方案@@N@@：螺旋矩阵递归填充）
class Matrix {
  int n;
  List<List<int>> m;
  Matrix(this.n) : m = List.generate(n, (_) => List<int>.filled(n, 0));

  void fill(int num, int begin, int size) {
    if (size == 0) return;
    if (size == 1) {
      m[begin][begin] = num;
      return;
    }
    for (var j = 0; j < size - 1; j++) {
      m[begin + j][begin] = num;
      num++;
    }
    for (var j = 0; j < size - 1; j++) {
      m[begin + size - 1][begin + j] = num;
      num++;
    }
    for (var j = size - 1; j > 0; j--) {
      m[begin + j][begin + size - 1] = num;
      num++;
    }
    for (var j = size - 1; j > 0; j--) {
      m[begin][begin + j] = num;
      num++;
    }
    fill(num, begin + 1, size - 2);
  }
}

String fmtRow(List<int> row) => row.map((x) => x.toString().padLeft(2)).join(' ');

void main() {
  final m = Matrix(6);
  m.fill(1, 0, 6);
  final want = <String>[
    ' 1 20 19 18 17 16',
    ' 2 21 32 31 30 15',
    ' 3 22 33 36 29 14',
    ' 4 23 34 35 28 13',
    ' 5 24 25 26 27 12',
    ' 6  7  8  9 10 11',
  ];
  for (var i = 0; i < 6; i++) {
    final got = fmtRow(m.m[i]);
    if (got != want[i]) throw StateError('spiral6 row $i failed');
  }
  print('PASS');
}
''',
}

# ---------------- B: s4 方向模拟 placeFill ----------------
B = {
"rust": '''// @@BLOG@@
// LeetCode 107737496. 代码重构_隔离变化 — Rust 版（方案4：螺旋矩阵方向模拟 placeFill）
fn place_fill(n: usize) -> Vec<Vec<i32>> {
    let mut m = vec![vec![0i32; n]; n];
    let (mut row, mut col) = (0usize, 0usize);
    let mut direction = 'D';
    let mut num = 1i32;
    let total = n * n;
    while num <= total as i32 {
        m[row][col] = num;
        num += 1;
        if direction == 'D' {
            if row + 1 < n && m[row + 1][col] == 0 {
                row += 1;
            } else {
                direction = 'R';
                col += 1;
            }
        } else if direction == 'R' {
            if col + 1 < n && m[row][col + 1] == 0 {
                col += 1;
            } else {
                direction = 'U';
                row -= 1;
            }
        } else if direction == 'U' {
            if row >= 1 && m[row - 1][col] == 0 {
                row -= 1;
            } else {
                direction = 'L';
                col -= 1;
            }
        } else {
            if col >= 1 && m[row][col - 1] == 0 {
                col -= 1;
            } else {
                direction = 'D';
                row += 1;
            }
        }
    }
    m
}

fn eq_mat(a: &[Vec<i32>], b: &[&[i32]]) -> bool {
    a.len() == b.len()
        && a.iter().zip(b.iter()).all(|(x, y)| x.as_slice() == *y)
}

fn main() {
    let got3 = place_fill(3);
    assert!(eq_mat(&got3, &[&[1, 8, 7], &[2, 9, 6], &[3, 4, 5]]), "place3");
    let got4 = place_fill(4);
    assert!(eq_mat(&got4, &[&[1, 12, 11, 10], &[2, 13, 16, 9], &[3, 14, 15, 8], &[4, 5, 6, 7]]), "place4");
    println!("PASS");
}
''',
"lua": '''-- @@BLOG@@
-- LeetCode 107737496. 代码重构_隔离变化 — Lua 版（方案4：螺旋矩阵方向模拟 placeFill）
local function place_fill(n)
    local m = {}
    for i = 1, n do
        m[i] = {}
        for j = 1, n do m[i][j] = 0 end
    end
    -- 内部 1 基，输出 0 基
    local row, col = 1, 1
    local direction = "D"
    local num = 1
    local total = n * n
    while num <= total do
        m[row][col] = num
        num = num + 1
        if direction == "D" then
            if row + 1 <= n and m[row + 1][col] == 0 then row = row + 1
            else direction = "R"; col = col + 1 end
        elseif direction == "R" then
            if col + 1 <= n and m[row][col + 1] == 0 then col = col + 1
            else direction = "U"; row = row - 1 end
        elseif direction == "U" then
            if row - 1 >= 1 and m[row - 1][col] == 0 then row = row - 1
            else direction = "L"; col = col - 1 end
        else
            if col - 1 >= 1 and m[row][col - 1] == 0 then col = col - 1
            else direction = "D"; row = row + 1 end
        end
    end
    -- 转 0 基输出
    local out = {}
    for i = 1, n do
        out[i] = {}
        for j = 1, n do out[i][j] = m[i][j] end
    end
    return out
end

local got3 = place_fill(3)
local want3 = {{1, 8, 7}, {2, 9, 6}, {3, 4, 5}}
for i = 1, 3 do for j = 1, 3 do assert(got3[i][j] == want3[i][j], "place3") end end
local got4 = place_fill(4)
local want4 = {{1, 12, 11, 10}, {2, 13, 16, 9}, {3, 14, 15, 8}, {4, 5, 6, 7}}
for i = 1, 4 do for j = 1, 4 do assert(got4[i][j] == want4[i][j], "place4") end end
print("PASS")
''',
"c": '''/* @@BLOG@@
 * LeetCode 107737496. 代码重构_隔离变化 — C 版（方案4：螺旋矩阵方向模拟 placeFill）
 */
#include <stdio.h>
#include <string.h>

static void place_fill(int n, int m[][8]) {
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++) m[i][j] = 0;
    int row = 0, col = 0;
    char direction = 'D';
    int num = 1;
    int total = n * n;
    while (num <= total) {
        m[row][col] = num;
        num++;
        if (direction == 'D') {
            if (row + 1 < n && m[row + 1][col] == 0) row++;
            else { direction = 'R'; col++; }
        } else if (direction == 'R') {
            if (col + 1 < n && m[row][col + 1] == 0) col++;
            else { direction = 'U'; row--; }
        } else if (direction == 'U') {
            if (row - 1 >= 0 && m[row - 1][col] == 0) row--;
            else { direction = 'L'; col--; }
        } else {
            if (col - 1 >= 0 && m[row][col - 1] == 0) col--;
            else { direction = 'D'; row++; }
        }
    }
}

static int eq_mat(const int a[][8], const int want[][8], int n) {
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            if (a[i][j] != want[i][j]) return 0;
    return 1;
}

int main(void) {
    int got[8][8];
    int want3[3][8] = {{1, 8, 7}, {2, 9, 6}, {3, 4, 5}};
    int want4[4][8] = {{1, 12, 11, 10}, {2, 13, 16, 9}, {3, 14, 15, 8}, {4, 5, 6, 7}};
    place_fill(3, got);
    if (!eq_mat(got, want3, 3)) { printf("place3 failed\\n"); return 1; }
    place_fill(4, got);
    if (!eq_mat(got, want4, 4)) { printf("place4 failed\\n"); return 1; }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''// @@BLOG@@
// LeetCode 107737496. 代码重构_隔离变化 — C++ 版（方案4：螺旋矩阵方向模拟 placeFill）
#include <iostream>
#include <vector>

static std::vector<std::vector<int>> place_fill(int n) {
    std::vector<std::vector<int>> m(n, std::vector<int>(n, 0));
    int row = 0, col = 0;
    char direction = 'D';
    int num = 1;
    int total = n * n;
    while (num <= total) {
        m[row][col] = num;
        ++num;
        if (direction == 'D') {
            if (row + 1 < n && m[row + 1][col] == 0) ++row;
            else { direction = 'R'; ++col; }
        } else if (direction == 'R') {
            if (col + 1 < n && m[row][col + 1] == 0) ++col;
            else { direction = 'U'; --row; }
        } else if (direction == 'U') {
            if (row - 1 >= 0 && m[row - 1][col] == 0) --row;
            else { direction = 'L'; --col; }
        } else {
            if (col - 1 >= 0 && m[row][col - 1] == 0) --col;
            else { direction = 'D'; ++row; }
        }
    }
    return m;
}

int main() {
    auto got3 = place_fill(3);
    if (got3 != std::vector<std::vector<int>>({{1, 8, 7}, {2, 9, 6}, {3, 4, 5}})) {
        std::cout << "place3 failed" << std::endl;
        return 1;
    }
    auto got4 = place_fill(4);
    if (got4 != std::vector<std::vector<int>>({{1, 12, 11, 10}, {2, 13, 16, 9}, {3, 14, 15, 8}, {4, 5, 6, 7}})) {
        std::cout << "place4 failed" << std::endl;
        return 1;
    }
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''# @@BLOG@@
# LeetCode 107737496. 代码重构_隔离变化 — R 版（方案4：螺旋矩阵方向模拟 placeFill）
place_fill <- function(n) {
  m <- matrix(0L, nrow = n, ncol = n)
  row <- 1L; col <- 1L
  direction <- "D"
  num <- 1L
  total <- n * n
  while (num <= total) {
    m[row, col] <- num
    num <- num + 1L
    if (direction == "D") {
      if (row + 1L <= n && m[row + 1L, col] == 0L) {
        row <- row + 1L
      } else {
        direction <- "R"; col <- col + 1L
      }
    } else if (direction == "R") {
      if (col + 1L <= n && m[row, col + 1L] == 0L) {
        col <- col + 1L
      } else {
        direction <- "U"; row <- row - 1L
      }
    } else if (direction == "U") {
      if (row - 1L >= 1L && m[row - 1L, col] == 0L) {
        row <- row - 1L
      } else {
        direction <- "L"; col <- col - 1L
      }
    } else {
      if (col - 1L >= 1L && m[row, col - 1L] == 0L) {
        col <- col - 1L
      } else {
        direction <- "D"; row <- row + 1L
      }
    }
  }
  m
}

got3 <- place_fill(3L)
want3 <- matrix(c(1, 8, 7, 2, 9, 6, 3, 4, 5), nrow = 3, byrow = TRUE)
stopifnot(identical(as.integer(got3), as.integer(want3)))
got4 <- place_fill(4L)
want4 <- matrix(c(1, 12, 11, 10, 2, 13, 16, 9, 3, 14, 15, 8, 4, 5, 6, 7), nrow = 4, byrow = TRUE)
stopifnot(identical(as.integer(got4), as.integer(want4)))
cat("PASS\\n")
''',
"zig": '''// @@BLOG@@
// LeetCode 107737496. 代码重构_隔离变化 — Zig 版（方案4：螺旋矩阵方向模拟 placeFill）
const std = @import("std");

fn placeFill(n: usize, m: *[8][8]i32) void {
    for (0..n) |i| {
        for (0..n) |j| m[i][j] = 0;
    }
    var row: usize = 0;
    var col: usize = 0;
    var direction: u8 = 'D';
    var num: i32 = 1;
    const total: i32 = @intCast(n * n);
    while (num <= total) {
        m[row][col] = num;
        num += 1;
        if (direction == 'D') {
            if (row + 1 < n and m[row + 1][col] == 0) {
                row += 1;
            } else {
                direction = 'R';
                col += 1;
            }
        } else if (direction == 'R') {
            if (col + 1 < n and m[row][col + 1] == 0) {
                col += 1;
            } else {
                direction = 'U';
                row -= 1;
            }
        } else if (direction == 'U') {
            if (row >= 1 and m[row - 1][col] == 0) {
                row -= 1;
            } else {
                direction = 'L';
                col -= 1;
            }
        } else {
            if (col >= 1 and m[row][col - 1] == 0) {
                col -= 1;
            } else {
                direction = 'D';
                row += 1;
            }
        }
    }
}

fn eqMat(a: *[8][8]i32, want: []const []const i32, n: usize) bool {
    for (0..n) |i| {
        for (0..n) |j| {
            if (a[i][j] != want[i][j]) return false;
        }
    }
    return true;
}

pub fn main() !void {
    var got: [8][8]i32 = undefined;
    const want3 = [3][]const i32{ &.{ 1, 8, 7 }, &.{ 2, 9, 6 }, &.{ 3, 4, 5 } };
    placeFill(3, &got);
    if (!eqMat(&got, &want3, 3)) return error.TestFailed;
    const want4 = [4][]const i32{ &.{ 1, 12, 11, 10 }, &.{ 2, 13, 16, 9 }, &.{ 3, 14, 15, 8 }, &.{ 4, 5, 6, 7 } };
    placeFill(4, &got);
    if (!eqMat(&got, &want4, 4)) return error.TestFailed;
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''// @@BLOG@@
// LeetCode 107737496. 代码重构_隔离变化 — Dart 版（方案4：螺旋矩阵方向模拟 placeFill）
List<List<int>> placeFill(int n) {
  final m = List.generate(n, (_) => List<int>.filled(n, 0));
  var row = 0, col = 0;
  var direction = 'D';
  var num = 1;
  final total = n * n;
  while (num <= total) {
    m[row][col] = num;
    num++;
    if (direction == 'D') {
      if (row + 1 < n && m[row + 1][col] == 0) {
        row++;
      } else {
        direction = 'R';
        col++;
      }
    } else if (direction == 'R') {
      if (col + 1 < n && m[row][col + 1] == 0) {
        col++;
      } else {
        direction = 'U';
        row--;
      }
    } else if (direction == 'U') {
      if (row - 1 >= 0 && m[row - 1][col] == 0) {
        row--;
      } else {
        direction = 'L';
        col--;
      }
    } else {
      if (col - 1 >= 0 && m[row][col - 1] == 0) {
        col--;
      } else {
        direction = 'D';
        row++;
      }
    }
  }
  return m;
}

void main() {
  if (placeFill(3).toString() != '[[1, 8, 7], [2, 9, 6], [3, 4, 5]]') {
    throw StateError('place3 failed');
  }
  if (placeFill(4).toString() != '[[1, 12, 11, 10], [2, 13, 16, 9], [3, 14, 15, 8], [4, 5, 6, 7]]') {
    throw StateError('place4 failed');
  }
  print('PASS');
}
''',
}

# ---------------- C: s5 Matrix 封装（set + call） ----------------
C = {
"rust": '''// @@BLOG@@
// LeetCode 107737496. 代码重构_隔离变化 — Rust 版（方案5：Matrix 封装 set/call）
struct Matrix {
    row: usize,
    col: usize,
    buf: Vec<Vec<i32>>,
}

impl Matrix {
    fn new(r: usize, c: usize) -> Self {
        Matrix { row: r, col: c, buf: vec![vec![0i32; c]; r] }
    }
    fn set(&mut self, r: usize, c: usize, v: i32) {
        self.buf[r][c] = v;
    }
    fn call(&self, r: usize, c: usize) -> i32 {
        self.buf[r][c]
    }
}

fn main() {
    let mut m = Matrix::new(4, 5);
    for i in 0..4 {
        for j in 0..5 {
            m.set(i, j, (i * j) as i32);
        }
    }
    assert_eq!(m.call(2, 3), 6, "matrix call");
    println!("PASS");
}
''',
"lua": '''-- @@BLOG@@
-- LeetCode 107737496. 代码重构_隔离变化 — Lua 版（方案5：Matrix 封装 set/call）
local Matrix = {}
Matrix.__index = Matrix
function Matrix.new(r, c)
    local m = setmetatable({ row = r, col = c, buf = {} }, Matrix)
    for i = 1, r do
        m.buf[i] = {}
        for j = 1, c do m.buf[i][j] = 0 end
    end
    return m
end
function Matrix:set(r, c, v) self.buf[r + 1][c + 1] = v end
function Matrix:call(r, c) return self.buf[r + 1][c + 1] end

local m = Matrix.new(4, 5)
for i = 0, 3 do
    for j = 0, 4 do m:set(i, j, i * j) end
end
assert(m:call(2, 3) == 6, "matrix call")
print("PASS")
''',
"c": '''/* @@BLOG@@
 * LeetCode 107737496. 代码重构_隔离变化 — C 版（方案5：Matrix 封装 set/call）
 */
#include <stdio.h>
#include <string.h>

typedef struct {
    int row, col;
    int buf[8][8];
} Matrix;

static void matrix_init(Matrix *m, int r, int c) {
    m->row = r;
    m->col = c;
    memset(m->buf, 0, sizeof(m->buf));
}

static void matrix_set(Matrix *m, int r, int c, int v) {
    m->buf[r][c] = v;
}

static int matrix_call(const Matrix *m, int r, int c) {
    return m->buf[r][c];
}

int main(void) {
    Matrix m;
    matrix_init(&m, 4, 5);
    for (int i = 0; i < 4; i++)
        for (int j = 0; j < 5; j++)
            matrix_set(&m, i, j, i * j);
    if (matrix_call(&m, 2, 3) != 6) { printf("matrix call failed\\n"); return 1; }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''// @@BLOG@@
// LeetCode 107737496. 代码重构_隔离变化 — C++ 版（方案5：Matrix 封装 set/call）
#include <iostream>
#include <vector>

class Matrix {
public:
    Matrix(int r, int c) : row_(r), col_(c), buf_(r, std::vector<int>(c, 0)) {}
    void set(int r, int c, int v) { buf_[r][c] = v; }
    int call(int r, int c) const { return buf_[r][c]; }

private:
    int row_;
    int col_;
    std::vector<std::vector<int>> buf_;
};

int main() {
    Matrix m(4, 5);
    for (int i = 0; i < 4; ++i)
        for (int j = 0; j < 5; ++j)
            m.set(i, j, i * j);
    if (m.call(2, 3) != 6) { std::cout << "matrix call failed" << std::endl; return 1; }
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''# @@BLOG@@
# LeetCode 107737496. 代码重构_隔离变化 — R 版（方案5：Matrix 封装 set/call）
Matrix <- function(r, c) {
  e <- new.env(parent = emptyenv())
  e$row <- r
  e$col <- c
  e$buf <- matrix(0L, nrow = r, ncol = c)
  class(e) <- "Matrix"
  e
}

matrix_set <- function(m, r, c, v) m$buf[r + 1L, c + 1L] <- v
matrix_call <- function(m, r, c) m$buf[r + 1L, c + 1L]

m <- Matrix(4L, 5L)
for (i in 0:3) {
  for (j in 0:4) matrix_set(m, i, j, i * j)
}
stopifnot(matrix_call(m, 2L, 3L) == 6L)
cat("PASS\\n")
''',
"zig": '''// @@BLOG@@
// LeetCode 107737496. 代码重构_隔离变化 — Zig 版（方案5：Matrix 封装 set/call）
const std = @import("std");

const Matrix = struct {
    row: usize,
    col: usize,
    buf: [8][8]i32 = [_][8]i32{[_]i32{0} ** 8} ** 8,

    fn init(r: usize, c: usize) Matrix {
        return .{ .row = r, .col = c };
    }
    fn set(self: *Matrix, r: usize, c: usize, v: i32) void {
        self.buf[r][c] = v;
    }
    fn call(self: *const Matrix, r: usize, c: usize) i32 {
        return self.buf[r][c];
    }
};

pub fn main() !void {
    var m = Matrix.init(4, 5);
    var i: usize = 0;
    while (i < 4) : (i += 1) {
        var j: usize = 0;
        while (j < 5) : (j += 1) {
            m.set(i, j, @intCast(i * j));
        }
    }
    if (m.call(2, 3) != 6) return error.TestFailed;
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''// @@BLOG@@
// LeetCode 107737496. 代码重构_隔离变化 — Dart 版（方案5：Matrix 封装 set/call）
class Matrix {
  int row, col;
  List<List<int>> buf;
  Matrix(this.row, this.col)
      : buf = List.generate(row, (_) => List<int>.filled(col, 0));

  void set(int r, int c, int v) {
    buf[r][c] = v;
  }

  int call(int r, int c) {
    return buf[r][c];
  }
}

void main() {
  final m = Matrix(4, 5);
  for (var i = 0; i < 4; i++) {
    for (var j = 0; j < 5; j++) {
      m.set(i, j, i * j);
    }
  }
  if (m.call(2, 3) != 6) throw StateError('matrix call failed');
  print('PASS');
}
''',
}

# ---------------- D: s6 Matrix 直接 buf 访问 ----------------
D = {
"rust": '''// @@BLOG@@
// LeetCode 107737496. 代码重构_隔离变化 — Rust 版（方案6：Matrix 公开 buf 直接访问）
struct Matrix {
    row: usize,
    col: usize,
    buf: Vec<Vec<i32>>,
}

impl Matrix {
    fn new(r: usize, c: usize) -> Self {
        Matrix { row: r, col: c, buf: vec![vec![0i32; c]; r] }
    }
    fn call(&self, r: usize, c: usize) -> i32 {
        self.buf[r][c]
    }
}

fn main() {
    let mut m = Matrix::new(4, 5);
    for i in 0..4 {
        for j in 0..5 {
            m.buf[i][j] = (i * j) as i32; // 直接访问 buf
        }
    }
    assert_eq!(m.call(2, 3), 6, "matrix call");
    println!("PASS");
}
''',
"lua": '''-- @@BLOG@@
-- LeetCode 107737496. 代码重构_隔离变化 — Lua 版（方案6：Matrix 公开 buf 直接访问）
local Matrix = {}
Matrix.__index = Matrix
function Matrix.new(r, c)
    local m = setmetatable({ row = r, col = c, buf = {} }, Matrix)
    for i = 1, r do
        m.buf[i] = {}
        for j = 1, c do m.buf[i][j] = 0 end
    end
    return m
end
function Matrix:call(r, c) return self.buf[r + 1][c + 1] end

local m = Matrix.new(4, 5)
for i = 0, 3 do
    for j = 0, 4 do m.buf[i + 1][j + 1] = i * j end
end
assert(m:call(2, 3) == 6, "matrix call")
print("PASS")
''',
"c": '''/* @@BLOG@@
 * LeetCode 107737496. 代码重构_隔离变化 — C 版（方案6：Matrix 公开 buf 直接访问）
 */
#include <stdio.h>
#include <string.h>

typedef struct {
    int row, col;
    int buf[8][8];
} Matrix;

static void matrix_init(Matrix *m, int r, int c) {
    m->row = r;
    m->col = c;
    memset(m->buf, 0, sizeof(m->buf));
}

static int matrix_call(const Matrix *m, int r, int c) {
    return m->buf[r][c];
}

int main(void) {
    Matrix m;
    matrix_init(&m, 4, 5);
    for (int i = 0; i < 4; i++)
        for (int j = 0; j < 5; j++)
            m.buf[i][j] = i * j; /* 直接访问 buf */
    if (matrix_call(&m, 2, 3) != 6) { printf("matrix call failed\\n"); return 1; }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''// @@BLOG@@
// LeetCode 107737496. 代码重构_隔离变化 — C++ 版（方案6：Matrix 公开 buf 直接访问）
#include <iostream>
#include <vector>

class Matrix {
public:
    int row, col;
    std::vector<std::vector<int>> buf;
    Matrix(int r, int c) : row(r), col(c), buf(r, std::vector<int>(c, 0)) {}
    int call(int r, int c) const { return buf[r][c]; }
};

int main() {
    Matrix m(4, 5);
    for (int i = 0; i < 4; ++i)
        for (int j = 0; j < 5; ++j)
            m.buf[i][j] = i * j; /* 直接访问 buf */
    if (m.call(2, 3) != 6) { std::cout << "matrix call failed" << std::endl; return 1; }
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''# @@BLOG@@
# LeetCode 107737496. 代码重构_隔离变化 — R 版（方案6：Matrix 公开 buf 直接访问）
Matrix <- function(r, c) {
  e <- new.env(parent = emptyenv())
  e$row <- r
  e$col <- c
  e$buf <- matrix(0L, nrow = r, ncol = c)
  class(e) <- "Matrix"
  e
}

matrix_call <- function(m, r, c) m$buf[r + 1L, c + 1L]

m <- Matrix(4L, 5L)
for (i in 0:3) {
  for (j in 0:4) m$buf[i + 1L, j + 1L] <- i * j  # 直接访问 buf
}
stopifnot(matrix_call(m, 2L, 3L) == 6L)
cat("PASS\\n")
''',
"zig": '''// @@BLOG@@
// LeetCode 107737496. 代码重构_隔离变化 — Zig 版（方案6：Matrix 公开 buf 直接访问）
const std = @import("std");

const Matrix = struct {
    row: usize,
    col: usize,
    buf: [8][8]i32 = [_][8]i32{[_]i32{0} ** 8} ** 8,

    fn init(r: usize, c: usize) Matrix {
        return .{ .row = r, .col = c };
    }
    fn call(self: *const Matrix, r: usize, c: usize) i32 {
        return self.buf[r][c];
    }
};

pub fn main() !void {
    var m = Matrix.init(4, 5);
    var i: usize = 0;
    while (i < 4) : (i += 1) {
        var j: usize = 0;
        while (j < 5) : (j += 1) {
            m.buf[i][j] = @intCast(i * j); // 直接访问 buf
        }
    }
    if (m.call(2, 3) != 6) return error.TestFailed;
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''// @@BLOG@@
// LeetCode 107737496. 代码重构_隔离变化 — Dart 版（方案6：Matrix 公开 buf 直接访问）
class Matrix {
  int row, col;
  List<List<int>> buf;
  Matrix(this.row, this.col)
      : buf = List.generate(row, (_) => List<int>.filled(col, 0));

  int call(int r, int c) {
    return buf[r][c];
  }
}

void main() {
  final m = Matrix(4, 5);
  for (var i = 0; i < 4; i++) {
    for (var j = 0; j < 5; j++) {
      m.buf[i][j] = i * j; // 直接访问 buf
    }
  }
  if (m.call(2, 3) != 6) throw StateError('matrix call failed');
  print('PASS');
}
''',
}

# ---------------- E: s7 分派表 place ----------------
E = {
"rust": '''// @@BLOG@@
// LeetCode 107737496. 代码重构_隔离变化 — Rust 版（方案7：螺旋矩阵分派表 place）
enum Move {
    Keep(usize, usize),
    Turn(usize, usize, char),
}

fn place(row: usize, col: usize, direction: char, n: usize, m: &[Vec<i32>]) -> Move {
    match direction {
        'D' => {
            if row + 1 < n && m[row + 1][col] == 0 {
                Move::Keep(row + 1, col)
            } else {
                Move::Turn(row, col + 1, 'R')
            }
        }
        'R' => {
            if col + 1 < n && m[row][col + 1] == 0 {
                Move::Keep(row, col + 1)
            } else {
                Move::Turn(row - 1, col, 'U')
            }
        }
        'U' => {
            if row >= 1 && m[row - 1][col] == 0 {
                Move::Keep(row - 1, col)
            } else {
                Move::Turn(row, col - 1, 'L')
            }
        }
        _ => {
            if col >= 1 && m[row][col - 1] == 0 {
                Move::Keep(row, col - 1)
            } else {
                Move::Turn(row + 1, col, 'D')
            }
        }
    }
}

fn fill_spiral(n: usize) -> Vec<Vec<i32>> {
    let mut m = vec![vec![0i32; n]; n];
    let (mut row, mut col) = (0usize, 0usize);
    let mut direction = 'D';
    let mut num = 1i32;
    while num <= (n * n) as i32 {
        m[row][col] = num;
        num += 1;
        match place(row, col, direction, n, &m) {
            Move::Keep(r, c) => {
                row = r;
                col = c;
            }
            Move::Turn(r, c, d) => {
                row = r;
                col = c;
                direction = d;
            }
        }
    }
    m
}

fn main() {
    let got3 = fill_spiral(3);
    assert_eq!(got3, vec![vec![1, 8, 7], vec![2, 9, 6], vec![3, 4, 5]], "spiral3");
    let got4 = fill_spiral(4);
    assert_eq!(got4, vec![vec![1, 12, 11, 10], vec![2, 13, 16, 9], vec![3, 14, 15, 8], vec![4, 5, 6, 7]], "spiral4");
    println!("PASS");
}
''',
"lua": '''-- @@BLOG@@
-- LeetCode 107737496. 代码重构_隔离变化 — Lua 版（方案7：螺旋矩阵分派表 place）
local function place(row, col, direction, n, m)
    local handlers = {
        D = function()
            if row + 1 <= n and m[row + 1][col] == 0 then return row + 1, col, nil end
            return row, col + 1, "R"
        end,
        R = function()
            if col + 1 <= n and m[row][col + 1] == 0 then return row, col + 1, nil end
            return row - 1, col, "U"
        end,
        U = function()
            if row - 1 >= 1 and m[row - 1][col] == 0 then return row - 1, col, nil end
            return row, col - 1, "L"
        end,
        L = function()
            if col - 1 >= 1 and m[row][col - 1] == 0 then return row, col - 1, nil end
            return row + 1, col, "D"
        end,
    }
    return handlers[direction]()
end

local function fill_spiral(n)
    local m = {}
    for i = 1, n do
        m[i] = {}
        for j = 1, n do m[i][j] = 0 end
    end
    local row, col = 1, 1
    local direction = "D"
    local num = 1
    while num <= n * n do
        m[row][col] = num
        num = num + 1
        local r, c, d = place(row, col, direction, n, m)
        row, col = r, c
        if d then direction = d end
    end
    return m
end

local function check(got, want, n, tag)
    for i = 1, n do
        for j = 1, n do
            assert(got[i][j] == want[i][j], tag)
        end
    end
end

check(fill_spiral(3), {{1, 8, 7}, {2, 9, 6}, {3, 4, 5}}, 3, "spiral3")
check(fill_spiral(4), {{1, 12, 11, 10}, {2, 13, 16, 9}, {3, 14, 15, 8}, {4, 5, 6, 7}}, 4, "spiral4")
print("PASS")
''',
"c": '''/* @@BLOG@@
 * LeetCode 107737496. 代码重构_隔离变化 — C 版（方案7：螺旋矩阵分派表 place）
 */
#include <stdio.h>
#include <string.h>

typedef struct {
    int row, col;
    char next_dir; /* 0 表示不变向 */
} Move;

static Move place(int row, int col, char direction, int n, const int m[][8]) {
    Move mv;
    switch (direction) {
        case 'D':
            if (row + 1 < n && m[row + 1][col] == 0) { mv.row = row + 1; mv.col = col; mv.next_dir = 0; }
            else { mv.row = row; mv.col = col + 1; mv.next_dir = 'R'; }
            break;
        case 'R':
            if (col + 1 < n && m[row][col + 1] == 0) { mv.row = row; mv.col = col + 1; mv.next_dir = 0; }
            else { mv.row = row - 1; mv.col = col; mv.next_dir = 'U'; }
            break;
        case 'U':
            if (row - 1 >= 0 && m[row - 1][col] == 0) { mv.row = row - 1; mv.col = col; mv.next_dir = 0; }
            else { mv.row = row; mv.col = col - 1; mv.next_dir = 'L'; }
            break;
        default:
            if (col - 1 >= 0 && m[row][col - 1] == 0) { mv.row = row; mv.col = col - 1; mv.next_dir = 0; }
            else { mv.row = row + 1; mv.col = col; mv.next_dir = 'D'; }
            break;
    }
    return mv;
}

static void fill_spiral(int n, int m[][8]) {
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++) m[i][j] = 0;
    int row = 0, col = 0;
    char direction = 'D';
    int num = 1;
    while (num <= n * n) {
        m[row][col] = num;
        num++;
        Move mv = place(row, col, direction, n, m);
        row = mv.row;
        col = mv.col;
        if (mv.next_dir) direction = mv.next_dir;
    }
}

int main(void) {
    int m[8][8];
    int want3[3][3] = {{1, 8, 7}, {2, 9, 6}, {3, 4, 5}};
    int want4[4][4] = {{1, 12, 11, 10}, {2, 13, 16, 9}, {3, 14, 15, 8}, {4, 5, 6, 7}};
    fill_spiral(3, m);
    for (int i = 0; i < 3; i++)
        for (int j = 0; j < 3; j++)
            if (m[i][j] != want3[i][j]) { printf("spiral3 failed\\n"); return 1; }
    fill_spiral(4, m);
    for (int i = 0; i < 4; i++)
        for (int j = 0; j < 4; j++)
            if (m[i][j] != want4[i][j]) { printf("spiral4 failed\\n"); return 1; }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''// @@BLOG@@
// LeetCode 107737496. 代码重构_隔离变化 — C++ 版（方案7：螺旋矩阵分派表 place）
#include <functional>
#include <iostream>
#include <map>
#include <vector>

static std::vector<int> place(int row, int col, char direction, int n,
                              const std::vector<std::vector<int>> &m) {
    // 返回 {row, col} 或 {row, col, direction}（长度 3 表示转向）
    std::map<char, std::function<std::vector<int>()>> handlers = {
        {'D', [&]() -> std::vector<int> {
             if (row + 1 < n && m[row + 1][col] == 0) return {row + 1, col};
             return {row, col + 1, 'R'};
         }},
        {'R', [&]() -> std::vector<int> {
             if (col + 1 < n && m[row][col + 1] == 0) return {row, col + 1};
             return {row - 1, col, 'U'};
         }},
        {'U', [&]() -> std::vector<int> {
             if (row - 1 >= 0 && m[row - 1][col] == 0) return {row - 1, col};
             return {row, col - 1, 'L'};
         }},
        {'L', [&]() -> std::vector<int> {
             if (col - 1 >= 0 && m[row][col - 1] == 0) return {row, col - 1};
             return {row + 1, col, 'D'};
         }},
    };
    return handlers[direction]();
}

static std::vector<std::vector<int>> fill_spiral(int n) {
    std::vector<std::vector<int>> m(n, std::vector<int>(n, 0));
    int row = 0, col = 0;
    char direction = 'D';
    int num = 1;
    while (num <= n * n) {
        m[row][col] = num;
        ++num;
        auto res = place(row, col, direction, n, m);
        row = res[0];
        col = res[1];
        if (res.size() == 3) direction = static_cast<char>(res[2]);
    }
    return m;
}

int main() {
    if (fill_spiral(3) != std::vector<std::vector<int>>({{1, 8, 7}, {2, 9, 6}, {3, 4, 5}})) {
        std::cout << "spiral3 failed" << std::endl;
        return 1;
    }
    if (fill_spiral(4) != std::vector<std::vector<int>>({{1, 12, 11, 10}, {2, 13, 16, 9}, {3, 14, 15, 8}, {4, 5, 6, 7}})) {
        std::cout << "spiral4 failed" << std::endl;
        return 1;
    }
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''# @@BLOG@@
# LeetCode 107737496. 代码重构_隔离变化 — R 版（方案7：螺旋矩阵分派表 place）
place_step <- function(row, col, direction, n, m) {
  handlers <- list(
    D = function() {
      if (row + 1L <= n && m[row + 1L, col] == 0L) return(list(row + 1L, col, NULL))
      list(row, col + 1L, "R")
    },
    R = function() {
      if (col + 1L <= n && m[row, col + 1L] == 0L) return(list(row, col + 1L, NULL))
      list(row - 1L, col, "U")
    },
    U = function() {
      if (row - 1L >= 1L && m[row - 1L, col] == 0L) return(list(row - 1L, col, NULL))
      list(row, col - 1L, "L")
    },
    L = function() {
      if (col - 1L >= 1L && m[row, col - 1L] == 0L) return(list(row, col - 1L, NULL))
      list(row + 1L, col, "D")
    }
  )
  handlers[[direction]]()
}

fill_spiral <- function(n) {
  m <- matrix(0L, nrow = n, ncol = n)
  row <- 1L; col <- 1L
  direction <- "D"
  num <- 1L
  while (num <= n * n) {
    m[row, col] <- num
    num <- num + 1L
    res <- place_step(row, col, direction, n, m)
    row <- res[[1]]
    col <- res[[2]]
    if (!is.null(res[[3]])) direction <- res[[3]]
  }
  m
}

got3 <- fill_spiral(3L)
want3 <- matrix(c(1, 8, 7, 2, 9, 6, 3, 4, 5), nrow = 3, byrow = TRUE)
stopifnot(identical(as.integer(got3), as.integer(want3)))
got4 <- fill_spiral(4L)
want4 <- matrix(c(1, 12, 11, 10, 2, 13, 16, 9, 3, 14, 15, 8, 4, 5, 6, 7), nrow = 4, byrow = TRUE)
stopifnot(identical(as.integer(got4), as.integer(want4)))
cat("PASS\\n")
''',
"zig": '''// @@BLOG@@
// LeetCode 107737496. 代码重构_隔离变化 — Zig 版（方案7：螺旋矩阵分派表 place）
const std = @import("std");

const Move = struct {
    row: usize,
    col: usize,
    next_dir: u8 = 0, // 0 表示不变向
};

fn place(row: usize, col: usize, direction: u8, n: usize, m: *const [8][8]i32) Move {
    return switch (direction) {
        'D' => if (row + 1 < n and m[row + 1][col] == 0)
            Move{ .row = row + 1, .col = col }
        else
            Move{ .row = row, .col = col + 1, .next_dir = 'R' },
        'R' => if (col + 1 < n and m[row][col + 1] == 0)
            Move{ .row = row, .col = col + 1 }
        else
            Move{ .row = row - 1, .col = col, .next_dir = 'U' },
        'U' => if (row >= 1 and m[row - 1][col] == 0)
            Move{ .row = row - 1, .col = col }
        else
            Move{ .row = row, .col = col - 1, .next_dir = 'L' },
        else => if (col >= 1 and m[row][col - 1] == 0)
            Move{ .row = row, .col = col - 1 }
        else
            Move{ .row = row + 1, .col = col, .next_dir = 'D' },
    };
}

fn fillSpiral(n: usize, m: *[8][8]i32) void {
    for (0..n) |i| {
        for (0..n) |j| m[i][j] = 0;
    }
    var row: usize = 0;
    var col: usize = 0;
    var direction: u8 = 'D';
    var num: i32 = 1;
    while (num <= @as(i32, @intCast(n * n))) {
        m[row][col] = num;
        num += 1;
        const mv = place(row, col, direction, n, m);
        row = mv.row;
        col = mv.col;
        if (mv.next_dir != 0) direction = mv.next_dir;
    }
}

pub fn main() !void {
    var m: [8][8]i32 = undefined;
    const want3 = [3][3]i32{ .{ 1, 8, 7 }, .{ 2, 9, 6 }, .{ 3, 4, 5 } };
    fillSpiral(3, &m);
    for (want3, 0..) |row, i| {
        for (row, 0..) |x, j| {
            if (m[i][j] != x) return error.TestFailed;
        }
    }
    const want4 = [4][4]i32{ .{ 1, 12, 11, 10 }, .{ 2, 13, 16, 9 }, .{ 3, 14, 15, 8 }, .{ 4, 5, 6, 7 } };
    fillSpiral(4, &m);
    for (want4, 0..) |row, i| {
        for (row, 0..) |x, j| {
            if (m[i][j] != x) return error.TestFailed;
        }
    }
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''// @@BLOG@@
// LeetCode 107737496. 代码重构_隔离变化 — Dart 版（方案7：螺旋矩阵分派表 place）
List<int> place(int row, int col, String direction, int n, List<List<int>> m) {
  final handlers = <String, List<int> Function()>{
    'D': () => (row + 1 < n && m[row + 1][col] == 0) ? [row + 1, col] : [row, col + 1, 'R'.codeUnitAt(0)],
    'R': () => (col + 1 < n && m[row][col + 1] == 0) ? [row, col + 1] : [row - 1, col, 'U'.codeUnitAt(0)],
    'U': () => (row - 1 >= 0 && m[row - 1][col] == 0) ? [row - 1, col] : [row, col - 1, 'L'.codeUnitAt(0)],
    'L': () => (col - 1 >= 0 && m[row][col - 1] == 0) ? [row, col - 1] : [row + 1, col, 'D'.codeUnitAt(0)],
  };
  return handlers[direction]!();
}

List<List<int>> fillSpiral(int n) {
  final m = List.generate(n, (_) => List<int>.filled(n, 0));
  var row = 0, col = 0;
  var direction = 'D';
  var num = 1;
  while (num <= n * n) {
    m[row][col] = num;
    num++;
    final res = place(row, col, direction, n, m);
    row = res[0];
    col = res[1];
    if (res.length == 3) direction = String.fromCharCode(res[2]);
  }
  return m;
}

void main() {
  if (fillSpiral(3).toString() != '[[1, 8, 7], [2, 9, 6], [3, 4, 5]]') throw StateError('spiral3 failed');
  if (fillSpiral(4).toString() != '[[1, 12, 11, 10], [2, 13, 16, 9], [3, 14, 15, 8], [4, 5, 6, 7]]') {
    throw StateError('spiral4 failed');
  }
  print('PASS');
}
''',
}

# ---------------- F: s8 Filler + hasNext（部分填充） ----------------
F = {
"rust": '''// @@BLOG@@
// LeetCode 107737496. 代码重构_隔离变化 — Rust 版（方案8：Filler 状态机 + hasNext 部分填充）
struct Filler {
    row_num: usize,
    col_num: usize,
    rule: String,
    pos: (usize, usize),
    idx: usize,
    r_min: usize,
    c_min: usize,
    r_max: usize,
    c_max: usize,
}

impl Filler {
    fn new(rn: usize, cn: usize) -> Self {
        Filler {
            row_num: rn,
            col_num: cn,
            rule: "ESVM".to_string(),
            pos: (0, 0),
            idx: 0,
            r_min: 0,
            c_min: 0,
            r_max: rn - 1,
            c_max: cn - 1,
        }
    }
    fn set_rule(&mut self, r: &str) {
        self.rule = r.to_string();
    }
    fn has_next(&self) -> bool {
        self.r_min <= self.pos.0
            && self.pos.0 <= self.r_max
            && self.c_min <= self.pos.1
            && self.pos.1 <= self.c_max
    }
    fn next(&mut self) -> (usize, usize) {
        let r = self.pos.0;
        let c = self.pos.1;
        self.advance();
        (r, c)
    }
    fn advance(&mut self) {
        let cmd = self.rule.as_bytes()[self.idx % 4] as char;
        if cmd == 'E' {
            self.pos.0 += 1;
            if self.pos.0 == self.r_max {
                self.idx += 1;
                self.c_min += 1;
            }
        } else if cmd == 'S' {
            self.pos.1 += 1;
            if self.pos.1 == self.c_max {
                self.idx += 1;
                self.r_max -= 1;
            }
        } else if cmd == 'V' {
            self.pos.0 -= 1;
            if self.pos.0 == self.r_min {
                self.idx += 1;
                self.c_max -= 1;
            }
        } else if cmd == 'M' {
            self.pos.1 -= 1;
            if self.pos.1 == self.c_min {
                self.idx += 1;
                self.r_min += 1;
            }
        }
    }
}

fn fill_matrix(rn: usize, cn: usize, rule: &str) -> Vec<Vec<i32>> {
    let mut mat = vec![vec![0i32; cn]; rn];
    let mut f = Filler::new(rn, cn);
    f.set_rule(rule);
    let mut i = 1i32;
    while f.has_next() {
        let (r, c) = f.next();
        mat[r][c] = i;
        i += 1;
    }
    mat
}

fn main() {
    let want1 = vec![
        vec![1, 0, 0, 0, 0, 0],
        vec![2, 0, 0, 0, 0, 0],
        vec![3, 0, 0, 0, 0, 0],
        vec![4, 0, 0, 0, 0, 0],
        vec![5, 0, 0, 0, 0, 0],
        vec![0, 0, 0, 0, 0, 0],
    ];
    assert_eq!(fill_matrix(6, 6, "ESVM"), want1, "case1");
    let want2 = vec![vec![1, 0, 0], vec![2, 0, 0], vec![0, 0, 0]];
    assert_eq!(fill_matrix(3, 3, "ESVM"), want2, "case2");
    println!("PASS");
}
''',
"lua": '''-- @@BLOG@@
-- LeetCode 107737496. 代码重构_隔离变化 — Lua 版（方案8：Filler 状态机 + hasNext 部分填充）
local Filler = {}
Filler.__index = Filler
function Filler.new(rn, cn)
    local f = setmetatable({ rowNum = rn, colNum = cn, rule = "ESVM" }, Filler)
    f:reset()
    return f
end
function Filler:reset()
    self.pos = { 0, 0 }   -- 0 基
    self.idx = 0
    self.rMin = 0
    self.cMin = 0
    self.rMax = self.rowNum - 1
    self.cMax = self.colNum - 1
end
function Filler:setRule(r) self.rule = r end
function Filler:hasNext()
    return self.rMin <= self.pos[1] and self.pos[1] <= self.rMax
        and self.cMin <= self.pos[2] and self.pos[2] <= self.cMax
end
function Filler:next()
    local r, c = self.pos[1], self.pos[2]
    self:_advance()
    return r, c
end
function Filler:_advance()
    local cmd = self.rule:sub(self.idx % 4 + 1, self.idx % 4 + 1)
    if cmd == "E" then
        self.pos[1] = self.pos[1] + 1
        if self.pos[1] == self.rMax then self.idx = self.idx + 1; self.cMin = self.cMin + 1 end
    elseif cmd == "S" then
        self.pos[2] = self.pos[2] + 1
        if self.pos[2] == self.cMax then self.idx = self.idx + 1; self.rMax = self.rMax - 1 end
    elseif cmd == "V" then
        self.pos[1] = self.pos[1] - 1
        if self.pos[1] == self.rMin then self.idx = self.idx + 1; self.cMax = self.cMax - 1 end
    elseif cmd == "M" then
        self.pos[2] = self.pos[2] - 1
        if self.pos[2] == self.cMin then self.idx = self.idx + 1; self.rMin = self.rMin + 1 end
    end
end

local function fill_matrix(rn, cn, rule)
    local mat = {}
    for i = 1, rn do
        mat[i] = {}
        for j = 1, cn do mat[i][j] = 0 end
    end
    local f = Filler.new(rn, cn)
    f:setRule(rule)
    local i = 1
    while f:hasNext() do
        local r, c = f:next()
        mat[r + 1][c + 1] = i
        i = i + 1
    end
    return mat
end

local got1 = fill_matrix(6, 6, "ESVM")
local want1 = {
    {1, 0, 0, 0, 0, 0},
    {2, 0, 0, 0, 0, 0},
    {3, 0, 0, 0, 0, 0},
    {4, 0, 0, 0, 0, 0},
    {5, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0},
}
for i = 1, 6 do for j = 1, 6 do assert(got1[i][j] == want1[i][j], "case1") end end
local got2 = fill_matrix(3, 3, "ESVM")
local want2 = {{1, 0, 0}, {2, 0, 0}, {0, 0, 0}}
for i = 1, 3 do for j = 1, 3 do assert(got2[i][j] == want2[i][j], "case2") end end
print("PASS")
''',
"c": '''/* @@BLOG@@
 * LeetCode 107737496. 代码重构_隔离变化 — C 版（方案8：Filler 状态机 + hasNext 部分填充）
 */
#include <stdio.h>
#include <string.h>

typedef struct {
    int row_num, col_num;
    char rule[8];
    int pos_row, pos_col;
    int idx;
    int r_min, c_min, r_max, c_max;
} Filler;

static void filler_init(Filler *f, int rn, int cn) {
    f->row_num = rn;
    f->col_num = cn;
    strcpy(f->rule, "ESVM");
    f->pos_row = 0;
    f->pos_col = 0;
    f->idx = 0;
    f->r_min = 0;
    f->c_min = 0;
    f->r_max = rn - 1;
    f->c_max = cn - 1;
}

static void filler_set_rule(Filler *f, const char *r) {
    strcpy(f->rule, r);
}

static int filler_has_next(const Filler *f) {
    return f->r_min <= f->pos_row && f->pos_row <= f->r_max &&
           f->c_min <= f->pos_col && f->pos_col <= f->c_max;
}

static void filler_next(Filler *f, int *out_r, int *out_c) {
    *out_r = f->pos_row;
    *out_c = f->pos_col;
    char cmd = f->rule[f->idx % 4];
    if (cmd == 'E') {
        f->pos_row += 1;
        if (f->pos_row == f->r_max) { f->idx += 1; f->c_min += 1; }
    } else if (cmd == 'S') {
        f->pos_col += 1;
        if (f->pos_col == f->c_max) { f->idx += 1; f->r_max -= 1; }
    } else if (cmd == 'V') {
        f->pos_row -= 1;
        if (f->pos_row == f->r_min) { f->idx += 1; f->c_max -= 1; }
    } else if (cmd == 'M') {
        f->pos_col -= 1;
        if (f->pos_col == f->c_min) { f->idx += 1; f->r_min += 1; }
    }
}

static void fill_matrix(int rn, int cn, const char *rule, int mat[][8]) {
    for (int i = 0; i < rn; i++)
        for (int j = 0; j < cn; j++) mat[i][j] = 0;
    Filler f;
    filler_init(&f, rn, cn);
    filler_set_rule(&f, rule);
    int i = 1, r, c;
    while (filler_has_next(&f)) {
        filler_next(&f, &r, &c);
        mat[r][c] = i;
        i++;
    }
}

int main(void) {
    int mat[8][8];
    int want1[6][6] = {
        {1, 0, 0, 0, 0, 0},
        {2, 0, 0, 0, 0, 0},
        {3, 0, 0, 0, 0, 0},
        {4, 0, 0, 0, 0, 0},
        {5, 0, 0, 0, 0, 0},
        {0, 0, 0, 0, 0, 0},
    };
    fill_matrix(6, 6, "ESVM", mat);
    for (int i = 0; i < 6; i++)
        for (int j = 0; j < 6; j++)
            if (mat[i][j] != want1[i][j]) { printf("case1 failed\\n"); return 1; }
    int want2[3][3] = {{1, 0, 0}, {2, 0, 0}, {0, 0, 0}};
    fill_matrix(3, 3, "ESVM", mat);
    for (int i = 0; i < 3; i++)
        for (int j = 0; j < 3; j++)
            if (mat[i][j] != want2[i][j]) { printf("case2 failed\\n"); return 1; }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''// @@BLOG@@
// LeetCode 107737496. 代码重构_隔离变化 — C++ 版（方案8：Filler 状态机 + hasNext 部分填充）
#include <iostream>
#include <string>
#include <vector>

class Filler {
public:
    Filler(int rn, int cn) : rowNum_(rn), colNum_(cn), rule_("ESVM") {
        reset();
    }
    void setRule(const std::string &r) { rule_ = r; }
    bool hasNext() const {
        return rMin_ <= posRow_ && posRow_ <= rMax_ &&
               cMin_ <= posCol_ && posCol_ <= cMax_;
    }
    std::pair<int, int> next() {
        int r = posRow_, c = posCol_;
        advance();
        return {r, c};
    }

private:
    void reset() {
        posRow_ = posCol_ = 0;
        idx_ = 0;
        rMin_ = cMin_ = 0;
        rMax_ = rowNum_ - 1;
        cMax_ = colNum_ - 1;
    }
    void advance() {
        char cmd = rule_[idx_ % 4];
        if (cmd == 'E') {
            ++posRow_;
            if (posRow_ == rMax_) { ++idx_; ++cMin_; }
        } else if (cmd == 'S') {
            ++posCol_;
            if (posCol_ == cMax_) { ++idx_; --rMax_; }
        } else if (cmd == 'V') {
            --posRow_;
            if (posRow_ == rMin_) { ++idx_; --cMax_; }
        } else if (cmd == 'M') {
            --posCol_;
            if (posCol_ == cMin_) { ++idx_; ++rMin_; }
        }
    }

    int rowNum_, colNum_;
    std::string rule_;
    int posRow_, posCol_, idx_;
    int rMin_, cMin_, rMax_, cMax_;
};

static std::vector<std::vector<int>> fillMatrix(int rn, int cn, const std::string &rule) {
    std::vector<std::vector<int>> mat(rn, std::vector<int>(cn, 0));
    Filler f(rn, cn);
    f.setRule(rule);
    int i = 1;
    while (f.hasNext()) {
        auto [r, c] = f.next();
        mat[r][c] = i;
        ++i;
    }
    return mat;
}

int main() {
    std::vector<std::vector<int>> want1 = {
        {1, 0, 0, 0, 0, 0},
        {2, 0, 0, 0, 0, 0},
        {3, 0, 0, 0, 0, 0},
        {4, 0, 0, 0, 0, 0},
        {5, 0, 0, 0, 0, 0},
        {0, 0, 0, 0, 0, 0},
    };
    if (fillMatrix(6, 6, "ESVM") != want1) { std::cout << "case1 failed" << std::endl; return 1; }
    std::vector<std::vector<int>> want2 = {{1, 0, 0}, {2, 0, 0}, {0, 0, 0}};
    if (fillMatrix(3, 3, "ESVM") != want2) { std::cout << "case2 failed" << std::endl; return 1; }
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''# @@BLOG@@
# LeetCode 107737496. 代码重构_隔离变化 — R 版（方案8：Filler 状态机 + hasNext 部分填充）
Filler <- function(rn, cn) {
  e <- new.env(parent = emptyenv())
  e$rowNum <- rn
  e$colNum <- cn
  e$rule <- "ESVM"
  e$pos <- c(0L, 0L)  # 0 基
  e$idx <- 0L
  e$rMin <- 0L
  e$cMin <- 0L
  e$rMax <- rn - 1L
  e$cMax <- cn - 1L
  class(e) <- "Filler"
  e
}

filler_set_rule <- function(f, r) f$rule <- r

filler_has_next <- function(f) {
  f$rMin <= f$pos[1] && f$pos[1] <= f$rMax &&
    f$cMin <= f$pos[2] && f$pos[2] <= f$cMax
}

filler_next <- function(f) {
  r <- f$pos[1]
  c <- f$pos[2]
  cmd <- substr(f$rule, f$idx %% 4L + 1L, f$idx %% 4L + 1L)
  if (cmd == "E") {
    f$pos[1] <- f$pos[1] + 1L
    if (f$pos[1] == f$rMax) { f$idx <- f$idx + 1L; f$cMin <- f$cMin + 1L }
  } else if (cmd == "S") {
    f$pos[2] <- f$pos[2] + 1L
    if (f$pos[2] == f$cMax) { f$idx <- f$idx + 1L; f$rMax <- f$rMax - 1L }
  } else if (cmd == "V") {
    f$pos[1] <- f$pos[1] - 1L
    if (f$pos[1] == f$rMin) { f$idx <- f$idx + 1L; f$cMax <- f$cMax - 1L }
  } else if (cmd == "M") {
    f$pos[2] <- f$pos[2] - 1L
    if (f$pos[2] == f$cMin) { f$idx <- f$idx + 1L; f$rMin <- f$rMin + 1L }
  }
  c(r, c)
}

fill_matrix <- function(rn, cn, rule) {
  mat <- matrix(0L, nrow = rn, ncol = cn)
  f <- Filler(rn, cn)
  filler_set_rule(f, rule)
  i <- 1L
  while (filler_has_next(f)) {
    rc <- filler_next(f)
    mat[rc[1] + 1L, rc[2] + 1L] <- i
    i <- i + 1L
  }
  mat
}

got1 <- fill_matrix(6L, 6L, "ESVM")
want1 <- matrix(c(1,0,0,0,0,0, 2,0,0,0,0,0, 3,0,0,0,0,0, 4,0,0,0,0,0, 5,0,0,0,0,0, 0,0,0,0,0,0), nrow = 6, byrow = TRUE)
stopifnot(identical(as.integer(got1), as.integer(want1)))
got2 <- fill_matrix(3L, 3L, "ESVM")
want2 <- matrix(c(1,0,0, 2,0,0, 0,0,0), nrow = 3, byrow = TRUE)
stopifnot(identical(as.integer(got2), as.integer(want2)))
cat("PASS\\n")
''',
"zig": '''// @@BLOG@@
// LeetCode 107737496. 代码重构_隔离变化 — Zig 版（方案8：Filler 状态机 + hasNext 部分填充）
const std = @import("std");

const Filler = struct {
    row_num: usize,
    col_num: usize,
    rule: [8]u8 = undefined,
    rule_len: usize = 0,
    pos_row: usize = 0,
    pos_col: usize = 0,
    idx: usize = 0,
    r_min: usize = 0,
    c_min: usize = 0,
    r_max: usize,
    c_max: usize,

    fn init(rn: usize, cn: usize) Filler {
        return .{ .row_num = rn, .col_num = cn, .r_max = rn - 1, .c_max = cn - 1 };
    }
    fn setRule(self: *Filler, r: []const u8) void {
        for (r, 0..) |ch, i| self.rule[i] = ch;
        self.rule_len = r.len;
    }
    fn hasNext(self: *const Filler) bool {
        return self.r_min <= self.pos_row and self.pos_row <= self.r_max and
            self.c_min <= self.pos_col and self.pos_col <= self.c_max;
    }
    fn next(self: *Filler) struct { r: usize, c: usize } {
        const r = self.pos_row;
        const c = self.pos_col;
        self.advance();
        return .{ .r = r, .c = c };
    }
    fn advance(self: *Filler) void {
        const cmd = self.rule[self.idx % 4];
        if (cmd == 'E') {
            self.pos_row += 1;
            if (self.pos_row == self.r_max) {
                self.idx += 1;
                self.c_min += 1;
            }
        } else if (cmd == 'S') {
            self.pos_col += 1;
            if (self.pos_col == self.c_max) {
                self.idx += 1;
                self.r_max -= 1;
            }
        } else if (cmd == 'V') {
            self.pos_row -= 1;
            if (self.pos_row == self.r_min) {
                self.idx += 1;
                self.c_max -= 1;
            }
        } else if (cmd == 'M') {
            self.pos_col -= 1;
            if (self.pos_col == self.c_min) {
                self.idx += 1;
                self.r_min += 1;
            }
        }
    }
};

fn fillMatrix(rn: usize, cn: usize, rule: []const u8, mat: *[8][8]i32) void {
    for (0..rn) |i| {
        for (0..cn) |j| mat[i][j] = 0;
    }
    var f = Filler.init(rn, cn);
    f.setRule(rule);
    var i: i32 = 1;
    while (f.hasNext()) {
        const rc = f.next();
        mat[rc.r][rc.c] = i;
        i += 1;
    }
}

pub fn main() !void {
    var mat: [8][8]i32 = undefined;
    const want1 = [6][6]i32{
        .{ 1, 0, 0, 0, 0, 0 },
        .{ 2, 0, 0, 0, 0, 0 },
        .{ 3, 0, 0, 0, 0, 0 },
        .{ 4, 0, 0, 0, 0, 0 },
        .{ 5, 0, 0, 0, 0, 0 },
        .{ 0, 0, 0, 0, 0, 0 },
    };
    fillMatrix(6, 6, "ESVM", &mat);
    for (want1, 0..) |row, i| {
        for (row, 0..) |x, j| {
            if (mat[i][j] != x) return error.TestFailed;
        }
    }
    const want2 = [3][3]i32{ .{ 1, 0, 0 }, .{ 2, 0, 0 }, .{ 0, 0, 0 } };
    fillMatrix(3, 3, "ESVM", &mat);
    for (want2, 0..) |row, i| {
        for (row, 0..) |x, j| {
            if (mat[i][j] != x) return error.TestFailed;
        }
    }
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''// @@BLOG@@
// LeetCode 107737496. 代码重构_隔离变化 — Dart 版（方案8：Filler 状态机 + hasNext 部分填充）
class Filler {
  int rowNum, colNum;
  String rule = 'ESVM';
  int posRow = 0, posCol = 0, idx = 0;
  int rMin = 0, cMin = 0, rMax = 0, cMax = 0;

  Filler(this.rowNum, this.colNum) {
    rMax = rowNum - 1;
    cMax = colNum - 1;
  }

  void setRule(String r) {
    rule = r;
  }

  bool hasNext() {
    return rMin <= posRow && posRow <= rMax && cMin <= posCol && posCol <= cMax;
  }

  List<int> next() {
    final r = posRow, c = posCol;
    _advance();
    return [r, c];
  }

  void _advance() {
    final cmd = rule[idx % 4];
    if (cmd == 'E') {
      posRow += 1;
      if (posRow == rMax) {
        idx += 1;
        cMin += 1;
      }
    } else if (cmd == 'S') {
      posCol += 1;
      if (posCol == cMax) {
        idx += 1;
        rMax -= 1;
      }
    } else if (cmd == 'V') {
      posRow -= 1;
      if (posRow == rMin) {
        idx += 1;
        cMax -= 1;
      }
    } else if (cmd == 'M') {
      posCol -= 1;
      if (posCol == cMin) {
        idx += 1;
        rMin += 1;
      }
    }
  }
}

List<List<int>> fillMatrix(int rn, int cn, String rule) {
  final mat = List.generate(rn, (_) => List<int>.filled(cn, 0));
  final f = Filler(rn, cn);
  f.setRule(rule);
  var i = 1;
  while (f.hasNext()) {
    final rc = f.next();
    mat[rc[0]][rc[1]] = i;
    i++;
  }
  return mat;
}

void main() {
  final want1 = <List<int>>[
    [1, 0, 0, 0, 0, 0],
    [2, 0, 0, 0, 0, 0],
    [3, 0, 0, 0, 0, 0],
    [4, 0, 0, 0, 0, 0],
    [5, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
  ];
  if (fillMatrix(6, 6, 'ESVM').toString() != want1.toString()) throw StateError('case1 failed');
  final want2 = <List<int>>[[1, 0, 0], [2, 0, 0], [0, 0, 0]];
  if (fillMatrix(3, 3, 'ESVM').toString() != want2.toString()) throw StateError('case2 failed');
  print('PASS');
}
''',
}

# ---------------- G: s9 规则串状态机（8 方向字母） ----------------
# 统一核心：next() 依据 rule[idx % rule.len] 分支，testFiller 输出序列
G_CORE = '''// @@BLOG@@
// LeetCode 107737496. 代码重构_隔离变化 — {LANG} 版（方案9：规则串状态机，8 方向字母）
'''

def g_test_cases():
    return {
        "ESVM": [[0,0],[1,0],[2,0],[3,0],[3,1],[3,2],[3,3],[2,3],[1,3],[0,3],[0,2],[0,1],[1,1],[2,1],[2,2],[1,2]],
        "semv": [[0,0],[0,1],[0,2],[0,3],[1,3],[2,3],[3,3],[3,2],[3,1],[3,0],[2,0],[1,0],[1,1],[1,2],[2,2],[2,1]],
    }

G = {
"rust": '''// @@BLOG@@
// LeetCode 107737496. 代码重构_隔离变化 — Rust 版（方案9：规则串状态机，8 方向字母）
struct Location {
    row: i32,
    col: i32,
}

struct Filler {
    row_num: i32,
    col_num: i32,
    pos: Location,
    idx: usize,
    r_min: i32,
    c_min: i32,
    r_max: i32,
    c_max: i32,
    rule: String,
}

impl Filler {
    fn new(rn: i32, cn: i32) -> Self {
        Filler {
            row_num: rn,
            col_num: cn,
            pos: Location { row: 0, col: 0 },
            idx: 0,
            r_min: 0,
            c_min: 0,
            r_max: rn - 1,
            c_max: cn - 1,
            rule: "ESVM".to_string(),
        }
    }
    fn set_rule(&mut self, rule: &str) {
        self.rule = rule.to_string();
    }
    fn next(&mut self) -> (i32, i32) {
        let res = (self.pos.row, self.pos.col);
        let ch = self.rule.as_bytes()[self.idx % self.rule.len()] as char;
        if ch == 'E' {
            self.pos.row += 1;
            if self.pos.row == self.r_max { self.idx += 1; self.c_min += 1; }
        } else if ch == 'S' {
            self.pos.col += 1;
            if self.pos.col == self.c_max { self.idx += 1; self.r_max -= 1; }
        } else if ch == 'V' {
            self.pos.row -= 1;
            if self.pos.row == self.r_min { self.idx += 1; self.c_max -= 1; }
        } else if ch == 'M' {
            self.pos.col -= 1;
            if self.pos.col == self.c_min { self.idx += 1; self.r_min += 1; }
        } else if ch == 'e' {
            self.pos.row += 1;
            if self.pos.row == self.r_max { self.idx += 1; self.c_max -= 1; }
        } else if ch == 's' {
            self.pos.col += 1;
            if self.pos.col == self.c_max { self.idx += 1; self.r_min += 1; }
        } else if ch == 'v' {
            self.pos.row -= 1;
            if self.pos.row == self.r_min { self.idx += 1; self.c_min += 1; }
        } else if ch == 'm' {
            self.pos.col -= 1;
            if self.pos.col == self.c_min { self.idx += 1; self.r_max -= 1; }
        }
        res
    }
}

fn test_filler(rule: &str, rn: i32, cn: i32) -> Vec<Vec<i32>> {
    let mut obj = Filler::new(rn, cn);
    obj.set_rule(rule);
    let mut seq: Vec<Vec<i32>> = vec![];
    for _ in 0..(rn * cn) {
        let (r, c) = obj.next();
        seq.push(vec![r, c]);
    }
    seq
}

fn main() {
    let want_esvm = vec![
        vec![0,0], vec![1,0], vec![2,0], vec![3,0], vec![3,1], vec![3,2], vec![3,3],
        vec![2,3], vec![1,3], vec![0,3], vec![0,2], vec![0,1], vec![1,1], vec![2,1], vec![2,2], vec![1,2],
    ];
    assert_eq!(test_filler("ESVM", 4, 4), want_esvm, "ESVM");
    let want_semv = vec![
        vec![0,0], vec![0,1], vec![0,2], vec![0,3], vec![1,3], vec![2,3], vec![3,3],
        vec![3,2], vec![3,1], vec![3,0], vec![2,0], vec![1,0], vec![1,1], vec![1,2], vec![2,2], vec![2,1],
    ];
    assert_eq!(test_filler("semv", 4, 4), want_semv, "semv");
    println!("PASS");
}
''',
"lua": '''-- @@BLOG@@
-- LeetCode 107737496. 代码重构_隔离变化 — Lua 版（方案9：规则串状态机，8 方向字母）
local Filler = {}
Filler.__index = Filler
function Filler.new(rn, cn)
    local f = setmetatable({ rowNum = rn, colNum = cn, rule = "ESVM" }, Filler)
    f.pos = { 0, 0 }
    f.idx = 0
    f.rMin = 0
    f.cMin = 0
    f.rMax = rn - 1
    f.cMax = cn - 1
    return f
end
function Filler:setRule(rule) self.rule = rule end
function Filler:next()
    local res = { self.pos[1], self.pos[2] }
    local ch = self.rule:sub(self.idx % #self.rule + 1, self.idx % #self.rule + 1)
    if ch == "E" then
        self.pos[1] = self.pos[1] + 1
        if self.pos[1] == self.rMax then self.idx = self.idx + 1; self.cMin = self.cMin + 1 end
    elseif ch == "S" then
        self.pos[2] = self.pos[2] + 1
        if self.pos[2] == self.cMax then self.idx = self.idx + 1; self.rMax = self.rMax - 1 end
    elseif ch == "V" then
        self.pos[1] = self.pos[1] - 1
        if self.pos[1] == self.rMin then self.idx = self.idx + 1; self.cMax = self.cMax - 1 end
    elseif ch == "M" then
        self.pos[2] = self.pos[2] - 1
        if self.pos[2] == self.cMin then self.idx = self.idx + 1; self.rMin = self.rMin + 1 end
    elseif ch == "e" then
        self.pos[1] = self.pos[1] + 1
        if self.pos[1] == self.rMax then self.idx = self.idx + 1; self.cMax = self.cMax - 1 end
    elseif ch == "s" then
        self.pos[2] = self.pos[2] + 1
        if self.pos[2] == self.cMax then self.idx = self.idx + 1; self.rMin = self.rMin + 1 end
    elseif ch == "v" then
        self.pos[1] = self.pos[1] - 1
        if self.pos[1] == self.rMin then self.idx = self.idx + 1; self.cMin = self.cMin + 1 end
    elseif ch == "m" then
        self.pos[2] = self.pos[2] - 1
        if self.pos[2] == self.cMin then self.idx = self.idx + 1; self.rMax = self.rMax - 1 end
    end
    return res[1], res[2]
end

local function test_filler(rule, rn, cn)
    local obj = Filler.new(rn, cn)
    obj:setRule(rule)
    local seq = {}
    for _ = 1, rn * cn do
        local r, c = obj:next()
        seq[#seq + 1] = { r, c }
    end
    return seq
end

local function check_seq(got, want, tag)
    assert(#got == #want, tag .. " length")
    for i = 1, #want do
        assert(got[i][1] == want[i][1] and got[i][2] == want[i][2], tag .. " at " .. i)
    end
end

check_seq(test_filler("ESVM", 4, 4), {{0,0},{1,0},{2,0},{3,0},{3,1},{3,2},{3,3},{2,3},{1,3},{0,3},{0,2},{0,1},{1,1},{2,1},{2,2},{1,2}}, "ESVM")
check_seq(test_filler("semv", 4, 4), {{0,0},{0,1},{0,2},{0,3},{1,3},{2,3},{3,3},{3,2},{3,1},{3,0},{2,0},{1,0},{1,1},{1,2},{2,2},{2,1}}, "semv")
print("PASS")
''',
"c": '''/* @@BLOG@@
 * LeetCode 107737496. 代码重构_隔离变化 — C 版（方案9：规则串状态机，8 方向字母）
 */
#include <stdio.h>
#include <string.h>

typedef struct {
    int row_num, col_num;
    int pos_row, pos_col, idx;
    int r_min, c_min, r_max, c_max;
    char rule[8];
} Filler;

static void filler_init(Filler *f, int rn, int cn) {
    f->row_num = rn; f->col_num = cn;
    f->pos_row = f->pos_col = f->idx = 0;
    f->r_min = f->c_min = 0;
    f->r_max = rn - 1;
    f->c_max = cn - 1;
    strcpy(f->rule, "ESVM");
}

static void filler_set_rule(Filler *f, const char *rule) {
    strcpy(f->rule, rule);
}

static void filler_next(Filler *f, int *out_r, int *out_c) {
    *out_r = f->pos_row;
    *out_c = f->pos_col;
    char ch = f->rule[f->idx % strlen(f->rule)];
    if (ch == 'E') {
        f->pos_row++;
        if (f->pos_row == f->r_max) { f->idx++; f->c_min++; }
    } else if (ch == 'S') {
        f->pos_col++;
        if (f->pos_col == f->c_max) { f->idx++; f->r_max--; }
    } else if (ch == 'V') {
        f->pos_row--;
        if (f->pos_row == f->r_min) { f->idx++; f->c_max--; }
    } else if (ch == 'M') {
        f->pos_col--;
        if (f->pos_col == f->c_min) { f->idx++; f->r_min++; }
    } else if (ch == 'e') {
        f->pos_row++;
        if (f->pos_row == f->r_max) { f->idx++; f->c_max--; }
    } else if (ch == 's') {
        f->pos_col++;
        if (f->pos_col == f->c_max) { f->idx++; f->r_min++; }
    } else if (ch == 'v') {
        f->pos_row--;
        if (f->pos_row == f->r_min) { f->idx++; f->c_min++; }
    } else if (ch == 'm') {
        f->pos_col--;
        if (f->pos_col == f->c_min) { f->idx++; f->r_max--; }
    }
}

static void test_filler(const char *rule, int rn, int cn, int seq[][2]) {
    Filler f;
    filler_init(&f, rn, cn);
    filler_set_rule(&f, rule);
    for (int i = 0; i < rn * cn; i++) {
        int r, c;
        filler_next(&f, &r, &c);
        seq[i][0] = r;
        seq[i][1] = c;
    }
}

int main(void) {
    int seq[16][2];
    int want_esvm[16][2] = {
        {0,0},{1,0},{2,0},{3,0},{3,1},{3,2},{3,3},{2,3},
        {1,3},{0,3},{0,2},{0,1},{1,1},{2,1},{2,2},{1,2},
    };
    test_filler("ESVM", 4, 4, seq);
    for (int i = 0; i < 16; i++)
        if (seq[i][0] != want_esvm[i][0] || seq[i][1] != want_esvm[i][1]) { printf("ESVM failed\\n"); return 1; }
    int want_semv[16][2] = {
        {0,0},{0,1},{0,2},{0,3},{1,3},{2,3},{3,3},{3,2},
        {3,1},{3,0},{2,0},{1,0},{1,1},{1,2},{2,2},{2,1},
    };
    test_filler("semv", 4, 4, seq);
    for (int i = 0; i < 16; i++)
        if (seq[i][0] != want_semv[i][0] || seq[i][1] != want_semv[i][1]) { printf("semv failed\\n"); return 1; }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''// @@BLOG@@
// LeetCode 107737496. 代码重构_隔离变化 — C++ 版（方案9：规则串状态机，8 方向字母）
#include <iostream>
#include <string>
#include <vector>

struct Location {
    int row = 0, col = 0;
};

class Filler {
public:
    Filler(int rn, int cn) : rowNum_(rn), colNum_(cn), rMax_(rn - 1), cMax_(cn - 1) {}
    void setRule(const std::string &rule) { rule_ = rule; }
    std::pair<int, int> next() {
        std::pair<int, int> res{pos_.row, pos_.col};
        char ch = rule_[idx_ % rule_.size()];
        if (ch == 'E') {
            ++pos_.row;
            if (pos_.row == rMax_) { ++idx_; ++cMin_; }
        } else if (ch == 'S') {
            ++pos_.col;
            if (pos_.col == cMax_) { ++idx_; --rMax_; }
        } else if (ch == 'V') {
            --pos_.row;
            if (pos_.row == rMin_) { ++idx_; --cMax_; }
        } else if (ch == 'M') {
            --pos_.col;
            if (pos_.col == cMin_) { ++idx_; ++rMin_; }
        } else if (ch == 'e') {
            ++pos_.row;
            if (pos_.row == rMax_) { ++idx_; --cMax_; }
        } else if (ch == 's') {
            ++pos_.col;
            if (pos_.col == cMax_) { ++idx_; ++rMin_; }
        } else if (ch == 'v') {
            --pos_.row;
            if (pos_.row == rMin_) { ++idx_; ++cMin_; }
        } else if (ch == 'm') {
            --pos_.col;
            if (pos_.col == cMin_) { ++idx_; --rMax_; }
        }
        return res;
    }

private:
    int rowNum_, colNum_;
    Location pos_;
    size_t idx_ = 0;
    int rMin_ = 0, cMin_ = 0, rMax_, cMax_;
    std::string rule_ = "ESVM";
};

static std::vector<std::vector<int>> test_filler(const std::string &rule, int rn, int cn) {
    Filler obj(rn, cn);
    obj.setRule(rule);
    std::vector<std::vector<int>> seq;
    for (int i = 0; i < rn * cn; ++i) {
        auto [r, c] = obj.next();
        seq.push_back({r, c});
    }
    return seq;
}

int main() {
    std::vector<std::vector<int>> want_esvm = {
        {0,0},{1,0},{2,0},{3,0},{3,1},{3,2},{3,3},{2,3},
        {1,3},{0,3},{0,2},{0,1},{1,1},{2,1},{2,2},{1,2},
    };
    if (test_filler("ESVM", 4, 4) != want_esvm) { std::cout << "ESVM failed" << std::endl; return 1; }
    std::vector<std::vector<int>> want_semv = {
        {0,0},{0,1},{0,2},{0,3},{1,3},{2,3},{3,3},{3,2},
        {3,1},{3,0},{2,0},{1,0},{1,1},{1,2},{2,2},{2,1},
    };
    if (test_filler("semv", 4, 4) != want_semv) { std::cout << "semv failed" << std::endl; return 1; }
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''# @@BLOG@@
# LeetCode 107737496. 代码重构_隔离变化 — R 版（方案9：规则串状态机，8 方向字母）
Filler <- function(rn, cn) {
  e <- new.env(parent = emptyenv())
  e$rowNum <- rn
  e$colNum <- cn
  e$pos <- c(0L, 0L)
  e$idx <- 0L
  e$rMin <- 0L
  e$cMin <- 0L
  e$rMax <- rn - 1L
  e$cMax <- cn - 1L
  e$rule <- "ESVM"
  class(e) <- "Filler"
  e
}

filler_set_rule <- function(f, rule) f$rule <- rule

filler_next <- function(f) {
  res <- c(f$pos[1], f$pos[2])
  ch <- substr(f$rule, f$idx %% nchar(f$rule) + 1L, f$idx %% nchar(f$rule) + 1L)
  if (ch == "E") {
    f$pos[1] <- f$pos[1] + 1L
    if (f$pos[1] == f$rMax) { f$idx <- f$idx + 1L; f$cMin <- f$cMin + 1L }
  } else if (ch == "S") {
    f$pos[2] <- f$pos[2] + 1L
    if (f$pos[2] == f$cMax) { f$idx <- f$idx + 1L; f$rMax <- f$rMax - 1L }
  } else if (ch == "V") {
    f$pos[1] <- f$pos[1] - 1L
    if (f$pos[1] == f$rMin) { f$idx <- f$idx + 1L; f$cMax <- f$cMax - 1L }
  } else if (ch == "M") {
    f$pos[2] <- f$pos[2] - 1L
    if (f$pos[2] == f$cMin) { f$idx <- f$idx + 1L; f$rMin <- f$rMin + 1L }
  } else if (ch == "e") {
    f$pos[1] <- f$pos[1] + 1L
    if (f$pos[1] == f$rMax) { f$idx <- f$idx + 1L; f$cMax <- f$cMax - 1L }
  } else if (ch == "s") {
    f$pos[2] <- f$pos[2] + 1L
    if (f$pos[2] == f$cMax) { f$idx <- f$idx + 1L; f$rMin <- f$rMin + 1L }
  } else if (ch == "v") {
    f$pos[1] <- f$pos[1] - 1L
    if (f$pos[1] == f$rMin) { f$idx <- f$idx + 1L; f$cMin <- f$cMin + 1L }
  } else if (ch == "m") {
    f$pos[2] <- f$pos[2] - 1L
    if (f$pos[2] == f$cMin) { f$idx <- f$idx + 1L; f$rMax <- f$rMax - 1L }
  }
  res
}

test_filler <- function(rule, rn, cn) {
  obj <- Filler(rn, cn)
  filler_set_rule(obj, rule)
  seq <- list()
  for (i in 1:(rn * cn)) {
    rc <- filler_next(obj)
    seq[[i]] <- as.integer(rc)
  }
  seq
}

want_esvm <- list(c(0,0), c(1,0), c(2,0), c(3,0), c(3,1), c(3,2), c(3,3), c(2,3),
                   c(1,3), c(0,3), c(0,2), c(0,1), c(1,1), c(2,1), c(2,2), c(1,2))
got <- test_filler("ESVM", 4L, 4L)
for (i in 1:16) stopifnot(identical(got[[i]], as.integer(want_esvm[[i]])))
want_semv <- list(c(0,0), c(0,1), c(0,2), c(0,3), c(1,3), c(2,3), c(3,3), c(3,2),
                   c(3,1), c(3,0), c(2,0), c(1,0), c(1,1), c(1,2), c(2,2), c(2,1))
got <- test_filler("semv", 4L, 4L)
for (i in 1:16) stopifnot(identical(got[[i]], as.integer(want_semv[[i]])))
cat("PASS\\n")
''',
"zig": '''// @@BLOG@@
// LeetCode 107737496. 代码重构_隔离变化 — Zig 版（方案9：规则串状态机，8 方向字母）
const std = @import("std");

const RC = struct { r: i32, c: i32 };

const Filler = struct {
    row_num: i32,
    col_num: i32,
    pos_row: i32 = 0,
    pos_col: i32 = 0,
    idx: usize = 0,
    r_min: i32 = 0,
    c_min: i32 = 0,
    r_max: i32,
    c_max: i32,
    rule: []const u8 = "ESVM",

    fn init(rn: i32, cn: i32) Filler {
        return .{ .row_num = rn, .col_num = cn, .r_max = rn - 1, .c_max = cn - 1 };
    }
    fn setRule(self: *Filler, rule: []const u8) void {
        self.rule = rule;
    }
    fn next(self: *Filler) RC {
        const res = RC{ .r = self.pos_row, .c = self.pos_col };
        const ch = self.rule[self.idx % self.rule.len];
        if (ch == 'E') {
            self.pos_row += 1;
            if (self.pos_row == self.r_max) {
                self.idx += 1;
                self.c_min += 1;
            }
        } else if (ch == 'S') {
            self.pos_col += 1;
            if (self.pos_col == self.c_max) {
                self.idx += 1;
                self.r_max -= 1;
            }
        } else if (ch == 'V') {
            self.pos_row -= 1;
            if (self.pos_row == self.r_min) {
                self.idx += 1;
                self.c_max -= 1;
            }
        } else if (ch == 'M') {
            self.pos_col -= 1;
            if (self.pos_col == self.c_min) {
                self.idx += 1;
                self.r_min += 1;
            }
        } else if (ch == 'e') {
            self.pos_row += 1;
            if (self.pos_row == self.r_max) {
                self.idx += 1;
                self.c_max -= 1;
            }
        } else if (ch == 's') {
            self.pos_col += 1;
            if (self.pos_col == self.c_max) {
                self.idx += 1;
                self.r_min += 1;
            }
        } else if (ch == 'v') {
            self.pos_row -= 1;
            if (self.pos_row == self.r_min) {
                self.idx += 1;
                self.c_min += 1;
            }
        } else if (ch == 'm') {
            self.pos_col -= 1;
            if (self.pos_col == self.c_min) {
                self.idx += 1;
                self.r_max -= 1;
            }
        }
        return res;
    }
};

fn testFiller(rule: []const u8, rn: i32, cn: i32, seq: *[16][2]i32) void {
    var obj = Filler.init(rn, cn);
    obj.setRule(rule);
    for (0..@intCast(rn * cn)) |i| {
        const rc = obj.next();
        seq[i][0] = rc.r;
        seq[i][1] = rc.c;
    }
}

pub fn main() !void {
    var seq: [16][2]i32 = undefined;
    const want_esvm = [16][2]i32{
        .{ 0, 0 }, .{ 1, 0 }, .{ 2, 0 }, .{ 3, 0 }, .{ 3, 1 }, .{ 3, 2 }, .{ 3, 3 }, .{ 2, 3 },
        .{ 1, 3 }, .{ 0, 3 }, .{ 0, 2 }, .{ 0, 1 }, .{ 1, 1 }, .{ 2, 1 }, .{ 2, 2 }, .{ 1, 2 },
    };
    testFiller("ESVM", 4, 4, &seq);
    for (want_esvm, 0..) |w, i| {
        if (seq[i][0] != w[0] or seq[i][1] != w[1]) return error.TestFailed;
    }
    const want_semv = [16][2]i32{
        .{ 0, 0 }, .{ 0, 1 }, .{ 0, 2 }, .{ 0, 3 }, .{ 1, 3 }, .{ 2, 3 }, .{ 3, 3 }, .{ 3, 2 },
        .{ 3, 1 }, .{ 3, 0 }, .{ 2, 0 }, .{ 1, 0 }, .{ 1, 1 }, .{ 1, 2 }, .{ 2, 2 }, .{ 2, 1 },
    };
    testFiller("semv", 4, 4, &seq);
    for (want_semv, 0..) |w, i| {
        if (seq[i][0] != w[0] or seq[i][1] != w[1]) return error.TestFailed;
    }
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''// @@BLOG@@
// LeetCode 107737496. 代码重构_隔离变化 — Dart 版（方案9：规则串状态机，8 方向字母）
class Location {
  int row = 0, col = 0;
}

class Filler {
  int rowNum, colNum;
  Location pos = Location();
  int idx = 0;
  int rMin = 0, cMin = 0, rMax = 0, cMax = 0;
  String rule = 'ESVM';

  Filler(this.rowNum, this.colNum) {
    rMax = rowNum - 1;
    cMax = colNum - 1;
  }

  void setRule(String rule) {
    rule = rule;
  }

  List<int> next() {
    final res = [pos.row, pos.col];
    final ch = rule[idx % rule.length];
    if (ch == 'E') {
      pos.row += 1;
      if (pos.row == rMax) {
        idx += 1;
        cMin += 1;
      }
    } else if (ch == 'S') {
      pos.col += 1;
      if (pos.col == cMax) {
        idx += 1;
        rMax -= 1;
      }
    } else if (ch == 'V') {
      pos.row -= 1;
      if (pos.row == rMin) {
        idx += 1;
        cMax -= 1;
      }
    } else if (ch == 'M') {
      pos.col -= 1;
      if (pos.col == cMin) {
        idx += 1;
        rMin += 1;
      }
    } else if (ch == 'e') {
      pos.row += 1;
      if (pos.row == rMax) {
        idx += 1;
        cMax -= 1;
      }
    } else if (ch == 's') {
      pos.col += 1;
      if (pos.col == cMax) {
        idx += 1;
        rMin += 1;
      }
    } else if (ch == 'v') {
      pos.row -= 1;
      if (pos.row == rMin) {
        idx += 1;
        cMin += 1;
      }
    } else if (ch == 'm') {
      pos.col -= 1;
      if (pos.col == cMin) {
        idx += 1;
        rMax -= 1;
      }
    }
    return res;
  }
}

List<List<int>> testFiller(String rule, int rn, int cn) {
  final obj = Filler(rn, cn);
  obj.rule = rule; // setRule（注意 Dart 里 this.rule = rule 需要显式 this）
  final seq = <List<int>>[];
  for (var i = 0; i < rn * cn; i++) {
    seq.add(obj.next());
  }
  return seq;
}

void main() {
  final wantEsvm = <List<int>>[
    [0, 0], [1, 0], [2, 0], [3, 0], [3, 1], [3, 2], [3, 3], [2, 3],
    [1, 3], [0, 3], [0, 2], [0, 1], [1, 1], [2, 1], [2, 2], [1, 2],
  ];
  if (testFiller('ESVM', 4, 4).toString() != wantEsvm.toString()) throw StateError('ESVM failed');
  final wantSemv = <List<int>>[
    [0, 0], [0, 1], [0, 2], [0, 3], [1, 3], [2, 3], [3, 3], [3, 2],
    [3, 1], [3, 0], [2, 0], [1, 0], [1, 1], [1, 2], [2, 2], [2, 1],
  ];
  if (testFiller('semv', 4, 4).toString() != wantSemv.toString()) throw StateError('semv failed');
  print('PASS');
}
''',
}

# ---------------- H: s10 9x9 全螺旋（Filler + Matrix + fmtRow） ----------------
H = {
"rust": '''// @@BLOG@@
// LeetCode 107737496. 代码重构_隔离变化 — Rust 版（方案10：Filler+Matrix 组合 9x9 全螺旋）
struct Filler {
    pos_row: usize,
    pos_col: usize,
    idx: usize,
    r_min: usize,
    c_min: usize,
    r_max: usize,
    c_max: usize,
}

impl Filler {
    fn new(rn: usize, cn: usize) -> Self {
        Filler { pos_row: 0, pos_col: 0, idx: 0, r_min: 0, c_min: 0, r_max: rn - 1, c_max: cn - 1 }
    }
    fn next(&mut self) -> (usize, usize) {
        let res = (self.pos_row, self.pos_col);
        let cmd = "ESVM".as_bytes()[self.idx % 4] as char;
        if cmd == 'E' {
            self.pos_row += 1;
            if self.pos_row == self.r_max { self.idx += 1; self.c_min += 1; }
        } else if cmd == 'S' {
            self.pos_col += 1;
            if self.pos_col == self.c_max { self.idx += 1; self.r_max -= 1; }
        } else if cmd == 'V' {
            self.pos_row -= 1;
            if self.pos_row == self.r_min { self.idx += 1; self.c_max -= 1; }
        } else if cmd == 'M' {
            self.pos_col -= 1;
            if self.pos_col == self.c_min { self.idx += 1; self.r_min += 1; }
        }
        res
    }
}

fn fmt_row(row: &[i32]) -> String {
    row.iter().map(|x| format!("{:2}", x)).collect::<Vec<_>>().join(" ")
}

fn main() {
    let (rn, cn) = (9usize, 9usize);
    let mut obj = Filler::new(rn, cn);
    let mut m = vec![vec![0i32; cn]; rn];
    for i in 0..rn * cn {
        let (r, c) = obj.next();
        m[r][c] = (i + 1) as i32;
    }
    let want = [
        " 1 32 31 30 29 28 27 26 25",
        " 2 33 56 55 54 53 52 51 24",
        " 3 34 57 72 71 70 69 50 23",
        " 4 35 58 73 80 79 68 49 22",
        " 5 36 59 74 81 78 67 48 21",
        " 6 37 60 75 76 77 66 47 20",
        " 7 38 61 62 63 64 65 46 19",
        " 8 39 40 41 42 43 44 45 18",
        " 9 10 11 12 13 14 15 16 17",
    ];
    for i in 0..rn {
        let got = fmt_row(&m[i]);
        assert_eq!(got, want[i], "matrix9 row {}", i);
    }
    println!("PASS");
}
''',
"lua": '''-- @@BLOG@@
-- LeetCode 107737496. 代码重构_隔离变化 — Lua 版（方案10：Filler+Matrix 组合 9x9 全螺旋）
local Filler = {}
Filler.__index = Filler
function Filler.new(rn, cn)
    local f = setmetatable({}, Filler)
    f.pos = { 0, 0 }
    f.idx = 0
    f.rMin = 0
    f.cMin = 0
    f.rMax = rn - 1
    f.cMax = cn - 1
    return f
end
local RULE = "ESVM"

function Filler:next()
    local r, c = self.pos[1], self.pos[2]
    local cmd = RULE:sub(self.idx % 4 + 1, self.idx % 4 + 1)
    if cmd == "E" then
        self.pos[1] = self.pos[1] + 1
        if self.pos[1] == self.rMax then self.idx = self.idx + 1; self.cMin = self.cMin + 1 end
    elseif cmd == "S" then
        self.pos[2] = self.pos[2] + 1
        if self.pos[2] == self.cMax then self.idx = self.idx + 1; self.rMax = self.rMax - 1 end
    elseif cmd == "V" then
        self.pos[1] = self.pos[1] - 1
        if self.pos[1] == self.rMin then self.idx = self.idx + 1; self.cMax = self.cMax - 1 end
    elseif cmd == "M" then
        self.pos[2] = self.pos[2] - 1
        if self.pos[2] == self.cMin then self.idx = self.idx + 1; self.rMin = self.rMin + 1 end
    end
    return r, c
end

local function fmt_row(row)
    local parts = {}
    for i, x in ipairs(row) do parts[i] = string.format("%2d", x) end
    return table.concat(parts, " ")
end

local rn, cn = 9, 9
local obj = Filler.new(rn, cn)
local m = {}
for i = 1, rn do
    m[i] = {}
    for j = 1, cn do m[i][j] = 0 end
end
for i = 1, rn * cn do
    local r, c = obj:next()
    m[r + 1][c + 1] = i
end
local want = {
    " 1 32 31 30 29 28 27 26 25",
    " 2 33 56 55 54 53 52 51 24",
    " 3 34 57 72 71 70 69 50 23",
    " 4 35 58 73 80 79 68 49 22",
    " 5 36 59 74 81 78 67 48 21",
    " 6 37 60 75 76 77 66 47 20",
    " 7 38 61 62 63 64 65 46 19",
    " 8 39 40 41 42 43 44 45 18",
    " 9 10 11 12 13 14 15 16 17",
}
for i = 1, rn do
    local got = fmt_row(m[i])
    assert(got == want[i], "matrix9 row " .. i)
end
print("PASS")
''',
"c": '''/* @@BLOG@@
 * LeetCode 107737496. 代码重构_隔离变化 — C 版（方案10：Filler+Matrix 组合 9x9 全螺旋）
 */
#include <stdio.h>
#include <string.h>

typedef struct {
    int pos_row, pos_col, idx;
    int r_min, c_min, r_max, c_max;
} Filler;

static void filler_init(Filler *f, int rn, int cn) {
    f->pos_row = f->pos_col = f->idx = 0;
    f->r_min = f->c_min = 0;
    f->r_max = rn - 1;
    f->c_max = cn - 1;
}

static void filler_next(Filler *f, int *out_r, int *out_c) {
    *out_r = f->pos_row;
    *out_c = f->pos_col;
    const char *rule = "ESVM";
    char cmd = rule[f->idx % 4];
    if (cmd == 'E') {
        f->pos_row++;
        if (f->pos_row == f->r_max) { f->idx++; f->c_min++; }
    } else if (cmd == 'S') {
        f->pos_col++;
        if (f->pos_col == f->c_max) { f->idx++; f->r_max--; }
    } else if (cmd == 'V') {
        f->pos_row--;
        if (f->pos_row == f->r_min) { f->idx++; f->c_max--; }
    } else if (cmd == 'M') {
        f->pos_col--;
        if (f->pos_col == f->c_min) { f->idx++; f->r_min++; }
    }
}

static void fmt_row(const int *row, int n, char *out) {
    out[0] = 0;
    char cell[8];
    for (int i = 0; i < n; i++) {
        snprintf(cell, sizeof(cell), "%2d", row[i]);
        if (i) strcat(out, " ");
        strcat(out, cell);
    }
}

int main(void) {
    const int rn = 9, cn = 9;
    Filler obj;
    filler_init(&obj, rn, cn);
    int m[9][9];
    memset(m, 0, sizeof(m));
    for (int i = 0; i < rn * cn; i++) {
        int r, c;
        filler_next(&obj, &r, &c);
        m[r][c] = i + 1;
    }
    const char *want[9] = {
        " 1 32 31 30 29 28 27 26 25",
        " 2 33 56 55 54 53 52 51 24",
        " 3 34 57 72 71 70 69 50 23",
        " 4 35 58 73 80 79 68 49 22",
        " 5 36 59 74 81 78 67 48 21",
        " 6 37 60 75 76 77 66 47 20",
        " 7 38 61 62 63 64 65 46 19",
        " 8 39 40 41 42 43 44 45 18",
        " 9 10 11 12 13 14 15 16 17",
    };
    for (int i = 0; i < rn; i++) {
        char got[64];
        fmt_row(m[i], cn, got);
        if (strcmp(got, want[i]) != 0) {
            printf("matrix9 row %d failed: got [%s]\\n", i, got);
            return 1;
        }
    }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''// @@BLOG@@
// LeetCode 107737496. 代码重构_隔离变化 — C++ 版（方案10：Filler+Matrix 组合 9x9 全螺旋）
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

class Filler {
public:
    Filler(int rn, int cn) : rMax_(rn - 1), cMax_(cn - 1) {}
    std::pair<int, int> next() {
        std::pair<int, int> res{posRow_, posCol_};
        const std::string rule = "ESVM";
        char cmd = rule[idx_ % 4];
        if (cmd == 'E') {
            ++posRow_;
            if (posRow_ == rMax_) { ++idx_; ++cMin_; }
        } else if (cmd == 'S') {
            ++posCol_;
            if (posCol_ == cMax_) { ++idx_; --rMax_; }
        } else if (cmd == 'V') {
            --posRow_;
            if (posRow_ == rMin_) { ++idx_; --cMax_; }
        } else if (cmd == 'M') {
            --posCol_;
            if (posCol_ == cMin_) { ++idx_; ++rMin_; }
        }
        return res;
    }

private:
    int posRow_ = 0, posCol_ = 0, idx_ = 0;
    int rMin_ = 0, cMin_ = 0, rMax_, cMax_;
};

static std::string fmt_row(const std::vector<int> &row) {
    std::ostringstream oss;
    for (size_t i = 0; i < row.size(); ++i) {
        if (i) oss << " ";
        oss.width(2);
        oss << row[i];
    }
    return oss.str();
}

int main() {
    const int rn = 9, cn = 9;
    Filler obj(rn, cn);
    std::vector<std::vector<int>> m(rn, std::vector<int>(cn, 0));
    for (int i = 0; i < rn * cn; ++i) {
        auto [r, c] = obj.next();
        m[r][c] = i + 1;
    }
    const char *want[9] = {
        " 1 32 31 30 29 28 27 26 25",
        " 2 33 56 55 54 53 52 51 24",
        " 3 34 57 72 71 70 69 50 23",
        " 4 35 58 73 80 79 68 49 22",
        " 5 36 59 74 81 78 67 48 21",
        " 6 37 60 75 76 77 66 47 20",
        " 7 38 61 62 63 64 65 46 19",
        " 8 39 40 41 42 43 44 45 18",
        " 9 10 11 12 13 14 15 16 17",
    };
    for (int i = 0; i < rn; ++i) {
        if (fmt_row(m[i]) != want[i]) { std::cout << "matrix9 row " << i << " failed" << std::endl; return 1; }
    }
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''# @@BLOG@@
# LeetCode 107737496. 代码重构_隔离变化 — R 版（方案10：Filler+Matrix 组合 9x9 全螺旋）
Filler <- function(rn, cn) {
  e <- new.env(parent = emptyenv())
  e$pos <- c(0L, 0L)
  e$idx <- 0L
  e$rMin <- 0L
  e$cMin <- 0L
  e$rMax <- rn - 1L
  e$cMax <- cn - 1L
  class(e) <- "Filler"
  e
}

filler_next <- function(f) {
  res <- c(f$pos[1], f$pos[2])
  cmd <- substr("ESVM", f$idx %% 4L + 1L, f$idx %% 4L + 1L)
  if (cmd == "E") {
    f$pos[1] <- f$pos[1] + 1L
    if (f$pos[1] == f$rMax) { f$idx <- f$idx + 1L; f$cMin <- f$cMin + 1L }
  } else if (cmd == "S") {
    f$pos[2] <- f$pos[2] + 1L
    if (f$pos[2] == f$cMax) { f$idx <- f$idx + 1L; f$rMax <- f$rMax - 1L }
  } else if (cmd == "V") {
    f$pos[1] <- f$pos[1] - 1L
    if (f$pos[1] == f$rMin) { f$idx <- f$idx + 1L; f$cMax <- f$cMax - 1L }
  } else if (cmd == "M") {
    f$pos[2] <- f$pos[2] - 1L
    if (f$pos[2] == f$cMin) { f$idx <- f$idx + 1L; f$rMin <- f$rMin + 1L }
  }
  res
}

fmt_row <- function(row) paste(sprintf("%2d", row), collapse = " ")

rn <- 9L; cn <- 9L
obj <- Filler(rn, cn)
m <- matrix(0L, nrow = rn, ncol = cn)
for (i in 1:(rn * cn)) {
  rc <- filler_next(obj)
  m[rc[1] + 1L, rc[2] + 1L] <- i
}
want <- c(
  " 1 32 31 30 29 28 27 26 25",
  " 2 33 56 55 54 53 52 51 24",
  " 3 34 57 72 71 70 69 50 23",
  " 4 35 58 73 80 79 68 49 22",
  " 5 36 59 74 81 78 67 48 21",
  " 6 37 60 75 76 77 66 47 20",
  " 7 38 61 62 63 64 65 46 19",
  " 8 39 40 41 42 43 44 45 18",
  " 9 10 11 12 13 14 15 16 17"
)
for (i in 1:rn) {
  got <- fmt_row(m[i, ])
  stopifnot(identical(got, want[i]))
}
cat("PASS\\n")
''',
"zig": '''// @@BLOG@@
// LeetCode 107737496. 代码重构_隔离变化 — Zig 版（方案10：Filler+Matrix 组合 9x9 全螺旋）
const std = @import("std");

const RCu = struct { r: usize, c: usize };

const Filler = struct {
    pos_row: usize = 0,
    pos_col: usize = 0,
    idx: usize = 0,
    r_min: usize = 0,
    c_min: usize = 0,
    r_max: usize,
    c_max: usize,

    fn init(rn: usize, cn: usize) Filler {
        return .{ .r_max = rn - 1, .c_max = cn - 1 };
    }
    fn next(self: *Filler) RCu {
        const res = RCu{ .r = self.pos_row, .c = self.pos_col };
        const rule = "ESVM";
        const cmd = rule[self.idx % 4];
        if (cmd == 'E') {
            self.pos_row += 1;
            if (self.pos_row == self.r_max) {
                self.idx += 1;
                self.c_min += 1;
            }
        } else if (cmd == 'S') {
            self.pos_col += 1;
            if (self.pos_col == self.c_max) {
                self.idx += 1;
                self.r_max -= 1;
            }
        } else if (cmd == 'V') {
            self.pos_row -= 1;
            if (self.pos_row == self.r_min) {
                self.idx += 1;
                self.c_max -= 1;
            }
        } else if (cmd == 'M') {
            self.pos_col -= 1;
            if (self.pos_col == self.c_min) {
                self.idx += 1;
                self.r_min += 1;
            }
        }
        return res;
    }
};

fn fmtRow(buf: []u8, row: []const i32) ![]u8 {
    var n: usize = 0;
    for (row, 0..) |x, i| {
        if (i != 0) {
            buf[n] = ' ';
            n += 1;
        }
        var cell_buf: [16]u8 = undefined;
        const cell = try std.fmt.bufPrint(&cell_buf, "{d}", .{x});
        if (cell.len < 2) {
            buf[n] = ' ';
            n += 1;
        }
        for (cell) |ch| {
            buf[n] = ch;
            n += 1;
        }
    }
    return buf[0..n];
}

pub fn main() !void {
    const rn: usize = 9;
    const cn: usize = 9;
    var obj = Filler.init(rn, cn);
    var m: [9][9]i32 = undefined;
    for (&m) |*row| {
        for (row) |*x| x.* = 0;
    }
    for (0..rn * cn) |i| {
        const rc = obj.next();
        m[rc.r][rc.c] = @intCast(i + 1);
    }
    const want = [9][]const u8{
        " 1 32 31 30 29 28 27 26 25",
        " 2 33 56 55 54 53 52 51 24",
        " 3 34 57 72 71 70 69 50 23",
        " 4 35 58 73 80 79 68 49 22",
        " 5 36 59 74 81 78 67 48 21",
        " 6 37 60 75 76 77 66 47 20",
        " 7 38 61 62 63 64 65 46 19",
        " 8 39 40 41 42 43 44 45 18",
        " 9 10 11 12 13 14 15 16 17",
    };
    var buf: [64]u8 = undefined;
    for (want, 0..) |w, i| {
        const got = try fmtRow(&buf, &m[i]);
        if (!std.mem.eql(u8, got, w)) {
            std.debug.print("matrix9 row {d} failed\\n", .{i});
            return error.TestFailed;
        }
    }
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''// @@BLOG@@
// LeetCode 107737496. 代码重构_隔离变化 — Dart 版（方案10：Filler+Matrix 组合 9x9 全螺旋）
class Filler {
  int posRow = 0, posCol = 0, idx = 0;
  int rMin = 0, cMin = 0, rMax = 0, cMax = 0;
  Filler(int rn, int cn) {
    rMax = rn - 1;
    cMax = cn - 1;
  }

  List<int> next() {
    final res = [posRow, posCol];
    final cmd = 'ESVM'[idx % 4];
    if (cmd == 'E') {
      posRow += 1;
      if (posRow == rMax) {
        idx += 1;
        cMin += 1;
      }
    } else if (cmd == 'S') {
      posCol += 1;
      if (posCol == cMax) {
        idx += 1;
        rMax -= 1;
      }
    } else if (cmd == 'V') {
      posRow -= 1;
      if (posRow == rMin) {
        idx += 1;
        cMax -= 1;
      }
    } else if (cmd == 'M') {
      posCol -= 1;
      if (posCol == cMin) {
        idx += 1;
        rMin += 1;
      }
    }
    return res;
  }
}

String fmtRow(List<int> row) => row.map((x) => x.toString().padLeft(2)).join(' ');

void main() {
  const rn = 9, cn = 9;
  final obj = Filler(rn, cn);
  final m = List.generate(rn, (_) => List<int>.filled(cn, 0));
  for (var i = 0; i < rn * cn; i++) {
    final rc = obj.next();
    m[rc[0]][rc[1]] = i + 1;
  }
  const want = <String>[
    ' 1 32 31 30 29 28 27 26 25',
    ' 2 33 56 55 54 53 52 51 24',
    ' 3 34 57 72 71 70 69 50 23',
    ' 4 35 58 73 80 79 68 49 22',
    ' 5 36 59 74 81 78 67 48 21',
    ' 6 37 60 75 76 77 66 47 20',
    ' 7 38 61 62 63 64 65 46 19',
    ' 8 39 40 41 42 43 44 45 18',
    ' 9 10 11 12 13 14 15 16 17',
  ];
  for (var i = 0; i < rn; i++) {
    if (fmtRow(m[i]) != want[i]) throw StateError('matrix9 row $i failed');
  }
  print('PASS');
}
''',
}

# ---------------- I: s11 Rule 循环 ----------------
I = {
"rust": '''// @@BLOG@@
// LeetCode 107737496. 代码重构_隔离变化 — Rust 版（方案11：Rule 循环游标）
struct Rule {
    data: Vec<char>,
    idx: usize,
}

impl Rule {
    fn new(r: &str) -> Self {
        Rule { data: r.chars().collect(), idx: 0 }
    }
    fn next(&mut self) -> char {
        let ch = self.data[self.idx];
        self.idx = (self.idx + 1) % self.data.len();
        ch
    }
    fn peek(&self) -> char {
        self.data[self.idx]
    }
}

fn main() {
    let mut r = Rule::new("ESVM");
    let s1: String = (0..10).map(|_| r.next()).collect();
    let mut r2 = Rule::new("semv");
    let s2: String = (0..6).map(|_| r2.next()).collect();
    assert_eq!(s1, "ESVMESVMES", "rule1");
    assert_eq!(s2, "semvse", "rule2");
    println!("PASS");
}
''',
"lua": '''-- @@BLOG@@
-- LeetCode 107737496. 代码重构_隔离变化 — Lua 版（方案11：Rule 循环游标）
local Rule = {}
Rule.__index = Rule
function Rule.new(r)
    return setmetatable({ data = r, idx = 1, len = #r }, Rule)
end
function Rule:next()
    local ch = self.data:sub(self.idx, self.idx)
    self.idx = (self.idx - 1 + 1) % self.len + 1
    return ch
end
function Rule:peek()
    return self.data:sub(self.idx, self.idx)
end

local r = Rule.new("ESVM")
local s1 = {}
for _ = 1, 10 do s1[#s1 + 1] = r:next() end
local r2 = Rule.new("semv")
local s2 = {}
for _ = 1, 6 do s2[#s2 + 1] = r2:next() end
assert(table.concat(s1) == "ESVMESVMES", "rule1")
assert(table.concat(s2) == "semvse", "rule2")
print("PASS")
''',
"c": '''/* @@BLOG@@
 * LeetCode 107737496. 代码重构_隔离变化 — C 版（方案11：Rule 循环游标）
 */
#include <stdio.h>
#include <string.h>

typedef struct {
    char data[16];
    int idx;
    int length;
} Rule;

static void rule_init(Rule *r, const char *s) {
    strcpy(r->data, s);
    r->idx = 0;
    r->length = (int)strlen(s);
}

static char rule_next(Rule *r) {
    char ch = r->data[r->idx];
    r->idx = (r->idx + 1) % r->length;
    return ch;
}

static char rule_peek(const Rule *r) {
    return r->data[r->idx];
}

int main(void) {
    Rule r;
    rule_init(&r, "ESVM");
    char s1[16] = "";
    for (int i = 0; i < 10; i++) {
        char buf[2] = { rule_next(&r), 0 };
        strcat(s1, buf);
    }
    Rule r2;
    rule_init(&r2, "semv");
    char s2[16] = "";
    for (int i = 0; i < 6; i++) {
        char buf[2] = { rule_next(&r2), 0 };
        strcat(s2, buf);
    }
    if (strcmp(s1, "ESVMESVMES") != 0) { printf("rule1 failed\\n"); return 1; }
    if (strcmp(s2, "semvse") != 0) { printf("rule2 failed\\n"); return 1; }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''// @@BLOG@@
// LeetCode 107737496. 代码重构_隔离变化 — C++ 版（方案11：Rule 循环游标）
#include <iostream>
#include <string>
#include <vector>

class Rule {
public:
    explicit Rule(const std::string &r) : data_(r.begin(), r.end()), idx_(0), length_(r.size()) {}
    char next() {
        char ch = data_[idx_];
        idx_ = (idx_ + 1) % length_;
        return ch;
    }
    char peek() const {
        return data_[idx_];
    }

private:
    std::vector<char> data_;
    size_t idx_;
    size_t length_;
};

int main() {
    Rule r("ESVM");
    std::string s1;
    for (int i = 0; i < 10; ++i) s1 += r.next();
    Rule r2("semv");
    std::string s2;
    for (int i = 0; i < 6; ++i) s2 += r2.next();
    if (s1 != "ESVMESVMES") { std::cout << "rule1 failed" << std::endl; return 1; }
    if (s2 != "semvse") { std::cout << "rule2 failed" << std::endl; return 1; }
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''# @@BLOG@@
# LeetCode 107737496. 代码重构_隔离变化 — R 版（方案11：Rule 循环游标）
Rule <- function(r) {
  e <- new.env(parent = emptyenv())
  e$data <- strsplit(r, "")[[1]]
  e$idx <- 1L
  e$len <- nchar(r)
  class(e) <- "Rule"
  e
}

rule_next <- function(r) {
  ch <- r$data[r$idx]
  r$idx <- (r$idx - 1L + 1L) %% r$len + 1L
  ch
}

r <- Rule("ESVM")
s1 <- paste(replicate(10L, rule_next(r)), collapse = "")
r2 <- Rule("semv")
s2 <- paste(replicate(6L, rule_next(r2)), collapse = "")
stopifnot(identical(s1, "ESVMESVMES"))
stopifnot(identical(s2, "semvse"))
cat("PASS\\n")
''',
"zig": '''// @@BLOG@@
// LeetCode 107737496. 代码重构_隔离变化 — Zig 版（方案11：Rule 循环游标）
const std = @import("std");

const Rule = struct {
    data: []const u8,
    idx: usize = 0,

    fn init(r: []const u8) Rule {
        return .{ .data = r };
    }
    fn next(self: *Rule) u8 {
        const ch = self.data[self.idx];
        self.idx = (self.idx + 1) % self.data.len;
        return ch;
    }
    fn peek(self: *const Rule) u8 {
        return self.data[self.idx];
    }
};

pub fn main() !void {
    var r = Rule.init("ESVM");
    var s1: [10]u8 = undefined;
    for (0..10) |i| s1[i] = r.next();
    var r2 = Rule.init("semv");
    var s2: [6]u8 = undefined;
    for (0..6) |i| s2[i] = r2.next();
    if (!std.mem.eql(u8, &s1, "ESVMESVMES")) return error.TestFailed;
    if (!std.mem.eql(u8, &s2, "semvse")) return error.TestFailed;
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''// @@BLOG@@
// LeetCode 107737496. 代码重构_隔离变化 — Dart 版（方案11：Rule 循环游标）
class Rule {
  String data;
  int idx = 0;
  Rule(this.data);

  String next() {
    final ch = data[idx];
    idx = (idx + 1) % data.length;
    return ch;
  }

  String peek() {
    return data[idx];
  }
}

void main() {
  final r = Rule('ESVM');
  final s1 = List.generate(10, (_) => r.next()).join('');
  final r2 = Rule('semv');
  final s2 = List.generate(6, (_) => r2.next()).join('');
  if (s1 != 'ESVMESVMES') throw StateError('rule1 failed');
  if (s2 != 'semvse') throw StateError('rule2 failed');
  print('PASS');
}
''',
}

# ---------------- J: s12 Location/Rule/Filler 组合（ESVM 4x4 序列） ----------------
J = {
"rust": '''// @@BLOG@@
// LeetCode 107737496. 代码重构_隔离变化 — Rust 版（方案12：Location/Rule/Filler 组合）
#[derive(Clone)]
struct Rule {
    data: Vec<char>,
    idx: usize,
}

impl Rule {
    fn new(r: &str) -> Self {
        Rule { data: r.chars().collect(), idx: 0 }
    }
    fn current(&self) -> char {
        self.data[self.idx]
    }
    fn advance(&mut self) {
        self.idx = (self.idx + 1) % self.data.len();
    }
}

struct Filler {
    pos: (i32, i32),
    r_min: i32,
    c_min: i32,
    r_max: i32,
    c_max: i32,
    cmd: Rule,
}

impl Filler {
    fn new(rn: i32, cn: i32, rule: &str) -> Self {
        Filler {
            pos: (0, 0),
            r_min: 0,
            c_min: 0,
            r_max: rn - 1,
            c_max: cn - 1,
            cmd: Rule::new(rule),
        }
    }
    fn next(&mut self) -> (i32, i32) {
        let res = self.pos;
        let ch = self.cmd.current();
        if ch == 'E' {
            self.pos.0 += 1;
            if self.pos.0 == self.r_max { self.cmd.advance(); self.c_min += 1; }
        } else if ch == 'S' {
            self.pos.1 += 1;
            if self.pos.1 == self.c_max { self.cmd.advance(); self.r_max -= 1; }
        } else if ch == 'V' {
            self.pos.0 -= 1;
            if self.pos.0 == self.r_min { self.cmd.advance(); self.c_max -= 1; }
        } else if ch == 'M' {
            self.pos.1 -= 1;
            if self.pos.1 == self.c_min { self.cmd.advance(); self.r_min += 1; }
        }
        res
    }
}

fn test_filler(rule: &str, rn: i32, cn: i32) -> Vec<Vec<i32>> {
    let mut obj = Filler::new(rn, cn, rule);
    let mut seq: Vec<Vec<i32>> = vec![];
    for _ in 0..(rn * cn) {
        let (r, c) = obj.next();
        seq.push(vec![r, c]);
    }
    seq
}

fn main() {
    let want = vec![
        vec![0,0], vec![1,0], vec![2,0], vec![3,0], vec![3,1], vec![3,2], vec![3,3],
        vec![2,3], vec![1,3], vec![0,3], vec![0,2], vec![0,1], vec![1,1], vec![2,1], vec![2,2], vec![1,2],
    ];
    assert_eq!(test_filler("ESVM", 4, 4), want, "filler4");
    println!("PASS");
}
''',
"lua": '''-- @@BLOG@@
-- LeetCode 107737496. 代码重构_隔离变化 — Lua 版（方案12：Location/Rule/Filler 组合）
local Rule = {}
Rule.__index = Rule
function Rule.new(r)
    return setmetatable({ data = r, idx = 1, len = #r }, Rule)
end
function Rule:current() return self.data:sub(self.idx, self.idx) end
function Rule:advance() self.idx = (self.idx - 1 + 1) % self.len + 1 end

local Filler = {}
Filler.__index = Filler
function Filler.new(rn, cn, rule)
    local f = setmetatable({}, Filler)
    f.pos = { 0, 0 }
    f.rMin = 0
    f.cMin = 0
    f.rMax = rn - 1
    f.cMax = cn - 1
    f.cmd = Rule.new(rule)
    return f
end
function Filler:next()
    local res = { self.pos[1], self.pos[2] }
    local ch = self.cmd:current()
    if ch == "E" then
        self.pos[1] = self.pos[1] + 1
        if self.pos[1] == self.rMax then self.cmd:advance(); self.cMin = self.cMin + 1 end
    elseif ch == "S" then
        self.pos[2] = self.pos[2] + 1
        if self.pos[2] == self.cMax then self.cmd:advance(); self.rMax = self.rMax - 1 end
    elseif ch == "V" then
        self.pos[1] = self.pos[1] - 1
        if self.pos[1] == self.rMin then self.cmd:advance(); self.cMax = self.cMax - 1 end
    elseif ch == "M" then
        self.pos[2] = self.pos[2] - 1
        if self.pos[2] == self.cMin then self.cmd:advance(); self.rMin = self.rMin + 1 end
    end
    return res[1], res[2]
end

local function test_filler(rule, rn, cn)
    local obj = Filler.new(rn, cn, rule)
    local seq = {}
    for _ = 1, rn * cn do
        local r, c = obj:next()
        seq[#seq + 1] = { r, c }
    end
    return seq
end

local got = test_filler("ESVM", 4, 4)
local want = {{0,0},{1,0},{2,0},{3,0},{3,1},{3,2},{3,3},{2,3},{1,3},{0,3},{0,2},{0,1},{1,1},{2,1},{2,2},{1,2}}
for i = 1, 16 do
    assert(got[i][1] == want[i][1] and got[i][2] == want[i][2], "filler4 at " .. i)
end
print("PASS")
''',
"c": '''/* @@BLOG@@
 * LeetCode 107737496. 代码重构_隔离变化 — C 版（方案12：Location/Rule/Filler 组合）
 */
#include <stdio.h>
#include <string.h>

typedef struct {
    char data[16];
    int idx;
    int length;
} Rule;

static void rule_init(Rule *r, const char *s) {
    strcpy(r->data, s);
    r->idx = 0;
    r->length = (int)strlen(s);
}

static char rule_current(const Rule *r) {
    return r->data[r->idx];
}

static void rule_advance(Rule *r) {
    r->idx = (r->idx + 1) % r->length;
}

typedef struct {
    int pos_row, pos_col;
    int r_min, c_min, r_max, c_max;
    Rule cmd;
} Filler;

static void filler_next(Filler *f, int *out_r, int *out_c) {
    *out_r = f->pos_row;
    *out_c = f->pos_col;
    char ch = rule_current(&f->cmd);
    if (ch == 'E') {
        f->pos_row++;
        if (f->pos_row == f->r_max) { rule_advance(&f->cmd); f->c_min++; }
    } else if (ch == 'S') {
        f->pos_col++;
        if (f->pos_col == f->c_max) { rule_advance(&f->cmd); f->r_max--; }
    } else if (ch == 'V') {
        f->pos_row--;
        if (f->pos_row == f->r_min) { rule_advance(&f->cmd); f->c_max--; }
    } else if (ch == 'M') {
        f->pos_col--;
        if (f->pos_col == f->c_min) { rule_advance(&f->cmd); f->r_min++; }
    }
}

int main(void) {
    Filler f;
    f.pos_row = f.pos_col = 0;
    f.r_min = f.c_min = 0;
    f.r_max = 3;
    f.c_max = 3;
    rule_init(&f.cmd, "ESVM");
    int want[16][2] = {
        {0,0},{1,0},{2,0},{3,0},{3,1},{3,2},{3,3},{2,3},
        {1,3},{0,3},{0,2},{0,1},{1,1},{2,1},{2,2},{1,2},
    };
    for (int i = 0; i < 16; i++) {
        int r, c;
        filler_next(&f, &r, &c);
        if (r != want[i][0] || c != want[i][1]) { printf("filler4 at %d failed\\n", i); return 1; }
    }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''// @@BLOG@@
// LeetCode 107737496. 代码重构_隔离变化 — C++ 版（方案12：Location/Rule/Filler 组合）
#include <iostream>
#include <string>
#include <vector>

class Rule {
public:
    explicit Rule(const std::string &r) : data_(r), idx_(0) {}
    char current() const { return data_[idx_]; }
    void advance() { idx_ = (idx_ + 1) % data_.size(); }

private:
    std::string data_;
    size_t idx_;
};

class Filler {
public:
    Filler(int rn, int cn, const std::string &rule)
        : rMax_(rn - 1), cMax_(cn - 1), cmd_(rule) {}
    std::pair<int, int> next() {
        std::pair<int, int> res{posRow_, posCol_};
        char ch = cmd_.current();
        if (ch == 'E') {
            ++posRow_;
            if (posRow_ == rMax_) { cmd_.advance(); ++cMin_; }
        } else if (ch == 'S') {
            ++posCol_;
            if (posCol_ == cMax_) { cmd_.advance(); --rMax_; }
        } else if (ch == 'V') {
            --posRow_;
            if (posRow_ == rMin_) { cmd_.advance(); --cMax_; }
        } else if (ch == 'M') {
            --posCol_;
            if (posCol_ == cMin_) { cmd_.advance(); ++rMin_; }
        }
        return res;
    }

private:
    int posRow_ = 0, posCol_ = 0;
    int rMin_ = 0, cMin_ = 0, rMax_, cMax_;
    Rule cmd_;
};

int main() {
    Filler obj(4, 4, "ESVM");
    std::vector<std::pair<int, int>> want = {
        {0,0},{1,0},{2,0},{3,0},{3,1},{3,2},{3,3},{2,3},
        {1,3},{0,3},{0,2},{0,1},{1,1},{2,1},{2,2},{1,2},
    };
    for (int i = 0; i < 16; ++i) {
        auto rc = obj.next();
        if (rc != want[i]) { std::cout << "filler4 at " << i << " failed" << std::endl; return 1; }
    }
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''# @@BLOG@@
# LeetCode 107737496. 代码重构_隔离变化 — R 版（方案12：Location/Rule/Filler 组合）
Rule <- function(r) {
  e <- new.env(parent = emptyenv())
  e$data <- r
  e$idx <- 1L
  e$len <- nchar(r)
  class(e) <- "Rule"
  e
}
rule_current <- function(r) substr(r$data, r$idx, r$idx)
rule_advance <- function(r) r$idx <- (r$idx - 1L + 1L) %% r$len + 1L

Filler <- function(rn, cn, rule) {
  e <- new.env(parent = emptyenv())
  e$pos <- c(0L, 0L)
  e$rMin <- 0L
  e$cMin <- 0L
  e$rMax <- rn - 1L
  e$cMax <- cn - 1L
  e$cmd <- Rule(rule)
  class(e) <- "Filler"
  e
}

filler_next <- function(f) {
  res <- c(f$pos[1], f$pos[2])
  ch <- rule_current(f$cmd)
  if (ch == "E") {
    f$pos[1] <- f$pos[1] + 1L
    if (f$pos[1] == f$rMax) { rule_advance(f$cmd); f$cMin <- f$cMin + 1L }
  } else if (ch == "S") {
    f$pos[2] <- f$pos[2] + 1L
    if (f$pos[2] == f$cMax) { rule_advance(f$cmd); f$rMax <- f$rMax - 1L }
  } else if (ch == "V") {
    f$pos[1] <- f$pos[1] - 1L
    if (f$pos[1] == f$rMin) { rule_advance(f$cmd); f$cMax <- f$cMax - 1L }
  } else if (ch == "M") {
    f$pos[2] <- f$pos[2] - 1L
    if (f$pos[2] == f$cMin) { rule_advance(f$cmd); f$rMin <- f$rMin + 1L }
  }
  res
}

obj <- Filler(4L, 4L, "ESVM")
want <- list(c(0,0), c(1,0), c(2,0), c(3,0), c(3,1), c(3,2), c(3,3), c(2,3),
             c(1,3), c(0,3), c(0,2), c(0,1), c(1,1), c(2,1), c(2,2), c(1,2))
for (i in 1:16) {
  rc <- as.integer(filler_next(obj))
  stopifnot(identical(rc, as.integer(want[[i]])))
}
cat("PASS\\n")
''',
"zig": '''// @@BLOG@@
// LeetCode 107737496. 代码重构_隔离变化 — Zig 版（方案12：Location/Rule/Filler 组合）
const std = @import("std");

const Rule = struct {
    data: []const u8,
    idx: usize = 0,

    fn init(r: []const u8) Rule {
        return .{ .data = r };
    }
    fn current(self: *const Rule) u8 {
        return self.data[self.idx];
    }
    fn advance(self: *Rule) void {
        self.idx = (self.idx + 1) % self.data.len;
    }
};

const RC = struct { r: i32, c: i32 };

const Filler = struct {
    pos_row: i32 = 0,
    pos_col: i32 = 0,
    r_min: i32 = 0,
    c_min: i32 = 0,
    r_max: i32,
    c_max: i32,
    cmd: Rule,

    fn init(rn: i32, cn: i32, rule: []const u8) Filler {
        return .{ .r_max = rn - 1, .c_max = cn - 1, .cmd = Rule.init(rule) };
    }
    fn next(self: *Filler) RC {
        const res = RC{ .r = self.pos_row, .c = self.pos_col };
        const ch = self.cmd.current();
        if (ch == 'E') {
            self.pos_row += 1;
            if (self.pos_row == self.r_max) {
                self.cmd.advance();
                self.c_min += 1;
            }
        } else if (ch == 'S') {
            self.pos_col += 1;
            if (self.pos_col == self.c_max) {
                self.cmd.advance();
                self.r_max -= 1;
            }
        } else if (ch == 'V') {
            self.pos_row -= 1;
            if (self.pos_row == self.r_min) {
                self.cmd.advance();
                self.c_max -= 1;
            }
        } else if (ch == 'M') {
            self.pos_col -= 1;
            if (self.pos_col == self.c_min) {
                self.cmd.advance();
                self.r_min += 1;
            }
        }
        return res;
    }
};

pub fn main() !void {
    var obj = Filler.init(4, 4, "ESVM");
    const want = [16][2]i32{
        .{ 0, 0 }, .{ 1, 0 }, .{ 2, 0 }, .{ 3, 0 }, .{ 3, 1 }, .{ 3, 2 }, .{ 3, 3 }, .{ 2, 3 },
        .{ 1, 3 }, .{ 0, 3 }, .{ 0, 2 }, .{ 0, 1 }, .{ 1, 1 }, .{ 2, 1 }, .{ 2, 2 }, .{ 1, 2 },
    };
    for (want) |w| {
        const rc = obj.next();
        if (rc.r != w[0] or rc.c != w[1]) return error.TestFailed;
    }
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''// @@BLOG@@
// LeetCode 107737496. 代码重构_隔离变化 — Dart 版（方案12：Location/Rule/Filler 组合）
class Rule {
  String data;
  int idx = 0;
  Rule(this.data);

  String current() {
    return data[idx];
  }

  void advance() {
    idx = (idx + 1) % data.length;
  }
}

class Filler {
  int posRow = 0, posCol = 0;
  int rMin = 0, cMin = 0, rMax = 0, cMax = 0;
  Rule cmd;
  Filler(int rn, int cn, this.cmd) {
    rMax = rn - 1;
    cMax = cn - 1;
  }

  List<int> next() {
    final res = [posRow, posCol];
    final ch = cmd.current();
    if (ch == 'E') {
      posRow += 1;
      if (posRow == rMax) {
        cmd.advance();
        cMin += 1;
      }
    } else if (ch == 'S') {
      posCol += 1;
      if (posCol == cMax) {
        cmd.advance();
        rMax -= 1;
      }
    } else if (ch == 'V') {
      posRow -= 1;
      if (posRow == rMin) {
        cmd.advance();
        cMax -= 1;
      }
    } else if (ch == 'M') {
      posCol -= 1;
      if (posCol == cMin) {
        cmd.advance();
        rMin += 1;
      }
    }
    return res;
  }
}

void main() {
  final obj = Filler(4, 4, Rule('ESVM'));
  final want = <List<int>>[
    [0, 0], [1, 0], [2, 0], [3, 0], [3, 1], [3, 2], [3, 3], [2, 3],
    [1, 3], [0, 3], [0, 2], [0, 1], [1, 1], [2, 1], [2, 2], [1, 2],
  ];
  for (final w in want) {
    final rc = obj.next();
    if (rc[0] != w[0] || rc[1] != w[1]) throw StateError('filler4 failed');
  }
  print('PASS');
}
''',
}

# ---------------- K: s13 正则匹配 ----------------
K = {
"rust": '''// @@BLOG@@
// LeetCode 107737496. 代码重构_隔离变化 — Rust 版（方案13：微型正则匹配 match/matchhere/matchstar）
fn matchhere(re: &str, text: &str) -> bool {
    let rb = re.as_bytes();
    let tb = text.as_bytes();
    if re.is_empty() {
        return true;
    }
    if rb.len() >= 2 && rb[1] == b'*' {
        return matchstar(rb[0], &re[2..], text);
    }
    if rb[0] == b'$' && rb.len() == 1 {
        return text.is_empty();
    }
    if !tb.is_empty() && (rb[0] == b'.' || rb[0] == tb[0]) {
        return matchhere(&re[1..], &text[1..]);
    }
    false
}

fn matchstar(c: u8, re: &str, text: &str) -> bool {
    let tb = text.as_bytes();
    let mut i = 0usize;
    loop {
        if matchhere(re, &text[i..]) {
            return true;
        }
        if i >= tb.len() {
            break;
        }
        if tb[i] != c && c != b'.' {
            break;
        }
        i += 1;
    }
    false
}

fn match_re(re: &str, text: &str) -> bool {
    if !re.is_empty() && re.as_bytes()[0] == b'^' {
        return matchhere(&re[1..], text);
    }
    let mut i = 0usize;
    loop {
        if matchhere(re, &text[i..]) {
            return true;
        }
        if i >= text.len() {
            break;
        }
        i += 1;
    }
    false
}

fn main() {
    assert!(match_re("abc", "xxabcxx"), "m1");
    assert!(match_re("a.c", "axc"), "m2");
    assert!(match_re("a*", "aaaa"), "m3");
    assert!(!match_re("^a", "ba"), "m4");
    assert!(match_re("c$", "abc"), "m5");
    assert!(match_re("a.*c", "aXYZc"), "m6");
    println!("PASS");
}
''',
"lua": '''-- @@BLOG@@
-- LeetCode 107737496. 代码重构_隔离变化 — Lua 版（方案13：微型正则匹配 match/matchhere/matchstar）
local function matchstar(c, re, text)
    local i = 0
    while true do
        if matchhere(re, text:sub(i + 1)) then return true end
        if i >= #text then break end
        if text:sub(i + 1, i + 1) ~= c and c ~= "." then break end
        i = i + 1
    end
    return false
end

function matchhere(re, text)
    if re == "" then return true end
    if #re >= 2 and re:sub(2, 2) == "*" then
        return matchstar(re:sub(1, 1), re:sub(3), text)
    end
    if re:sub(1, 1) == "$" and #re == 1 then return text == "" end
    if #text > 0 and (re:sub(1, 1) == "." or re:sub(1, 1) == text:sub(1, 1)) then
        return matchhere(re:sub(2), text:sub(2))
    end
    return false
end

local function match(re, text)
    if #re > 0 and re:sub(1, 1) == "^" then
        return matchhere(re:sub(2), text)
    end
    local i = 0
    while true do
        if matchhere(re, text:sub(i + 1)) then return true end
        if i >= #text then break end
        i = i + 1
    end
    return false
end

assert(match("abc", "xxabcxx") == true, "m1")
assert(match("a.c", "axc") == true, "m2")
assert(match("a*", "aaaa") == true, "m3")
assert(match("^a", "ba") == false, "m4")
assert(match("c$", "abc") == true, "m5")
assert(match("a.*c", "aXYZc") == true, "m6")
print("PASS")
''',
"c": '''/* @@BLOG@@
 * LeetCode 107737496. 代码重构_隔离变化 — C 版（方案13：微型正则匹配 match/matchhere/matchstar）
 */
#include <stdbool.h>
#include <stdio.h>

static bool matchhere(const char *re, const char *text);

static bool matchstar(char c, const char *re, const char *text) {
    const char *t = text;
    while (true) {
        if (matchhere(re, t)) return true;
        if (*t == 0) break;
        if (*t != c && c != '.') break;
        t++;
    }
    return false;
}

static bool matchhere(const char *re, const char *text) {
    if (*re == 0) return true;
    if (re[1] == '*') return matchstar(re[0], re + 2, text);
    if (re[0] == '$' && re[1] == 0) return *text == 0;
    if (*text != 0 && (re[0] == '.' || re[0] == *text)) return matchhere(re + 1, text + 1);
    return false;
}

static bool match(const char *re, const char *text) {
    if (*re == '^') return matchhere(re + 1, text);
    const char *t = text;
    while (true) {
        if (matchhere(re, t)) return true;
        if (*t == 0) break;
        t++;
    }
    return false;
}

int main(void) {
    if (!match("abc", "xxabcxx")) { printf("m1 failed\\n"); return 1; }
    if (!match("a.c", "axc")) { printf("m2 failed\\n"); return 1; }
    if (!match("a*", "aaaa")) { printf("m3 failed\\n"); return 1; }
    if (match("^a", "ba")) { printf("m4 failed\\n"); return 1; }
    if (!match("c$", "abc")) { printf("m5 failed\\n"); return 1; }
    if (!match("a.*c", "aXYZc")) { printf("m6 failed\\n"); return 1; }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''// @@BLOG@@
// LeetCode 107737496. 代码重构_隔离变化 — C++ 版（方案13：微型正则匹配 match/matchhere/matchstar）
#include <iostream>
#include <string>

static bool matchhere(const std::string &re, const std::string &text);

static bool matchstar(char c, const std::string &re, const std::string &text) {
    size_t i = 0;
    while (true) {
        if (matchhere(re, text.substr(i))) return true;
        if (i >= text.size()) break;
        if (text[i] != c && c != '.') break;
        ++i;
    }
    return false;
}

static bool matchhere(const std::string &re, const std::string &text) {
    if (re.empty()) return true;
    if (re.size() >= 2 && re[1] == '*') return matchstar(re[0], re.substr(2), text);
    if (re[0] == '$' && re.size() == 1) return text.empty();
    if (!text.empty() && (re[0] == '.' || re[0] == text[0])) return matchhere(re.substr(1), text.substr(1));
    return false;
}

static bool match(const std::string &re, const std::string &text) {
    if (!re.empty() && re[0] == '^') return matchhere(re.substr(1), text);
    size_t i = 0;
    while (true) {
        if (matchhere(re, text.substr(i))) return true;
        if (i >= text.size()) break;
        ++i;
    }
    return false;
}

int main() {
    if (!match("abc", "xxabcxx")) { std::cout << "m1 failed" << std::endl; return 1; }
    if (!match("a.c", "axc")) { std::cout << "m2 failed" << std::endl; return 1; }
    if (!match("a*", "aaaa")) { std::cout << "m3 failed" << std::endl; return 1; }
    if (match("^a", "ba")) { std::cout << "m4 failed" << std::endl; return 1; }
    if (!match("c$", "abc")) { std::cout << "m5 failed" << std::endl; return 1; }
    if (!match("a.*c", "aXYZc")) { std::cout << "m6 failed" << std::endl; return 1; }
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''# @@BLOG@@
# LeetCode 107737496. 代码重构_隔离变化 — R 版（方案13：微型正则匹配 match/matchhere/matchstar）
matchstar <- function(c, re, text) {
  i <- 0L
  repeat {
    if (matchhere(re, substr(text, i + 1L, nchar(text)))) return(TRUE)
    if (i >= nchar(text)) break
    if (substr(text, i + 1L, i + 1L) != c && c != ".") break
    i <- i + 1L
  }
  FALSE
}

matchhere <- function(re, text) {
  if (nchar(re) == 0L) return(TRUE)
  if (nchar(re) >= 2L && substr(re, 2L, 2L) == "*") {
    return(matchstar(substr(re, 1L, 1L), substr(re, 3L, nchar(re)), text))
  }
  if (substr(re, 1L, 1L) == "$" && nchar(re) == 1L) return(nchar(text) == 0L)
  if (nchar(text) > 0L && (substr(re, 1L, 1L) == "." || substr(re, 1L, 1L) == substr(text, 1L, 1L))) {
    return(matchhere(substr(re, 2L, nchar(re)), substr(text, 2L, nchar(text))))
  }
  FALSE
}

match_re <- function(re, text) {
  if (nchar(re) > 0L && substr(re, 1L, 1L) == "^") {
    return(matchhere(substr(re, 2L, nchar(re)), text))
  }
  i <- 0L
  repeat {
    if (matchhere(re, substr(text, i + 1L, nchar(text)))) return(TRUE)
    if (i >= nchar(text)) break
    i <- i + 1L
  }
  FALSE
}

stopifnot(match_re("abc", "xxabcxx"))
stopifnot(match_re("a.c", "axc"))
stopifnot(match_re("a*", "aaaa"))
stopifnot(!match_re("^a", "ba"))
stopifnot(match_re("c$", "abc"))
stopifnot(match_re("a.*c", "aXYZc"))
cat("PASS\\n")
''',
"zig": '''// @@BLOG@@
// LeetCode 107737496. 代码重构_隔离变化 — Zig 版（方案13：微型正则匹配 match/matchhere/matchstar）
const std = @import("std");

fn matchhere(re: []const u8, text: []const u8) bool {
    if (re.len == 0) return true;
    if (re.len >= 2 and re[1] == '*') return matchstar(re[0], re[2..], text);
    if (re[0] == '$' and re.len == 1) return text.len == 0;
    if (text.len > 0 and (re[0] == '.' or re[0] == text[0])) return matchhere(re[1..], text[1..]);
    return false;
}

fn matchstar(c: u8, re: []const u8, text: []const u8) bool {
    var i: usize = 0;
    while (true) {
        if (matchhere(re, text[i..])) return true;
        if (i >= text.len) break;
        if (text[i] != c and c != '.') break;
        i += 1;
    }
    return false;
}

fn match(re: []const u8, text: []const u8) bool {
    if (re.len > 0 and re[0] == '^') return matchhere(re[1..], text);
    var i: usize = 0;
    while (true) {
        if (matchhere(re, text[i..])) return true;
        if (i >= text.len) break;
        i += 1;
    }
    return false;
}

pub fn main() !void {
    if (!match("abc", "xxabcxx")) return error.TestFailed;
    if (!match("a.c", "axc")) return error.TestFailed;
    if (!match("a*", "aaaa")) return error.TestFailed;
    if (match("^a", "ba")) return error.TestFailed;
    if (!match("c$", "abc")) return error.TestFailed;
    if (!match("a.*c", "aXYZc")) return error.TestFailed;
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''// @@BLOG@@
// LeetCode 107737496. 代码重构_隔离变化 — Dart 版（方案13：微型正则匹配 match/matchhere/matchstar）
bool matchstar(String c, String re, String text) {
  var i = 0;
  while (true) {
    if (matchhere(re, text.substring(i))) return true;
    if (i >= text.length) break;
    if (text[i] != c && c != '.') break;
    i++;
  }
  return false;
}

bool matchhere(String re, String text) {
  if (re.isEmpty) return true;
  if (re.length >= 2 && re[1] == '*') return matchstar(re[0], re.substring(2), text);
  if (re[0] == r'$' && re.length == 1) return text.isEmpty;
  if (text.isNotEmpty && (re[0] == '.' || re[0] == text[0])) {
    return matchhere(re.substring(1), text.substring(1));
  }
  return false;
}

bool match(String re, String text) {
  if (re.isNotEmpty && re[0] == '^') return matchhere(re.substring(1), text);
  var i = 0;
  while (true) {
    if (matchhere(re, text.substring(i))) return true;
    if (i >= text.length) break;
    i++;
  }
  return false;
}

void main() {
  if (!match('abc', 'xxabcxx')) throw StateError('m1 failed');
  if (!match('a.c', 'axc')) throw StateError('m2 failed');
  if (!match('a*', 'aaaa')) throw StateError('m3 failed');
  if (match('^a', 'ba')) throw StateError('m4 failed');
  if (!match(r'c$', 'abc')) throw StateError('m5 failed');
  if (!match('a.*c', 'aXYZc')) throw StateError('m6 failed');
  print('PASS');
}
''',
}

EXTS = {"rust": ".rs", "lua": ".lua", "c": ".c", "cpp": ".cpp", "r": ".R", "zig": ".zig", "dart": ".dart"}

def main():
    # s1/s2/s3 = A（同实现，注释区分）
    for sol in (1, 2, 3):
        for lang, t in A.items():
            emit(lang, REL + "/solution_%d___%d%s" % (sol, sol, EXTS[lang]), t.replace("@@BLOG@@", BLOG).replace("@@N@@", str(sol)))
    for sol, block in ((4, B), (5, C), (6, D), (7, E), (8, F), (9, G), (10, H), (11, I), (12, J), (13, K)):
        for lang, t in block.items():
            emit(lang, REL + "/solution_%d___%d%s" % (sol, sol, EXTS[lang]), t.replace("@@BLOG@@", BLOG))

if __name__ == "__main__":
    main()
