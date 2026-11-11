#!/usr/bin/env python3
# gen_fix_n01.py — 补齐 notes/lc_107849059 gnome_sort+bubble_sort+贪心找零 × 7 语言
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from langlib import emit

BLOG = "来源（blog）：https://blog.csdn.net/tyro_java/article/details/107849059"
REL = "notes/lc_107849059_gnome_sort_bubble_sort以及贪心策略的相关对比改进"
HEAD = "%s\n%s"

T_RUST = HEAD + '''
fn gnome_sort(arr: &[i32]) -> Vec<i32> {
    let mut a = arr.to_vec();
    let mut i = 0usize;
    while i < a.len() {
        if i == 0 || a[i] >= a[i - 1] {
            i += 1;
        } else {
            a.swap(i - 1, i);
            i -= 1;
        }
    }
    a
}

fn bubble_sort(arr: &[i32]) -> Vec<i32> {
    let mut a = arr.to_vec();
    let mut swapped = true;
    while swapped {
        swapped = false;
        for i in 0..a.len().saturating_sub(1) {
            if a[i] > a[i + 1] {
                a.swap(i, i + 1);
                swapped = true;
            }
        }
    }
    a
}

fn coin_change(coins: &[i32], amount: i32) -> i32 {
    let mut cs = coins.to_vec();
    cs.sort_by(|x, y| y.cmp(x));
    let mut remaining = amount;
    let mut count = 0;
    for coin in cs {
        while remaining >= coin {
            remaining -= coin;
            count += 1;
        }
    }
    if remaining == 0 { count } else { -1 }
}

fn main() {
    assert_eq!(gnome_sort(&[3, 2, 1]), vec![1, 2, 3], "g");
    assert_eq!(bubble_sort(&[3, 2, 1]), vec![1, 2, 3], "b");
    assert_eq!(coin_change(&[1, 5, 10, 25], 63), 6, "c");
    println!("PASS");
}
'''

T_LUA = HEAD + '''
local function gnome_sort(arr)
    local a = {}
    for i, v in ipairs(arr) do a[i] = v end
    local i = 1
    while i <= #a do
        if i == 1 or a[i] >= a[i - 1] then
            i = i + 1
        else
            a[i - 1], a[i] = a[i], a[i - 1]
            i = i - 1
        end
    end
    return a
end

local function bubble_sort(arr)
    local a = {}
    for i, v in ipairs(arr) do a[i] = v end
    local swapped = true
    while swapped do
        swapped = false
        for i = 1, #a - 1 do
            if a[i] > a[i + 1] then
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = true
            end
        end
    end
    return a
end

local function coin_change(coins, amount)
    local cs = {}
    for i, v in ipairs(coins) do cs[i] = v end
    table.sort(cs, function(x, y) return x > y end)
    local remaining = amount
    local count = 0
    for _, coin in ipairs(cs) do
        while remaining >= coin do
            remaining = remaining - coin
            count = count + 1
        end
    end
    if remaining == 0 then return count else return -1 end
end

local function eq_arr(x, y)
    if #x ~= #y then return false end
    for i = 1, #x do if x[i] ~= y[i] then return false end end
    return true
end

assert(eq_arr(gnome_sort({3, 2, 1}), {1, 2, 3}), "g")
assert(eq_arr(bubble_sort({3, 2, 1}), {1, 2, 3}), "b")
assert(coin_change({1, 5, 10, 25}, 63) == 6, "c")
print("PASS")
'''

T_C = HEAD + '''
#include <stdio.h>

static void gnome_sort(int *a, int n) {
    int i = 0;
    while (i < n) {
        if (i == 0 || a[i] >= a[i - 1]) i++;
        else { int t = a[i - 1]; a[i - 1] = a[i]; a[i] = t; i--; }
    }
}

static void bubble_sort(int *a, int n) {
    int swapped = 1;
    while (swapped) {
        swapped = 0;
        for (int i = 0; i < n - 1; i++) {
            if (a[i] > a[i + 1]) { int t = a[i]; a[i] = a[i + 1]; a[i + 1] = t; swapped = 1; }
        }
    }
}

static int coin_change(const int *coins, int n, int amount) {
    int cs[64];
    for (int i = 0; i < n; i++) cs[i] = coins[i];
    for (int i = 0; i < n - 1; i++)
        for (int j = 0; j < n - 1 - i; j++)
            if (cs[j] < cs[j + 1]) { int t = cs[j]; cs[j] = cs[j + 1]; cs[j + 1] = t; }
    int remaining = amount, count = 0;
    for (int i = 0; i < n; i++)
        while (remaining >= cs[i]) { remaining -= cs[i]; count++; }
    return remaining == 0 ? count : -1;
}

static int eq_arr(const int *x, const int *y, int n) {
    for (int i = 0; i < n; i++) if (x[i] != y[i]) return 0;
    return 1;
}

int main(void) {
    int a[3] = {3, 2, 1};
    int want[3] = {1, 2, 3};
    gnome_sort(a, 3);
    if (!eq_arr(a, want, 3)) { printf("g failed\\n"); return 1; }
    int b[3] = {3, 2, 1};
    bubble_sort(b, 3);
    if (!eq_arr(b, want, 3)) { printf("b failed\\n"); return 1; }
    int coins[4] = {1, 5, 10, 25};
    if (coin_change(coins, 4, 63) != 6) { printf("c failed\\n"); return 1; }
    printf("PASS\\n");
    return 0;
}
'''

T_CPP = HEAD + '''
#include <algorithm>
#include <cassert>
#include <iostream>
#include <vector>

static void gnome_sort_inplace(std::vector<int> &a) {
    size_t i = 0;
    while (i < a.size()) {
        if (i == 0 || a[i] >= a[i - 1]) i++;
        else { std::swap(a[i - 1], a[i]); i--; }
    }
}

static void bubble_sort_inplace(std::vector<int> &a) {
    bool swapped = true;
    while (swapped) {
        swapped = false;
        for (size_t i = 0; i + 1 < a.size(); i++) {
            if (a[i] > a[i + 1]) { std::swap(a[i], a[i + 1]); swapped = true; }
        }
    }
}

static int coin_change(std::vector<int> coins, int amount) {
    std::sort(coins.begin(), coins.end(), std::greater<int>());
    int remaining = amount, count = 0;
    for (int coin : coins)
        while (remaining >= coin) { remaining -= coin; count++; }
    return remaining == 0 ? count : -1;
}

int main() {
    std::vector<int> a{3, 2, 1};
    gnome_sort_inplace(a);
    assert((a == std::vector<int>{1, 2, 3}));
    std::vector<int> b{3, 2, 1};
    bubble_sort_inplace(b);
    assert((b == std::vector<int>{1, 2, 3}));
    assert(coin_change({1, 5, 10, 25}, 63) == 6);
    std::cout << "PASS" << std::endl;
    return 0;
}
'''

T_R = HEAD + '''
gnome_sort <- function(arr) {
  a <- as.list(arr)
  i <- 1L
  n <- length(a)
  while (i <= n) {
    if (i == 1L || a[[i]] >= a[[i - 1L]]) {
      i <- i + 1L
    } else {
      tmp <- a[[i - 1L]]
      a[[i - 1L]] <- a[[i]]
      a[[i]] <- tmp
      i <- i - 1L
    }
  }
  as.integer(vapply(a, function(x) x, integer(1)))
}

bubble_sort <- function(arr) {
  a <- as.list(arr)
  n <- length(a)
  swapped <- TRUE
  while (swapped) {
    swapped <- FALSE
    for (i in 1:(n - 1L)) {
      if (a[[i]] > a[[i + 1L]]) {
        tmp <- a[[i]]
        a[[i]] <- a[[i + 1L]]
        a[[i + 1L]] <- tmp
        swapped <- TRUE
      }
    }
  }
  as.integer(vapply(a, function(x) x, integer(1)))
}

coin_change <- function(coins, amount) {
  cs <- sort(coins, decreasing = TRUE)
  remaining <- amount
  count <- 0L
  for (coin in cs) {
    while (remaining >= coin) {
      remaining <- remaining - coin
      count <- count + 1L
    }
  }
  if (remaining == 0) count else -1L
}

g <- gnome_sort(c(3L, 2L, 1L))
stopifnot(identical(as.integer(g), 1:3))
b <- bubble_sort(c(3L, 2L, 1L))
stopifnot(identical(as.integer(b), 1:3))
stopifnot(coin_change(c(1L, 5L, 10L, 25L), 63L) == 6L)
cat("PASS\\n")
'''

T_ZIG = HEAD + '''
const std = @import("std");

fn gnomeSort(a: []i32) void {
    var i: usize = 0;
    while (i < a.len) {
        if (i == 0 or a[i] >= a[i - 1]) {
            i += 1;
        } else {
            const t = a[i - 1];
            a[i - 1] = a[i];
            a[i] = t;
            i -= 1;
        }
    }
}

fn bubbleSort(a: []i32) void {
    var swapped = true;
    while (swapped) {
        swapped = false;
        var i: usize = 0;
        while (i + 1 < a.len) : (i += 1) {
            if (a[i] > a[i + 1]) {
                const t = a[i];
                a[i] = a[i + 1];
                a[i + 1] = t;
                swapped = true;
            }
        }
    }
}

fn coinChange(coins: []const i32, amount: i32) i32 {
    var cs: [64]i32 = undefined;
    var n: usize = 0;
    for (coins) |c| {
        cs[n] = c;
        n += 1;
    }
    // 降序冒泡
    var i: usize = 0;
    while (i + 1 < n) : (i += 1) {
        var j: usize = 0;
        while (j + 1 < n - i) : (j += 1) {
            if (cs[j] < cs[j + 1]) {
                const t = cs[j];
                cs[j] = cs[j + 1];
                cs[j + 1] = t;
            }
        }
    }
    var remaining = amount;
    var count: i32 = 0;
    for (cs[0..n]) |coin| {
        while (remaining >= coin) {
            remaining -= coin;
            count += 1;
        }
    }
    if (remaining == 0) return count;
    return -1;
}

pub fn main() !void {
    var gpa = std.heap.GeneralPurposeAllocator(.{}){};
    defer _ = gpa.deinit();
    const allocator = gpa.allocator();

    var g = [_]i32{ 3, 2, 1 };
    gnomeSort(&g);
    const want = [_]i32{ 1, 2, 3 };
    if (!std.mem.eql(i32, &g, &want)) return error.TestFailed;

    var b = [_]i32{ 3, 2, 1 };
    bubbleSort(&b);
    if (!std.mem.eql(i32, &b, &want)) return error.TestFailed;

    const coins = [_]i32{ 1, 5, 10, 25 };
    if (coinChange(&coins, 63) != 6) return error.TestFailed;

    _ = allocator;
    std.debug.print("PASS\\n", .{});
}
'''

T_DART = HEAD + '''
List<int> gnomeSort(List<int> arr) {
  final a = List<int>.from(arr);
  var i = 0;
  while (i < a.length) {
    if (i == 0 || a[i] >= a[i - 1]) {
      i++;
    } else {
      final t = a[i - 1];
      a[i - 1] = a[i];
      a[i] = t;
      i--;
    }
  }
  return a;
}

List<int> bubbleSort(List<int> arr) {
  final a = List<int>.from(arr);
  var swapped = true;
  while (swapped) {
    swapped = false;
    for (var i = 0; i < a.length - 1; i++) {
      if (a[i] > a[i + 1]) {
        final t = a[i];
        a[i] = a[i + 1];
        a[i + 1] = t;
        swapped = true;
      }
    }
  }
  return a;
}

int coinChange(List<int> coins, int amount) {
  final cs = List<int>.from(coins)..sort((x, y) => y.compareTo(x));
  var remaining = amount;
  var count = 0;
  for (final coin in cs) {
    while (remaining >= coin) {
      remaining -= coin;
      count++;
    }
  }
  return remaining == 0 ? count : -1;
}

void main() {
  final want = <int>[1, 2, 3];
  assert(gnomeSort([3, 2, 1]).toString() == want.toString(), 'g');
  assert(bubbleSort([3, 2, 1]).toString() == want.toString(), 'b');
  assert(coinChange([1, 5, 10, 25], 63) == 6, 'c');
  print('PASS');
}
'''

GENS = {"rust": T_RUST, "lua": T_LUA, "c": T_C, "cpp": T_CPP, "r": T_R, "zig": T_ZIG, "dart": T_DART}

def main():
    exts = {"rust": "rs", "lua": "lua", "c": "c", "cpp": "cpp", "r": "R", "zig": "zig", "dart": "dart"}
    prefix = {"rust": "// ", "lua": "-- ", "c": "// ", "cpp": "// ", "r": "# ", "zig": "// ", "dart": "// "}
    for lang, t in GENS.items():
        emit(lang, REL + "/solution_1___1." + exts[lang], t % (prefix[lang] + BLOG, prefix[lang] + "Gnome Sort（侏儒排序）+ Bubble Sort（冒泡排序）+ 贪心找零 对比"))

if __name__ == "__main__":
    main()
