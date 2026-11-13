#!/usr/bin/env python3
# gen_fix_n02.py — 补齐 notes/lc_98685358 农夫过河问题（BFS 最短路）× 7 语言
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from langlib import emit

REL = "notes/lc_98685358_数据结构与算法笔记_农夫过河问题python3实现"
BLOG = "来源（blog）：https://blog.csdn.net/tyro_java/article/details/98685358"
DESC = "农夫过河问题：BFS 求最短过河序列，状态 (农夫,狼,羊,菜)，0=左岸 1=右岸"

T_RUST = '''// @@BLOG@@
// LeetCode 98685358. 农夫过河问题 — Rust 版（@@DESC@@）
use std::collections::HashMap;

// 安全判定：狼与羊单独相处或羊与菜单独相处则不安全
fn is_safe(s: &[i32; 4]) -> bool {
    let (farmer, wolf, goat, cabbage) = (s[0], s[1], s[2], s[3]);
    if wolf == goat && farmer != wolf {
        return false;
    }
    if goat == cabbage && farmer != goat {
        return false;
    }
    true
}

fn key(s: &[i32; 4]) -> String {
    format!("{},{},{},{}", s[0], s[1], s[2], s[3])
}

fn solve() -> Option<Vec<[i32; 4]>> {
    let start = [0, 0, 0, 0];
    let goal = [1, 1, 1, 1];
    let mut prev: HashMap<String, Option<[i32; 4]>> = HashMap::new();
    prev.insert(key(&start), None);
    let mut q: Vec<[i32; 4]> = vec![start];
    let mut head = 0usize;
    while head < q.len() {
        let cur = q[head];
        head += 1;
        let cur_key = key(&cur);
        if cur == goal {
            let mut path: Vec<[i32; 4]> = vec![];
            let mut k: Option<[i32; 4]> = Some(cur);
            while let Some(s) = k {
                path.push(s);
                k = *prev.get(&key(&s)).unwrap();
            }
            path.reverse();
            return Some(path);
        }
        let farmer = cur[0];
        for i in 0..4usize {
            if i != 0 && cur[i] != farmer {
                continue;
            }
            let mut nxt = cur;
            nxt[0] = 1 - farmer;
            if i != 0 {
                nxt[i] = 1 - farmer;
            }
            let nk = key(&nxt);
            if prev.contains_key(&nk) {
                continue;
            }
            if !is_safe(&nxt) {
                continue;
            }
            prev.insert(nk, Some(cur));
            q.push(nxt);
        }
    }
    None
}

fn main() {
    let want: Vec<[i32; 4]> = vec![
        [0, 0, 0, 0],
        [1, 0, 1, 0],
        [0, 0, 1, 0],
        [1, 1, 1, 0],
        [0, 1, 0, 0],
        [1, 1, 0, 1],
        [0, 1, 0, 1],
        [1, 1, 1, 1],
    ];
    let path = solve().expect("FAILED: 无解");
    assert_eq!(path, want, "path mismatch");
    println!("PASS");
}
'''

T_LUA = '''-- @@BLOG@@
-- LeetCode 98685358. 农夫过河问题 — Lua 版（@@DESC@@）

local function is_safe(s)
    if s[2] == s[3] and s[1] ~= s[2] then return false end
    if s[3] == s[4] and s[1] ~= s[3] then return false end
    return true
end

local function key(s)
    return table.concat(s, ",")
end

local function solve()
    local start = {0, 0, 0, 0}
    local goal = {1, 1, 1, 1}
    local prev = {}        -- key -> 父 key（起点无父，缺省 nil）
    local state_by = {}    -- key -> 状态表
    prev[key(start)] = false
    state_by[key(start)] = start
    local q = {start}
    local head = 1
    while head <= #q do
        local cur = q[head]
        head = head + 1
        local ck = key(cur)
        if ck == key(goal) then
            local path = {}
            local k = ck
            while k and k ~= false do
                path[#path + 1] = state_by[k]
                k = prev[k]
            end
            -- 反转
            local n = #path
            for i = 1, math.floor(n / 2) do
                path[i], path[n - i + 1] = path[n - i + 1], path[i]
            end
            return path
        end
        local farmer = cur[1]
        for i = 1, 4 do
            if i == 1 or cur[i] == farmer then
                local nxt = {cur[1], cur[2], cur[3], cur[4]}
                nxt[1] = 1 - farmer
                if i ~= 1 then nxt[i] = 1 - farmer end
                local nk = key(nxt)
                if prev[nk] == nil then
                    if is_safe(nxt) then
                        prev[nk] = ck
                        state_by[nk] = nxt
                        q[#q + 1] = nxt
                    end
                end
            end
        end
    end
    return nil
end

local want = {
    {0, 0, 0, 0},
    {1, 0, 1, 0},
    {0, 0, 1, 0},
    {1, 1, 1, 0},
    {0, 1, 0, 0},
    {1, 1, 0, 1},
    {0, 1, 0, 1},
    {1, 1, 1, 1},
}
local path = solve()
assert(path ~= nil, "FAILED: 无解")
assert(#path == #want, "path length mismatch")
for i = 1, #want do
    for j = 1, 4 do
        assert(path[i][j] == want[i][j], "path mismatch at " .. i .. "," .. j)
    end
end
print("PASS")
'''

T_C = '''/* @@BLOG@@
 * LeetCode 98685358. 农夫过河问题 — C 版（@@DESC@@）
 * 状态编码为 4bit 整数：bit3=农夫 bit2=狼 bit1=羊 bit0=菜
 */
#include <stdio.h>

static int is_safe(int s) {
    int farmer = (s >> 3) & 1, wolf = (s >> 2) & 1, goat = (s >> 1) & 1, cabbage = s & 1;
    if (wolf == goat && farmer != wolf) return 0;
    if (goat == cabbage && farmer != goat) return 0;
    return 1;
}

static void dec(int s, int out[4]) {
    out[0] = (s >> 3) & 1; out[1] = (s >> 2) & 1; out[2] = (s >> 1) & 1; out[3] = s & 1;
}

static int enc(int v[4]) {
    return v[0] * 8 + v[1] * 4 + v[2] * 2 + v[3];
}

static int solve(int path[][4]) {
    int start = 0, goal = 15;
    int prev[16];
    for (int i = 0; i < 16; i++) prev[i] = -2;   /* -2 未访问, -1 起点 */
    int q[16], head = 0, tail = 0;
    prev[start] = -1;
    q[tail++] = start;
    while (head < tail) {
        int cur = q[head++];
        if (cur == goal) {
            int n = 0, tmp[16];
            int k = cur;
            while (k != -1) { tmp[n++] = k; k = prev[k]; }
            for (int i = 0; i < n; i++) dec(tmp[n - 1 - i], path[i]);
            return n;
        }
        int farmer = (cur >> 3) & 1;
        for (int i = 0; i < 4; i++) {
            if (i != 0 && ((cur >> (3 - i)) & 1) != farmer) continue;
            int v[4];
            dec(cur, v);
            v[0] = 1 - farmer;
            if (i != 0) v[i] = 1 - farmer;
            int nk = enc(v);
            if (prev[nk] != -2) continue;
            if (!is_safe(nk)) continue;
            prev[nk] = cur;
            q[tail++] = nk;
        }
    }
    return -1;
}

int main(void) {
    int want[8][4] = {
        {0, 0, 0, 0}, {1, 0, 1, 0}, {0, 0, 1, 0}, {1, 1, 1, 0},
        {0, 1, 0, 0}, {1, 1, 0, 1}, {0, 1, 0, 1}, {1, 1, 1, 1},
    };
    int path[16][4];
    int n = solve(path);
    if (n != 8) { printf("FAILED: path length %d\\n", n); return 1; }
    for (int i = 0; i < 8; i++)
        for (int j = 0; j < 4; j++)
            if (path[i][j] != want[i][j]) {
                printf("FAILED: mismatch at %d,%d\\n", i, j);
                return 1;
            }
    printf("PASS\\n");
    return 0;
}
'''

T_CPP = '''// @@BLOG@@
// LeetCode 98685358. 农夫过河问题 — C++ 版（@@DESC@@）
#include <iostream>
#include <map>
#include <vector>

static bool is_safe(const std::vector<int> &s) {
    if (s[1] == s[2] && s[0] != s[1]) return false;
    if (s[2] == s[3] && s[0] != s[2]) return false;
    return true;
}

static std::string key(const std::vector<int> &s) {
    std::string k;
    for (size_t i = 0; i < s.size(); ++i) {
        if (i) k += ",";
        k += std::to_string(s[i]);
    }
    return k;
}

static std::vector<std::vector<int>> solve() {
    std::vector<int> start{0, 0, 0, 0};
    std::vector<int> goal{1, 1, 1, 1};
    std::map<std::string, std::vector<int>> prev;   // key -> 父状态（空表表示起点）
    std::vector<std::vector<int>> q{start};
    prev[key(start)] = {};
    size_t head = 0;
    while (head < q.size()) {
        std::vector<int> cur = q[head++];
        std::string ck = key(cur);
        if (cur == goal) {
            std::vector<std::vector<int>> path;
            std::string k = ck;
            while (true) {
                path.push_back(k.empty() ? std::vector<int>{0, 0, 0, 0} : key_to_state(k));
                if (k.empty()) break;
                std::string pk = prev.at(k).empty() ? std::string() : key(prev.at(k));
                if (prev.at(k).empty()) { path.push_back({0, 0, 0, 0}); /* placeholder */ }
                k = pk;
            }
            // 上一段 reconstruct 复杂，改用 parent 指针数组，见下
            return path;
        }
    }
    return {};
}

int main() {
    std::cout << "PASS" << std::endl;
    return 0;
}
'''

# 上面 CPP 草稿过于绕，直接用简洁重写替换：
T_CPP = '''// @@BLOG@@
// LeetCode 98685358. 农夫过河问题 — C++ 版（@@DESC@@）
#include <iostream>
#include <map>
#include <vector>

static bool is_safe(const std::vector<int> &s) {
    if (s[1] == s[2] && s[0] != s[1]) return false;
    if (s[2] == s[3] && s[0] != s[2]) return false;
    return true;
}

static std::string key(const std::vector<int> &s) {
    std::string k;
    for (size_t i = 0; i < s.size(); ++i) {
        if (i) k += ",";
        k += std::to_string(s[i]);
    }
    return k;
}

static std::vector<std::vector<int>> solve() {
    std::vector<int> start{0, 0, 0, 0};
    std::vector<int> goal{1, 1, 1, 1};
    // prev: key -> (是否有父状态, 父key)
    std::map<std::string, std::pair<bool, std::string>> prev;
    prev[key(start)] = {false, ""};
    std::map<std::string, std::vector<int>> state_by;
    state_by[key(start)] = start;
    std::vector<std::vector<int>> q{start};
    size_t head = 0;
    while (head < q.size()) {
        std::vector<int> cur = q[head++];
        std::string ck = key(cur);
        if (cur == goal) {
            std::vector<std::vector<int>> path;
            std::string k = ck;
            while (true) {
                path.push_back(state_by.at(k));
                if (!prev.at(k).first) break;
                k = prev.at(k).second;
            }
            std::reverse(path.begin(), path.end());
            return path;
        }
        int farmer = cur[0];
        for (int i = 0; i < 4; ++i) {
            if (i != 0 && cur[i] != farmer) continue;
            std::vector<int> nxt = cur;
            nxt[0] = 1 - farmer;
            if (i != 0) nxt[i] = 1 - farmer;
            std::string nk = key(nxt);
            if (prev.count(nk)) continue;
            if (!is_safe(nxt)) continue;
            prev[nk] = {true, ck};
            state_by[nk] = nxt;
            q.push_back(nxt);
        }
    }
    return {};
}

int main() {
    std::vector<std::vector<int>> want = {
        {0, 0, 0, 0}, {1, 0, 1, 0}, {0, 0, 1, 0}, {1, 1, 1, 0},
        {0, 1, 0, 0}, {1, 1, 0, 1}, {0, 1, 0, 1}, {1, 1, 1, 1},
    };
    std::vector<std::vector<int>> path = solve();
    if (path.empty()) { std::cout << "FAILED: 无解" << std::endl; return 1; }
    if (path != want) { std::cout << "FAILED: path mismatch" << std::endl; return 1; }
    std::cout << "PASS" << std::endl;
    return 0;
}
'''

T_R = '''# @@BLOG@@
# LeetCode 98685358. 农夫过河问题 — R 版（@@DESC@@）

is_safe <- function(s) {
  if (s[2] == s[3] && s[1] != s[2]) return(FALSE)
  if (s[3] == s[4] && s[1] != s[3]) return(FALSE)
  TRUE
}

key_of <- function(s) paste(s, collapse = ",")

solve <- function() {
  start <- c(0L, 0L, 0L, 0L)
  goal <- c(1L, 1L, 1L, 1L)
  prev <- new.env(parent = emptyenv())   # key -> 父 key（起点为 NA）
  state_by <- new.env(parent = emptyenv())
  prev[[key_of(start)]] <- NA_character_
  state_by[[key_of(start)]] <- start
  q <- list(start)
  head <- 1L
  while (head <= length(q)) {
    cur <- q[[head]]
    head <- head + 1L
    ck <- key_of(cur)
    if (identical(ck, key_of(goal))) {
      path <- list()
      k <- ck
      while (!is.na(k)) {
        path[[length(path) + 1L]] <- state_by[[k]]
        k <- prev[[k]]
      }
      return(rev(path))
    }
    farmer <- cur[1]
    for (i in 1:4) {
      if (i != 1L && cur[i] != farmer) next
      nxt <- cur
      nxt[1] <- 1L - farmer
      if (i != 1L) nxt[i] <- 1L - farmer
      nk <- key_of(nxt)
      if (!is.null(prev[[nk]])) next
      if (!is_safe(nxt)) next
      prev[[nk]] <- ck
      state_by[[nk]] <- nxt
      q[[length(q) + 1L]] <- nxt
    }
  }
  NULL
}

want <- list(
  c(0L, 0L, 0L, 0L), c(1L, 0L, 1L, 0L), c(0L, 0L, 1L, 0L), c(1L, 1L, 1L, 0L),
  c(0L, 1L, 0L, 0L), c(1L, 1L, 0L, 1L), c(0L, 1L, 0L, 1L), c(1L, 1L, 1L, 1L)
)
path <- solve()
stopifnot(!is.null(path))
stopifnot(length(path) == length(want))
for (i in seq_along(want)) {
  stopifnot(identical(as.integer(path[[i]]), as.integer(want[[i]])))
}
cat("PASS\\n")
'''

T_ZIG = '''// @@BLOG@@
// LeetCode 98685358. 农夫过河问题 — Zig 版（@@DESC@@）
// 状态编码为 4bit：bit3=农夫 bit2=狼 bit1=羊 bit0=菜
const std = @import("std");

fn isSafe(s: u4) bool {
    const farmer: u1 = @truncate(s >> 3);
    const wolf: u1 = @truncate(s >> 2);
    const goat: u1 = @truncate(s >> 1);
    const cabbage: u1 = @truncate(s);
    if (wolf == goat and farmer != wolf) return false;
    if (goat == cabbage and farmer != goat) return false;
    return true;
}

fn dec(s: u4) [4]i32 {
    return .{
        @as(i32, @intCast((s >> 3) & 1)),
        @as(i32, @intCast((s >> 2) & 1)),
        @as(i32, @intCast((s >> 1) & 1)),
        @as(i32, @intCast(s & 1)),
    };
}

fn enc(v: [4]i32) u4 {
    return @intCast(v[0] * 8 + v[1] * 4 + v[2] * 2 + v[3]);
}

fn solve(path: *[16][4]i32) !usize {
    const start: u4 = 0;
    const goal: u4 = 15;
    var prev: [16]i8 = undefined;
    for (&prev) |*p| p.* = -2; // -2 未访问, -1 起点
    var q: [16]u4 = undefined;
    var head: usize = 0;
    var tail: usize = 0;
    prev[start] = -1;
    q[tail] = start;
    tail += 1;
    while (head < tail) {
        const cur = q[head];
        head += 1;
        if (cur == goal) {
            var n: usize = 0;
            var tmp: [16]u4 = undefined;
            var k: i16 = cur;
            while (k != -1) {
                tmp[n] = @intCast(k);
                n += 1;
                k = prev[@intCast(k)];
            }
            var i: usize = 0;
            while (i < n) : (i += 1) {
                path[i] = dec(tmp[n - 1 - i]);
            }
            return n;
        }
        const farmer: i32 = @intCast((cur >> 3) & 1);
        var i: usize = 0;
        while (i < 4) : (i += 1) {
            const bit: i32 = @intCast((cur >> @intCast(3 - i)) & 1);
            if (i != 0 and bit != farmer) continue;
            var v = dec(cur);
            v[0] = 1 - farmer;
            if (i != 0) v[i] = 1 - farmer;
            const nk = enc(v);
            if (prev[nk] != -2) continue;
            if (!isSafe(nk)) continue;
            prev[nk] = @intCast(cur);
            q[tail] = nk;
            tail += 1;
        }
    }
    return error.NoSolution;
}

pub fn main() !void {
    const want = [8][4]i32{
        .{ 0, 0, 0, 0 }, .{ 1, 0, 1, 0 }, .{ 0, 0, 1, 0 }, .{ 1, 1, 1, 0 },
        .{ 0, 1, 0, 0 }, .{ 1, 1, 0, 1 }, .{ 0, 1, 0, 1 }, .{ 1, 1, 1, 1 },
    };
    var path: [16][4]i32 = undefined;
    const n = solve(&path) catch {
        std.debug.print("FAILED: 无解\\n", .{});
        return error.NoSolution;
    };
    if (n != 8) {
        std.debug.print("FAILED: path length {d}\\n", .{n});
        return error.TestFailed;
    }
    for (want, 0..) |row, i| {
        for (row, 0..) |x, j| {
            if (path[i][j] != x) {
                std.debug.print("FAILED: mismatch at {d},{d}\\n", .{ i, j });
                return error.TestFailed;
            }
        }
    }
    std.debug.print("PASS\\n", .{});
}
'''

T_DART = '''// @@BLOG@@
// LeetCode 98685358. 农夫过河问题 — Dart 版（@@DESC@@）

bool isSafe(List<int> s) {
  if (s[1] == s[2] && s[0] != s[1]) return false;
  if (s[2] == s[3] && s[0] != s[2]) return false;
  return true;
}

String key(List<int> s) => s.join(',');

List<List<int>>? solve() {
  final start = <int>[0, 0, 0, 0];
  final goal = <int>[1, 1, 1, 1];
  final prev = <String, String?>{};      // key -> 父 key（起点为 null）
  final stateBy = <String, List<int>>{};
  prev[key(start)] = null;
  stateBy[key(start)] = start;
  final q = <List<int>>[start];
  var head = 0;
  while (head < q.length) {
    final cur = q[head++];
    final ck = key(cur);
    if (ck == key(goal)) {
      final path = <List<int>>[];
      String? k = ck;
      while (k != null) {
        path.add(stateBy[k]!);
        k = prev[k];
      }
      return path.reversed.toList();
    }
    final farmer = cur[0];
    for (var i = 0; i < 4; i++) {
      if (i != 0 && cur[i] != farmer) continue;
      final nxt = List<int>.from(cur);
      nxt[0] = 1 - farmer;
      if (i != 0) nxt[i] = 1 - farmer;
      final nk = key(nxt);
      if (prev.containsKey(nk)) continue;
      if (!isSafe(nxt)) continue;
      prev[nk] = ck;
      stateBy[nk] = nxt;
      q.add(nxt);
    }
  }
  return null;
}

void main() {
  final want = <List<int>>[
    <int>[0, 0, 0, 0],
    <int>[1, 0, 1, 0],
    <int>[0, 0, 1, 0],
    <int>[1, 1, 1, 0],
    <int>[0, 1, 0, 0],
    <int>[1, 1, 0, 1],
    <int>[0, 1, 0, 1],
    <int>[1, 1, 1, 1],
  ];
  final path = solve();
  if (path == null) throw StateError('FAILED: 无解');
  final ok = path.length == want.length &&
      List.generate(want.length, (i) => path[i].toString() == want[i].toString()).every((x) => x);
  if (!ok) throw StateError('FAILED: path mismatch');
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
