#!/usr/bin/env python3
# gen_dp1.py — dp 第一批 15 题 × 7语言（纯单括号模板）
import sys, os; sys.path.insert(0, "/Users/Wang/Code/github/web-x-blog/work/blog/courses/20.dsa/_tools")
from langlib import emit, head_comment, EXT

B = {"509":"130510175","70":"130506068","746":"130521152","53":"130497821","198":"130644389","213":"130716392","121":"130515763","322":"130683917","518":"130734179","62":"130641517","63":"130704336","300":"130727613","674":"130771608","1143":"130815631","392":"130753613"}
LANGNAME = {"rust": "Rust", "lua": "Lua", "c": "C", "cpp": "C++", "r": "R", "zig": "Zig", "dart": "Dart"}

T = {}
T["509"] = {
"rust":'''fn fib(n: i32) -> i32 { if n < 2 { return n; } let (mut a, mut b) = (0, 1); for _ in 2..=n { let t = a + b; a = b; b = t; } b }
fn main() { assert_eq!(fib(2), 1); assert_eq!(fib(3), 2); assert_eq!(fib(4), 3); assert_eq!(fib(10), 55); println!("PASS"); }''',
"lua":'''local function fib(n) if n < 2 then return n end local a, b = 0, 1 for _ = 2, n do a, b = b, a + b end return b end
assert(fib(2) == 1); assert(fib(3) == 2); assert(fib(4) == 3); assert(fib(10) == 55); print("PASS")''',
"c":'''#include <stdio.h>
static int fib(int n) { if (n < 2) return n; int a = 0, b = 1; for (int i = 2; i <= n; i++) { int t = a + b; a = b; b = t; } return b; }
int main(void) { if (fib(2) != 1 || fib(3) != 2 || fib(4) != 3 || fib(10) != 55) { printf("FAIL\\n"); return 1; } printf("PASS\\n"); return 0; }''',
"cpp":'''#include <cassert>
#include <iostream>
static int fib(int n) { if (n < 2) return n; int a = 0, b = 1; for (int i = 2; i <= n; ++i) { int t = a + b; a = b; b = t; } return b; }
int main() { assert(fib(2) == 1); assert(fib(3) == 2); assert(fib(4) == 3); assert(fib(10) == 55); std::cout << "PASS" << std::endl; }''',
"r":'''fib <- function(n) { if (n < 2) return(n) ; a <- 0; b <- 1; for (i in 2:n) { t <- a + b; a <- b; b <- t }; b }
stopifnot(fib(2) == 1, fib(3) == 2, fib(4) == 3, fib(10) == 55)
cat("PASS\\n")''',
"zig":'''const std = @import("std");
fn fib(n: i32) i32 { if (n < 2) return n; var a: i32 = 0; var b: i32 = 1; var i: i32 = 2; while (i <= n) : (i += 1) { const t = a + b; a = b; b = t; } return b; }
pub fn main() !void { if (fib(2) != 1 or fib(3) != 2 or fib(4) != 3 or fib(10) != 55) return error.TestFailed; std.debug.print("PASS\\n", .{}); }''',
"dart":'''int fib(int n) { if (n < 2) return n; var a = 0, b = 1; for (var i = 2; i <= n; i++) { final t = a + b; a = b; b = t; } return b; }
void main() { if (fib(2) != 1 || fib(3) != 2 || fib(4) != 3 || fib(10) != 55) throw StateError('x'); print('PASS'); }''',
}
T["70"] = {
"rust":'''fn climb_stairs(n: i32) -> i32 { if n <= 2 { return n; } let (mut a, mut b) = (1, 2); for _ in 3..=n { let t = a + b; a = b; b = t; } b }
fn main() { assert_eq!(climb_stairs(2), 2); assert_eq!(climb_stairs(3), 3); assert_eq!(climb_stairs(10), 89); println!("PASS"); }''',
"lua":'''local function climb_stairs(n) if n <= 2 then return n end local a, b = 1, 2 for _ = 3, n do a, b = b, a + b end return b end
assert(climb_stairs(2) == 2); assert(climb_stairs(3) == 3); assert(climb_stairs(10) == 89); print("PASS")''',
"c":'''#include <stdio.h>
static int climb_stairs(int n) { if (n <= 2) return n; int a = 1, b = 2; for (int i = 3; i <= n; i++) { int t = a + b; a = b; b = t; } return b; }
int main(void) { if (climb_stairs(2) != 2 || climb_stairs(3) != 3 || climb_stairs(10) != 89) { printf("FAIL\\n"); return 1; } printf("PASS\\n"); return 0; }''',
"cpp":'''#include <cassert>
#include <iostream>
static int climbStairs(int n) { if (n <= 2) return n; int a = 1, b = 2; for (int i = 3; i <= n; ++i) { int t = a + b; a = b; b = t; } return b; }
int main() { assert(climbStairs(2) == 2); assert(climbStairs(3) == 3); assert(climbStairs(10) == 89); std::cout << "PASS" << std::endl; }''',
"r":'''climb_stairs <- function(n) { if (n <= 2) return(n); a <- 1L; b <- 2L; for (i in 3:n) { t <- a + b; a <- b; b <- t }; b }
stopifnot(climb_stairs(2) == 2, climb_stairs(3) == 3, climb_stairs(10) == 89)
cat("PASS\\n")''',
"zig":'''const std = @import("std");
fn climbStairs(n: i32) i32 { if (n <= 2) return n; var a: i32 = 1; var b: i32 = 2; var i: i32 = 3; while (i <= n) : (i += 1) { const t = a + b; a = b; b = t; } return b; }
pub fn main() !void { if (climbStairs(2) != 2 or climbStairs(3) != 3 or climbStairs(10) != 89) return error.TestFailed; std.debug.print("PASS\\n", .{}); }''',
"dart":'''int climbStairs(int n) { if (n <= 2) return n; var a = 1, b = 2; for (var i = 3; i <= n; i++) { final t = a + b; a = b; b = t; } return b; }
void main() { if (climbStairs(2) != 2 || climbStairs(3) != 3 || climbStairs(10) != 89) throw StateError('x'); print('PASS'); }''',
}
T["746"] = {
"rust":'''fn min_cost_climbing_stairs(cost: Vec<i32>) -> i32 {
    let (mut a, mut b) = (0, 0);
    for i in 2..=cost.len() {
        let t = (a + cost[i - 2]).min(b + cost[i - 1]);
        a = b; b = t;
    }
    b
}
fn main() { assert_eq!(min_cost_climbing_stairs(vec![10,15,20]), 15); assert_eq!(min_cost_climbing_stairs(vec![1,100,1,1,1,100,1,1,100,1]), 6); println!("PASS"); }''',
"lua":'''local function min_cost_climbing_stairs(cost)
    local a, b = 0, 0
    for i = 3, #cost + 1 do
        local t = math.min(a + cost[i - 2], b + cost[i - 1])
        a, b = b, t
    end
    return b
end
assert(min_cost_climbing_stairs({10,15,20}) == 15)
assert(min_cost_climbing_stairs({1,100,1,1,1,100,1,1,100,1}) == 6)
print("PASS")''',
"c":'''#include <stdio.h>
static int min_cost_climbing_stairs(const int *cost, int n) {
    int a = 0, b = 0;
    for (int i = 2; i <= n; i++) {
        int x = a + cost[i - 2], y = b + cost[i - 1];
        int t = x < y ? x : y;
        a = b; b = t;
    }
    return b;
}
int main(void) {
    if (min_cost_climbing_stairs((int[]){10,15,20}, 3) != 15) { printf("FAIL 1\\n"); return 1; }
    if (min_cost_climbing_stairs((int[]){1,100,1,1,1,100,1,1,100,1}, 10) != 6) { printf("FAIL 2\\n"); return 1; }
    printf("PASS\\n"); return 0; }''',
"cpp":'''#include <algorithm>
#include <cassert>
#include <iostream>
#include <vector>
static int minCostClimbingStairs(const std::vector<int> &cost) {
    int a = 0, b = 0;
    for (size_t i = 2; i <= cost.size(); ++i) {
        int t = std::min(a + cost[i - 2], b + cost[i - 1]);
        a = b; b = t;
    }
    return b;
}
int main() { assert(minCostClimbingStairs({10,15,20}) == 15); assert(minCostClimbingStairs({1,100,1,1,1,100,1,1,100,1}) == 6); std::cout << "PASS" << std::endl; }''',
"r":'''min_cost_climbing_stairs <- function(cost) {
  a <- 0; b <- 0
  for (i in 3:(length(cost) + 1)) {
    t <- min(a + cost[i - 2], b + cost[i - 1])
    a <- b; b <- t
  }
  b
}
stopifnot(min_cost_climbing_stairs(c(10, 15, 20)) == 15)
stopifnot(min_cost_climbing_stairs(c(1, 100, 1, 1, 1, 100, 1, 1, 100, 1)) == 6)
cat("PASS\\n")''',
"zig":'''const std = @import("std");
fn minCostClimbingStairs(cost: []const i32) i32 {
    var a: i32 = 0;
    var b: i32 = 0;
    for (2..cost.len + 1) |i| {
        const x = a + cost[i - 2];
        const y = b + cost[i - 1];
        const t = if (x < y) x else y;
        a = b;
        b = t;
    }
    return b;
}
pub fn main() !void {
    if (minCostClimbingStairs(&[_]i32{ 10, 15, 20 }) != 15) return error.TestFailed;
    if (minCostClimbingStairs(&[_]i32{ 1, 100, 1, 1, 1, 100, 1, 1, 100, 1 }) != 6) return error.TestFailed;
    std.debug.print("PASS\\n", .{}); }''',
"dart":'''int minCostClimbingStairs(List<int> cost) {
  var a = 0, b = 0;
  for (var i = 2; i <= cost.length; i++) {
    final t = (a + cost[i - 2]) < (b + cost[i - 1]) ? (a + cost[i - 2]) : (b + cost[i - 1]);
    a = b; b = t;
  }
  return b;
}
void main() { if (minCostClimbingStairs([10,15,20]) != 15) throw StateError('c1'); if (minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]) != 6) throw StateError('c2'); print('PASS'); }''',
}
T["53"] = {
"rust":'''fn max_sub_array(nums: Vec<i32>) -> i32 {
    let (mut best, mut cur) = (nums[0], nums[0]);
    for &v in nums.iter().skip(1) {
        cur = if cur > 0 { cur + v } else { v };
        best = best.max(cur);
    }
    best
}
fn main() { assert_eq!(max_sub_array(vec![-2,1,-3,4,-1,2,1,-5,4]), 6); assert_eq!(max_sub_array(vec![1]), 1); assert_eq!(max_sub_array(vec![5,4,-1,7,8]), 23); println!("PASS"); }''',
"lua":'''local function max_sub_array(nums)
    local best, cur = nums[1], nums[1]
    for i = 2, #nums do
        cur = cur > 0 and cur + nums[i] or nums[i]
        if cur > best then best = cur end
    end
    return best
end
assert(max_sub_array({-2,1,-3,4,-1,2,1,-5,4}) == 6)
assert(max_sub_array({1}) == 1)
assert(max_sub_array({5,4,-1,7,8}) == 23)
print("PASS")''',
"c":'''#include <stdio.h>
static int max_sub_array(const int *n, int len) {
    int best = n[0], cur = n[0];
    for (int i = 1; i < len; i++) {
        cur = cur > 0 ? cur + n[i] : n[i];
        if (cur > best) best = cur;
    }
    return best;
}
int main(void) {
    if (max_sub_array((int[]){-2,1,-3,4,-1,2,1,-5,4}, 9) != 6) { printf("FAIL 1\\n"); return 1; }
    if (max_sub_array((int[]){1}, 1) != 1) { printf("FAIL 2\\n"); return 1; }
    if (max_sub_array((int[]){5,4,-1,7,8}, 5) != 23) { printf("FAIL 3\\n"); return 1; }
    printf("PASS\\n"); return 0; }''',
"cpp":'''#include <algorithm>
#include <cassert>
#include <iostream>
#include <vector>
static int maxSubArray(const std::vector<int> &nums) {
    int best = nums[0], cur = nums[0];
    for (size_t i = 1; i < nums.size(); ++i) {
        cur = std::max(cur + nums[i], nums[i]);
        best = std::max(best, cur);
    }
    return best;
}
int main() { assert(maxSubArray({-2,1,-3,4,-1,2,1,-5,4}) == 6); assert(maxSubArray({1}) == 1); assert(maxSubArray({5,4,-1,7,8}) == 23); std::cout << "PASS" << std::endl; }''',
"r":'''max_sub_array <- function(nums) {
  best <- nums[1]; cur <- nums[1]
  for (v in nums[-1]) {
    cur <- max(cur + v, v)
    best <- max(best, cur)
  }
  best
}
stopifnot(max_sub_array(c(-2, 1, -3, 4, -1, 2, 1, -5, 4)) == 6)
stopifnot(max_sub_array(c(1)) == 1)
stopifnot(max_sub_array(c(5, 4, -1, 7, 8)) == 23)
cat("PASS\\n")''',
"zig":'''const std = @import("std");
fn maxSubArray(nums: []const i32) i32 {
    var best = nums[0];
    var cur = nums[0];
    for (nums[1..]) |v| {
        cur = @max(cur + v, v);
        best = @max(best, cur);
    }
    return best;
}
pub fn main() !void {
    if (maxSubArray(&[_]i32{ -2, 1, -3, 4, -1, 2, 1, -5, 4 }) != 6) return error.TestFailed;
    if (maxSubArray(&[_]i32{1}) != 1) return error.TestFailed;
    if (maxSubArray(&[_]i32{ 5, 4, -1, 7, 8 }) != 23) return error.TestFailed;
    std.debug.print("PASS\\n", .{}); }''',
"dart":'''int maxSubArray(List<int> nums) {
  var best = nums[0], cur = nums[0];
  for (var i = 1; i < nums.length; i++) {
    cur = cur > 0 ? cur + nums[i] : nums[i];
    if (cur > best) best = cur;
  }
  return best;
}
void main() { if (maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) != 6) throw StateError('c1'); if (maxSubArray([1]) != 1) throw StateError('c2'); if (maxSubArray([5,4,-1,7,8]) != 23) throw StateError('c3'); print('PASS'); }''',
}
T["198"] = {
"rust":'''fn rob(nums: Vec<i32>) -> i32 {
    let (mut a, mut b) = (0, 0);
    for v in nums { let t = (b).max(a + v); a = b; b = t; }
    b
}
fn main() { assert_eq!(rob(vec![1,2,3,1]), 4); assert_eq!(rob(vec![2,7,9,3,1]), 12); println!("PASS"); }''',
"lua":'''local function rob(nums) local a, b = 0, 0 for _, v in ipairs(nums) do a, b = b, math.max(b, a + v) end return b end
assert(rob({1,2,3,1}) == 4); assert(rob({2,7,9,3,1}) == 12); print("PASS")''',
"c":'''#include <stdio.h>
static int rob(const int *n, int len) { int a = 0, b = 0; for (int i = 0; i < len; i++) { int t = b > a + n[i] ? b : a + n[i]; a = b; b = t; } return b; }
int main(void) { if (rob((int[]){1,2,3,1}, 4) != 4) { printf("FAIL 1\\n"); return 1; } if (rob((int[]){2,7,9,3,1}, 5) != 12) { printf("FAIL 2\\n"); return 1; } printf("PASS\\n"); return 0; }''',
"cpp":'''#include <algorithm>
#include <cassert>
#include <iostream>
#include <vector>
static int rob(const std::vector<int> &nums) { int a = 0, b = 0; for (int v : nums) { int t = std::max(b, a + v); a = b; b = t; } return b; }
int main() { assert(rob({1,2,3,1}) == 4); assert(rob({2,7,9,3,1}) == 12); std::cout << "PASS" << std::endl; }''',
"r":'''rob_houses <- function(nums) { a <- 0L; b <- 0L; for (v in nums) { t <- max(b, a + v); a <- b; b <- t }; b }
stopifnot(rob_houses(c(1, 2, 3, 1)) == 4)
stopifnot(rob_houses(c(2, 7, 9, 3, 1)) == 12)
cat("PASS\\n")''',
"zig":'''const std = @import("std");
fn rob(nums: []const i32) i32 { var a: i32 = 0; var b: i32 = 0; for (nums) |v| { const t = @max(b, a + v); a = b; b = t; } return b; }
pub fn main() !void { if (rob(&[_]i32{ 1, 2, 3, 1 }) != 4) return error.TestFailed; if (rob(&[_]i32{ 2, 7, 9, 3, 1 }) != 12) return error.TestFailed; std.debug.print("PASS\\n", .{}); }''',
"dart":'''int rob(List<int> nums) { var a = 0, b = 0; for (final v in nums) { final t = b > a + v ? b : a + v; a = b; b = t; } return b; }
void main() { if (rob([1,2,3,1]) != 4) throw StateError('c1'); if (rob([2,7,9,3,1]) != 12) throw StateError('c2'); print('PASS'); }''',
}
T["213"] = {
"rust":'''fn rob_ii(nums: Vec<i32>) -> i32 {
    if nums.len() == 1 { return nums[0]; }
    let rob1 = |slice: &[i32]| -> i32 { let (mut a, mut b) = (0, 0); for &v in slice { let t = b.max(a + v); a = b; b = t; } b };
    rob_ii_helper(&nums[1..]).max(rob1(&nums[..nums.len() - 1]))
}
fn rob_ii_helper(nums: &[i32]) -> i32 { let (mut a, mut b) = (0, 0); for &v in nums { let t = b.max(a + v); a = b; b = t; } b }
fn main() { assert_eq!(rob_ii(vec![2,3,2]), 3); assert_eq!(rob_ii(vec![1,2,3,1]), 4); assert_eq!(rob_ii(vec![1]), 1); println!("PASS"); }''',
"lua":'''local function rob_line(nums) local a, b = 0, 0 for _, v in ipairs(nums) do a, b = b, math.max(b, a + v) end return b end
local function rob_ii(nums)
    if #nums == 1 then return nums[1] end
    local skip_first, skip_last = {}, {}
    for i = 2, #nums do skip_first[#skip_first + 1] = nums[i] end
    for i = 1, #nums - 1 do skip_last[#skip_last + 1] = nums[i] end
    return math.max(rob_line(skip_first), rob_line(skip_last))
end
assert(rob_ii({2,3,2}) == 3)
assert(rob_ii({1,2,3,1}) == 4)
assert(rob_ii({1}) == 1)
print("PASS")''',
"c":'''#include <stdio.h>
static int rob_line(const int *n, int len) { int a = 0, b = 0; for (int i = 0; i < len; i++) { int t = b > a + n[i] ? b : a + n[i]; a = b; b = t; } return b; }
static int rob_ii(const int *n, int len) {
    if (len == 1) return n[0];
    int r1 = rob_line(n + 1, len - 1);
    int r2 = rob_line(n, len - 1);
    return r1 > r2 ? r1 : r2;
}
int main(void) {
    if (rob_ii((int[]){2,3,2}, 3) != 3) { printf("FAIL 1\\n"); return 1; }
    if (rob_ii((int[]){1,2,3,1}, 4) != 4) { printf("FAIL 2\\n"); return 1; }
    if (rob_ii((int[]){1}, 1) != 1) { printf("FAIL 3\\n"); return 1; }
    printf("PASS\\n"); return 0; }''',
"cpp":'''#include <algorithm>
#include <cassert>
#include <iostream>
#include <vector>
static int robLine(const std::vector<int> &nums) { int a = 0, b = 0; for (int v : nums) { int t = std::max(b, a + v); a = b; b = t; } return b; }
static int robII(const std::vector<int> &nums) {
    if (nums.size() == 1) return nums[0];
    std::vector<int> skipFirst(nums.begin() + 1, nums.end());
    std::vector<int> skipLast(nums.begin(), nums.end() - 1);
    return std::max(robLine(skipFirst), robLine(skipLast));
}
int main() { assert(robII({2,3,2}) == 3); assert(robII({1,2,3,1}) == 4); assert(robII({1}) == 1); std::cout << "PASS" << std::endl; }''',
"r":'''rob_line <- function(nums) { a <- 0L; b <- 0L; for (v in nums) { t <- max(b, a + v); a <- b; b <- t }; b }
rob_ii <- function(nums) {
  if (length(nums) == 1) return(nums)
  max(rob_line(nums[-1]), rob_line(nums[-length(nums)]))
}
stopifnot(rob_ii(c(2, 3, 2)) == 3)
stopifnot(rob_ii(c(1, 2, 3, 1)) == 4)
stopifnot(rob_ii(c(1)) == 1)
cat("PASS\\n")''',
"zig":'''const std = @import("std");
fn robLine(nums: []const i32) i32 { var a: i32 = 0; var b: i32 = 0; for (nums) |v| { const t = @max(b, a + v); a = b; b = t; } return b; }
fn robII(nums: []const i32) i32 {
    if (nums.len == 1) return nums[0];
    const r1 = robLine(nums[1..]);
    const r2 = robLine(nums[0 .. nums.len - 1]);
    return @max(r1, r2);
}
pub fn main() !void { if (robII(&[_]i32{ 2, 3, 2 }) != 3) return error.TestFailed; if (robII(&[_]i32{ 1, 2, 3, 1 }) != 4) return error.TestFailed; if (robII(&[_]i32{1}) != 1) return error.TestFailed; std.debug.print("PASS\\n", .{}); }''',
"dart":'''int robLine(List<int> nums) { var a = 0, b = 0; for (final v in nums) { final t = b > a + v ? b : a + v; a = b; b = t; } return b; }
int robII(List<int> nums) {
  if (nums.length == 1) return nums[0];
  return robLine(nums.sublist(1)).compareTo(robLine(nums.sublist(0, nums.length - 1))) >= 0
      ? robLine(nums.sublist(1))
      : robLine(nums.sublist(0, nums.length - 1));
}
void main() { if (robII([2,3,2]) != 3) throw StateError('c1'); if (robII([1,2,3,1]) != 4) throw StateError('c2'); if (robII([1]) != 1) throw StateError('c3'); print('PASS'); }''',
}
T["121"] = {
"rust":'''fn max_profit(prices: Vec<i32>) -> i32 {
    let (mut min_p, mut best) = (i32::MAX, 0);
    for &p in &prices {
        if p < min_p { min_p = p; }
        if p - min_p > best { best = p - min_p; }
    }
    best
}
fn main() { assert_eq!(max_profit(vec![7,1,5,3,6,4]), 5); assert_eq!(max_profit(vec![7,6,4,3,1]), 0); println!("PASS"); }''',
"lua":'''local function max_profit(prices)
    local min_p, best = math.huge, 0
    for _, p in ipairs(prices) do
        if p < min_p then min_p = p end
        if p - min_p > best then best = p - min_p end
    end
    return best
end
assert(max_profit({7,1,5,3,6,4}) == 5)
assert(max_profit({7,6,4,3,1}) == 0)
print("PASS")''',
"c":'''#include <stdio.h>
static int max_profit(const int *p, int n) {
    int min_p = 1 << 30, best = 0;
    for (int i = 0; i < n; i++) {
        if (p[i] < min_p) min_p = p[i];
        if (p[i] - min_p > best) best = p[i] - min_p;
    }
    return best;
}
int main(void) {
    if (max_profit((int[]){7,1,5,3,6,4}, 6) != 5) { printf("FAIL 1\\n"); return 1; }
    if (max_profit((int[]){7,6,4,3,1}, 5) != 0) { printf("FAIL 2\\n"); return 1; }
    printf("PASS\\n"); return 0; }''',
"cpp":'''#include <algorithm>
#include <cassert>
#include <iostream>
#include <vector>
static int maxProfit(const std::vector<int> &prices) {
    int minP = -1, best = 0;
    for (int p : prices) {
        if (minP == -1 || p < minP) minP = p;
        if (p - minP > best) best = p - minP;
    }
    return best;
}
int main() { assert(maxProfit({7,1,5,3,6,4}) == 5); assert(maxProfit({7,6,4,3,1}) == 0); std::cout << "PASS" << std::endl; }''',
"r":'''max_profit_stock <- function(prices) {
  min_p <- .Machine$integer.max; best <- 0L
  for (p in prices) {
    if (p < min_p) min_p <- p
    if (p - min_p > best) best <- p - min_p
  }
  best
}
stopifnot(max_profit_stock(c(7, 1, 5, 3, 6, 4)) == 5)
stopifnot(max_profit_stock(c(7, 6, 4, 3, 1)) == 0)
cat("PASS\\n")''',
"zig":'''const std = @import("std");
fn maxProfit(prices: []const i32) i32 {
    var min_p: i32 = std.math.maxInt(i32);
    var best: i32 = 0;
    for (prices) |p| {
        if (p < min_p) min_p = p;
        if (p - min_p > best) best = p - min_p;
    }
    return best;
}
pub fn main() !void { if (maxProfit(&[_]i32{ 7, 1, 5, 3, 6, 4 }) != 5) return error.TestFailed; if (maxProfit(&[_]i32{ 7, 6, 4, 3, 1 }) != 0) return error.TestFailed; std.debug.print("PASS\\n", .{}); }''',
"dart":'''int maxProfit(List<int> prices) {
  var minP = -1, best = 0;
  for (final p in prices) {
    if (minP == -1 || p < minP) minP = p;
    if (p - minP > best) best = p - minP;
  }
  return best;
}
void main() { if (maxProfit([7,1,5,3,6,4]) != 5) throw StateError('c1'); if (maxProfit([7,6,4,3,1]) != 0) throw StateError('c2'); print('PASS'); }''',
}
T["322"] = {
"rust":'''fn coin_change(coins: Vec<i32>, amount: i32) -> i32 {
    let mut dp = vec![i32::MAX; amount as usize + 1];
    dp[0] = 0;
    for a in 1..=amount as usize {
        for &c in &coins {
            if c as usize <= a && dp[a - c as usize] != i32::MAX {
                dp[a] = dp[a].min(dp[a - c as usize] + 1);
            }
        }
    }
    if dp[amount as usize] == i32::MAX { -1 } else { dp[amount as usize] }
}
fn main() { assert_eq!(coin_change(vec![1,2,5], 11), 3); assert_eq!(coin_change(vec![2], 3), -1); assert_eq!(coin_change(vec![1], 0), 0); println!("PASS"); }''',
"lua":'''local function coin_change(coins, amount)
    local dp = {}
    for i = 0, amount do dp[i] = math.huge end
    dp[0] = 0
    for a = 1, amount do
        for _, c in ipairs(coins) do
            if c <= a and dp[a - c] ~= math.huge then
                if dp[a - c] + 1 < dp[a] then dp[a] = dp[a - c] + 1 end
            end
        end
    end
    if dp[amount] == math.huge then return -1 end
    return dp[amount]
end
assert(coin_change({1,2,5}, 11) == 3)
assert(coin_change({2}, 3) == -1)
assert(coin_change({1}, 0) == 0)
print("PASS")''',
"c":'''#include <stdio.h>
static int coin_change(const int *coins, int nc, int amount) {
    long dp[10001];
    dp[0] = 0;
    for (int a = 1; a <= amount; a++) dp[a] = 1L << 40;
    for (int a = 1; a <= amount; a++) {
        for (int i = 0; i < nc; i++) {
            if (coins[i] <= a && dp[a - coins[i]] < (1L << 40)) {
                if (dp[a - coins[i]] + 1 < dp[a]) dp[a] = dp[a - coins[i]] + 1;
            }
        }
    }
    return dp[amount] >= (1L << 40) ? -1 : (int)dp[amount];
}
int main(void) {
    if (coin_change((int[]){1,2,5}, 3, 11) != 3) { printf("FAIL 1\\n"); return 1; }
    if (coin_change((int[]){2}, 1, 3) != -1) { printf("FAIL 2\\n"); return 1; }
    if (coin_change((int[]){1}, 1, 0) != 0) { printf("FAIL 3\\n"); return 1; }
    printf("PASS\\n"); return 0; }''',
"cpp":'''#include <algorithm>
#include <cassert>
#include <iostream>
#include <vector>
static int coinChange(const std::vector<int> &coins, int amount) {
    std::vector<int> dp(amount + 1, -1);
    dp[0] = 0;
    for (int a = 1; a <= amount; ++a) {
        for (int c : coins) {
            if (c <= a && dp[a - c] != -1) {
                if (dp[a] == -1 || dp[a - c] + 1 < dp[a]) dp[a] = dp[a - c] + 1;
            }
        }
    }
    return dp[amount];
}
int main() { assert(coinChange({1,2,5}, 11) == 3); assert(coinChange({2}, 3) == -1); assert(coinChange({1}, 0) == 0); std::cout << "PASS" << std::endl; }''',
"r":'''coin_change <- function(coins, amount) {
  dp <- rep(Inf, amount + 1)
  dp[1] <- 0
  for (a in 1:amount) {
    for (c in coins) {
      if (c <= a && is.finite(dp[a - c + 1])) {
        dp[a + 1] <- min(dp[a + 1], dp[a - c + 1] + 1)
      }
    }
  }
  if (is.infinite(dp[amount + 1])) -1L else as.integer(dp[amount + 1])
}
stopifnot(coin_change(c(1, 2, 5), 11) == 3)
stopifnot(coin_change(c(2), 3) == -1)
stopifnot(coin_change(c(1), 0) == 0)
cat("PASS\\n")''',
"zig":'''const std = @import("std");
fn coinChange(coins: []const i32, amount: i32) i32 {
    var dp: [10001]i64 = undefined;
    dp[0] = 0;
    for (1..@intCast(amount + 1)) |a| dp[a] = 1 << 40;
    for (1..@intCast(amount + 1)) |ai| {
        for (coins) |c| {
            const ci: usize = @intCast(c);
            if (ci <= ai and dp[ai - ci] < (1 << 40)) {
                if (dp[ai - ci] + 1 < dp[ai]) dp[ai] = dp[ai - ci] + 1;
            }
        }
    }
    const r = dp[@intCast(amount)];
    return if (r >= (1 << 40)) -1 else @intCast(r);
}
pub fn main() !void {
    if (coinChange(&[_]i32{ 1, 2, 5 }, 11) != 3) return error.TestFailed;
    if (coinChange(&[_]i32{2}, 3) != -1) return error.TestFailed;
    if (coinChange(&[_]i32{1}, 0) != 0) return error.TestFailed;
    std.debug.print("PASS\\n", .{}); }''',
"dart":'''int coinChange(List<int> coins, int amount) {
  final dp = List<int>.filled(amount + 1, -1);
  dp[0] = 0;
  for (var a = 1; a <= amount; a++) {
    for (final c in coins) {
      if (c <= a && dp[a - c] != -1) {
        if (dp[a] == -1 || dp[a - c] + 1 < dp[a]) dp[a] = dp[a - c] + 1;
      }
    }
  }
  return dp[amount];
}
void main() { if (coinChange([1,2,5], 11) != 3) throw StateError('c1'); if (coinChange([2], 3) != -1) throw StateError('c2'); if (coinChange([1], 0) != 0) throw StateError('c3'); print('PASS'); }''',
}
T["518"] = {
"rust":'''fn change(amount: i32, coins: Vec<i32>) -> i32 {
    let mut dp = vec![0i64; amount as usize + 1];
    dp[0] = 1;
    for &c in &coins {
        for a in c as usize..=amount as usize {
            dp[a] += dp[a - c as usize];
        }
    }
    dp[amount as usize] as i32
}
fn main() { assert_eq!(change(5, vec![1,2,5]), 4); assert_eq!(change(3, vec![2]), 0); assert_eq!(change(10, vec![1,2,5]), 10); assert_eq!(change(0, vec![1,2]), 1); println!("PASS"); }''',
"lua":'''local function change(amount, coins)
    local dp = {}
    for i = 0, amount do dp[i] = 0 end
    dp[0] = 1
    for _, c in ipairs(coins) do
        for a = c, amount do
            dp[a] = dp[a] + dp[a - c]
        end
    end
    return dp[amount]
end
assert(change(5, {1,2,5}) == 4)
assert(change(3, {2}) == 0)
assert(change(10, {1,2,5}) == 10)
assert(change(0, {1,2}) == 1)
print("PASS")''',
"c":'''#include <stdio.h>
static long change(int amount, const int *coins, int nc) {
    long dp[10001] = {0};
    dp[0] = 1;
    for (int i = 0; i < nc; i++) {
        for (int a = coins[i]; a <= amount; a++) dp[a] += dp[a - coins[i]];
    }
    return dp[amount];
}
int main(void) {
    if (change(5, (int[]){1,2,5}, 3) != 4) { printf("FAIL 1\\n"); return 1; }
    if (change(3, (int[]){2}, 1) != 0) { printf("FAIL 2\\n"); return 1; }
    if (change(10, (int[]){1,2,5}, 3) != 10) { printf("FAIL 3\\n"); return 1; }
    if (change(0, (int[]){1,2}, 2) != 1) { printf("FAIL 4\\n"); return 1; }
    printf("PASS\\n"); return 0; }''',
"cpp":'''#include <cassert>
#include <iostream>
#include <vector>
static int change(int amount, const std::vector<int> &coins) {
    std::vector<long long> dp(amount + 1, 0);
    dp[0] = 1;
    for (int c : coins) {
        for (int a = c; a <= amount; ++a) dp[a] += dp[a - c];
    }
    return static_cast<int>(dp[amount]);
}
int main() { assert(change(5, {1,2,5}) == 4); assert(change(3, {2}) == 0); assert(change(10, {1,2,5}) == 10); assert(change(0, {1,2}) == 1); std::cout << "PASS" << std::endl; }''',
"r":'''change_ways <- function(amount, coins) {
  dp <- rep(0L, amount + 1)
  dp[1] <- 1L
  for (c in coins) {
    if (c <= amount) {
      for (a in c:amount) dp[a + 1] <- dp[a + 1] + dp[a - c + 1]
    }
  }
  dp[amount + 1]
}
stopifnot(change_ways(5, c(1, 2, 5)) == 4)
stopifnot(change_ways(3, c(2)) == 0)
stopifnot(change_ways(10, c(1, 2, 5)) == 10)
stopifnot(change_ways(0, c(1, 2)) == 1)
cat("PASS\\n")''',
"zig":'''const std = @import("std");
fn change(amount: i32, coins: []const i32) i32 {
    var dp: [10001]i64 = undefined;
    dp[0] = 1;
    for (1..@intCast(amount + 1)) |a| dp[a] = 0;
    for (coins) |c| {
        const ci: usize = @intCast(c);
        var a = ci;
        while (a <= @as(usize, @intCast(amount))) : (a += 1) dp[a] += dp[a - ci];
    }
    return @intCast(dp[@intCast(amount)]);
}
pub fn main() !void {
    if (change(5, &[_]i32{ 1, 2, 5 }) != 4) return error.TestFailed;
    if (change(3, &[_]i32{2}) != 0) return error.TestFailed;
    if (change(10, &[_]i32{ 1, 2, 5 }) != 10) return error.TestFailed;
    if (change(0, &[_]i32{ 1, 2 }) != 1) return error.TestFailed;
    std.debug.print("PASS\\n", .{}); }''',
"dart":'''int change(int amount, List<int> coins) {
  final dp = List<int>.filled(amount + 1, 0);
  dp[0] = 1;
  for (final c in coins) {
    for (var a = c; a <= amount; a++) dp[a] += dp[a - c];
  }
  return dp[amount];
}
void main() { if (change(5, [1,2,5]) != 4) throw StateError('c1'); if (change(3, [2]) != 0) throw StateError('c2'); if (change(10, [1,2,5]) != 10) throw StateError('c3'); if (change(0, [1,2]) != 1) throw StateError('c4'); print('PASS'); }''',
}
T["62"] = {
"rust":'''fn unique_paths(m: i32, n: i32) -> i32 {
    let mut dp = vec![1i32; n as usize];
    for _ in 1..m {
        for j in 1..n as usize { dp[j] += dp[j - 1]; }
    }
    dp[n as usize - 1]
}
fn main() { assert_eq!(unique_paths(3, 7), 28); assert_eq!(unique_paths(3, 2), 3); assert_eq!(unique_paths(1, 1), 1); println!("PASS"); }''',
"lua":'''local function unique_paths(m, n)
    local dp = {}
    for j = 1, n do dp[j] = 1 end
    for _ = 2, m do
        for j = 2, n do dp[j] = dp[j] + dp[j - 1] end
    end
    return dp[n]
end
assert(unique_paths(3, 7) == 28)
assert(unique_paths(3, 2) == 3)
assert(unique_paths(1, 1) == 1)
print("PASS")''',
"c":'''#include <stdio.h>
static int unique_paths(int m, int n) {
    int dp[101];
    for (int j = 0; j < n; j++) dp[j] = 1;
    for (int i = 1; i < m; i++)
        for (int j = 1; j < n; j++) dp[j] += dp[j - 1];
    return dp[n - 1];
}
int main(void) {
    if (unique_paths(3, 7) != 28) { printf("FAIL 1\\n"); return 1; }
    if (unique_paths(3, 2) != 3) { printf("FAIL 2\\n"); return 1; }
    if (unique_paths(1, 1) != 1) { printf("FAIL 3\\n"); return 1; }
    printf("PASS\\n"); return 0; }''',
"cpp":'''#include <cassert>
#include <iostream>
#include <vector>
static int uniquePaths(int m, int n) {
    std::vector<int> dp(n, 1);
    for (int i = 1; i < m; ++i)
        for (int j = 1; j < n; ++j) dp[j] += dp[j - 1];
    return dp[n - 1];
}
int main() { assert(uniquePaths(3, 7) == 28); assert(uniquePaths(3, 2) == 3); assert(uniquePaths(1, 1) == 1); std::cout << "PASS" << std::endl; }''',
"r":'''unique_paths <- function(m, n) {
  dp <- rep(1L, n)
  if (m >= 2 && n >= 2) {
    for (i in 2:m) for (j in 2:n) dp[j] <- dp[j] + dp[j - 1]
  }
  dp[n]
}
stopifnot(unique_paths(3, 7) == 28)
stopifnot(unique_paths(3, 2) == 3)
stopifnot(unique_paths(1, 1) == 1)
cat("PASS\\n")''',
"zig":'''const std = @import("std");
fn uniquePaths(m: i32, n: i32) i32 {
    var dp: [101]i32 = undefined;
    for (0..@intCast(n)) |j| dp[j] = 1;
    var i: i32 = 1;
    while (i < m) : (i += 1) {
        var j: usize = 1;
        while (j < @as(usize, @intCast(n))) : (j += 1) dp[j] += dp[j - 1];
    }
    return dp[@intCast(n - 1)];
}
pub fn main() !void {
    if (uniquePaths(3, 7) != 28) return error.TestFailed;
    if (uniquePaths(3, 2) != 3) return error.TestFailed;
    if (uniquePaths(1, 1) != 1) return error.TestFailed;
    std.debug.print("PASS\\n", .{}); }''',
"dart":'''int uniquePaths(int m, int n) {
  final dp = List<int>.filled(n, 1);
  for (var i = 1; i < m; i++) {
    for (var j = 1; j < n; j++) dp[j] += dp[j - 1];
  }
  return dp[n - 1];
}
void main() { if (uniquePaths(3, 7) != 28) throw StateError('c1'); if (uniquePaths(3, 2) != 3) throw StateError('c2'); if (uniquePaths(1, 1) != 1) throw StateError('c3'); print('PASS'); }''',
}
T["63"] = {
"rust":'''fn unique_paths_with_obstacles(grid: Vec<Vec<i32>>) -> i32 {
    let m = grid.len();
    let n = grid[0].len();
    let mut dp = vec![0i32; n];
    dp[0] = if grid[0][0] == 1 { 0 } else { 1 };
    for i in 0..m {
        for j in 0..n {
            if grid[i][j] == 1 { dp[j] = 0; }
            else if j > 0 { dp[j] += dp[j - 1]; }
        }
    }
    dp[n - 1]
}
fn main() {
    let g = vec![vec![0,0,0],vec![0,1,0],vec![0,0,0]];
    assert_eq!(unique_paths_with_obstacles(g), 2);
    let g2 = vec![vec![0,1],vec![0,0]];
    assert_eq!(unique_paths_with_obstacles(g2), 1);
    println!("PASS"); }''',
"lua":'''local function unique_paths_with_obstacles(grid)
    local m, n = #grid, #grid[1]
    local dp = {}
    for j = 1, n do dp[j] = 0 end
    dp[1] = grid[1][1] == 1 and 0 or 1
    for i = 1, m do
        for j = 1, n do
            if grid[i][j] == 1 then dp[j] = 0
            elseif j > 1 then dp[j] = dp[j] + dp[j - 1] end
        end
    end
    return dp[n]
end
assert(unique_paths_with_obstacles({{0,0,0},{0,1,0},{0,0,0}}) == 2)
assert(unique_paths_with_obstacles({{0,1},{0,0}}) == 1)
print("PASS")''',
"c":'''#include <stdio.h>
static int unique_paths_with_obstacles(int grid[][3], int m, int n) {
    int dp[3] = {0};
    dp[0] = grid[0][0] == 1 ? 0 : 1;
    for (int i = 0; i < m; i++)
        for (int j = 0; j < n; j++) {
            if (grid[i][j] == 1) dp[j] = 0;
            else if (j > 0) dp[j] += dp[j - 1];
        }
    return dp[n - 1];
}
int main(void) {
    int g1[3][3] = {{0,0,0},{0,1,0},{0,0,0}};
    if (unique_paths_with_obstacles(g1, 3, 3) != 2) { printf("FAIL 1\\n"); return 1; }
    int g2[2][3] = {{0,1,0},{0,0,0}};
    if (unique_paths_with_obstacles(g2, 2, 3) != 1) { printf("FAIL 2\\n"); return 1; }
    printf("PASS\\n"); return 0; }''',
"cpp":'''#include <cassert>
#include <iostream>
#include <vector>
static int uniquePathsWithObstacles(const std::vector<std::vector<int>> &grid) {
    size_t m = grid.size(), n = grid[0].size();
    std::vector<int> dp(n, 0);
    dp[0] = grid[0][0] == 1 ? 0 : 1;
    for (size_t i = 0; i < m; ++i)
        for (size_t j = 0; j < n; ++j) {
            if (grid[i][j] == 1) dp[j] = 0;
            else if (j > 0) dp[j] += dp[j - 1];
        }
    return dp[n - 1];
}
int main() {
    assert(uniquePathsWithObstacles({{0,0,0},{0,1,0},{0,0,0}}) == 2);
    assert(uniquePathsWithObstacles({{0,1},{0,0}}) == 1);
    std::cout << "PASS" << std::endl; }''',
"r":'''unique_paths_with_obstacles <- function(grid) {
  m <- nrow(grid); n <- ncol(grid)
  dp <- rep(0L, n)
  dp[1] <- if (grid[1, 1] == 1) 0L else 1L
  for (i in 1:m) for (j in 1:n) {
    if (grid[i, j] == 1) dp[j] <- 0L
    else if (j > 1) dp[j] <- dp[j] + dp[j - 1]
  }
  dp[n]
}
g1 <- matrix(c(0,0,0,0,1,0,0,0,0), nrow = 3, byrow = TRUE)
stopifnot(unique_paths_with_obstacles(g1) == 2)
g2 <- matrix(c(0,1,0,0), nrow = 2, byrow = TRUE)
stopifnot(unique_paths_with_obstacles(g2) == 1)
cat("PASS\\n")''',
"zig":'''const std = @import("std");
fn uniquePathsWithObstacles(grid: []const []const i32) i32 {
    const m = grid.len;
    const n = grid[0].len;
    var dp: [101]i32 = undefined;
    for (0..101) |k| dp[k] = 0;
    dp[0] = if (grid[0][0] == 1) 0 else 1;
    for (0..m) |i| {
        for (0..n) |j| {
            if (grid[i][j] == 1) {
                dp[j] = 0;
            } else if (j > 0) {
                dp[j] += dp[j - 1];
            }
        }
    }
    return dp[n - 1];
}
pub fn main() !void {
    const r1 = [_]i32{ 0, 0, 0 };
    const r2 = [_]i32{ 0, 1, 0 };
    const r3 = [_]i32{ 0, 0, 0 };
    const g1 = [_][]const i32{ &r1, &r2, &r3 };
    if (uniquePathsWithObstacles(&g1) != 2) return error.TestFailed;
    const s1 = [_]i32{ 0, 1 };
    const s2 = [_]i32{ 0, 0 };
    const g2 = [_][]const i32{ &s1, &s2 };
    if (uniquePathsWithObstacles(&g2) != 1) return error.TestFailed;
    std.debug.print("PASS\\n", .{}); }''',
"dart":'''int uniquePathsWithObstacles(List<List<int>> grid) {
  final m = grid.length, n = grid[0].length;
  final dp = List<int>.filled(n, 0);
  dp[0] = grid[0][0] == 1 ? 0 : 1;
  for (var i = 0; i < m; i++) {
    for (var j = 0; j < n; j++) {
      if (grid[i][j] == 1) { dp[j] = 0; }
      else if (j > 0) { dp[j] += dp[j - 1]; }
    }
  }
  return dp[n - 1];
}
void main() {
  if (uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]) != 2) throw StateError('c1');
  if (uniquePathsWithObstacles([[0,1],[0,0]]) != 1) throw StateError('c2');
  print('PASS'); }''',
}
T["300"] = {
"rust":'''fn length_of_lis(nums: Vec<i32>) -> i32 {
    let mut dp = vec![1i32; nums.len()];
    let mut best = 0;
    for i in 0..nums.len() {
        for j in 0..i {
            if nums[j] < nums[i] { dp[i] = dp[i].max(dp[j] + 1); }
        }
        best = best.max(dp[i]);
    }
    best
}
fn main() { assert_eq!(length_of_lis(vec![10,9,2,5,3,7,101,18]), 4); assert_eq!(length_of_lis(vec![0,1,0,3,2,3]), 4); assert_eq!(length_of_lis(vec![7,7,7,7]), 1); println!("PASS"); }''',
"lua":'''local function length_of_lis(nums)
    local n = #nums
    local dp = {}
    for i = 1, n do dp[i] = 1 end
    local best = 0
    for i = 1, n do
        for j = 1, i - 1 do
            if nums[j] < nums[i] and dp[j] + 1 > dp[i] then dp[i] = dp[j] + 1 end
        end
        if dp[i] > best then best = dp[i] end
    end
    return best
end
assert(length_of_lis({10,9,2,5,3,7,101,18}) == 4)
assert(length_of_lis({0,1,0,3,2,3}) == 4)
assert(length_of_lis({7,7,7,7}) == 1)
print("PASS")''',
"c":'''#include <stdio.h>
static int length_of_lis(const int *n, int len) {
    int dp[4096], best = 0;
    for (int i = 0; i < len; i++) {
        dp[i] = 1;
        for (int j = 0; j < i; j++)
            if (n[j] < n[i] && dp[j] + 1 > dp[i]) dp[i] = dp[j] + 1;
        if (dp[i] > best) best = dp[i];
    }
    return best;
}
int main(void) {
    if (length_of_lis((int[]){10,9,2,5,3,7,101,18}, 8) != 4) { printf("FAIL 1\\n"); return 1; }
    if (length_of_lis((int[]){0,1,0,3,2,3}, 6) != 4) { printf("FAIL 2\\n"); return 1; }
    if (length_of_lis((int[]){7,7,7,7}, 4) != 1) { printf("FAIL 3\\n"); return 1; }
    printf("PASS\\n"); return 0; }''',
"cpp":'''#include <algorithm>
#include <cassert>
#include <iostream>
#include <vector>
static int lengthOfLIS(const std::vector<int> &nums) {
    std::vector<int> dp(nums.size(), 1);
    int best = 0;
    for (size_t i = 0; i < nums.size(); ++i) {
        for (size_t j = 0; j < i; ++j)
            if (nums[j] < nums[i]) dp[i] = std::max(dp[i], dp[j] + 1);
        best = std::max(best, dp[i]);
    }
    return best;
}
int main() { assert(lengthOfLIS({10,9,2,5,3,7,101,18}) == 4); assert(lengthOfLIS({0,1,0,3,2,3}) == 4); assert(lengthOfLIS({7,7,7,7}) == 1); std::cout << "PASS" << std::endl; }''',
"r":'''length_of_lis <- function(nums) {
  n <- length(nums)
  dp <- rep(1L, n)
  best <- 0L
  for (i in seq_len(n)) {
    for (j in seq_len(i - 1)) {
      if (nums[j] < nums[i] && dp[j] + 1L > dp[i]) dp[i] <- dp[j] + 1L
    }
    if (dp[i] > best) best <- dp[i]
  }
  best
}
stopifnot(length_of_lis(c(10, 9, 2, 5, 3, 7, 101, 18)) == 4)
stopifnot(length_of_lis(c(0, 1, 0, 3, 2, 3)) == 4)
stopifnot(length_of_lis(c(7, 7, 7, 7)) == 1)
cat("PASS\\n")''',
"zig":'''const std = @import("std");
fn lengthOfLIS(nums: []const i32) i32 {
    var dp: [4096]i32 = undefined;
    var best: i32 = 0;
    for (0..nums.len) |i| {
        dp[i] = 1;
        for (0..i) |j| {
            if (nums[j] < nums[i] and dp[j] + 1 > dp[i]) dp[i] = dp[j] + 1;
        }
        if (dp[i] > best) best = dp[i];
    }
    return best;
}
pub fn main() !void {
    if (lengthOfLIS(&[_]i32{ 10, 9, 2, 5, 3, 7, 101, 18 }) != 4) return error.TestFailed;
    if (lengthOfLIS(&[_]i32{ 0, 1, 0, 3, 2, 3 }) != 4) return error.TestFailed;
    if (lengthOfLIS(&[_]i32{ 7, 7, 7, 7 }) != 1) return error.TestFailed;
    std.debug.print("PASS\\n", .{}); }''',
"dart":'''int lengthOfLIS(List<int> nums) {
  final n = nums.length;
  final dp = List<int>.filled(n, 1);
  var best = 0;
  for (var i = 0; i < n; i++) {
    for (var j = 0; j < i; j++) {
      if (nums[j] < nums[i] && dp[j] + 1 > dp[i]) dp[i] = dp[j] + 1;
    }
    if (dp[i] > best) best = dp[i];
  }
  return best;
}
void main() { if (lengthOfLIS([10,9,2,5,3,7,101,18]) != 4) throw StateError('c1'); if (lengthOfLIS([0,1,0,3,2,3]) != 4) throw StateError('c2'); if (lengthOfLIS([7,7,7,7]) != 1) throw StateError('c3'); print('PASS'); }''',
}
T["674"] = {
"rust":'''fn find_length_of_lcis(nums: Vec<i32>) -> i32 {
    let (mut best, mut cur) = (1, 1);
    for i in 1..nums.len() {
        if nums[i] > nums[i - 1] { cur += 1; if cur > best { best = cur; } } else { cur = 1; }
    }
    if nums.is_empty() { 0 } else { best }
}
fn main() { assert_eq!(find_length_of_lcis(vec![1,3,5,4,7]), 3); assert_eq!(find_length_of_lcis(vec![2,2,2,2,2]), 1); println!("PASS"); }''',
"lua":'''local function find_length_of_lcis(nums)
    if #nums == 0 then return 0 end
    local best, cur = 1, 1
    for i = 2, #nums do
        if nums[i] > nums[i - 1] then
            cur = cur + 1
            if cur > best then best = cur end
        else
            cur = 1
        end
    end
    return best
end
assert(find_length_of_lcis({1,3,5,4,7}) == 3)
assert(find_length_of_lcis({2,2,2,2,2}) == 1)
print("PASS")''',
"c":'''#include <stdio.h>
static int find_length_of_lcis(const int *n, int len) {
    if (len == 0) return 0;
    int best = 1, cur = 1;
    for (int i = 1; i < len; i++) {
        if (n[i] > n[i - 1]) { cur++; if (cur > best) best = cur; }
        else cur = 1;
    }
    return best;
}
int main(void) {
    if (find_length_of_lcis((int[]){1,3,5,4,7}, 5) != 3) { printf("FAIL 1\\n"); return 1; }
    if (find_length_of_lcis((int[]){2,2,2,2,2}, 5) != 1) { printf("FAIL 2\\n"); return 1; }
    printf("PASS\\n"); return 0; }''',
"cpp":'''#include <algorithm>
#include <cassert>
#include <iostream>
#include <vector>
static int findLengthOfLCIS(const std::vector<int> &nums) {
    if (nums.empty()) return 0;
    int best = 1, cur = 1;
    for (size_t i = 1; i < nums.size(); ++i) {
        if (nums[i] > nums[i - 1]) { ++cur; best = std::max(best, cur); }
        else cur = 1;
    }
    return best;
}
int main() { assert(findLengthOfLCIS({1,3,5,4,7}) == 3); assert(findLengthOfLCIS({2,2,2,2,2}) == 1); std::cout << "PASS" << std::endl; }''',
"r":'''find_length_of_lcis <- function(nums) {
  if (length(nums) == 0) return(0L)
  best <- 1L; cur <- 1L
  for (i in 2:length(nums)) {
    if (nums[i] > nums[i - 1]) { cur <- cur + 1L; if (cur > best) best <- cur } else cur <- 1L
  }
  best
}
stopifnot(find_length_of_lcis(c(1, 3, 5, 4, 7)) == 3)
stopifnot(find_length_of_lcis(c(2, 2, 2, 2, 2)) == 1)
cat("PASS\\n")''',
"zig":'''const std = @import("std");
fn findLengthOfLCIS(nums: []const i32) i32 {
    if (nums.len == 0) return 0;
    var best: i32 = 1;
    var cur: i32 = 1;
    for (1..nums.len) |i| {
        if (nums[i] > nums[i - 1]) {
            cur += 1;
            if (cur > best) best = cur;
        } else cur = 1;
    }
    return best;
}
pub fn main() !void {
    if (findLengthOfLCIS(&[_]i32{ 1, 3, 5, 4, 7 }) != 3) return error.TestFailed;
    if (findLengthOfLCIS(&[_]i32{ 2, 2, 2, 2, 2 }) != 1) return error.TestFailed;
    std.debug.print("PASS\\n", .{}); }''',
"dart":'''int findLengthOfLCIS(List<int> nums) {
  if (nums.isEmpty) return 0;
  var best = 1, cur = 1;
  for (var i = 1; i < nums.length; i++) {
    if (nums[i] > nums[i - 1]) { cur++; if (cur > best) best = cur; } else { cur = 1; }
  }
  return best;
}
void main() { if (findLengthOfLCIS([1,3,5,4,7]) != 3) throw StateError('c1'); if (findLengthOfLCIS([2,2,2,2,2]) != 1) throw StateError('c2'); print('PASS'); }''',
}
T["1143"] = {
"rust":'''fn longest_common_subsequence(t1: String, t2: String) -> i32 {
    let a: Vec<char> = t1.chars().collect();
    let b: Vec<char> = t2.chars().collect();
    let (m, n) = (a.len(), b.len());
    let mut dp = vec![0i32; n + 1];
    for i in 1..=m {
        let mut prev_diag = 0;
        for j in 1..=n {
            let tmp = dp[j];
            dp[j] = if a[i - 1] == b[j - 1] { prev_diag + 1 } else { dp[j].max(dp[j - 1]) };
            prev_diag = tmp;
        }
    }
    dp[n]
}
fn main() { assert_eq!(longest_common_subsequence("abcde".into(), "ace".into()), 3); assert_eq!(longest_common_subsequence("abc".into(), "abc".into()), 3); assert_eq!(longest_common_subsequence("abc".into(), "def".into()), 0); println!("PASS"); }''',
"lua":'''local function longest_common_subsequence(t1, t2)
    local m, n = #t1, #t2
    local dp = {}
    for j = 0, n do dp[j] = 0 end
    for i = 1, m do
        local prev_diag = 0
        for j = 1, n do
            local tmp = dp[j]
            if t1:sub(i, i) == t2:sub(j, j) then dp[j] = prev_diag + 1
            else dp[j] = math.max(dp[j], dp[j - 1]) end
            prev_diag = tmp
        end
    end
    return dp[n]
end
assert(longest_common_subsequence("abcde", "ace") == 3)
assert(longest_common_subsequence("abc", "abc") == 3)
assert(longest_common_subsequence("abc", "def") == 0)
print("PASS")''',
"c":'''#include <stdio.h>
#include <string.h>
static int longest_common_subsequence(const char *t1, const char *t2) {
    int m = (int)strlen(t1), n = (int)strlen(t2);
    int dp[1001] = {0};
    for (int i = 1; i <= m; i++) {
        int prev_diag = 0;
        for (int j = 1; j <= n; j++) {
            int tmp = dp[j];
            dp[j] = t1[i - 1] == t2[j - 1] ? prev_diag + 1 : (dp[j] > dp[j - 1] ? dp[j] : dp[j - 1]);
            prev_diag = tmp;
        }
    }
    return dp[n];
}
int main(void) {
    if (longest_common_subsequence("abcde", "ace") != 3) { printf("FAIL 1\\n"); return 1; }
    if (longest_common_subsequence("abc", "abc") != 3) { printf("FAIL 2\\n"); return 1; }
    if (longest_common_subsequence("abc", "def") != 0) { printf("FAIL 3\\n"); return 1; }
    printf("PASS\\n"); return 0; }''',
"cpp":'''#include <algorithm>
#include <cassert>
#include <iostream>
#include <string>
#include <vector>
static int longestCommonSubsequence(const std::string &t1, const std::string &t2) {
    int m = static_cast<int>(t1.size()), n = static_cast<int>(t2.size());
    std::vector<int> dp(n + 1, 0);
    for (int i = 1; i <= m; ++i) {
        int prevDiag = 0;
        for (int j = 1; j <= n; ++j) {
            int tmp = dp[j];
            dp[j] = (t1[i - 1] == t2[j - 1]) ? prevDiag + 1 : std::max(dp[j], dp[j - 1]);
            prevDiag = tmp;
        }
    }
    return dp[n];
}
int main() { assert(longestCommonSubsequence("abcde", "ace") == 3); assert(longestCommonSubsequence("abc", "abc") == 3); assert(longestCommonSubsequence("abc", "def") == 0); std::cout << "PASS" << std::endl; }''',
"r":'''lcs_len <- function(t1, t2) {
  chars1 <- strsplit(t1, "")[[1]]
  chars2 <- strsplit(t2, "")[[1]]
  m <- length(chars1); n <- length(chars2)
  dp <- rep(0L, n + 1)
  for (i in 1:m) {
    prev_diag <- 0L
    for (j in 1:n) {
      tmp <- dp[j + 1]
      dp[j + 1] <- if (chars1[i] == chars2[j]) prev_diag + 1L else max(dp[j + 1], dp[j])
      prev_diag <- tmp
    }
  }
  dp[n + 1]
}
stopifnot(lcs_len("abcde", "ace") == 3)
stopifnot(lcs_len("abc", "abc") == 3)
stopifnot(lcs_len("abc", "def") == 0)
cat("PASS\\n")''',
"zig":'''const std = @import("std");
fn longestCommonSubsequence(t1: []const u8, t2: []const u8) i32 {
    const m = t1.len;
    const n = t2.len;
    var dp: [1001]i32 = undefined;
    dp[0] = 0;
    for (1..n + 1) |j| dp[j] = 0;
    for (1..m + 1) |i| {
        var prev_diag: i32 = 0;
        for (1..n + 1) |j| {
            const tmp = dp[j];
            dp[j] = if (t1[i - 1] == t2[j - 1]) prev_diag + 1 else @max(dp[j], dp[j - 1]);
            prev_diag = tmp;
        }
    }
    return dp[n];
}
pub fn main() !void {
    if (longestCommonSubsequence("abcde", "ace") != 3) return error.TestFailed;
    if (longestCommonSubsequence("abc", "abc") != 3) return error.TestFailed;
    if (longestCommonSubsequence("abc", "def") != 0) return error.TestFailed;
    std.debug.print("PASS\\n", .{}); }''',
"dart":'''int longestCommonSubsequence(String t1, String t2) {
  final m = t1.length, n = t2.length;
  final dp = List<int>.filled(n + 1, 0);
  for (var i = 1; i <= m; i++) {
    var prevDiag = 0;
    for (var j = 1; j <= n; j++) {
      final tmp = dp[j];
      dp[j] = t1[i - 1] == t2[j - 1] ? prevDiag + 1 : (dp[j] > dp[j - 1] ? dp[j] : dp[j - 1]);
      prevDiag = tmp;
    }
  }
  return dp[n];
}
void main() { if (longestCommonSubsequence('abcde', 'ace') != 3) throw StateError('c1'); if (longestCommonSubsequence('abc', 'abc') != 3) throw StateError('c2'); if (longestCommonSubsequence('abc', 'def') != 0) throw StateError('c3'); print('PASS'); }''',
}
T["392"] = {
"rust":'''fn is_subsequence(s: String, t: String) -> bool {
    let (sb, tb) = (s.as_bytes(), t.as_bytes());
    let mut i = 0usize;
    for &c in tb {
        if i < sb.len() && sb[i] == c { i += 1; }
    }
    i == sb.len()
}
fn main() { assert!(is_subsequence("abc".into(), "ahbgdc".into())); assert!(!is_subsequence("axc".into(), "ahbgdc".into())); println!("PASS"); }''',
"lua":'''local function is_subsequence(s, t)
    local i = 1
    for j = 1, #t do
        if i <= #s and s:sub(i, i) == t:sub(j, j) then i = i + 1 end
    end
    return i > #s
end
assert(is_subsequence("abc", "ahbgdc") == true)
assert(is_subsequence("axc", "ahbgdc") == false)
print("PASS")''',
"c":'''#include <stdio.h>
#include <string.h>
static int is_subsequence(const char *s, const char *t) {
    int i = 0;
    for (const char *p = t; *p; p++) {
        if (s[i] && s[i] == *p) i++;
    }
    return s[i] == '\\0';
}
int main(void) {
    if (!is_subsequence("abc", "ahbgdc")) { printf("FAIL 1\\n"); return 1; }
    if (is_subsequence("axc", "ahbgdc")) { printf("FAIL 2\\n"); return 1; }
    printf("PASS\\n"); return 0; }''',
"cpp":'''#include <cassert>
#include <iostream>
#include <string>
static bool isSubsequence(const std::string &s, const std::string &t) {
    size_t i = 0;
    for (char c : t) {
        if (i < s.size() && s[i] == c) ++i;
    }
    return i == s.size();
}
int main() { assert(isSubsequence("abc", "ahbgdc")); assert(!isSubsequence("axc", "ahbgdc")); std::cout << "PASS" << std::endl; }''',
"r":'''is_subsequence <- function(s, t) {
  si <- 1L
  chars_t <- strsplit(t, "")[[1]]
  chars_s <- strsplit(s, "")[[1]]
  for (ch in chars_t) {
    if (si <= length(chars_s) && chars_s[si] == ch) si <- si + 1L
  }
  si > length(chars_s)
}
stopifnot(is_subsequence("abc", "ahbgdc"))
stopifnot(!is_subsequence("axc", "ahbgdc"))
cat("PASS\\n")''',
"zig":'''const std = @import("std");
fn isSubsequence(s: []const u8, t: []const u8) bool {
    var i: usize = 0;
    for (t) |c| {
        if (i < s.len and s[i] == c) i += 1;
    }
    return i == s.len;
}
pub fn main() !void {
    if (!isSubsequence("abc", "ahbgdc")) return error.TestFailed;
    if (isSubsequence("axc", "ahbgdc")) return error.TestFailed;
    std.debug.print("PASS\\n", .{}); }''',
"dart":'''bool isSubsequence(String s, String t) {
  var i = 0;
  for (final c in t.split('')) {
    if (i < s.length && s[i] == c) i++;
  }
  return i == s.length;
}
void main() { if (!isSubsequence('abc', 'ahbgdc')) throw StateError('c1'); if (isSubsequence('axc', 'ahbgdc')) throw StateError('c2'); print('PASS'); }''',
}

PROBS = [
    ("509", "lc_509_斐波那契数", "LeetCode 509. 斐波那契数"),
    ("70", "lc_70_爬楼梯", "LeetCode 70. 爬楼梯"),
    ("746", "lc_746_使用最小花费爬楼梯", "LeetCode 746. 使用最小花费爬楼梯"),
    ("53", "lc_53_最大子数组和", "LeetCode 53. 最大子数组和"),
    ("198", "lc_198_打家劫舍", "LeetCode 198. 打家劫舍"),
    ("213", "lc_213_打家劫舍_ii", "LeetCode 213. 打家劫舍II"),
    ("121", "lc_121_买卖股票的最佳时机", "LeetCode 121. 买卖股票的最佳时机"),
    ("322", "lc_322_零钱兑换", "LeetCode 322. 零钱兑换"),
    ("518", "lc_518_零钱兑换_ii", "LeetCode 518. 零钱兑换II"),
    ("62", "lc_62_不同路径", "LeetCode 62. 不同路径"),
    ("63", "lc_63_不同路径_ii", "LeetCode 63. 不同路径II"),
    ("300", "lc_300_最长递增子序列", "LeetCode 300. 最长递增子序列"),
    ("674", "lc_674_最长连续递增序列", "LeetCode 674. 最长连续递增序列"),
    ("1143", "lc_1143_最长公共子序列", "LeetCode 1143. 最长公共子序列"),
    ("392", "lc_392_判断子序列", "LeetCode 392. 判断子序列"),
]
count = 0
for pid, pdir, title in PROBS:
    bid = B[pid]
    ts_dir = f"/Users/Wang/Code/github/web-x-blog/work/blog/courses/20.dsa/ts/dp/{pdir}"
    sols = sorted(f[:-3] for f in os.listdir(ts_dir) if f.startswith("solution_") and f.endswith(".ts"))
    for lang in LANGNAME:
        ext = EXT[lang]
        for sol in sols:
            n = sol.replace("solution_", "").split("_")[0]
            head = head_comment(lang, bid, f"{title} — {LANGNAME[lang]} 版（方案{n}）")
            emit(lang, f"dp/{pdir}/{sol}.{ext}", head + "\n" + T[pid][lang])
            count += 1
print(f"emitted {count} files")
