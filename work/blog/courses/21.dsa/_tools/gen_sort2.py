#!/usr/bin/env python3
# gen_sort2.py — sort 第二批：lc_41/lc_164/lc_21 × 7语言
import sys, os; sys.path.insert(0, "/Users/Wang/Code/github/web-x-blog/work/blog/courses/21.dsa/_tools")
from langlib import emit, head_comment, EXT

B = {"41": "134066015", "164": "135003383", "21": "133594090"}
LANGNAME = {"rust": "Rust", "lua": "Lua", "c": "C", "cpp": "C++", "r": "R", "zig": "Zig", "dart": "Dart"}

A41 = {
"rust": '''fn first_missing_positive(nums: Vec<i32>) -> i32 {
    if nums.is_empty() { return 1; }
    let mut pos: Vec<i32> = nums.iter().cloned().filter(|&x| x > 0).collect();
    if pos.is_empty() { return 1; }
    pos.sort();
    if pos[0] != 1 { return 1; }
    let n = pos.len();
    for i in 0..n - 1 {
        if pos[i + 1] - pos[i] > 1 { return pos[i] + 1; }
    }
    pos[n - 1] + 1
}
fn main() {
    assert_eq!(first_missing_positive(vec![1, 2, 0]), 3);
    assert_eq!(first_missing_positive(vec![3, 4, -1, 1]), 2);
    assert_eq!(first_missing_positive(vec![7, 8, 9, 11, 12]), 1);
    assert_eq!(first_missing_positive(vec![]), 1);
    println!("PASS");
}
''',
"lua": '''local function first_missing_positive(nums)
    if #nums == 0 then return 1 end
    local pos = {}
    for _, v in ipairs(nums) do
        if v > 0 then pos[#pos + 1] = v end
    end
    if #pos == 0 then return 1 end
    table.sort(pos)
    if pos[1] ~= 1 then return 1 end
    local n = #pos
    for i = 1, n - 1 do
        if pos[i + 1] - pos[i] > 1 then return pos[i] + 1 end
    end
    return pos[n] + 1
end
assert(first_missing_positive({1, 2, 0}) == 3)
assert(first_missing_positive({3, 4, -1, 1}) == 2)
assert(first_missing_positive({7, 8, 9, 11, 12}) == 1)
assert(first_missing_positive({}) == 1)
print("PASS")
''',
"c": '''#include <stdio.h>
#include <stdlib.h>
static int cmp_int(const void *a, const void *b) { return *(const int *)a - *(const int *)b; }
static int first_missing_positive(const int *nums, int n) {
    if (n == 0) return 1;
    int pos[4096], pn = 0;
    for (int i = 0; i < n; i++) if (nums[i] > 0) pos[pn++] = nums[i];
    if (pn == 0) return 1;
    qsort(pos, pn, sizeof(int), cmp_int);
    if (pos[0] != 1) return 1;
    for (int i = 0; i < pn - 1; i++) {
        if (pos[i + 1] - pos[i] > 1) return pos[i] + 1;
    }
    return pos[pn - 1] + 1;
}
int main(void) {
    if (first_missing_positive((int[]){1,2,0}, 3) != 3) { printf("FAIL 1\\n"); return 1; }
    if (first_missing_positive((int[]){3,4,-1,1}, 4) != 2) { printf("FAIL 2\\n"); return 1; }
    if (first_missing_positive((int[]){7,8,9,11,12}, 5) != 1) { printf("FAIL 3\\n"); return 1; }
    if (first_missing_positive(NULL, 0) != 1) { printf("FAIL 4\\n"); return 1; }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''#include <algorithm>
#include <cassert>
#include <iostream>
#include <vector>
static int firstMissingPositive(const std::vector<int> &nums) {
    if (nums.empty()) return 1;
    std::vector<int> pos;
    for (int v : nums) if (v > 0) pos.push_back(v);
    if (pos.empty()) return 1;
    std::sort(pos.begin(), pos.end());
    if (pos[0] != 1) return 1;
    for (size_t i = 0; i + 1 < pos.size(); ++i) {
        if (pos[i + 1] - pos[i] > 1) return pos[i] + 1;
    }
    return pos.back() + 1;
}
int main() {
    assert(firstMissingPositive({1, 2, 0}) == 3);
    assert(firstMissingPositive({3, 4, -1, 1}) == 2);
    assert(firstMissingPositive({7, 8, 9, 11, 12}) == 1);
    assert(firstMissingPositive({}) == 1);
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''first_missing_positive <- function(nums) {
  if (length(nums) == 0L) return(1L)
  pos <- sort(nums[nums > 0])
  if (length(pos) == 0L) return(1L)
  if (pos[1] != 1) return(1L)
  n <- length(pos)
  for (i in 1:(n - 1)) {
    if (pos[i + 1] - pos[i] > 1) return(pos[i] + 1)
  }
  pos[n] + 1
}
stopifnot(first_missing_positive(c(1, 2, 0)) == 3)
stopifnot(first_missing_positive(c(3, 4, -1, 1)) == 2)
stopifnot(first_missing_positive(c(7, 8, 9, 11, 12)) == 1)
stopifnot(first_missing_positive(integer(0)) == 1)
cat("PASS\\n")
''',
"zig": '''const std = @import("std");
fn firstMissingPositive(nums: []const i32, alloc: std.mem.Allocator) i32 {
    if (nums.len == 0) return 1;
    var pos = std.ArrayList(i32).init(alloc);
    for (nums) |v| if (v > 0) pos.append(v) catch unreachable;
    if (pos.items.len == 0) return 1;
    std.sort.pdq(i32, pos.items, {}, std.sort.asc(i32));
    if (pos.items[0] != 1) return 1;
    const n = pos.items.len;
    for (0..n - 1) |i| {
        if (pos.items[i + 1] - pos.items[i] > 1) return pos.items[i] + 1;
    }
    return pos.items[n - 1] + 1;
}
pub fn main() !void {
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();
    const alloc = arena.allocator();
    if (firstMissingPositive(&[_]i32{ 1, 2, 0 }, alloc) != 3) return error.TestFailed;
    if (firstMissingPositive(&[_]i32{ 3, 4, -1, 1 }, alloc) != 2) return error.TestFailed;
    if (firstMissingPositive(&[_]i32{ 7, 8, 9, 11, 12 }, alloc) != 1) return error.TestFailed;
    if (firstMissingPositive(&[_]i32{}, alloc) != 1) return error.TestFailed;
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''int firstMissingPositive(List<int> nums) {
  if (nums.isEmpty) return 1;
  final pos = nums.where((v) => v > 0).toList()..sort();
  if (pos.isEmpty) return 1;
  if (pos[0] != 1) return 1;
  final n = pos.length;
  for (var i = 0; i < n - 1; i++) {
    if (pos[i + 1] - pos[i] > 1) return pos[i] + 1;
  }
  return pos[n - 1] + 1;
}
void main() {
  if (firstMissingPositive([1, 2, 0]) != 3) throw StateError('c1');
  if (firstMissingPositive([3, 4, -1, 1]) != 2) throw StateError('c2');
  if (firstMissingPositive([7, 8, 9, 11, 12]) != 1) throw StateError('c3');
  if (firstMissingPositive([]) != 1) throw StateError('c4');
  print('PASS');
}
''',
}

A164 = {
"rust": '''fn maximum_gap(nums: Vec<i32>) -> i32 {
    let n = nums.len();
    if n < 2 { return 0; }
    let min_val = *nums.iter().min().unwrap();
    let max_val = *nums.iter().max().unwrap();
    if min_val == max_val { return 0; }
    let d = std::cmp::max(1, (max_val - min_val) / (n as i32 - 1));
    let bucket_size = ((max_val - min_val) / d) as usize + 1;
    let mut buckets: Vec<(i32, i32)> = vec![(-1, -1); bucket_size];
    for &x in &nums {
        let idx = ((x - min_val) / d) as usize;
        if buckets[idx].0 == -1 { buckets[idx] = (x, x); }
        else {
            buckets[idx].0 = buckets[idx].0.min(x);
            buckets[idx].1 = buckets[idx].1.max(x);
        }
    }
    let mut ans = 0;
    let mut prev_max = -1i32;
    for b in buckets {
        if b.0 == -1 { continue; }
        if prev_max != -1 { ans = ans.max(b.0 - prev_max); }
        prev_max = b.1;
    }
    ans
}
fn main() {
    assert_eq!(maximum_gap(vec![1, 2, 3]), 1);
    assert_eq!(maximum_gap(vec![3, 6, 9, 1]), 3);
    assert_eq!(maximum_gap(vec![10]), 0);
    assert_eq!(maximum_gap(vec![]), 0);
    assert_eq!(maximum_gap(vec![1, 10000000]), 9999999);
    println!("PASS");
}
''',
"lua": '''local function maximum_gap(nums)
    local n = #nums
    if n < 2 then return 0 end
    local min_val, max_val = math.huge, -math.huge
    for _, x in ipairs(nums) do
        if x < min_val then min_val = x end
        if x > max_val then max_val = x end
    end
    if min_val == max_val then return 0 end
    local d = math.max(1, math.floor((max_val - min_val) / (n - 1)))
    local bucket_size = math.floor((max_val - min_val) / d) + 1
    local buckets = {}
    for i = 1, bucket_size do buckets[i] = {-1, -1} end
    for _, x in ipairs(nums) do
        local idx = math.floor((x - min_val) / d) + 1
        if buckets[idx][1] == -1 then buckets[idx] = {x, x}
        else
            if x < buckets[idx][1] then buckets[idx][1] = x end
            if x > buckets[idx][2] then buckets[idx][2] = x end
        end
    end
    local ans, prev_max = 0, -1
    for _, b in ipairs(buckets) do
        if b[1] ~= -1 then
            if prev_max ~= -1 and b[1] - prev_max > ans then ans = b[1] - prev_max end
            prev_max = b[2]
        end
    end
    return ans
end
assert(maximum_gap({1, 2, 3}) == 1)
assert(maximum_gap({3, 6, 9, 1}) == 3)
assert(maximum_gap({10}) == 0)
assert(maximum_gap({}) == 0)
assert(maximum_gap({1, 10000000}) == 9999999)
print("PASS")
''',
"c": '''#include <stdio.h>
#include <stdlib.h>
static int maximum_gap(const int *nums, int n) {
    if (n < 2) return 0;
    int min_val = nums[0], max_val = nums[0];
    for (int i = 1; i < n; i++) {
        if (nums[i] < min_val) min_val = nums[i];
        if (nums[i] > max_val) max_val = nums[i];
    }
    if (min_val == max_val) return 0;
    int d = (max_val - min_val) / (n - 1);
    if (d < 1) d = 1;
    int bucket_size = (max_val - min_val) / d + 1;
    int (*buckets)[2] = malloc(sizeof(int) * 2 * bucket_size);
    for (int i = 0; i < bucket_size; i++) { buckets[i][0] = -1; buckets[i][1] = -1; }
    for (int i = 0; i < n; i++) {
        int idx = (nums[i] - min_val) / d;
        if (buckets[idx][0] == -1) { buckets[idx][0] = nums[i]; buckets[idx][1] = nums[i]; }
        else {
            if (nums[i] < buckets[idx][0]) buckets[idx][0] = nums[i];
            if (nums[i] > buckets[idx][1]) buckets[idx][1] = nums[i];
        }
    }
    int ans = 0, prev_max = -1;
    for (int i = 0; i < bucket_size; i++) {
        if (buckets[i][0] == -1) continue;
        if (prev_max != -1 && buckets[i][0] - prev_max > ans) ans = buckets[i][0] - prev_max;
        prev_max = buckets[i][1];
    }
    free(buckets);
    return ans;
}
int main(void) {
    if (maximum_gap((int[]){1,2,3}, 3) != 1) { printf("FAIL 1\\n"); return 1; }
    if (maximum_gap((int[]){3,6,9,1}, 4) != 3) { printf("FAIL 2\\n"); return 1; }
    if (maximum_gap((int[]){10}, 1) != 0) { printf("FAIL 3\\n"); return 1; }
    if (maximum_gap(NULL, 0) != 0) { printf("FAIL 4\\n"); return 1; }
    if (maximum_gap((int[]){1,10000000}, 2) != 9999999) { printf("FAIL 5\\n"); return 1; }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''#include <cassert>
#include <iostream>
#include <vector>
static int maximumGap(const std::vector<int> &nums) {
    int n = static_cast<int>(nums.size());
    if (n < 2) return 0;
    int minVal = nums[0], maxVal = nums[0];
    for (int v : nums) {
        minVal = std::min(minVal, v);
        maxVal = std::max(maxVal, v);
    }
    if (minVal == maxVal) return 0;
    int d = std::max(1, (maxVal - minVal) / (n - 1));
    int bucketSize = (maxVal - minVal) / d + 1;
    std::vector<std::pair<int, int>> buckets(bucketSize, {-1, -1});
    for (int v : nums) {
        int idx = (v - minVal) / d;
        if (buckets[idx].first == -1) buckets[idx] = {v, v};
        else {
            buckets[idx].first = std::min(buckets[idx].first, v);
            buckets[idx].second = std::max(buckets[idx].second, v);
        }
    }
    int ans = 0, prevMax = -1;
    for (auto &[lo, hi] : buckets) {
        if (lo == -1) continue;
        if (prevMax != -1) ans = std::max(ans, lo - prevMax);
        prevMax = hi;
    }
    return ans;
}
int main() {
    assert(maximumGap({1, 2, 3}) == 1);
    assert(maximumGap({3, 6, 9, 1}) == 3);
    assert(maximumGap({10}) == 0);
    assert(maximumGap({}) == 0);
    assert(maximumGap({1, 10000000}) == 9999999);
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''maximum_gap <- function(nums) {
  n <- length(nums)
  if (n < 2L) return(0L)
  min_val <- min(nums); max_val <- max(nums)
  if (min_val == max_val) return(0L)
  d <- max(1, (max_val - min_val) %/% (n - 1L))
  bucket_size <- (max_val - min_val) %/% d + 1L
  buckets <- matrix(-1L, nrow = bucket_size, ncol = 2)
  for (x in nums) {
    idx <- (x - min_val) %/% d + 1L
    if (buckets[idx, 1] == -1L) {
      buckets[idx, 1] <- x; buckets[idx, 2] <- x
    } else {
      if (x < buckets[idx, 1]) buckets[idx, 1] <- x
      if (x > buckets[idx, 2]) buckets[idx, 2] <- x
    }
  }
  ans <- 0L; prev_max <- -1L
  for (i in seq_len(bucket_size)) {
    if (buckets[i, 1] == -1L) next
    if (prev_max != -1L && buckets[i, 1] - prev_max > ans) ans <- buckets[i, 1] - prev_max
    prev_max <- buckets[i, 2]
  }
  ans
}
stopifnot(maximum_gap(c(1, 2, 3)) == 1)
stopifnot(maximum_gap(c(3, 6, 9, 1)) == 3)
stopifnot(maximum_gap(c(10)) == 0)
stopifnot(maximum_gap(integer(0)) == 0)
stopifnot(maximum_gap(c(1, 10000000)) == 9999999)
cat("PASS\\n")
''',
"zig": '''const std = @import("std");
fn maximumGap(nums: []const i32, alloc: std.mem.Allocator) i32 {
    const n = nums.len;
    if (n < 2) return 0;
    var min_val = nums[0];
    var max_val = nums[0];
    for (nums) |x| {
        if (x < min_val) min_val = x;
        if (x > max_val) max_val = x;
    }
    if (min_val == max_val) return 0;
    var d = @divTrunc(max_val - min_val, @as(i32, @intCast(n)) - 1);
    if (d < 1) d = 1;
    const bucket_size: usize = @intCast(@divTrunc(max_val - min_val, d) + 1);
    const buckets = alloc.alloc([2]i32, bucket_size) catch unreachable;
    for (buckets) |*b| b.* = .{ -1, -1 };
    for (nums) |x| {
        const idx: usize = @intCast(@divTrunc(x - min_val, d));
        if (buckets[idx][0] == -1) {
            buckets[idx] = .{ x, x };
        } else {
            if (x < buckets[idx][0]) buckets[idx][0] = x;
            if (x > buckets[idx][1]) buckets[idx][1] = x;
        }
    }
    var ans: i32 = 0;
    var prev_max: i32 = -1;
    for (buckets) |b| {
        if (b[0] == -1) continue;
        if (prev_max != -1 and b[0] - prev_max > ans) ans = b[0] - prev_max;
        prev_max = b[1];
    }
    return ans;
}
pub fn main() !void {
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();
    const alloc = arena.allocator();
    if (maximumGap(&[_]i32{ 1, 2, 3 }, alloc) != 1) return error.TestFailed;
    if (maximumGap(&[_]i32{ 3, 6, 9, 1 }, alloc) != 3) return error.TestFailed;
    if (maximumGap(&[_]i32{10}, alloc) != 0) return error.TestFailed;
    if (maximumGap(&[_]i32{}, alloc) != 0) return error.TestFailed;
    if (maximumGap(&[_]i32{ 1, 10000000 }, alloc) != 9999999) return error.TestFailed;
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''int maximumGap(List<int> nums) {
  final n = nums.length;
  if (n < 2) return 0;
  var minVal = nums[0], maxVal = nums[0];
  for (final x in nums) {
    if (x < minVal) minVal = x;
    if (x > maxVal) maxVal = x;
  }
  if (minVal == maxVal) return 0;
  var d = (maxVal - minVal) ~/ (n - 1);
  if (d < 1) d = 1;
  final bucketSize = (maxVal - minVal) ~/ d + 1;
  final buckets = List.generate(bucketSize, (_) => <int>[-1, -1]);
  for (final x in nums) {
    final idx = (x - minVal) ~/ d;
    if (buckets[idx][0] == -1) {
      buckets[idx][0] = x;
      buckets[idx][1] = x;
    } else {
      if (x < buckets[idx][0]) buckets[idx][0] = x;
      if (x > buckets[idx][1]) buckets[idx][1] = x;
    }
  }
  var ans = 0;
  var prevMax = -1;
  for (final b in buckets) {
    if (b[0] == -1) continue;
    if (prevMax != -1 && b[0] - prevMax > ans) ans = b[0] - prevMax;
    prevMax = b[1];
  }
  return ans;
}
void main() {
  if (maximumGap([1, 2, 3]) != 1) throw StateError('c1');
  if (maximumGap([3, 6, 9, 1]) != 3) throw StateError('c2');
  if (maximumGap([10]) != 0) throw StateError('c3');
  if (maximumGap([]) != 0) throw StateError('c4');
  if (maximumGap([1, 10000000]) != 9999999) throw StateError('c5');
  print('PASS');
}
''',
}

A21 = {
"rust": '''#[derive(Debug)]
struct ListNode {{ val: i32, next: Option<Box<ListNode>> }}
fn build_list(vals: &[i32]) -> Option<Box<ListNode>> {{
    let mut head: Option<Box<ListNode>> = None;
    for &v in vals.iter().rev() {{
        let mut n = Box::new(ListNode {{ val: v, next: head }});
        head = Some(n);
    }}
    head
}}
fn list_to_vec(head: &Option<Box<ListNode>>) -> Vec<i32> {{
    let mut out = Vec::new();
    let mut cur = head;
    while let Some(n) = cur {{ out.push(n.val); cur = &n.next; }}
    out
}}
fn merge_two_lists(list1: Option<Box<ListNode>>, list2: Option<Box<ListNode>>) -> Option<Box<ListNode>> {{
    let mut dummy = Box::new(ListNode {{ val: 0, next: None }});
    let mut p: &mut Option<Box<ListNode>> = &mut dummy.next;
    let mut p1 = list1;
    let mut p2 = list2;
    while let (Some(a), Some(b)) = (p1.as_ref(), p2.as_ref()) {{
        if a.val < b.val {{
            let next = p1.as_mut().unwrap().next.take();
            *p = Some(p1.take().unwrap());
            p1 = next;
        }} else {{
            let next = p2.as_mut().unwrap().next.take();
            *p = Some(p2.take().unwrap());
            p2 = next;
        }}
        p = &mut p.as_mut().unwrap().next;
    }}
    *p = if p1.is_some() {{ p1 }} else {{ p2 }};
    dummy.next
}}
fn main() {{
    let got = list_to_vec(&merge_two_lists(build_list(&[1, 2, 4]), build_list(&[1, 3, 4])));
    assert_eq!(got, vec![1, 1, 2, 3, 4, 4]);
    assert_eq!(list_to_vec(&merge_two_lists(build_list(&[]), build_list(&[]))), Vec::<i32>::new());
    let got3 = list_to_vec(&merge_two_lists(build_list(&[]), build_list(&[0])));
    assert_eq!(got3, vec![0]);
    println!("PASS");
}}
''',
"lua": '''local ListNode = {}
ListNode.__index = ListNode
function ListNode.new(val, next) return setmetatable({val = val, next = next}, ListNode) end
local function build_list(vals)
    local head, cur = nil, nil
    for _, v in ipairs(vals) do
        local n = ListNode.new(v)
        if not head then head, cur = n, n else cur.next, cur = n, n end
    end
    return head
end
local function list_to_vec(head)
    local out = {}
    while head do out[#out + 1] = head.val; head = head.next end
    return out
end
local function merge_two_lists(list1, list2)
    local dummy = ListNode.new(0)
    local p = dummy
    local p1, p2 = list1, list2
    while p1 and p2 do
        if p1.val < p2.val then
            p.next = p1
            p1 = p1.next
        else
            p.next = p2
            p2 = p2.next
        end
        p = p.next
    end
    p.next = p1 or p2
    return dummy.next
end
local a = list_to_vec(merge_two_lists(build_list({1, 2, 4}), build_list({1, 3, 4})))
assert(#a == 6 and table.concat(a, ",") == "1,1,2,3,4,4")
assert(#list_to_vec(merge_two_lists(build_list({}), build_list({}))) == 0)
local c = list_to_vec(merge_two_lists(build_list({}), build_list({0})))
assert(#c == 1 and c[1] == 0)
print("PASS")
''',
"c": '''#include <stdio.h>
#include <stdlib.h>
typedef struct LNode {{ int val; struct LNode *next; }} LNode;
static LNode *build_list(const int *vals, int n) {{
    LNode *head = NULL, **cur = &head;
    for (int i = 0; i < n; i++) {{
        LNode *node = malloc(sizeof(LNode));
        node->val = vals[i]; node->next = NULL;
        *cur = node; cur = &node->next;
    }}
    return head;
}}
static void free_list(LNode *h) {{ while (h) {{ LNode *n = h->next; free(h); h = n; }} }}
static int list_check(LNode *h, const int *want, int wn) {{
    int i = 0;
    while (h) {{
        if (i >= wn || h->val != want[i]) return 0;
        i++; h = h->next;
    }}
    return i == wn;
}}
static LNode *merge_two_lists(LNode *list1, LNode *list2) {{
    LNode dummy = {{0, NULL}};
    LNode *p = &dummy;
    while (list1 && list2) {{
        if (list1->val < list2->val) {{ p->next = list1; list1 = list1->next; }}
        else {{ p->next = list2; list2 = list2->next; }}
        p = p->next;
    }}
    p->next = list1 ? list1 : list2;
    return dummy.next;
}}
int main(void) {{
    LNode *got = merge_two_lists(build_list((int[]){{1,2,4}}, 3), build_list((int[]){{1,3,4}}, 3));
    int w1[] = {{1,1,2,3,4,4}};
    if (!list_check(got, w1, 6)) {{ printf("FAIL 1\\n"); return 1; }}
    free_list(got);
    LNode *got2 = merge_two_lists(NULL, NULL);
    if (got2 != NULL) {{ printf("FAIL 2\\n"); return 1; }}
    LNode *got3 = merge_two_lists(NULL, build_list((int[]){{0}}, 1));
    int w3[] = {{0}};
    if (!list_check(got3, w3, 1)) {{ printf("FAIL 3\\n"); return 1; }}
    free_list(got3);
    printf("PASS\\n");
    return 0;
}}
''',
"cpp": '''#include <cassert>
#include <iostream>
#include <memory>
#include <vector>
struct ListNode {
    int val;
    std::unique_ptr<ListNode> next;
    explicit ListNode(int v) : val(v) {}
};
static std::unique_ptr<ListNode> buildList(const std::vector<int> &vals) {
    ListNode dummy(0);
    ListNode *cur = &dummy;
    for (int v : vals) {
        cur->next = std::make_unique<ListNode>(v);
        cur = cur->next.get();
    }
    return std::move(dummy.next);
}
static std::vector<int> listToVec(ListNode *head) {
    std::vector<int> out;
    while (head) { out.push_back(head->val); head = head->next.get(); }
    return out;
}
static std::unique_ptr<ListNode> mergeTwoLists(std::unique_ptr<ListNode> l1, std::unique_ptr<ListNode> l2) {
    ListNode dummy(0);
    ListNode *p = &dummy;
    while (l1 && l2) {
        if (l1->val < l2->val) {
            p->next = std::move(l1);
            l1 = std::move(p->next->next);
        } else {
            p->next = std::move(l2);
            l2 = std::move(p->next->next);
        }
        p = p->next.get();
    }
    p->next = l1 ? std::move(l1) : std::move(l2);
    return std::move(dummy.next);
}
int main() {
    auto got = listToVec(mergeTwoLists(buildList({1, 2, 4}), buildList({1, 3, 4})).get());
    assert((got == std::vector<int>{1, 1, 2, 3, 4, 4}));
    assert(listToVec(mergeTwoLists(nullptr, nullptr).get()).empty());
    auto got3 = listToVec(mergeTwoLists(nullptr, buildList({0})).get());
    assert((got3 == std::vector<int>{0}));
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''build_list <- function(vals) {
  if (length(vals) == 0) return(NULL)
  head <- NULL; cur <- NULL
  for (v in vals) {
    n <- new.env(parent = emptyenv()); n$val <- v; n$nxt <- NULL
    if (is.null(head)) { head <- n; cur <- n } else { cur$nxt <- n; cur <- n }
  }
  head
}
list_to_vec <- function(head) {
  out <- integer(0)
  while (!is.null(head)) { out[[length(out) + 1L]] <- head$val; head <- head$nxt }
  out
}
merge_two_lists <- function(list1, list2) {
  dummy <- new.env(parent = emptyenv()); dummy$val <- 0L; dummy$nxt <- NULL
  p <- dummy
  p1 <- list1; p2 <- list2
  while (!is.null(p1) && !is.null(p2)) {
    if (p1$val < p2$val) { p$nxt <- p1; p1 <- p1$nxt } else { p$nxt <- p2; p2 <- p2$nxt }
    p <- p$nxt
  }
  p$nxt <- if (!is.null(p1)) p1 else p2
  dummy$nxt
}
a <- list_to_vec(merge_two_lists(build_list(c(1L, 2L, 4L)), build_list(c(1L, 3L, 4L))))
stopifnot(identical(a, c(1L, 1L, 2L, 3L, 4L, 4L)))
stopifnot(is.null(merge_two_lists(NULL, NULL)))
c3 <- list_to_vec(merge_two_lists(NULL, build_list(0L)))
stopifnot(identical(c3, 0L))
cat("PASS\\n")
''',
"zig": '''const std = @import("std");
const LNode = struct { val: i32, next: ?*LNode };
fn buildList(alloc: std.mem.Allocator, vals: []const i32) ?*LNode {
    var head: ?*LNode = null;
    var tail: ?*LNode = null;
    for (vals) |v| {
        const n = alloc.create(LNode) catch unreachable;
        n.* = .{ .val = v, .next = null };
        if (tail) |t| t.next = n else head = n;
        tail = n;
    }
    return head;
}
fn listToVec(head: ?*LNode, out: *std.ArrayList(i32)) void {
    var cur = head;
    while (cur) |n| {
        out.append(n.val) catch unreachable;
        cur = n.next;
    }
}
fn mergeTwoLists(alloc: std.mem.Allocator, l1_in: ?*LNode, l2_in: ?*LNode) ?*LNode {
    const dummy = alloc.create(LNode) catch unreachable;
    dummy.* = .{ .val = 0, .next = null };
    var p = dummy;
    var l1 = l1_in;
    var l2 = l2_in;
    while (l1 != null and l2 != null) {
        if (l1.?.val < l2.?.val) {
            p.next = l1;
            l1 = l1.?.next;
        } else {
            p.next = l2;
            l2 = l2.?.next;
        }
        p = p.next.?;
    }
    p.next = if (l1) |x| x else l2;
    return dummy.next;
}
pub fn main() !void {
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();
    const alloc = arena.allocator();
    var out = std.ArrayList(i32).init(std.heap.page_allocator);
    defer out.deinit();
    const got = mergeTwoLists(alloc, buildList(alloc, &[_]i32{ 1, 2, 4 }), buildList(alloc, &[_]i32{ 1, 3, 4 }));
    listToVec(got, &out);
    const want = [_]i32{ 1, 1, 2, 3, 4, 4 };
    if (out.items.len != want.len) return error.TestFailed;
    for (want, 0..) |w, i| if (out.items[i] != w) return error.TestFailed;
    if (mergeTwoLists(alloc, null, null) != null) return error.TestFailed;
    out.clearRetainingCapacity();
    listToVec(mergeTwoLists(alloc, null, buildList(alloc, &[_]i32{0})), &out);
    if (out.items.len != 1 or out.items[0] != 0) return error.TestFailed;
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''class LNode {
  final int val;
  LNode? next;
  LNode(this.val);
}
LNode? buildList(List<int> vals) {
  LNode? head;
  LNode? cur;
  for (final v in vals) {
    final n = LNode(v);
    if (head == null) {
      head = n;
    } else {
      cur!.next = n;
    }
    cur = n;
  }
  return head;
}
List<int> listToVec(LNode? head) {
  final out = <int>[];
  while (head != null) {
    out.add(head.val);
    head = head.next;
  }
  return out;
}
LNode? mergeTwoLists(LNode? list1, LNode? list2) {
  final dummy = LNode(0);
  var p = dummy;
  var p1 = list1, p2 = list2;
  while (p1 != null && p2 != null) {
    if (p1.val < p2.val) {
      p.next = p1;
      p1 = p1.next;
    } else {
      p.next = p2;
      p2 = p2.next;
    }
    p = p.next!;
  }
  p.next = p1 ?? p2;
  return dummy.next;
}
void main() {
  if (listToVec(mergeTwoLists(buildList([1, 2, 4]), buildList([1, 3, 4]))).toString() != '[1, 1, 2, 3, 4, 4]') throw StateError('c1');
  if (mergeTwoLists(null, null) != null) throw StateError('c2');
  if (listToVec(mergeTwoLists(null, buildList([0]))).toString() != '[0]') throw StateError('c3');
  print('PASS');
}
''',
}

PROBS = [
    ("lc_41_缺失的第一个正数", A41, "LeetCode 41. 缺失的第一个正数"),
    ("lc_164_最大间距", A164, "LeetCode 164. 最大间距"),
    ("lc_21_合并两个有序链表", A21, "LeetCode 21. 合并两个有序链表"),
]
count = 0
for prob, algo, title in PROBS:
    bid = B[prob.split("_")[1]]
    ts_dir = f"/Users/Wang/Code/github/web-x-blog/work/blog/courses/21.dsa/ts/sort/{prob}"
    sols = sorted(f[:-3] for f in os.listdir(ts_dir) if f.startswith("solution_") and f.endswith(".ts"))
    for lang in EXT:
        ext = EXT[lang]
        for sol in sols:
            n = sol.replace("solution_", "").split("_")[0]
            head = head_comment(lang, bid, f"{title} — {LANGNAME[lang]} 版（方案{n}）")
            body = algo[lang].replace("{H}", "").replace("{{", "{").replace("}}", "}")
            emit(lang, f"sort/{prob}/{sol}.{ext}", head + "\n" + body)
            count += 1
print(f"emitted {count} files")
