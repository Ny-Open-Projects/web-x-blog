#!/usr/bin/env python3
# gen_fix_n05.py — 补齐 notes/lc_107836586 Big-O 记号 × 7 语言
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from langlib import emit

REL = "notes/lc_107836586_big-o记号_数据结构与算法的关系以及几种基本的数据结构"
BLOG = "来源（blog）：https://blog.csdn.net/tyro_java/article/details/107836586"
DESC = "Big-O 记号：按最高次非零系数给出多项式复杂度分类"

T_RUST = '''// @@BLOG@@
// LeetCode 107836586. Big-O 记号 — Rust 版（@@DESC@@）

// coeffs[i] 为 n^i 的系数，返回最高次非零项对应的复杂度记号
fn classify(coeffs: &[i64]) -> String {
    for deg in (0..coeffs.len()).rev() {
        if coeffs[deg] != 0 {
            if deg > 1 {
                return format!("O(n^{})", deg);
            } else if deg == 1 {
                return "O(n)".to_string();
            } else {
                return "O(1)".to_string();
            }
        }
    }
    "O(1)".to_string()
}

fn main() {
    let cases: Vec<(Vec<i64>, &str)> = vec![
        (vec![1, 0, 0, 0], "O(1)"),
        (vec![0, 0, 0, 35], "O(n^3)"),
        (vec![0, 0, 1, 0], "O(n^2)"),
        (vec![0, 1, 0, 0], "O(n)"),
    ];
    for (idx, (c, want)) in cases.iter().enumerate() {
        let got = classify(c);
        assert_eq!(got, *want, "case {} failed", idx);
    }
    println!("PASS");
}
'''

T_LUA = '''-- @@BLOG@@
-- LeetCode 107836586. Big-O 记号 — Lua 版（@@DESC@@）
local function classify(coeffs)
    for deg = #coeffs, 1, -1 do
        if coeffs[deg] ~= 0 then
            local d = deg - 1  -- 转 0 基次数
            if d > 1 then
                return string.format("O(n^%d)", d)
            elseif d == 1 then
                return "O(n)"
            else
                return "O(1)"
            end
        end
    end
    return "O(1)"
end

local cases = {
    {{1, 0, 0, 0}, "O(1)"},
    {{0, 0, 0, 35}, "O(n^3)"},
    {{0, 0, 1, 0}, "O(n^2)"},
    {{0, 1, 0, 0}, "O(n)"},
}
for idx, c in ipairs(cases) do
    local got = classify(c[1])
    assert(got == c[2], string.format("case %d failed: got %s want %s", idx, got, c[2]))
end
print("PASS")
'''

T_C = '''/* @@BLOG@@
 * LeetCode 107836586. Big-O 记号 — C 版（@@DESC@@）
 */
#include <stdio.h>
#include <string.h>

/* coeffs[i] 为 n^i 的系数，deg_count 为个数 */
static void classify(const long long *coeffs, int deg_count, char *out, int out_size) {
    for (int deg = deg_count - 1; deg >= 0; deg--) {
        if (coeffs[deg] != 0) {
            if (deg > 1) snprintf(out, out_size, "O(n^%d)", deg);
            else if (deg == 1) snprintf(out, out_size, "O(n)");
            else snprintf(out, out_size, "O(1)");
            return;
        }
    }
    snprintf(out, out_size, "O(1)");
}

int main(void) {
    long long c0[4] = {1, 0, 0, 0};
    long long c1[4] = {0, 0, 0, 35};
    long long c2[4] = {0, 0, 1, 0};
    long long c3[4] = {0, 1, 0, 0};
    const char *wants[4] = {"O(1)", "O(n^3)", "O(n^2)", "O(n)"};
    long long *as[4] = {c0, c1, c2, c3};
    char got[32];
    for (int i = 0; i < 4; i++) {
        classify(as[i], 4, got, sizeof(got));
        if (strcmp(got, wants[i]) != 0) {
            printf("case %d failed: got %s want %s\\n", i, got, wants[i]);
            return 1;
        }
    }
    printf("PASS\\n");
    return 0;
}
'''

T_CPP = '''// @@BLOG@@
// LeetCode 107836586. Big-O 记号 — C++ 版（@@DESC@@）
#include <iostream>
#include <string>
#include <vector>

// coeffs[i] 为 n^i 的系数，返回最高次非零项对应的复杂度记号
static std::string classify(const std::vector<long long> &coeffs) {
    for (int deg = static_cast<int>(coeffs.size()) - 1; deg >= 0; --deg) {
        if (coeffs[deg] != 0) {
            if (deg > 1) return "O(n^" + std::to_string(deg) + ")";
            if (deg == 1) return "O(n)";
            return "O(1)";
        }
    }
    return "O(1)";
}

int main() {
    std::vector<std::pair<std::vector<long long>, std::string>> cases = {
        {{1, 0, 0, 0}, "O(1)"},
        {{0, 0, 0, 35}, "O(n^3)"},
        {{0, 0, 1, 0}, "O(n^2)"},
        {{0, 1, 0, 0}, "O(n)"},
    };
    for (size_t idx = 0; idx < cases.size(); ++idx) {
        std::string got = classify(cases[idx].first);
        if (got != cases[idx].second) {
            std::cout << "case " << idx << " failed: got " << got << " want " << cases[idx].second << std::endl;
            return 1;
        }
    }
    std::cout << "PASS" << std::endl;
    return 0;
}
'''

T_R = '''# @@BLOG@@
# LeetCode 107836586. Big-O 记号 — R 版（@@DESC@@）

# coeffs[i] 为 n^i 的系数（R 下标从 1 起），返回最高次非零项对应的复杂度记号
classify <- function(coeffs) {
  for (deg in length(coeffs):1) {
    if (coeffs[deg] != 0) {
      d <- deg - 1L  # 转 0 基次数
      if (d > 1L) return(sprintf("O(n^%d)", d))
      if (d == 1L) return("O(n)")
      return("O(1)")
    }
  }
  "O(1)"
}

cases <- list(
  list(c(1, 0, 0, 0), "O(1)"),
  list(c(0, 0, 0, 35), "O(n^3)"),
  list(c(0, 0, 1, 0), "O(n^2)"),
  list(c(0, 1, 0, 0), "O(n)")
)
for (idx in seq_along(cases)) {
  got <- classify(cases[[idx]][[1]])
  stopifnot(identical(got, cases[[idx]][[2]]))
}
cat("PASS\\n")
'''

T_ZIG = '''// @@BLOG@@
// LeetCode 107836586. Big-O 记号 — Zig 版（@@DESC@@）
const std = @import("std");

// coeffs[i] 为 n^i 的系数，返回最高次非零项对应的复杂度记号
fn classify(buf: []u8, coeffs: []const i64) ![]u8 {
    var deg: usize = coeffs.len;
    while (deg > 0) {
        deg -= 1;
        if (coeffs[deg] != 0) {
            if (deg > 1) {
                return std.fmt.bufPrint(buf, "O(n^{d})", .{deg});
            } else if (deg == 1) {
                return std.fmt.bufPrint(buf, "O(n)", .{});
            } else {
                return std.fmt.bufPrint(buf, "O(1)", .{});
            }
        }
    }
    return std.fmt.bufPrint(buf, "O(1)", .{});
}

pub fn main() !void {
    var buf: [32]u8 = undefined;
    const Case = struct { coeffs: []const i64, want: []const u8 };
    const cases = [_]Case{
        .{ .coeffs = &[_]i64{ 1, 0, 0, 0 }, .want = "O(1)" },
        .{ .coeffs = &[_]i64{ 0, 0, 0, 35 }, .want = "O(n^3)" },
        .{ .coeffs = &[_]i64{ 0, 0, 1, 0 }, .want = "O(n^2)" },
        .{ .coeffs = &[_]i64{ 0, 1, 0, 0 }, .want = "O(n)" },
    };
    for (cases, 0..) |c, idx| {
        const got = try classify(&buf, c.coeffs);
        if (!std.mem.eql(u8, got, c.want)) {
            std.debug.print("case {d} failed: got {s} want {s}\\n", .{ idx, got, c.want });
            return error.TestFailed;
        }
    }
    std.debug.print("PASS\\n", .{});
}
'''

T_DART = '''// @@BLOG@@
// LeetCode 107836586. Big-O 记号 — Dart 版（@@DESC@@）

// coeffs[i] 为 n^i 的系数，返回最高次非零项对应的复杂度记号
String classify(List<int> coeffs) {
  for (var deg = coeffs.length - 1; deg >= 0; deg--) {
    if (coeffs[deg] != 0) {
      if (deg > 1) return 'O(n^$deg)';
      if (deg == 1) return 'O(n)';
      return 'O(1)';
    }
  }
  return 'O(1)';
}

void main() {
  final cases = <List<int>, String>{
    [1, 0, 0, 0]: 'O(1)',
    [0, 0, 0, 35]: 'O(n^3)',
    [0, 0, 1, 0]: 'O(n^2)',
    [0, 1, 0, 0]: 'O(n)',
  };
  var idx = 0;
  cases.forEach((coeffs, want) {
    final got = classify(coeffs);
    if (got != want) throw StateError('case $idx failed: got $got want $want');
    idx++;
  });
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
BASE = "solution_1_主解法"

def main():
    for lang, (t, ext) in GENS.items():
        out = t.replace("@@BLOG@@", BLOG).replace("@@DESC@@", DESC)
        emit(lang, REL + "/" + BASE + ext, out)

if __name__ == "__main__":
    main()
