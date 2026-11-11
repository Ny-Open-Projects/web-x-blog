#!/usr/bin/env python3
# gen_sort1.py — sort 第一批：lc_15/lc_18/lc_179/lc_1356/lc_937/lc_922 × 7语言
import sys, os; sys.path.insert(0, "/Users/Wang/Code/webfault-ai/dsa/_tools")
from langlib import emit, head_comment, EXT

B = {"15": "133845474", "18": "133894317", "179": "134577890", "1356": "138671078", "937": "139965098", "922": "145565975"}
LANGNAME = {"rust": "Rust", "lua": "Lua", "c": "C", "cpp": "C++", "r": "R", "zig": "Zig", "dart": "Dart"}

A15 = {
"rust": '''fn three_sum(nums: Vec<i32>) -> Vec<Vec<i32>> {
    let mut arr = nums;
    arr.sort();
    let mut ans: Vec<Vec<i32>> = Vec::new();
    let n = arr.len();
    for first in 0..n {
        if first > 0 && arr[first] == arr[first - 1] { continue; }
        let mut third = n - 1;
        let target = -arr[first];
        for second in first + 1..n {
            if second > first + 1 && arr[second] == arr[second - 1] { continue; }
            while second < third && arr[second] + arr[third] > target { third -= 1; }
            if second == third { break; }
            if arr[second] + arr[third] == target {
                ans.push(vec![arr[first], arr[second], arr[third]]);
            }
        }
    }
    ans
}
fn main() {
    let mut got = three_sum(vec![-1, 0, 1, 2, -1, -4]);
    got.sort();
    assert_eq!(got, vec![vec![-1, -1, 2], vec![-1, 0, 1]]);
    assert!(three_sum(vec![0, 0, 0]).iter().all(|t| t == &vec![0, 0, 0]) && three_sum(vec![0, 0, 0]).len() == 1);
    println!("PASS");
}
''',
"lua": '''local function three_sum(nums)
    local arr = {table.unpack(nums)}
    table.sort(arr)
    local ans = {}
    local n = #arr
    for first = 1, n do
        if first == 1 or arr[first] ~= arr[first - 1] then
            local third = n
            local target = -arr[first]
            for second = first + 1, n do
                if second == first + 1 or arr[second] ~= arr[second - 1] then
                    while second < third and arr[second] + arr[third] > target do third = third - 1 end
                    if second == third then break end
                    if arr[second] + arr[third] == target then
                        ans[#ans + 1] = {arr[first], arr[second], arr[third]}
                    end
                end
            end
        end
    end
    return ans
end
local got = three_sum({-1, 0, 1, 2, -1, -4})
table.sort(got, function(a, b) return a[1] < b[1] or (a[1] == b[1] and a[2] < b[2]) end)
assert(#got == 2)
assert(got[1][1] == -1 and got[1][2] == -1 and got[1][3] == 2)
assert(got[2][1] == -1 and got[2][2] == 0 and got[2][3] == 1)
local g2 = three_sum({0, 0, 0})
assert(#g2 == 1 and g2[1][1] == 0)
print("PASS")
''',
"c": '''#include <stdio.h>
#include <stdlib.h>
static int cmp_int(const void *a, const void *b) { return *(const int *)a - *(const int *)b; }
static int three_sum(const int *nums, int n, int out[][3]) {
    int arr[4096];
    for (int i = 0; i < n; i++) arr[i] = nums[i];
    qsort(arr, n, sizeof(int), cmp_int);
    int cnt = 0;
    for (int first = 0; first < n; first++) {
        if (first > 0 && arr[first] == arr[first - 1]) continue;
        int third = n - 1;
        int target = -arr[first];
        for (int second = first + 1; second < n; second++) {
            if (second > first + 1 && arr[second] == arr[second - 1]) continue;
            while (second < third && arr[second] + arr[third] > target) third--;
            if (second == third) break;
            if (arr[second] + arr[third] == target) {
                out[cnt][0] = arr[first]; out[cnt][1] = arr[second]; out[cnt][2] = arr[third];
                cnt++;
            }
        }
    }
    return cnt;
}
int main(void) {
    int out[64][3];
    int n = three_sum((int[]){-1,0,1,2,-1,-4}, 6, out);
    /* 期望两组：[-1,-1,2] 与 [-1,0,1]（已按序生成） */
    if (n != 2) { printf("FAIL cnt=%d\\n", n); return 1; }
    if (out[0][0] != -1 || out[0][1] != -1 || out[0][2] != 2) { printf("FAIL t1\\n"); return 1; }
    if (out[1][0] != -1 || out[1][1] != 0 || out[1][2] != 1) { printf("FAIL t2\\n"); return 1; }
    n = three_sum((int[]){0,0,0}, 3, out);
    if (n != 1 || out[0][0] != 0) { printf("FAIL z\\n"); return 1; }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''#include <algorithm>
#include <cassert>
#include <iostream>
#include <vector>
static std::vector<std::vector<int>> threeSum(std::vector<int> nums) {
    std::sort(nums.begin(), nums.end());
    std::vector<std::vector<int>> ans;
    int n = static_cast<int>(nums.size());
    for (int first = 0; first < n; ++first) {
        if (first > 0 && nums[first] == nums[first - 1]) continue;
        int third = n - 1;
        int target = -nums[first];
        for (int second = first + 1; second < n; ++second) {
            if (second > first + 1 && nums[second] == nums[second - 1]) continue;
            while (second < third && nums[second] + nums[third] > target) --third;
            if (second == third) break;
            if (nums[second] + nums[third] == target) {
                ans.push_back({nums[first], nums[second], nums[third]});
            }
        }
    }
    return ans;
}
int main() {
    auto got = threeSum({-1, 0, 1, 2, -1, -4});
    std::sort(got.begin(), got.end());
    assert((got == std::vector<std::vector<int>>{{{-1, -1, 2}, {-1, 0, 1}}}));
    auto g2 = threeSum({0, 0, 0});
    assert(g2.size() == 1 && g2[0] == std::vector<int>({0, 0, 0}));
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''three_sum <- function(nums) {
  arr <- sort(nums)
  ans <- list()
  n <- length(arr)
  for (first in seq_len(n)) {
    if (first > 1 && arr[first] == arr[first - 1]) next
    third <- n
    target <- -arr[first]
    for (second in (first + 1):n) {
      if (second > n) break
      if (second > first + 1 && arr[second] == arr[second - 1]) next
      while (second < third && arr[second] + arr[third] > target) third <- third - 1L
      if (second == third) break
      if (arr[second] + arr[third] == target) {
        ans[[length(ans) + 1L]] <- c(arr[first], arr[second], arr[third])
      }
    }
  }
  ans
}
got <- three_sum(c(-1, 0, 1, 2, -1, -4))
stopifnot(length(got) == 2)
got <- got[order(vapply(got, function(x) paste(x, collapse = ","), ""))]
stopifnot(identical(got[[1]], c(-1, -1, 2)))
stopifnot(identical(got[[2]], c(-1, 0, 1)))
g2 <- three_sum(c(0, 0, 0))
stopifnot(length(g2) == 1, identical(g2[[1]], c(0, 0, 0)))
cat("PASS\\n")
''',
"zig": '''const std = @import("std");
fn threeSum(nums: []const i32, alloc: std.mem.Allocator, out: *std.ArrayList([3]i32)) void {
    const arr = alloc.dupe(i32, nums) catch unreachable;
    std.sort.pdq(i32, arr, {}, std.sort.asc(i32));
    const n = arr.len;
    for (0..n) |first| {
        if (first > 0 and arr[first] == arr[first - 1]) continue;
        var third = n - 1;
        const target = -arr[first];
        var second = first + 1;
        while (second < n) : (second += 1) {
            if (second > first + 1 and arr[second] == arr[second - 1]) continue;
            while (second < third and arr[second] + arr[third] > target) third -= 1;
            if (second == third) break;
            if (arr[second] + arr[third] == target) {
                out.append(.{ arr[first], arr[second], arr[third] }) catch unreachable;
            }
        }
    }
}
pub fn main() !void {
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();
    const alloc = arena.allocator();
    var out = std.ArrayList([3]i32).init(std.heap.page_allocator);
    defer out.deinit();
    threeSum(&[_]i32{ -1, 0, 1, 2, -1, -4 }, alloc, &out);
    if (out.items.len != 2) return error.TestFailed;
    if (out.items[0][0] != -1 or out.items[0][1] != -1 or out.items[0][2] != 2) return error.TestFailed;
    if (out.items[1][0] != -1 or out.items[1][1] != 0 or out.items[1][2] != 1) return error.TestFailed;
    out.clearRetainingCapacity();
    threeSum(&[_]i32{ 0, 0, 0 }, alloc, &out);
    if (out.items.len != 1 or out.items[0][0] != 0) return error.TestFailed;
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''List<List<int>> threeSum(List<int> nums) {
  final arr = List<int>.from(nums)..sort();
  final ans = <List<int>>[];
  final n = arr.length;
  for (var first = 0; first < n; first++) {
    if (first > 0 && arr[first] == arr[first - 1]) continue;
    var third = n - 1;
    final target = -arr[first];
    for (var second = first + 1; second < n; second++) {
      if (second > first + 1 && arr[second] == arr[second - 1]) continue;
      while (second < third && arr[second] + arr[third] > target) third--;
      if (second == third) break;
      if (arr[second] + arr[third] == target) {
        ans.add([arr[first], arr[second], arr[third]]);
      }
    }
  }
  return ans;
}
void main() {
  final got = threeSum([-1, 0, 1, 2, -1, -4]);
  if (got.length != 2) throw StateError('cnt');
  if (got[0].toString() != '[-1, -1, 2]' || got[1].toString() != '[-1, 0, 1]') throw StateError('t');
  final g2 = threeSum([0, 0, 0]);
  if (g2.length != 1 || g2[0].toString() != '[0, 0, 0]') throw StateError('z');
  print('PASS');
}
''',
}

A18 = {
"rust": '''fn four_sum(nums: Vec<i32>, target: i32) -> Vec<Vec<i32>> {
    let mut arr = nums;
    arr.sort();
    let mut res: Vec<Vec<i32>> = Vec::new();
    let n = arr.len() as i64;
    let t = target as i64;
    for i in 0..n {
        if i > 0 && arr[i as usize] == arr[(i - 1) as usize] { continue; }
        for j in i + 1..n {
            if j > i + 1 && arr[j as usize] == arr[(j - 1) as usize] { continue; }
            let (mut left, mut right) = (j + 1, n - 1);
            while left < right {
                let s = arr[i as usize] as i64 + arr[j as usize] as i64 + arr[left as usize] as i64 + arr[right as usize] as i64;
                if s == t {
                    res.push(vec![arr[i as usize], arr[j as usize], arr[left as usize], arr[right as usize]]);
                    left += 1;
                    right -= 1;
                    while left < right && arr[left as usize] == arr[(left - 1) as usize] { left += 1; }
                    while left < right && arr[right as usize] == arr[(right + 1) as usize] { right -= 1; }
                } else if s < t { left += 1; } else { right -= 1; }
            }
        }
    }
    res
}
fn main() {
    let got = four_sum(vec![1, 0, -1, 0, -2, 2], 0);
    assert_eq!(got.len(), 3);
    println!("PASS");
}
''',
"lua": '''local function four_sum(nums, target)
    local arr = {table.unpack(nums)}
    table.sort(arr)
    local res = {}
    local n = #arr
    for i = 1, n do
        if i == 1 or arr[i] ~= arr[i - 1] then
            for j = i + 1, n do
                if j == i + 1 or arr[j] ~= arr[j - 1] then
                    local left, right = j + 1, n
                    while left < right do
                        local s = arr[i] + arr[j] + arr[left] + arr[right]
                        if s == target then
                            res[#res + 1] = {arr[i], arr[j], arr[left], arr[right]}
                            left = left + 1
                            right = right - 1
                            while left < right and arr[left] == arr[left - 1] do left = left + 1 end
                            while left < right and arr[right] == arr[right + 1] do right = right - 1 end
                        elseif s < target then left = left + 1
                        else right = right - 1 end
                    end
                end
            end
        end
    end
    return res
end
local got = four_sum({1, 0, -1, 0, -2, 2}, 0)
assert(#got == 3, "count " .. #got)
print("PASS")
''',
"c": '''#include <stdio.h>
#include <stdlib.h>
static int cmp_int(const void *a, const void *b) { return *(const int *)a - *(const int *)b; }
static int four_sum(const int *nums, int n, int target, int out[][4]) {
    int arr[4096];
    for (int i = 0; i < n; i++) arr[i] = nums[i];
    qsort(arr, n, sizeof(int), cmp_int);
    int cnt = 0;
    for (int i = 0; i < n; i++) {
        if (i > 0 && arr[i] == arr[i - 1]) continue;
        for (int j = i + 1; j < n; j++) {
            if (j > i + 1 && arr[j] == arr[j - 1]) continue;
            int left = j + 1, right = n - 1;
            while (left < right) {
                long s = (long)arr[i] + arr[j] + arr[left] + arr[right];
                if (s == target) {
                    out[cnt][0] = arr[i]; out[cnt][1] = arr[j]; out[cnt][2] = arr[left]; out[cnt][3] = arr[right];
                    cnt++;
                    left++; right--;
                    while (left < right && arr[left] == arr[left - 1]) left++;
                    while (left < right && arr[right] == arr[right + 1]) right--;
                } else if (s < target) left++;
                else right--;
            }
        }
    }
    return cnt;
}
int main(void) {
    int out[64][4];
    int n = four_sum((int[]){1,0,-1,0,-2,2}, 6, 0, out);
    if (n != 3) { printf("FAIL cnt=%d\\n", n); return 1; }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''#include <algorithm>
#include <cassert>
#include <iostream>
#include <vector>
static std::vector<std::vector<int>> fourSum(std::vector<int> nums, int target) {
    std::sort(nums.begin(), nums.end());
    std::vector<std::vector<int>> res;
    int n = static_cast<int>(nums.size());
    for (int i = 0; i < n; ++i) {
        if (i > 0 && nums[i] == nums[i - 1]) continue;
        for (int j = i + 1; j < n; ++j) {
            if (j > i + 1 && nums[j] == nums[j - 1]) continue;
            int left = j + 1, right = n - 1;
            while (left < right) {
                long long s = static_cast<long long>(nums[i]) + nums[j] + nums[left] + nums[right];
                if (s == target) {
                    res.push_back({nums[i], nums[j], nums[left], nums[right]});
                    ++left; --right;
                    while (left < right && nums[left] == nums[left - 1]) ++left;
                    while (left < right && nums[right] == nums[right + 1]) --right;
                } else if (s < target) ++left;
                else --right;
            }
        }
    }
    return res;
}
int main() {
    auto got = fourSum({1, 0, -1, 0, -2, 2}, 0);
    assert(got.size() == 3);
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''four_sum <- function(nums, target) {
  arr <- sort(nums)
  res <- list()
  n <- length(arr)
  for (i in seq_len(n)) {
    if (i > 1 && arr[i] == arr[i - 1]) next
    for (j in (i + 1):n) {
      if (j > i + 1 && arr[j] == arr[j - 1]) next
      left <- j + 1; right <- n
      while (left < right) {
        s <- arr[i] + arr[j] + arr[left] + arr[right]
        if (s == target) {
          res[[length(res) + 1L]] <- c(arr[i], arr[j], arr[left], arr[right])
          left <- left + 1; right <- right - 1
          while (left < right && arr[left] == arr[left - 1]) left <- left + 1
          while (left < right && arr[right] == arr[right + 1]) right <- right - 1
        } else if (s < target) left <- left + 1
        else right <- right - 1
      }
    }
  }
  res
}
got <- four_sum(c(1, 0, -1, 0, -2, 2), 0)
stopifnot(length(got) == 3)
cat("PASS\\n")
''',
"zig": '''const std = @import("std");
fn fourSum(nums: []const i32, target: i32, alloc: std.mem.Allocator, out: *std.ArrayList([4]i32)) void {
    const arr = alloc.dupe(i32, nums) catch unreachable;
    std.sort.pdq(i32, arr, {}, std.sort.asc(i32));
    const n = arr.len;
    for (0..n) |i| {
        if (i > 0 and arr[i] == arr[i - 1]) continue;
        for (i + 1..n) |j| {
            if (j > i + 1 and arr[j] == arr[j - 1]) continue;
            var left = j + 1;
            var right = n - 1;
            while (left < right) {
                const s = @as(i64, arr[i]) + arr[j] + arr[left] + arr[right];
                if (s == target) {
                    out.append(.{ arr[i], arr[j], arr[left], arr[right] }) catch unreachable;
                    left += 1;
                    right -= 1;
                    while (left < right and arr[left] == arr[left - 1]) left += 1;
                    while (left < right and arr[right] == arr[right + 1]) right -= 1;
                } else if (s < target) left += 1
                else right -= 1;
            }
        }
    }
}
pub fn main() !void {
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();
    var out = std.ArrayList([4]i32).init(std.heap.page_allocator);
    defer out.deinit();
    fourSum(&[_]i32{ 1, 0, -1, 0, -2, 2 }, 0, arena.allocator(), &out);
    if (out.items.len != 3) return error.TestFailed;
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''List<List<int>> fourSum(List<int> nums, int target) {
  final arr = List<int>.from(nums)..sort();
  final res = <List<int>>[];
  final n = arr.length;
  for (var i = 0; i < n; i++) {
    if (i > 0 && arr[i] == arr[i - 1]) continue;
    for (var j = i + 1; j < n; j++) {
      if (j > i + 1 && arr[j] == arr[j - 1]) continue;
      var left = j + 1, right = n - 1;
      while (left < right) {
        final s = arr[i] + arr[j] + arr[left] + arr[right];
        if (s == target) {
          res.add([arr[i], arr[j], arr[left], arr[right]]);
          left++;
          right--;
          while (left < right && arr[left] == arr[left - 1]) left++;
          while (left < right && arr[right] == arr[right + 1]) right--;
        } else if (s < target) {
          left++;
        } else {
          right--;
        }
      }
    }
  }
  return res;
}
void main() {
  if (fourSum([1, 0, -1, 0, -2, 2], 0).length != 3) throw StateError('c1');
  print('PASS');
}
''',
}

A179 = {
"rust": '''fn largest_number(nums: Vec<i32>) -> String {
    let mut strs: Vec<String> = nums.iter().map(|x| x.to_string()).collect();
    strs.sort_by(|a, b| {
        let ab = format!("{}{}", a, b);
        let ba = format!("{}{}", b, a);
        ba.cmp(&ab)
    });
    if strs[0] == "0" { return "0".to_string(); }
    strs.concat()
}
fn main() {
    assert_eq!(largest_number(vec![10, 2]), "210");
    assert_eq!(largest_number(vec![3, 30, 34, 5, 9]), "9534330");
    assert_eq!(largest_number(vec![0, 0]), "0");
    println!("PASS");
}
''',
"lua": '''local function largest_number(nums)
    local strs = {}
    for i, v in ipairs(nums) do strs[i] = tostring(v) end
    table.sort(strs, function(a, b)
        return a .. b > b .. a
    end)
    if strs[1] == "0" then return "0" end
    return table.concat(strs)
end
assert(largest_number({10, 2}) == "210")
assert(largest_number({3, 30, 34, 5, 9}) == "9534330")
assert(largest_number({0, 0}) == "0")
print("PASS")
''',
"c": '''#include <stdio.h>
#include <stdlib.h>
#include <string.h>
static int cmp_str(const void *a, const void *b) {
    char ab[64], ba[64];
    snprintf(ab, sizeof(ab), "%s%s", *(const char **)a, *(const char **)b);
    snprintf(ba, sizeof(ba), "%s%s", *(const char **)b, *(const char **)a);
    return strcmp(ba, ab);
}
static void largest_number(const int *nums, int n, char out[]) {
    char strs[64][16];
    const char *ptrs[64];
    for (int i = 0; i < n; i++) {
        snprintf(strs[i], sizeof(strs[i]), "%d", nums[i]);
        ptrs[i] = strs[i];
    }
    qsort(ptrs, n, sizeof(char *), cmp_str);
    if (n > 0 && strcmp(ptrs[0], "0") == 0) { strcpy(out, "0"); return; }
    out[0] = '\\0';
    for (int i = 0; i < n; i++) strcat(out, ptrs[i]);
}
int main(void) {
    char out[4096];
    largest_number((int[]){10,2}, 2, out);
    if (strcmp(out, "210") != 0) { printf("FAIL 1 %s\\n", out); return 1; }
    largest_number((int[]){3,30,34,5,9}, 5, out);
    if (strcmp(out, "9534330") != 0) { printf("FAIL 2 %s\\n", out); return 1; }
    largest_number((int[]){0,0}, 2, out);
    if (strcmp(out, "0") != 0) { printf("FAIL 3 %s\\n", out); return 1; }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''#include <algorithm>
#include <cassert>
#include <iostream>
#include <string>
#include <vector>
static std::string largestNumber(const std::vector<int> &nums) {
    std::vector<std::string> strs;
    for (int v : nums) strs.push_back(std::to_string(v));
    std::sort(strs.begin(), strs.end(), [](const std::string &a, const std::string &b) {
        return a + b > b + a;
    });
    if (strs[0] == "0") return "0";
    std::string res;
    for (auto &s : strs) res += s;
    return res;
}
int main() {
    assert(largestNumber({10, 2}) == "210");
    assert(largestNumber({3, 30, 34, 5, 9}) == "9534330");
    assert(largestNumber({0, 0}) == "0");
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''cmp_concat_gt <- function(a, b) {
  # a+b 是否大于 b+a（字节序，免 locale 影响）
  ab <- utf8ToInt(paste0(a, b))
  ba <- utf8ToInt(paste0(b, a))
  for (i in seq_along(ab)) {
    if (ab[i] != ba[i]) return(ab[i] > ba[i])
  }
  FALSE
}
largest_number <- function(nums) {
  strs <- as.character(nums)
  n <- length(strs)
  repeat {
    changed <- FALSE
    for (i in 1:(n - 1)) {
      if (cmp_concat_gt(strs[i + 1], strs[i])) {
        t <- strs[i]; strs[i] <- strs[i + 1]; strs[i + 1] <- t
        changed <- TRUE
      }
    }
    if (!changed) break
  }
  if (strs[1] == "0") return("0")
  paste0(strs, collapse = "")
}
stopifnot(largest_number(c(10, 2)) == "210")
stopifnot(largest_number(c(3, 30, 34, 5, 9)) == "9534330")
stopifnot(largest_number(c(0, 0)) == "0")
cat("PASS\\n")
''',
"zig": '''const std = @import("std");
fn largestNumber(nums: []const i32, alloc: std.mem.Allocator, out: *std.ArrayList(u8)) void {
    var strs = std.ArrayList([]const u8).init(alloc);
    for (nums) |v| {
        var buf: [16]u8 = undefined;
        const s = std.fmt.bufPrint(&buf, "{d}", .{v}) catch unreachable;
        strs.append(alloc.dupe(u8, s) catch unreachable) catch unreachable;
    }
    const S = struct {
        fn lt(_: void, a: []const u8, b: []const u8) bool {
            var ab: [64]u8 = undefined;
            var ba: [64]u8 = undefined;
            const ablen = std.fmt.bufPrint(&ab, "{s}{s}", .{ a, b }) catch unreachable;
            const balen = std.fmt.bufPrint(&ba, "{s}{s}", .{ b, a }) catch unreachable;
            return std.mem.order(u8, ablen, balen) == .gt;
        }
    };
    std.sort.pdq([]const u8, strs.items, {}, S.lt);
    if (strs.items.len > 0 and std.mem.eql(u8, strs.items[0], "0")) {
        out.appendSlice("0") catch unreachable;
        return;
    }
    for (strs.items) |s| out.appendSlice(s) catch unreachable;
}
pub fn main() !void {
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();
    const alloc = arena.allocator();
    var out = std.ArrayList(u8).init(std.heap.page_allocator);
    defer out.deinit();
    largestNumber(&[_]i32{ 10, 2 }, alloc, &out);
    if (!std.mem.eql(u8, out.items, "210")) return error.TestFailed;
    out.clearRetainingCapacity();
    largestNumber(&[_]i32{ 3, 30, 34, 5, 9 }, alloc, &out);
    if (!std.mem.eql(u8, out.items, "9534330")) return error.TestFailed;
    out.clearRetainingCapacity();
    largestNumber(&[_]i32{ 0, 0 }, alloc, &out);
    if (!std.mem.eql(u8, out.items, "0")) return error.TestFailed;
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''String largestNumber(List<int> nums) {
  final strs = nums.map((v) => v.toString()).toList();
  strs.sort((a, b) => (b + a).compareTo(a + b));
  if (strs[0] == '0') return '0';
  return strs.join();
}
void main() {
  if (largestNumber([10, 2]) != '210') throw StateError('c1');
  if (largestNumber([3, 30, 34, 5, 9]) != '9534330') throw StateError('c2');
  if (largestNumber([0, 0]) != '0') throw StateError('c3');
  print('PASS');
}
''',
}

A1356 = {
"rust": '''fn count_bits(mut n: i32) -> i32 {
    let mut c = 0;
    while n > 0 { c += n & 1; n >>= 1; }
    c
}
fn sort_by_bits(nums: Vec<i32>) -> Vec<i32> {
    let mut arr = nums;
    arr.sort_by(|&a, &b| {
        let (ba, bb) = (count_bits(a), count_bits(b));
        ba.cmp(&bb).then(a.cmp(&b))
    });
    arr
}
fn main() {
    assert_eq!(sort_by_bits(vec![0, 1, 2, 3, 4, 5, 6, 7, 8]), vec![0, 1, 2, 4, 8, 3, 5, 6, 7]);
    assert_eq!(sort_by_bits(vec![1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]), vec![1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]);
    println!("PASS");
}
''',
"lua": '''local function count_bits(n)
    local c = 0
    while n > 0 do
        c = c + (n & 1)
        n = n >> 1
    end
    return c
end
local function sort_by_bits(nums)
    local arr = {table.unpack(nums)}
    table.sort(arr, function(a, b)
        local ba, bb = count_bits(a), count_bits(b)
        if ba ~= bb then return ba < bb end
        return a < b
    end)
    return arr
end
local a = sort_by_bits({0, 1, 2, 3, 4, 5, 6, 7, 8})
assert(#a == 9 and a[1] == 0 and a[2] == 1 and a[3] == 2 and a[4] == 4 and a[5] == 8 and a[6] == 3 and a[9] == 7)
print("PASS")
''',
"c": '''#include <stdio.h>
#include <stdlib.h>
static int count_bits(int n) { int c = 0; while (n) { c += n & 1; n >>= 1; } return c; }
static int cmp_bits(const void *a, const void *b) {
    int x = *(const int *)a, y = *(const int *)b;
    int bx = count_bits(x), by = count_bits(y);
    if (bx != by) return bx - by;
    return x - y;
}
static void sort_by_bits(const int *nums, int n, int out[]) {
    for (int i = 0; i < n; i++) out[i] = nums[i];
    qsort(out, n, sizeof(int), cmp_bits);
}
int main(void) {
    int out[64];
    int w[] = {0,1,2,4,8,3,5,6,7};
    sort_by_bits((int[]){0,1,2,3,4,5,6,7,8}, 9, out);
    for (int i = 0; i < 9; i++) if (out[i] != w[i]) { printf("FAIL %d\\n", i); return 1; }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''#include <algorithm>
#include <cassert>
#include <iostream>
#include <vector>
static int countBits(int n) { int c = 0; while (n) { c += n & 1; n >>= 1; } return c; }
static std::vector<int> sortByBits(std::vector<int> nums) {
    std::sort(nums.begin(), nums.end(), [](int a, int b) {
        int ba = countBits(a), bb = countBits(b);
        if (ba != bb) return ba < bb;
        return a < b;
    });
    return nums;
}
int main() {
    assert((sortByBits({0, 1, 2, 3, 4, 5, 6, 7, 8}) == std::vector<int>{0, 1, 2, 4, 8, 3, 5, 6, 7}));
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''count_bits <- function(n) {
  c <- 0L
  while (n > 0) { c <- c + bitwAnd(n, 1); n <- bitwShiftR(n, 1) }
  c
}
sort_by_bits <- function(nums) {
  b <- vapply(nums, count_bits, 0L)
  nums[order(b, nums)]
}
stopifnot(identical(sort_by_bits(0:8), c(0L, 1L, 2L, 4L, 8L, 3L, 5L, 6L, 7L)))
cat("PASS\\n")
''',
"zig": '''const std = @import("std");
fn countBits(n0: i32) i32 {
    var c: i32 = 0;
    var n = n0;
    while (n > 0) : (n >>= 1) c += n & 1;
    return c;
}
fn sortByBits(nums: []const i32, alloc: std.mem.Allocator) []i32 {
    const arr = alloc.dupe(i32, nums) catch unreachable;
    const S = struct {
        fn lt(_: void, a: i32, b: i32) bool {
            const ba = countBits(a);
            const bb = countBits(b);
            if (ba != bb) return ba < bb;
            return a < b;
        }
    };
    std.sort.pdq(i32, arr, {}, S.lt);
    return arr;
}
pub fn main() !void {
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();
    const got = sortByBits(&[_]i32{ 0, 1, 2, 3, 4, 5, 6, 7, 8 }, arena.allocator());
    const want = [_]i32{ 0, 1, 2, 4, 8, 3, 5, 6, 7 };
    if (got.len != want.len) return error.TestFailed;
    for (want, 0..) |w, i| if (got[i] != w) return error.TestFailed;
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''int countBits(int n) {
  var c = 0;
  while (n > 0) {
    c += n & 1;
    n >>= 1;
  }
  return c;
}
List<int> sortByBits(List<int> nums) {
  final arr = List<int>.from(nums)
    ..sort((a, b) {
      final ba = countBits(a), bb = countBits(b);
      if (ba != bb) return ba.compareTo(bb);
      return a.compareTo(b);
    });
  return arr;
}
void main() {
  if (sortByBits([0, 1, 2, 3, 4, 5, 6, 7, 8]).toString() != '[0, 1, 2, 4, 8, 3, 5, 6, 7]') throw StateError('c1');
  print('PASS');
}
''',
}

A937 = {
"rust": '''fn reorder_log_files(logs: Vec<String>) -> Vec<String> {
    let is_digit = |s: &str| !s.is_empty() && s.as_bytes()[0].is_ascii_digit();
    let mut letter: Vec<String> = Vec::new();
    let mut digit: Vec<String> = Vec::new();
    for log in logs {
        let idx = log.find(' ').unwrap();
        let content = &log[idx + 1..];
        if is_digit(content) { digit.push(log); } else { letter.push(log); }
    }
    letter.sort_by(|a, b| {
        let ia = a.find(' ').unwrap();
        let ib = b.find(' ').unwrap();
        let ca = &a[ia + 1..];
        let cb = &b[ib + 1..];
        ca.cmp(cb).then(a.cmp(b))
    });
    letter.extend(digit);
    letter
}
fn main() {
    let logs = vec![
        "a1 9 2 3 1".to_string(),
        "g1 act car".to_string(),
        "zo4 4 7".to_string(),
        "ab1 off key dog".to_string(),
        "a8 act zoo".to_string(),
    ];
    let got = reorder_log_files(logs);
    assert_eq!(got, vec!["g1 act car", "a8 act zoo", "ab1 off key dog", "a1 9 2 3 1", "zo4 4 7"]);
    println!("PASS");
}
''',
"lua": '''local function reorder_log_files(logs)
    local function is_digit(s)
        local c = s:sub(1, 1)
        return c >= "0" and c <= "9"
    end
    local letter, digit = {}, {}
    for _, log in ipairs(logs) do
        local content = log:match(" (.+)$")
        if is_digit(content) then digit[#digit + 1] = log else letter[#letter + 1] = log end
    end
    table.sort(letter, function(a, b)
        local ca = a:match(" (.+)$")
        local cb = b:match(" (.+)$")
        if ca ~= cb then return ca < cb end
        return a < b
    end)
    for _, d in ipairs(digit) do letter[#letter + 1] = d end
    return letter
end
local got = reorder_log_files({"a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"})
assert(#got == 5)
assert(got[1] == "g1 act car" and got[2] == "a8 act zoo" and got[3] == "ab1 off key dog" and got[4] == "a1 9 2 3 1" and got[5] == "zo4 4 7")
print("PASS")
''',
"c": '''#include <stdio.h>
#include <stdlib.h>
#include <string.h>
static const char *content_of(const char *log) {
    const char *sp = strchr(log, ' ');
    return sp ? sp + 1 : "";
}
static int is_digit_log(const char *log) {
    const char *c = content_of(log);
    return c[0] >= '0' && c[0] <= '9';
}
static int cmp_letter(const void *a, const void *b) {
    const char *la = *(const char **)a;
    const char *lb = *(const char **)b;
    int cr = strcmp(content_of(la), content_of(lb));
    if (cr != 0) return cr;
    return strcmp(la, lb);
}
static int reorder_log_files(const char *logs[], int n, const char *out[]) {
    const char *letter[64], *digit[64];
    int ln = 0, dn = 0;
    for (int i = 0; i < n; i++) {
        if (is_digit_log(logs[i])) digit[dn++] = logs[i];
        else letter[ln++] = logs[i];
    }
    qsort(letter, ln, sizeof(char *), cmp_letter);
    for (int i = 0; i < ln; i++) out[i] = letter[i];
    for (int i = 0; i < dn; i++) out[ln + i] = digit[i];
    return ln + dn;
}
int main(void) {
    const char *logs[] = {"a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"};
    const char *wants[] = {"g1 act car", "a8 act zoo", "ab1 off key dog", "a1 9 2 3 1", "zo4 4 7"};
    const char *out[64];
    int n = reorder_log_files(logs, 5, out);
    if (n != 5) { printf("FAIL n\\n"); return 1; }
    for (int i = 0; i < 5; i++) if (strcmp(out[i], wants[i]) != 0) { printf("FAIL %d: %s\\n", i, out[i]); return 1; }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''#include <algorithm>
#include <cassert>
#include <iostream>
#include <string>
#include <vector>
static std::vector<std::string> reorderLogFiles(std::vector<std::string> logs) {
    auto isDigit = [](const std::string &s) { return !s.empty() && isdigit(static_cast<unsigned char>(s[0])); };
    std::vector<std::string> letter, digit;
    for (auto &log : logs) {
        auto idx = log.find(' ');
        auto content = log.substr(idx + 1);
        if (isDigit(content)) digit.push_back(std::move(log));
        else letter.push_back(std::move(log));
    }
    std::stable_sort(letter.begin(), letter.end(), [](const std::string &a, const std::string &b) {
        auto ca = a.substr(a.find(' ') + 1);
        auto cb = b.substr(b.find(' ') + 1);
        if (ca != cb) return ca < cb;
        return a < b;
    });
    letter.insert(letter.end(), digit.begin(), digit.end());
    return letter;
}
int main() {
    auto got = reorderLogFiles({"a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"});
    assert((got == std::vector<std::string>{"g1 act car", "a8 act zoo", "ab1 off key dog", "a1 9 2 3 1", "zo4 4 7"}));
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''reorder_log_files <- function(logs) {
  content_of <- function(log) sub("^[^ ]+ ", "", log)
  is_digit <- function(log) {
    c <- substr(content_of(log), 1, 1)
    grepl("[0-9]", c)
  }
  letter <- character(0); digit <- character(0)
  for (log in logs) {
    if (is_digit(log)) digit <- c(digit, log) else letter <- c(letter, log)
  }
  # 排序：content 升序，平局按原字符串
  ord <- order(vapply(letter, content_of, ""), letter)
  c(letter[ord], digit)
}
got <- reorder_log_files(c("a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"))
stopifnot(identical(got, c("g1 act car", "a8 act zoo", "ab1 off key dog", "a1 9 2 3 1", "zo4 4 7")))
cat("PASS\\n")
''',
"zig": '''const std = @import("std");
fn contentOf(log: []const u8) []const u8 {
    const idx = std.mem.indexOfScalar(u8, log, ' ') orelse return "";
    return log[idx + 1 ..];
}
fn isDigitLog(log: []const u8) bool {
    const c = contentOf(log);
    return c.len > 0 and c[0] >= '0' and c[0] <= '9';
}
pub fn main() !void {
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();
    const alloc = arena.allocator();
    const logs = [_][]const u8{ "a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo" };
    var letter = std.ArrayList([]const u8).init(alloc);
    var digit = std.ArrayList([]const u8).init(alloc);
    for (logs) |log| {
        if (isDigitLog(log)) digit.append(log) catch unreachable else letter.append(log) catch unreachable;
    }
    const S = struct {
        fn lt(_: void, a: []const u8, b: []const u8) bool {
            const cr = std.mem.order(u8, contentOf(a), contentOf(b));
            if (cr != .eq) return cr == .lt;
            return std.mem.order(u8, a, b) == .lt;
        }
    };
    std.sort.pdq([]const u8, letter.items, {}, S.lt);
    const wants = [_][]const u8{ "g1 act car", "a8 act zoo", "ab1 off key dog", "a1 9 2 3 1", "zo4 4 7" };
    var wi: usize = 0;
    for (letter.items) |l| {
        if (!std.mem.eql(u8, l, wants[wi])) return error.TestFailed;
        wi += 1;
    }
    for (digit.items) |d| {
        if (!std.mem.eql(u8, d, wants[wi])) return error.TestFailed;
        wi += 1;
    }
    if (wi != 5) return error.TestFailed;
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''List<String> reorderLogFiles(List<String> logs) {
  bool isDigit(String s) => s.isNotEmpty && s[0].codeUnitAt(0) >= 0x30 && s[0].codeUnitAt(0) <= 0x39;
  String contentOf(String log) {
    final idx = log.indexOf(' ');
    return log.substring(idx + 1);
  }
  final letter = <String>[];
  final digit = <String>[];
  for (final log in logs) {
    if (isDigit(contentOf(log))) {
      digit.add(log);
    } else {
      letter.add(log);
    }
  }
  letter.sort((a, b) {
    final ca = contentOf(a);
    final cb = contentOf(b);
    if (ca != cb) return ca.compareTo(cb);
    return a.compareTo(b);
  });
  return [...letter, ...digit];
}
void main() {
  final got = reorderLogFiles(['a1 9 2 3 1', 'g1 act car', 'zo4 4 7', 'ab1 off key dog', 'a8 act zoo']);
  if (got.toString() != '[g1 act car, a8 act zoo, ab1 off key dog, a1 9 2 3 1, zo4 4 7]') throw StateError('c1');
  print('PASS');
}
''',
}

A922 = {
"rust": '''fn sort_array_by_parity_ii(nums: Vec<i32>) -> Vec<i32> {
    let mut sorted = nums;
    sorted.sort();
    let mut res = vec![0; sorted.len()];
    let (mut odd, mut even) = (1usize, 0usize);
    for &item in &sorted {
        if item % 2 != 0 { res[odd] = item; odd += 2; }
        else { res[even] = item; even += 2; }
    }
    res
}
fn main() {
    assert_eq!(sort_array_by_parity_ii(vec![4, 2, 5, 7]), vec![2, 5, 4, 7]);
    assert_eq!(sort_array_by_parity_ii(vec![2, 3]), vec![2, 3]);
    println!("PASS");
}
''',
"lua": '''local function sort_array_by_parity_ii(nums)
    local sorted = {table.unpack(nums)}
    table.sort(sorted)
    local res = {}
    local odd, even = 2, 1
    for _, item in ipairs(sorted) do
        if item % 2 == 1 then
            res[odd] = item
            odd = odd + 2
        else
            res[even] = item
            even = even + 2
        end
    end
    return res
end
local a = sort_array_by_parity_ii({4, 2, 5, 7})
assert(#a == 4 and a[1] == 2 and a[2] == 5 and a[3] == 4 and a[4] == 7)
local b = sort_array_by_parity_ii({2, 3})
assert(b[1] == 2 and b[2] == 3)
print("PASS")
''',
"c": '''#include <stdio.h>
#include <stdlib.h>
static int cmp_int(const void *a, const void *b) { return *(const int *)a - *(const int *)b; }
static void sort_array_by_parity_ii(const int *nums, int n, int res[]) {
    int sorted[4096];
    for (int i = 0; i < n; i++) sorted[i] = nums[i];
    qsort(sorted, n, sizeof(int), cmp_int);
    int odd = 1, even = 0;
    for (int i = 0; i < n; i++) {
        if (sorted[i] % 2 != 0) { res[odd] = sorted[i]; odd += 2; }
        else { res[even] = sorted[i]; even += 2; }
    }
}
int main(void) {
    int res[64];
    sort_array_by_parity_ii((int[]){4,2,5,7}, 4, res);
    if (res[0] != 2 || res[1] != 5 || res[2] != 4 || res[3] != 7) { printf("FAIL 1\\n"); return 1; }
    sort_array_by_parity_ii((int[]){2,3}, 2, res);
    if (res[0] != 2 || res[1] != 3) { printf("FAIL 2\\n"); return 1; }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''#include <algorithm>
#include <cassert>
#include <iostream>
#include <vector>
static std::vector<int> sortArrayByParityII(std::vector<int> nums) {
    std::sort(nums.begin(), nums.end());
    std::vector<int> res(nums.size());
    int odd = 1, even = 0;
    for (int item : nums) {
        if (item % 2 != 0) { res[odd] = item; odd += 2; }
        else { res[even] = item; even += 2; }
    }
    return res;
}
int main() {
    assert((sortArrayByParityII({4, 2, 5, 7}) == std::vector<int>{2, 5, 4, 7}));
    assert((sortArrayByParityII({2, 3}) == std::vector<int>{2, 3}));
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''sort_array_by_parity_ii <- function(nums) {
  sorted <- sort(nums)
  res <- integer(length(sorted))
  odd <- 2; even <- 1
  for (item in sorted) {
    if (item %% 2 == 1) { res[odd] <- item; odd <- odd + 2 } else { res[even] <- item; even <- even + 2 }
  }
  res
}
stopifnot(identical(sort_array_by_parity_ii(c(4, 2, 5, 7)), c(2, 5, 4, 7)))
stopifnot(identical(sort_array_by_parity_ii(c(2, 3)), c(2, 3)))
cat("PASS\\n")
''',
"zig": '''const std = @import("std");
fn sortArrayByParityII(nums: []const i32, alloc: std.mem.Allocator) []i32 {
    const sorted = alloc.dupe(i32, nums) catch unreachable;
    std.sort.pdq(i32, sorted, {}, std.sort.asc(i32));
    const res = alloc.alloc(i32, sorted.len) catch unreachable;
    var odd: usize = 1;
    var even: usize = 0;
    for (sorted) |item| {
        if (@mod(item, 2) != 0) {
            res[odd] = item;
            odd += 2;
        } else {
            res[even] = item;
            even += 2;
        }
    }
    return res;
}
pub fn main() !void {
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();
    const got = sortArrayByParityII(&[_]i32{ 4, 2, 5, 7 }, arena.allocator());
    const want = [_]i32{ 2, 5, 4, 7 };
    if (got.len != want.len) return error.TestFailed;
    for (want, 0..) |w, i| if (got[i] != w) return error.TestFailed;
    const got2 = sortArrayByParityII(&[_]i32{ 2, 3 }, arena.allocator());
    if (got2[0] != 2 or got2[1] != 3) return error.TestFailed;
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''List<int> sortArrayByParityII(List<int> nums) {
  final sorted = List<int>.from(nums)..sort();
  final res = List<int>.filled(sorted.length, 0);
  var odd = 1, even = 0;
  for (final item in sorted) {
    if (item % 2 != 0) {
      res[odd] = item;
      odd += 2;
    } else {
      res[even] = item;
      even += 2;
    }
  }
  return res;
}
void main() {
  if (sortArrayByParityII([4, 2, 5, 7]).toString() != '[2, 5, 4, 7]') throw StateError('c1');
  if (sortArrayByParityII([2, 3]).toString() != '[2, 3]') throw StateError('c2');
  print('PASS');
}
''',
}

PROBS = [
    ("lc_15_三数之和", A15, "LeetCode 15. 三数之和"),
    ("lc_18_四数之和", A18, "LeetCode 18. 四数之和"),
    ("lc_179_最大数", A179, "LeetCode 179. 最大数"),
    ("lc_1356_根据数字二进制下_1_的数目排序", A1356, "LeetCode 1356. 根据数字二进制下1的数目排序"),
    ("lc_937_重新排列日志文件", A937, "LeetCode 937. 重新排列日志文件"),
    ("lc_922_按奇偶排序数组_ii", A922, "LeetCode 922. 按奇偶排序数组II"),
]
count = 0
for prob, algo, title in PROBS:
    bid = B[prob.split("_")[1]]
    ts_dir = f"/Users/Wang/Code/webfault-ai/dsa/ts/sort/{prob}"
    sols = sorted(f[:-3] for f in os.listdir(ts_dir) if f.startswith("solution_") and f.endswith(".ts"))
    for lang in EXT:
        ext = EXT[lang]
        for sol in sols:
            n = sol.replace("solution_", "").split("_")[0]
            head = head_comment(lang, bid, f"{title} — {LANGNAME[lang]} 版（方案{n}）")
            emit(lang, f"sort/{prob}/{sol}.{ext}", head + "\n" + algo[lang])
            count += 1
print(f"emitted {count} files")
