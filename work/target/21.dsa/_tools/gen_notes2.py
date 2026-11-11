#!/usr/bin/env python3
# gen_notes2.py — notes 第二批：计数/基数/桶/希尔/堆排序 + 复杂度笔记 × 7语言
import sys, os; sys.path.insert(0, "/Users/Wang/Code/github/web-x-blog/work/target/21.dsa/_tools")
from langlib import emit, head_comment, EXT

LANGNAME = {"rust": "Rust", "lua": "Lua", "c": "C", "cpp": "C++", "r": "R", "zig": "Zig", "dart": "Dart"}

COUNT = {
"rust":'''fn count_sort(nums: Vec<i32>) -> Vec<i32> {
    if nums.is_empty() { return nums; }
    let (mut mx, mut mn) = (nums[0], nums[0]);
    for &v in &nums { if v > mx { mx = v; } if v < mn { mn = v; } }
    let range = (mx - mn + 1) as usize;
    let mut count = vec![0i32; range];
    let mut output = vec![0i32; nums.len()];
    for &v in &nums { count[(v - mn) as usize] += 1; }
    for i in 1..range { count[i] += count[i - 1]; }
    for i in (0..nums.len()).rev() {
        let idx = (nums[i] - mn) as usize;
        output[(count[idx] - 1) as usize] = nums[i];
        count[idx] -= 1;
    }
    output
}
fn main() {
    assert_eq!(count_sort(vec![5,3,8,3,1]), vec![1,3,3,5,8]);
    let big = vec![102,103,108,107,101,102,102,102,107,103,109,108,102,101,104,102,104,106,109,102];
    let got = count_sort(big);
    for i in 1..got.len() { assert!(got[i - 1] <= got[i]); }
    assert_eq!(got.len(), 20);
    println!("PASS"); }''',
"lua":'''local function count_sort(nums)
    if #nums == 0 then return nums end
    local mx, mn = nums[1], nums[1]
    for _, v in ipairs(nums) do
        if v > mx then mx = v end
        if v < mn then mn = v end
    end
    local range = mx - mn + 1
    local count = {}
    for i = 1, range do count[i] = 0 end
    for _, v in ipairs(nums) do count[v - mn + 1] = count[v - mn + 1] + 1 end
    for i = 2, range do count[i] = count[i] + count[i - 1] end
    local output = {}
    for i = #nums, 1, -1 do
        local idx = nums[i] - mn + 1
        output[count[idx]] = nums[i]
        count[idx] = count[idx] - 1
    end
    return output
end
assert(table.concat(count_sort({5,3,8,3,1}), ",") == "1,3,3,5,8")
local big = count_sort({102,103,108,107,101,102,102,102,107,103,109,108,102,101,104,102,104,106,109,102})
assert(#big == 20 and big[1] == 101 and big[20] == 109)
print("PASS")''',
"c":'''#include <stdio.h>
static void count_sort(int v[], int n) {
    if (n == 0) return;
    int mx = v[0], mn = v[0];
    for (int i = 1; i < n; i++) { if (v[i] > mx) mx = v[i]; if (v[i] < mn) mn = v[i]; }
    int range = mx - mn + 1;
    int count[65536] = {0};
    for (int i = 0; i < n; i++) count[v[i] - mn]++;
    for (int i = 1; i < range; i++) count[i] += count[i - 1];
    int output[4096];
    for (int i = n - 1; i >= 0; i--) {
        output[count[v[i] - mn] - 1] = v[i];
        count[v[i] - mn]--;
    }
    for (int i = 0; i < n; i++) v[i] = output[i];
}
int main(void) {
    int v1[] = {5,3,8,3,1};
    count_sort(v1, 5);
    int w1[] = {1,3,3,5,8};
    for (int i = 0; i < 5; i++) if (v1[i] != w1[i]) { printf("FAIL 1\\n"); return 1; }
    printf("PASS\\n"); return 0; }''',
"cpp":'''#include <cassert>
#include <iostream>
#include <vector>
static std::vector<int> countSort(const std::vector<int> &nums) {
    if (nums.empty()) return nums;
    int mx = nums[0], mn = nums[0];
    for (int v : nums) { mx = std::max(mx, v); mn = std::min(mn, v); }
    int range = mx - mn + 1;
    std::vector<int> count(range, 0), output(nums.size());
    for (int v : nums) count[v - mn]++;
    for (int i = 1; i < range; ++i) count[i] += count[i - 1];
    for (int i = static_cast<int>(nums.size()) - 1; i >= 0; --i) {
        output[--count[nums[i] - mn]] = nums[i];
    }
    return output;
}
int main() {
    assert((countSort({5,3,8,3,1}) == std::vector<int>{1,3,3,5,8}));
    auto big = countSort({102,103,108,107,101,102,102,102,107,103,109,108,102,101,104,102,104,106,109,102});
    assert(big.size() == 20 && big.front() == 101 && big.back() == 109);
    std::cout << "PASS" << std::endl; }''',
"r":'''count_sort <- function(nums) {
  if (length(nums) == 0) return(nums)
  mx <- max(nums); mn <- min(nums)
  range_ <- mx - mn + 1L
  count <- rep(0L, range_)
  for (v in nums) count[v - mn + 1L] <- count[v - mn + 1L] + 1L
  for (i in 2:range_) count[i] <- count[i] + count[i - 1L]
  output <- integer(length(nums))
  for (i in length(nums):1) {
    idx <- nums[i] - mn + 1L
    output[count[idx]] <- nums[i]
    count[idx] <- count[idx] - 1L
  }
  output
}
stopifnot(identical(as.integer(count_sort(c(5, 3, 8, 3, 1))), c(1L, 3L, 3L, 5L, 8L)))
big <- count_sort(c(102,103,108,107,101,102,102,102,107,103,109,108,102,101,104,102,104,106,109,102))
stopifnot(length(big) == 20, as.integer(big[1]) == 101, as.integer(big[20]) == 109)
cat("PASS\\n")''',
"zig":'''const std = @import("std");
fn countSort(nums: []i32, alloc: std.mem.Allocator) []i32 {
    if (nums.len == 0) return nums;
    var mx = nums[0];
    var mn = nums[0];
    for (nums) |v| {
        if (v > mx) mx = v;
        if (v < mn) mn = v;
    }
    const range: usize = @intCast(mx - mn + 1);
    var count = alloc.alloc(i32, range) catch unreachable;
    var output = alloc.alloc(i32, nums.len) catch unreachable;
    for (0..range) |i| count[i] = 0;
    for (nums) |v| count[@intCast(v - mn)] += 1;
    for (1..range) |i| count[i] += count[i - 1];
    var i: usize = nums.len;
    while (i > 0) {
        i -= 1;
        const idx: usize = @intCast(nums[i] - mn);
        count[idx] -= 1;
        output[@intCast(count[idx])] = nums[i];
    }
    return output;
}
pub fn main() !void {
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();
    const alloc = arena.allocator();
    var v1 = [_]i32{ 5, 3, 8, 3, 1 };
    const got = countSort(&v1, alloc);
    const want = [_]i32{ 1, 3, 3, 5, 8 };
    for (want, 0..) |w, i| if (got[i] != w) return error.TestFailed;
    std.debug.print("PASS\\n", .{}); }''',
"dart":'''List<int> countSort(List<int> nums) {
  if (nums.isEmpty) return nums;
  var mx = nums[0], mn = nums[0];
  for (final v in nums) { if (v > mx) mx = v; if (v < mn) mn = v; }
  final range = mx - mn + 1;
  final count = List<int>.filled(range, 0);
  final output = List<int>.filled(nums.length, 0);
  for (final v in nums) { count[v - mn]++; }
  for (var i = 1; i < range; i++) { count[i] += count[i - 1]; }
  for (var i = nums.length - 1; i >= 0; i--) {
    output[count[nums[i] - mn] - 1] = nums[i];
    count[nums[i] - mn]--;
  }
  return output;
}
void main() {
  if (countSort([5,3,8,3,1]).toString() != '[1, 3, 3, 5, 8]') throw StateError('c1');
  final big = countSort([102,103,108,107,101,102,102,102,107,103,109,108,102,101,104,102,104,106,109,102]);
  if (big.length != 20 || big.first != 101 || big.last != 109) throw StateError('c2');
  print('PASS'); }''',
}

RADIX = {
"rust":'''fn radix_sort(nums: Vec<i32>) -> Vec<i32> {
    if nums.is_empty() { return nums; }
    let (mut mn, mut mx) = (nums[0], nums[0]);
    for &v in &nums { if v < mn { mn = v; } if v > mx { mx = v; } }
    let offset = if mn < 0 { -mn } else { 0 };
    let mut adj: Vec<i64> = nums.iter().map(|&x| (x + offset) as i64).collect();
    let mut max_adj: i64 = adj[0];
    for &x in &adj { if x > max_adj { max_adj = x; } }
    let mut radix: i64 = 1;
    let mut tmp = vec![0i64; adj.len()];
    while max_adj >= radix {
        let mut bucket = [0i64; 10];
        for &x in &adj { bucket[((x / radix) % 10) as usize] += 1; }
        for i in 1..10 { bucket[i] += bucket[i - 1]; }
        for i in (0..adj.len()).rev() {
            let d = ((adj[i] / radix) % 10) as usize;
            bucket[d] -= 1;
            tmp[bucket[d] as usize] = adj[i];
        }
        adj.copy_from_slice(&tmp);
        radix *= 10;
    }
    adj.into_iter().map(|x| (x - offset as i64) as i32).collect()
}
fn main() {
    assert_eq!(radix_sort(vec![1,2,3]), vec![1,2,3]);
    assert_eq!(radix_sort(vec![5,4,3,2,1]), vec![1,2,3,4,5]);
    assert_eq!(radix_sort(vec![3,1,4,1,5,9,2,6,5,3,5]), vec![1,1,2,3,3,4,5,5,5,6,9]);
    println!("PASS"); }''',
"lua":'''local function radix_sort(nums)
    if #nums == 0 then return nums end
    local mn, mx = nums[1], nums[1]
    for _, v in ipairs(nums) do
        if v < mn then mn = v end
        if v > mx then mx = v end
    end
    local offset = mn < 0 and -mn or 0
    local adj = {}
    for i, v in ipairs(nums) do adj[i] = v + offset end
    local max_adj = adj[1]
    for _, v in ipairs(adj) do if v > max_adj then max_adj = v end end
    local radix = 1
    local tmp = {}
    while max_adj >= radix do
        local bucket = {}
        for i = 0, 9 do bucket[i] = 0 end
        for _, v in ipairs(adj) do
            local d = math.floor(v / radix) % 10
            bucket[d] = bucket[d] + 1
        end
        for i = 1, 9 do bucket[i] = bucket[i] + bucket[i - 1] end
        for i = #adj, 1, -1 do
            local d = math.floor(adj[i] / radix) % 10
            tmp[bucket[d]] = adj[i]
            bucket[d] = bucket[d] - 1
        end
        for i = 1, #adj do adj[i] = tmp[i] end
        radix = radix * 10
    end
    for i, v in ipairs(adj) do adj[i] = v - offset end
    return adj
end
assert(table.concat(radix_sort({1,2,3}), ",") == "1,2,3")
assert(table.concat(radix_sort({5,4,3,2,1}), ",") == "1,2,3,4,5")
assert(table.concat(radix_sort({3,1,4,1,5,9,2,6,5,3,5}), ",") == "1,1,2,3,3,4,5,5,5,6,9")
print("PASS")''',
"c":'''#include <stdio.h>
static void radix_sort(int v[], int n) {
    if (n == 0) return;
    int mn = v[0], mx = v[0];
    for (int i = 1; i < n; i++) { if (v[i] < mn) mn = v[i]; if (v[i] > mx) mx = v[i]; }
    int offset = mn < 0 ? -mn : 0;
    long adj[4096];
    long max_adj = 0;
    for (int i = 0; i < n; i++) { adj[i] = v[i] + offset; if (adj[i] > max_adj) max_adj = adj[i]; }
    long radix = 1;
    long tmp[4096];
    while (max_adj >= radix) {
        long bucket[10] = {0};
        for (int i = 0; i < n; i++) bucket[(adj[i] / radix) % 10]++;
        for (int i = 1; i < 10; i++) bucket[i] += bucket[i - 1];
        for (int i = n - 1; i >= 0; i--) {
            int d = (int)((adj[i] / radix) % 10);
            tmp[--bucket[d]] = adj[i];
        }
        for (int i = 0; i < n; i++) adj[i] = tmp[i];
        radix *= 10;
    }
    for (int i = 0; i < n; i++) v[i] = (int)(adj[i] - offset);
}
int main(void) {
    int v1[] = {5,4,3,2,1};
    radix_sort(v1, 5);
    for (int i = 0; i < 5; i++) if (v1[i] != i + 1) { printf("FAIL\\n"); return 1; }
    printf("PASS\\n"); return 0; }''',
"cpp":'''#include <cassert>
#include <iostream>
#include <vector>
static std::vector<int> radixSort(const std::vector<int> &nums) {
    if (nums.empty()) return nums;
    int mn = nums[0], mx = nums[0];
    for (int v : nums) { mn = std::min(mn, v); mx = std::max(mx, v); }
    int offset = mn < 0 ? -mn : 0;
    std::vector<long long> adj;
    long long maxAdj = 0;
    for (int v : nums) { adj.push_back(v + offset); maxAdj = std::max(maxAdj, static_cast<long long>(v) + offset); }
    long long radix = 1;
    std::vector<long long> tmp(nums.size());
    while (maxAdj >= radix) {
        long long bucket[10] = {0};
        for (auto x : adj) bucket[(x / radix) % 10]++;
        for (int i = 1; i < 10; ++i) bucket[i] += bucket[i - 1];
        for (int i = static_cast<int>(adj.size()) - 1; i >= 0; --i) {
            tmp[--bucket[(adj[i] / radix) % 10]] = adj[i];
        }
        adj = tmp;
        radix *= 10;
    }
    std::vector<int> out;
    for (auto x : adj) out.push_back(static_cast<int>(x - offset));
    return out;
}
int main() {
    assert((radixSort({5,4,3,2,1}) == std::vector<int>{1,2,3,4,5}));
    assert((radixSort({3,1,4,1,5,9,2,6,5,3,5}) == std::vector<int>{1,1,2,3,3,4,5,5,5,6,9}));
    std::cout << "PASS" << std::endl; }''',
"r":'''radix_sort <- function(nums) {
  if (length(nums) == 0) return(nums)
  mn <- min(nums); mx <- max(nums)
  offset <- if (mn < 0) -mn else 0
  adj <- as.numeric(nums) + offset
  max_adj <- max(adj)
  radix <- 1
  tmp <- numeric(length(adj))
  while (max_adj >= radix) {
    bucket <- rep(0, 10)
    for (v in adj) {
      d <- floor(v / radix) %% 10
      bucket[d + 1] <- bucket[d + 1] + 1
    }
    for (i in 2:10) bucket[i] <- bucket[i] + bucket[i - 1]
    for (i in length(adj):1) {
      d <- floor(adj[i] / radix) %% 10
      tmp[bucket[d + 1]] <- adj[i]
      bucket[d + 1] <- bucket[d + 1] - 1
    }
    for (i in seq_along(adj)) adj[i] <- tmp[i]
    radix <- radix * 10
  }
  as.integer(adj - offset)
}
stopifnot(identical(radix_sort(c(5, 4, 3, 2, 1)), 1:5))
stopifnot(identical(radix_sort(c(3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5)), c(1L, 1L, 2L, 3L, 3L, 4L, 5L, 5L, 5L, 6L, 9L)))
cat("PASS\\n")''',
"zig":'''const std = @import("std");
fn radixSort(nums: []i32, alloc: std.mem.Allocator) []i32 {
    if (nums.len == 0) return nums;
    var mn = nums[0];
    var mx = nums[0];
    for (nums) |v| {
        if (v < mn) mn = v;
        if (v > mx) mx = v;
    }
    const offset: i64 = if (mn < 0) -mn else 0;
    var adj = alloc.alloc(i64, nums.len) catch unreachable;
    var max_adj: i64 = 0;
    for (nums, 0..) |v, i| {
        adj[i] = @as(i64, v) + offset;
        if (adj[i] > max_adj) max_adj = adj[i];
    }
    var radix: i64 = 1;
    var tmp = alloc.alloc(i64, nums.len) catch unreachable;
    while (max_adj >= radix) {
        var bucket = [_]i64{0} ** 10;
        for (adj) |x| bucket[@intCast(@mod(@divTrunc(x, radix), 10))] += 1;
        for (1..10) |i| bucket[i] += bucket[i - 1];
        var i: usize = nums.len;
        while (i > 0) {
            i -= 1;
            const d: usize = @intCast(@mod(@divTrunc(adj[i], radix), 10));
            bucket[d] -= 1;
            tmp[@intCast(bucket[d])] = adj[i];
        }
        for (0..nums.len) |k| adj[k] = tmp[k];
        radix *= 10;
    }
    const out = alloc.alloc(i32, nums.len) catch unreachable;
    for (adj, 0..) |x, i| out[i] = @intCast(x - offset);
    return out;
}
pub fn main() !void {
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();
    var v1 = [_]i32{ 5, 4, 3, 2, 1 };
    const got = radixSort(&v1, arena.allocator());
    for (got, 0..) |g, i| if (g != @as(i32, @intCast(i + 1))) return error.TestFailed;
    std.debug.print("PASS\\n", .{}); }''',
"dart":'''List<int> radixSort(List<int> nums) {
  if (nums.isEmpty) return nums;
  var mn = nums[0], mx = nums[0];
  for (final v in nums) { if (v < mn) mn = v; if (v > mx) mx = v; }
  final offset = mn < 0 ? -mn : 0;
  final adj = nums.map((v) => v + offset).toList();
  var maxAdj = adj[0];
  for (final v in adj) { if (v > maxAdj) maxAdj = v; }
  var radix = 1;
  final tmp = List<int>.filled(adj.length, 0);
  while (maxAdj >= radix) {
    final bucket = List<int>.filled(10, 0);
    for (final v in adj) { bucket[(v ~/ radix) % 10]++; }
    for (var i = 1; i < 10; i++) { bucket[i] += bucket[i - 1]; }
    for (var i = adj.length - 1; i >= 0; i--) {
      tmp[--bucket[(adj[i] ~/ radix) % 10]] = adj[i];
    }
    for (var i = 0; i < adj.length; i++) { adj[i] = tmp[i]; }
    radix *= 10;
  }
  return adj.map((x) => x - offset).toList();
}
void main() {
  if (radixSort([5,4,3,2,1]).toString() != '[1, 2, 3, 4, 5]') throw StateError('c1');
  if (radixSort([3,1,4,1,5,9,2,6,5,3,5]).toString() != '[1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]') throw StateError('c2');
  print('PASS'); }''',
}

SHELL = {
"rust":'''fn shell_sort(nums: Vec<i32>) -> Vec<i32> {
    let mut v = nums;
    let n = v.len();
    let mut gap = n / 2;
    while gap > 0 {
        for i in gap..n {
            let key = v[i];
            let mut j = i;
            while j >= gap && v[j - gap] > key { v[j] = v[j - gap]; j -= gap; }
            v[j] = key;
        }
        gap /= 2;
    }
    v
}
fn main() {
    assert_eq!(shell_sort(vec![5,2,4,6,1,3]), vec![1,2,3,4,5,6]);
    assert_eq!(shell_sort(vec![9,8,7,6,5,4,3,2,1]), vec![1,2,3,4,5,6,7,8,9]);
    println!("PASS"); }''',
"lua":'''local function shell_sort(nums)
    local v = {table.unpack(nums)}
    local n = #v
    local gap = n // 2
    while gap > 0 do
        for i = gap + 1, n do
            local key = v[i]
            local j = i - gap
            while j >= 1 and v[j] > key do v[j + gap] = v[j]; j = j - gap end
            v[j + gap] = key
        end
        gap = gap // 2
    end
    return v
end
assert(table.concat(shell_sort({5,2,4,6,1,3}), ",") == "1,2,3,4,5,6")
assert(table.concat(shell_sort({9,8,7,6,5,4,3,2,1}), ",") == "1,2,3,4,5,6,7,8,9")
print("PASS")''',
"c":'''#include <stdio.h>
static void shell_sort(int v[], int n) {
    for (int gap = n / 2; gap > 0; gap /= 2) {
        for (int i = gap; i < n; i++) {
            int key = v[i];
            int j = i - gap;
            while (j >= 0 && v[j] > key) { v[j + gap] = v[j]; j -= gap; }
            v[j + gap] = key;
        }
    }
}
int main(void) {
    int v1[] = {5,2,4,6,1,3};
    shell_sort(v1, 6);
    for (int i = 0; i < 6; i++) if (v1[i] != i + 1) { printf("FAIL\\n"); return 1; }
    printf("PASS\\n"); return 0; }''',
"cpp":'''#include <cassert>
#include <iostream>
#include <vector>
static std::vector<int> shellSort(std::vector<int> v) {
    size_t n = v.size();
    for (size_t gap = n / 2; gap > 0; gap /= 2) {
        for (size_t i = gap; i < n; ++i) {
            int key = v[i];
            size_t j = i;
            while (j >= gap && v[j - gap] > key) { v[j] = v[j - gap]; j -= gap; }
            v[j] = key;
        }
    }
    return v;
}
int main() { assert((shellSort({5,2,4,6,1,3}) == std::vector<int>{1,2,3,4,5,6})); std::cout << "PASS" << std::endl; }''',
"r":'''shell_sort <- function(nums) {
  v <- nums
  n <- length(v)
  gap <- n %/% 2
  while (gap > 0) {
    for (i in (gap + 1):n) {
      key <- v[i]
      j <- i - gap
      while (j >= 1 && v[j] > key) { v[j + gap] <- v[j]; j <- j - gap }
      v[j + gap] <- key
    }
    gap <- gap %/% 2
  }
  v
}
stopifnot(identical(as.integer(shell_sort(c(5, 2, 4, 6, 1, 3))), 1:6))
stopifnot(identical(as.integer(shell_sort(c(9, 8, 7, 6, 5, 4, 3, 2, 1))), 1:9))
cat("PASS\\n")''',
"zig":'''const std = @import("std");
fn shellSort(nums: []i32) void {
    const n = nums.len;
    var gap = n / 2;
    while (gap > 0) : (gap /= 2) {
        for (gap..n) |i| {
            const key = nums[i];
            var j = i;
            while (j >= gap and nums[j - gap] > key) {
                nums[j] = nums[j - gap];
                j -= gap;
            }
            nums[j] = key;
        }
    }
}
pub fn main() !void {
    var v1 = [_]i32{ 5, 2, 4, 6, 1, 3 };
    shellSort(&v1);
    for (v1, 0..) |v, i| if (v != @as(i32, @intCast(i + 1))) return error.TestFailed;
    std.debug.print("PASS\\n", .{}); }''',
"dart":'''List<int> shellSort(List<int> nums) {
  final v = List<int>.from(nums);
  var gap = v.length ~/ 2;
  while (gap > 0) {
    for (var i = gap; i < v.length; i++) {
      final key = v[i];
      var j = i - gap;
      while (j >= 0 && v[j] > key) { v[j + gap] = v[j]; j -= gap; }
      v[j + gap] = key;
    }
    gap ~/= 2;
  }
  return v;
}
void main() { if (shellSort([5,2,4,6,1,3]).toString() != '[1, 2, 3, 4, 5, 6]') throw StateError('c1'); print('PASS'); }''',
}

HEAPSORT = {
"rust":'''fn heap_sort(nums: Vec<i32>) -> Vec<i32> {
    let mut v = nums;
    let n = v.len();
    fn sift(v: &mut Vec<i32>, start: usize, end: usize) {
        let mut root = start;
        loop {
            let child = 2 * root + 1;
            if child > end { break; }
            let mut swap = root;
            if v[swap] < v[child] { swap = child; }
            if child + 1 <= end && v[swap] < v[child + 1] { swap = child + 1; }
            if swap == root { break; }
            v.swap(root, swap);
            root = swap;
        }
    }
    for i in (0..n / 2).rev() { sift(&mut v, i, n - 1); }
    for end in (1..n).rev() {
        v.swap(0, end);
        sift(&mut v, 0, end - 1);
    }
    v
}
fn main() {
    assert_eq!(heap_sort(vec![5,2,4,6,1,3]), vec![1,2,3,4,5,6]);
    assert_eq!(heap_sort(vec![9,8,7,6,5]), vec![5,6,7,8,9]);
    println!("PASS"); }''',
"lua":'''local function heap_sort(nums)
    local v = {table.unpack(nums)}
    local n = #v
    local function sift(start, end_)
        local root = start
        while true do
            local child = 2 * root
            if child > end_ then break end
            local swap = root
            if v[swap] < v[child] then swap = child end
            if child + 1 <= end_ and v[swap] < v[child + 1] then swap = child + 1 end
            if swap == root then break end
            v[root], v[swap] = v[swap], v[root]
            root = swap
        end
    end
    for i = n // 2, 1, -1 do sift(i, n) end
    for end_ = n, 2, -1 do
        v[1], v[end_] = v[end_], v[1]
        sift(1, end_ - 1)
    end
    return v
end
assert(table.concat(heap_sort({5,2,4,6,1,3}), ",") == "1,2,3,4,5,6")
assert(table.concat(heap_sort({9,8,7,6,5}), ",") == "5,6,7,8,9")
print("PASS")''',
"c":'''#include <stdio.h>
static void sift(int v[], int start, int end) {
    int root = start;
    while (1) {
        int child = 2 * root + 1;
        if (child > end) break;
        int swap = root;
        if (v[swap] < v[child]) swap = child;
        if (child + 1 <= end && v[swap] < v[child + 1]) swap = child + 1;
        if (swap == root) break;
        int t = v[root]; v[root] = v[swap]; v[swap] = t;
        root = swap;
    }
}
static void heap_sort(int v[], int n) {
    for (int i = n / 2 - 1; i >= 0; i--) sift(v, i, n - 1);
    for (int end = n - 1; end >= 1; end--) {
        int t = v[0]; v[0] = v[end]; v[end] = t;
        sift(v, 0, end - 1);
    }
}
int main(void) {
    int v1[] = {5,2,4,6,1,3};
    heap_sort(v1, 6);
    for (int i = 0; i < 6; i++) if (v1[i] != i + 1) { printf("FAIL\\n"); return 1; }
    printf("PASS\\n"); return 0; }''',
"cpp":'''#include <cassert>
#include <iostream>
#include <vector>
static void sift(std::vector<int> &v, size_t start, size_t end) {
    size_t root = start;
    while (true) {
        size_t child = 2 * root + 1;
        if (child > end) break;
        size_t swap = root;
        if (v[swap] < v[child]) swap = child;
        if (child + 1 <= end && v[swap] < v[child + 1]) swap = child + 1;
        if (swap == root) break;
        std::swap(v[root], v[swap]);
        root = swap;
    }
}
static std::vector<int> heapSort(std::vector<int> v) {
    if (v.empty()) return v;
    size_t n = v.size();
    for (size_t i = n / 2; i > 0; --i) sift(v, i - 1, n - 1);
    for (size_t end = n; end > 1; --end) {
        std::swap(v[0], v[end - 1]);
        sift(v, 0, end - 2);
    }
    return v;
}
int main() {
    assert((heapSort({5,2,4,6,1,3}) == std::vector<int>{1,2,3,4,5,6}));
    assert((heapSort({9,8,7,6,5}) == std::vector<int>{5,6,7,8,9}));
    std::cout << "PASS" << std::endl; }''',
"r":'''heap_sort <- function(nums) {
  e <- new.env(parent = emptyenv())
  e$v <- nums
  n <- length(nums)
  sift <- function(start, end_) {
    root <- start
    while (TRUE) {
      child <- 2L * root
      if (child > end_) break
      swap <- root
      if (e$v[swap] < e$v[child]) swap <- child
      if (child + 1L <= end_ && e$v[swap] < e$v[child + 1L]) swap <- child + 1L
      if (swap == root) break
      t <- e$v[root]
      e$v[root] <- e$v[swap]
      e$v[swap] <- t
      root <- swap
    }
  }
  if (n >= 2) {
    for (i in (n %/% 2L):1) sift(i, n)
    for (end_ in n:2) {
      t <- e$v[1]
      e$v[1] <- e$v[end_]
      e$v[end_] <- t
      sift(1, end_ - 1L)
    }
  }
  e$v
}
stopifnot(identical(as.integer(heap_sort(c(5, 2, 4, 6, 1, 3))), 1:6))
stopifnot(identical(as.integer(heap_sort(c(9, 8, 7, 6, 5))), 5:9))
cat("PASS\\n")''',
"zig":'''const std = @import("std");
fn sift(nums: []i32, start: usize, end: usize) void {
    var root = start;
    while (true) {
        const child = 2 * root + 1;
        if (child > end) break;
        var swap = root;
        if (nums[swap] < nums[child]) swap = child;
        if (child + 1 <= end and nums[swap] < nums[child + 1]) swap = child + 1;
        if (swap == root) break;
        const t = nums[root];
        nums[root] = nums[swap];
        nums[swap] = t;
        root = swap;
    }
}
fn heapSort(nums: []i32) void {
    const n = nums.len;
    if (n == 0) return;
    var i: usize = n / 2;
    while (i > 0) : (i -= 1) sift(nums, i - 1, n - 1);
    var end = n;
    while (end > 1) : (end -= 1) {
        const t = nums[0];
        nums[0] = nums[end - 1];
        nums[end - 1] = t;
        sift(nums, 0, end - 2);
    }
}
pub fn main() !void {
    var v1 = [_]i32{ 5, 2, 4, 6, 1, 3 };
    heapSort(&v1);
    for (v1, 0..) |v, i| if (v != @as(i32, @intCast(i + 1))) return error.TestFailed;
    std.debug.print("PASS\\n", .{}); }''',
"dart":'''List<int> heapSort(List<int> nums) {
  final v = List<int>.from(nums);
  final n = v.length;
  if (n == 0) return v;
  void sift(int start, int end) {
    var root = start;
    while (true) {
      final child = 2 * root + 1;
      if (child > end) break;
      var swap = root;
      if (v[swap] < v[child]) swap = child;
      if (child + 1 <= end && v[swap] < v[child + 1]) swap = child + 1;
      if (swap == root) break;
      final t = v[root];
      v[root] = v[swap];
      v[swap] = t;
      root = swap;
    }
  }
  for (var i = n ~/ 2 - 1; i >= 0; i--) { sift(i, n - 1); }
  for (var end = n - 1; end >= 1; end--) {
    final t = v[0];
    v[0] = v[end];
    v[end] = t;
    sift(0, end - 1);
  }
  return v;
}
void main() { if (heapSort([5,2,4,6,1,3]).toString() != '[1, 2, 3, 4, 5, 6]') throw StateError('c1'); print('PASS'); }''',
}

BUCKET = {
"rust":'''fn get_index(arr: &[i32], k: i32) -> i32 {
    if arr.contains(&k) { k } else { -1 }
}
fn main() {
    assert_eq!(get_index(&[1,2,3], 1), 1);
    assert_eq!(get_index(&[1,2,3], 2), 2);
    assert_eq!(get_index(&[1,2,3], 3), 3);
    assert_eq!(get_index(&[3,1,2], 2), 2);
    assert_eq!(get_index(&[1,2,3], 5), -1);
    println!("PASS"); }''',
"lua":'''local function get_index(arr, k)
    for _, v in ipairs(arr) do
        if v == k then return k end
    end
    return -1
end
assert(get_index({1,2,3}, 1) == 1)
assert(get_index({1,2,3}, 2) == 2)
assert(get_index({1,2,3}, 3) == 3)
assert(get_index({3,1,2}, 2) == 2)
assert(get_index({1,2,3}, 5) == -1)
print("PASS")''',
"c":'''#include <stdio.h>
static int get_index(const int *arr, int n, int k) {
    for (int i = 0; i < n; i++) if (arr[i] == k) return k;
    return -1;
}
int main(void) {
    int a[] = {1,2,3};
    if (get_index(a, 3, 1) != 1) { printf("FAIL 1\\n"); return 1; }
    if (get_index(a, 3, 3) != 3) { printf("FAIL 2\\n"); return 1; }
    if (get_index(a, 3, 5) != -1) { printf("FAIL 3\\n"); return 1; }
    printf("PASS\\n"); return 0; }''',
"cpp":'''#include <cassert>
#include <iostream>
#include <vector>
static int getIndex(const std::vector<int> &arr, int k) {
    for (int v : arr) if (v == k) return k;
    return -1;
}
int main() {
    assert(getIndex({1,2,3}, 1) == 1);
    assert(getIndex({1,2,3}, 3) == 3);
    assert(getIndex({1,2,3}, 5) == -1);
    std::cout << "PASS" << std::endl; }''',
"r":'''get_index <- function(arr, k) {
  if (k %in% arr) as.integer(k) else -1L
}
stopifnot(get_index(c(1, 2, 3), 1) == 1)
stopifnot(get_index(c(1, 2, 3), 3) == 3)
stopifnot(get_index(c(1, 2, 3), 5) == -1)
cat("PASS\\n")''',
"zig":'''const std = @import("std");
fn getIndex(arr: []const i32, k: i32) i32 {
    for (arr) |v| if (v == k) return k;
    return -1;
}
pub fn main() !void {
    const a = [_]i32{ 1, 2, 3 };
    if (getIndex(&a, 1) != 1) return error.TestFailed;
    if (getIndex(&a, 3) != 3) return error.TestFailed;
    if (getIndex(&a, 5) != -1) return error.TestFailed;
    std.debug.print("PASS\\n", .{}); }''',
"dart":'''int getIndex(List<int> arr, int k) {
  for (final v in arr) { if (v == k) return k; }
  return -1;
}
void main() {
  if (getIndex([1,2,3], 1) != 1) throw StateError('c1');
  if (getIndex([1,2,3], 3) != 3) throw StateError('c2');
  if (getIndex([1,2,3], 5) != -1) throw StateError('c3');
  print('PASS'); }''',
}

COMPLEXITY = {
"rust":'''fn func_calls(n: i32) -> i64 {
    // func(n) = func(n-1) + func(n-1)，总调用次数 = 2^n - 1（指数复杂度示例）
    if n <= 1 { return 1; }
    2 * func_calls(n - 1)
}
fn main() {
    assert_eq!(func_calls(1), 1);
    assert_eq!(func_calls(2), 2);
    assert_eq!(func_calls(5), 16);
    assert_eq!(func_calls(10), 512);
    println!("PASS"); }''',
"lua":'''local function func_calls(n)
    if n <= 1 then return 1 end
    return 2 * func_calls(n - 1)
end
assert(func_calls(1) == 1)
assert(func_calls(2) == 2)
assert(func_calls(5) == 16)
assert(func_calls(10) == 512)
print("PASS")''',
"c":'''#include <stdio.h>
static long func_calls(int n) {
    if (n <= 1) return 1;
    return 2 * func_calls(n - 1);
}
int main(void) {
    if (func_calls(1) != 1 || func_calls(2) != 2 || func_calls(5) != 16 || func_calls(10) != 512) { printf("FAIL\\n"); return 1; }
    printf("PASS\\n"); return 0; }''',
"cpp":'''#include <cassert>
#include <iostream>
static long long funcCalls(int n) {
    if (n <= 1) return 1;
    return 2 * funcCalls(n - 1);
}
int main() { assert(funcCalls(1) == 1); assert(funcCalls(2) == 2); assert(funcCalls(5) == 16); assert(funcCalls(10) == 512); std::cout << "PASS" << std::endl; }''',
"r":'''func_calls <- function(n) {
  if (n <= 1) return(1)
  2 * func_calls(n - 1)
}
stopifnot(func_calls(1) == 1, func_calls(2) == 2, func_calls(5) == 16, func_calls(10) == 512)
cat("PASS\\n")''',
"zig":'''const std = @import("std");
fn funcCalls(n: i32) i64 {
    if (n <= 1) return 1;
    return 2 * funcCalls(n - 1);
}
pub fn main() !void {
    if (funcCalls(1) != 1 or funcCalls(2) != 2 or funcCalls(5) != 16 or funcCalls(10) != 512) return error.TestFailed;
    std.debug.print("PASS\\n", .{}); }''',
"dart":'''int funcCalls(int n) {
  if (n <= 1) return 1;
  return 2 * funcCalls(n - 1);
}
void main() { if (funcCalls(1) != 1 || funcCalls(2) != 2 || funcCalls(5) != 16 || funcCalls(10) != 512) throw StateError('x'); print('PASS'); }''',
}

PROBS = [
    ("lc_134172583_计数排序", COUNT, "134172583", "数据结构与算法之排序: 计数排序"),
    ("lc_134191965_基数排序", RADIX, "134191965", "数据结构与算法之排序: 基数排序"),
    ("lc_134150438_希尔排序", SHELL, "134150438", "数据结构与算法之排序: 希尔排序"),
    ("lc_134085409_堆排序", HEAPSORT, "134085409", "数据结构与算法之排序: 堆排序"),
    ("lc_134205361_桶排序", BUCKET, "134205361", "数据结构与算法之排序: 桶排序"),
    ("lc_93536806_数据结构与算法笔记_复杂度", COMPLEXITY, "93536806", "数据结构与算法笔记: 复杂度"),
]
count = 0
for pdir, algo, bid, title in PROBS:
    ts_dir = f"/Users/Wang/Code/github/web-x-blog/work/target/21.dsa/ts/notes/{pdir}"
    sols = sorted(f[:-3] for f in os.listdir(ts_dir) if f.startswith("solution_") and f.endswith(".ts"))
    for lang in LANGNAME:
        ext = EXT[lang]
        for sol in sols:
            n = sol.replace("solution_", "").split("_")[0]
            head = head_comment(lang, bid, f"{title} — {LANGNAME[lang]} 版（方案{n}）")
            emit(lang, f"notes/{pdir}/{sol}.{ext}", head + "\n" + algo[lang])
            count += 1
print(f"emitted {count} files")
