#!/usr/bin/env python3
# gen_notes1.py — notes 第一批：排序笔记族 × 7语言
# 冒泡/快速/插入/归并/选择/侏儒/计数/基数/桶/希尔/堆排序 — 各语言模板化
import sys, os; sys.path.insert(0, "/Users/Wang/Code/github/web-x-blog/work/target/21.dsa/_tools")
from langlib import emit, head_comment, EXT

LANGNAME = {"rust": "Rust", "lua": "Lua", "c": "C", "cpp": "C++", "r": "R", "zig": "Zig", "dart": "Dart"}

# 每种排序的 7 语言实现模板（funcname, 语言体）—— 通用「值数组进出 + sorted 断言」模式
BUBBLE = {
"rust":'''fn gnome_sort_bubble(nums: Vec<i32>) -> Vec<i32> {
    let mut v = nums;
    let n = v.len();
    for i in 0..n {
        for j in 0..n - 1 - i {
            if v[j] > v[j + 1] { v.swap(j, j + 1); }
        }
    }
    v
}
fn main() {
    assert_eq!(gnome_sort_bubble(vec![5,4,3,2,1]), vec![1,2,3,4,5]);
    assert_eq!(gnome_sort_bubble(vec![3,1,2]), vec![1,2,3]);
    assert_eq!(gnome_sort_bubble(vec![]), Vec::<i32>::new());
    println!("PASS"); }''',
"lua":'''local function gnome_sort_bubble(nums)
    local v = {table.unpack(nums)}
    local n = #v
    for i = 1, n do
        for j = 1, n - i do
            if v[j] > v[j + 1] then v[j], v[j + 1] = v[j + 1], v[j] end
        end
    end
    return v
end
assert(table.concat(gnome_sort_bubble({5,4,3,2,1}), ",") == "1,2,3,4,5")
assert(table.concat(gnome_sort_bubble({3,1,2}), ",") == "1,2,3")
assert(#gnome_sort_bubble({}) == 0)
print("PASS")''',
"c":'''#include <stdio.h>
static void gnome_sort_bubble(int v[], int n) {
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n - 1 - i; j++)
            if (v[j] > v[j + 1]) { int t = v[j]; v[j] = v[j + 1]; v[j + 1] = t; }
}
static int check(const int *v, int n, const int *w) {
    for (int i = 0; i < n; i++) if (v[i] != w[i]) return 0;
    return 1;
}
int main(void) {
    int v1[] = {5,4,3,2,1};
    gnome_sort_bubble(v1, 5);
    int w1[] = {1,2,3,4,5};
    if (!check(v1, 5, w1)) { printf("FAIL 1\\n"); return 1; }
    int v2[] = {3,1,2};
    gnome_sort_bubble(v2, 3);
    int w2[] = {1,2,3};
    if (!check(v2, 3, w2)) { printf("FAIL 2\\n"); return 1; }
    printf("PASS\\n"); return 0; }''',
"cpp":'''#include <cassert>
#include <iostream>
#include <vector>
static std::vector<int> gnomeSortBubble(std::vector<int> v) {
    for (size_t i = 0; i < v.size(); ++i)
        for (size_t j = 0; j + 1 < v.size() - i; ++j)
            if (v[j] > v[j + 1]) std::swap(v[j], v[j + 1]);
    return v;
}
int main() {
    assert((gnomeSortBubble({5,4,3,2,1}) == std::vector<int>{1,2,3,4,5}));
    assert((gnomeSortBubble({3,1,2}) == std::vector<int>{1,2,3}));
    assert(gnomeSortBubble({}).empty());
    std::cout << "PASS" << std::endl; }''',
"r":'''gnome_sort_bubble <- function(nums) {
  v <- nums
  n <- length(v)
  if (n >= 2) {
    for (i in seq_len(n - 1)) {
      for (j in 1:(n - i)) {
        if (v[j] > v[j + 1]) { t <- v[j]; v[j] <- v[j + 1]; v[j + 1] <- t }
      }
    }
  }
  v
}
stopifnot(identical(as.integer(gnome_sort_bubble(c(5, 4, 3, 2, 1))), 1:5))
stopifnot(identical(as.integer(gnome_sort_bubble(c(3, 1, 2))), c(1L, 2L, 3L)))
stopifnot(length(gnome_sort_bubble(integer(0))) == 0)
cat("PASS\\n")''',
"zig":'''const std = @import("std");
fn gnomeSortBubble(nums: []i32) void {
    const n = nums.len;
    for (0..n) |i| {
        for (0..n - 1 - i) |j| {
            if (nums[j] > nums[j + 1]) {
                const t = nums[j];
                nums[j] = nums[j + 1];
                nums[j + 1] = t;
            }
        }
    }
}
pub fn main() !void {
    var v1 = [_]i32{ 5, 4, 3, 2, 1 };
    gnomeSortBubble(&v1);
    if (v1[0] != 1 or v1[4] != 5) return error.TestFailed;
    var v2 = [_]i32{ 3, 1, 2 };
    gnomeSortBubble(&v2);
    if (v2[0] != 1 or v2[2] != 3) return error.TestFailed;
    std.debug.print("PASS\\n", .{}); }''',
"dart":'''List<int> gnomeSortBubble(List<int> nums) {
  final v = List<int>.from(nums);
  final n = v.length;
  for (var i = 0; i < n; i++) {
    for (var j = 0; j < n - 1 - i; j++) {
      if (v[j] > v[j + 1]) {
        final t = v[j];
        v[j] = v[j + 1];
        v[j + 1] = t;
      }
    }
  }
  return v;
}
void main() { if (gnomeSortBubble([5,4,3,2,1]).toString() != '[1, 2, 3, 4, 5]') throw StateError('c1'); if (gnomeSortBubble([3,1,2]).toString() != '[1, 2, 3]') throw StateError('c2'); if (gnomeSortBubble([]).isNotEmpty) throw StateError('c3'); print('PASS'); }''',
}

QUICK = {
"rust":'''fn quick_sort(nums: Vec<i32>) -> Vec<i32> {
    if nums.len() <= 1 { return nums; }
    let pivot = nums[nums.len() / 2];
    let mut lt: Vec<i32> = Vec::new();
    let mut eq: Vec<i32> = Vec::new();
    let mut gt: Vec<i32> = Vec::new();
    for &x in &nums {
        if x < pivot { lt.push(x); } else if x == pivot { eq.push(x); } else { gt.push(x); }
    }
    let mut out = quick_sort(lt);
    out.extend(eq);
    out.extend(quick_sort(gt));
    out
}
fn main() {
    assert_eq!(quick_sort(vec![5,4,3,2,1]), vec![1,2,3,4,5]);
    assert_eq!(quick_sort(vec![3,1,4,1,5]), vec![1,1,3,4,5]);
    println!("PASS"); }''',
"lua":'''local function quick_sort(nums)
    if #nums <= 1 then return nums end
    local pivot = nums[#nums // 2 + 1]
    local lt, eq, gt = {}, {}, {}
    for _, x in ipairs(nums) do
        if x < pivot then lt[#lt + 1] = x
        elseif x == pivot then eq[#eq + 1] = x
        else gt[#gt + 1] = x end
    end
    local out = {}
    for _, v in ipairs(quick_sort(lt)) do out[#out + 1] = v end
    for _, v in ipairs(eq) do out[#out + 1] = v end
    for _, v in ipairs(quick_sort(gt)) do out[#out + 1] = v end
    return out
end
assert(table.concat(quick_sort({5,4,3,2,1}), ",") == "1,2,3,4,5")
assert(table.concat(quick_sort({3,1,4,1,5}), ",") == "1,1,3,4,5")
print("PASS")''',
"c":'''#include <stdio.h>
static void qs(int v[], int lo, int hi) {
    if (lo >= hi) return;
    int pivot = v[(lo + hi) / 2];
    int i = lo, j = hi;
    while (i <= j) {
        while (v[i] < pivot) i++;
        while (v[j] > pivot) j--;
        if (i <= j) { int t = v[i]; v[i] = v[j]; v[j] = t; i++; j--; }
    }
    qs(v, lo, j);
    qs(v, i, hi);
}
int main(void) {
    int v1[] = {5,4,3,2,1};
    qs(v1, 0, 4);
    for (int i = 0; i < 5; i++) if (v1[i] != i + 1) { printf("FAIL 1\\n"); return 1; }
    int v2[] = {3,1,4,1,5};
    qs(v2, 0, 4);
    if (!(v2[0]==1&&v2[1]==1&&v2[4]==5)) { printf("FAIL 2\\n"); return 1; }
    printf("PASS\\n"); return 0; }''',
"cpp":'''#include <cassert>
#include <iostream>
#include <vector>
static std::vector<int> quickSort(const std::vector<int> &nums) {
    if (nums.size() <= 1) return nums;
    int pivot = nums[nums.size() / 2];
    std::vector<int> lt, eq, gt;
    for (int x : nums) {
        if (x < pivot) lt.push_back(x);
        else if (x == pivot) eq.push_back(x);
        else gt.push_back(x);
    }
    auto out = quickSort(lt);
    out.insert(out.end(), eq.begin(), eq.end());
    auto r = quickSort(gt);
    out.insert(out.end(), r.begin(), r.end());
    return out;
}
int main() {
    assert((quickSort({5,4,3,2,1}) == std::vector<int>{1,2,3,4,5}));
    assert((quickSort({3,1,4,1,5}) == std::vector<int>{1,1,3,4,5}));
    std::cout << "PASS" << std::endl; }''',
"r":'''quick_sort <- function(nums) {
  if (length(nums) <= 1) return(nums)
  pivot <- nums[floor(length(nums) / 2) + 1]
  c(quick_sort(nums[nums < pivot]), nums[nums == pivot], quick_sort(nums[nums > pivot]))
}
stopifnot(identical(as.integer(quick_sort(c(5, 4, 3, 2, 1))), 1:5))
stopifnot(identical(as.integer(quick_sort(c(3, 1, 4, 1, 5))), c(1L, 1L, 3L, 4L, 5L)))
cat("PASS\\n")''',
"zig":'''const std = @import("std");
fn quickSortPart(nums: []i32, lo: isize, hi: isize) void {
    if (lo >= hi) return;
    const pivot = nums[@intCast(@divTrunc(lo + hi, 2))];
    var i = lo;
    var j = hi;
    while (i <= j) {
        while (nums[@intCast(i)] < pivot) i += 1;
        while (nums[@intCast(j)] > pivot) j -= 1;
        if (i <= j) {
            const t = nums[@intCast(i)];
            nums[@intCast(i)] = nums[@intCast(j)];
            nums[@intCast(j)] = t;
            i += 1;
            j -= 1;
        }
    }
    quickSortPart(nums, lo, j);
    quickSortPart(nums, i, hi);
}
pub fn main() !void {
    var v1 = [_]i32{ 5, 4, 3, 2, 1 };
    quickSortPart(&v1, 0, 4);
    if (v1[0] != 1 or v1[4] != 5) return error.TestFailed;
    var v2 = [_]i32{ 3, 1, 4, 1, 5 };
    quickSortPart(&v2, 0, 4);
    if (v2[0] != 1 or v2[1] != 1 or v2[4] != 5) return error.TestFailed;
    std.debug.print("PASS\\n", .{}); }''',
"dart":'''List<int> quickSort(List<int> nums) {
  if (nums.length <= 1) return nums;
  final pivot = nums[nums.length ~/ 2];
  final lt = <int>[], eq = <int>[], gt = <int>[];
  for (final x in nums) {
    if (x < pivot) { lt.add(x); } else if (x == pivot) { eq.add(x); } else { gt.add(x); }
  }
  return [...quickSort(lt), ...eq, ...quickSort(gt)];
}
void main() { if (quickSort([5,4,3,2,1]).toString() != '[1, 2, 3, 4, 5]') throw StateError('c1'); if (quickSort([3,1,4,1,5]).toString() != '[1, 1, 3, 4, 5]') throw StateError('c2'); print('PASS'); }''',
}

INSERTION = {
"rust":'''fn insertion_sort(nums: Vec<i32>) -> Vec<i32> {
    let mut v = nums;
    for i in 1..v.len() {
        let key = v[i];
        let mut j = i;
        while j > 0 && v[j - 1] > key { v[j] = v[j - 1]; j -= 1; }
        v[j] = key;
    }
    v
}
fn main() {
    assert_eq!(insertion_sort(vec![5,4,3,2,1]), vec![1,2,3,4,5]);
    assert_eq!(insertion_sort(vec![3,1,2]), vec![1,2,3]);
    println!("PASS"); }''',
"lua":'''local function insertion_sort(nums)
    local v = {table.unpack(nums)}
    for i = 2, #v do
        local key = v[i]
        local j = i - 1
        while j >= 1 and v[j] > key do v[j + 1] = v[j]; j = j - 1 end
        v[j + 1] = key
    end
    return v
end
assert(table.concat(insertion_sort({5,4,3,2,1}), ",") == "1,2,3,4,5")
assert(table.concat(insertion_sort({3,1,2}), ",") == "1,2,3")
print("PASS")''',
"c":'''#include <stdio.h>
static void insertion_sort(int v[], int n) {
    for (int i = 1; i < n; i++) {
        int key = v[i];
        int j = i - 1;
        while (j >= 0 && v[j] > key) { v[j + 1] = v[j]; j--; }
        v[j + 1] = key;
    }
}
int main(void) {
    int v1[] = {5,4,3,2,1};
    insertion_sort(v1, 5);
    for (int i = 0; i < 5; i++) if (v1[i] != i + 1) { printf("FAIL\\n"); return 1; }
    printf("PASS\\n"); return 0; }''',
"cpp":'''#include <cassert>
#include <iostream>
#include <vector>
static std::vector<int> insertionSort(std::vector<int> v) {
    for (size_t i = 1; i < v.size(); ++i) {
        int key = v[i];
        size_t j = i;
        while (j > 0 && v[j - 1] > key) { v[j] = v[j - 1]; --j; }
        v[j] = key;
    }
    return v;
}
int main() { assert((insertionSort({5,4,3,2,1}) == std::vector<int>{1,2,3,4,5})); std::cout << "PASS" << std::endl; }''',
"r":'''insertion_sort <- function(nums) {
  v <- nums
  for (i in 2:length(v)) {
    key <- v[i]
    j <- i - 1
    while (j >= 1 && v[j] > key) { v[j + 1] <- v[j]; j <- j - 1 }
    v[j + 1] <- key
  }
  v
}
stopifnot(identical(as.integer(insertion_sort(c(5, 4, 3, 2, 1))), 1:5))
stopifnot(identical(as.integer(insertion_sort(c(3, 1, 2))), c(1L, 2L, 3L)))
cat("PASS\\n")''',
"zig":'''const std = @import("std");
fn insertionSort(nums: []i32) void {
    for (1..nums.len) |i| {
        const key = nums[i];
        var j = i;
        while (j > 0 and nums[j - 1] > key) {
            nums[j] = nums[j - 1];
            j -= 1;
        }
        nums[j] = key;
    }
}
pub fn main() !void {
    var v1 = [_]i32{ 5, 4, 3, 2, 1 };
    insertionSort(&v1);
    if (v1[0] != 1 or v1[4] != 5) return error.TestFailed;
    std.debug.print("PASS\\n", .{}); }''',
"dart":'''List<int> insertionSort(List<int> nums) {
  final v = List<int>.from(nums);
  for (var i = 1; i < v.length; i++) {
    final key = v[i];
    var j = i - 1;
    while (j >= 0 && v[j] > key) { v[j + 1] = v[j]; j--; }
    v[j + 1] = key;
  }
  return v;
}
void main() { if (insertionSort([5,4,3,2,1]).toString() != '[1, 2, 3, 4, 5]') throw StateError('c1'); print('PASS'); }''',
}

MERGE = {
"rust":'''fn merge_sort(nums: Vec<i32>) -> Vec<i32> {
    if nums.len() <= 1 { return nums; }
    let mid = nums.len() / 2;
    let left = merge_sort(nums[..mid].to_vec());
    let right = merge_sort(nums[mid..].to_vec());
    let mut out = Vec::with_capacity(nums.len());
    let (mut i, mut j) = (0usize, 0usize);
    while i < left.len() && j < right.len() {
        if left[i] <= right[j] { out.push(left[i]); i += 1; } else { out.push(right[j]); j += 1; }
    }
    out.extend_from_slice(&left[i..]);
    out.extend_from_slice(&right[j..]);
    out
}
fn main() {
    assert_eq!(merge_sort(vec![5,4,3,2,1]), vec![1,2,3,4,5]);
    assert_eq!(merge_sort(vec![3,1,4,1,5]), vec![1,1,3,4,5]);
    println!("PASS"); }''',
"lua":'''local function merge_sort(nums)
    if #nums <= 1 then return nums end
    local mid = #nums // 2
    local left, right = {}, {}
    for i = 1, mid do left[i] = nums[i] end
    for i = mid + 1, #nums do right[i - mid] = nums[i] end
    left = merge_sort(left)
    right = merge_sort(right)
    local out, i, j = {}, 1, 1
    while i <= #left and j <= #right do
        if left[i] <= right[j] then out[#out + 1] = left[i]; i = i + 1
        else out[#out + 1] = right[j]; j = j + 1 end
    end
    while i <= #left do out[#out + 1] = left[i]; i = i + 1 end
    while j <= #right do out[#out + 1] = right[j]; j = j + 1 end
    return out
end
assert(table.concat(merge_sort({5,4,3,2,1}), ",") == "1,2,3,4,5")
assert(table.concat(merge_sort({3,1,4,1,5}), ",") == "1,1,3,4,5")
print("PASS")''',
"c":'''#include <stdio.h>
#include <stdlib.h>
static void ms(int v[], int lo, int hi) {
    if (lo >= hi) return;
    int mid = (lo + hi) / 2;
    ms(v, lo, mid);
    ms(v, mid + 1, hi);
    int tmp[4096];
    int i = lo, j = mid + 1, k = 0;
    while (i <= mid && j <= hi) {
        if (v[i] <= v[j]) tmp[k++] = v[i++];
        else tmp[k++] = v[j++];
    }
    while (i <= mid) tmp[k++] = v[i++];
    while (j <= hi) tmp[k++] = v[j++];
    for (int x = 0; x < k; x++) v[lo + x] = tmp[x];
}
int main(void) {
    int v1[] = {5,4,3,2,1};
    ms(v1, 0, 4);
    for (int i = 0; i < 5; i++) if (v1[i] != i + 1) { printf("FAIL\\n"); return 1; }
    printf("PASS\\n"); return 0; }''',
"cpp":'''#include <cassert>
#include <iostream>
#include <vector>
static std::vector<int> mergeSort(const std::vector<int> &nums) {
    if (nums.size() <= 1) return nums;
    size_t mid = nums.size() / 2;
    auto left = mergeSort(std::vector<int>(nums.begin(), nums.begin() + mid));
    auto right = mergeSort(std::vector<int>(nums.begin() + mid, nums.end()));
    std::vector<int> out;
    size_t i = 0, j = 0;
    while (i < left.size() && j < right.size()) {
        if (left[i] <= right[j]) out.push_back(left[i++]);
        else out.push_back(right[j++]);
    }
    while (i < left.size()) out.push_back(left[i++]);
    while (j < right.size()) out.push_back(right[j++]);
    return out;
}
int main() {
    assert((mergeSort({5,4,3,2,1}) == std::vector<int>{1,2,3,4,5}));
    assert((mergeSort({3,1,4,1,5}) == std::vector<int>{1,1,3,4,5}));
    std::cout << "PASS" << std::endl; }''',
"r":'''merge_sort <- function(nums) {
  if (length(nums) <= 1) return(nums)
  mid <- length(nums) %/% 2
  left <- merge_sort(nums[1:mid])
  right <- merge_sort(nums[(mid + 1):length(nums)])
  out <- integer(0)
  i <- 1L; j <- 1L
  while (i <= length(left) && j <= length(right)) {
    if (left[i] <= right[j]) { out <- c(out, left[i]); i <- i + 1 }
    else { out <- c(out, right[j]); j <- j + 1 }
  }
  while (i <= length(left)) { out <- c(out, left[i]); i <- i + 1 }
  while (j <= length(right)) { out <- c(out, right[j]); j <- j + 1 }
  out
}
stopifnot(identical(as.integer(merge_sort(c(5, 4, 3, 2, 1))), 1:5))
stopifnot(identical(as.integer(merge_sort(c(3, 1, 4, 1, 5))), c(1L, 1L, 3L, 4L, 5L)))
cat("PASS\\n")''',
"zig":'''const std = @import("std");
fn mergeSort(nums: []i32, tmp: []i32, lo: usize, hi: usize) void {
    if (lo >= hi) return;
    const mid = (lo + hi) / 2;
    mergeSort(nums, tmp, lo, mid);
    mergeSort(nums, tmp, mid + 1, hi);
    var i = lo;
    var j = mid + 1;
    var k: usize = 0;
    while (i <= mid and j <= hi) {
        if (nums[i] <= nums[j]) {
            tmp[k] = nums[i];
            i += 1;
        } else {
            tmp[k] = nums[j];
            j += 1;
        }
        k += 1;
    }
    while (i <= mid) {
        tmp[k] = nums[i];
        i += 1;
        k += 1;
    }
    while (j <= hi) {
        tmp[k] = nums[j];
        j += 1;
        k += 1;
    }
    for (0..k) |x| nums[lo + x] = tmp[x];
}
pub fn main() !void {
    var v1 = [_]i32{ 5, 4, 3, 2, 1 };
    var tmp: [8]i32 = undefined;
    mergeSort(&v1, &tmp, 0, 4);
    if (v1[0] != 1 or v1[4] != 5) return error.TestFailed;
    std.debug.print("PASS\\n", .{}); }''',
"dart":'''List<int> mergeSort(List<int> nums) {
  if (nums.length <= 1) return nums;
  final mid = nums.length ~/ 2;
  final left = mergeSort(nums.sublist(0, mid));
  final right = mergeSort(nums.sublist(mid));
  final out = <int>[];
  var i = 0, j = 0;
  while (i < left.length && j < right.length) {
    if (left[i] <= right[j]) { out.add(left[i++]); } else { out.add(right[j++]); }
  }
  while (i < left.length) { out.add(left[i++]); }
  while (j < right.length) { out.add(right[j++]); }
  return out;
}
void main() { if (mergeSort([5,4,3,2,1]).toString() != '[1, 2, 3, 4, 5]') throw StateError('c1'); print('PASS'); }''',
}

SELECTION = {
"rust":'''fn selection_sort(nums: Vec<i32>) -> Vec<i32> {
    let mut v = nums;
    let n = v.len();
    for i in 0..n {
        let mut m = i;
        for j in i + 1..n { if v[j] < v[m] { m = j; } }
        v.swap(i, m);
    }
    v
}
fn main() {
    assert_eq!(selection_sort(vec![5,4,3,2,1]), vec![1,2,3,4,5]);
    assert_eq!(selection_sort(vec![3,1,2]), vec![1,2,3]);
    println!("PASS"); }''',
"lua":'''local function selection_sort(nums)
    local v = {table.unpack(nums)}
    local n = #v
    for i = 1, n - 1 do
        local m = i
        for j = i + 1, n do if v[j] < v[m] then m = j end end
        v[i], v[m] = v[m], v[i]
    end
    return v
end
assert(table.concat(selection_sort({5,4,3,2,1}), ",") == "1,2,3,4,5")
assert(table.concat(selection_sort({3,1,2}), ",") == "1,2,3")
print("PASS")''',
"c":'''#include <stdio.h>
static void selection_sort(int v[], int n) {
    for (int i = 0; i < n - 1; i++) {
        int m = i;
        for (int j = i + 1; j < n; j++) if (v[j] < v[m]) m = j;
        int t = v[i]; v[i] = v[m]; v[m] = t;
    }
}
int main(void) {
    int v1[] = {5,4,3,2,1};
    selection_sort(v1, 5);
    for (int i = 0; i < 5; i++) if (v1[i] != i + 1) { printf("FAIL\\n"); return 1; }
    printf("PASS\\n"); return 0; }''',
"cpp":'''#include <cassert>
#include <iostream>
#include <vector>
static std::vector<int> selectionSort(std::vector<int> v) {
    for (size_t i = 0; i + 1 < v.size(); ++i) {
        size_t m = i;
        for (size_t j = i + 1; j < v.size(); ++j) if (v[j] < v[m]) m = j;
        std::swap(v[i], v[m]);
    }
    return v;
}
int main() { assert((selectionSort({5,4,3,2,1}) == std::vector<int>{1,2,3,4,5})); std::cout << "PASS" << std::endl; }''',
"r":'''selection_sort <- function(nums) {
  v <- nums
  n <- length(v)
  for (i in 1:(n - 1)) {
    m <- i
    for (j in (i + 1):n) if (v[j] < v[m]) m <- j
    t <- v[i]; v[i] <- v[m]; v[m] <- t
  }
  v
}
stopifnot(identical(as.integer(selection_sort(c(5, 4, 3, 2, 1))), 1:5))
stopifnot(identical(as.integer(selection_sort(c(3, 1, 2))), c(1L, 2L, 3L)))
cat("PASS\\n")''',
"zig":'''const std = @import("std");
fn selectionSort(nums: []i32) void {
    const n = nums.len;
    for (0..n - 1) |i| {
        var m = i;
        for (i + 1..n) |j| {
            if (nums[j] < nums[m]) m = j;
        }
        const t = nums[i];
        nums[i] = nums[m];
        nums[m] = t;
    }
}
pub fn main() !void {
    var v1 = [_]i32{ 5, 4, 3, 2, 1 };
    selectionSort(&v1);
    if (v1[0] != 1 or v1[4] != 5) return error.TestFailed;
    std.debug.print("PASS\\n", .{}); }''',
"dart":'''List<int> selectionSort(List<int> nums) {
  final v = List<int>.from(nums);
  for (var i = 0; i + 1 < v.length; i++) {
    var m = i;
    for (var j = i + 1; j < v.length; j++) { if (v[j] < v[m]) m = j; }
    final t = v[i];
    v[i] = v[m];
    v[m] = t;
  }
  return v;
}
void main() { if (selectionSort([5,4,3,2,1]).toString() != '[1, 2, 3, 4, 5]') throw StateError('c1'); print('PASS'); }''',
}

GNOME = {
"rust":'''fn gnome_sort(nums: Vec<i32>) -> Vec<i32> {
    let mut v = nums;
    let mut i = 0usize;
    while i < v.len() {
        if i == 0 || v[i - 1] <= v[i] { i += 1; }
        else { v.swap(i - 1, i); i -= 1; }
    }
    v
}
fn main() {
    assert_eq!(gnome_sort(vec![5,4,3,2,1]), vec![1,2,3,4,5]);
    assert_eq!(gnome_sort(vec![3,1,2]), vec![1,2,3]);
    println!("PASS"); }''',
"lua":'''local function gnome_sort(nums)
    local v = {table.unpack(nums)}
    local i = 1
    while i <= #v do
        if i == 1 or v[i - 1] <= v[i] then i = i + 1
        else v[i - 1], v[i] = v[i], v[i - 1]; i = i - 1 end
    end
    return v
end
assert(table.concat(gnome_sort({5,4,3,2,1}), ",") == "1,2,3,4,5")
assert(table.concat(gnome_sort({3,1,2}), ",") == "1,2,3")
print("PASS")''',
"c":'''#include <stdio.h>
static void gnome_sort(int v[], int n) {
    int i = 0;
    while (i < n) {
        if (i == 0 || v[i - 1] <= v[i]) i++;
        else { int t = v[i - 1]; v[i - 1] = v[i]; v[i] = t; i--; }
    }
}
int main(void) {
    int v1[] = {5,4,3,2,1};
    gnome_sort(v1, 5);
    for (int i = 0; i < 5; i++) if (v1[i] != i + 1) { printf("FAIL\\n"); return 1; }
    printf("PASS\\n"); return 0; }''',
"cpp":'''#include <cassert>
#include <iostream>
#include <vector>
static std::vector<int> gnomeSort(std::vector<int> v) {
    size_t i = 0;
    while (i < v.size()) {
        if (i == 0 || v[i - 1] <= v[i]) ++i;
        else { std::swap(v[i - 1], v[i]); --i; }
    }
    return v;
}
int main() { assert((gnomeSort({5,4,3,2,1}) == std::vector<int>{1,2,3,4,5})); std::cout << "PASS" << std::endl; }''',
"r":'''gnome_sort <- function(nums) {
  v <- nums
  i <- 1L
  while (i <= length(v)) {
    if (i == 1L || v[i - 1L] <= v[i]) i <- i + 1L
    else { t <- v[i - 1L]; v[i - 1L] <- v[i]; v[i] <- t; i <- i - 1L }
  }
  v
}
stopifnot(identical(as.integer(gnome_sort(c(5, 4, 3, 2, 1))), 1:5))
stopifnot(identical(as.integer(gnome_sort(c(3, 1, 2))), c(1L, 2L, 3L)))
cat("PASS\\n")''',
"zig":'''const std = @import("std");
fn gnomeSort(nums: []i32) void {
    var i: usize = 0;
    while (i < nums.len) {
        if (i == 0 or nums[i - 1] <= nums[i]) {
            i += 1;
        } else {
            const t = nums[i - 1];
            nums[i - 1] = nums[i];
            nums[i] = t;
            i -= 1;
        }
    }
}
pub fn main() !void {
    var v1 = [_]i32{ 5, 4, 3, 2, 1 };
    gnomeSort(&v1);
    if (v1[0] != 1 or v1[4] != 5) return error.TestFailed;
    std.debug.print("PASS\\n", .{}); }''',
"dart":'''List<int> gnomeSort(List<int> nums) {
  final v = List<int>.from(nums);
  var i = 0;
  while (i < v.length) {
    if (i == 0 || v[i - 1] <= v[i]) { i++; }
    else {
      final t = v[i - 1];
      v[i - 1] = v[i];
      v[i] = t;
      i--;
    }
  }
  return v;
}
void main() { if (gnomeSort([5,4,3,2,1]).toString() != '[1, 2, 3, 4, 5]') throw StateError('c1'); print('PASS'); }''',
}

PROB_SORTS = [
    ("lc_134066237_冒泡排序", BUBBLE, "134066237", "数据结构与算法之排序: 冒泡排序"),
    ("lc_134073792_快速排序", QUICK, "134073792", "数据结构与算法之排序: 快速排序"),
    ("lc_134082074_插入排序", INSERTION, "134082074", "数据结构与算法之排序: 插入排序"),
    ("lc_134083295_归并排序", MERGE, "134083295", "数据结构与算法之排序: 归并排序"),
    ("lc_134085384_选择排序", SELECTION, "134085384", "数据结构与算法之排序: 选择排序"),
    ("lc_134053461_侏儒排序", GNOME, "134053461", "数据结构与算法之排序: 侏儒排序"),
]
count = 0
for pdir, algo, bid, title in PROB_SORTS:
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
