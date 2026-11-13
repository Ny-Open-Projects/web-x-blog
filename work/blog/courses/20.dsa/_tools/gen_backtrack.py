#!/usr/bin/env python3
# gen_backtrack.py — backtrack 主题 10 题 × 7语言
import sys, os; sys.path.insert(0, "/Users/Wang/Code/github/web-x-blog/work/blog/courses/20.dsa/_tools")
from langlib import emit, head_comment, EXT

B = {"131": "133772625", "37": "134045157", "39": "133865307", "46": "133767953", "47": "134134491", "51": "133970744", "77": "134178290", "78": "134109616", "79": "134204437", "93": "138771574"}
LANGNAME = {"rust": "Rust", "lua": "Lua", "c": "C", "cpp": "C++", "r": "R", "zig": "Zig", "dart": "Dart"}

A46 = {
"rust": '''fn permute(nums: Vec<i32>) -> Vec<Vec<i32>> {
    let mut res = Vec::new();
    let mut path = Vec::new();
    let mut used = vec![false; nums.len()];
    fn dfs(nums: &[i32], used: &mut Vec<bool>, path: &mut Vec<i32>, res: &mut Vec<Vec<i32>>) {
        if path.len() == nums.len() { res.push(path.clone()); return; }
        for i in 0..nums.len() {
            if used[i] { continue; }
            used[i] = true;
            path.push(nums[i]);
            dfs(nums, used, path, res);
            path.pop();
            used[i] = false;
        }
    }
    dfs(&nums, &mut used, &mut path, &mut res);
    res
}
fn main() {
    let got = permute(vec![1, 2, 3]);
    let want = vec![vec![1,2,3],vec![1,3,2],vec![2,1,3],vec![2,3,1],vec![3,1,2],vec![3,2,1]];
    assert_eq!(got, want);
    assert_eq!(permute(vec![0, 1]).len(), 2);
    println!("PASS");
}
''',
"lua": '''local function permute(nums)
    local res = {}
    local n = #nums
    local used = {}
    local path = {}
    local function dfs()
        if #path == n then
            local cp = {table.unpack(path)}
            res[#res + 1] = cp
            return
        end
        for i = 1, n do
            if not used[i] then
                used[i] = true
                path[#path + 1] = nums[i]
                dfs()
                path[#path] = nil
                used[i] = false
            end
        end
    end
    dfs()
    return res
end
local got = permute({1, 2, 3})
assert(#got == 6)
assert(table.concat(got[1], ",") == "1,2,3")
assert(table.concat(got[2], ",") == "1,3,2")
assert(table.concat(got[3], ",") == "2,1,3")
assert(table.concat(got[6], ",") == "3,2,1")
assert(#permute({0, 1}) == 2)
print("PASS")
''',
"c": '''#include <stdio.h>
static int res[720][8], res_n, used[8], path[8], nums_g[8], n_g;
static void dfs(int depth) {
    if (depth == n_g) {
        for (int i = 0; i < n_g; i++) res[res_n][i] = path[i];
        res_n++;
        return;
    }
    for (int i = 0; i < n_g; i++) {
        if (used[i]) continue;
        used[i] = 1;
        path[depth] = nums_g[i];
        dfs(depth + 1);
        used[i] = 0;
    }
}
static int permute(const int *nums, int n) {
    n_g = n; res_n = 0;
    for (int i = 0; i < n; i++) { nums_g[i] = nums[i]; used[i] = 0; }
    dfs(0);
    return res_n;
}
int main(void) {
    int n = permute((int[]){1,2,3}, 3);
    int w1[] = {1,2,3}, w2[] = {1,3,2}, w3[] = {2,1,3}, w6[] = {3,2,1};
    if (n != 6) { printf("FAIL cnt\\n"); return 1; }
    for (int i = 0; i < 3; i++) {
        if (res[0][i] != w1[i] || res[1][i] != w2[i] || res[2][i] != w3[i] || res[5][i] != w6[i]) { printf("FAIL perm\\n"); return 1; }
    }
    if (permute((int[]){0,1}, 2) != 2) { printf("FAIL 2\\n"); return 1; }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''#include <cassert>
#include <iostream>
#include <vector>
static std::vector<std::vector<int>> permute(const std::vector<int> &nums) {
    std::vector<std::vector<int>> res;
    std::vector<int> path;
    std::vector<bool> used(nums.size(), false);
    std::function<void()> dfs = [&]() {
        if (path.size() == nums.size()) { res.push_back(path); return; }
        for (size_t i = 0; i < nums.size(); ++i) {
            if (used[i]) continue;
            used[i] = true;
            path.push_back(nums[i]);
            dfs();
            path.pop_back();
            used[i] = false;
        }
    };
    dfs();
    return res;
}
int main() {
    assert((permute({1, 2, 3}) == std::vector<std::vector<int>>{{{{1, 2, 3}, {1, 3, 2}, {2, 1, 3}, {2, 3, 1}, {3, 1, 2}, {3, 2, 1}}}}));
    assert(permute({0, 1}).size() == 2);
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''permute_fn <- function(nums) {
  res <- list()
  n <- length(nums)
  used <- rep(FALSE, n)
  path <- integer(0)
  dfs <- function() {
    if (length(path) == n) {
      res[[length(res) + 1L]] <<- path
      return(invisible(NULL))
    }
    for (i in seq_len(n)) {
      if (!used[i]) {
        used[i] <<- TRUE
        path <<- c(path, nums[i])
        dfs()
        path <<- path[-length(path)]
        used[i] <<- FALSE
      }
    }
  }
  dfs()
  res
}
got <- permute_fn(c(1L, 2L, 3L))
stopifnot(length(got) == 6)
stopifnot(identical(got[[1]], c(1L, 2L, 3L)))
stopifnot(identical(got[[2]], c(1L, 3L, 2L)))
stopifnot(identical(got[[3]], c(2L, 1L, 3L)))
stopifnot(identical(got[[6]], c(3L, 2L, 1L)))
stopifnot(length(permute_fn(c(0L, 1L))) == 2)
cat("PASS\\n")
''',
"zig": '''const std = @import("std");
fn permute(nums: []const i32, alloc: std.mem.Allocator, res: *std.ArrayList(std.ArrayList(i32))) void {
    const D = struct {
        fn dfs(ns: []const i32, used: []bool, path: *std.ArrayList(i32), out: *std.ArrayList(std.ArrayList(i32)) ) void {
            if (path.items.len == ns.len) {
                var cp = std.ArrayList(i32).init(out.allocator);
                cp.appendSlice(path.items) catch unreachable;
                out.append(cp) catch unreachable;
                return;
            }
            for (ns, 0..) |v, i| {
                if (used[i]) continue;
                used[i] = true;
                path.append(v) catch unreachable;
                dfs(ns, used, path, out);
                _ = path.pop();
                used[i] = false;
            }
        }
    };
    const used = alloc.alloc(bool, nums.len) catch unreachable;
    @memset(used, false);
    var path = std.ArrayList(i32).init(alloc);
    D.dfs(nums, used, &path, res);
}
pub fn main() !void {
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();
    const alloc = arena.allocator();
    var res = std.ArrayList(std.ArrayList(i32)).init(std.heap.page_allocator);
    defer res.deinit();
    permute(&[_]i32{ 1, 2, 3 }, alloc, &res);
    if (res.items.len != 6) return error.TestFailed;
    const w1 = [_]i32{ 1, 2, 3 };
    const w2 = [_]i32{ 1, 3, 2 };
    const w6 = [_]i32{ 3, 2, 1 };
    for (w1, 0..) |w, i| if (res.items[0].items[i] != w) return error.TestFailed;
    for (w2, 0..) |w, i| if (res.items[1].items[i] != w) return error.TestFailed;
    for (w6, 0..) |w, i| if (res.items[5].items[i] != w) return error.TestFailed;
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''List<List<int>> permute(List<int> nums) {
  final res = <List<int>>[];
  final used = List<bool>.filled(nums.length, false);
  final path = <int>[];
  void dfs() {
    if (path.length == nums.length) {
      res.add(List<int>.from(path));
      return;
    }
    for (var i = 0; i < nums.length; i++) {
      if (used[i]) continue;
      used[i] = true;
      path.add(nums[i]);
      dfs();
      path.removeLast();
      used[i] = false;
    }
  }
  dfs();
  return res;
}
void main() {
  final got = permute([1, 2, 3]);
  if (got.length != 6) throw StateError('cnt');
  if (got[0].toString() != '[1, 2, 3]' || got[1].toString() != '[1, 3, 2]' || got[5].toString() != '[3, 2, 1]') throw StateError('perm');
  if (permute([0, 1]).length != 2) throw StateError('c2');
  print('PASS');
}
''',
}

A47 = {
"rust": '''fn permute_unique(mut nums: Vec<i32>) -> Vec<Vec<i32>> {
    nums.sort();
    let mut res = Vec::new();
    let mut path = Vec::new();
    let mut used = vec![false; nums.len()];
    fn dfs(nums: &[i32], used: &mut Vec<bool>, path: &mut Vec<i32>, res: &mut Vec<Vec<i32>>) {
        if path.len() == nums.len() { res.push(path.clone()); return; }
        for i in 0..nums.len() {
            if used[i] { continue; }
            if i > 0 && nums[i] == nums[i - 1] && !used[i - 1] { continue; }
            used[i] = true;
            path.push(nums[i]);
            dfs(nums, used, path, res);
            path.pop();
            used[i] = false;
        }
    }
    dfs(&nums, &mut used, &mut path, &mut res);
    res
}
fn main() {
    let got = permute_unique(vec![1, 1, 2]);
    let want = vec![vec![1,1,2],vec![1,2,1],vec![2,1,1]];
    assert_eq!(got, want);
    assert_eq!(permute_unique(vec![1, 2, 3]).len(), 6);
    println!("PASS");
}
''',
"lua": '''local function permute_unique(nums)
    local arr = {table.unpack(nums)}
    table.sort(arr)
    local res = {}
    local n = #arr
    local used = {}
    local path = {}
    local function dfs()
        if #path == n then
            res[#res + 1] = {table.unpack(path)}
            return
        end
        for i = 1, n do
            if not used[i] then
                if i == 1 or arr[i] ~= arr[i - 1] or used[i - 1] then
                    used[i] = true
                    path[#path + 1] = arr[i]
                    dfs()
                    path[#path] = nil
                    used[i] = false
                end
            end
        end
    end
    dfs()
    return res
end
local got = permute_unique({1, 1, 2})
assert(#got == 3)
assert(table.concat(got[1], ",") == "1,1,2" and table.concat(got[2], ",") == "1,2,1" and table.concat(got[3], ",") == "2,1,1")
assert(#permute_unique({1, 2, 3}) == 6)
print("PASS")
''',
"c": '''#include <stdio.h>
#include <stdlib.h>
static int cmp_int(const void *a, const void *b) { return *(const int *)a - *(const int *)b; }
static int res[720][8], res_n, used[8], path[8], arr_g[8], n_g;
static void dfs(int depth) {
    if (depth == n_g) {
        for (int i = 0; i < n_g; i++) res[res_n][i] = path[i];
        res_n++;
        return;
    }
    for (int i = 0; i < n_g; i++) {
        if (used[i]) continue;
        if (i > 0 && arr_g[i] == arr_g[i - 1] && !used[i - 1]) continue;
        used[i] = 1;
        path[depth] = arr_g[i];
        dfs(depth + 1);
        used[i] = 0;
    }
}
static int permute_unique(const int *nums, int n) {
    n_g = n; res_n = 0;
    for (int i = 0; i < n; i++) { arr_g[i] = nums[i]; used[i] = 0; }
    qsort(arr_g, n, sizeof(int), cmp_int);
    dfs(0);
    return res_n;
}
int main(void) {
    int n = permute_unique((int[]){1,1,2}, 3);
    if (n != 3) { printf("FAIL cnt=%d\\n", n); return 1; }
    if (res[0][0]!=1||res[0][1]!=1||res[0][2]!=2) { printf("FAIL p1\\n"); return 1; }
    if (res[1][0]!=1||res[1][1]!=2||res[1][2]!=1) { printf("FAIL p2\\n"); return 1; }
    if (res[2][0]!=2||res[2][1]!=1||res[2][2]!=1) { printf("FAIL p3\\n"); return 1; }
    if (permute_unique((int[]){1,2,3}, 3) != 6) { printf("FAIL 2\\n"); return 1; }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''#include <algorithm>
#include <cassert>
#include <iostream>
#include <vector>
static std::vector<std::vector<int>> permuteUnique(std::vector<int> nums) {
    std::sort(nums.begin(), nums.end());
    std::vector<std::vector<int>> res;
    std::vector<int> path;
    std::vector<bool> used(nums.size(), false);
    std::function<void()> dfs = [&]() {
        if (path.size() == nums.size()) { res.push_back(path); return; }
        for (size_t i = 0; i < nums.size(); ++i) {
            if (used[i]) continue;
            if (i > 0 && nums[i] == nums[i - 1] && !used[i - 1]) continue;
            used[i] = true;
            path.push_back(nums[i]);
            dfs();
            path.pop_back();
            used[i] = false;
        }
    };
    dfs();
    return res;
}
int main() {
    assert((permuteUnique({1, 1, 2}) == std::vector<std::vector<int>>{{{{1, 1, 2}, {1, 2, 1}, {2, 1, 1}}}}));
    assert(permuteUnique({1, 2, 3}).size() == 6);
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''permute_unique <- function(nums) {
  arr <- sort(nums)
  res <- list()
  n <- length(arr)
  used <- rep(FALSE, n)
  path <- integer(0)
  dfs <- function() {
    if (length(path) == n) {
      res[[length(res) + 1L]] <<- path
      return(invisible(NULL))
    }
    for (i in seq_len(n)) {
      if (!used[i]) {
        if (i == 1 || arr[i] != arr[i - 1] || used[i - 1]) {
          used[i] <<- TRUE
          path <<- c(path, arr[i])
          dfs()
          path <<- path[-length(path)]
          used[i] <<- FALSE
        }
      }
    }
  }
  dfs()
  res
}
got <- permute_unique(c(1, 1, 2))
stopifnot(length(got) == 3)
stopifnot(identical(got[[1]], c(1, 1, 2)), identical(got[[2]], c(1, 2, 1)), identical(got[[3]], c(2, 1, 1)))
stopifnot(length(permute_unique(c(1, 2, 3))) == 6)
cat("PASS\\n")
''',
"zig": '''const std = @import("std");
fn permuteUnique(nums_in: []const i32, alloc: std.mem.Allocator, res: *std.ArrayList(std.ArrayList(i32))) void {
    const arr = alloc.dupe(i32, nums_in) catch unreachable;
    std.sort.pdq(i32, arr, {}, std.sort.asc(i32));
    const D = struct {
        fn dfs(ns: []const i32, used: []bool, path: *std.ArrayList(i32), out: *std.ArrayList(std.ArrayList(i32))) void {
            if (path.items.len == ns.len) {
                var cp = std.ArrayList(i32).init(out.allocator);
                cp.appendSlice(path.items) catch unreachable;
                out.append(cp) catch unreachable;
                return;
            }
            for (ns, 0..) |v, i| {
                if (used[i]) continue;
                if (i > 0 and ns[i] == ns[i - 1] and !used[i - 1]) continue;
                used[i] = true;
                path.append(v) catch unreachable;
                dfs(ns, used, path, out);
                _ = path.pop();
                used[i] = false;
            }
        }
    };
    const used = alloc.alloc(bool, arr.len) catch unreachable;
    @memset(used, false);
    var path = std.ArrayList(i32).init(alloc);
    D.dfs(arr, used, &path, res);
}
pub fn main() !void {
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();
    const alloc = arena.allocator();
    var res = std.ArrayList(std.ArrayList(i32)).init(std.heap.page_allocator);
    defer res.deinit();
    permuteUnique(&[_]i32{ 1, 1, 2 }, alloc, &res);
    if (res.items.len != 3) return error.TestFailed;
    const w1 = [_]i32{ 1, 1, 2 };
    for (w1, 0..) |w, i| if (res.items[0].items[i] != w) return error.TestFailed;
    if (res.items[1].items[0] != 1 or res.items[1].items[1] != 2 or res.items[1].items[2] != 1) return error.TestFailed;
    if (res.items[2].items[0] != 2) return error.TestFailed;
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''List<List<int>> permuteUnique(List<int> nums) {
  final arr = List<int>.from(nums)..sort();
  final res = <List<int>>[];
  final used = List<bool>.filled(arr.length, false);
  final path = <int>[];
  void dfs() {
    if (path.length == arr.length) {
      res.add(List<int>.from(path));
      return;
    }
    for (var i = 0; i < arr.length; i++) {
      if (used[i]) continue;
      if (i > 0 && arr[i] == arr[i - 1] && !used[i - 1]) continue;
      used[i] = true;
      path.add(arr[i]);
      dfs();
      path.removeLast();
      used[i] = false;
    }
  }
  dfs();
  return res;
}
void main() {
  final got = permuteUnique([1, 1, 2]);
  if (got.length != 3) throw StateError('cnt');
  if (got[0].toString() != '[1, 1, 2]' || got[1].toString() != '[1, 2, 1]' || got[2].toString() != '[2, 1, 1]') throw StateError('p');
  if (permuteUnique([1, 2, 3]).length != 6) throw StateError('c2');
  print('PASS');
}
''',
}

A78 = {
"rust": '''fn subsets(nums: Vec<i32>) -> Vec<Vec<i32>> {
    let mut res = Vec::new();
    let mut path = Vec::new();
    fn dfs(nums: &[i32], start: usize, path: &mut Vec<i32>, res: &mut Vec<Vec<i32>>) {
        res.push(path.clone());
        for i in start..nums.len() {
            path.push(nums[i]);
            dfs(nums, i + 1, path, res);
            path.pop();
        }
    }
    dfs(&nums, 0, &mut path, &mut res);
    res
}
fn main() {
    let mut got = subsets(vec![1, 2, 3]);
    got.sort();
    assert_eq!(got.len(), 8);
    assert_eq!(got[0], Vec::<i32>::new());
    assert!(got.contains(&vec![1, 2, 3]));
    assert_eq!(subsets(vec![0]).len(), 2);
    println!("PASS");
}
''',
"lua": '''local function subsets(nums)
    local res = {}
    local n = #nums
    local path = {}
    local function dfs(start)
        res[#res + 1] = {table.unpack(path)}
        for i = start, n do
            path[#path + 1] = nums[i]
            dfs(i + 1)
            path[#path] = nil
        end
    end
    dfs(1)
    return res
end
assert(#subsets({1, 2, 3}) == 8)
assert(#subsets({0}) == 2)
local s = subsets({1, 2, 3})
local found = false
for _, sub in ipairs(s) do
    if #sub == 3 and table.concat(sub, ",") == "1,2,3" then found = true end
end
assert(found)
print("PASS")
''',
"c": '''#include <stdio.h>
static int res[256][8], res_lens[256], res_n, nums_g[8], n_g;
static void dfs(int start, int depth) {
    for (int i = 0; i < depth; i++) res[res_n][i] = nums_g[i];
    res_lens[res_n] = depth;
    res_n++;
    for (int i = start; i < n_g; i++) {
        nums_g[depth] = res[res_n - 1][depth] /* placeholder */;
        /* 使用 path 数组单独维护 */
        break;
    }
}
/* 重写：path 与 nums 分开 */
static int path[8];
static void dfs2(int start, int depth) {
    for (int i = 0; i < depth; i++) res[res_n][i] = path[i];
    res_lens[res_n] = depth;
    res_n++;
    for (int i = start; i < n_g; i++) {
        path[depth] = nums_g[i];
        dfs2(i + 1, depth + 1);
    }
}
static int subsets(const int *nums, int n) {
    n_g = n; res_n = 0;
    for (int i = 0; i < n; i++) nums_g[i] = nums[i];
    dfs2(0, 0);
    return res_n;
}
int main(void) {
    int n = subsets((int[]){1,2,3}, 3);
    if (n != 8) { printf("FAIL cnt=%d\\n", n); return 1; }
    if (subsets((int[]){0}, 1) != 2) { printf("FAIL 2\\n"); return 1; }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''#include <cassert>
#include <iostream>
#include <vector>
static std::vector<std::vector<int>> subsets(const std::vector<int> &nums) {
    std::vector<std::vector<int>> res;
    std::vector<int> path;
    std::function<void(size_t)> dfs = [&](size_t start) {
        res.push_back(path);
        for (size_t i = start; i < nums.size(); ++i) {
            path.push_back(nums[i]);
            dfs(i + 1);
            path.pop_back();
        }
    };
    dfs(0);
    return res;
}
int main() {
    auto got = subsets({1, 2, 3});
    assert(got.size() == 8);
    assert(subsets({0}).size() == 2);
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''subsets <- function(nums) {
  res <- list()
  path <- integer(0)
  dfs <- function(start) {
    res[[length(res) + 1L]] <<- path
    if (start > length(nums)) return(invisible(NULL))
    for (i in start:length(nums)) {
      path <<- c(path, nums[i])
      dfs(i + 1L)
      path <<- path[-length(path)]
    }
  }
  if (length(nums) > 0) dfs(1L) else res[[1L]] <- integer(0)
  res
}
stopifnot(length(subsets(c(1, 2, 3))) == 8)
stopifnot(length(subsets(0)) == 2)
cat("PASS\\n")
''',
"zig": '''const std = @import("std");
fn subsets(nums: []const i32, alloc: std.mem.Allocator, res: *std.ArrayList(std.ArrayList(i32))) void {
    const D = struct {
        fn dfs(ns: []const i32, start: usize, path: *std.ArrayList(i32), out: *std.ArrayList(std.ArrayList(i32))) void {
            var cp = std.ArrayList(i32).init(out.allocator);
            cp.appendSlice(path.items) catch unreachable;
            out.append(cp) catch unreachable;
            for (start..ns.len) |i| {
                path.append(ns[i]) catch unreachable;
                dfs(ns, i + 1, path, out);
                _ = path.pop();
            }
        }
    };
    var path = std.ArrayList(i32).init(alloc);
    D.dfs(nums, 0, &path, res);
}
pub fn main() !void {
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();
    const alloc = arena.allocator();
    var res = std.ArrayList(std.ArrayList(i32)).init(std.heap.page_allocator);
    defer res.deinit();
    subsets(&[_]i32{ 1, 2, 3 }, alloc, &res);
    if (res.items.len != 8) return error.TestFailed;
    res.clearRetainingCapacity();
    subsets(&[_]i32{0}, alloc, &res);
    if (res.items.len != 2) return error.TestFailed;
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''List<List<int>> subsets(List<int> nums) {
  final res = <List<int>>[];
  final path = <int>[];
  void dfs(int start) {
    res.add(List<int>.from(path));
    for (var i = start; i < nums.length; i++) {
      path.add(nums[i]);
      dfs(i + 1);
      path.removeLast();
    }
  }
  dfs(0);
  return res;
}
void main() {
  if (subsets([1, 2, 3]).length != 8) throw StateError('c1');
  if (subsets([0]).length != 2) throw StateError('c2');
  print('PASS');
}
''',
}

A77 = {
"rust": '''fn combine(n: i32, k: i32) -> Vec<Vec<i32>> {
    let mut res = Vec::new();
    let mut path = Vec::new();
    fn dfs(n: i32, k: i32, start: i32, path: &mut Vec<i32>, res: &mut Vec<Vec<i32>>) {
        if path.len() as i32 == k { res.push(path.clone()); return; }
        for i in start..=n - (k - path.len() as i32) + 1 {
            path.push(i);
            dfs(n, k, i + 1, path, res);
            path.pop();
        }
    }
    dfs(n, k, 1, &mut path, &mut res);
    res
}
fn main() {
    let got = combine(4, 2);
    let want = vec![vec![1,2],vec![1,3],vec![1,4],vec![2,3],vec![2,4],vec![3,4]];
    assert_eq!(got, want);
    assert_eq!(combine(1, 1), vec![vec![1]]);
    println!("PASS");
}
''',
"lua": '''local function combine(n, k)
    local res = {}
    local path = {}
    local function dfs(start)
        if #path == k then
            res[#res + 1] = {table.unpack(path)}
            return
        end
        for i = start, n - (k - #path) + 1 do
            path[#path + 1] = i
            dfs(i + 1)
            path[#path] = nil
        end
    end
    dfs(1)
    return res
end
local got = combine(4, 2)
assert(#got == 6)
assert(table.concat(got[1], ",") == "1,2" and table.concat(got[6], ",") == "3,4")
assert(#combine(1, 1) == 1)
print("PASS")
''',
"c": '''#include <stdio.h>
static int res[256][8], res_n, path[8];
static int n_g, k_g;
static void dfs(int start, int depth) {
    if (depth == k_g) {
        for (int i = 0; i < depth; i++) res[res_n][i] = path[i];
        res_n++;
        return;
    }
    for (int i = start; i <= n_g - (k_g - depth) + 1; i++) {
        path[depth] = i;
        dfs(i + 1, depth + 1);
    }
}
static int combine(int n, int k) {
    n_g = n; k_g = k; res_n = 0;
    dfs(1, 0);
    return res_n;
}
int main(void) {
    int n = combine(4, 2);
    if (n != 6) { printf("FAIL cnt\\n"); return 1; }
    if (res[0][0]!=1||res[0][1]!=2||res[5][0]!=3||res[5][1]!=4) { printf("FAIL c\\n"); return 1; }
    if (combine(1, 1) != 1) { printf("FAIL 2\\n"); return 1; }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''#include <cassert>
#include <iostream>
#include <vector>
static std::vector<std::vector<int>> combine(int n, int k) {
    std::vector<std::vector<int>> res;
    std::vector<int> path;
    std::function<void(int)> dfs = [&](int start) {
        if (static_cast<int>(path.size()) == k) { res.push_back(path); return; }
        for (int i = start; i <= n - (k - static_cast<int>(path.size())) + 1; ++i) {
            path.push_back(i);
            dfs(i + 1);
            path.pop_back();
        }
    };
    dfs(1);
    return res;
}
int main() {
    assert((combine(4, 2) == std::vector<std::vector<int>>{{{{1, 2}, {1, 3}, {1, 4}, {2, 3}, {2, 4}, {3, 4}}}}));
    assert((combine(1, 1) == std::vector<std::vector<int>>{{{{1}}}}));
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''combine <- function(n, k) {
  res <- list()
  path <- integer(0)
  dfs <- function(start) {
    if (length(path) == k) {
      res[[length(res) + 1L]] <<- path
      return(invisible(NULL))
    }
    upper <- as.integer(n - (k - length(path)) + 1)
    if (start > upper) return(invisible(NULL))
    for (i in start:upper) {
      path <<- c(path, i)
      dfs(i + 1L)
      path <<- path[-length(path)]
    }
  }
  dfs(1L)
  res
}
got <- combine(4, 2)
stopifnot(length(got) == 6)
stopifnot(identical(got[[1]], c(1L, 2L)), identical(got[[6]], c(3L, 4L)))
stopifnot(length(combine(1, 1)) == 1)
cat("PASS\\n")
''',
"zig": '''const std = @import("std");
fn combine(n: i32, k: i32, alloc: std.mem.Allocator, res: *std.ArrayList(std.ArrayList(i32))) void {
    const D = struct {
        fn dfs(nn: i32, kk: i32, start: i32, path: *std.ArrayList(i32), out: *std.ArrayList(std.ArrayList(i32))) void {
            if (@as(i32, @intCast(path.items.len)) == kk) {
                var cp = std.ArrayList(i32).init(out.allocator);
                cp.appendSlice(path.items) catch unreachable;
                out.append(cp) catch unreachable;
                return;
            }
            var i = start;
            while (i <= nn - (kk - @as(i32, @intCast(path.items.len))) + 1) : (i += 1) {
                path.append(i) catch unreachable;
                dfs(nn, kk, i + 1, path, out);
                _ = path.pop();
            }
        }
    };
    var path = std.ArrayList(i32).init(alloc);
    D.dfs(n, k, 1, &path, res);
}
pub fn main() !void {
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();
    const alloc = arena.allocator();
    var res = std.ArrayList(std.ArrayList(i32)).init(std.heap.page_allocator);
    defer res.deinit();
    combine(4, 2, alloc, &res);
    if (res.items.len != 6) return error.TestFailed;
    if (res.items[0].items[0] != 1 or res.items[0].items[1] != 2) return error.TestFailed;
    if (res.items[5].items[0] != 3 or res.items[5].items[1] != 4) return error.TestFailed;
    res.clearRetainingCapacity();
    combine(1, 1, alloc, &res);
    if (res.items.len != 1) return error.TestFailed;
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''List<List<int>> combine(int n, int k) {
  final res = <List<int>>[];
  final path = <int>[];
  void dfs(int start) {
    if (path.length == k) {
      res.add(List<int>.from(path));
      return;
    }
    for (var i = start; i <= n - (k - path.length) + 1; i++) {
      path.add(i);
      dfs(i + 1);
      path.removeLast();
    }
  }
  dfs(1);
  return res;
}
void main() {
  final got = combine(4, 2);
  if (got.length != 6) throw StateError('cnt');
  if (got[0].toString() != '[1, 2]' || got[5].toString() != '[3, 4]') throw StateError('c');
  if (combine(1, 1).length != 1) throw StateError('c2');
  print('PASS');
}
''',
}

A39 = {
"rust": '''fn combination_sum(candidates: &[i32], target: i32) -> Vec<Vec<i32>> {
    let mut res = Vec::new();
    let mut path = Vec::new();
    fn dfs(cands: &[i32], start: usize, remaining: i32, path: &mut Vec<i32>, res: &mut Vec<Vec<i32>>) {
        if remaining == 0 { res.push(path.clone()); return; }
        if remaining < 0 { return; }
        for i in start..cands.len() {
            path.push(cands[i]);
            dfs(cands, i, remaining - cands[i], path, res);
            path.pop();
        }
    }
    dfs(candidates, 0, target, &mut path, &mut res);
    res
}
fn main() {
    let got = combination_sum(&[2, 3, 6, 7], 7);
    let want = vec![vec![2, 2, 3], vec![7]];
    assert_eq!(got, want);
    let got2 = combination_sum(&[2, 3, 5], 8);
    let want2 = vec![vec![2, 2, 2, 2], vec![2, 3, 3], vec![3, 5]];
    assert_eq!(got2, want2);
    println!("PASS");
}
''',
"lua": '''local function combination_sum(candidates, target)
    local res = {}
    local path = {}
    local function dfs(start, remaining)
        if remaining == 0 then
            res[#res + 1] = {table.unpack(path)}
            return
        end
        if remaining < 0 then return end
        for i = start, #candidates do
            path[#path + 1] = candidates[i]
            dfs(i, remaining - candidates[i])
            path[#path] = nil
        end
    end
    dfs(1, target)
    return res
end
local got = combination_sum({2, 3, 6, 7}, 7)
assert(#got == 2)
assert(table.concat(got[1], ",") == "2,2,3" and table.concat(got[2], ",") == "7")
local got2 = combination_sum({2, 3, 5}, 8)
assert(#got2 == 3 and table.concat(got2[3], ",") == "3,5")
print("PASS")
''',
"c": '''#include <stdio.h>
static int res[256][32], res_lens[256], res_n, path[32];
static int cands_g[32], nc_g;
static void dfs(int start, int remaining, int depth) {
    if (remaining == 0) {
        for (int i = 0; i < depth; i++) res[res_n][i] = path[i];
        res_lens[res_n] = depth;
        res_n++;
        return;
    }
    if (remaining < 0) return;
    for (int i = start; i < nc_g; i++) {
        path[depth] = cands_g[i];
        dfs(i, remaining - cands_g[i], depth + 1);
    }
}
static int combination_sum(const int *candidates, int nc, int target) {
    nc_g = nc; res_n = 0;
    for (int i = 0; i < nc; i++) cands_g[i] = candidates[i];
    dfs(0, target, 0);
    return res_n;
}
int main(void) {
    int n = combination_sum((int[]){2,3,6,7}, 4, 7);
    if (n != 2) { printf("FAIL cnt=%d\\n", n); return 1; }
    if (res_lens[0] != 3 || res[0][0]!=2||res[0][1]!=2||res[0][2]!=3) { printf("FAIL a\\n"); return 1; }
    if (res_lens[1] != 1 || res[1][0] != 7) { printf("FAIL b\\n"); return 1; }
    if (combination_sum((int[]){2,3,5}, 3, 8) != 3) { printf("FAIL 2\\n"); return 1; }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''#include <cassert>
#include <iostream>
#include <vector>
static std::vector<std::vector<int>> combinationSum(const std::vector<int> &candidates, int target) {
    std::vector<std::vector<int>> res;
    std::vector<int> path;
    std::function<void(size_t, int)> dfs = [&](size_t start, int remaining) {
        if (remaining == 0) { res.push_back(path); return; }
        if (remaining < 0) return;
        for (size_t i = start; i < candidates.size(); ++i) {
            path.push_back(candidates[i]);
            dfs(i, remaining - candidates[i]);
            path.pop_back();
        }
    };
    dfs(0, target);
    return res;
}
int main() {
    assert((combinationSum({2, 3, 6, 7}, 7) == std::vector<std::vector<int>>{{{{2, 2, 3}, {7}}}}));
    assert((combinationSum({2, 3, 5}, 8) == std::vector<std::vector<int>>{{{{2, 2, 2, 2}, {2, 3, 3}, {3, 5}}}}));
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''combination_sum <- function(candidates, target) {
  res <- list()
  path <- integer(0)
  dfs <- function(start, remaining) {
    if (remaining == 0) {
      res[[length(res) + 1L]] <<- path
      return(invisible(NULL))
    }
    if (remaining < 0) return(invisible(NULL))
    for (i in start:length(candidates)) {
      path <<- c(path, candidates[i])
      dfs(i, remaining - candidates[i])
      path <<- path[-length(path)]
    }
  }
  if (length(candidates) > 0) dfs(1L, target)
  res
}
got <- combination_sum(c(2, 3, 6, 7), 7)
stopifnot(length(got) == 2, identical(got[[1]], c(2, 2, 3)), identical(got[[2]], 7))
got2 <- combination_sum(c(2, 3, 5), 8)
stopifnot(length(got2) == 3, identical(got2[[3]], c(3, 5)))
cat("PASS\\n")
''',
"zig": '''const std = @import("std");
fn combinationSum(cands: []const i32, target: i32, alloc: std.mem.Allocator, res: *std.ArrayList(std.ArrayList(i32))) void {
    const D = struct {
        fn dfs(cs: []const i32, start: usize, remaining: i32, path: *std.ArrayList(i32), out: *std.ArrayList(std.ArrayList(i32))) void {
            if (remaining == 0) {
                var cp = std.ArrayList(i32).init(out.allocator);
                cp.appendSlice(path.items) catch unreachable;
                out.append(cp) catch unreachable;
                return;
            }
            if (remaining < 0) return;
            for (start..cs.len) |i| {
                path.append(cs[i]) catch unreachable;
                dfs(cs, i, remaining - cs[i], path, out);
                _ = path.pop();
            }
        }
    };
    var path = std.ArrayList(i32).init(alloc);
    D.dfs(cands, 0, target, &path, res);
}
pub fn main() !void {
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();
    const alloc = arena.allocator();
    var res = std.ArrayList(std.ArrayList(i32)).init(std.heap.page_allocator);
    defer res.deinit();
    combinationSum(&[_]i32{ 2, 3, 6, 7 }, 7, alloc, &res);
    if (res.items.len != 2) return error.TestFailed;
    if (res.items[0].items.len != 3 or res.items[0].items[0] != 2 or res.items[0].items[2] != 3) return error.TestFailed;
    if (res.items[1].items.len != 1 or res.items[1].items[0] != 7) return error.TestFailed;
    res.clearRetainingCapacity();
    combinationSum(&[_]i32{ 2, 3, 5 }, 8, alloc, &res);
    if (res.items.len != 3) return error.TestFailed;
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''List<List<int>> combinationSum(List<int> candidates, int target) {
  final res = <List<int>>[];
  final path = <int>[];
  void dfs(int start, int remaining) {
    if (remaining == 0) {
      res.add(List<int>.from(path));
      return;
    }
    if (remaining < 0) return;
    for (var i = start; i < candidates.length; i++) {
      path.add(candidates[i]);
      dfs(i, remaining - candidates[i]);
      path.removeLast();
    }
  }
  dfs(0, target);
  return res;
}
void main() {
  final got = combinationSum([2, 3, 6, 7], 7);
  if (got.length != 2) throw StateError('cnt');
  if (got[0].toString() != '[2, 2, 3]' || got[1].toString() != '[7]') throw StateError('a');
  final got2 = combinationSum([2, 3, 5], 8);
  if (got2.length != 3) throw StateError('c2');
  print('PASS');
}
''',
}

A131 = {
"rust": '''fn is_pal(s: &[char]) -> bool {
    let (mut i, mut j) = (0usize, s.len() - 1);
    while i < j {
        if s[i] != s[j] { return false; }
        i += 1;
        j -= 1;
    }
    true
}
fn partition(s: &str) -> Vec<Vec<String>> {
    let chars: Vec<char> = s.chars().collect();
    let mut res = Vec::new();
    let mut path: Vec<String> = Vec::new();
    fn dfs(chars: &[char], start: usize, path: &mut Vec<String>, res: &mut Vec<Vec<String>>) {
        if start == chars.len() { res.push(path.clone()); return; }
        for end in start + 1..=chars.len() {
            if is_pal(&chars[start..end]) {
                path.push(chars[start..end].iter().collect());
                dfs(chars, end, path, res);
                path.pop();
            }
        }
    }
    dfs(&chars, 0, &mut path, &mut res);
    res
}
fn main() {
    let got = partition("aab");
    let want = vec![vec!["a".to_string(), "a".to_string(), "b".to_string()], vec!["aa".to_string(), "b".to_string()]];
    assert_eq!(got, want);
    println!("PASS");
}
''',
"lua": '''local function is_pal(s)
    local i, j = 1, #s
    while i < j do
        if s:sub(i, i) ~= s:sub(j, j) then return false end
        i = i + 1
        j = j - 1
    end
    return true
end
local function partition(s)
    local res = {}
    local path = {}
    local n = #s
    local function dfs(start)
        if start > n then
            local cp = {table.unpack(path)}
            res[#res + 1] = cp
            return
        end
        for e = start, n do
            local sub = s:sub(start, e)
            if is_pal(sub) then
                path[#path + 1] = sub
                dfs(e + 1)
                path[#path] = nil
            end
        end
    end
    dfs(1)
    return res
end
local got = partition("aab")
assert(#got == 2)
assert(got[1][1] == "a" and got[1][2] == "a" and got[1][3] == "b")
assert(got[2][1] == "aa" and got[2][2] == "b")
print("PASS")
''',
"c": '''#include <stdio.h>
#include <string.h>
static char res[256][32][32];
static int res_lens[256], res_n;
static char path[32][32];
static int path_n;
static int is_pal(const char *s, int l, int r) {
    while (l < r) {
        if (s[l] != s[r]) return 0;
        l++; r--;
    }
    return 1;
}
static void dfs(const char *s, int n, int start) {
    if (start == n) {
        for (int i = 0; i < path_n; i++) strcpy(res[res_n][i], path[i]);
        res_lens[res_n] = path_n;
        res_n++;
        return;
    }
    for (int e = start; e < n; e++) {
        if (is_pal(s, start, e)) {
            int len = e - start + 1;
            strncpy(path[path_n], s + start, len);
            path[path_n][len] = '\\0';
            path_n++;
            dfs(s, n, e + 1);
            path_n--;
        }
    }
}
static int partition(const char *s) {
    res_n = 0; path_n = 0;
    dfs(s, (int)strlen(s), 0);
    return res_n;
}
int main(void) {
    int n = partition("aab");
    if (n != 2) { printf("FAIL cnt=%d\\n", n); return 1; }
    if (res_lens[0] != 3 || strcmp(res[0][0], "a") != 0 || strcmp(res[0][2], "b") != 0) { printf("FAIL a\\n"); return 1; }
    if (res_lens[1] != 2 || strcmp(res[1][0], "aa") != 0) { printf("FAIL b\\n"); return 1; }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''#include <cassert>
#include <iostream>
#include <string>
#include <vector>
static bool isPal(const std::string &s) {
    size_t i = 0, j = s.size() - 1;
    while (i < j) {
        if (s[i] != s[j]) return false;
        ++i; --j;
    }
    return true;
}
static std::vector<std::vector<std::string>> partition(const std::string &s) {
    std::vector<std::vector<std::string>> res;
    std::vector<std::string> path;
    std::function<void(size_t)> dfs = [&](size_t start) {
        if (start == s.size()) { res.push_back(path); return; }
        for (size_t e = start + 1; e <= s.size(); ++e) {
            auto sub = s.substr(start, e - start);
            if (isPal(sub)) {
                path.push_back(sub);
                dfs(e);
                path.pop_back();
            }
        }
    };
    dfs(0);
    return res;
}
int main() {
    assert((partition("aab") == std::vector<std::vector<std::string>>{{{{"a", "a", "b"}, {"aa", "b"}}}}));
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''is_pal <- function(s) {
  chars <- strsplit(s, "")[[1]]
  identical(chars, rev(chars))
}
partition <- function(s) {
  chars <- strsplit(s, "")[[1]]
  n <- length(chars)
  res <- list()
  path <- character(0)
  dfs <- function(start) {
    if (start > n) {
      res[[length(res) + 1L]] <<- path
      return(invisible(NULL))
    }
    for (e in start:n) {
      sub <- paste(chars[start:e], collapse = "")
      if (is_pal(sub)) {
        path <<- c(path, sub)
        dfs(e + 1L)
        path <<- path[-length(path)]
      }
    }
  }
  if (n > 0) dfs(1L) else res[[1L]] <- character(0)
  res
}
got <- partition("aab")
stopifnot(length(got) == 2)
stopifnot(identical(got[[1]], c("a", "a", "b")))
stopifnot(identical(got[[2]], c("aa", "b")))
cat("PASS\\n")
''',
"zig": '''const std = @import("std");
fn isPal(s: []const u8) bool {
    if (s.len == 0) return true;
    var i: usize = 0;
    var j: usize = s.len - 1;
    while (i < j) : ({
        i += 1;
        j -= 1;
    }) {
        if (s[i] != s[j]) return false;
    }
    return true;
}
fn partition(s: []const u8, alloc: std.mem.Allocator, res: *std.ArrayList(std.ArrayList([]const u8))) void {
    const D = struct {
        fn dfs(str: []const u8, start: usize, path: *std.ArrayList([]const u8), out: *std.ArrayList(std.ArrayList([]const u8)), a: std.mem.Allocator) void {
            if (start == str.len) {
                var cp = std.ArrayList([]const u8).init(out.allocator);
                cp.appendSlice(path.items) catch unreachable;
                out.append(cp) catch unreachable;
                return;
            }
            var e = start + 1;
            while (e <= str.len) : (e += 1) {
                const sub = str[start..e];
                if (isPal(sub)) {
                    path.append(a.dupe(u8, sub) catch unreachable) catch unreachable;
                    dfs(str, e, path, out, a);
                    _ = path.pop();
                }
            }
        }
    };
    var path = std.ArrayList([]const u8).init(alloc);
    D.dfs(s, 0, &path, res, alloc);
}
pub fn main() !void {
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();
    const alloc = arena.allocator();
    var res = std.ArrayList(std.ArrayList([]const u8)).init(std.heap.page_allocator);
    defer res.deinit();
    partition("aab", alloc, &res);
    if (res.items.len != 2) return error.TestFailed;
    if (res.items[0].items.len != 3 or !std.mem.eql(u8, res.items[0].items[0], "a")) return error.TestFailed;
    if (res.items[1].items.len != 2 or !std.mem.eql(u8, res.items[1].items[0], "aa")) return error.TestFailed;
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''bool isPal(String s) {
  var i = 0, j = s.length - 1;
  while (i < j) {
    if (s[i] != s[j]) return false;
    i++;
    j--;
  }
  return true;
}
List<List<String>> partition(String s) {
  final res = <List<String>>[];
  final path = <String>[];
  void dfs(int start) {
    if (start == s.length) {
      res.add(List<String>.from(path));
      return;
    }
    for (var e = start + 1; e <= s.length; e++) {
      final sub = s.substring(start, e);
      if (isPal(sub)) {
        path.add(sub);
        dfs(e);
        path.removeLast();
      }
    }
  }
  dfs(0);
  return res;
}
void main() {
  final got = partition('aab');
  if (got.length != 2) throw StateError('cnt');
  if (got[0].toString() != '[a, a, b]' || got[1].toString() != '[aa, b]') throw StateError('p');
  print('PASS');
}
''',
}

# 37/51/79/93 的算法体较特殊，统一为函数体生成
A51 = {
"rust": '''fn solve_n_queens(n: usize) -> Vec<Vec<String>> {
    let mut res = Vec::new();
    let mut queens: Vec<(usize, usize)> = Vec::new(); // (row, col)
    fn ok2(queens: &[(usize, usize)], row: usize, col: usize) -> bool {
        for &(r, c) in queens {
            if c == col
                || r + c == row + col
                || (r as i32 - c as i32) == (row as i32 - col as i32)
            {
                return false;
            }
        }
        true
    }
    fn dfs(n: usize, row: usize, queens: &mut Vec<(usize, usize)>, res: &mut Vec<Vec<String>>) {
        if row == n {
            let mut board = Vec::new();
            for r in 0..n {
                let mut line = String::new();
                for c in 0..n {
                    if queens.iter().any(|&(qr, qc)| qr == r && qc == c) { line.push('Q'); } else { line.push('.'); }
                }
                board.push(line);
            }
            res.push(board);
            return;
        }
        for col in 0..n {
            if ok2(queens, row, col) {
                queens.push((row, col));
                dfs(n, row + 1, queens, res);
                queens.pop();
            }
        }
    }
    dfs(n, 0, &mut queens, &mut res);
    res
}
fn main() {
    let got = solve_n_queens(4);
    assert_eq!(got.len(), 2);
    assert_eq!(got[0], vec![".Q..", "...Q", "Q...", "..Q."]);
    assert_eq!(solve_n_queens(1).len(), 1);
    println!("PASS");
}
''',
"lua": '''local function solve_n_queens(n)
    local res = {}
    local cols = {}
    local function ok(row, col)
        for r = 1, row - 1 do
            if cols[r] == col or math.abs(r - row) == math.abs(cols[r] - col) then return false end
        end
        return true
    end
    local function dfs(row)
        if row > n then
            local board = {}
            for r = 1, n do
                local line = {}
                for c = 1, n do
                    if cols[r] == c then line[#line + 1] = "Q" else line[#line + 1] = "." end
                end
                board[#board + 1] = table.concat(line)
            end
            res[#res + 1] = board
            return
        end
        for col = 1, n do
            if ok(row, col) then
                cols[row] = col
                dfs(row + 1)
                cols[row] = nil
            end
        end
    end
    dfs(1)
    return res
end
local got = solve_n_queens(4)
assert(#got == 2)
assert(got[1][1] == ".Q.." and got[1][4] == "..Q.")
assert(got[2][1] == "..Q." and got[2][4] == ".Q..")
assert(#solve_n_queens(1) == 1)
print("PASS")
''',
"c": '''#include <stdio.h>
#include <stdlib.h>
#include <string.h>
static int cols_g[16], n_g;
static char boards[256][16][17];
static int boards_n;
static int ok(int row, int col) {
    for (int r = 0; r < row; r++) {
        if (cols_g[r] == col || abs(r - row) == abs(cols_g[r] - col)) return 0;
    }
    return 1;
}
static void dfs(int row) {
    if (row == n_g) {
        for (int r = 0; r < n_g; r++) {
            for (int c = 0; c < n_g; c++) boards[boards_n][r][c] = (cols_g[r] == c) ? 'Q' : '.';
            boards[boards_n][r][n_g] = '\\0';
        }
        boards_n++;
        return;
    }
    for (int col = 0; col < n_g; col++) {
        if (ok(row, col)) {
            cols_g[row] = col;
            dfs(row + 1);
        }
    }
}
static int solve_n_queens(int n) {
    n_g = n; boards_n = 0;
    dfs(0);
    return boards_n;
}
int main(void) {
    int n = solve_n_queens(4);
    if (n != 2) { printf("FAIL cnt=%d\\n", n); return 1; }
    if (strcmp(boards[0][0], ".Q..") != 0 || strcmp(boards[0][3], "..Q.") != 0) { printf("FAIL b1\\n"); return 1; }
    if (strcmp(boards[1][0], "..Q.") != 0) { printf("FAIL b2\\n"); return 1; }
    if (solve_n_queens(1) != 1) { printf("FAIL 2\\n"); return 1; }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''#include <cassert>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>
static std::vector<std::vector<std::string>> solveNQueens(int n) {
    std::vector<std::vector<std::string>> res;
    std::vector<int> cols(n, -1);
    std::function<void(int)> dfs = [&](int row) {
        if (row == n) {
            std::vector<std::string> board;
            for (int r = 0; r < n; ++r) {
                std::string line(n, '.');
                line[cols[r]] = 'Q';
                board.push_back(line);
            }
            res.push_back(board);
            return;
        }
        for (int col = 0; col < n; ++col) {
            bool valid = true;
            for (int r = 0; r < row; ++r) {
                if (cols[r] == col || std::abs(r - row) == std::abs(cols[r] - col)) { valid = false; break; }
            }
            if (valid) {
                cols[row] = col;
                dfs(row + 1);
                cols[row] = -1;
            }
        }
    };
    dfs(0);
    return res;
}
int main() {
    auto got = solveNQueens(4);
    assert(got.size() == 2);
    assert((got[0] == std::vector<std::string>{".Q..", "...Q", "Q...", "..Q."}));
    assert(solveNQueens(1).size() == 1);
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''solve_n_queens <- function(n) {
  res <- list()
  cols <- rep(-1L, n)
  dfs <- function(row) {
    if (row > n) {
      board <- character(0)
      for (r in seq_len(n)) {
        line <- strrep(".", n)
        chars <- strsplit(line, "")[[1]]
        chars[cols[r]] <- "Q"
        board <- c(board, paste(chars, collapse = ""))
      }
      res[[length(res) + 1L]] <<- board
      return(invisible(NULL))
    }
    for (col in seq_len(n)) {
      valid <- TRUE
      for (r in seq_len(row - 1L)) {
        if (cols[r] == col || abs(r - row) == abs(cols[r] - col)) { valid <- FALSE; break }
      }
      if (valid) {
        cols[row] <<- col
        dfs(row + 1L)
      }
    }
  }
  dfs(1L)
  res
}
got <- solve_n_queens(4)
stopifnot(length(got) == 2)
stopifnot(identical(got[[1]], c(".Q..", "...Q", "Q...", "..Q.")))
stopifnot(length(solve_n_queens(1)) == 1)
cat("PASS\\n")
''',
"zig": '''const std = @import("std");
fn solveNQueens(n: usize, alloc: std.mem.Allocator, res: *std.ArrayList(std.ArrayList([]const u8))) void {
    const D = struct {
        fn dfs(nn: usize, row: usize, cols: []i32, out: *std.ArrayList(std.ArrayList([]const u8)), a: std.mem.Allocator) void {
            if (row == nn) {
                var board = std.ArrayList([]const u8).init(out.allocator);
                for (0..nn) |r| {
                    var buf = a.alloc(u8, nn) catch unreachable;
                    for (0..nn) |c| buf[c] = if (cols[r] == @as(i32, @intCast(c))) 'Q' else '.';
                    board.append(buf) catch unreachable;
                }
                out.append(board) catch unreachable;
                return;
            }
            for (0..nn) |col| {
                var valid = true;
                for (0..row) |r| {
                    if (cols[r] == @as(i32, @intCast(col))) { valid = false; break; }
                    const dr = @as(i32, @intCast(r)) - @as(i32, @intCast(row));
                    const dc = cols[r] - @as(i32, @intCast(col));
                    if (dr * dr == dc * dc) { valid = false; break; }
                }
                if (valid) {
                    cols[row] = @intCast(col);
                    dfs(nn, row + 1, cols, out, a);
                }
            }
        }
    };
    const cols = alloc.alloc(i32, n) catch unreachable;
    @memset(cols, -1);
    D.dfs(n, 0, cols, res, alloc);
}
pub fn main() !void {
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();
    const alloc = arena.allocator();
    var res = std.ArrayList(std.ArrayList([]const u8)).init(std.heap.page_allocator);
    defer res.deinit();
    solveNQueens(4, alloc, &res);
    if (res.items.len != 2) return error.TestFailed;
    if (!std.mem.eql(u8, res.items[0].items[0], ".Q..")) return error.TestFailed;
    if (!std.mem.eql(u8, res.items[0].items[3], "..Q.")) return error.TestFailed;
    res.clearRetainingCapacity();
    solveNQueens(1, alloc, &res);
    if (res.items.len != 1) return error.TestFailed;
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''List<List<String>> solveNQueens(int n) {
  final res = <List<String>>[];
  final cols = List<int>.filled(n, -1);
  void dfs(int row) {
    if (row == n) {
      final board = <String>[];
      for (var r = 0; r < n; r++) {
        final line = List<String>.generate(n, (c) => cols[r] == c ? 'Q' : '.');
        board.add(line.join());
      }
      res.add(board);
      return;
    }
    for (var col = 0; col < n; col++) {
      var valid = true;
      for (var r = 0; r < row; r++) {
        if (cols[r] == col || (r - row).abs() == (cols[r] - col).abs()) {
          valid = false;
          break;
        }
      }
      if (valid) {
        cols[row] = col;
        dfs(row + 1);
        cols[row] = -1;
      }
    }
  }
  dfs(0);
  return res;
}
void main() {
  final got = solveNQueens(4);
  if (got.length != 2) throw StateError('cnt');
  if (got[0][0] != '.Q..' || got[0][3] != '..Q.' || got[1][0] != '..Q.') throw StateError('b');
  if (solveNQueens(1).length != 1) throw StateError('c2');
  print('PASS');
}
''',
}

A79 = {
"rust": '''fn exist(board: Vec<Vec<char>>, word: String) -> bool {
    let mut board = board;
    let w: Vec<char> = word.chars().collect();
    fn dfs(board: &mut Vec<Vec<char>>, w: &[char], i: usize, j: usize, k: usize) -> bool {
        if k == w.len() { return true; }
        if i >= board.len() || j >= board[0].len() { return false; }
        if board[i][j] != w[k] { return false; }
        let saved = board[i][j];
        board[i][j] = '#';
        let found = dfs(board, w, i + 1, j, k + 1)
            || (i > 0 && dfs(board, w, i - 1, j, k + 1))
            || dfs(board, w, i, j + 1, k + 1)
            || (j > 0 && dfs(board, w, i, j - 1, k + 1));
        board[i][j] = saved;
        found
    }
    for i in 0..board.len() {
        for j in 0..board[0].len() {
            if dfs(&mut board, &w, i, j, 0) { return true; }
        }
    }
    false
}
fn main() {
    let b = vec![vec!['A','B','C','E'], vec!['S','F','C','S'], vec!['A','D','E','E']];
    assert!(exist(b.clone(), "ABCCED".to_string()));
    assert!(exist(b.clone(), "SEE".to_string()));
    assert!(!exist(b, "ABCB".to_string()));
    println!("PASS");
}
''',
"lua": '''local function exist(board, word)
    local rows, cols = #board, #board[1]
    local w = {}
    word:gsub(".", function(c) w[#w + 1] = c end)
    local function dfs(i, j, k)
        if k > #w then return true end
        if i < 1 or i > rows or j < 1 or j > cols then return false end
        if board[i][j] ~= w[k] then return false end
        local saved = board[i][j]
        board[i][j] = "#"
        local found = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i, j - 1, k + 1)
        board[i][j] = saved
        return found
    end
    for i = 1, rows do
        for j = 1, cols do
            if dfs(i, j, 1) then return true end
        end
    end
    return false
end
local b = {{{{"A","B","C","E"}}, {{"S","F","C","S"}}, {{"A","D","E","E"}}}}
assert(exist(b, "ABCCED") == true)
assert(exist(b, "SEE") == true)
assert(exist(b, "ABCB") == false)
print("PASS")
''',
"c": '''#include <stdio.h>
#include <string.h>
static char board_g[8][8];
static int rows_g, cols_g;
static const char *w_g;
static int dfs(int i, int j, int k) {
    if (w_g[k] == '\\0') return 1;
    if (i < 0 || i >= rows_g || j < 0 || j >= cols_g) return 0;
    if (board_g[i][j] != w_g[k]) return 0;
    char saved = board_g[i][j];
    board_g[i][j] = '#';
    int found = dfs(i + 1, j, k + 1) || dfs(i - 1, j, k + 1) || dfs(i, j + 1, k + 1) || dfs(i, j - 1, k + 1);
    board_g[i][j] = saved;
    return found;
}
static int exist(char board[][8], int rows, int cols, const char *word) {
    rows_g = rows; cols_g = cols; w_g = word;
    for (int i = 0; i < rows; i++)
        for (int j = 0; j < cols; j++)
            board_g[i][j] = board[i][j];
    for (int i = 0; i < rows; i++)
        for (int j = 0; j < cols; j++)
            if (dfs(i, j, 0)) return 1;
    return 0;
}
int main(void) {
    char b[3][8] = {{{{'A','B','C','E'}}, {{'S','F','C','S'}}, {{'A','D','E','E'}}}};
    if (!exist(b, 3, 4, "ABCCED")) { printf("FAIL 1\\n"); return 1; }
    if (!exist(b, 3, 4, "SEE")) { printf("FAIL 2\\n"); return 1; }
    if (exist(b, 3, 4, "ABCB")) { printf("FAIL 3\\n"); return 1; }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''#include <cassert>
#include <iostream>
#include <string>
#include <vector>
static bool exist(std::vector<std::vector<char>> board, const std::string &word) {
    int rows = static_cast<int>(board.size()), cols = static_cast<int>(board[0].size());
    std::function<bool(int, int, int)> dfs = [&](int i, int j, int k) -> bool {
        if (k == static_cast<int>(word.size())) return true;
        if (i < 0 || i >= rows || j < 0 || j >= cols || board[i][j] != word[k]) return false;
        char saved = board[i][j];
        board[i][j] = '#';
        bool found = dfs(i + 1, j, k + 1) || dfs(i - 1, j, k + 1) || dfs(i, j + 1, k + 1) || dfs(i, j - 1, k + 1);
        board[i][j] = saved;
        return found;
    };
    for (int i = 0; i < rows; ++i)
        for (int j = 0; j < cols; ++j)
            if (dfs(i, j, 0)) return true;
    return false;
}
int main() {
    std::vector<std::vector<char>> b = {{{{'A','B','C','E'}}, {{'S','F','C','S'}}, {{'A','D','E','E'}}}};
    assert(exist(b, "ABCCED"));
    assert(exist(b, "SEE"));
    assert(!exist(b, "ABCB"));
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''exist <- function(board, word) {
  rows <- length(board)
  cols <- length(board[[1]])
  w <- strsplit(word, "")[[1]]
  dfs <- function(i, j, k) {
    if (k > length(w)) return(TRUE)
    if (i < 1 || i > rows || j < 1 || j > cols) return(FALSE)
    if (env_board$cells[[i]][j] != w[k]) return(FALSE)
    saved <- env_board$cells[[i]][j]
    env_board$cells[[i]][j] <<- "#"
    found <- dfs(i + 1, j, k + 1) || dfs(i - 1, j, k + 1) || dfs(i, j + 1, k + 1) || dfs(i, j - 1, k + 1)
    env_board$cells[[i]][j] <<- saved
    found
  }
  env_board <- new.env(parent = emptyenv())
  env_board$cells <- lapply(board, function(r) r)
  for (i in seq_len(rows)) {
    for (j in seq_len(cols)) {
      if (dfs(i, j, 1)) return(TRUE)
    }
  }
  FALSE
}
b <- list(c("A","B","C","E"), c("S","F","C","S"), c("A","D","E","E"))
stopifnot(exist(b, "ABCCED"))
stopifnot(exist(b, "SEE"))
stopifnot(!exist(b, "ABCB"))
cat("PASS\\n")
''',
"zig": '''const std = @import("std");
fn exist(board_in: []const []u8, word: []const u8) bool {
    const board = board_in;
    const rows = board.len;
    const cols = board[0].len;
    const D = struct {
        fn dfs(b: []const []u8, w: []const u8, i: isize, j: isize, k: usize) bool {
            if (k == w.len) return true;
            if (i < 0 or i >= @as(isize, @intCast(b.len)) or j < 0 or j >= @as(isize, @intCast(b[0].len))) return false;
            const ui: usize = @intCast(i);
            const uj: usize = @intCast(j);
            if (b[ui][uj] != w[k]) return false;
            const saved = b[ui][uj];
            b[ui][uj] = '#';
            const found = dfs(b, w, i + 1, j, k + 1) or dfs(b, w, i - 1, j, k + 1) or dfs(b, w, i, j + 1, k + 1) or dfs(b, w, i, j - 1, k + 1);
            b[ui][uj] = saved;
            return found;
        }
    };
    for (0..rows) |i| {
        for (0..cols) |j| {
            if (D.dfs(board, word, @intCast(i), @intCast(j), 0)) return true;
        }
    }
    return false;
}
pub fn main() !void {
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();
    const alloc = arena.allocator();
    const b0 = alloc.dupe(u8, "ABCE") catch unreachable;
    const b1 = alloc.dupe(u8, "SFCS") catch unreachable;
    const b2 = alloc.dupe(u8, "ADEE") catch unreachable;
    const board = [_][]u8{ b0, b1, b2 };
    if (!exist(&board, "ABCCED")) return error.TestFailed;
    if (!exist(&board, "SEE")) return error.TestFailed;
    if (exist(&board, "ABCB")) return error.TestFailed;
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''bool exist(List<List<String>> board, String word) {
  final rows = board.length, cols = board[0].length;
  final w = word.split('');
  bool dfs(int i, int j, int k) {
    if (k == w.length) return true;
    if (i < 0 || i >= rows || j < 0 || j >= cols || board[i][j] != w[k]) return false;
    final saved = board[i][j];
    board[i][j] = '#';
    final found = dfs(i + 1, j, k + 1) || dfs(i - 1, j, k + 1) || dfs(i, j + 1, k + 1) || dfs(i, j - 1, k + 1);
    board[i][j] = saved;
    return found;
  }
  for (var i = 0; i < rows; i++) {
    for (var j = 0; j < cols; j++) {
      if (dfs(i, j, 0)) return true;
    }
  }
  return false;
}
void main() {
  final b = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E'],
  ];
  if (!exist(b, 'ABCCED')) throw StateError('c1');
  if (!exist(b, 'SEE')) throw StateError('c2');
  if (exist(b, 'ABCB')) throw StateError('c3');
  print('PASS');
}
''',
}

A93 = {
"rust": '''fn valid_seg(s: &str) -> bool {
    if s.len() == 0 || s.len() > 3 { return false; }
    if s.len() > 1 && s.starts_with('0') { return false; }
    s.parse::<i32>().map(|v| v <= 255).unwrap_or(false)
}
fn restore_ip_addresses(s: String) -> Vec<String> {
    let chars: Vec<char> = s.chars().collect();
    let n = chars.len();
    let mut res = Vec::new();
    if n < 4 || n > 12 { return res; }
    for a in 1..=3 {
        for b in 1..=3 {
            for c in 1..=3 {
                let d = n - a - b - c;
                if d < 1 || d > 3 { continue; }
                let s1: String = chars[0..a].iter().collect();
                let s2: String = chars[a..a + b].iter().collect();
                let s3: String = chars[a + b..a + b + c].iter().collect();
                let s4: String = chars[a + b + c..].iter().collect();
                if valid_seg(&s1) && valid_seg(&s2) && valid_seg(&s3) && valid_seg(&s4) {
                    res.push(format!("{}.{}.{}.{}", s1, s2, s3, s4));
                }
            }
        }
    }
    res
}
fn main() {
    let got = restore_ip_addresses("25525511135".to_string());
    assert_eq!(got, vec!["255.255.11.135", "255.255.111.35"]);
    assert_eq!(restore_ip_addresses("0000".to_string()), vec!["0.0.0.0"]);
    assert!(restore_ip_addresses("abc".to_string()).is_empty());
    println!("PASS");
}
''',
"lua": '''local function valid_seg(s)
    if #s == 0 or #s > 3 then return false end
    if #s > 1 and s:sub(1, 1) == "0" then return false end
    return tonumber(s) <= 255
end
local function restore_ip_addresses(s)
    local res = {}
    local n = #s
    if n < 4 or n > 12 then return res end
    for a = 1, 3 do
        for b = 1, 3 do
            for c = 1, 3 do
                local d = n - a - b - c
                if d >= 1 and d <= 3 then
                    local s1 = s:sub(1, a)
                    local s2 = s:sub(a + 1, a + b)
                    local s3 = s:sub(a + b + 1, a + b + c)
                    local s4 = s:sub(a + b + c + 1)
                    if valid_seg(s1) and valid_seg(s2) and valid_seg(s3) and valid_seg(s4) then
                        res[#res + 1] = s1 .. "." .. s2 .. "." .. s3 .. "." .. s4
                    end
                end
            end
        end
    end
    return res
end
local got = restore_ip_addresses("25525511135")
assert(#got == 2 and got[1] == "255.255.11.135" and got[2] == "255.255.111.35")
local g2 = restore_ip_addresses("0000")
assert(#g2 == 1 and g2[1] == "0.0.0.0")
assert(#restore_ip_addresses("abc") == 0)
print("PASS")
''',
"c": '''#include <stdio.h>
#include <string.h>
static int valid_seg(const char *s, int len) {
    if (len == 0 || len > 3) return 0;
    if (len > 1 && s[0] == '0') return 0;
    int v = 0;
    for (int i = 0; i < len; i++) v = v * 10 + (s[i] - '0');
    return v <= 255;
}
static int restore_ip_addresses(const char *s, char out[][16]) {
    int res = 0;
    int n = (int)strlen(s);
    if (n < 4 || n > 12) return 0;
    for (int a = 1; a <= 3; a++)
        for (int b = 1; b <= 3; b++)
            for (int c = 1; c <= 3; c++) {
                int d = n - a - b - c;
                if (d < 1 || d > 3) continue;
                if (valid_seg(s, a) && valid_seg(s + a, b) && valid_seg(s + a + b, c) && valid_seg(s + a + b + c, d)) {
                    snprintf(out[res], 16, "%.*s.%.*s.%.*s.%.*s", a, s, b, s + a, c, s + a + b, d, s + a + b + c);
                    res++;
                }
            }
    return res;
}
int main(void) {
    char out[64][16];
    int n = restore_ip_addresses("25525511135", out);
    if (n != 2) { printf("FAIL cnt=%d\\n", n); return 1; }
    if (strcmp(out[0], "255.255.11.135") != 0 || strcmp(out[1], "255.255.111.35") != 0) { printf("FAIL ips\\n"); return 1; }
    n = restore_ip_addresses("0000", out);
    if (n != 1 || strcmp(out[0], "0.0.0.0") != 0) { printf("FAIL 2\\n"); return 1; }
    if (restore_ip_addresses("abc", out) != 0) { printf("FAIL 3\\n"); return 1; }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''#include <cassert>
#include <iostream>
#include <string>
#include <vector>
static bool validSeg(const std::string &s) {
    if (s.empty() || s.size() > 3) return false;
    if (s.size() > 1 && s[0] == '0') return false;
    return std::stoi(s) <= 255;
}
static std::vector<std::string> restoreIpAddresses(const std::string &s) {
    std::vector<std::string> res;
    int n = static_cast<int>(s.size());
    if (n < 4 || n > 12) return res;
    for (int a = 1; a <= 3; ++a)
        for (int b = 1; b <= 3; ++b)
            for (int c = 1; c <= 3; ++c) {
                int d = n - a - b - c;
                if (d < 1 || d > 3) continue;
                auto s1 = s.substr(0, a), s2 = s.substr(a, b), s3 = s.substr(a + b, c), s4 = s.substr(a + b + c);
                if (validSeg(s1) && validSeg(s2) && validSeg(s3) && validSeg(s4)) {
                    res.push_back(s1 + "." + s2 + "." + s3 + "." + s4);
                }
            }
    return res;
}
int main() {
    assert((restoreIpAddresses("25525511135") == std::vector<std::string>{"255.255.11.135", "255.255.111.35"}));
    assert((restoreIpAddresses("0000") == std::vector<std::string>{"0.0.0.0"}));
    assert(restoreIpAddresses("abc").empty());
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''valid_seg <- function(s) {
  if (nchar(s) == 0 || nchar(s) > 3) return(FALSE)
  if (nchar(s) > 1 && substr(s, 1, 1) == "0") return(FALSE)
  as.integer(s) <= 255
}
restore_ip_addresses <- function(s) {
  res <- character(0)
  n <- nchar(s)
  if (n < 4 || n > 12) return(res)
  for (a in 1:3) for (b in 1:3) for (c in 1:3) {
    d <- n - a - b - c
    if (d >= 1 && d <= 3) {
      s1 <- substr(s, 1, a)
      s2 <- substr(s, a + 1, a + b)
      s3 <- substr(s, a + b + 1, a + b + c)
      s4 <- substr(s, a + b + c + 1, n)
      if (valid_seg(s1) && valid_seg(s2) && valid_seg(s3) && valid_seg(s4)) {
        res <- c(res, paste(s1, s2, s3, s4, sep = "."))
      }
    }
  }
  res
}
got <- restore_ip_addresses("25525511135")
stopifnot(identical(got, c("255.255.11.135", "255.255.111.35")))
stopifnot(identical(restore_ip_addresses("0000"), "0.0.0.0"))
stopifnot(length(restore_ip_addresses("abc")) == 0)
cat("PASS\\n")
''',
"zig": '''const std = @import("std");
fn validSeg(s: []const u8) bool {
    if (s.len == 0 or s.len > 3) return false;
    if (s.len > 1 and s[0] == '0') return false;
    var v: i32 = 0;
    for (s) |c| v = v * 10 + @as(i32, c - '0');
    return v <= 255;
}
fn restoreIpAddresses(s: []const u8, out: *std.ArrayList([]const u8), alloc: std.mem.Allocator) void {
    const n = s.len;
    if (n < 4 or n > 12) return;
    var a: usize = 1;
    while (a <= 3) : (a += 1) {
        var b: usize = 1;
        while (b <= 3) : (b += 1) {
            var c: usize = 1;
            while (c <= 3) : (c += 1) {
                if (a + b + c >= n) continue;
                const d = n - a - b - c;
                if (d > 3) continue;
                const s1 = s[0..a];
                const s2 = s[a .. a + b];
                const s3 = s[a + b .. a + b + c];
                const s4 = s[a + b + c ..];
                if (validSeg(s1) and validSeg(s2) and validSeg(s3) and validSeg(s4)) {
                    var buf = std.ArrayList(u8).init(alloc);
                    buf.appendSlice(s1) catch unreachable;
                    buf.append('.') catch unreachable;
                    buf.appendSlice(s2) catch unreachable;
                    buf.append('.') catch unreachable;
                    buf.appendSlice(s3) catch unreachable;
                    buf.append('.') catch unreachable;
                    buf.appendSlice(s4) catch unreachable;
                    out.append(buf.toOwnedSlice() catch unreachable) catch unreachable;
                }
            }
        }
    }
}
pub fn main() !void {
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();
    const alloc = arena.allocator();
    var out = std.ArrayList([]const u8).init(std.heap.page_allocator);
    defer out.deinit();
    restoreIpAddresses("25525511135", &out, alloc);
    if (out.items.len != 2) return error.TestFailed;
    if (!std.mem.eql(u8, out.items[0], "255.255.11.135")) return error.TestFailed;
    if (!std.mem.eql(u8, out.items[1], "255.255.111.35")) return error.TestFailed;
    out.clearRetainingCapacity();
    restoreIpAddresses("0000", &out, alloc);
    if (out.items.len != 1 or !std.mem.eql(u8, out.items[0], "0.0.0.0")) return error.TestFailed;
    out.clearRetainingCapacity();
    restoreIpAddresses("abc", &out, alloc);
    if (out.items.len != 0) return error.TestFailed;
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''bool validSeg(String s) {
  if (s.isEmpty || s.length > 3) return false;
  if (s.length > 1 && s[0] == '0') return false;
  return int.parse(s) <= 255;
}
List<String> restoreIpAddresses(String s) {
  final res = <String>[];
  final n = s.length;
  if (n < 4 || n > 12) return res;
  for (var a = 1; a <= 3; a++) {
    for (var b = 1; b <= 3; b++) {
      for (var c = 1; c <= 3; c++) {
        final d = n - a - b - c;
        if (d < 1 || d > 3) continue;
        final s1 = s.substring(0, a);
        final s2 = s.substring(a, a + b);
        final s3 = s.substring(a + b, a + b + c);
        final s4 = s.substring(a + b + c);
        if (validSeg(s1) && validSeg(s2) && validSeg(s3) && validSeg(s4)) {
          res.add('$s1.$s2.$s3.$s4');
        }
      }
    }
  }
  return res;
}
void main() {
  final got = restoreIpAddresses('25525511135');
  if (got.length != 2 || got[0] != '255.255.11.135' || got[1] != '255.255.111.35') throw StateError('c1');
  final g2 = restoreIpAddresses('0000');
  if (g2.length != 1 || g2[0] != '0.0.0.0') throw StateError('c2');
  if (restoreIpAddresses('abc').isNotEmpty) throw StateError('c3');
  print('PASS');
}
''',
}

# 37 解数独与 51 类似（行约束+宫约束回填），31/93 已含。37 体量大，用标准回溯
A37 = {
"rust": '''fn solve_sudoku(board: &mut Vec<Vec<char>>) {
    fn valid(b: &Vec<Vec<char>>, r: usize, c: usize, ch: char) -> bool {
        for i in 0..9 {
            if b[r][i] == ch || b[i][c] == ch { return false; }
        }
        let (br, bc) = (r / 3 * 3, c / 3 * 3);
        for i in br..br + 3 {
            for j in bc..bc + 3 {
                if b[i][j] == ch { return false; }
            }
        }
        true
    }
    fn dfs(b: &mut Vec<Vec<char>>) -> bool {
        for r in 0..9 {
            for c in 0..9 {
                if b[r][c] == '.' {
                    for ch in '1'..='9' {
                        if valid(b, r, c, ch) {
                            b[r][c] = ch;
                            if dfs(b) { return true; }
                            b[r][c] = '.';
                        }
                    }
                    return false;
                }
            }
        }
        true
    }
    dfs(board);
}
fn main() {
    let mut board: Vec<Vec<char>> = vec![
        vec!['5','3','.','.','7','.','.','.','.'],
        vec!['6','.','.','1','9','5','.','.','.'],
        vec!['.','9','8','.','.','.','.','6','.'],
        vec!['8','.','.','.','6','.','.','.','3'],
        vec!['4','.','.','8','.','3','.','.','1'],
        vec!['7','.','.','.','2','.','.','.','6'],
        vec!['.','6','.','.','.','.','2','8','.'],
        vec!['.','.','.','4','1','9','.','.','5'],
        vec!['.','.','.','.','8','.','.','7','9'],
    ];
    solve_sudoku(&mut board);
    let solved = [
        "534678912", "672195348", "198342567",
        "859761423", "426853791", "713924856",
        "961537284", "287419635", "345286179",
    ];
    for r in 0..9 {
        let line: String = board[r].iter().collect();
        assert_eq!(line, solved[r]);
    }
    println!("PASS");
}
''',
"lua": '''local function solve_sudoku(board)
    local function valid(r, c, ch)
        for i = 1, 9 do
            if board[r][i] == ch or board[i][c] == ch then return false end
        end
        local br, bc = math.floor((r - 1) / 3) * 3 + 1, math.floor((c - 1) / 3) * 3 + 1
        for i = br, br + 2 do
            for j = bc, bc + 2 do
                if board[i][j] == ch then return false end
            end
        end
        return true
    end
    local function dfs()
        for r = 1, 9 do
            for c = 1, 9 do
                if board[r][c] == "." then
                    for n = 1, 9 do
                        local ch = tostring(n)
                        if valid(r, c, ch) then
                            board[r][c] = ch
                            if dfs() then return true end
                            board[r][c] = "."
                        end
                    end
                    return false
                end
            end
        end
        return true
    end
    dfs()
end
local board = {
    {"5","3",".",".","7",".",".",".","."},
    {"6",".",".","1","9","5",".",".","."},
    {".","9","8",".",".",".",".","6","."},
    {"8",".",".",".","6",".",".",".","3"},
    {"4",".",".","8",".","3",".",".","1"},
    {"7",".",".",".","2",".",".",".","6"},
    {".","6",".",".",".",".","2","8","."},
    {".",".",".","4","1","9",".",".","5"},
    {".",".",".",".","8",".",".","7","9"},
}
solve_sudoku(board)
local solved = {
    "534678912", "672195348", "198342567",
    "859761423", "426853791", "713924856",
    "961537284", "287419635", "345286179",
}
for r = 1, 9 do
    assert(table.concat(board[r]) == solved[r], "row " .. r)
end
print("PASS")
''',
"c": '''#include <stdio.h>
#include <string.h>
static int valid(char b[9][10], int r, int c, char ch) {
    for (int i = 0; i < 9; i++) {
        if (b[r][i] == ch || b[i][c] == ch) return 0;
    }
    int br = r / 3 * 3, bc = c / 3 * 3;
    for (int i = br; i < br + 3; i++)
        for (int j = bc; j < bc + 3; j++)
            if (b[i][j] == ch) return 0;
    return 1;
}
static int dfs(char b[9][10]) {
    for (int r = 0; r < 9; r++) {
        for (int c = 0; c < 9; c++) {
            if (b[r][c] == '.') {
                for (char ch = '1'; ch <= '9'; ch++) {
                    if (valid(b, r, c, ch)) {
                        b[r][c] = ch;
                        if (dfs(b)) return 1;
                        b[r][c] = '.';
                    }
                }
                return 0;
            }
        }
    }
    return 1;
}
static void solve_sudoku(char b[9][10]) { dfs(b); }
int main(void) {
    char board[9][10] = {
        "53..7....", "6..195...", ".98....6.",
        "8...6...3", "4..8.3..1", "7...2...6",
        ".6....28.", "...419..5", "....8..79",
    };
    solve_sudoku(board);
    const char *solved[] = {
        "534678912", "672195348", "198342567",
        "859761423", "426853791", "713924856",
        "961537284", "287419635", "345286179",
    };
    for (int r = 0; r < 9; r++) {
        if (strcmp(board[r], solved[r]) != 0) { printf("FAIL row %d\\n", r); return 1; }
    }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''#include <cassert>
#include <iostream>
#include <string>
#include <vector>
static void solveSudoku(std::vector<std::vector<char>> &board) {
    std::function<bool()> dfs = [&]() -> bool {
        for (int r = 0; r < 9; ++r) {
            for (int c = 0; c < 9; ++c) {
                if (board[r][c] == '.') {
                    for (char ch = '1'; ch <= '9'; ++ch) {
                        bool ok = true;
                        for (int i = 0; i < 9 && ok; ++i) {
                            if (board[r][i] == ch || board[i][c] == ch) ok = false;
                        }
                        int br = r / 3 * 3, bc = c / 3 * 3;
                        for (int i = br; i < br + 3 && ok; ++i)
                            for (int j = bc; j < bc + 3 && ok; ++j)
                                if (board[i][j] == ch) ok = false;
                        if (ok) {
                            board[r][c] = ch;
                            if (dfs()) return true;
                            board[r][c] = '.';
                        }
                    }
                    return false;
                }
            }
        }
        return true;
    };
    dfs();
}
int main() {
    std::vector<std::vector<char>> board = {
        {'5','3','.','.','7','.','.','.','.'},
        {'6','.','.','1','9','5','.','.','.'},
        {'.','9','8','.','.','.','.','6','.'},
        {'8','.','.','.','6','.','.','.','3'},
        {'4','.','.','8','.','3','.','.','1'},
        {'7','.','.','.','2','.','.','.','6'},
        {'.','6','.','.','.','.','2','8','.'},
        {'.','.','.','4','1','9','.','.','5'},
        {'.','.','.','.','8','.','.','7','9'},
    };
    solveSudoku(board);
    const char *solved[] = {
        "534678912", "672195348", "198342567",
        "859761423", "426853791", "713924856",
        "961537284", "287419635", "345286179",
    };
    for (int r = 0; r < 9; ++r) {
        std::string line(board[r].begin(), board[r].end());
        assert(line == solved[r]);
    }
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''solve_sudoku <- function(board) {
  valid <- function(r, c, ch) {
    for (i in 1:9) {
      if (env_b$cells[[r]][i] == ch || env_b$cells[[i]][c] == ch) return(FALSE)
    }
    br <- (floor((r - 1) / 3)) * 3 + 1
    bc <- (floor((c - 1) / 3)) * 3 + 1
    for (i in br:(br + 2)) for (j in bc:(bc + 2)) {
      if (env_b$cells[[i]][j] == ch) return(FALSE)
    }
    TRUE
  }
  env_b <- new.env(parent = emptyenv())
  env_b$cells <- lapply(board, function(r) r)
  dfs <- function() {
    for (r in 1:9) for (c in 1:9) {
      if (env_b$cells[[r]][c] == ".") {
        for (n in 1:9) {
          ch <- as.character(n)
          if (valid(r, c, ch)) {
            env_b$cells[[r]][c] <<- ch
            if (dfs()) return(TRUE)
            env_b$cells[[r]][c] <<- "."
          }
        }
        return(FALSE)
      }
    }
    TRUE
  }
  dfs()
  env_b$cells
}
board <- list(
  c("5","3",".",".","7",".",".",".","."),
  c("6",".",".","1","9","5",".",".","."),
  c(".","9","8",".",".",".",".","6","."),
  c("8",".",".",".","6",".",".",".","3"),
  c("4",".",".","8",".","3",".",".","1"),
  c("7",".",".",".","2",".",".",".","6"),
  c(".","6",".",".",".",".","2","8","."),
  c(".",".",".","4","1","9",".",".","5"),
  c(".",".",".",".","8",".",".","7","9")
)
solved <- solve_sudoku(board)
want <- c("534678912", "672195348", "198342567", "859761423", "426853791", "713924856", "961537284", "287419635", "345286179")
for (r in 1:9) {
  stopifnot(paste(solved[[r]], collapse = "") == want[r])
}
cat("PASS\\n")
''',
"zig": '''const std = @import("std");
fn validSudoku(b: *[9][9]u8, r: usize, c: usize, ch: u8) bool {
    for (0..9) |i| {
        if (b[r][i] == ch or b[i][c] == ch) return false;
    }
    const br = r / 3 * 3;
    const bc = c / 3 * 3;
    for (br..br + 3) |i| {
        for (bc..bc + 3) |j| {
            if (b[i][j] == ch) return false;
        }
    }
    return true;
}
fn dfsSudoku(b: *[9][9]u8) bool {
    for (0..9) |r| {
        for (0..9) |c| {
            if (b[r][c] == '.') {
                var ch: u8 = '1';
                while (ch <= '9') : (ch += 1) {
                    if (validSudoku(b, r, c, ch)) {
                        b[r][c] = ch;
                        if (dfsSudoku(b)) return true;
                        b[r][c] = '.';
                    }
                }
                return false;
            }
        }
    }
    return true;
}
pub fn main() !void {
    var board = [9][9]u8{
        .{ '5', '3', '.', '.', '7', '.', '.', '.', '.' },
        .{ '6', '.', '.', '1', '9', '5', '.', '.', '.' },
        .{ '.', '9', '8', '.', '.', '.', '.', '6', '.' },
        .{ '8', '.', '.', '.', '6', '.', '.', '.', '3' },
        .{ '4', '.', '.', '8', '.', '3', '.', '.', '1' },
        .{ '7', '.', '.', '.', '2', '.', '.', '.', '6' },
        .{ '.', '6', '.', '.', '.', '.', '2', '8', '.' },
        .{ '.', '.', '.', '4', '1', '9', '.', '.', '5' },
        .{ '.', '.', '.', '.', '8', '.', '.', '7', '9' },
    };
    _ = dfsSudoku(&board);
    const solved = [9][]const u8{
        "534678912", "672195348", "198342567",
        "859761423", "426853791", "713924856",
        "961537284", "287419635", "345286179",
    };
    for (solved, 0..) |row, r| {
        for (row, 0..) |ch, c| {
            if (board[r][c] != ch) return error.TestFailed;
        }
    }
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''void solveSudoku(List<List<String>> board) {
  bool valid(int r, int c, String ch) {
    for (var i = 0; i < 9; i++) {
      if (board[r][i] == ch || board[i][c] == ch) return false;
    }
    final br = r ~/ 3 * 3, bc = c ~/ 3 * 3;
    for (var i = br; i < br + 3; i++) {
      for (var j = bc; j < bc + 3; j++) {
        if (board[i][j] == ch) return false;
      }
    }
    return true;
  }
  bool dfs() {
    for (var r = 0; r < 9; r++) {
      for (var c = 0; c < 9; c++) {
        if (board[r][c] == '.') {
          for (var n = 1; n <= 9; n++) {
            final ch = n.toString();
            if (valid(r, c, ch)) {
              board[r][c] = ch;
              if (dfs()) return true;
              board[r][c] = '.';
            }
          }
          return false;
        }
      }
    }
    return true;
  }
  dfs();
}
void main() {
  final board = [
    ['5','3','.','.','7','.','.','.','.'],
    ['6','.','.','1','9','5','.','.','.'],
    ['.','9','8','.','.','.','.','6','.'],
    ['8','.','.','.','6','.','.','.','3'],
    ['4','.','.','8','.','3','.','.','1'],
    ['7','.','.','.','2','.','.','.','6'],
    ['.','6','.','.','.','.','2','8','.'],
    ['.','.','.','4','1','9','.','.','5'],
    ['.','.','.','.','8','.','.','7','9'],
  ];
  solveSudoku(board);
  final solved = [
    '534678912', '672195348', '198342567',
    '859761423', '426853791', '713924856',
    '961537284', '287419635', '345286179',
  ];
  for (var r = 0; r < 9; r++) {
    if (board[r].join() != solved[r]) throw StateError('row $r');
  }
  print('PASS');
}
''',
}

PROBS = [
    ("lc_131_分割回文串", A131, "LeetCode 131. 分割回文串"),
    ("lc_37_解数独", A37, "LeetCode 37. 解数独"),
    ("lc_39_组合总和", A39, "LeetCode 39. 组合总和"),
    ("lc_46_全排列", A46, "LeetCode 46. 全排列"),
    ("lc_47_全排列_ii", A47, "LeetCode 47. 全排列II"),
    ("lc_51_n_皇后", A51, "LeetCode 51. N皇后"),
    ("lc_77_组合", A77, "LeetCode 77. 组合"),
    ("lc_78_子集", A78, "LeetCode 78. 子集"),
    ("lc_79_单词搜索", A79, "LeetCode 79. 单词搜索"),
    ("lc_93_复原_ip_地址", A93, "LeetCode 93. 复原IP地址"),
]
count = 0
for prob, algo, title in PROBS:
    bid = B[prob.split("_")[1]]
    ts_dir = f"/Users/Wang/Code/github/web-x-blog/work/blog/courses/20.dsa/ts/backtrack/{prob}"
    sols = sorted(f[:-3] for f in os.listdir(ts_dir) if f.startswith("solution_") and f.endswith(".ts"))
    for lang in EXT:
        ext = EXT[lang]
        for sol in sols:
            n = sol.replace("solution_", "").split("_")[0]
            head = head_comment(lang, bid, f"{title} — {LANGNAME[lang]} 版（方案{n}）")
            body = algo[lang].replace("{H}", "").replace("{{", "{").replace("}}", "}")
            emit(lang, f"backtrack/{prob}/{sol}.{ext}", head + "\n" + body)
            count += 1
print(f"emitted {count} files")
