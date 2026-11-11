#!/usr/bin/env python3
# gen_ll3.py — linked_list 收官：2/92/234/148/146/460/707 × 7语言
# 全部用「值数组进出」模式，规避各语言指针/所有权差异
import sys, os; sys.path.insert(0, "/Users/Wang/Code/webfault-ai/dsa/_tools")
from langlib import emit, head_comment, EXT

B = {"2": "133598918", "92": "133657416", "234": "133812752", "148": "133904873", "146": "134537871", "460": "137295891", "707": "134120377"}
LANGNAME = {"rust": "Rust", "lua": "Lua", "c": "C", "cpp": "C++", "r": "R", "zig": "Zig", "dart": "Dart"}

A2 = {
"rust": '''fn add_two_numbers(a: Vec<i32>, b: Vec<i32>) -> Vec<i32> {
    let (mut i, mut j, mut carry) = (0usize, 0usize, 0i32);
    let mut out = Vec::new();
    while i < a.len() || j < b.len() || carry > 0 {
        let mut total = carry;
        if i < a.len() { total += a[i]; i += 1; }
        if j < b.len() { total += b[j]; j += 1; }
        out.push(total % 10);
        carry = total / 10;
    }
    if out.is_empty() { out.push(0); }
    out
}
fn main() {
    assert_eq!(add_two_numbers(vec![2, 4, 3], vec![5, 6, 4]), vec![7, 0, 8]);
    assert_eq!(add_two_numbers(vec![0], vec![0]), vec![0]);
    assert_eq!(add_two_numbers(vec![9, 9, 9, 9, 9, 9, 9], vec![9, 9, 9, 9]), vec![8, 9, 9, 9, 0, 0, 0, 1]);
    println!("PASS");
}
''',
"lua": '''local function add_two_numbers(a, b)
    local i, j, carry = 1, 1, 0
    local out = {}
    while i <= #a or j <= #b or carry > 0 do
        local total = carry
        if i <= #a then total = total + a[i]; i = i + 1 end
        if j <= #b then total = total + b[j]; j = j + 1 end
        out[#out + 1] = total % 10
        carry = math.floor(total / 10)
    end
    if #out == 0 then out[1] = 0 end
    return out
end
assert(table.concat(add_two_numbers({2, 4, 3}, {5, 6, 4}), ",") == "7,0,8")
assert(table.concat(add_two_numbers({0}, {0}), ",") == "0")
assert(table.concat(add_two_numbers({9,9,9,9,9,9,9}, {9,9,9,9}), ",") == "8,9,9,9,0,0,0,1")
print("PASS")
''',
"c": '''#include <stdio.h>
static int add_two_numbers(const int *a, int na, const int *b, int nb, int out[]) {
    int i = 0, j = 0, carry = 0, n = 0;
    while (i < na || j < nb || carry) {
        int total = carry;
        if (i < na) { total += a[i++]; }
        if (j < nb) { total += b[j++]; }
        out[n++] = total % 10;
        carry = total / 10;
    }
    if (n == 0) out[n++] = 0;
    return n;
}
int main(void) {
    int out[64], n;
    int w1[] = {7,0,8}, w2[] = {0}, w3[] = {8,9,9,9,0,0,0,1};
    n = add_two_numbers((int[]){2,4,3}, 3, (int[]){5,6,4}, 3, out);
    if (n != 3) { printf("FAIL n1\\n"); return 1; }
    for (int i = 0; i < 3; i++) if (out[i] != w1[i]) { printf("FAIL 1\\n"); return 1; }
    n = add_two_numbers((int[]){0}, 1, (int[]){0}, 1, out);
    if (n != 1 || out[0] != 0) { printf("FAIL 2\\n"); return 1; }
    n = add_two_numbers((int[]){9,9,9,9,9,9,9}, 7, (int[]){9,9,9,9}, 4, out);
    if (n != 8) { printf("FAIL n3\\n"); return 1; }
    for (int i = 0; i < 8; i++) if (out[i] != w3[i]) { printf("FAIL 3\\n"); return 1; }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''#include <cassert>
#include <iostream>
#include <vector>
static std::vector<int> addTwoNumbers(const std::vector<int> &a, const std::vector<int> &b) {
    size_t i = 0, j = 0;
    int carry = 0;
    std::vector<int> out;
    while (i < a.size() || j < b.size() || carry) {
        int total = carry;
        if (i < a.size()) total += a[i++];
        if (j < b.size()) total += b[j++];
        out.push_back(total % 10);
        carry = total / 10;
    }
    if (out.empty()) out.push_back(0);
    return out;
}
int main() {
    assert((addTwoNumbers({2, 4, 3}, {5, 6, 4}) == std::vector<int>{7, 0, 8}));
    assert((addTwoNumbers({0}, {0}) == std::vector<int>{0}));
    assert((addTwoNumbers({9, 9, 9, 9, 9, 9, 9}, {9, 9, 9, 9}) == std::vector<int>{8, 9, 9, 9, 0, 0, 0, 1}));
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''add_two_numbers <- function(a, b) {
  i <- 1L; j <- 1L; carry <- 0L
  out <- integer(0)
  while (i <= length(a) || j <= length(b) || carry > 0) {
    total <- carry
    if (i <= length(a)) { total <- total + a[i]; i <- i + 1L }
    if (j <= length(b)) { total <- total + b[j]; j <- j + 1L }
    out <- c(out, total %% 10)
    carry <- total %/% 10
  }
  if (length(out) == 0) out <- 0L
  out
}
stopifnot(identical(add_two_numbers(c(2, 4, 3), c(5, 6, 4)), c(7, 0, 8)))
stopifnot(identical(add_two_numbers(0, 0), 0))
stopifnot(identical(add_two_numbers(c(9,9,9,9,9,9,9), c(9,9,9,9)), c(8, 9, 9, 9, 0, 0, 0, 1)))
cat("PASS\\n")
''',
"zig": '''const std = @import("std");
fn addTwoNumbers(a: []const i32, b: []const i32, out: *std.ArrayList(i32)) void {
    var i: usize = 0;
    var j: usize = 0;
    var carry: i32 = 0;
    while (i < a.len or j < b.len or carry > 0) {
        var total: i32 = carry;
        if (i < a.len) { total += a[i]; i += 1; }
        if (j < b.len) { total += b[j]; j += 1; }
        out.append(@mod(total, 10)) catch unreachable;
        carry = @divTrunc(total, 10);
    }
    if (out.items.len == 0) out.append(0) catch unreachable;
}
pub fn main() !void {
    var out = std.ArrayList(i32).init(std.heap.page_allocator);
    defer out.deinit();
    addTwoNumbers(&[_]i32{ 2, 4, 3 }, &[_]i32{ 5, 6, 4 }, &out);
    if (out.items.len != 3 or out.items[0] != 7 or out.items[2] != 8) return error.TestFailed;
    out.clearRetainingCapacity();
    addTwoNumbers(&[_]i32{0}, &[_]i32{0}, &out);
    if (out.items.len != 1 or out.items[0] != 0) return error.TestFailed;
    out.clearRetainingCapacity();
    addTwoNumbers(&[_]i32{ 9, 9, 9, 9, 9, 9, 9 }, &[_]i32{ 9, 9, 9, 9 }, &out);
    if (out.items.len != 8 or out.items[7] != 1) return error.TestFailed;
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''List<int> addTwoNumbers(List<int> a, List<int> b) {
  var i = 0, j = 0, carry = 0;
  final out = <int>[];
  while (i < a.length || j < b.length || carry > 0) {
    var total = carry;
    if (i < a.length) {
      total += a[i++];
    }
    if (j < b.length) {
      total += b[j++];
    }
    out.add(total % 10);
    carry = total ~/ 10;
  }
  if (out.isEmpty) out.add(0);
  return out;
}
void main() {
  if (addTwoNumbers([2, 4, 3], [5, 6, 4]).toString() != '[7, 0, 8]') throw StateError('c1');
  if (addTwoNumbers([0], [0]).toString() != '[0]') throw StateError('c2');
  if (addTwoNumbers([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9]).toString() != '[8, 9, 9, 9, 0, 0, 0, 1]') throw StateError('c3');
  print('PASS');
}
''',
}

A92 = {
"rust": '''fn reverse_between(vals: Vec<i32>, left: i32, right: i32) -> Vec<i32> {
    let mut v = vals;
    let (l, r) = ((left - 1) as usize, (right - 1) as usize);
    let seg: Vec<i32> = v[l..=r].iter().rev().cloned().collect();
    v[l..=r].copy_from_slice(&seg);
    v
}
fn main() {
    assert_eq!(reverse_between(vec![1, 2, 3, 4, 5], 2, 4), vec![1, 4, 3, 2, 5]);
    assert_eq!(reverse_between(vec![1, 2, 3, 4, 5], 1, 4), vec![4, 3, 2, 1, 5]);
    assert_eq!(reverse_between(vec![5], 1, 1), vec![5]);
    println!("PASS");
}
''',
"lua": '''local function reverse_between(vals, left, right)
    local v = {table.unpack(vals)}
    local seg = {}
    for i = right, left, -1 do seg[#seg + 1] = v[i] end
    for i = 1, #seg do v[left + i - 1] = seg[i] end
    return v
end
assert(table.concat(reverse_between({1, 2, 3, 4, 5}, 2, 4), ",") == "1,4,3,2,5")
assert(table.concat(reverse_between({1, 2, 3, 4, 5}, 1, 4), ",") == "4,3,2,1,5")
assert(table.concat(reverse_between({5}, 1, 1), ",") == "5")
print("PASS")
''',
"c": '''#include <stdio.h>
static void reverse_between(int v[], int n, int left, int right) {
    int l = left - 1, r = right - 1;
    while (l < r) {
        int t = v[l]; v[l] = v[r]; v[r] = t;
        l++; r--;
    }
}
int main(void) {
    int v1[] = {1,2,3,4,5};
    reverse_between(v1, 5, 2, 4);
    if (!(v1[0]==1&&v1[1]==4&&v1[2]==3&&v1[3]==2&&v1[4]==5)) { printf("FAIL 1\\n"); return 1; }
    int v2[] = {1,2,3,4,5};
    reverse_between(v2, 5, 1, 4);
    if (!(v2[0]==4&&v2[1]==3&&v2[2]==2&&v2[3]==1&&v2[4]==5)) { printf("FAIL 2\\n"); return 1; }
    int v3[] = {5};
    reverse_between(v3, 1, 1, 1);
    if (v3[0] != 5) { printf("FAIL 3\\n"); return 1; }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''#include <algorithm>
#include <cassert>
#include <iostream>
#include <vector>
static std::vector<int> reverseBetween(std::vector<int> vals, int left, int right) {
    std::reverse(vals.begin() + (left - 1), vals.begin() + right);
    return vals;
}
int main() {
    assert((reverseBetween({1, 2, 3, 4, 5}, 2, 4) == std::vector<int>{1, 4, 3, 2, 5}));
    assert((reverseBetween({1, 2, 3, 4, 5}, 1, 4) == std::vector<int>{4, 3, 2, 1, 5}));
    assert((reverseBetween({5}, 1, 1) == std::vector<int>{5}));
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''reverse_between <- function(vals, left, right) {
  v <- vals
  v[left:right] <- rev(v[left:right])
  v
}
stopifnot(identical(reverse_between(1:5, 2, 4), c(1L, 4L, 3L, 2L, 5L)))
stopifnot(identical(reverse_between(1:5, 1, 4), c(4L, 3L, 2L, 1L, 5L)))
stopifnot(identical(reverse_between(5, 1, 1), 5))
cat("PASS\\n")
''',
"zig": '''const std = @import("std");
fn reverseBetween(vals: []const i32, left: i32, right: i32, out: []i32) void {
    @memcpy(out[0..vals.len], vals);
    var l: usize = @intCast(left - 1);
    var r: usize = @intCast(right - 1);
    while (l < r) {
        const t = out[l];
        out[l] = out[r];
        out[r] = t;
        l += 1;
        r -= 1;
    }
}
pub fn main() !void {
    var buf: [8]i32 = undefined;
    reverseBetween(&[_]i32{ 1, 2, 3, 4, 5 }, 2, 4, &buf);
    if (buf[1] != 4 or buf[3] != 2) return error.TestFailed;
    reverseBetween(&[_]i32{ 1, 2, 3, 4, 5 }, 1, 4, &buf);
    if (buf[0] != 4 or buf[3] != 1 or buf[4] != 5) return error.TestFailed;
    reverseBetween(&[_]i32{5}, 1, 1, &buf);
    if (buf[0] != 5) return error.TestFailed;
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''List<int> reverseBetween(List<int> vals, int left, int right) {
  final v = List<int>.from(vals);
  var l = left - 1, r = right - 1;
  while (l < r) {
    final t = v[l];
    v[l] = v[r];
    v[r] = t;
    l++;
    r--;
  }
  return v;
}
void main() {
  if (reverseBetween([1, 2, 3, 4, 5], 2, 4).toString() != '[1, 4, 3, 2, 5]') throw StateError('c1');
  if (reverseBetween([1, 2, 3, 4, 5], 1, 4).toString() != '[4, 3, 2, 1, 5]') throw StateError('c2');
  if (reverseBetween([5], 1, 1).toString() != '[5]') throw StateError('c3');
  print('PASS');
}
''',
}

A234 = {
"rust": '''fn is_palindrome_list(vals: Vec<i32>) -> bool {
    let (mut i, mut j) = (0usize, vals.len());
    if j == 0 { return true; }
    j -= 1;
    while i < j {
        if vals[i] != vals[j] { return false; }
        i += 1;
        if j == 0 { break; }
        j -= 1;
    }
    true
}
fn main() {
    assert!(is_palindrome_list(vec![]));
    assert!(is_palindrome_list(vec![1, 2, 2, 1]));
    assert!(!is_palindrome_list(vec![1, 2]));
    println!("PASS");
}
''',
"lua": '''local function is_palindrome_list(vals)
    local i, j = 1, #vals
    while i < j do
        if vals[i] ~= vals[j] then return false end
        i = i + 1
        j = j - 1
    end
    return true
end
assert(is_palindrome_list({}) == true)
assert(is_palindrome_list({1, 2, 2, 1}) == true)
assert(is_palindrome_list({1, 2}) == false)
print("PASS")
''',
"c": '''#include <stdio.h>
static int is_palindrome_list(const int *v, int n) {
    int i = 0, j = n - 1;
    while (i < j) {
        if (v[i] != v[j]) return 0;
        i++; j--;
    }
    return 1;
}
int main(void) {
    int v1[] = {1,2,2,1}, v2[] = {1,2};
    if (!is_palindrome_list(NULL, 0)) { printf("FAIL 0\\n"); return 1; }
    if (!is_palindrome_list(v1, 4)) { printf("FAIL 1\\n"); return 1; }
    if (is_palindrome_list(v2, 2)) { printf("FAIL 2\\n"); return 1; }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''#include <cassert>
#include <iostream>
#include <vector>
static bool isPalindromeList(const std::vector<int> &v) {
    size_t i = 0, j = v.size();
    if (j == 0) return true;
    --j;
    while (i < j) {
        if (v[i] != v[j]) return false;
        ++i; --j;
    }
    return true;
}
int main() {
    assert(isPalindromeList({}));
    assert(isPalindromeList({1, 2, 2, 1}));
    assert(!isPalindromeList({1, 2}));
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''is_palindrome_list <- function(vals) {
  if (length(vals) == 0) return(TRUE)
  identical(vals, rev(vals))
}
stopifnot(is_palindrome_list(integer(0)))
stopifnot(is_palindrome_list(c(1, 2, 2, 1)))
stopifnot(!is_palindrome_list(c(1, 2)))
cat("PASS\\n")
''',
"zig": '''const std = @import("std");
fn isPalindromeList(v: []const i32) bool {
    if (v.len == 0) return true;
    var i: usize = 0;
    var j: usize = v.len - 1;
    while (i < j) {
        if (v[i] != v[j]) return false;
        i += 1;
        j -= 1;
    }
    return true;
}
pub fn main() !void {
    if (!isPalindromeList(&[_]i32{})) return error.TestFailed;
    if (!isPalindromeList(&[_]i32{ 1, 2, 2, 1 })) return error.TestFailed;
    if (isPalindromeList(&[_]i32{ 1, 2 })) return error.TestFailed;
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''bool isPalindromeList(List<int> v) {
  var i = 0, j = v.length - 1;
  while (i < j) {
    if (v[i] != v[j]) return false;
    i++;
    j--;
  }
  return true;
}
void main() {
  if (!isPalindromeList([])) throw StateError('c0');
  if (!isPalindromeList([1, 2, 2, 1])) throw StateError('c1');
  if (isPalindromeList([1, 2])) throw StateError('c2');
  print('PASS');
}
''',
}

A148 = {
"rust": '''fn sort_list(vals: Vec<i32>) -> Vec<i32> {
    let mut v = vals;
    v.sort();
    v
}
fn main() {
    assert_eq!(sort_list(vec![4, 2, 1, 3]), vec![1, 2, 3, 4]);
    assert_eq!(sort_list(vec![-1, 5, 3, 4, 0]), vec![-1, 0, 3, 4, 5]);
    assert!(sort_list(vec![]).is_empty());
    println!("PASS");
}
''',
"lua": '''local function sort_list(vals)
    local v = {table.unpack(vals)}
    table.sort(v)
    return v
end
assert(table.concat(sort_list({4, 2, 1, 3}), ",") == "1,2,3,4")
assert(table.concat(sort_list({-1, 5, 3, 4, 0}), ",") == "-1,0,3,4,5")
assert(#sort_list({}) == 0)
print("PASS")
''',
"c": '''#include <stdio.h>
#include <stdlib.h>
static int cmp_int(const void *a, const void *b) { return *(const int *)a - *(const int *)b; }
static void sort_list(int v[], int n) {
    qsort(v, n, sizeof(int), cmp_int);
}
int main(void) {
    int v1[] = {4,2,1,3};
    sort_list(v1, 4);
    if (!(v1[0]==1&&v1[1]==2&&v1[2]==3&&v1[3]==4)) { printf("FAIL 1\\n"); return 1; }
    int v2[] = {-1,5,3,4,0};
    sort_list(v2, 5);
    if (!(v2[0]==-1&&v2[1]==0&&v2[2]==3&&v2[3]==4&&v2[4]==5)) { printf("FAIL 2\\n"); return 1; }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''#include <algorithm>
#include <cassert>
#include <iostream>
#include <vector>
static std::vector<int> sortList(std::vector<int> vals) {
    std::sort(vals.begin(), vals.end());
    return vals;
}
int main() {
    assert((sortList({4, 2, 1, 3}) == std::vector<int>{1, 2, 3, 4}));
    assert((sortList({-1, 5, 3, 4, 0}) == std::vector<int>{-1, 0, 3, 4, 5}));
    assert(sortList({}).empty());
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''sort_list <- function(vals) as.integer(sort(vals))
stopifnot(identical(sort_list(c(4, 2, 1, 3)), 1:4))
stopifnot(identical(sort_list(c(-1, 5, 3, 4, 0)), c(-1L, 0L, 3L, 4L, 5L)))
stopifnot(length(sort_list(integer(0))) == 0)
cat("PASS\\n")
''',
"zig": '''const std = @import("std");
fn sortList(vals: []const i32, out: []i32) void {
    @memcpy(out[0..vals.len], vals);
    std.sort.pdq(i32, out[0..vals.len], {}, std.sort.asc(i32));
}
pub fn main() !void {
    var buf: [8]i32 = undefined;
    sortList(&[_]i32{ 4, 2, 1, 3 }, &buf);
    if (buf[0] != 1 or buf[3] != 4) return error.TestFailed;
    sortList(&[_]i32{ -1, 5, 3, 4, 0 }, &buf);
    if (buf[0] != -1 or buf[4] != 5) return error.TestFailed;
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''List<int> sortList(List<int> vals) {
  final v = List<int>.from(vals)..sort();
  return v;
}
void main() {
  if (sortList([4, 2, 1, 3]).toString() != '[1, 2, 3, 4]') throw StateError('c1');
  if (sortList([-1, 5, 3, 4, 0]).toString() != '[-1, 0, 3, 4, 5]') throw StateError('c2');
  if (sortList([]).isNotEmpty) throw StateError('c3');
  print('PASS');
}
''',
}

# 146 LRU / 460 LFU / 707 设计链表：模拟命令序列验证
A146 = {
"rust": '''#[derive(Clone)]
enum Op { Put(i32, i32), Get(i32) }
struct LruSim { cap: usize, keys: std::collections::VecDeque<i32>, vals: std::collections::HashMap<i32, i32> }
impl LruSim {
    fn new(cap: usize) -> Self { LruSim { cap, keys: Default::default(), vals: Default::default() } }
    fn get(&mut self, k: i32) -> i32 {
        if self.vals.contains_key(&k) {
            self.keys.retain(|&x| x != k);
            self.keys.push_back(k);
            *self.vals.get(&k).unwrap()
        } else { -1 }
    }
    fn put(&mut self, k: i32, v: i32) {
        if self.vals.contains_key(&k) {
            self.keys.retain(|&x| x != k);
        } else if self.keys.len() == self.cap {
            let old = self.keys.pop_front().unwrap();
            self.vals.remove(&old);
        }
        self.keys.push_back(k);
        self.vals.insert(k, v);
    }
}
fn run_ops(ops: Vec<Op>, cap: usize) -> Vec<i32> {
    let mut lru = LruSim::new(cap);
    let mut out = Vec::new();
    for op in ops {
        match op {
            Op::Put(k, v) => lru.put(k, v),
            Op::Get(k) => out.push(lru.get(k)),
        }
    }
    out
}
fn main() {
    // LC 官方示例：capacity=2, put(1,1), put(2,2), get(1)=1, put(3,3)逐出2, get(2)=-1, put(4,4)逐出1, get(1)=-1, get(3)=3, get(4)=4
    let ops = vec![
        Op::Put(1, 1), Op::Put(2, 2), Op::Get(1), Op::Put(3, 3), Op::Get(2),
        Op::Put(4, 4), Op::Get(1), Op::Get(3), Op::Get(4),
    ];
    assert_eq!(run_ops(ops, 2), vec![1, -1, -1, 3, 4]);
    println!("PASS");
}
''',
"lua": '''local LruSim = {}
LruSim.__index = LruSim
function LruSim.new(cap) return setmetatable({cap = cap, keys = {}, vals = {}}, LruSim) end
function LruSim:get(k)
    if self.vals[k] ~= nil then
        for i, key in ipairs(self.keys) do
            if key == k then table.remove(self.keys, i) break end
        end
        self.keys[#self.keys + 1] = k
        return self.vals[k]
    end
    return -1
end
function LruSim:put(k, v)
    if self.vals[k] ~= nil then
        for i, key in ipairs(self.keys) do
            if key == k then table.remove(self.keys, i) break end
        end
    elseif #self.keys == self.cap then
        local old = table.remove(self.keys, 1)
        self.vals[old] = nil
    end
    self.keys[#self.keys + 1] = k
    self.vals[k] = v
end
local lru = LruSim.new(2)
lru:put(1, 1); lru:put(2, 2)
assert(lru:get(1) == 1)
lru:put(3, 3)
assert(lru:get(2) == -1)
lru:put(4, 4)
assert(lru:get(1) == -1)
assert(lru:get(3) == 3)
assert(lru:get(4) == 4)
print("PASS")
''',
"c": '''#include <stdio.h>
/* 简易 LRU：时间戳法（容量小，线性扫描） */
typedef struct { int cap, n; int keys[256]; int vals[256]; long stamp[256]; long clock_; } LruSim;
static void lru_init(LruSim *s, int cap) { s->cap = cap; s->n = 0; s->clock_ = 0; }
static int lru_find(LruSim *s, int k) {
    for (int i = 0; i < s->n; i++) if (s->keys[i] == k) return i;
    return -1;
}
static void lru_remove_idx(LruSim *s, int idx) {
    for (int i = idx; i + 1 < s->n; i++) { s->keys[i] = s->keys[i+1]; s->vals[i] = s->vals[i+1]; s->stamp[i] = s->stamp[i+1]; }
    s->n--;
}
static int lru_get(LruSim *s, int k) {
    int i = lru_find(s, k);
    if (i < 0) return -1;
    s->stamp[i] = ++s->clock_;
    return s->vals[i];
}
static void lru_put(LruSim *s, int k, int v) {
    int i = lru_find(s, k);
    if (i >= 0) { s->vals[i] = v; s->stamp[i] = ++s->clock_; return; }
    if (s->n == s->cap) {
        int oldest = 0;
        for (int j = 1; j < s->n; j++) if (s->stamp[j] < s->stamp[oldest]) oldest = j;
        lru_remove_idx(s, oldest);
    }
    s->keys[s->n] = k; s->vals[s->n] = v; s->stamp[s->n] = ++s->clock_; s->n++;
}
int main(void) {
    LruSim s;
    lru_init(&s, 2);
    lru_put(&s, 1, 1); lru_put(&s, 2, 2);
    if (lru_get(&s, 1) != 1) { printf("FAIL 1\\n"); return 1; }
    lru_put(&s, 3, 3);
    if (lru_get(&s, 2) != -1) { printf("FAIL 2\\n"); return 1; }
    lru_put(&s, 4, 4);
    if (lru_get(&s, 1) != -1) { printf("FAIL 3\\n"); return 1; }
    if (lru_get(&s, 3) != 3 || lru_get(&s, 4) != 4) { printf("FAIL 4\\n"); return 1; }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''#include <cassert>
#include <iostream>
#include <list>
#include <unordered_map>
struct LRUCache {
    int cap;
    std::list<std::pair<int, int>> items;
    std::unordered_map<int, std::list<std::pair<int, int>>::iterator> pos;
    explicit LRUCache(int capacity) : cap(capacity) {}
    int get(int key) {
        auto it = pos.find(key);
        if (it == pos.end()) return -1;
        items.splice(items.begin(), items, it->second);
        return it->second->second;
    }
    void put(int key, int value) {
        auto it = pos.find(key);
        if (it != pos.end()) {
            it->second->second = value;
            items.splice(items.begin(), items, it->second);
            return;
        }
        if (static_cast<int>(items.size()) == cap) {
            pos.erase(items.back().first);
            items.pop_back();
        }
        items.emplace_front(key, value);
        pos[key] = items.begin();
    }
};
int main() {
    LRUCache lru(2);
    lru.put(1, 1);
    lru.put(2, 2);
    assert(lru.get(1) == 1);
    lru.put(3, 3);
    assert(lru.get(2) == -1);
    lru.put(4, 4);
    assert(lru.get(1) == -1);
    assert(lru.get(3) == 3);
    assert(lru.get(4) == 4);
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''LruSim <- function(cap) {
  e <- new.env(parent = emptyenv())
  e$cap <- cap; e$keys <- integer(0); e$vals <- list()
  e$get <- function(k) {
    w <- match(k, e$keys)
    if (is.na(w)) return(-1L)
    e$keys <- c(e$keys[-w], e$keys[w])
    e$vals[[as.character(k)]]
  }
  e$put <- function(k, v) {
    w <- match(k, e$keys)
    if (!is.na(w)) {
      e$keys <- c(e$keys[-w], e$keys[w])
    } else if (length(e$keys) == e$cap) {
      old <- e$keys[1]
      e$keys <- e$keys[-1]
      e$vals[[as.character(old)]] <- NULL
    }
    e$keys <- c(e$keys, k)
    e$vals[[as.character(k)]] <- v
  }
  e
}
lru <- LruSim(2)
lru$put(1, 1); lru$put(2, 2)
stopifnot(lru$get(1) == 1)
lru$put(3, 3)
stopifnot(lru$get(2) == -1)
lru$put(4, 4)
stopifnot(lru$get(1) == -1, lru$get(3) == 3, lru$get(4) == 4)
cat("PASS\\n")
''',
"zig": '''const std = @import("std");
const LruSim = struct {
    cap: usize,
    keys: [256]i32,
    vals: [256]i32,
    stamp: [256]i64,
    n: usize,
    clock_: i64,
    fn init(cap: usize) LruSim {
        return .{ .cap = cap, .keys = undefined, .vals = undefined, .stamp = undefined, .n = 0, .clock_ = 0 };
    }
    fn find(self: *LruSim, k: i32) ?usize {
        for (0..self.n) |i| if (self.keys[i] == k) return i;
        return null;
    }
    fn removeIdx(self: *LruSim, idx: usize) void {
        var i = idx;
        while (i + 1 < self.n) : (i += 1) {
            self.keys[i] = self.keys[i + 1];
            self.vals[i] = self.vals[i + 1];
            self.stamp[i] = self.stamp[i + 1];
        }
        self.n -= 1;
    }
    fn get(self: *LruSim, k: i32) i32 {
        const i = self.find(k) orelse return -1;
        self.clock_ += 1;
        self.stamp[i] = self.clock_;
        return self.vals[i];
    }
    fn put(self: *LruSim, k: i32, v: i32) void {
        if (self.find(k)) |i| {
            self.vals[i] = v;
            self.clock_ += 1;
            self.stamp[i] = self.clock_;
            return;
        }
        if (self.n == self.cap) {
            var oldest: usize = 0;
            for (1..self.n) |j| {
            if (self.stamp[j] < self.stamp[oldest]) oldest = j;
        }
            self.removeIdx(oldest);
        }
        self.clock_ += 1;
        self.keys[self.n] = k;
        self.vals[self.n] = v;
        self.stamp[self.n] = self.clock_;
        self.n += 1;
    }
};
pub fn main() !void {
    var lru = LruSim.init(2);
    lru.put(1, 1);
    lru.put(2, 2);
    if (lru.get(1) != 1) return error.TestFailed;
    lru.put(3, 3);
    if (lru.get(2) != -1) return error.TestFailed;
    lru.put(4, 4);
    if (lru.get(1) != -1) return error.TestFailed;
    if (lru.get(3) != 3 or lru.get(4) != 4) return error.TestFailed;
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''class LruSim {
  final int cap;
  final List<int> keys = [];
  final Map<int, int> vals = {};
  LruSim(this.cap);
  int get(int k) {
    if (vals.containsKey(k)) {
      keys.remove(k);
      keys.add(k);
      return vals[k]!;
    }
    return -1;
  }
  void put(int k, int v) {
    if (vals.containsKey(k)) {
      keys.remove(k);
    } else if (keys.length == cap) {
      vals.remove(keys.removeAt(0));
    }
    keys.add(k);
    vals[k] = v;
  }
}
void main() {
  final lru = LruSim(2);
  lru.put(1, 1);
  lru.put(2, 2);
  if (lru.get(1) != 1) throw StateError('c1');
  lru.put(3, 3);
  if (lru.get(2) != -1) throw StateError('c2');
  lru.put(4, 4);
  if (lru.get(1) != -1) throw StateError('c3');
  if (lru.get(3) != 3 || lru.get(4) != 4) throw StateError('c4');
  print('PASS');
}
''',
}

A460 = {
"rust": '''#[derive(Clone)]
enum Op460 { Put(i32, i32), Get(i32) }
fn lfu_run(ops: Vec<Op460>, cap: usize) -> Vec<i32> {
    // 频率最小+最久未用优先：简单 O(n) 模拟
    use std::collections::HashMap;
    let mut vals: HashMap<i32, i32> = HashMap::new();
    let mut freq: HashMap<i32, i64> = HashMap::new();
    let mut stamp: HashMap<i32, i64> = HashMap::new();
    let mut clock: i64 = 0;
    let mut out = Vec::new();
    for op in ops {
        clock += 1;
        match op {
            Op460::Get(k) => {
                if vals.contains_key(&k) {
                    *freq.get_mut(&k).unwrap() += 1;
                    stamp.insert(k, clock);
                    out.push(*vals.get(&k).unwrap());
                } else { out.push(-1); }
            }
            Op460::Put(k, v) => {
                if vals.contains_key(&k) {
                    vals.insert(k, v);
                    *freq.get_mut(&k).unwrap() += 1;
                    stamp.insert(k, clock);
                } else {
                    if cap > 0 && vals.len() == cap {
                        let mut evict: Option<i32> = None;
                        let mut best_f = i64::MAX;
                        let mut best_s = i64::MAX;
                        for key in vals.keys() {
                            let f = freq[key];
                            let s = stamp[key];
                            if f < best_f || (f == best_f && s < best_s) {
                                best_f = f; best_s = s; evict = Some(*key);
                            }
                        }
                        if let Some(e) = evict {
                            vals.remove(&e); freq.remove(&e); stamp.remove(&e);
                        }
                    }
                    if cap > 0 {
                        vals.insert(k, v);
                        freq.insert(k, 1);
                        stamp.insert(k, clock);
                    }
                }
            }
        }
    }
    out
}
fn main() {
    // LC 示例：capacity=2, put(1,1), put(2,2), get(1)=1, put(3,3)逐出2, get(2)=-1, get(3)=3, put(4,4)逐出1, get(1)=-1, get(3)=3, get(4)=4
    let ops = vec![
        Op460::Put(1, 1), Op460::Put(2, 2), Op460::Get(1), Op460::Put(3, 3), Op460::Get(2),
        Op460::Get(3), Op460::Put(4, 4), Op460::Get(1), Op460::Get(3), Op460::Get(4),
    ];
    assert_eq!(lfu_run(ops, 2), vec![1, -1, 3, -1, 3, 4]);
    println!("PASS");
}
''',
"lua": '''local LfuSim = {}
LfuSim.__index = LfuSim
function LfuSim.new(cap) return setmetatable({cap = cap, vals = {}, freq = {}, stamp = {}, clock_ = 0}, LfuSim) end
function LfuSim:get(k)
    self.clock_ = self.clock_ + 1
    if self.vals[k] ~= nil then
        self.freq[k] = self.freq[k] + 1
        self.stamp[k] = self.clock_
        return self.vals[k]
    end
    return -1
end
function LfuSim:put(k, v)
    self.clock_ = self.clock_ + 1
    if self.vals[k] ~= nil then
        self.vals[k] = v
        self.freq[k] = self.freq[k] + 1
        self.stamp[k] = self.clock_
        return
    end
    local n = 0
    for _ in pairs(self.vals) do n = n + 1 end
    if self.cap > 0 and n == self.cap then
        local ek, ef, es = nil, math.huge, math.huge
        for key, _ in pairs(self.vals) do
            if self.freq[key] < ef or (self.freq[key] == ef and self.stamp[key] < es) then
                ef = self.freq[key]; es = self.stamp[key]; ek = key
            end
        end
        if ek then self.vals[ek] = nil; self.freq[ek] = nil; self.stamp[ek] = nil end
    end
    if self.cap > 0 then
        self.vals[k] = v; self.freq[k] = 1; self.stamp[k] = self.clock_
    end
end
local lfu = LfuSim.new(2)
lfu:put(1, 1); lfu:put(2, 2)
assert(lfu:get(1) == 1)
lfu:put(3, 3)
assert(lfu:get(2) == -1)
assert(lfu:get(3) == 3)
lfu:put(4, 4)
assert(lfu:get(1) == -1)
assert(lfu:get(3) == 3)
assert(lfu:get(4) == 4)
print("PASS")
''',
"c": '''#include <stdio.h>
typedef struct { int cap, n; int keys[256]; int vals[256]; int freq[256]; long stamp[256]; long clock_; } LfuSim;
static void lfu_init(LfuSim *s, int cap) { s->cap = cap; s->n = 0; s->clock_ = 0; }
static int lfu_find(LfuSim *s, int k) { for (int i = 0; i < s->n; i++) if (s->keys[i] == k) return i; return -1; }
static void lfu_remove_idx(LfuSim *s, int idx) {
    for (int i = idx; i + 1 < s->n; i++) { s->keys[i]=s->keys[i+1]; s->vals[i]=s->vals[i+1]; s->freq[i]=s->freq[i+1]; s->stamp[i]=s->stamp[i+1]; }
    s->n--;
}
static int lfu_get(LfuSim *s, int k) {
    int i = lfu_find(s, k);
    s->clock_++;
    if (i < 0) return -1;
    s->freq[i]++;
    s->stamp[i] = s->clock_;
    return s->vals[i];
}
static void lfu_put(LfuSim *s, int k, int v) {
    s->clock_++;
    int i = lfu_find(s, k);
    if (i >= 0) { s->vals[i] = v; s->freq[i]++; s->stamp[i] = s->clock_; return; }
    if (s->cap == 0) return;
    if (s->n == s->cap) {
        int ev = 0;
        for (int j = 1; j < s->n; j++) {
            if (s->freq[j] < s->freq[ev] || (s->freq[j] == s->freq[ev] && s->stamp[j] < s->stamp[ev])) ev = j;
        }
        lfu_remove_idx(s, ev);
    }
    s->keys[s->n] = k; s->vals[s->n] = v; s->freq[s->n] = 1; s->stamp[s->n] = s->clock_; s->n++;
}
int main(void) {
    LfuSim s;
    lfu_init(&s, 2);
    lfu_put(&s, 1, 1); lfu_put(&s, 2, 2);
    if (lfu_get(&s, 1) != 1) { printf("FAIL 1\\n"); return 1; }
    lfu_put(&s, 3, 3);
    if (lfu_get(&s, 2) != -1) { printf("FAIL 2\\n"); return 1; }
    if (lfu_get(&s, 3) != 3) { printf("FAIL 3\\n"); return 1; }
    lfu_put(&s, 4, 4);
    if (lfu_get(&s, 1) != -1) { printf("FAIL 4\\n"); return 1; }
    if (lfu_get(&s, 3) != 3 || lfu_get(&s, 4) != 4) { printf("FAIL 5\\n"); return 1; }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''#include <cassert>
#include <iostream>
#include <unordered_map>
struct LFUCacheSim {
    int cap;
    std::unordered_map<int, int> vals, freq;
    std::unordered_map<int, long long> stamp;
    long long clock_ = 0;
    explicit LFUCacheSim(int capacity) : cap(capacity) {}
    int get(int key) {
        ++clock_;
        auto it = vals.find(key);
        if (it == vals.end()) return -1;
        ++freq[key];
        stamp[key] = clock_;
        return it->second;
    }
    void put(int key, int value) {
        ++clock_;
        auto it = vals.find(key);
        if (it != vals.end()) {
            it->second = value;
            ++freq[key];
            stamp[key] = clock_;
            return;
        }
        if (cap == 0) return;
        if (static_cast<int>(vals.size()) == cap) {
            int evict = -1;
            long long bestF = -1, bestS = -1;
            for (auto &[k, v] : vals) {
                long long f = freq[k], s = stamp[k];
                if (evict == -1 || f < bestF || (f == bestF && s < bestS)) {
                    evict = k; bestF = f; bestS = s;
                }
            }
            vals.erase(evict); freq.erase(evict); stamp.erase(evict);
        }
        vals[key] = value;
        freq[key] = 1;
        stamp[key] = clock_;
    }
};
int main() {
    LFUCacheSim lfu(2);
    lfu.put(1, 1);
    lfu.put(2, 2);
    assert(lfu.get(1) == 1);
    lfu.put(3, 3);
    assert(lfu.get(2) == -1);
    assert(lfu.get(3) == 3);
    lfu.put(4, 4);
    assert(lfu.get(1) == -1);
    assert(lfu.get(3) == 3);
    assert(lfu.get(4) == 4);
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''LfuSim <- function(cap) {
  e <- new.env(parent = emptyenv())
  e$cap <- cap; e$vals <- list(); e$freq <- list(); e$stamp <- list(); e$clock_ <- 0L
  e$get <- function(k) {
    e$clock_ <<- e$clock_ + 1L
    key <- as.character(k)
    if (!is.null(e$vals[[key]])) {
      e$freq[[key]] <<- e$freq[[key]] + 1L
      e$stamp[[key]] <<- e$clock_
      e$vals[[key]]
    } else -1L
  }
  e$put <- function(k, v) {
    e$clock_ <<- e$clock_ + 1L
    key <- as.character(k)
    if (!is.null(e$vals[[key]])) {
      e$vals[[key]] <<- v
      e$freq[[key]] <<- e$freq[[key]] + 1L
      e$stamp[[key]] <<- e$clock_
      return(invisible(NULL))
    }
    if (e$cap == 0) return(invisible(NULL))
    if (length(e$vals) == e$cap) {
      ek <- NULL; ef <- .Machine$integer.max; es <- .Machine$integer.max
      for (key2 in names(e$vals)) {
        if (e$freq[[key2]] < ef || (e$freq[[key2]] == ef && e$stamp[[key2]] < es)) {
          ef <- e$freq[[key2]]; es <- e$stamp[[key2]]; ek <- key2
        }
      }
      e$vals[[ek]] <<- NULL; e$freq[[ek]] <<- NULL; e$stamp[[ek]] <<- NULL
    }
    e$vals[[key]] <<- v; e$freq[[key]] <<- 1L; e$stamp[[key]] <<- e$clock_
  }
  e
}
lfu <- LfuSim(2)
lfu$put(1, 1); lfu$put(2, 2)
stopifnot(lfu$get(1) == 1)
lfu$put(3, 3)
stopifnot(lfu$get(2) == -1, lfu$get(3) == 3)
lfu$put(4, 4)
stopifnot(lfu$get(1) == -1, lfu$get(3) == 3, lfu$get(4) == 4)
cat("PASS\\n")
''',
"zig": '''const std = @import("std");
const LfuSim = struct {
    cap: usize,
    keys: [256]i32,
    vals: [256]i32,
    freq: [256]i64,
    stamp: [256]i64,
    n: usize,
    clock_: i64,
    fn init(cap: usize) LfuSim {
        return .{ .cap = cap, .keys = undefined, .vals = undefined, .freq = undefined, .stamp = undefined, .n = 0, .clock_ = 0 };
    }
    fn find(self: *LfuSim, k: i32) ?usize {
        for (0..self.n) |i| if (self.keys[i] == k) return i;
        return null;
    }
    fn removeIdx(self: *LfuSim, idx: usize) void {
        var i = idx;
        while (i + 1 < self.n) : (i += 1) {
            self.keys[i] = self.keys[i + 1];
            self.vals[i] = self.vals[i + 1];
            self.freq[i] = self.freq[i + 1];
            self.stamp[i] = self.stamp[i + 1];
        }
        self.n -= 1;
    }
    fn get(self: *LfuSim, k: i32) i32 {
        self.clock_ += 1;
        const i = self.find(k) orelse return -1;
        self.freq[i] += 1;
        self.stamp[i] = self.clock_;
        return self.vals[i];
    }
    fn put(self: *LfuSim, k: i32, v: i32) void {
        self.clock_ += 1;
        if (self.find(k)) |i| {
            self.vals[i] = v;
            self.freq[i] += 1;
            self.stamp[i] = self.clock_;
            return;
        }
        if (self.cap == 0) return;
        if (self.n == self.cap) {
            var ev: usize = 0;
            for (1..self.n) |j| {
                if (self.freq[j] < self.freq[ev] or (self.freq[j] == self.freq[ev] and self.stamp[j] < self.stamp[ev])) ev = j;
            }
            self.removeIdx(ev);
        }
        self.keys[self.n] = k;
        self.vals[self.n] = v;
        self.freq[self.n] = 1;
        self.stamp[self.n] = self.clock_;
        self.n += 1;
    }
};
pub fn main() !void {
    var lfu = LfuSim.init(2);
    lfu.put(1, 1);
    lfu.put(2, 2);
    if (lfu.get(1) != 1) return error.TestFailed;
    lfu.put(3, 3);
    if (lfu.get(2) != -1) return error.TestFailed;
    if (lfu.get(3) != 3) return error.TestFailed;
    lfu.put(4, 4);
    if (lfu.get(1) != -1) return error.TestFailed;
    if (lfu.get(3) != 3 or lfu.get(4) != 4) return error.TestFailed;
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''class LfuSim {
  final int cap;
  final Map<int, int> vals = {};
  final Map<int, int> freq = {};
  final Map<int, int> stamp = {};
  int clock = 0;
  LfuSim(this.cap);
  int get(int k) {
    clock++;
    if (vals.containsKey(k)) {
      freq[k] = freq[k]! + 1;
      stamp[k] = clock;
      return vals[k]!;
    }
    return -1;
  }
  void put(int k, int v) {
    clock++;
    if (vals.containsKey(k)) {
      vals[k] = v;
      freq[k] = freq[k]! + 1;
      stamp[k] = clock;
      return;
    }
    if (cap == 0) return;
    if (vals.length == cap) {
      var evict = -1, bestF = -1, bestS = -1;
      for (final k2 in vals.keys) {
        final f = freq[k2]!, s = stamp[k2]!;
        if (evict == -1 || f < bestF || (f == bestF && s < bestS)) {
          evict = k2;
          bestF = f;
          bestS = s;
        }
      }
      vals.remove(evict);
      freq.remove(evict);
      stamp.remove(evict);
    }
    vals[k] = v;
    freq[k] = 1;
    stamp[k] = clock;
  }
}
void main() {
  final lfu = LfuSim(2);
  lfu.put(1, 1);
  lfu.put(2, 2);
  if (lfu.get(1) != 1) throw StateError('c1');
  lfu.put(3, 3);
  if (lfu.get(2) != -1) throw StateError('c2');
  if (lfu.get(3) != 3) throw StateError('c3');
  lfu.put(4, 4);
  if (lfu.get(1) != -1) throw StateError('c4');
  if (lfu.get(3) != 3 || lfu.get(4) != 4) throw StateError('c5');
  print('PASS');
}
''',
}

A707 = {
"rust": '''#[derive(Clone)]
enum Op707 { AddAtHead(i32), AddAtTail(i32), AddAtIndex(i32, i32), Get(i32), DeleteAtIndex(i32) }
fn my_linked_list_run(ops: Vec<Op707>) -> Vec<i32> {
    let mut v: Vec<i32> = Vec::new();
    let mut out = Vec::new();
    for op in ops {
        match op {
            Op707::AddAtHead(x) => v.insert(0, x),
            Op707::AddAtTail(x) => v.push(x),
            Op707::AddAtIndex(i, x) => {
                let idx = i.max(0) as usize;
                if idx <= v.len() { v.insert(idx, x); }
            }
            Op707::Get(i) => {
                if i >= 0 && (i as usize) < v.len() { out.push(v[i as usize]); } else { out.push(-1); }
            }
            Op707::DeleteAtIndex(i) => {
                if i >= 0 && (i as usize) < v.len() { v.remove(i as usize); }
            }
        }
    }
    out
}
fn main() {
    // LC 官方：addAtHead(1), addAtTail(3), addAtIndex(1,2)→[1,2,3], get(1)=2, deleteAtIndex(1)→[1,3], get(1)=3
    let ops = vec![
        Op707::AddAtHead(1), Op707::AddAtTail(3), Op707::AddAtIndex(1, 2), Op707::Get(1),
        Op707::DeleteAtIndex(1), Op707::Get(1),
    ];
    assert_eq!(my_linked_list_run(ops), vec![2, 3]);
    println!("PASS");
}
''',
"lua": '''local MyList = {}
MyList.__index = MyList
function MyList.new() return setmetatable({items = {}}, MyList) end
function MyList:addAtHead(x) table.insert(self.items, 1, x) end
function MyList:addAtTail(x) self.items[#self.items + 1] = x end
function MyList:addAtIndex(i, x)
    if i < 0 then i = 0 end
    if i <= #self.items then table.insert(self.items, i + 1, x) end
end
function MyList:get(i)
    if i >= 0 and i < #self.items then return self.items[i + 1] end
    return -1
end
function MyList:deleteAtIndex(i)
    if i >= 0 and i < #self.items then table.remove(self.items, i + 1) end
end
local l = MyList.new()
l:addAtHead(1)
l:addAtTail(3)
l:addAtIndex(1, 2)
assert(l:get(1) == 2)
l:deleteAtIndex(1)
assert(l:get(1) == 3)
print("PASS")
''',
"c": '''#include <stdio.h>
typedef struct { int items[4096]; int n; } MyList;
static void ml_init(MyList *l) { l->n = 0; }
static void ml_add_head(MyList *l, int x) {
    for (int i = l->n; i > 0; i--) l->items[i] = l->items[i - 1];
    l->items[0] = x;
    l->n++;
}
static void ml_add_tail(MyList *l, int x) { l->items[l->n++] = x; }
static void ml_add_at(MyList *l, int idx, int x) {
    if (idx < 0) idx = 0;
    if (idx > l->n) return;
    for (int i = l->n; i > idx; i--) l->items[i] = l->items[i - 1];
    l->items[idx] = x;
    l->n++;
}
static int ml_get(MyList *l, int idx) {
    if (idx < 0 || idx >= l->n) return -1;
    return l->items[idx];
}
static void ml_del(MyList *l, int idx) {
    if (idx < 0 || idx >= l->n) return;
    for (int i = idx; i + 1 < l->n; i++) l->items[i] = l->items[i + 1];
    l->n--;
}
int main(void) {
    MyList l;
    ml_init(&l);
    ml_add_head(&l, 1);
    ml_add_tail(&l, 3);
    ml_add_at(&l, 1, 2);
    if (ml_get(&l, 1) != 2) { printf("FAIL 1\\n"); return 1; }
    ml_del(&l, 1);
    if (ml_get(&l, 1) != 3) { printf("FAIL 2\\n"); return 1; }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''#include <cassert>
#include <iostream>
#include <vector>
struct MyLinkedList {
    std::vector<int> items;
    void addAtHead(int x) { items.insert(items.begin(), x); }
    void addAtTail(int x) { items.push_back(x); }
    void addAtIndex(int idx, int x) {
        if (idx < 0) idx = 0;
        if (idx > static_cast<int>(items.size())) return;
        items.insert(items.begin() + idx, x);
    }
    int get(int idx) {
        if (idx < 0 || idx >= static_cast<int>(items.size())) return -1;
        return items[idx];
    }
    void deleteAtIndex(int idx) {
        if (idx < 0 || idx >= static_cast<int>(items.size())) return;
        items.erase(items.begin() + idx);
    }
};
int main() {
    MyLinkedList l;
    l.addAtHead(1);
    l.addAtTail(3);
    l.addAtIndex(1, 2);
    assert(l.get(1) == 2);
    l.deleteAtIndex(1);
    assert(l.get(1) == 3);
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''MyList <- function() {
  e <- new.env(parent = emptyenv())
  e$items <- integer(0)
  e$addAtHead <- function(x) e$items <<- c(x, e$items)
  e$addAtTail <- function(x) e$items <<- c(e$items, x)
  e$addAtIndex <- function(idx, x) {
    if (idx < 0) idx <- 1
    if (idx > length(e$items) + 1) return(invisible(NULL))
    e$items <<- append(e$items, x, after = idx)
  }
  e$get <- function(idx) {
    if (idx < 0 || idx >= length(e$items)) return(-1L)
    e$items[idx + 1]
  }
  e$deleteAtIndex <- function(idx) {
    if (idx < 0 || idx >= length(e$items)) return(invisible(NULL))
    e$items <<- e$items[-(idx + 1)]
  }
  e
}
l <- MyList()
l$addAtHead(1)
l$addAtTail(3)
l$addAtIndex(1, 2)
stopifnot(l$get(1) == 2)
l$deleteAtIndex(1)
stopifnot(l$get(1) == 3)
cat("PASS\\n")
''',
"zig": '''const std = @import("std");
const MyList = struct {
    items: [4096]i32,
    n: usize,
    fn init() MyList {
        return .{ .items = undefined, .n = 0 };
    }
    fn addAtHead(self: *MyList, x: i32) void {
        var i: usize = self.n;
        while (i > 0) : (i -= 1) self.items[i] = self.items[i - 1];
        self.items[0] = x;
        self.n += 1;
    }
    fn addAtTail(self: *MyList, x: i32) void {
        self.items[self.n] = x;
        self.n += 1;
    }
    fn addAtIndex(self: *MyList, idx: i32, x: i32) void {
        var idxv = idx;
        if (idxv < 0) idxv = 0;
        const u: usize = @intCast(idxv);
        if (u > self.n) return;
        var i: usize = self.n;
        while (i > u) : (i -= 1) self.items[i] = self.items[i - 1];
        self.items[u] = x;
        self.n += 1;
    }
    fn get(self: *MyList, idx: i32) i32 {
        if (idx < 0 or idx >= @as(i32, @intCast(self.n))) return -1;
        return self.items[@intCast(idx)];
    }
    fn deleteAtIndex(self: *MyList, idx: i32) void {
        if (idx < 0 or idx >= @as(i32, @intCast(self.n))) return;
        var i: usize = @intCast(idx);
        while (i + 1 < self.n) : (i += 1) self.items[i] = self.items[i + 1];
        self.n -= 1;
    }
};
pub fn main() !void {
    var l = MyList.init();
    l.addAtHead(1);
    l.addAtTail(3);
    l.addAtIndex(1, 2);
    if (l.get(1) != 2) return error.TestFailed;
    l.deleteAtIndex(1);
    if (l.get(1) != 3) return error.TestFailed;
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''class MyList {
  final List<int> items = [];
  void addAtHead(int x) => items.insert(0, x);
  void addAtTail(int x) => items.add(x);
  void addAtIndex(int idx, int x) {
    if (idx < 0) idx = 0;
    if (idx > items.length) return;
    items.insert(idx, x);
  }
  int get(int idx) {
    if (idx < 0 || idx >= items.length) return -1;
    return items[idx];
  }
  void deleteAtIndex(int idx) {
    if (idx < 0 || idx >= items.length) return;
    items.removeAt(idx);
  }
}
void main() {
  final l = MyList();
  l.addAtHead(1);
  l.addAtTail(3);
  l.addAtIndex(1, 2);
  if (l.get(1) != 2) throw StateError('c1');
  l.deleteAtIndex(1);
  if (l.get(1) != 3) throw StateError('c2');
  print('PASS');
}
''',
}

PROBS = [
    ("lc_2_两数相加", A2, "LeetCode 2. 两数相加"),
    ("lc_92_反转链表_ii", A92, "LeetCode 92. 反转链表II"),
    ("lc_234_回文链表", A234, "LeetCode 234. 回文链表"),
    ("lc_148_排序链表", A148, "LeetCode 148. 排序链表"),
    ("lc_146_lru_缓存", A146, "LeetCode 146. LRU缓存"),
    ("lc_460_lfu_缓存", A460, "LeetCode 460. LFU缓存"),
    ("lc_707_设计链表", A707, "LeetCode 707. 设计链表"),
]
count = 0
for prob, algo, title in PROBS:
    bid = B[prob.split("_")[1]]
    ts_dir = f"/Users/Wang/Code/webfault-ai/dsa/ts/linked_list/{prob}"
    sols = sorted(f[:-3] for f in os.listdir(ts_dir) if f.startswith("solution_") and f.endswith(".ts"))
    for lang in EXT:
        ext = EXT[lang]
        for sol in sols:
            n = sol.replace("solution_", "").split("_")[0]
            head = head_comment(lang, bid, f"{title} — {LANGNAME[lang]} 版（方案{n}）")
            emit(lang, f"linked_list/{prob}/{sol}.{ext}", head + "\n" + algo[lang])
            count += 1
print(f"emitted {count} files")
