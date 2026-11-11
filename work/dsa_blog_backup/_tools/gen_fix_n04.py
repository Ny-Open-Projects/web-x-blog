#!/usr/bin/env python3
# gen_fix_n04.py — 补齐 notes/lc_112548608 经典农夫过河问题（DFS 版）× 7 语言
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from langlib import emit

REL = "notes/lc_112548608_计算思维之经典农夫过河问题c++实现"
BLOG = "https://blog.csdn.net/tyro_java/article/details/112548608"
HEAD = "LeetCode 112548608. 计算思维之经典农夫过河问题C++实现（DFS 求任一可行过河序列）"
WANT_LUA = "local wantPath = {\"S\", \"-\", \"W\", \"S\", \"V\", \"-\", \"S\"}"

T_RUST = '''// 来源（blog）：@@BLOG@@
// @@HEAD@@
fn invalid(st: &[i32; 4]) -> bool {
    let (h, w, s, v) = (st[0], st[1], st[2], st[3]);
    if h != s && s == w {
        return true;
    }
    if h != s && s == v {
        return true;
    }
    false
}

const ROLES: [char; 4] = ['-', 'W', 'S', 'V'];
const ROLE_IDX: [usize; 4] = [0, 1, 2, 3]; // '-'->0 占位, W->1, S->2, V->3

fn solve_farmer() -> Vec<char> {
    let mut path: Vec<char> = vec![];
    let mut visited: std::collections::HashSet<[i32; 4]> = std::collections::HashSet::new();

    fn go(st: [i32; 4], visited: &mut std::collections::HashSet<[i32; 4]>, path: &mut Vec<char>) -> bool {
        if st == [1, 1, 1, 1] {
            return true;
        }
        if visited.contains(&st) {
            return false;
        }
        visited.insert(st);
        for ri in 0..4usize {
            let mut ns = st;
            ns[0] = 1 - ns[0]; // 农夫总是过河
            if ri != 0 {
                let idx = ROLE_IDX[ri];
                // 农夫必须与所带物品在出发前同岸
                if st[0] != st[idx] {
                    continue;
                }
                ns[idx] = 1 - ns[idx];
            }
            if invalid(&ns) {
                continue;
            }
            if go(ns, visited, path) {
                path.push(ROLES[ri]);
                return true;
            }
        }
        false
    }

    go([0, 0, 0, 0], &mut visited, &mut path);
    path.reverse();
    path
}

// 模拟走 path，校验每步合法且终点为 (1,1,1,1)
fn simulate(path: &[char]) -> bool {
    let mut st = [0i32; 4];
    for &role in path {
        let before = st;
        st[0] = 1 - st[0];
        if role != '-' {
            let idx = match role {
                'W' => 1,
                'S' => 2,
                'V' => 3,
                _ => 0,
            };
            if before[0] != before[idx] {
                return false;
            }
            st[idx] = 1 - st[idx];
        }
        if invalid(&st) {
            return false;
        }
    }
    st == [1, 1, 1, 1]
}

fn main() {
    let want_path = ['S', '-', 'W', 'S', 'V', '-', 'S'];
    let want_readable = "HS H HW HS HV H HS";

    let got_path = solve_farmer();

    // case1: 完整路径与参考实现一致
    assert_eq!(got_path.len(), want_path.len(), "path length mismatch");
    for (i, (g, w)) in got_path.iter().zip(want_path.iter()).enumerate() {
        assert_eq!(g, w, "path[{}] mismatch", i);
    }

    // case2: 可读方案串一致
    let got_readable: String = got_path
        .iter()
        .map(|&r| {
            if r != '-' {
                format!("H{}", r)
            } else {
                "H".to_string()
            }
        })
        .collect::<Vec<_>>()
        .join(" ");
    assert_eq!(got_readable, want_readable, "readable mismatch");

    // case3: 路径 7 步
    assert_eq!(got_path.len(), 7, "steps mismatch");

    // case4: 模拟校验每步合法且到达终点
    assert!(simulate(&got_path), "simulate failed");

    println!("PASS");
}
'''

T_LUA = '''-- 来源（blog）：@@BLOG@@
-- @@HEAD@@

local function invalid(st)
    local h, w, s, v = st[1], st[2], st[3], st[4]
    if h ~= s and s == w then return true end
    if h ~= s and s == v then return true end
    return false
end

local role_idx = { ["-"] = 0, ["W"] = 1, ["S"] = 2, ["V"] = 3 }

local function solve_farmer()
    local path = {}
    local visited = {}

    local go
    go = function(st)
        if st[1] == 1 and st[2] == 1 and st[3] == 1 and st[4] == 1 then
            return true
        end
        local key = table.concat(st, ",")
        if visited[key] then return false end
        visited[key] = true
        for _, role in ipairs({ "-", "W", "S", "V" }) do
            local ns = { st[1], st[2], st[3], st[4] }
            ns[1] = 1 - ns[1]  -- 农夫总是过河
            if role ~= "-" then
                local idx = role_idx[role] + 1
                -- 农夫必须与所带物品在出发前同岸
                if st[1] ~= st[idx] then
                    -- continue 语义：不递归
                    goto continue_role
                end
                ns[idx] = 1 - ns[idx]
            end
            if not invalid(ns) then
                if go(ns) then
                    path[#path + 1] = role
                    return true
                end
            end
            ::continue_role::
        end
        return false
    end

    go({0, 0, 0, 0})
    -- 反转
    local n = #path
    for i = 1, math.floor(n / 2) do
        path[i], path[n - i + 1] = path[n - i + 1], path[i]
    end
    return path
end

-- 模拟走 path，校验每步合法且终点为 (1,1,1,1)
local function simulate(path)
    local st = {0, 0, 0, 0}
    for _, role in ipairs(path) do
        local before = { st[1], st[2], st[3], st[4] }
        st[1] = 1 - st[1]
        if role ~= "-" then
            local idx = role_idx[role] + 1
            if before[1] ~= before[idx] then return false end
            st[idx] = 1 - st[idx]
        end
        if invalid(st) then return false end
    end
    return st[1] == 1 and st[2] == 1 and st[3] == 1 and st[4] == 1
end

@@WANT@@
local wantReadable = "HS H HW HS HV H HS"

local gotPath = solve_farmer()

-- case1: 完整路径一致
assert(#gotPath == #wantPath, "path length mismatch")
for i = 1, #wantPath do
    assert(gotPath[i] == wantPath[i], "path[" .. i .. "] mismatch: got " .. tostring(gotPath[i]))
end

-- case2: 可读方案串一致
local parts = {}
for i, r in ipairs(gotPath) do
    if r ~= "-" then parts[i] = "H" .. r else parts[i] = "H" end
end
local gotReadable = table.concat(parts, " ")
assert(gotReadable == wantReadable, "readable mismatch: got " .. gotReadable)

-- case3: 路径 7 步
assert(#gotPath == 7, "steps mismatch")

-- case4: 模拟校验
assert(simulate(gotPath), "simulate failed")

print("PASS")
'''

T_C = '''/* 来源（blog）：@@BLOG@@
 * @@HEAD@@
 * 状态编码 4bit：bit3=农夫 bit2=狼(W) bit1=羊(S) bit0=菜(V)
 */
#include <stdio.h>
#include <string.h>

static int invalid(int s) {
    int h = (s >> 3) & 1, w = (s >> 2) & 1, sg = (s >> 1) & 1, v = s & 1;
    if (h != sg && sg == w) return 1;
    if (h != sg && sg == v) return 1;
    return 0;
}

static char path[16];
static int path_len = 0;
static int visited[16];

static int go(int st) {
    if (st == 15) return 1;
    if (visited[st]) return 0;
    visited[st] = 1;
    static const char roles[4] = { '-', 'W', 'S', 'V' };
    for (int ri = 0; ri < 4; ri++) {
        int shift = (ri == 0) ? -1 : (3 - ri); /* W->bit2 S->bit1 V->bit0 */
        int ns = st ^ 8; /* 农夫总是过河 */
        if (ri != 0) {
            if (((st >> 3) & 1) != ((st >> shift) & 1)) continue; /* 出发前同岸 */
            ns = ns ^ (1 << shift);
        }
        if (invalid(ns)) continue;
        if (go(ns)) {
            path[path_len++] = roles[ri];
            return 1;
        }
    }
    return 0;
}

static int simulate(const char *p, int n) {
    int st = 0;
    for (int i = n - 1; i >= 0; i--) { /* path 逆序存放，模拟按正序走 */
        char role = p[i];
        int before = st;
        st ^= 8;
        if (role != '-') {
            int shift = (role == 'W') ? 2 : (role == 'S') ? 1 : 0;
            if (((before >> 3) & 1) != ((before >> shift) & 1)) return 0;
            st ^= (1 << shift);
        }
        if (invalid(st)) return 0;
    }
    return st == 15;
}

int main(void) {
    const char want_path[7] = { 'S', '-', 'W', 'S', 'V', '-', 'S' };
    const char *want_readable = "HS H HW HS HV H HS";

    memset(visited, 0, sizeof(visited));
    go(0);

    /* case1: 路径一致（path 为逆序存放） */
    if (path_len != 7) { printf("FAIL length %d\\n", path_len); return 1; }
    for (int i = 0; i < 7; i++) {
        if (path[6 - i] != want_path[i]) {
            printf("FAIL path[%d] got %c want %c\\n", i, path[6 - i], want_path[i]);
            return 1;
        }
    }

    /* case2: 可读方案串 */
    char got_readable[64] = "";
    for (int i = 0; i < 7; i++) {
        char role = path[6 - i];
        char piece[4];
        if (role != '-') snprintf(piece, sizeof(piece), "H%c", role);
        else snprintf(piece, sizeof(piece), "H");
        if (i) strcat(got_readable, " ");
        strcat(got_readable, piece);
    }
    if (strcmp(got_readable, want_readable) != 0) {
        printf("FAIL readable got %s\\n", got_readable);
        return 1;
    }

    /* case3 + case4 */
    if (!simulate(path, path_len)) { printf("FAIL simulate\\n"); return 1; }

    printf("PASS\\n");
    return 0;
}
'''

T_CPP = '''// 来源（blog）：@@BLOG@@
// @@HEAD@@
#include <iostream>
#include <set>
#include <string>
#include <vector>

static bool invalid(const std::vector<int> &st) {
    int h = st[0], w = st[1], s = st[2], v = st[3];
    if (h != s && s == w) return true;
    if (h != s && s == v) return true;
    return false;
}

static std::vector<char> solve_farmer() {
    std::vector<char> path;
    std::set<std::string> visited;
    static const char roles[4] = { '-', 'W', 'S', 'V' };
    static const int role_idx[4] = { 0, 1, 2, 3 };

    std::function<bool(std::vector<int>)> go = [&](std::vector<int> st) -> bool {
        if (st == std::vector<int>{1, 1, 1, 1}) return true;
        std::string key;
        for (size_t i = 0; i < 4; ++i) { if (i) key += ","; key += std::to_string(st[i]); }
        if (visited.count(key)) return false;
        visited.insert(key);
        for (int ri = 0; ri < 4; ++ri) {
            std::vector<int> ns = st;
            ns[0] = 1 - ns[0]; // 农夫总是过河
            if (ri != 0) {
                int idx = role_idx[ri];
                if (st[0] != st[idx]) continue; // 出发前同岸
                ns[idx] = 1 - ns[idx];
            }
            if (invalid(ns)) continue;
            if (go(ns)) {
                path.push_back(roles[ri]);
                return true;
            }
        }
        return false;
    };

    go({0, 0, 0, 0});
    std::reverse(path.begin(), path.end());
    return path;
}

static bool simulate(const std::vector<char> &path) {
    std::vector<int> st{0, 0, 0, 0};
    for (char role : path) {
        std::vector<int> before = st;
        st[0] = 1 - st[0];
        if (role != '-') {
            int idx = (role == 'W') ? 1 : (role == 'S') ? 2 : 3;
            if (before[0] != before[idx]) return false;
            st[idx] = 1 - st[idx];
        }
        if (invalid(st)) return false;
    }
    return st == std::vector<int>{1, 1, 1, 1};
}

int main() {
    std::vector<char> want_path = {'S', '-', 'W', 'S', 'V', '-', 'S'};
    std::string want_readable = "HS H HW HS HV H HS";

    std::vector<char> got_path = solve_farmer();

    // case1: 路径一致
    if (got_path != want_path) { std::cout << "FAIL path mismatch" << std::endl; return 1; }

    // case2: 可读方案串
    std::string got_readable;
    for (size_t i = 0; i < got_path.size(); ++i) {
        char r = got_path[i];
        if (i) got_readable += " ";
        got_readable += 'H';
        if (r != '-') got_readable += r;
    }
    if (got_readable != want_readable) { std::cout << "FAIL readable: " << got_readable << std::endl; return 1; }

    // case3: 7 步
    if (got_path.size() != 7) { std::cout << "FAIL steps" << std::endl; return 1; }

    // case4: 模拟校验
    if (!simulate(got_path)) { std::cout << "FAIL simulate" << std::endl; return 1; }

    std::cout << "PASS" << std::endl;
    return 0;
}
'''

T_R = '''# 来源（blog）：@@BLOG@@
# @@HEAD@@

invalid <- function(st) {
  h <- st[1]; w <- st[2]; s <- st[3]; v <- st[4]
  if (h != s && s == w) return(TRUE)
  if (h != s && s == v) return(TRUE)
  FALSE
}

role_idx <- c("-" = 0, "W" = 1, "S" = 2, "V" = 3)

solve_farmer <- function() {
  path <- character(0)
  visited <- new.env(parent = emptyenv())

  go <- function(st) {
    if (st[1] == 1L && st[2] == 1L && st[3] == 1L && st[4] == 1L) return(TRUE)
    key <- paste(st, collapse = ",")
    if (!is.null(visited[[key]])) return(FALSE)
    visited[[key]] <- TRUE
    for (role in c("-", "W", "S", "V")) {
      ns <- st
      ns[1] <- 1L - ns[1]  # 农夫总是过河
      ok <- TRUE
      if (role != "-") {
        idx <- as.integer(role_idx[[role]]) + 1L
        if (st[1] != st[idx]) {
          ok <- FALSE  # 出发前不同岸，跳过
        } else {
          ns[idx] <- 1L - ns[idx]
        }
      }
      if (ok && !invalid(ns)) {
        if (go(ns)) {
          path <<- c(path, role)
          return(TRUE)
        }
      }
    }
    FALSE
  }

  go(c(0L, 0L, 0L, 0L))
  rev(path)
}

simulate <- function(p) {
  st <- c(0L, 0L, 0L, 0L)
  for (role in p) {
    before <- st
    st[1] <- 1L - st[1]
    if (role != "-") {
      idx <- as.integer(role_idx[[role]]) + 1L
      if (before[1] != before[idx]) return(FALSE)
      st[idx] <- 1L - st[idx]
    }
    if (invalid(st)) return(FALSE)
  }
  st[1] == 1L && st[2] == 1L && st[3] == 1L && st[4] == 1L
}

wantPath <- c("S", "-", "W", "S", "V", "-", "S")
wantReadable <- "HS H HW HS HV H HS"

gotPath <- solve_farmer()

# case1: 路径一致
stopifnot(length(gotPath) == length(wantPath))
for (i in seq_along(wantPath)) {
  stopifnot(identical(gotPath[i], wantPath[i]))
}

# case2: 可读方案串
parts <- ifelse(gotPath != "-", paste0("H", gotPath), "H")
gotReadable <- paste(parts, collapse = " ")
stopifnot(identical(gotReadable, wantReadable))

# case3: 7 步
stopifnot(length(gotPath) == 7L)

# case4: 模拟校验
stopifnot(simulate(gotPath))

cat("PASS\\n")
'''

T_ZIG = '''// 来源（blog）：@@BLOG@@
// @@HEAD@@
// 状态编码 4bit：bit3=农夫 bit2=狼(W) bit1=羊(S) bit0=菜(V)
const std = @import("std");

fn invalid(s: u4) bool {
    const h: u1 = @truncate(s >> 3);
    const w: u1 = @truncate(s >> 2);
    const sg: u1 = @truncate(s >> 1);
    const v: u1 = @truncate(s);
    if (h != sg and sg == w) return true;
    if (h != sg and sg == v) return true;
    return false;
}

var path_buf: [16]u8 = undefined;
var path_len: usize = 0;
var visited: [16]bool = undefined;

fn go(st: u4) bool {
    if (st == 15) return true;
    if (visited[st]) return false;
    visited[st] = true;
    const roles = [4]u8{ '-', 'W', 'S', 'V' };
    var ri: usize = 0;
    while (ri < 4) : (ri += 1) {
        const shift: u2 = if (ri == 0) 0 else @intCast(3 - ri); // W->2 S->1 V->0
        var ns: u4 = st ^ 8; // 农夫总是过河
        if (ri != 0) {
            if ((st >> 3 & 1) != (st >> shift & 1)) continue; // 出发前同岸
            ns = ns ^ (@as(u4, 1) << shift);
        }
        if (invalid(ns)) continue;
        if (go(ns)) {
            path_buf[path_len] = roles[ri];
            path_len += 1;
            return true;
        }
    }
    return false;
}

fn simulate(p: []const u8) bool {
    var st: u4 = 0;
    var i: usize = p.len;
    while (i > 0) { // path 逆序存放，模拟按正序走
        i -= 1;
        const role = p[i];
        const before = st;
        st = st ^ 8;
        if (role != '-') {
            const shift: u2 = if (role == 'W') 2 else if (role == 'S') 1 else 0;
            if ((before >> 3 & 1) != (before >> shift & 1)) return false;
            st = st ^ (@as(u4, 1) << shift);
        }
        if (invalid(st)) return false;
    }
    return st == 15;
}

pub fn main() !void {
    const want_path = [7]u8{ 'S', '-', 'W', 'S', 'V', '-', 'S' };
    const want_readable = "HS H HW HS HV H HS";

    @memset(&visited, false);
    _ = go(0);

    // case1: 路径一致（path_buf 逆序存放）
    if (path_len != 7) {
        std.debug.print("FAIL length {d}\\n", .{path_len});
        return error.TestFailed;
    }
    for (want_path, 0..) |w, i| {
        if (path_buf[6 - i] != w) {
            std.debug.print("FAIL path[{d}] got {c} want {c}\\n", .{ i, path_buf[6 - i], w });
            return error.TestFailed;
        }
    }

    // case2: 可读方案串
    var buf: [64]u8 = undefined;
    var n: usize = 0;
    for (0..7) |i| {
        const role = path_buf[6 - i];
        if (i != 0) {
            buf[n] = ' ';
            n += 1;
        }
        buf[n] = 'H';
        n += 1;
        if (role != '-') {
            buf[n] = role;
            n += 1;
        }
    }
    const got_readable = buf[0..n];
    if (!std.mem.eql(u8, got_readable, want_readable)) {
        std.debug.print("FAIL readable: {s}\\n", .{got_readable});
        return error.TestFailed;
    }

    // case3 + case4
    if (!simulate(path_buf[0..path_len])) {
        std.debug.print("FAIL simulate\\n", .{});
        return error.TestFailed;
    }

    std.debug.print("PASS\\n", .{});
}
'''

T_DART = '''// 来源（blog）：@@BLOG@@
// @@HEAD@@

bool invalid(List<int> st) {
  final h = st[0], w = st[1], s = st[2], v = st[3];
  if (h != s && s == w) return true;
  if (h != s && s == v) return true;
  return false;
}

const roleIdx = {'W': 1, 'S': 2, 'V': 3};

List<String> solveFarmer() {
  final path = <String>[];
  final visited = <String>{};

  bool go(List<int> st) {
    if (st[0] == 1 && st[1] == 1 && st[2] == 1 && st[3] == 1) return true;
    final key = st.join(',');
    if (visited.contains(key)) return false;
    visited.add(key);
    for (final role in ['-', 'W', 'S', 'V']) {
      final ns = List<int>.from(st);
      ns[0] = 1 - ns[0]; // 农夫总是过河
      if (role != '-') {
        final idx = roleIdx[role]!;
        if (st[0] != st[idx]) continue; // 出发前同岸
        ns[idx] = 1 - ns[idx];
      }
      if (invalid(ns)) continue;
      if (go(ns)) {
        path.add(role);
        return true;
      }
    }
    return false;
  }

  go(<int>[0, 0, 0, 0]);
  return path.reversed.toList();
}

bool simulate(List<String> path) {
  final st = <int>[0, 0, 0, 0];
  for (final role in path) {
    final before = List<int>.from(st);
    st[0] = 1 - st[0];
    if (role != '-') {
      final idx = roleIdx[role]!;
      if (before[0] != before[idx]) return false;
      st[idx] = 1 - st[idx];
    }
    if (invalid(st)) return false;
  }
  return st[0] == 1 && st[1] == 1 && st[2] == 1 && st[3] == 1;
}

void main() {
  final wantPath = <String>['S', '-', 'W', 'S', 'V', '-', 'S'];
  final wantReadable = 'HS H HW HS HV H HS';

  final gotPath = solveFarmer();

  // case1: 路径一致
  if (gotPath.toString() != wantPath.toString()) {
    throw StateError('FAIL path mismatch: ' + gotPath.toString());
  }

  // case2: 可读方案串
  final gotReadable = gotPath.map((r) => r != '-' ? 'H' + r : 'H').join(' ');
  if (gotReadable != wantReadable) {
    throw StateError('FAIL readable: ' + gotReadable);
  }

  // case3: 7 步
  if (gotPath.length != 7) throw StateError('FAIL steps');

  // case4: 模拟校验
  if (!simulate(gotPath)) throw StateError('FAIL simulate');

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
        out = t.replace("@@BLOG@@", BLOG).replace("@@HEAD@@", HEAD).replace("@@WANT@@", WANT_LUA)
        emit(lang, REL + "/solution_1___1" + ext, out)

if __name__ == "__main__":
    main()
