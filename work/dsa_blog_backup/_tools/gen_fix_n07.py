#!/usr/bin/env python3
# gen_fix_n07.py — 补齐 notes/lc_107524703 人鬼渡河问题 × 7 语言（4 解法）
# s1: 安全判定谓词  s2/s3: DFS+奇偶步求解  s4: 方向入状态的 DFS 变体（断言无解）
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from langlib import emit

REL = "notes/lc_107524703_计算思维之人鬼渡河问题"
BLOG = "来源（blog）：https://blog.csdn.net/tyro_java/article/details/107524703"
DESC = "人鬼渡河问题（3 传教士 3 野人）"

# ---------- s1: is_safe ----------
S1 = {
"rust": '''// @@BLOG@@
// LeetCode 107524703. 人鬼渡河问题 — Rust 版（方案1：安全判定谓词）
fn is_safe(r: i32, g: i32) -> bool {
    0 <= r && r <= 3 && 0 <= g && g <= 3 && (r == 0 || r == 3 || r == g)
}

fn main() {
    let cases: Vec<(i32, i32, bool)> = vec![
        (3, 3, true),
        (3, 1, true),
        (2, 2, true),
        (1, 3, false),
        (0, 0, true),
    ];
    for (idx, (r, g, want)) in cases.iter().enumerate() {
        assert_eq!(is_safe(*r, *g), *want, "is_safe({},{}) failed", r, g);
    }
    println!("PASS");
}
''',
"lua": '''-- @@BLOG@@
-- LeetCode 107524703. 人鬼渡河问题 — Lua 版（方案1：安全判定谓词）
local function is_safe(r, g)
    return 0 <= r and r <= 3 and 0 <= g and g <= 3 and (r == 0 or r == 3 or r == g)
end

local cases = {
    {3, 3, true}, {3, 1, true}, {2, 2, true}, {1, 3, false}, {0, 0, true},
}
for idx, c in ipairs(cases) do
    assert(is_safe(c[1], c[2]) == c[3], "is_safe(" .. c[1] .. "," .. c[2] .. ") failed")
end
print("PASS")
''',
"c": '''/* @@BLOG@@
 * LeetCode 107524703. 人鬼渡河问题 — C 版（方案1：安全判定谓词）
 */
#include <stdio.h>

static int is_safe(int r, int g) {
    return 0 <= r && r <= 3 && 0 <= g && g <= 3 && (r == 0 || r == 3 || r == g);
}

int main(void) {
    int rs[5] = {3, 3, 2, 1, 0};
    int gs[5] = {3, 1, 2, 3, 0};
    int ws[5] = {1, 1, 1, 0, 1};
    for (int i = 0; i < 5; i++) {
        if (is_safe(rs[i], gs[i]) != ws[i]) {
            printf("is_safe(%d,%d) failed\\n", rs[i], gs[i]);
            return 1;
        }
    }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''// @@BLOG@@
// LeetCode 107524703. 人鬼渡河问题 — C++ 版（方案1：安全判定谓词）
#include <iostream>
#include <vector>

static bool is_safe(int r, int g) {
    return 0 <= r && r <= 3 && 0 <= g && g <= 3 && (r == 0 || r == 3 || r == g);
}

int main() {
    std::vector<std::tuple<int, int, bool>> cases = {
        {3, 3, true}, {3, 1, true}, {2, 2, true}, {1, 3, false}, {0, 0, true},
    };
    for (auto &[r, g, want] : cases) {
        if (is_safe(r, g) != want) { std::cout << "is_safe failed" << std::endl; return 1; }
    }
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''# @@BLOG@@
# LeetCode 107524703. 人鬼渡河问题 — R 版（方案1：安全判定谓词）
is_safe <- function(r, g) {
  0 <= r && r <= 3 && 0 <= g && g <= 3 && (r == 0 || r == 3 || r == g)
}

cases <- list(
  list(3L, 3L, TRUE), list(3L, 1L, TRUE), list(2L, 2L, TRUE),
  list(1L, 3L, FALSE), list(0L, 0L, TRUE)
)
for (idx in seq_along(cases)) {
  stopifnot(is_safe(cases[[idx]][[1]], cases[[idx]][[2]]) == cases[[idx]][[3]])
}
cat("PASS\\n")
''',
"zig": '''// @@BLOG@@
// LeetCode 107524703. 人鬼渡河问题 — Zig 版（方案1：安全判定谓词）
const std = @import("std");

fn isSafe(r: i32, g: i32) bool {
    return 0 <= r and r <= 3 and 0 <= g and g <= 3 and (r == 0 or r == 3 or r == g);
}

pub fn main() !void {
    const Case = struct { r: i32, g: i32, want: bool };
    const cases = [_]Case{
        .{ .r = 3, .g = 3, .want = true },
        .{ .r = 3, .g = 1, .want = true },
        .{ .r = 2, .g = 2, .want = true },
        .{ .r = 1, .g = 3, .want = false },
        .{ .r = 0, .g = 0, .want = true },
    };
    for (cases) |c| {
        if (isSafe(c.r, c.g) != c.want) {
            std.debug.print("isSafe({d},{d}) failed\\n", .{ c.r, c.g });
            return error.TestFailed;
        }
    }
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''// @@BLOG@@
// LeetCode 107524703. 人鬼渡河问题 — Dart 版（方案1：安全判定谓词）
bool isSafe(int r, int g) {
  return 0 <= r && r <= 3 && 0 <= g && g <= 3 && (r == 0 || r == 3 || r == g);
}

void main() {
  final cases = <List<dynamic>>[
    [3, 3, true], [3, 1, true], [2, 2, true], [1, 3, false], [0, 0, true],
  ];
  for (var i = 0; i < cases.length; i++) {
    final c = cases[i];
    if (isSafe(c[0] as int, c[1] as int) != c[2] as bool) {
      throw StateError('is_safe(${c[0]},${c[1]}) failed');
    }
  }
  print('PASS');
}
''',
}

# ---------- s2/s3: DFS 求解（两份相同实现） ----------
def dfs_solver(comment_head, comment_tag):
    return {
"rust": '''// @@BLOG@@
// LeetCode 107524703. 人鬼渡河问题 — Rust 版（@@TAG@@：DFS+奇偶步求解）
use std::collections::HashSet;
use std::cell::RefCell;

const D: [[i32; 2]; 5] = [[2, 0], [1, 0], [1, 1], [0, 1], [0, 2]];

fn safe(r: i32, g: i32) -> bool {
    0 <= r && r <= 3 && 0 <= g && g <= 3 && (r == 0 || r == 3 || r == g)
}

fn solve() -> Vec<[i32; 2]> {
    let path: RefCell<Vec<[i32; 2]>> = RefCell::new(vec![]);
    let visited: RefCell<HashSet<String>> = RefCell::new(HashSet::new());

    fn dfs(r: i32, g: i32, step: i32, visited: &RefCell<HashSet<String>>, path: &RefCell<Vec<[i32; 2]>>) -> bool {
        if r == 0 && g == 0 {
            return true;
        }
        let key = format!("{},{},{}", r, g, step % 2);
        if visited.borrow().contains(&key) {
            return false;
        }
        visited.borrow_mut().insert(key);
        let odd = step % 2 == 1;
        for d in D.iter() {
            let (dr, dg) = (d[0], d[1]);
            let (nr, ng);
            if odd {
                if r < dr || g < dg {
                    continue;
                }
                nr = r - dr;
                ng = g - dg;
            } else {
                if (3 - r) < dr || (3 - g) < dg {
                    continue;
                }
                nr = r + dr;
                ng = g + dg;
            }
            if !safe(nr, ng) {
                continue;
            }
            if dfs(nr, ng, step + 1, visited, path) {
                path.borrow_mut().push([dr, dg]);
                return true;
            }
        }
        false
    }

    dfs(3, 3, 1, &visited, &path);
    let mut p = path.borrow().clone();
    p.reverse();
    p
}

fn main() {
    let want: Vec<[i32; 2]> = vec![
        [1, 1], [1, 0], [0, 2], [0, 1], [2, 0],
        [1, 1], [2, 0], [0, 1], [0, 2], [1, 0], [1, 1],
    ];
    let got = solve();
    assert_eq!(got.len(), want.len(), "solve length mismatch");
    for i in 0..want.len() {
        assert_eq!(got[i], want[i], "solve at {} mismatch", i);
    }
    println!("PASS");
}
''',
"lua": '''-- @@BLOG@@
-- LeetCode 107524703. 人鬼渡河问题 — Lua 版（@@TAG@@：DFS+奇偶步求解）
local D = {{2, 0}, {1, 0}, {1, 1}, {0, 1}, {0, 2}}

local function safe(r, g)
    return 0 <= r and r <= 3 and 0 <= g and g <= 3 and (r == 0 or r == 3 or r == g)
end

local function solve()
    local path = {}
    local visited = {}

    local dfs
    dfs = function(r, g, step)
        if r == 0 and g == 0 then return true end
        local key = r .. "," .. g .. "," .. (step % 2)
        if visited[key] then return false end
        visited[key] = true
        local odd = (step % 2 == 1)
        for _, d in ipairs(D) do
            local dr, dg = d[1], d[2]
            local nr, ng
            if odd then
                if r < dr or g < dg then
                    -- 跳过
                    goto continue_move
                end
                nr = r - dr
                ng = g - dg
            else
                if (3 - r) < dr or (3 - g) < dg then
                    goto continue_move
                end
                nr = r + dr
                ng = g + dg
            end
            if safe(nr, ng) and dfs(nr, ng, step + 1) then
                path[#path + 1] = {dr, dg}
                return true
            end
            ::continue_move::
        end
        return false
    end

    dfs(3, 3, 1)
    -- 反转
    local n = #path
    for i = 1, math.floor(n / 2) do
        path[i], path[n - i + 1] = path[n - i + 1], path[i]
    end
    return path
end

local want = {
    {1, 1}, {1, 0}, {0, 2}, {0, 1}, {2, 0},
    {1, 1}, {2, 0}, {0, 1}, {0, 2}, {1, 0}, {1, 1},
}
local got = solve()
assert(#got == #want, "solve length mismatch")
for i = 1, #want do
    assert(got[i][1] == want[i][1] and got[i][2] == want[i][2], "solve at " .. i .. " mismatch")
end
print("PASS")
''',
"c": '''/* @@BLOG@@
 * LeetCode 107524703. 人鬼渡河问题 — C 版（@@TAG@@：DFS+奇偶步求解）
 */
#include <stdio.h>

static const int D[5][2] = {{2, 0}, {1, 0}, {1, 1}, {0, 1}, {0, 2}};
static int path[32][2];
static int path_len = 0;
static int visited_r[64], visited_g[64], visited_p[64], visited_n = 0;

static int safe(int r, int g) {
    return 0 <= r && r <= 3 && 0 <= g && g <= 3 && (r == 0 || r == 3 || r == g);
}

static int is_visited(int r, int g, int parity) {
    for (int i = 0; i < visited_n; i++)
        if (visited_r[i] == r && visited_g[i] == g && visited_p[i] == parity) return 1;
    return 0;
}

static void mark(int r, int g, int parity) {
    visited_r[visited_n] = r; visited_g[visited_n] = g; visited_p[visited_n] = parity;
    visited_n++;
}

static int dfs(int r, int g, int step) {
    if (r == 0 && g == 0) return 1;
    int parity = step % 2;
    if (is_visited(r, g, parity)) return 0;
    mark(r, g, parity);
    int odd = (step % 2 == 1);
    for (int i = 0; i < 5; i++) {
        int dr = D[i][0], dg = D[i][1];
        int nr, ng;
        if (odd) {
            if (r < dr || g < dg) continue;
            nr = r - dr; ng = g - dg;
        } else {
            if ((3 - r) < dr || (3 - g) < dg) continue;
            nr = r + dr; ng = g + dg;
        }
        if (!safe(nr, ng)) continue;
        if (dfs(nr, ng, step + 1)) {
            path[path_len][0] = dr; path[path_len][1] = dg;
            path_len++;
            return 1;
        }
    }
    return 0;
}

int main(void) {
    int want[11][2] = {
        {1, 1}, {1, 0}, {0, 2}, {0, 1}, {2, 0},
        {1, 1}, {2, 0}, {0, 1}, {0, 2}, {1, 0}, {1, 1},
    };
    dfs(3, 3, 1);
    if (path_len != 11) { printf("solve length mismatch: %d\\n", path_len); return 1; }
    for (int i = 0; i < 11; i++) {
        /* path 逆序存放 */
        if (path[10 - i][0] != want[i][0] || path[10 - i][1] != want[i][1]) {
            printf("solve at %d mismatch\\n", i);
            return 1;
        }
    }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''// @@BLOG@@
// LeetCode 107524703. 人鬼渡河问题 — C++ 版（@@TAG@@：DFS+奇偶步求解）
#include <functional>
#include <iostream>
#include <set>
#include <string>
#include <vector>

static const int D[5][2] = {{2, 0}, {1, 0}, {1, 1}, {0, 1}, {0, 2}};

static bool safe(int r, int g) {
    return 0 <= r && r <= 3 && 0 <= g && g <= 3 && (r == 0 || r == 3 || r == g);
}

static std::vector<std::vector<int>> solve() {
    std::vector<std::vector<int>> path;
    std::set<std::string> visited;

    std::function<bool(int, int, int)> dfs = [&](int r, int g, int step) -> bool {
        if (r == 0 && g == 0) return true;
        std::string key = std::to_string(r) + "," + std::to_string(g) + "," + std::to_string(step % 2);
        if (visited.count(key)) return false;
        visited.insert(key);
        bool odd = (step % 2 == 1);
        for (int i = 0; i < 5; ++i) {
            int dr = D[i][0], dg = D[i][1];
            int nr, ng;
            if (odd) {
                if (r < dr || g < dg) continue;
                nr = r - dr; ng = g - dg;
            } else {
                if ((3 - r) < dr || (3 - g) < dg) continue;
                nr = r + dr; ng = g + dg;
            }
            if (!safe(nr, ng)) continue;
            if (dfs(nr, ng, step + 1)) {
                path.push_back({dr, dg});
                return true;
            }
        }
        return false;
    };

    dfs(3, 3, 1);
    std::reverse(path.begin(), path.end());
    return path;
}

int main() {
    std::vector<std::vector<int>> want = {
        {1, 1}, {1, 0}, {0, 2}, {0, 1}, {2, 0},
        {1, 1}, {2, 0}, {0, 1}, {0, 2}, {1, 0}, {1, 1},
    };
    std::vector<std::vector<int>> got = solve();
    if (got != want) { std::cout << "solve mismatch" << std::endl; return 1; }
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''# @@BLOG@@
# LeetCode 107524703. 人鬼渡河问题 — R 版（@@TAG@@：DFS+奇偶步求解）

D <- list(c(2L, 0L), c(1L, 0L), c(1L, 1L), c(0L, 1L), c(0L, 2L))

safe <- function(r, g) {
  0 <= r && r <= 3 && 0 <= g && g <= 3 && (r == 0 || r == 3 || r == g)
}

solve <- function() {
  path <- list()
  visited <- new.env(parent = emptyenv())

  dfs <- function(r, g, step) {
    if (r == 0L && g == 0L) return(TRUE)
    key <- paste(r, g, step %% 2L, sep = ",")
    if (!is.null(visited[[key]])) return(FALSE)
    visited[[key]] <- TRUE
    odd <- (step %% 2L == 1L)
    for (d in D) {
      dr <- d[1]; dg <- d[2]
      nr <- 0L; ng <- 0L
      skip <- FALSE
      if (odd) {
        if (r < dr || g < dg) {
          skip <- TRUE
        } else {
          nr <- r - dr; ng <- g - dg
        }
      } else {
        if ((3L - r) < dr || (3L - g) < dg) {
          skip <- TRUE
        } else {
          nr <- r + dr; ng <- g + dg
        }
      }
      if (!skip && safe(nr, ng) && dfs(nr, ng, step + 1L)) {
        path <<- c(path, list(c(dr, dg)))
        return(TRUE)
      }
    }
    FALSE
  }

  dfs(3L, 3L, 1L)
  rev(path)
}

want <- list(
  c(1L, 1L), c(1L, 0L), c(0L, 2L), c(0L, 1L), c(2L, 0L),
  c(1L, 1L), c(2L, 0L), c(0L, 1L), c(0L, 2L), c(1L, 0L), c(1L, 1L)
)
got <- solve()
stopifnot(length(got) == length(want))
for (i in seq_along(want)) {
  stopifnot(identical(as.integer(got[[i]]), as.integer(want[[i]])))
}
cat("PASS\\n")
''',
"zig": '''// @@BLOG@@
// LeetCode 107524703. 人鬼渡河问题 — Zig 版（@@TAG@@：DFS+奇偶步求解）
const std = @import("std");

const D = [5][2]i32{ .{ 2, 0 }, .{ 1, 0 }, .{ 1, 1 }, .{ 0, 1 }, .{ 0, 2 } };

fn safe(r: i32, g: i32) bool {
    return 0 <= r and r <= 3 and 0 <= g and g <= 3 and (r == 0 or r == 3 or r == g);
}

var path_buf: [32][2]i32 = undefined;
var path_len: usize = 0;
var visited: [4][4][2]bool = undefined;

fn dfs(r: i32, g: i32, step: i32) bool {
    if (r == 0 and g == 0) return true;
    const parity: usize = @intCast(@mod(step, 2));
    const ru: usize = @intCast(r);
    const gu: usize = @intCast(g);
    if (visited[ru][gu][parity]) return false;
    visited[ru][gu][parity] = true;
    const odd = @mod(step, 2) == 1;
    for (D) |d| {
        const dr = d[0];
        const dg = d[1];
        var nr: i32 = undefined;
        var ng: i32 = undefined;
        var skip = false;
        if (odd) {
            if (r < dr or g < dg) {
                skip = true;
            } else {
                nr = r - dr;
                ng = g - dg;
            }
        } else {
            if ((3 - r) < dr or (3 - g) < dg) {
                skip = true;
            } else {
                nr = r + dr;
                ng = g + dg;
            }
        }
        if (skip) continue;
        if (!safe(nr, ng)) continue;
        if (dfs(nr, ng, step + 1)) {
            path_buf[path_len][0] = dr;
            path_buf[path_len][1] = dg;
            path_len += 1;
            return true;
        }
    }
    return false;
}

pub fn main() !void {
    const want = [11][2]i32{
        .{ 1, 1 }, .{ 1, 0 }, .{ 0, 2 }, .{ 0, 1 }, .{ 2, 0 },
        .{ 1, 1 }, .{ 2, 0 }, .{ 0, 1 }, .{ 0, 2 }, .{ 1, 0 }, .{ 1, 1 },
    };
    for (&visited) |*plane| {
        for (plane) |*row| {
            for (row) |*cell| cell.* = false;
        }
    }
    _ = dfs(3, 3, 1);
    if (path_len != 11) {
        std.debug.print("solve length mismatch: {d}\\n", .{path_len});
        return error.TestFailed;
    }
    for (want, 0..) |w, i| {
        if (path_buf[10 - i][0] != w[0] or path_buf[10 - i][1] != w[1]) {
            std.debug.print("solve at {d} mismatch\\n", .{i});
            return error.TestFailed;
        }
    }
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''// @@BLOG@@
// LeetCode 107524703. 人鬼渡河问题 — Dart 版（@@TAG@@：DFS+奇偶步求解）
const D = <List<int>>[[2, 0], [1, 0], [1, 1], [0, 1], [0, 2]];

bool safe(int r, int g) {
  return 0 <= r && r <= 3 && 0 <= g && g <= 3 && (r == 0 || r == 3 || r == g);
}

List<List<int>> solve() {
  final path = <List<int>>[];
  final visited = <String>{};

  bool dfs(int r, int g, int step) {
    if (r == 0 && g == 0) return true;
    final key = '$r,$g,${step % 2}';
    if (visited.contains(key)) return false;
    visited.add(key);
    final odd = step % 2 == 1;
    for (final d in D) {
      final dr = d[0], dg = d[1];
      var nr = 0, ng = 0;
      var skip = false;
      if (odd) {
        if (r < dr || g < dg) {
          skip = true;
        } else {
          nr = r - dr;
          ng = g - dg;
        }
      } else {
        if ((3 - r) < dr || (3 - g) < dg) {
          skip = true;
        } else {
          nr = r + dr;
          ng = g + dg;
        }
      }
      if (skip) continue;
      if (!safe(nr, ng)) continue;
      if (dfs(nr, ng, step + 1)) {
        path.add([dr, dg]);
        return true;
      }
    }
    return false;
  }

  dfs(3, 3, 1);
  return path.reversed.toList();
}

void main() {
  final want = <List<int>>[
    [1, 1], [1, 0], [0, 2], [0, 1], [2, 0],
    [1, 1], [2, 0], [0, 1], [0, 2], [1, 0], [1, 1],
  ];
  final got = solve();
  if (got.toString() != want.toString()) {
    throw StateError('solve mismatch: ' + got.toString());
  }
  print('PASS');
}
''',
    }

# ---------- s4: 方向入状态的 DFS 变体（断言返回空路径） ----------
S4 = {
"rust": '''// @@BLOG@@
// LeetCode 107524703. 人鬼渡河问题 — Rust 版（方案4：方向入状态的 DFS 变体，断言无可行路径）
use std::collections::HashSet;

const D: [[i32; 2]; 5] = [[2, 0], [1, 0], [1, 1], [0, 1], [0, 2]];

fn safe(r: i32, g: i32) -> bool {
    0 <= r && r <= 3 && 0 <= g && g <= 3 && (r == 0 || r == 3 || r == g)
}

fn solve() -> Vec<[i32; 2]> {
    let mut path: Vec<[i32; 2]> = vec![];
    let mut visited: HashSet<String> = HashSet::new();

    fn jump(dir: i32, r: i32, g: i32, step: i32, visited: &mut HashSet<String>, path: &mut Vec<[i32; 2]>) -> bool {
        if r == 0 && g == 0 && step % 2 == 0 {
            return true;
        }
        let key = format!("{},{},{}", r, g, step % 2);
        if visited.contains(&key) {
            return false;
        }
        visited.insert(key);
        for d in D.iter() {
            let (dr, dg) = (d[0], d[1]);
            let nr = r + dir * dr;
            let ng = g + dir * dg;
            if !safe(nr, ng) {
                continue;
            }
            if jump(-dir, nr, ng, step + 1, visited, path) {
                path.push([dr, dg]);
                return true;
            }
        }
        false
    }

    jump(-1, 3, 3, 0, &mut visited, &mut path);
    path.reverse();
    path
}

fn main() {
    // 与 TS 原文件一致：该变体断言返回空路径（parity 约束下无解）
    let got = solve();
    assert!(got.is_empty(), "solve 应返回空路径");
    println!("PASS");
}
''',
"lua": '''-- @@BLOG@@
-- LeetCode 107524703. 人鬼渡河问题 — Lua 版（方案4：方向入状态的 DFS 变体，断言无可行路径）
local D = {{2, 0}, {1, 0}, {1, 1}, {0, 1}, {0, 2}}

local function safe(r, g)
    return 0 <= r and r <= 3 and 0 <= g and g <= 3 and (r == 0 or r == 3 or r == g)
end

local function solve()
    local path = {}
    local visited = {}

    local jump
    jump = function(dir, r, g, step)
        if r == 0 and g == 0 and step % 2 == 0 then return true end
        local key = r .. "," .. g .. "," .. (step % 2)
        if visited[key] then return false end
        visited[key] = true
        for _, d in ipairs(D) do
            local dr, dg = d[1], d[2]
            local nr = r + dir * dr
            local ng = g + dir * dg
            if safe(nr, ng) and jump(-dir, nr, ng, step + 1) then
                path[#path + 1] = {dr, dg}
                return true
            end
        end
        return false
    end

    jump(-1, 3, 3, 0)
    local n = #path
    for i = 1, math.floor(n / 2) do
        path[i], path[n - i + 1] = path[n - i + 1], path[i]
    end
    return path
end

-- 与 TS 原文件一致：该变体断言返回空路径（parity 约束下无解）
local got = solve()
assert(#got == 0, "solve 应返回空路径")
print("PASS")
''',
"c": '''/* @@BLOG@@
 * LeetCode 107524703. 人鬼渡河问题 — C 版（方案4：方向入状态的 DFS 变体，断言无可行路径）
 */
#include <stdio.h>

static const int D[5][2] = {{2, 0}, {1, 0}, {1, 1}, {0, 1}, {0, 2}};
static int path[32][2];
static int path_len = 0;
static int visited_r[64], visited_g[64], visited_p[64], visited_n = 0;

static int safe(int r, int g) {
    return 0 <= r && r <= 3 && 0 <= g && g <= 3 && (r == 0 || r == 3 || r == g);
}

static int is_visited(int r, int g, int parity) {
    for (int i = 0; i < visited_n; i++)
        if (visited_r[i] == r && visited_g[i] == g && visited_p[i] == parity) return 1;
    return 0;
}

static void mark(int r, int g, int parity) {
    visited_r[visited_n] = r; visited_g[visited_n] = g; visited_p[visited_n] = parity;
    visited_n++;
}

static int jump(int dir, int r, int g, int step) {
    if (r == 0 && g == 0 && step % 2 == 0) return 1;
    int parity = step % 2;
    if (is_visited(r, g, parity)) return 0;
    mark(r, g, parity);
    for (int i = 0; i < 5; i++) {
        int dr = D[i][0], dg = D[i][1];
        int nr = r + dir * dr;
        int ng = g + dir * dg;
        if (!safe(nr, ng)) continue;
        if (jump(-dir, nr, ng, step + 1)) {
            path[path_len][0] = dr; path[path_len][1] = dg;
            path_len++;
            return 1;
        }
    }
    return 0;
}

int main(void) {
    jump(-1, 3, 3, 0);
    /* 与 TS 原文件一致：该变体断言返回空路径（parity 约束下无解） */
    if (path_len != 0) { printf("FAIL: got %d moves\\n", path_len); return 1; }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''// @@BLOG@@
// LeetCode 107524703. 人鬼渡河问题 — C++ 版（方案4：方向入状态的 DFS 变体，断言无可行路径）
#include <functional>
#include <iostream>
#include <set>
#include <string>
#include <vector>

static const int D[5][2] = {{2, 0}, {1, 0}, {1, 1}, {0, 1}, {0, 2}};

static bool safe(int r, int g) {
    return 0 <= r && r <= 3 && 0 <= g && g <= 3 && (r == 0 || r == 3 || r == g);
}

static std::vector<std::vector<int>> solve() {
    std::vector<std::vector<int>> path;
    std::set<std::string> visited;

    std::function<bool(int, int, int, int)> jump = [&](int dir, int r, int g, int step) -> bool {
        if (r == 0 && g == 0 && step % 2 == 0) return true;
        std::string key = std::to_string(r) + "," + std::to_string(g) + "," + std::to_string(step % 2);
        if (visited.count(key)) return false;
        visited.insert(key);
        for (int i = 0; i < 5; ++i) {
            int dr = D[i][0], dg = D[i][1];
            int nr = r + dir * dr;
            int ng = g + dir * dg;
            if (!safe(nr, ng)) continue;
            if (jump(-dir, nr, ng, step + 1)) {
                path.push_back({dr, dg});
                return true;
            }
        }
        return false;
    };

    jump(-1, 3, 3, 0);
    std::reverse(path.begin(), path.end());
    return path;
}

int main() {
    /* 与 TS 原文件一致：该变体断言返回空路径（parity 约束下无解） */
    std::vector<std::vector<int>> got = solve();
    if (!got.empty()) { std::cout << "FAIL: got " << got.size() << " moves" << std::endl; return 1; }
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''# @@BLOG@@
# LeetCode 107524703. 人鬼渡河问题 — R 版（方案4：方向入状态的 DFS 变体，断言无可行路径）

D <- list(c(2L, 0L), c(1L, 0L), c(1L, 1L), c(0L, 1L), c(0L, 2L))

safe <- function(r, g) {
  0 <= r && r <= 3 && 0 <= g && g <= 3 && (r == 0 || r == 3 || r == g)
}

solve <- function() {
  path <- list()
  visited <- new.env(parent = emptyenv())

  jump <- function(dir, r, g, step) {
    if (r == 0L && g == 0L && step %% 2L == 0L) return(TRUE)
    key <- paste(r, g, step %% 2L, sep = ",")
    if (!is.null(visited[[key]])) return(FALSE)
    visited[[key]] <- TRUE
    for (d in D) {
      dr <- d[1]; dg <- d[2]
      nr <- r + dir * dr
      ng <- g + dir * dg
      if (safe(nr, ng) && jump(-dir, nr, ng, step + 1L)) {
        path <<- c(path, list(c(dr, dg)))
        return(TRUE)
      }
    }
    FALSE
  }

  jump(-1L, 3L, 3L, 0L)
  rev(path)
}

# 与 TS 原文件一致：该变体断言返回空路径（parity 约束下无解）
got <- solve()
stopifnot(length(got) == 0L)
cat("PASS\\n")
''',
"zig": '''// @@BLOG@@
// LeetCode 107524703. 人鬼渡河问题 — Zig 版（方案4：方向入状态的 DFS 变体，断言无可行路径）
const std = @import("std");

const D = [5][2]i32{ .{ 2, 0 }, .{ 1, 0 }, .{ 1, 1 }, .{ 0, 1 }, .{ 0, 2 } };

fn safe(r: i32, g: i32) bool {
    return 0 <= r and r <= 3 and 0 <= g and g <= 3 and (r == 0 or r == 3 or r == g);
}

var path_len: usize = 0;
var visited: [4][4][2]bool = undefined;

fn jump(dir: i32, r: i32, g: i32, step: i32) bool {
    if (r == 0 and g == 0 and @mod(step, 2) == 0) return true;
    const parity: usize = @intCast(@mod(step, 2));
    const ru: usize = @intCast(r);
    const gu: usize = @intCast(g);
    if (visited[ru][gu][parity]) return false;
    visited[ru][gu][parity] = true;
    for (D) |d| {
        const nr = r + dir * d[0];
        const ng = g + dir * d[1];
        if (!safe(nr, ng)) continue;
        if (jump(-dir, nr, ng, step + 1)) {
            path_len += 1;
            return true;
        }
    }
    return false;
}

pub fn main() !void {
    for (&visited) |*plane| {
        for (plane) |*row| {
            for (row) |*cell| cell.* = false;
        }
    }
    _ = jump(-1, 3, 3, 0);
    // 与 TS 原文件一致：该变体断言返回空路径（parity 约束下无解）
    if (path_len != 0) {
        std.debug.print("FAIL: got {d} moves\\n", .{path_len});
        return error.TestFailed;
    }
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''// @@BLOG@@
// LeetCode 107524703. 人鬼渡河问题 — Dart 版（方案4：方向入状态的 DFS 变体，断言无可行路径）
const D = <List<int>>[[2, 0], [1, 0], [1, 1], [0, 1], [0, 2]];

bool safe(int r, int g) {
  return 0 <= r && r <= 3 && 0 <= g && g <= 3 && (r == 0 || r == 3 || r == g);
}

List<List<int>> solve() {
  final path = <List<int>>[];
  final visited = <String>{};

  bool jump(int dir, int r, int g, int step) {
    if (r == 0 && g == 0 && step % 2 == 0) return true;
    final key = '$r,$g,${step % 2}';
    if (visited.contains(key)) return false;
    visited.add(key);
    for (final d in D) {
      final dr = d[0], dg = d[1];
      final nr = r + dir * dr;
      final ng = g + dir * dg;
      if (!safe(nr, ng)) continue;
      if (jump(-dir, nr, ng, step + 1)) {
        path.add([dr, dg]);
        return true;
      }
    }
    return false;
  }

  jump(-1, 3, 3, 0);
  return path.reversed.toList();
}

void main() {
  // 与 TS 原文件一致：该变体断言返回空路径（parity 约束下无解）
  final got = solve();
  if (got.isNotEmpty) throw StateError('FAIL: got ${got.length} moves');
  print('PASS');
}
''',
}

def main():
    exts = {"rust": ".rs", "lua": ".lua", "c": ".c", "cpp": ".cpp", "r": ".R", "zig": ".zig", "dart": ".dart"}
    for sol in (2, 3):
        for lang, t in dfs_solver("", "方案%d" % sol).items():
            out = t.replace("@@BLOG@@", BLOG).replace("@@TAG@@", "方案%d" % sol)
            emit(lang, REL + "/solution_%d___%d%s" % (sol, sol, exts[lang]), out)
    for lang, t in S1.items():
        emit(lang, REL + "/solution_1___1" + exts[lang], t.replace("@@BLOG@@", BLOG))
    for lang, t in S4.items():
        emit(lang, REL + "/solution_4___4" + exts[lang], t.replace("@@BLOG@@", BLOG))

if __name__ == "__main__":
    main()
