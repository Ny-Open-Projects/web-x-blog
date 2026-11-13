#!/usr/bin/env python3
# gen_greedy.py — greedy 主题 9 题 × 7语言
import sys, os; sys.path.insert(0, "/Users/Wang/Code/github/web-x-blog/work/blog/courses/20.dsa/_tools")
from langlib import emit, head_comment, EXT

B = {"122": "133925028", "1518": "145386116", "435": "135941089", "452": "135949307", "455": "135096603", "45": "133911745", "55": "133844403", "649": "138684407", "860": "135167617"}
LANGNAME = {"rust": "Rust", "lua": "Lua", "c": "C", "cpp": "C++", "r": "R", "zig": "Zig", "dart": "Dart"}

A122 = {
"rust": '''fn max_profit(prices: &[i32]) -> i32 {
    let mut profit = 0;
    for i in 1..prices.len() {
        if prices[i] > prices[i - 1] {
            profit += prices[i] - prices[i - 1];
        }
    }
    profit
}
fn main() {
    assert_eq!(max_profit(&[7, 1, 5, 3, 6, 4]), 7);
    assert_eq!(max_profit(&[1, 2, 3, 4, 5]), 4);
    assert_eq!(max_profit(&[7, 6, 4, 3, 1]), 0);
    println!("PASS");
}
''',
"lua": '''local function max_profit(prices)
    local profit = 0
    for i = 2, #prices do
        if prices[i] > prices[i - 1] then
            profit = profit + prices[i] - prices[i - 1]
        end
    end
    return profit
end
assert(max_profit({7, 1, 5, 3, 6, 4}) == 7)
assert(max_profit({1, 2, 3, 4, 5}) == 4)
assert(max_profit({7, 6, 4, 3, 1}) == 0)
print("PASS")
''',
"c": '''#include <stdio.h>
static int max_profit(const int *prices, int n) {
    int profit = 0;
    for (int i = 1; i < n; i++) {
        if (prices[i] > prices[i - 1]) profit += prices[i] - prices[i - 1];
    }
    return profit;
}
int main(void) {
    if (max_profit((int[]){7,1,5,3,6,4}, 6) != 7) { printf("FAIL 1\\n"); return 1; }
    if (max_profit((int[]){1,2,3,4,5}, 5) != 4) { printf("FAIL 2\\n"); return 1; }
    if (max_profit((int[]){7,6,4,3,1}, 5) != 0) { printf("FAIL 3\\n"); return 1; }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''#include <cassert>
#include <iostream>
#include <vector>
static int maxProfit(const std::vector<int> &prices) {
    int profit = 0;
    for (size_t i = 1; i < prices.size(); ++i) {
        if (prices[i] > prices[i - 1]) profit += prices[i] - prices[i - 1];
    }
    return profit;
}
int main() {
    assert(maxProfit({7, 1, 5, 3, 6, 4}) == 7);
    assert(maxProfit({1, 2, 3, 4, 5}) == 4);
    assert(maxProfit({7, 6, 4, 3, 1}) == 0);
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''max_profit <- function(prices) {
  profit <- 0L
  for (i in 2:length(prices)) {
    if (prices[i] > prices[i - 1L]) profit <- profit + prices[i] - prices[i - 1L]
  }
  profit
}
stopifnot(max_profit(c(7L, 1L, 5L, 3L, 6L, 4L)) == 7L)
stopifnot(max_profit(c(1L, 2L, 3L, 4L, 5L)) == 4L)
stopifnot(max_profit(c(7L, 6L, 4L, 3L, 1L)) == 0L)
cat("PASS\\n")
''',
"zig": '''const std = @import("std");
fn maxProfit(prices: []const i32) i32 {
    var profit: i32 = 0;
    for (1..prices.len) |i| {
        if (prices[i] > prices[i - 1]) profit += prices[i] - prices[i - 1];
    }
    return profit;
}
pub fn main() !void {
    if (maxProfit(&[_]i32{ 7, 1, 5, 3, 6, 4 }) != 7) return error.TestFailed;
    if (maxProfit(&[_]i32{ 1, 2, 3, 4, 5 }) != 4) return error.TestFailed;
    if (maxProfit(&[_]i32{ 7, 6, 4, 3, 1 }) != 0) return error.TestFailed;
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''int maxProfit(List<int> prices) {
  var profit = 0;
  for (var i = 1; i < prices.length; i++) {
    if (prices[i] > prices[i - 1]) {
      profit += prices[i] - prices[i - 1];
    }
  }
  return profit;
}
void main() {
  if (maxProfit([7, 1, 5, 3, 6, 4]) != 7) throw StateError('c1');
  if (maxProfit([1, 2, 3, 4, 5]) != 4) throw StateError('c2');
  if (maxProfit([7, 6, 4, 3, 1]) != 0) throw StateError('c3');
  print('PASS');
}
''',
}

A1518 = {
"rust": '''fn num_water_bottles(num_bottles: i32, num_exchange: i32) -> i32 {
    let mut ans = num_bottles;
    let mut empty = num_bottles;
    while empty >= num_exchange {
        let new_b = empty / num_exchange;
        ans += new_b;
        empty = new_b + empty % num_exchange;
    }
    ans
}
fn main() {
    assert_eq!(num_water_bottles(9, 3), 13);
    assert_eq!(num_water_bottles(15, 4), 19);
    println!("PASS");
}
''',
"lua": '''local function num_water_bottles(num_bottles, num_exchange)
    local ans, empty = num_bottles, num_bottles
    while empty >= num_exchange do
        local new_b = math.floor(empty / num_exchange)
        ans = ans + new_b
        empty = new_b + empty % num_exchange
    end
    return ans
end
assert(num_water_bottles(9, 3) == 13)
assert(num_water_bottles(15, 4) == 19)
print("PASS")
''',
"c": '''#include <stdio.h>
static int num_water_bottles(int num_bottles, int num_exchange) {
    int ans = num_bottles, empty = num_bottles;
    while (empty >= num_exchange) {
        int new_b = empty / num_exchange;
        ans += new_b;
        empty = new_b + empty % num_exchange;
    }
    return ans;
}
int main(void) {
    if (num_water_bottles(9, 3) != 13) { printf("FAIL 1\\n"); return 1; }
    if (num_water_bottles(15, 4) != 19) { printf("FAIL 2\\n"); return 1; }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''#include <cassert>
#include <iostream>
static int numWaterBottles(int numBottles, int numExchange) {
    int ans = numBottles, empty = numBottles;
    while (empty >= numExchange) {
        int newB = empty / numExchange;
        ans += newB;
        empty = newB + empty % numExchange;
    }
    return ans;
}
int main() {
    assert(numWaterBottles(9, 3) == 13);
    assert(numWaterBottles(15, 4) == 19);
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''num_water_bottles <- function(num_bottles, num_exchange) {
  ans <- num_bottles; empty <- num_bottles
  while (empty >= num_exchange) {
    new_b <- empty %/% num_exchange
    ans <- ans + new_b
    empty <- new_b + empty %% num_exchange
  }
  ans
}
stopifnot(num_water_bottles(9L, 3L) == 13L)
stopifnot(num_water_bottles(15L, 4L) == 19L)
cat("PASS\\n")
''',
"zig": '''const std = @import("std");
fn numWaterBottles(numBottles: i32, numExchange: i32) i32 {
    var ans = numBottles;
    var empty = numBottles;
    while (empty >= numExchange) {
        const newB = @divTrunc(empty, numExchange);
        ans += newB;
        empty = newB + @mod(empty, numExchange);
    }
    return ans;
}
pub fn main() !void {
    if (numWaterBottles(9, 3) != 13) return error.TestFailed;
    if (numWaterBottles(15, 4) != 19) return error.TestFailed;
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''int numWaterBottles(int numBottles, int numExchange) {
  var ans = numBottles;
  var empty = numBottles;
  while (empty >= numExchange) {
    final newB = empty ~/ numExchange;
    ans += newB;
    empty = newB + empty % numExchange;
  }
  return ans;
}
void main() {
  if (numWaterBottles(9, 3) != 13) throw StateError('c1');
  if (numWaterBottles(15, 4) != 19) throw StateError('c2');
  print('PASS');
}
''',
}

A435 = {
"rust": '''fn erase_overlap_intervals(intervals: Vec<Vec<i32>>) -> i32 {
    if intervals.is_empty() { return 0; }
    let mut arr = intervals;
    arr.sort_by_key(|x| x[1]);
    let mut count = 1;
    let mut end = arr[0][1];
    for iv in arr.iter().skip(1) {
        if iv[0] >= end { count += 1; end = iv[1]; }
    }
    arr.len() as i32 - count
}
fn main() {
    assert_eq!(erase_overlap_intervals(vec![vec![1, 2], vec![2, 3], vec![3, 4], vec![1, 3]]), 1);
    assert_eq!(erase_overlap_intervals(vec![]), 0);
    assert_eq!(erase_overlap_intervals(vec![vec![1, 2], vec![1, 2], vec![1, 2]]), 2);
    println!("PASS");
}
''',
"lua": '''local function erase_overlap_intervals(intervals)
    if #intervals == 0 then return 0 end
    local arr = {}
    for i, iv in ipairs(intervals) do arr[i] = {iv[1], iv[2]} end
    table.sort(arr, function(a, b) return a[2] < b[2] end)
    local count, end_ = 1, arr[1][2]
    for i = 2, #arr do
        if arr[i][1] >= end_ then
            count = count + 1
            end_ = arr[i][2]
        end
    end
    return #arr - count
end
assert(erase_overlap_intervals({{1, 2}, {2, 3}, {3, 4}, {1, 3}}) == 1)
assert(erase_overlap_intervals({}) == 0)
assert(erase_overlap_intervals({{1, 2}, {1, 2}, {1, 2}}) == 2)
print("PASS")
''',
"c": '''#include <stdio.h>
#include <stdlib.h>
static int cmp_iv(const void *a, const void *b) { return ((const int *)a)[1] - ((const int *)b)[1]; }
static int erase_overlap_intervals(int intervals[][2], int n) {
    if (n == 0) return 0;
    int arr[256][2];
    for (int i = 0; i < n; i++) { arr[i][0] = intervals[i][0]; arr[i][1] = intervals[i][1]; }
    qsort(arr, n, sizeof(int) * 2, cmp_iv);
    int count = 1, end = arr[0][1];
    for (int i = 1; i < n; i++) {
        if (arr[i][0] >= end) { count++; end = arr[i][1]; }
    }
    return n - count;
}
int main(void) {
    int v1[][2] = {{1,2},{2,3},{3,4},{1,3}};
    int v3[][2] = {{1,2},{1,2},{1,2}};
    if (erase_overlap_intervals(v1, 4) != 1) { printf("FAIL 1\\n"); return 1; }
    if (erase_overlap_intervals(NULL, 0) != 0) { printf("FAIL 2\\n"); return 1; }
    if (erase_overlap_intervals(v3, 3) != 2) { printf("FAIL 3\\n"); return 1; }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''#include <algorithm>
#include <cassert>
#include <iostream>
#include <vector>
static int eraseOverlapIntervals(std::vector<std::vector<int>> intervals) {
    if (intervals.empty()) return 0;
    std::sort(intervals.begin(), intervals.end(), [](auto &a, auto &b) { return a[1] < b[1]; });
    int count = 1;
    int end = intervals[0][1];
    for (size_t i = 1; i < intervals.size(); ++i) {
        if (intervals[i][0] >= end) { ++count; end = intervals[i][1]; }
    }
    return static_cast<int>(intervals.size()) - count;
}
int main() {
    assert(eraseOverlapIntervals({{1, 2}, {2, 3}, {3, 4}, {1, 3}}) == 1);
    assert(eraseOverlapIntervals({}) == 0);
    assert(eraseOverlapIntervals({{1, 2}, {1, 2}, {1, 2}}) == 2);
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''erase_overlap_intervals <- function(intervals) {
  if (nrow(intervals) == 0) return(0L)
  ord <- order(intervals[, 2])
  arr <- intervals[ord, , drop = FALSE]
  count <- 1L; end_ <- arr[1, 2]
  for (i in 2:nrow(arr)) {
    if (arr[i, 1] >= end_) { count <- count + 1L; end_ <- arr[i, 2] }
  }
  nrow(arr) - count
}
m1 <- matrix(c(1, 2, 2, 3, 3, 4, 1, 3), ncol = 2, byrow = TRUE)
m3 <- matrix(c(1, 2, 1, 2, 1, 2), ncol = 2, byrow = TRUE)
stopifnot(erase_overlap_intervals(m1) == 1L)
stopifnot(erase_overlap_intervals(matrix(integer(0), ncol = 2)) == 0L)
stopifnot(erase_overlap_intervals(m3) == 2L)
cat("PASS\\n")
''',
"zig": '''const std = @import("std");
const IV = struct { s: i32, e: i32 };
fn eraseOverlapIntervals(intervals: []const [2]i32) i32 {
    if (intervals.len == 0) return 0;
    var arr: [256]IV = undefined;
    for (intervals, 0..) |iv, i| arr[i] = .{ .s = iv[0], .e = iv[1] };
    const S = struct {
        fn lt(_: void, a: IV, b: IV) bool { return a.e < b.e; }
    };
    std.sort.pdq(IV, arr[0..intervals.len], {}, S.lt);
    var count: i32 = 1;
    var end: i32 = arr[0].e;
    for (1..intervals.len) |i| {
        if (arr[i].s >= end) { count += 1; end = arr[i].e; }
    }
    return @as(i32, @intCast(intervals.len)) - count;
}
pub fn main() !void {
    if (eraseOverlapIntervals(&[_][2]i32{ .{ 1, 2 }, .{ 2, 3 }, .{ 3, 4 }, .{ 1, 3 } }) != 1) return error.TestFailed;
    if (eraseOverlapIntervals(&[_][2]i32{}) != 0) return error.TestFailed;
    if (eraseOverlapIntervals(&[_][2]i32{ .{ 1, 2 }, .{ 1, 2 }, .{ 1, 2 } }) != 2) return error.TestFailed;
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''int eraseOverlapIntervals(List<List<int>> intervals) {
  if (intervals.isEmpty) return 0;
  final arr = List<List<int>>.from(intervals)
    ..sort((a, b) => a[1].compareTo(b[1]));
  var count = 1;
  var end = arr[0][1];
  for (var i = 1; i < arr.length; i++) {
    if (arr[i][0] >= end) {
      count++;
      end = arr[i][1];
    }
  }
  return arr.length - count;
}
void main() {
  if (eraseOverlapIntervals([
    [1, 2],
    [2, 3],
    [3, 4],
    [1, 3]
  ]) != 1) throw StateError('c1');
  if (eraseOverlapIntervals([]) != 0) throw StateError('c2');
  if (eraseOverlapIntervals([
    [1, 2],
    [1, 2],
    [1, 2]
  ]) != 2) throw StateError('c3');
  print('PASS');
}
''',
}

A452 = {
"rust": '''fn find_min_arrow_shots(mut points: Vec<Vec<i32>>) -> i32 {
    if points.is_empty() { return 0; }
    points.sort_by_key(|x| x[1]);
    let mut arrows = 1;
    let mut end = points[0][1];
    for p in points.iter().skip(1) {
        if p[0] > end { arrows += 1; end = p[1]; }
    }
    arrows
}
fn main() {
    assert_eq!(find_min_arrow_shots(vec![vec![10, 16], vec![2, 8], vec![1, 6], vec![7, 12]]), 2);
    assert_eq!(find_min_arrow_shots(vec![]), 0);
    assert_eq!(find_min_arrow_shots(vec![vec![1, 2], vec![3, 4], vec![5, 6], vec![7, 8]]), 4);
    println!("PASS");
}
''',
"lua": '''local function find_min_arrow_shots(points)
    if #points == 0 then return 0 end
    local arr = {}
    for i, p in ipairs(points) do arr[i] = {p[1], p[2]} end
    table.sort(arr, function(a, b) return a[2] < b[2] end)
    local arrows, end_ = 1, arr[1][2]
    for k = 2, #arr do
        if arr[k][1] > end_ then
            arrows = arrows + 1
            end_ = arr[k][2]
        end
    end
    return arrows
end
assert(find_min_arrow_shots({{10, 16}, {2, 8}, {1, 6}, {7, 12}}) == 2)
assert(find_min_arrow_shots({}) == 0)
assert(find_min_arrow_shots({{1, 2}, {3, 4}, {5, 6}, {7, 8}}) == 4)
print("PASS")
''',
"c": '''#include <stdio.h>
#include <stdlib.h>
static int cmp_iv(const void *a, const void *b) { return ((const int *)a)[1] - ((const int *)b)[1]; }
static int find_min_arrow_shots(int points[][2], int n) {
    if (n == 0) return 0;
    int arr[256][2];
    for (int i = 0; i < n; i++) { arr[i][0] = points[i][0]; arr[i][1] = points[i][1]; }
    qsort(arr, n, sizeof(int) * 2, cmp_iv);
    int arrows = 1, end = arr[0][1];
    for (int k = 1; k < n; k++) {
        if (arr[k][0] > end) { arrows++; end = arr[k][1]; }
    }
    return arrows;
}
int main(void) {
    int v1[][2] = {{10,16},{2,8},{1,6},{7,12}};
    int v3[][2] = {{1,2},{3,4},{5,6},{7,8}};
    if (find_min_arrow_shots(v1, 4) != 2) { printf("FAIL 1\\n"); return 1; }
    if (find_min_arrow_shots(NULL, 0) != 0) { printf("FAIL 2\\n"); return 1; }
    if (find_min_arrow_shots(v3, 4) != 4) { printf("FAIL 3\\n"); return 1; }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''#include <algorithm>
#include <cassert>
#include <iostream>
#include <vector>
static int findMinArrowShots(std::vector<std::vector<int>> points) {
    if (points.empty()) return 0;
    std::sort(points.begin(), points.end(), [](auto &a, auto &b) { return a[1] < b[1]; });
    int arrows = 1;
    int end = points[0][1];
    for (size_t k = 1; k < points.size(); ++k) {
        if (points[k][0] > end) { ++arrows; end = points[k][1]; }
    }
    return arrows;
}
int main() {
    assert(findMinArrowShots({{10, 16}, {2, 8}, {1, 6}, {7, 12}}) == 2);
    assert(findMinArrowShots({}) == 0);
    assert(findMinArrowShots({{1, 2}, {3, 4}, {5, 6}, {7, 8}}) == 4);
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''find_min_arrow_shots <- function(points) {
  if (nrow(points) == 0) return(0L)
  arr <- points[order(points[, 2]), , drop = FALSE]
  arrows <- 1L; end_ <- arr[1, 2]
  for (k in 2:nrow(arr)) {
    if (arr[k, 1] > end_) { arrows <- arrows + 1L; end_ <- arr[k, 2] }
  }
  arrows
}
m1 <- matrix(c(10, 16, 2, 8, 1, 6, 7, 12), ncol = 2, byrow = TRUE)
m3 <- matrix(c(1, 2, 3, 4, 5, 6, 7, 8), ncol = 2, byrow = TRUE)
stopifnot(find_min_arrow_shots(m1) == 2L)
stopifnot(find_min_arrow_shots(matrix(integer(0), ncol = 2)) == 0L)
stopifnot(find_min_arrow_shots(m3) == 4L)
cat("PASS\\n")
''',
"zig": '''const std = @import("std");
const IV = struct { s: i32, e: i32 };
fn findMinArrowShots(points: []const [2]i32) i32 {
    if (points.len == 0) return 0;
    var arr: [256]IV = undefined;
    for (points, 0..) |p, i| arr[i] = .{ .s = p[0], .e = p[1] };
    const S = struct {
        fn lt(_: void, a: IV, b: IV) bool { return a.e < b.e; }
    };
    std.sort.pdq(IV, arr[0..points.len], {}, S.lt);
    var arrows: i32 = 1;
    var end: i32 = arr[0].e;
    for (1..points.len) |k| {
        if (arr[k].s > end) { arrows += 1; end = arr[k].e; }
    }
    return arrows;
}
pub fn main() !void {
    if (findMinArrowShots(&[_][2]i32{ .{ 10, 16 }, .{ 2, 8 }, .{ 1, 6 }, .{ 7, 12 } }) != 2) return error.TestFailed;
    if (findMinArrowShots(&[_][2]i32{}) != 0) return error.TestFailed;
    if (findMinArrowShots(&[_][2]i32{ .{ 1, 2 }, .{ 3, 4 }, .{ 5, 6 }, .{ 7, 8 } }) != 4) return error.TestFailed;
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''int findMinArrowShots(List<List<int>> points) {
  if (points.isEmpty) return 0;
  final arr = List<List<int>>.from(points)
    ..sort((a, b) => a[1].compareTo(b[1]));
  var arrows = 1;
  var end = arr[0][1];
  for (var k = 1; k < arr.length; k++) {
    if (arr[k][0] > end) {
      arrows++;
      end = arr[k][1];
    }
  }
  return arrows;
}
void main() {
  if (findMinArrowShots([
    [10, 16],
    [2, 8],
    [1, 6],
    [7, 12]
  ]) != 2) throw StateError('c1');
  if (findMinArrowShots([]) != 0) throw StateError('c2');
  if (findMinArrowShots([
    [1, 2],
    [3, 4],
    [5, 6],
    [7, 8]
  ]) != 4) throw StateError('c3');
  print('PASS');
}
''',
}

A455 = {
"rust": '''fn find_content_children(mut g: Vec<i32>, mut s: Vec<i32>) -> i32 {
    g.sort();
    s.sort();
    let (mut child, mut cookie) = (0usize, 0usize);
    while child < g.len() && cookie < s.len() {
        if s[cookie] >= g[child] { child += 1; }
        cookie += 1;
    }
    child as i32
}
fn main() {
    assert_eq!(find_content_children(vec![1, 2, 3], vec![1, 1]), 1);
    assert_eq!(find_content_children(vec![1, 2], vec![1, 2, 3]), 2);
    println!("PASS");
}
''',
"lua": '''local function find_content_children(g, s)
    table.sort(g)
    table.sort(s)
    local child, cookie = 1, 1
    while child <= #g and cookie <= #s do
        if s[cookie] >= g[child] then child = child + 1 end
        cookie = cookie + 1
    end
    return child - 1
end
assert(find_content_children({1, 2, 3}, {1, 1}) == 1)
assert(find_content_children({1, 2}, {1, 2, 3}) == 2)
print("PASS")
''',
"c": '''#include <stdio.h>
#include <stdlib.h>
static int cmp_int(const void *a, const void *b) { return *(const int *)a - *(const int *)b; }
static int find_content_children(int *g, int ng, int *s, int ns) {
    qsort(g, ng, sizeof(int), cmp_int);
    qsort(s, ns, sizeof(int), cmp_int);
    int child = 0, cookie = 0;
    while (child < ng && cookie < ns) {
        if (s[cookie] >= g[child]) child++;
        cookie++;
    }
    return child;
}
int main(void) {
    int g1[] = {1,2,3}, s1[] = {1,1};
    int g2[] = {1,2}, s2[] = {1,2,3};
    if (find_content_children(g1, 3, s1, 2) != 1) { printf("FAIL 1\\n"); return 1; }
    if (find_content_children(g2, 2, s2, 3) != 2) { printf("FAIL 2\\n"); return 1; }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''#include <algorithm>
#include <cassert>
#include <iostream>
#include <vector>
static int findContentChildren(std::vector<int> g, std::vector<int> s) {
    std::sort(g.begin(), g.end());
    std::sort(s.begin(), s.end());
    size_t child = 0, cookie = 0;
    while (child < g.size() && cookie < s.size()) {
        if (s[cookie] >= g[child]) ++child;
        ++cookie;
    }
    return static_cast<int>(child);
}
int main() {
    assert(findContentChildren({1, 2, 3}, {1, 1}) == 1);
    assert(findContentChildren({1, 2}, {1, 2, 3}) == 2);
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''find_content_children <- function(g, s) {
  g <- sort(g); s <- sort(s)
  child <- 1L; cookie <- 1L
  while (child <= length(g) && cookie <= length(s)) {
    if (s[cookie] >= g[child]) child <- child + 1L
    cookie <- cookie + 1L
  }
  child - 1L
}
stopifnot(find_content_children(c(1, 2, 3), c(1, 1)) == 1)
stopifnot(find_content_children(c(1, 2), c(1, 2, 3)) == 2)
cat("PASS\\n")
''',
"zig": '''const std = @import("std");
fn findContentChildren(g_in: []const i32, s_in: []const i32, alloc: std.mem.Allocator) i32 {
    const g = alloc.dupe(i32, g_in) catch unreachable;
    const s = alloc.dupe(i32, s_in) catch unreachable;
    std.sort.pdq(i32, g, {}, std.sort.asc(i32));
    std.sort.pdq(i32, s, {}, std.sort.asc(i32));
    var child: usize = 0;
    var cookie: usize = 0;
    while (child < g.len and cookie < s.len) {
        if (s[cookie] >= g[child]) child += 1;
        cookie += 1;
    }
    return @intCast(child);
}
pub fn main() !void {
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();
    const alloc = arena.allocator();
    if (findContentChildren(&[_]i32{ 1, 2, 3 }, &[_]i32{ 1, 1 }, alloc) != 1) return error.TestFailed;
    if (findContentChildren(&[_]i32{ 1, 2 }, &[_]i32{ 1, 2, 3 }, alloc) != 2) return error.TestFailed;
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''int findContentChildren(List<int> g, List<int> s) {
  final gg = List<int>.from(g)..sort();
  final ss = List<int>.from(s)..sort();
  var child = 0, cookie = 0;
  while (child < gg.length && cookie < ss.length) {
    if (ss[cookie] >= gg[child]) child++;
    cookie++;
  }
  return child;
}
void main() {
  if (findContentChildren([1, 2, 3], [1, 1]) != 1) throw StateError('c1');
  if (findContentChildren([1, 2], [1, 2, 3]) != 2) throw StateError('c2');
  print('PASS');
}
''',
}

A45 = {
"rust": '''fn jump(nums: Vec<i32>) -> i32 {
    let mut position = nums.len() - 1;
    let mut steps = 0;
    while position > 0 {
        for i in 0..position {
            if i + nums[i] as usize >= position {
                position = i;
                steps += 1;
                break;
            }
        }
    }
    steps
}
fn main() {
    assert_eq!(jump(vec![2, 3, 1, 1, 4]), 2);
    assert_eq!(jump(vec![2, 3, 0, 1, 4]), 2);
    assert_eq!(jump(vec![1]), 0);
    println!("PASS");
}
''',
"lua": '''local function jump(nums)
    local position, steps = #nums, 0
    while position > 1 do
        for i = 1, position - 1 do
            if i - 1 + nums[i] >= position - 1 then
                position = i
                steps = steps + 1
                break
            end
        end
    end
    return steps
end
assert(jump({2, 3, 1, 1, 4}) == 2)
assert(jump({2, 3, 0, 1, 4}) == 2)
assert(jump({1}) == 0)
print("PASS")
''',
"c": '''#include <stdio.h>
static int jump(const int *nums, int n) {
    int position = n - 1, steps = 0;
    while (position > 0) {
        for (int i = 0; i < position; i++) {
            if (i + nums[i] >= position) { position = i; steps++; break; }
        }
    }
    return steps;
}
int main(void) {
    if (jump((int[]){2,3,1,1,4}, 5) != 2) { printf("FAIL 1\\n"); return 1; }
    if (jump((int[]){2,3,0,1,4}, 5) != 2) { printf("FAIL 2\\n"); return 1; }
    if (jump((int[]){1}, 1) != 0) { printf("FAIL 3\\n"); return 1; }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''#include <cassert>
#include <iostream>
#include <vector>
static int jump(const std::vector<int> &nums) {
    int position = static_cast<int>(nums.size()) - 1, steps = 0;
    while (position > 0) {
        for (int i = 0; i < position; ++i) {
            if (i + nums[i] >= position) { position = i; ++steps; break; }
        }
    }
    return steps;
}
int main() {
    assert(jump({2, 3, 1, 1, 4}) == 2);
    assert(jump({2, 3, 0, 1, 4}) == 2);
    assert(jump({1}) == 0);
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''jump <- function(nums) {
  position <- length(nums); steps <- 0L
  while (position > 1L) {
    for (i in 1:(position - 1L)) {
      if ((i - 1L) + nums[i] >= position - 1L) {
        position <- i
        steps <- steps + 1L
        break
      }
    }
  }
  steps
}
stopifnot(jump(c(2, 3, 1, 1, 4)) == 2)
stopifnot(jump(c(2, 3, 0, 1, 4)) == 2)
stopifnot(jump(c(1)) == 0)
cat("PASS\\n")
''',
"zig": '''const std = @import("std");
fn jump(nums: []const i32) i32 {
    var position: usize = nums.len - 1;
    var steps: i32 = 0;
    while (position > 0) {
        for (0..position) |i| {
            if (i + @as(usize, @intCast(nums[i])) >= position) {
                position = i;
                steps += 1;
                break;
            }
        }
    }
    return steps;
}
pub fn main() !void {
    if (jump(&[_]i32{ 2, 3, 1, 1, 4 }) != 2) return error.TestFailed;
    if (jump(&[_]i32{ 2, 3, 0, 1, 4 }) != 2) return error.TestFailed;
    if (jump(&[_]i32{1}) != 0) return error.TestFailed;
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''int jump(List<int> nums) {
  var position = nums.length - 1;
  var steps = 0;
  while (position > 0) {
    for (var i = 0; i < position; i++) {
      if (i + nums[i] >= position) {
        position = i;
        steps++;
        break;
      }
    }
  }
  return steps;
}
void main() {
  if (jump([2, 3, 1, 1, 4]) != 2) throw StateError('c1');
  if (jump([2, 3, 0, 1, 4]) != 2) throw StateError('c2');
  if (jump([1]) != 0) throw StateError('c3');
  print('PASS');
}
''',
}

A55 = {
"rust": '''fn can_jump(nums: Vec<i32>) -> bool {
    let mut max_reach = 0usize;
    for i in 0..nums.len() {
        if i > max_reach { return false; }
        let r = i + nums[i] as usize;
        if r > max_reach { max_reach = r; }
    }
    true
}
fn main() {
    assert!(can_jump(vec![2, 3, 1, 1, 4]));
    assert!(!can_jump(vec![3, 2, 1, 0, 4]));
    println!("PASS");
}
''',
"lua": '''local function can_jump(nums)
    local max_reach = 0
    for i = 1, #nums do
        if i - 1 > max_reach then return false end
        local r = (i - 1) + nums[i]
        if r > max_reach then max_reach = r end
    end
    return true
end
assert(can_jump({2, 3, 1, 1, 4}) == true)
assert(can_jump({3, 2, 1, 0, 4}) == false)
print("PASS")
''',
"c": '''#include <stdio.h>
static int can_jump(const int *nums, int n) {
    int max_reach = 0;
    for (int i = 0; i < n; i++) {
        if (i > max_reach) return 0;
        if (i + nums[i] > max_reach) max_reach = i + nums[i];
    }
    return 1;
}
int main(void) {
    if (!can_jump((int[]){2,3,1,1,4}, 5)) { printf("FAIL 1\\n"); return 1; }
    if (can_jump((int[]){3,2,1,0,4}, 5)) { printf("FAIL 2\\n"); return 1; }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''#include <cassert>
#include <iostream>
#include <vector>
static bool canJump(const std::vector<int> &nums) {
    int maxReach = 0;
    for (int i = 0; i < static_cast<int>(nums.size()); ++i) {
        if (i > maxReach) return false;
        maxReach = std::max(maxReach, i + nums[i]);
    }
    return true;
}
int main() {
    assert(canJump({2, 3, 1, 1, 4}));
    assert(!canJump({3, 2, 1, 0, 4}));
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''can_jump <- function(nums) {
  max_reach <- 0L
  for (i in seq_along(nums)) {
    if ((i - 1L) > max_reach) return(FALSE)
    r <- (i - 1L) + nums[i]
    if (r > max_reach) max_reach <- r
  }
  TRUE
}
stopifnot(can_jump(c(2, 3, 1, 1, 4)))
stopifnot(!can_jump(c(3, 2, 1, 0, 4)))
cat("PASS\\n")
''',
"zig": '''const std = @import("std");
fn canJump(nums: []const i32) bool {
    var max_reach: usize = 0;
    for (nums, 0..) |v, i| {
        if (i > max_reach) return false;
        const r = i + @as(usize, @intCast(v));
        if (r > max_reach) max_reach = r;
    }
    return true;
}
pub fn main() !void {
    if (!canJump(&[_]i32{ 2, 3, 1, 1, 4 })) return error.TestFailed;
    if (canJump(&[_]i32{ 3, 2, 1, 0, 4 })) return error.TestFailed;
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''bool canJump(List<int> nums) {
  var maxReach = 0;
  for (var i = 0; i < nums.length; i++) {
    if (i > maxReach) return false;
    final r = i + nums[i];
    if (r > maxReach) maxReach = r;
  }
  return true;
}
void main() {
  if (!canJump([2, 3, 1, 1, 4])) throw StateError('c1');
  if (canJump([3, 2, 1, 0, 4])) throw StateError('c2');
  print('PASS');
}
''',
}

A649 = {
"rust": '''fn predict_party_victory(senate: &str) -> String {
    let n = senate.len() as i32;
    let mut radiant: std::collections::VecDeque<i32> = Default::default();
    let mut dire: std::collections::VecDeque<i32> = Default::default();
    for (i, c) in senate.chars().enumerate() {
        if c == 'R' { radiant.push_back(i as i32); } else { dire.push_back(i as i32); }
    }
    while !radiant.is_empty() && !dire.is_empty() {
        let r = radiant.pop_front().unwrap();
        let d = dire.pop_front().unwrap();
        if r < d { radiant.push_back(r + n); } else { dire.push_back(d + n); }
    }
    if radiant.is_empty() { "Dire".to_string() } else { "Radiant".to_string() }
}
fn main() {
    assert_eq!(predict_party_victory("RD"), "Radiant");
    assert_eq!(predict_party_victory("DDR"), "Dire");
    println!("PASS");
}
''',
"lua": '''local function predict_party_victory(senate)
    local n = #senate
    local radiant, dire = {}, {}
    local rh, dh = 1, 1
    for i = 1, n do
        if senate:sub(i, i) == "R" then radiant[#radiant + 1] = i - 1 else dire[#dire + 1] = i - 1 end
    end
    while rh <= #radiant and dh <= #dire do
        local r = radiant[rh]; rh = rh + 1
        local d = dire[dh]; dh = dh + 1
        if r < d then radiant[#radiant + 1] = r + n else dire[#dire + 1] = d + n end
    end
    if rh > #radiant then return "Dire" else return "Radiant" end
end
assert(predict_party_victory("RD") == "Radiant")
assert(predict_party_victory("DDR") == "Dire")
print("PASS")
''',
"c": '''#include <stdio.h>
#include <string.h>
static const char *predict_party_victory(const char *senate) {
    int n = (int)strlen(senate);
    int radiant[8192], dire[8192];
    int rn = 0, dn = 0, rh = 0, dh = 0;
    for (int i = 0; i < n; i++) {
        if (senate[i] == 'R') radiant[rn++] = i;
        else dire[dn++] = i;
    }
    while (rh < rn && dh < dn) {
        int r = radiant[rh++];
        int d = dire[dh++];
        if (r < d) radiant[rn++] = r + n;
        else dire[dn++] = d + n;
    }
    return rh >= rn ? "Dire" : "Radiant";
}
int main(void) {
    if (strcmp(predict_party_victory("RD"), "Radiant") != 0) { printf("FAIL 1\\n"); return 1; }
    if (strcmp(predict_party_victory("DDR"), "Dire") != 0) { printf("FAIL 2\\n"); return 1; }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''#include <cassert>
#include <deque>
#include <iostream>
#include <string>
static std::string predictPartyVictory(const std::string &senate) {
    int n = static_cast<int>(senate.size());
    std::deque<int> radiant, dire;
    for (int i = 0; i < n; ++i) {
        if (senate[i] == 'R') radiant.push_back(i);
        else dire.push_back(i);
    }
    while (!radiant.empty() && !dire.empty()) {
        int r = radiant.front();
        radiant.pop_front();
        int d = dire.front();
        dire.pop_front();
        if (r < d) radiant.push_back(r + n);
        else dire.push_back(d + n);
    }
    return radiant.empty() ? "Dire" : "Radiant";
}
int main() {
    assert(predictPartyVictory("RD") == "Radiant");
    assert(predictPartyVictory("DDR") == "Dire");
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''predict_party_victory <- function(senate) {
  chars <- strsplit(senate, "")[[1]]
  n <- length(chars)
  radiant <- which(chars == "R") - 1L
  dire <- which(chars != "R") - 1L
  rh <- 1L; dh <- 1L
  while (rh <= length(radiant) && dh <= length(dire)) {
    r <- radiant[rh]; rh <- rh + 1L
    d <- dire[dh]; dh <- dh + 1L
    if (r < d) radiant <- c(radiant, r + n) else dire <- c(dire, d + n)
  }
  if (rh > length(radiant)) "Dire" else "Radiant"
}
stopifnot(predict_party_victory("RD") == "Radiant")
stopifnot(predict_party_victory("DDR") == "Dire")
cat("PASS\\n")
''',
"zig": '''const std = @import("std");
fn predictPartyVictory(senate: []const u8) []const u8 {
    const n: i32 = @intCast(senate.len);
    var radiant_buf: [8192]i32 = undefined;
    var dire_buf: [8192]i32 = undefined;
    var rn: usize = 0;
    var dn: usize = 0;
    var rh: usize = 0;
    var dh: usize = 0;
    for (senate, 0..) |c, i| {
        if (c == 'R') {
            radiant_buf[rn] = @intCast(i);
            rn += 1;
        } else {
            dire_buf[dn] = @intCast(i);
            dn += 1;
        }
    }
    while (rh < rn and dh < dn) {
        const r = radiant_buf[rh];
        rh += 1;
        const d = dire_buf[dh];
        dh += 1;
        if (r < d) {
            radiant_buf[rn] = r + n;
            rn += 1;
        } else {
            dire_buf[dn] = d + n;
            dn += 1;
        }
    }
    return if (rh >= rn) "Dire" else "Radiant";
}
pub fn main() !void {
    if (!std.mem.eql(u8, predictPartyVictory("RD"), "Radiant")) return error.TestFailed;
    if (!std.mem.eql(u8, predictPartyVictory("DDR"), "Dire")) return error.TestFailed;
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''String predictPartyVictory(String senate) {
  final n = senate.length;
  final radiant = <int>[];
  final dire = <int>[];
  for (var i = 0; i < n; i++) {
    if (senate[i] == 'R') {
      radiant.add(i);
    } else {
      dire.add(i);
    }
  }
  var rh = 0, dh = 0;
  while (rh < radiant.length && dh < dire.length) {
    final r = radiant[rh++];
    final d = dire[dh++];
    if (r < d) {
      radiant.add(r + n);
    } else {
      dire.add(d + n);
    }
  }
  return rh >= radiant.length ? 'Dire' : 'Radiant';
}
void main() {
  if (predictPartyVictory('RD') != 'Radiant') throw StateError('c1');
  if (predictPartyVictory('DDR') != 'Dire') throw StateError('c2');
  print('PASS');
}
''',
}

A860 = {
"rust": '''fn lemonade_change(bills: Vec<i32>) -> bool {
    let (mut f5, mut f10) = (0i32, 0i32);
    for b in bills {
        if b == 5 { f5 += 1; }
        else if b == 10 { f10 += 1; f5 -= 1; }
        else {
            if f10 > 0 { f10 -= 1; f5 -= 1; }
            else { f5 -= 3; }
        }
        if f5 < 0 { return false; }
    }
    true
}
fn main() {
    assert!(lemonade_change(vec![5, 5, 5, 10, 20]));
    assert!(!lemonade_change(vec![5, 5, 10, 10, 20]));
    assert!(lemonade_change(vec![5, 5, 5, 5, 20]));
    println!("PASS");
}
''',
"lua": '''local function lemonade_change(bills)
    local f5, f10 = 0, 0
    for _, b in ipairs(bills) do
        if b == 5 then
            f5 = f5 + 1
        elseif b == 10 then
            f10 = f10 + 1; f5 = f5 - 1
        else
            if f10 > 0 then f10 = f10 - 1; f5 = f5 - 1 else f5 = f5 - 3 end
        end
        if f5 < 0 then return false end
    end
    return true
end
assert(lemonade_change({5, 5, 5, 10, 20}) == true)
assert(lemonade_change({5, 5, 10, 10, 20}) == false)
assert(lemonade_change({5, 5, 5, 5, 20}) == true)
print("PASS")
''',
"c": '''#include <stdio.h>
static int lemonade_change(const int *bills, int n) {
    int f5 = 0, f10 = 0;
    for (int i = 0; i < n; i++) {
        if (bills[i] == 5) f5++;
        else if (bills[i] == 10) { f10++; f5--; }
        else {
            if (f10 > 0) { f10--; f5--; } else f5 -= 3;
        }
        if (f5 < 0) return 0;
    }
    return 1;
}
int main(void) {
    if (!lemonade_change((int[]){5,5,5,10,20}, 5)) { printf("FAIL 1\\n"); return 1; }
    if (lemonade_change((int[]){5,5,10,10,20}, 5)) { printf("FAIL 2\\n"); return 1; }
    if (!lemonade_change((int[]){5,5,5,5,20}, 5)) { printf("FAIL 3\\n"); return 1; }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''#include <cassert>
#include <iostream>
#include <vector>
static bool lemonadeChange(const std::vector<int> &bills) {
    int f5 = 0, f10 = 0;
    for (int b : bills) {
        if (b == 5) ++f5;
        else if (b == 10) { ++f10; --f5; }
        else {
            if (f10 > 0) { --f10; --f5; }
            else f5 -= 3;
        }
        if (f5 < 0) return false;
    }
    return true;
}
int main() {
    assert(lemonadeChange({5, 5, 5, 10, 20}));
    assert(!lemonadeChange({5, 5, 10, 10, 20}));
    assert(lemonadeChange({5, 5, 5, 5, 20}));
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''lemonade_change <- function(bills) {
  f5 <- 0L; f10 <- 0L
  for (b in bills) {
    if (b == 5) f5 <- f5 + 1L
    else if (b == 10) { f10 <- f10 + 1L; f5 <- f5 - 1L }
    else {
      if (f10 > 0) { f10 <- f10 - 1L; f5 <- f5 - 1L } else f5 <- f5 - 3L
    }
    if (f5 < 0) return(FALSE)
  }
  TRUE
}
stopifnot(lemonade_change(c(5L, 5L, 5L, 10L, 20L)))
stopifnot(!lemonade_change(c(5L, 5L, 10L, 10L, 20L)))
stopifnot(lemonade_change(c(5L, 5L, 5L, 5L, 20L)))
cat("PASS\\n")
''',
"zig": '''const std = @import("std");
fn lemonadeChange(bills: []const i32) bool {
    var f5: i32 = 0;
    var f10: i32 = 0;
    for (bills) |b| {
        if (b == 5) {
            f5 += 1;
        } else if (b == 10) {
            f10 += 1;
            f5 -= 1;
        } else {
            if (f10 > 0) {
                f10 -= 1;
                f5 -= 1;
            } else {
                f5 -= 3;
            }
        }
        if (f5 < 0) return false;
    }
    return true;
}
pub fn main() !void {
    if (!lemonadeChange(&[_]i32{ 5, 5, 5, 10, 20 })) return error.TestFailed;
    if (lemonadeChange(&[_]i32{ 5, 5, 10, 10, 20 })) return error.TestFailed;
    if (!lemonadeChange(&[_]i32{ 5, 5, 5, 5, 20 })) return error.TestFailed;
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''bool lemonadeChange(List<int> bills) {
  var f5 = 0, f10 = 0;
  for (final b in bills) {
    if (b == 5) {
      f5++;
    } else if (b == 10) {
      f10++;
      f5--;
    } else {
      if (f10 > 0) {
        f10--;
        f5--;
      } else {
        f5 -= 3;
      }
    }
    if (f5 < 0) return false;
  }
  return true;
}
void main() {
  if (!lemonadeChange([5, 5, 5, 10, 20])) throw StateError('c1');
  if (lemonadeChange([5, 5, 10, 10, 20])) throw StateError('c2');
  if (!lemonadeChange([5, 5, 5, 5, 20])) throw StateError('c3');
  print('PASS');
}
''',
}

PROBS = [
    ("lc_122_买卖股票的最佳时机ii", A122, "LeetCode 122. 买卖股票的最佳时机II"),
    ("lc_1518_换水问题", A1518, "LeetCode 1518. 换水问题"),
    ("lc_435_无重叠区间", A435, "LeetCode 435. 无重叠区间"),
    ("lc_452_用最少数量的箭引爆气球", A452, "LeetCode 452. 用最少数量的箭引爆气球"),
    ("lc_455_分饼干", A455, "LeetCode 455. 分发饼干"),
    ("lc_45_跳跃游戏_ii", A45, "LeetCode 45. 跳跃游戏II"),
    ("lc_55_跳跃游戏", A55, "LeetCode 55. 跳跃游戏"),
    ("lc_649_dota2_参议院", A649, "LeetCode 649. Dota2参议院"),
    ("lc_860_柠檬水找零", A860, "LeetCode 860. 柠檬水找零"),
]
count = 0
for prob, algo, title in PROBS:
    bid = B[prob.split("_")[1]]
    ts_dir = f"/Users/Wang/Code/github/web-x-blog/work/blog/courses/20.dsa/ts/greedy/{prob}"
    sols = sorted(f[:-3] for f in os.listdir(ts_dir) if f.startswith("solution_") and f.endswith(".ts"))
    for lang in EXT:
        ext = EXT[lang]
        for sol in sols:
            n = sol.replace("solution_", "").split("_")[0]
            head = head_comment(lang, bid, f"{title} — {LANGNAME[lang]} 版（方案{n}）")
            emit(lang, f"greedy/{prob}/{sol}.{ext}", head + "\n" + algo[lang])
            count += 1
print(f"emitted {count} files")
