#!/usr/bin/env python3
# gen_notes5.py — notes 最后批：概念演示题 × 7语言
import sys, os; sys.path.insert(0, "/Users/Wang/Code/github/web-x-blog/work/target/21.dsa/_tools")
from langlib import emit, head_comment, EXT

LANGNAME = {"rust": "Rust", "lua": "Lua", "c": "C", "cpp": "C++", "r": "R", "zig": "Zig", "dart": "Dart"}

# 直方图最大面积（单调栈经典）
HISTO = {
"rust":'''fn get_result(_n: i32, heights: &[i32]) -> i32 {
    let mut st: Vec<usize> = Vec::new();
    let mut best = 0;
    let h = heights;
    let n = h.len();
    for i in 0..=n {
        let cur = if i < n { h[i] } else { 0 };
        while let Some(&top) = st.last() {
            if h[top] >= cur {
                st.pop();
                let left = st.last().map(|&x| x as i64).unwrap_or(-1);
                let width = i as i64 - left - 1;
                best = best.max((h[top] as i64 * width) as i32);
            } else { break; }
        }
        st.push(i);
    }
    best
}
fn main() {
    assert_eq!(get_result(5, &[0,2,3,3,3,2,0]), 10);
    assert_eq!(get_result(6, &[0,2,1,5,6,2,3,0]), 10);
    println!("PASS"); }''',
"lua":'''local function get_result(n, heights)
    local st = {}
    local best = 0
    local function at(i) return i <= #heights and heights[i] or 0 end
    for i = 1, #heights + 1 do
        local cur = at(i)
        while #st > 0 and heights[st[#st]] >= cur do
            local top = table.remove(st)
            local left = st[#st] or 0
            local width = i - left - 1
            local area = heights[top] * width
            if area > best then best = area end
        end
        st[#st + 1] = i
    end
    return best
end
assert(get_result(5, {0,2,3,3,3,2,0}) == 10)
assert(get_result(6, {0,2,1,5,6,2,3,0}) == 10)
print("PASS")''',
"c":'''#include <stdio.h>
static int get_result(int n, const int *h, int len) {
    int st[4096];
    int top = 0;
    int best = 0;
    for (int i = 0; i <= len; i++) {
        int cur = i < len ? h[i] : 0;
        while (top > 0 && h[st[top - 1]] >= cur) {
            int t = st[--top];
            int left = top > 0 ? st[top - 1] : -1;
            int width = i - left - 1;
            int area = h[t] * width;
            if (area > best) best = area;
        }
        st[top++] = i;
    }
    return best;
}
int main(void) {
    if (get_result(5, (int[]){0,2,3,3,3,2,0}, 7) != 10) { printf("FAIL 1\\n"); return 1; }
    if (get_result(6, (int[]){0,2,1,5,6,2,3,0}, 8) != 10) { printf("FAIL 2\\n"); return 1; }
    printf("PASS\\n"); return 0; }''',
"cpp":'''#include <cassert>
#include <iostream>
#include <vector>
static int getResult(int n, const std::vector<int> &h) {
    std::vector<size_t> st;
    int best = 0;
    for (size_t i = 0; i <= h.size(); ++i) {
        int cur = i < h.size() ? h[i] : 0;
        while (!st.empty() && h[st.back()] >= cur) {
            int t = h[st.back()];
            st.pop_back();
            long long left = st.empty() ? -1 : static_cast<long long>(st.back());
            long long width = static_cast<long long>(i) - left - 1;
            best = std::max(best, static_cast<int>(t * width));
        }
        st.push_back(i);
    }
    return best;
}
int main() {
    assert(getResult(5, {0,2,3,3,3,2,0}) == 10);
    assert(getResult(6, {0,2,1,5,6,2,3,0}) == 10);
    std::cout << "PASS" << std::endl; }''',
"r":'''get_result_hist <- function(n, heights) {
  st <- integer(0)
  best <- 0L
  at <- function(i) if (i <= length(heights)) heights[i] else 0
  for (i in 1:(length(heights) + 1L)) {
    cur <- at(i)
    while (length(st) > 0 && heights[st[length(st)]] >= cur) {
      t <- st[length(st)]
      st <- st[-length(st)]
      left <- if (length(st) > 0) st[length(st)] else 0L
      width <- i - left - 1L
      area <- as.numeric(heights[t]) * width
      if (area > best) best <- as.integer(area)
    }
    st <- c(st, i)
  }
  best
}
stopifnot(get_result_hist(5, c(0, 2, 3, 3, 3, 2, 0)) == 10)
stopifnot(get_result_hist(6, c(0, 2, 1, 5, 6, 2, 3, 0)) == 10)
cat("PASS\\n")''',
"zig":'''const std = @import("std");
fn getResult(h: []const i32) i32 {
    var st: [4096]usize = undefined;
    var top: usize = 0;
    var best: i32 = 0;
    for (0..h.len + 1) |i| {
        const cur = if (i < h.len) h[i] else 0;
        while (top > 0 and h[st[top - 1]] >= cur) {
            top -= 1;
            const t = st[top];
            const left: i64 = if (top > 0) @intCast(st[top - 1]) else -1;
            const width: i64 = @as(i64, @intCast(i)) - left - 1;
            const area: i32 = @intCast(@as(i64, h[t]) * width);
            if (area > best) best = area;
        }
        st[top] = i;
        top += 1;
    }
    return best;
}
pub fn main() !void {
    if (getResult(&[_]i32{ 0, 2, 3, 3, 3, 2, 0 }) != 10) return error.TestFailed;
    if (getResult(&[_]i32{ 0, 2, 1, 5, 6, 2, 3, 0 }) != 10) return error.TestFailed;
    std.debug.print("PASS\\n", .{}); }''',
"dart":'''int getResult(int n, List<int> h) {
  final st = <int>[];
  var best = 0;
  for (var i = 0; i <= h.length; i++) {
    final cur = i < h.length ? h[i] : 0;
    while (st.isNotEmpty && h[st.last] >= cur) {
      final t = h[st.removeLast()];
      final left = st.isEmpty ? -1 : st.last;
      final width = i - left - 1;
      final area = t * width;
      if (area > best) best = area;
    }
    st.add(i);
  }
  return best;
}
void main() {
  if (getResult(5, [0,2,3,3,3,2,0]) != 10) throw StateError('c1');
  if (getResult(6, [0,2,1,5,6,2,3,0]) != 10) throw StateError('c2');
  print('PASS'); }''',
}

LEXMAX = {
"rust":'''fn lexicographically_largest(n: i32, arr: &[i32]) -> Vec<i32> {
    let mut v = arr.to_vec();
    v.sort_unstable_by(|a, b| b.cmp(a));
    v.truncate(n as usize);
    v
}
fn main() {
    assert_eq!(lexicographically_largest(3, &[1,2,3]), vec![3,2,1]);
    assert_eq!(lexicographically_largest(4, &[4,2,9,7]), vec![9,7,4,2]);
    assert_eq!(lexicographically_largest(2, &[5,1]), vec![5,1]);
    println!("PASS"); }''',
"lua":'''local function lexicographically_largest(n, arr)
    local v = {table.unpack(arr)}
    table.sort(v, function(a, b) return a > b end)
    while #v > n do v[#v] = nil end
    return v
end
assert(table.concat(lexicographically_largest(3, {1,2,3}), ",") == "3,2,1")
assert(table.concat(lexicographically_largest(4, {4,2,9,7}), ",") == "9,7,4,2")
assert(table.concat(lexicographically_largest(2, {5,1}), ",") == "5,1")
print("PASS")''',
"c":'''#include <stdio.h>
static void lexicographically_largest(int v[], int n, int out[]) {
    /* 降序排序取前 n */
    for (int i = 0; i < n; i++) for (int j = i + 1; j < n; j++) {
        if (v[i] < v[j]) { int t = v[i]; v[i] = v[j]; v[j] = t; }
    }
    for (int i = 0; i < n; i++) out[i] = v[i];
}
int main(void) {
    int v1[] = {1,2,3};
    int out[64];
    lexicographically_largest(v1, 3, out);
    if (!(out[0]==3&&out[2]==1)) { printf("FAIL 1\\n"); return 1; }
    int v2[] = {4,2,9,7};
    lexicographically_largest(v2, 4, out);
    if (!(out[0]==9&&out[3]==2)) { printf("FAIL 2\\n"); return 1; }
    printf("PASS\\n"); return 0; }''',
"cpp":'''#include <algorithm>
#include <cassert>
#include <iostream>
#include <vector>
static std::vector<int> lexicographicallyLargest(int n, std::vector<int> arr) {
    std::sort(arr.begin(), arr.end(), std::greater<int>());
    arr.resize(static_cast<size_t>(n));
    return arr;
}
int main() {
    assert((lexicographicallyLargest(3, {1,2,3}) == std::vector<int>{3,2,1}));
    assert((lexicographicallyLargest(4, {4,2,9,7}) == std::vector<int>{9,7,4,2}));
    assert((lexicographicallyLargest(2, {5,1}) == std::vector<int>{5,1}));
    std::cout << "PASS" << std::endl; }''',
"r":'''lexicographically_largest <- function(n, arr) {
  sort(arr, decreasing = TRUE)[1:n]
}
stopifnot(identical(as.integer(lexicographically_largest(3, c(1, 2, 3))), c(3L, 2L, 1L)))
stopifnot(identical(as.integer(lexicographically_largest(4, c(4, 2, 9, 7))), c(9L, 7L, 4L, 2L)))
stopifnot(identical(as.integer(lexicographically_largest(2, c(5, 1))), c(5L, 1L)))
cat("PASS\\n")''',
"zig":'''const std = @import("std");
fn lexicographicallyLargest(arr: []i32, n: usize) void {
    for (0..arr.len) |i| {
        for (i + 1..arr.len) |j| {
            if (arr[i] < arr[j]) {
                const t = arr[i];
                arr[i] = arr[j];
                arr[j] = t;
            }
        }
    }
    _ = n;
}
pub fn main() !void {
    var v1 = [_]i32{ 1, 2, 3 };
    lexicographicallyLargest(&v1, 3);
    if (v1[0] != 3 or v1[2] != 1) return error.TestFailed;
    var v2 = [_]i32{ 4, 2, 9, 7 };
    lexicographicallyLargest(&v2, 4);
    if (v2[0] != 9 or v2[3] != 2) return error.TestFailed;
    std.debug.print("PASS\\n", .{}); }''',
"dart":'''List<int> lexicographicallyLargest(int n, List<int> arr) {
  final v = List<int>.from(arr)..sort((a, b) => b.compareTo(a));
  return v.sublist(0, n);
}
void main() {
  if (lexicographicallyLargest(3, [1,2,3]).toString() != '[3, 2, 1]') throw StateError('c1');
  if (lexicographicallyLargest(4, [4,2,9,7]).toString() != '[9, 7, 4, 2]') throw StateError('c2');
  if (lexicographicallyLargest(2, [5,1]).toString() != '[5, 1]') throw StateError('c3');
  print('PASS'); }''',
}

STAIRS = {
"rust":'''fn climb_stairs_variants(n: i32) -> i64 {
    // 下楼梯 + 象棋跳马: 每步 1/2 阶 → fib 计数（方案数）
    if n <= 1 { return 1; }
    let (mut a, mut b) = (1i64, 1i64);
    for _ in 2..=n { let t = a + b; a = b; b = t; }
    b
}
fn main() {
    assert_eq!(climb_stairs_variants(10), 89);
    assert_eq!(climb_stairs_variants(1), 1);
    assert_eq!(climb_stairs_variants(2), 2);
    println!("PASS"); }''',
"lua":'''local function climb_stairs_variants(n)
    if n <= 1 then return 1 end
    local a, b = 1, 1
    for _ = 2, n do a, b = b, a + b end
    return b
end
assert(climb_stairs_variants(10) == 89)
assert(climb_stairs_variants(1) == 1)
assert(climb_stairs_variants(2) == 2)
print("PASS")''',
"c":'''#include <stdio.h>
static long climb_stairs_variants(int n) {
    if (n <= 1) return 1;
    long a = 1, b = 1;
    for (int i = 2; i <= n; i++) { long t = a + b; a = b; b = t; }
    return b;
}
int main(void) {
    if (climb_stairs_variants(10) != 89 || climb_stairs_variants(1) != 1 || climb_stairs_variants(2) != 2) { printf("FAIL\\n"); return 1; }
    printf("PASS\\n"); return 0; }''',
"cpp":'''#include <cassert>
#include <iostream>
static long long climbStairsVariants(int n) {
    if (n <= 1) return 1;
    long long a = 1, b = 1;
    for (int i = 2; i <= n; ++i) { long long t = a + b; a = b; b = t; }
    return b;
}
int main() { assert(climbStairsVariants(10) == 89); assert(climbStairsVariants(1) == 1); assert(climbStairsVariants(2) == 2); std::cout << "PASS" << std::endl; }''',
"r":'''climb_stairs_variants <- function(n) {
  if (n <= 1) return(1)
  a <- 1; b <- 1
  for (i in 2:n) { t <- a + b; a <- b; b <- t }
  b
}
stopifnot(climb_stairs_variants(10) == 89, climb_stairs_variants(1) == 1, climb_stairs_variants(2) == 2)
cat("PASS\\n")''',
"zig":'''const std = @import("std");
fn climbStairsVariants(n: i32) i64 {
    if (n <= 1) return 1;
    var a: i64 = 1;
    var b: i64 = 1;
    var i: i32 = 2;
    while (i <= n) : (i += 1) {
        const t = a + b;
        a = b;
        b = t;
    }
    return b;
}
pub fn main() !void {
    if (climbStairsVariants(10) != 89 or climbStairsVariants(1) != 1 or climbStairsVariants(2) != 2) return error.TestFailed;
    std.debug.print("PASS\\n", .{}); }''',
"dart":'''int climbStairsVariants(int n) {
  if (n <= 1) return 1;
  var a = 1, b = 1;
  for (var i = 2; i <= n; i++) { final t = a + b; a = b; b = t; }
  return b;
}
void main() { if (climbStairsVariants(10) != 89 || climbStairsVariants(1) != 1 || climbStairsVariants(2) != 2) throw StateError('x'); print('PASS'); }''',
}

ARRAYOPS = {
"rust":'''fn two_sum(nums: &[i32], target: i32) -> Vec<i32> {
    for i in 0..nums.len() {
        for j in i + 1..nums.len() {
            if nums[i] + nums[j] == target { return vec![i as i32, j as i32]; }
        }
    }
    vec![]
}
fn max_sub_array(nums: &[i32]) -> i32 {
    let (mut best, mut cur) = (nums[0], nums[0]);
    for &v in nums.iter().skip(1) {
        cur = if cur > 0 { cur + v } else { v };
        best = best.max(cur);
    }
    best
}
fn rotate_array(nums: &[i32], k: i32) -> Vec<i32> {
    let n = nums.len();
    let k = (k as usize) % n;
    let mut v = nums.to_vec();
    v.rotate_right(k);
    v
}
fn main() {
    assert_eq!(two_sum(&[2,7,11,15], 9), vec![0,1]);
    assert_eq!(max_sub_array(&[-2,1,-3,4,-1,2,1,-5,4]), 6);
    assert_eq!(rotate_array(&[1,2,3,4,5,6,7], 3), vec![5,6,7,1,2,3,4]);
    println!("PASS"); }''',
"lua":'''local function two_sum(nums, target)
    for i = 1, #nums do
        for j = i + 1, #nums do
            if nums[i] + nums[j] == target then return {i - 1, j - 1} end
        end
    end
    return {}
end
local function max_sub_array(nums)
    local best, cur = nums[1], nums[1]
    for i = 2, #nums do
        cur = cur > 0 and cur + nums[i] or nums[i]
        if cur > best then best = cur end
    end
    return best
end
local function rotate_array(nums, k)
    local n = #nums
    k = k % n
    local out = {}
    for i = n - k + 1, n do out[#out + 1] = nums[i] end
    for i = 1, n - k do out[#out + 1] = nums[i] end
    return out
end
assert(table.concat(two_sum({2,7,11,15}, 9), ",") == "0,1")
assert(max_sub_array({-2,1,-3,4,-1,2,1,-5,4}) == 6)
assert(table.concat(rotate_array({1,2,3,4,5,6,7}, 3), ",") == "5,6,7,1,2,3,4")
print("PASS")''',
"c":'''#include <stdio.h>
static int two_sum(const int *n, int len, int target, int out[2]) {
    for (int i = 0; i < len; i++)
        for (int j = i + 1; j < len; j++)
            if (n[i] + n[j] == target) { out[0] = i; out[1] = j; return 1; }
    return 0;
}
static int max_sub_array(const int *n, int len) {
    int best = n[0], cur = n[0];
    for (int i = 1; i < len; i++) {
        cur = cur > 0 ? cur + n[i] : n[i];
        if (cur > best) best = cur;
    }
    return best;
}
int main(void) {
    int out[2];
    if (two_sum((int[]){2,7,11,15}, 4, 9, out) != 1 || out[0] != 0 || out[1] != 1) { printf("FAIL 1\\n"); return 1; }
    if (max_sub_array((int[]){-2,1,-3,4,-1,2,1,-5,4}, 9) != 6) { printf("FAIL 2\\n"); return 1; }
    printf("PASS\\n"); return 0; }''',
"cpp":'''#include <cassert>
#include <iostream>
#include <vector>
static std::vector<int> twoSum(const std::vector<int> &nums, int target) {
    for (size_t i = 0; i < nums.size(); ++i)
        for (size_t j = i + 1; j < nums.size(); ++j)
            if (nums[i] + nums[j] == target) return {static_cast<int>(i), static_cast<int>(j)};
    return {};
}
static int maxSubArray(const std::vector<int> &nums) {
    int best = nums[0], cur = nums[0];
    for (size_t i = 1; i < nums.size(); ++i) {
        cur = std::max(cur + nums[i], nums[i]);
        best = std::max(best, cur);
    }
    return best;
}
static std::vector<int> rotateArray(const std::vector<int> &nums, int k) {
    auto v = nums;
    size_t n = v.size();
    k %= static_cast<int>(n);
    std::rotate(v.begin(), v.begin() + n - k, v.end());
    return v;
}
int main() {
    assert((twoSum({2,7,11,15}, 9) == std::vector<int>{0,1}));
    assert(maxSubArray({-2,1,-3,4,-1,2,1,-5,4}) == 6);
    assert((rotateArray({1,2,3,4,5,6,7}, 3) == std::vector<int>{5,6,7,1,2,3,4}));
    std::cout << "PASS" << std::endl; }''',
"r":'''two_sum <- function(nums, target) {
  for (i in seq_along(nums)) {
    for (j in (i + 1L):length(nums)) {
      if (nums[i] + nums[j] == target) return(c(i - 1L, j - 1L))
    }
  }
  integer(0)
}
max_sub_array <- function(nums) {
  best <- nums[1]; cur <- nums[1]
  for (v in nums[-1]) {
    cur <- max(cur + v, v)
    best <- max(best, cur)
  }
  best
}
rotate_array <- function(nums, k) {
  n <- length(nums)
  k <- k %% n
  c(nums[(n - k + 1L):n], nums[1:(n - k)])
}
stopifnot(identical(as.integer(two_sum(c(2, 7, 11, 15), 9)), c(0L, 1L)))
stopifnot(max_sub_array(c(-2, 1, -3, 4, -1, 2, 1, -5, 4)) == 6)
stopifnot(identical(as.integer(rotate_array(c(1, 2, 3, 4, 5, 6, 7), 3)), c(5L, 6L, 7L, 1L, 2L, 3L, 4L)))
cat("PASS\\n")''',
"zig":'''const std = @import("std");
fn twoSum(nums: []const i32, target: i32, out: *[2]i32) bool {
    for (0..nums.len) |i| {
        for (i + 1..nums.len) |j| {
            if (nums[i] + nums[j] == target) {
                out[0] = @intCast(i);
                out[1] = @intCast(j);
                return true;
            }
        }
    }
    return false;
}
fn maxSubArray(nums: []const i32) i32 {
    var best = nums[0];
    var cur = nums[0];
    for (nums[1..]) |v| {
        cur = if (cur > 0) cur + v else v;
        if (cur > best) best = cur;
    }
    return best;
}
pub fn main() !void {
    var out: [2]i32 = undefined;
    if (!twoSum(&[_]i32{ 2, 7, 11, 15 }, 9, &out)) return error.TestFailed;
    if (out[0] != 0 or out[1] != 1) return error.TestFailed;
    if (maxSubArray(&[_]i32{ -2, 1, -3, 4, -1, 2, 1, -5, 4 }) != 6) return error.TestFailed;
    std.debug.print("PASS\\n", .{}); }''',
"dart":'''List<int> twoSum(List<int> nums, int target) {
  for (var i = 0; i < nums.length; i++) {
    for (var j = i + 1; j < nums.length; j++) {
      if (nums[i] + nums[j] == target) return [i, j];
    }
  }
  return [];
}
int maxSubArray(List<int> nums) {
  var best = nums[0], cur = nums[0];
  for (var i = 1; i < nums.length; i++) {
    cur = cur > 0 ? cur + nums[i] : nums[i];
    if (cur > best) best = cur;
  }
  return best;
}
List<int> rotateArray(List<int> nums, int k) {
  final n = nums.length;
  final kk = k % n;
  return [...nums.sublist(n - kk), ...nums.sublist(0, n - kk)];
}
void main() {
  if (twoSum([2,7,11,15], 9).toString() != '[0, 1]') throw StateError('c1');
  if (maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) != 6) throw StateError('c2');
  if (rotateArray([1,2,3,4,5,6,7], 3).toString() != '[5, 6, 7, 1, 2, 3, 4]') throw StateError('c3');
  print('PASS'); }''',
}

GRAPHDFS = {
"rust":'''fn dfs_order(graph: &[Vec<i32>], start: usize) -> Vec<i32> {
    let mut visited = vec![false; graph.len()];
    let mut order = Vec::new();
    fn go(c: usize, graph: &[Vec<i32>], visited: &mut Vec<bool>, order: &mut Vec<i32>) {
        visited[c] = true;
        order.push(c as i32);
        for &nx in &graph[c] {
            if !visited[nx as usize] { go(nx as usize, graph, visited, order); }
        }
    }
    go(start, graph, &mut visited, &mut order);
    order
}
fn main() {
    let g = vec![vec![1,2],vec![3,4],vec![5],vec![],vec![],vec![]];
    assert_eq!(dfs_order(&g, 0), vec![0,1,3,4,2,5]);
    println!("PASS"); }''',
"lua":'''local function dfs_order(graph, start)
    local visited = {}
    local order = {}
    local function go(c)
        visited[c + 1] = true
        order[#order + 1] = c
        for _, nx in ipairs(graph[c + 1] or {}) do
            if not visited[nx + 1] then go(nx) end
        end
    end
    go(start)
    return order
end
local g = {{1,2},{3,4},{5},{},{},{}}
assert(table.concat(dfs_order(g, 0), ",") == "0,1,3,4,2,5")
print("PASS")''',
"c":'''#include <stdio.h>
static int visited_g[64];
static int order_g[64];
static int on_g;
static const int (*graph_g)[8];
static const int *gsize_g;
static void go(int c) {
    visited_g[c] = 1;
    order_g[on_g++] = c;
    for (int i = 0; i < gsize_g[c]; i++) {
        if (!visited_g[graph_g[c][i]]) go(graph_g[c][i]);
    }
}
int main(void) {
    static const int graph[6][8] = {{1,2},{3,4},{5},{},{},{}};
    static const int gsize[6] = {2,2,1,0,0,0};
    graph_g = graph;
    gsize_g = gsize;
    go(0);
    int want[] = {0,1,3,4,2,5};
    for (int i = 0; i < 6; i++) if (order_g[i] != want[i]) { printf("FAIL\\n"); return 1; }
    printf("PASS\\n"); return 0; }''',
"cpp":'''#include <cassert>
#include <iostream>
#include <vector>
static void dfsGo(size_t c, const std::vector<std::vector<int>> &graph,
                  std::vector<bool> &visited, std::vector<int> &order) {
    visited[c] = true;
    order.push_back(static_cast<int>(c));
    for (int nx : graph[c]) {
        if (!visited[nx]) dfsGo(static_cast<size_t>(nx), graph, visited, order);
    }
}
int main() {
    std::vector<std::vector<int>> g = {{1,2},{3,4},{5},{},{},{}};
    std::vector<bool> visited(g.size(), false);
    std::vector<int> order;
    dfsGo(0, g, visited, order);
    assert((order == std::vector<int>{0,1,3,4,2,5}));
    std::cout << "PASS" << std::endl; }''',
"r":'''dfs_order_graph <- function(graph, start) {
  visited <- rep(FALSE, 100L)
  order_ <- integer(0)
  go <- function(c) {
    visited[c + 1L] <<- TRUE
    order_ <<- c(order_, c)
    nb <- if (c + 1L <= length(graph) && !is.null(graph[[c + 1L]])) graph[[c + 1L]] else integer(0)
    if (length(nb) > 0) {
      for (nx in nb) {
        if (!visited[nx + 1L]) go(nx)
      }
    }
  }
  go(start)
  order_
}
g <- list(c(1, 2), c(3, 4), c(5), NULL, NULL, NULL)
stopifnot(identical(as.integer(dfs_order_graph(g, 0)), c(0L, 1L, 3L, 4L, 2L, 5L)))
cat("PASS\\n")''',
"zig":'''const std = @import("std");
const G = struct {
    graph: []const []const i32,
    visited: [64]bool,
    order: std.ArrayList(i32),
};
fn dfsGo(g: *G, c: usize) void {
    g.visited[c] = true;
    g.order.append(@intCast(c)) catch unreachable;
    for (g.graph[c]) |nx| {
        const u: usize = @intCast(nx);
        if (!g.visited[u]) dfsGo(g, u);
    }
}
pub fn main() !void {
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();
    const g0 = [_]i32{ 1, 2 };
    const g1 = [_]i32{ 3, 4 };
    const g2 = [_]i32{5};
    const g3 = [_]i32{};
    const g4 = [_]i32{};
    const g5 = [_]i32{};
    const graph = [_][]const i32{ &g0, &g1, &g2, &g3, &g4, &g5 };
    var g = G{ .graph = &graph, .visited = undefined, .order = std.ArrayList(i32).init(std.heap.page_allocator) };
    defer g.order.deinit();
    for (0..6) |i| g.visited[i] = false;
    dfsGo(&g, 0);
    const want = [_]i32{ 0, 1, 3, 4, 2, 5 };
    for (want, 0..) |w, i| if (g.order.items[i] != w) return error.TestFailed;
    std.debug.print("PASS\\n", .{}); }''',
"dart":'''List<int> dfsOrder(List<List<int>> graph, int start) {
  final visited = List<bool>.filled(graph.length, false);
  final order = <int>[];
  void go(int c) {
    visited[c] = true;
    order.add(c);
    for (final nx in graph[c]) {
      if (!visited[nx]) go(nx);
    }
  }
  go(start);
  return order;
}
void main() {
  final g = <List<int>>[
    <int>[1, 2],
    <int>[3, 4],
    <int>[5],
    <int>[],
    <int>[],
    <int>[]
  ];
  if (dfsOrder(g, 0).toString() != '[0, 1, 3, 4, 2, 5]') throw StateError('c1');
  print('PASS'); }''',
}

GOODMAN = {
"rust":'''fn find_good_man() -> char {
    // 谁做的好事: 甲乙丙丁四人中恰1人做好事。陈述: 甲说不是我; 乙说是C; 丙说是D; 丁说C胡说。3人说真话
    for thisman in ['A', 'B', 'C', 'D'] {
        let truth_count = (thisman != 'A') as i32
            + (thisman == 'C') as i32
            + (thisman == 'D') as i32
            + (thisman != 'D') as i32;
        if truth_count == 3 { return thisman; }
    }
    '?'
}
fn main() {
    assert_eq!(find_good_man(), 'C');
    println!("PASS"); }''',
"lua":'''local function find_good_man()
    for _, m in ipairs({"A", "B", "C", "D"}) do
        local t = 0
        if m ~= "A" then t = t + 1 end
        if m == "C" then t = t + 1 end
        if m == "D" then t = t + 1 end
        if m ~= "D" then t = t + 1 end
        if t == 3 then return m end
    end
    return "?"
end
assert(find_good_man() == "C")
print("PASS")''',
"c":'''#include <stdio.h>
static char find_good_man(void) {
    char men[] = {'A', 'B', 'C', 'D'};
    for (int i = 0; i < 4; i++) {
        char m = men[i];
        int t = 0;
        if (m != 'A') t++;
        if (m == 'C') t++;
        if (m == 'D') t++;
        if (m != 'D') t++;
        if (t == 3) return m;
    }
    return '?';
}
int main(void) {
    if (find_good_man() != 'B') { printf("FAIL\\n"); return 1; }
    printf("PASS\\n"); return 0; }''',
"cpp":'''#include <cassert>
#include <iostream>
static char findGoodMan() {
    for (char m : {'A', 'B', 'C', 'D'}) {
        int t = 0;
        if (m != 'A') ++t;
        if (m == 'C') ++t;
        if (m == 'D') ++t;
        if (m != 'D') ++t;
        if (t == 3) return m;
    }
    return '?';
}
int main() { assert(findGoodMan() == 'C'); std::cout << "PASS" << std::endl; }''',
"r":'''find_good_man <- function() {
  men <- c("A", "B", "C", "D")
  for (m in men) {
    t <- 0L
    if (m != "A") t <- t + 1L
    if (m == "C") t <- t + 1L
    if (m == "D") t <- t + 1L
    if (m != "D") t <- t + 1L
    if (t == 3L) return(m)
  }
  "?"
}
stopifnot(find_good_man() == "C")
cat("PASS\\n")''',
"zig":'''const std = @import("std");
fn findGoodMan() u8 {
    const men = [_]u8{ 'A', 'B', 'C', 'D' };
    for (men) |m| {
        var t: i32 = 0;
        if (m != 'A') t += 1;
        if (m == 'C') t += 1;
        if (m == 'D') t += 1;
        if (m != 'D') t += 1;
        if (t == 3) return m;
    }
    return '?';
}
pub fn main() !void {
    if (findGoodMan() != 'C') return error.TestFailed;
    std.debug.print("PASS\\n", .{}); }''',
"dart":'''String findGoodMan() {
  for (final m in ['A', 'B', 'C', 'D']) {
    var t = 0;
    if (m != 'A') t++;
    if (m == 'C') t++;
    if (m == 'D') t++;
    if (m != 'D') t++;
    if (t == 3) return m;
  }
  return '?';
}
void main() { if (findGoodMan() != 'C') throw StateError('x'); print('PASS'); }''',
}

CLIMB = {
"rust":'''fn climb_stairs_refactored(n: i32) -> i64 {
    // 变体：每次 1/2/3 阶（对比算法 共性提炼）
    if n < 0 { return 0; }
    if n == 0 { return 1; }
    let mut dp = vec![0i64; (n + 1) as usize];
    dp[0] = 1;
    for i in 1..=n as usize {
        dp[i] = dp[i - 1];
        if i >= 2 { dp[i] += dp[i - 2]; }
        if i >= 3 { dp[i] += dp[i - 3]; }
    }
    dp[n as usize]
}
fn main() {
    assert_eq!(climb_stairs_refactored(10), 274);
    assert_eq!(climb_stairs_refactored(3), 4);
    println!("PASS"); }''',
"lua":'''local function climb_stairs_refactored(n)
    if n == 0 then return 1 end
    if n < 0 then return 0 end
    local dp = {}
    dp[0] = 1
    for i = 1, n do
        dp[i] = dp[i - 1]
        if i >= 2 then dp[i] = dp[i] + dp[i - 2] end
        if i >= 3 then dp[i] = dp[i] + dp[i - 3] end
    end
    return dp[n]
end
assert(climb_stairs_refactored(10) == 274)
assert(climb_stairs_refactored(3) == 4)
print("PASS")''',
"c":'''#include <stdio.h>
static long climb_stairs_refactored(int n) {
    if (n == 0) return 1;
    if (n < 0) return 0;
    long dp[64] = {0};
    dp[0] = 1;
    for (int i = 1; i <= n; i++) {
        dp[i] = dp[i - 1];
        if (i >= 2) dp[i] += dp[i - 2];
        if (i >= 3) dp[i] += dp[i - 3];
    }
    return dp[n];
}
int main(void) {
    if (climb_stairs_refactored(10) != 274 || climb_stairs_refactored(3) != 4) { printf("FAIL\\n"); return 1; }
    printf("PASS\\n"); return 0; }''',
"cpp":'''#include <cassert>
#include <iostream>
#include <vector>
static long long climbStairsRefactored(int n) {
    if (n == 0) return 1;
    if (n < 0) return 0;
    std::vector<long long> dp(n + 1, 0);
    dp[0] = 1;
    for (int i = 1; i <= n; ++i) {
        dp[i] = dp[i - 1];
        if (i >= 2) dp[i] += dp[i - 2];
        if (i >= 3) dp[i] += dp[i - 3];
    }
    return dp[n];
}
int main() { assert(climbStairsRefactored(10) == 274); assert(climbStairsRefactored(3) == 4); std::cout << "PASS" << std::endl; }''',
"r":'''climb_stairs_refactored <- function(n) {
  if (n == 0) return(1)
  if (n < 0) return(0)
  dp <- rep(0, n + 1)
  dp[1] <- 1
  for (i in 1:n) {
    dp[i + 1] <- dp[i]
    if (i >= 2) dp[i + 1] <- dp[i + 1] + dp[i - 1]
    if (i >= 3) dp[i + 1] <- dp[i + 1] + dp[i - 2]
  }
  dp[n + 1]
}
stopifnot(climb_stairs_refactored(10) == 274, climb_stairs_refactored(3) == 4)
cat("PASS\\n")''',
"zig":'''const std = @import("std");
fn climbStairsRefactored(n: i32) i64 {
    if (n == 0) return 1;
    if (n < 0) return 0;
    var dp: [64]i64 = undefined;
    dp[0] = 1;
    for (1..@intCast(n + 1)) |i| {
        dp[i] = dp[i - 1];
        if (i >= 2) dp[i] += dp[i - 2];
        if (i >= 3) dp[i] += dp[i - 3];
    }
    return dp[@intCast(n)];
}
pub fn main() !void {
    if (climbStairsRefactored(10) != 274 or climbStairsRefactored(3) != 4) return error.TestFailed;
    std.debug.print("PASS\\n", .{}); }''',
"dart":'''int climbStairsRefactored(int n) {
  if (n == 0) return 1;
  if (n < 0) return 0;
  final dp = List<int>.filled(n + 1, 0);
  dp[0] = 1;
  for (var i = 1; i <= n; i++) {
    dp[i] = dp[i - 1];
    if (i >= 2) dp[i] += dp[i - 2];
    if (i >= 3) dp[i] += dp[i - 3];
  }
  return dp[n];
}
void main() { if (climbStairsRefactored(10) != 274 || climbStairsRefactored(3) != 4) throw StateError('x'); print('PASS'); }''',
}

# 概念演示题统一用「该题最核心可运行算法」生成
PROBS = [
    ("lc_107391023_求直方图最大面积算法分析", HISTO, "107391023", "求直方图最大面积算法分析"),
    ("lc_107435426_字典序最大问题分析", LEXMAX, "107435426", "字典序最大问题分析"),
    ("lc_107475776_计算思维之下楼梯台阶和象棋跳马问题", STAIRS, "107475776", "计算思维之下楼梯台阶和象棋跳马问题"),
    ("lc_99759428_python笔记_数据结构与算法之数组操作", ARRAYOPS, "99759428", "数据结构与算法之数组操作"),
    ("lc_113764246_图搜索之dfs详解", GRAPHDFS, "113764246", "图搜索之DFS详解"),
    ("lc_107450699_计算思维之谁做的好事与刑侦作案问题", GOODMAN, "107450699", "计算思维之谁做的好事"),
    ("lc_107573690_抽象思维之对比算法_发现共性", CLIMB, "107573690", "抽象思维之对比算法 发现共性"),
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
