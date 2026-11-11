#!/usr/bin/env python3
# gen_stack2.py — stack 第二批：155/225/232/03_05/27/2454/3100/1685/556/641/341/1472 × 7语言
import sys, os; sys.path.insert(0, "/Users/Wang/Code/github/web-x-blog/work/target/21.dsa/_tools")
from langlib import emit, head_comment, EXT

B = {"155":"145245934","225":"145198996","232":"145114011","0305":"145397311","27":"145114689","2454":"145397916","3100":"145386116","1685":"136236962","556":"145397820","641":"145361774","341":"145078849","1472":"145338856"}
LANGNAME = {"rust": "Rust", "lua": "Lua", "c": "C", "cpp": "C++", "r": "R", "zig": "Zig", "dart": "Dart"}

T = {}
T["155"] = {
"rust":'''#[derive(Clone)]
enum Op { Push(i32), Pop, Top, GetMin }
fn min_stack_run(ops: Vec<Op>) -> Vec<i32> {
    let mut vals: Vec<i32> = Vec::new();
    let mut mins: Vec<i32> = Vec::new();
    let mut out = Vec::new();
    for op in ops {
        match op {
            Op::Push(v) => {
                vals.push(v);
                mins.push(if mins.is_empty() { v } else { (*mins.last().unwrap()).min(v) });
            }
            Op::Pop => { vals.pop(); mins.pop(); }
            Op::Top => out.push(*vals.last().unwrap_or(&-1)),
            Op::GetMin => out.push(*mins.last().unwrap_or(&-1)),
        }
    }
    out
}
fn main() {
    let ops = vec![Op::Push(-2), Op::Push(0), Op::Push(-3), Op::GetMin, Op::Pop, Op::Top, Op::GetMin];
    assert_eq!(min_stack_run(ops), vec![-3, 0, -2]);
    println!("PASS"); }''',
"lua":'''local MinStack = {}
MinStack.__index = MinStack
function MinStack.new() return setmetatable({vals = {}, mins = {}}, MinStack) end
function MinStack:push(v)
    self.vals[#self.vals + 1] = v
    local m = #self.mins > 0 and math.min(self.mins[#self.mins], v) or v
    self.mins[#self.mins + 1] = m
end
function MinStack:pop() self.vals[#self.vals] = nil; self.mins[#self.mins] = nil end
function MinStack:top() return self.vals[#self.vals] end
function MinStack:getMin() return self.mins[#self.mins] end
local ms = MinStack.new()
ms:push(-2); ms:push(0); ms:push(-3)
assert(ms:getMin() == -3)
ms:pop()
assert(ms:top() == 0)
assert(ms:getMin() == -2)
print("PASS")''',
"c":'''#include <stdio.h>
typedef struct { int vals[4096]; int mins[4096]; int top; } MinStack;
static void ms_init(MinStack *s) { s->top = 0; }
static void ms_push(MinStack *s, int v) {
    s->vals[s->top] = v;
    s->mins[s->top] = s->top > 0 && s->mins[s->top - 1] < v ? s->mins[s->top - 1] : v;
    s->top++;
}
static void ms_pop(MinStack *s) { s->top--; }
static int ms_top(MinStack *s) { return s->vals[s->top - 1]; }
static int ms_get_min(MinStack *s) { return s->mins[s->top - 1]; }
int main(void) {
    MinStack s;
    ms_init(&s);
    ms_push(&s, -2); ms_push(&s, 0); ms_push(&s, -3);
    if (ms_get_min(&s) != -3) { printf("FAIL 1\\n"); return 1; }
    ms_pop(&s);
    if (ms_top(&s) != 0) { printf("FAIL 2\\n"); return 1; }
    if (ms_get_min(&s) != -2) { printf("FAIL 3\\n"); return 1; }
    printf("PASS\\n"); return 0; }''',
"cpp":'''#include <cassert>
#include <iostream>
#include <vector>
struct MinStack {
    std::vector<int> vals, mins;
    void push(int v) {
        vals.push_back(v);
        mins.push_back(mins.empty() ? v : std::min(mins.back(), v));
    }
    void pop() { vals.pop_back(); mins.pop_back(); }
    int top() { return vals.back(); }
    int getMin() { return mins.back(); }
};
int main() {
    MinStack s;
    s.push(-2);
    s.push(0);
    s.push(-3);
    assert(s.getMin() == -3);
    s.pop();
    assert(s.top() == 0);
    assert(s.getMin() == -2);
    std::cout << "PASS" << std::endl; }''',
"r":'''MinStack <- function() {
  e <- new.env(parent = emptyenv())
  e$vals <- integer(0); e$mins <- integer(0)
  e$push <- function(v) {
    e$vals <<- c(e$vals, v)
    m <- if (length(e$mins) > 0) min(e$mins[length(e$mins)], v) else v
    e$mins <<- c(e$mins, m)
  }
  e$pop <- function() {
    e$vals <<- e$vals[-length(e$vals)]
    e$mins <<- e$mins[-length(e$mins)]
  }
  e$top <- function() e$vals[length(e$vals)]
  e$getMin <- function() e$mins[length(e$mins)]
  e
}
ms <- MinStack()
ms$push(-2); ms$push(0); ms$push(-3)
stopifnot(ms$getMin() == -3)
ms$pop()
stopifnot(ms$top() == 0, ms$getMin() == -2)
cat("PASS\\n")''',
"zig":'''const std = @import("std");
const MinStack = struct {
    vals: [4096]i32,
    mins: [4096]i32,
    n: usize,
    fn init() MinStack {
        return .{ .vals = undefined, .mins = undefined, .n = 0 };
    }
    fn push(self: *MinStack, v: i32) void {
        self.vals[self.n] = v;
        self.mins[self.n] = if (self.n > 0 and self.mins[self.n - 1] < v) self.mins[self.n - 1] else v;
        self.n += 1;
    }
    fn pop(self: *MinStack) void { self.n -= 1; }
    fn top(self: *MinStack) i32 { return self.vals[self.n - 1]; }
    fn getMin(self: *MinStack) i32 { return self.mins[self.n - 1]; }
};
pub fn main() !void {
    var s = MinStack.init();
    s.push(-2);
    s.push(0);
    s.push(-3);
    if (s.getMin() != -3) return error.TestFailed;
    s.pop();
    if (s.top() != 0) return error.TestFailed;
    if (s.getMin() != -2) return error.TestFailed;
    std.debug.print("PASS\\n", .{}); }''',
"dart":'''class MinStack {
  final List<int> vals = [];
  final List<int> mins = [];
  void push(int v) {
    vals.add(v);
    mins.add(mins.isEmpty ? v : (mins.last < v ? mins.last : v));
  }
  void pop() { vals.removeLast(); mins.removeLast(); }
  int top() => vals.last;
  int getMin() => mins.last;
}
void main() {
  final ms = MinStack();
  ms.push(-2); ms.push(0); ms.push(-3);
  if (ms.getMin() != -3) throw StateError('c1');
  ms.pop();
  if (ms.top() != 0) throw StateError('c2');
  if (ms.getMin() != -2) throw StateError('c3');
  print('PASS'); }''',
}

T["27"] = {
"rust":'''fn remove_element(nums: &mut Vec<i32>, val: i32) -> i32 {
    let mut k = 0usize;
    for i in 0..nums.len() {
        if nums[i] != val { nums[k] = nums[i]; k += 1; }
    }
    k as i32
}
fn main() {
    let mut v = vec![3,2,2,3];
    assert_eq!(remove_element(&mut v, 3), 2);
    assert_eq!(&v[..2], &[2, 2]);
    let mut v2 = vec![0,1,2,2,3,0,4,2];
    assert_eq!(remove_element(&mut v2, 2), 5);
    println!("PASS"); }''',
"lua":'''local function remove_element(nums, val)
    local k = 1
    for i = 1, #nums do
        if nums[i] ~= val then
            nums[k] = nums[i]
            k = k + 1
        end
    end
    return k - 1
end
assert(remove_element({3,2,2,3}, 3) == 2)
assert(remove_element({0,1,2,2,3,0,4,2}, 2) == 5)
print("PASS")''',
"c":'''#include <stdio.h>
static int remove_element(int n[], int len, int val) {
    int k = 0;
    for (int i = 0; i < len; i++) {
        if (n[i] != val) n[k++] = n[i];
    }
    return k;
}
int main(void) {
    int v1[] = {3,2,2,3};
    if (remove_element(v1, 4, 3) != 2) { printf("FAIL 1\\n"); return 1; }
    if (!(v1[0] == 2 && v1[1] == 2)) { printf("FAIL 1b\\n"); return 1; }
    int v2[] = {0,1,2,2,3,0,4,2};
    if (remove_element(v2, 8, 2) != 5) { printf("FAIL 2\\n"); return 1; }
    printf("PASS\\n"); return 0; }''',
"cpp":'''#include <cassert>
#include <iostream>
#include <vector>
static int removeElement(std::vector<int> &nums, int val) {
    size_t k = 0;
    for (size_t i = 0; i < nums.size(); ++i) {
        if (nums[i] != val) nums[k++] = nums[i];
    }
    return static_cast<int>(k);
}
int main() {
    std::vector<int> v = {3, 2, 2, 3};
    assert(removeElement(v, 3) == 2);
    assert(v[0] == 2 && v[1] == 2);
    std::vector<int> v2 = {0, 1, 2, 2, 3, 0, 4, 2};
    assert(removeElement(v2, 2) == 5);
    std::cout << "PASS" << std::endl; }''',
"r":'''remove_element <- function(nums, val) {
  k <- 1L
  for (i in seq_along(nums)) {
    if (nums[i] != val) {
      nums[k] <- nums[i]
      k <- k + 1L
    }
  }
  k - 1L
}
stopifnot(remove_element(c(3, 2, 2, 3), 3) == 2)
stopifnot(remove_element(c(0, 1, 2, 2, 3, 0, 4, 2), 2) == 5)
cat("PASS\\n")''',
"zig":'''const std = @import("std");
fn removeElement(nums: []i32, val: i32) i32 {
    var k: usize = 0;
    for (nums) |v| {
        if (v != val) {
            nums[k] = v;
            k += 1;
        }
    }
    return @intCast(k);
}
pub fn main() !void {
    var v1 = [_]i32{ 3, 2, 2, 3 };
    if (removeElement(&v1, 3) != 2) return error.TestFailed;
    if (v1[0] != 2 or v1[1] != 2) return error.TestFailed;
    var v2 = [_]i32{ 0, 1, 2, 2, 3, 0, 4, 2 };
    if (removeElement(&v2, 2) != 5) return error.TestFailed;
    std.debug.print("PASS\\n", .{}); }''',
"dart":'''int removeElement(List<int> nums, int val) {
  var k = 0;
  for (var i = 0; i < nums.length; i++) {
    if (nums[i] != val) { nums[k] = nums[i]; k++; }
  }
  return k;
}
void main() {
  final v = [3, 2, 2, 3];
  if (removeElement(v, 3) != 2) throw StateError('c1');
  if (v[0] != 2 || v[1] != 2) throw StateError('c1b');
  if (removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2) != 5) throw StateError('c2');
  print('PASS'); }''',
}

T["2454"] = {
"rust":'''fn second_greater(nums: Vec<i32>) -> Vec<i32> {
    let n = nums.len();
    let mut res = vec![-1i32; n];
    let mut s1: Vec<usize> = Vec::new();
    let mut s2: Vec<usize> = Vec::new();
    for i in 0..n {
        while let Some(&t) = s2.last() {
            if nums[t] < nums[i] { res[t] = nums[i]; s2.pop(); } else { break; }
        }
        while let Some(&t) = s1.last() {
            if nums[t] < nums[i] { s2.push(t); s1.pop(); } else { break; }
        }
        s1.push(i);
    }
    res
}
fn main() {
    assert_eq!(second_greater(vec![2,4,0,9,6]), vec![9,6,6,-1,-1]);
    assert_eq!(second_greater(vec![5,4,3,2,1]), vec![-1,-1,-1,-1,-1]);
    println!("PASS"); }''',
"lua":'''local function second_greater(nums)
    local n = #nums
    local res = {}
    for i = 1, n do res[i] = -1 end
    local s1, s2 = {}, {}
    for i = 1, n do
        while #s2 > 0 and nums[s2[#s2]] < nums[i] do
            res[s2[#s2]] = nums[i]
            s2[#s2] = nil
        end
        while #s1 > 0 and nums[s1[#s1]] < nums[i] do
            s2[#s2 + 1] = s1[#s1]
            s1[#s1] = nil
        end
        s1[#s1 + 1] = i
    end
    return res
end
assert(table.concat(second_greater({2,4,0,9,6}), ",") == "9,6,6,-1,-1")
assert(table.concat(second_greater({5,4,3,2,1}), ",") == "-1,-1,-1,-1,-1")
print("PASS")''',
"c":'''#include <stdio.h>
static void second_greater(const int *nums, int n, int out[]) {
    for (int i = 0; i < n; i++) out[i] = -1;
    int s1[4096], t1 = 0, s2[4096], t2 = 0;
    for (int i = 0; i < n; i++) {
        while (t2 > 0 && nums[s2[t2 - 1]] < nums[i]) out[s2[--t2]] = nums[i];
        while (t1 > 0 && nums[s1[t1 - 1]] < nums[i]) s2[t2++] = s1[--t1];
        s1[t1++] = i;
    }
}
int main(void) {
    int out[4096];
    second_greater((int[]){2,4,0,9,6}, 5, out);
    if (!(out[0]==9&&out[1]==6&&out[2]==6&&out[3]==-1&&out[4]==-1)) { printf("FAIL 1\\n"); return 1; }
    second_greater((int[]){5,4,3,2,1}, 5, out);
    if (!(out[0]==-1&&out[4]==-1)) { printf("FAIL 2\\n"); return 1; }
    printf("PASS\\n"); return 0; }''',
"cpp":'''#include <cassert>
#include <iostream>
#include <vector>
static std::vector<int> secondGreater(const std::vector<int> &nums) {
    size_t n = nums.size();
    std::vector<int> res(n, -1);
    std::vector<size_t> s1, s2;
    for (size_t i = 0; i < n; ++i) {
        while (!s2.empty() && nums[s2.back()] < nums[i]) res[s2.back()] = nums[i], s2.pop_back();
        while (!s1.empty() && nums[s1.back()] < nums[i]) s2.push_back(s1.back()), s1.pop_back();
        s1.push_back(i);
    }
    return res;
}
int main() { assert((secondGreater({2,4,0,9,6}) == std::vector<int>{9,6,6,-1,-1})); assert((secondGreater({5,4,3,2,1}) == std::vector<int>{-1,-1,-1,-1,-1})); std::cout << "PASS" << std::endl; }''',
"r":'''second_greater <- function(nums) {
  n <- length(nums)
  res <- rep(-1L, n)
  s1 <- integer(0); s2 <- integer(0)
  for (i in seq_len(n)) {
    while (length(s2) > 0 && nums[s2[length(s2)]] < nums[i]) {
      res[s2[length(s2)]] <- nums[i]
      s2 <- s2[-length(s2)]
    }
    while (length(s1) > 0 && nums[s1[length(s1)]] < nums[i]) {
      s2 <- c(s2, s1[length(s1)])
      s1 <- s1[-length(s1)]
    }
    s1 <- c(s1, i)
  }
  res
}
stopifnot(identical(as.integer(second_greater(c(2, 4, 0, 9, 6))), c(9L, 6L, 6L, -1L, -1L)))
stopifnot(identical(as.integer(second_greater(c(5, 4, 3, 2, 1))), rep(-1L, 5)))
cat("PASS\\n")''',
"zig":'''const std = @import("std");
fn secondGreater(nums: []const i32, out: []i32) void {
    const n = nums.len;
    for (0..n) |i| out[i] = -1;
    var s1: [4096]usize = undefined;
    var t1: usize = 0;
    var s2: [4096]usize = undefined;
    var t2: usize = 0;
    for (0..n) |i| {
        while (t2 > 0 and nums[s2[t2 - 1]] < nums[i]) {
            t2 -= 1;
            out[s2[t2]] = nums[i];
        }
        while (t1 > 0 and nums[s1[t1 - 1]] < nums[i]) {
            t1 -= 1;
            s2[t2] = s1[t1];
            t2 += 1;
        }
        s1[t1] = i;
        t1 += 1;
    }
}
pub fn main() !void {
    var out: [8]i32 = undefined;
    secondGreater(&[_]i32{ 2, 4, 0, 9, 6 }, &out);
    if (out[0] != 9 or out[2] != 6 or out[4] != -1) return error.TestFailed;
    secondGreater(&[_]i32{ 5, 4, 3, 2, 1 }, &out);
    if (out[0] != -1) return error.TestFailed;
    std.debug.print("PASS\\n", .{}); }''',
"dart":'''List<int> secondGreater(List<int> nums) {
  final n = nums.length;
  final res = List<int>.filled(n, -1);
  final s1 = <int>[];
  final s2 = <int>[];
  for (var i = 0; i < n; i++) {
    while (s2.isNotEmpty && nums[s2.last] < nums[i]) {
      res[s2.removeLast()] = nums[i];
    }
    while (s1.isNotEmpty && nums[s1.last] < nums[i]) {
      s2.add(s1.removeLast());
    }
    s1.add(i);
  }
  return res;
}
void main() { if (secondGreater([2,4,0,9,6]).toString() != '[9, 6, 6, -1, -1]') throw StateError('c1'); if (secondGreater([5,4,3,2,1]).toString() != '[-1, -1, -1, -1, -1]') throw StateError('c2'); print('PASS'); }''',
}

T["3100"] = {
"rust":'''fn max_bottles_drunk(num_bottles: i32, mut num_exchange: i32) -> i32 {
    let mut drunk = num_bottles;
    let mut empty = num_bottles;
    while empty >= num_exchange {
        empty -= num_exchange;
        num_exchange += 1;
        drunk += 1;
        empty += 1;
    }
    drunk
}
fn main() { assert_eq!(max_bottles_drunk(10, 3), 13); assert_eq!(max_bottles_drunk(1, 2), 1); println!("PASS"); }''',
"lua":'''local function max_bottles_drunk(num_bottles, num_exchange)
    local drunk = num_bottles
    local empty = num_bottles
    while empty >= num_exchange do
        empty = empty - num_exchange
        num_exchange = num_exchange + 1
        drunk = drunk + 1
        empty = empty + 1
    end
    return drunk
end
assert(max_bottles_drunk(10, 3) == 13)
assert(max_bottles_drunk(1, 2) == 1)
print("PASS")''',
"c":'''#include <stdio.h>
static int max_bottles_drunk(int nb, int ne) {
    int drunk = nb, empty = nb;
    while (empty >= ne) {
        empty -= ne;
        ne++;
        drunk++;
        empty++;
    }
    return drunk;
}
int main(void) {
    if (max_bottles_drunk(10, 3) != 13) { printf("FAIL 1\\n"); return 1; }
    if (max_bottles_drunk(1, 2) != 1) { printf("FAIL 2\\n"); return 1; }
    printf("PASS\\n"); return 0; }''',
"cpp":'''#include <cassert>
#include <iostream>
static int maxBottlesDrunk(int numBottles, int numExchange) {
    int drunk = numBottles, empty = numBottles;
    while (empty >= numExchange) {
        empty -= numExchange;
        ++numExchange;
        ++drunk;
        ++empty;
    }
    return drunk;
}
int main() { assert(maxBottlesDrunk(10, 3) == 13); assert(maxBottlesDrunk(1, 2) == 1); std::cout << "PASS" << std::endl; }''',
"r":'''max_bottles_drunk <- function(num_bottles, num_exchange) {
  drunk <- num_bottles; empty <- num_bottles
  while (empty >= num_exchange) {
    empty <- empty - num_exchange
    num_exchange <- num_exchange + 1
    drunk <- drunk + 1
    empty <- empty + 1
  }
  drunk
}
stopifnot(max_bottles_drunk(10, 3) == 13)
stopifnot(max_bottles_drunk(1, 2) == 1)
cat("PASS\\n")''',
"zig":'''const std = @import("std");
fn maxBottlesDrunk(nb_in: i32, ne_in: i32) i32 {
    var drunk = nb_in;
    var empty = nb_in;
    var ne = ne_in;
    while (empty >= ne) {
        empty -= ne;
        ne += 1;
        drunk += 1;
        empty += 1;
    }
    return drunk;
}
pub fn main() !void {
    if (maxBottlesDrunk(10, 3) != 13) return error.TestFailed;
    if (maxBottlesDrunk(1, 2) != 1) return error.TestFailed;
    std.debug.print("PASS\\n", .{}); }''',
"dart":'''int maxBottlesDrunk(int numBottles, int numExchange) {
  var drunk = numBottles, empty = numBottles, ne = numExchange;
  while (empty >= ne) {
    empty -= ne;
    ne++;
    drunk++;
    empty++;
  }
  return drunk;
}
void main() { if (maxBottlesDrunk(10, 3) != 13) throw StateError('c1'); if (maxBottlesDrunk(1, 2) != 1) throw StateError('c2'); print('PASS'); }''',
}

T["1685"] = {
"rust":'''fn get_sum_absolute_differences(nums: Vec<i32>) -> Vec<i32> {
    let n = nums.len();
    let total: i64 = nums.iter().map(|&x| x as i64).sum();
    let mut prefix = 0i64;
    let mut out = Vec::with_capacity(n);
    for i in 0..n {
        let v = nums[i] as i64;
        let left = (v * i as i64 - prefix) as i64;
        let right = ((total - prefix - v) - v * (n - 1 - i) as i64) as i64;
        out.push((left + right) as i32);
        prefix += v;
    }
    out
}
fn main() {
    assert_eq!(get_sum_absolute_differences(vec![2,3,5]), vec![4,3,5]);
    assert_eq!(get_sum_absolute_differences(vec![1,4,6,8,10]), vec![24,15,13,15,21]);
    println!("PASS"); }''',
"lua":'''local function get_sum_absolute_differences(nums)
    local n = #nums
    local total = 0
    for _, v in ipairs(nums) do total = total + v end
    local prefix = 0
    local out = {}
    for i = 1, n do
        local v = nums[i]
        local cnt_left = i - 1
        local cnt_right = n - i
        local left = v * cnt_left - prefix
        local right = (total - prefix - v) - v * cnt_right
        out[i] = left + right
        prefix = prefix + v
    end
    return out
end
assert(table.concat(get_sum_absolute_differences({2,3,5}), ",") == "4,3,5")
assert(table.concat(get_sum_absolute_differences({1,4,6,8,10}), ",") == "24,15,13,15,21")
print("PASS")''',
"c":'''#include <stdio.h>
static void get_sum_absolute_differences(const int *nums, int n, int out[]) {
    long total = 0;
    for (int i = 0; i < n; i++) total += nums[i];
    long prefix = 0;
    for (int i = 0; i < n; i++) {
        long v = nums[i];
        long left = v * i - prefix;
        long right = (total - prefix - v) - v * (n - 1 - i);
        out[i] = (int)(left + right);
        prefix += v;
    }
}
int main(void) {
    int out[4096];
    get_sum_absolute_differences((int[]){2,3,5}, 3, out);
    if (!(out[0]==4&&out[1]==3&&out[2]==5)) { printf("FAIL 1\\n"); return 1; }
    get_sum_absolute_differences((int[]){1,4,6,8,10}, 5, out);
    if (!(out[0]==24&&out[2]==13&&out[4]==21)) { printf("FAIL 2\\n"); return 1; }
    printf("PASS\\n"); return 0; }''',
"cpp":'''#include <cassert>
#include <iostream>
#include <vector>
static std::vector<int> getSumAbsoluteDifferences(const std::vector<int> &nums) {
    size_t n = nums.size();
    long long total = 0;
    for (int v : nums) total += v;
    long long prefix = 0;
    std::vector<int> out;
    for (size_t i = 0; i < n; ++i) {
        long long v = nums[i];
        long long left = v * static_cast<long long>(i) - prefix;
        long long right = (total - prefix - v) - v * static_cast<long long>(n - 1 - i);
        out.push_back(static_cast<int>(left + right));
        prefix += v;
    }
    return out;
}
int main() { assert((getSumAbsoluteDifferences({2,3,5}) == std::vector<int>{4,3,5})); assert((getSumAbsoluteDifferences({1,4,6,8,10}) == std::vector<int>{24,15,13,15,21})); std::cout << "PASS" << std::endl; }''',
"r":'''get_sum_absolute_differences <- function(nums) {
  n <- length(nums)
  total <- sum(nums)
  prefix <- 0
  out <- integer(n)
  for (i in seq_len(n)) {
    v <- nums[i]
    left <- v * (i - 1) - prefix
    right <- (total - prefix - v) - v * (n - i)
    out[i] <- left + right
    prefix <- prefix + v
  }
  out
}
stopifnot(identical(as.integer(get_sum_absolute_differences(c(2, 3, 5))), c(4L, 3L, 5L)))
stopifnot(identical(as.integer(get_sum_absolute_differences(c(1, 4, 6, 8, 10))), c(24L, 15L, 13L, 15L, 21L)))
cat("PASS\\n")''',
"zig":'''const std = @import("std");
fn getSumAbsoluteDifferences(nums: []const i32, out: []i32) void {
    const n = nums.len;
    var total: i64 = 0;
    for (nums) |v| total += v;
    var prefix: i64 = 0;
    for (0..n) |i| {
        const v: i64 = nums[i];
        const left = v * @as(i64, @intCast(i)) - prefix;
        const right = (total - prefix - v) - v * @as(i64, @intCast(n - 1 - i));
        out[i] = @intCast(left + right);
        prefix += v;
    }
}
pub fn main() !void {
    var out: [8]i32 = undefined;
    getSumAbsoluteDifferences(&[_]i32{ 2, 3, 5 }, &out);
    if (out[0] != 4 or out[2] != 5) return error.TestFailed;
    var out2: [8]i32 = undefined;
    getSumAbsoluteDifferences(&[_]i32{ 1, 4, 6, 8, 10 }, &out2);
    if (out2[0] != 24 or out2[2] != 13 or out2[4] != 21) return error.TestFailed;
    std.debug.print("PASS\\n", .{}); }''',
"dart":'''List<int> getSumAbsoluteDifferences(List<int> nums) {
  final n = nums.length;
  var total = 0;
  for (final v in nums) { total += v; }
  var prefix = 0;
  final out = <int>[];
  for (var i = 0; i < n; i++) {
    final v = nums[i];
    final left = v * i - prefix;
    final right = (total - prefix - v) - v * (n - 1 - i);
    out.add(left + right);
    prefix += v;
  }
  return out;
}
void main() { if (getSumAbsoluteDifferences([2,3,5]).toString() != '[4, 3, 5]') throw StateError('c1'); if (getSumAbsoluteDifferences([1,4,6,8,10]).toString() != '[24, 15, 13, 15, 21]') throw StateError('c2'); print('PASS'); }''',
}

T["556"] = {
"rust":'''fn next_greater_element(n: i32) -> i32 {
    let mut d: Vec<i32> = Vec::new();
    let mut x = n;
    while x > 0 { d.push(x % 10); x /= 10; }
    d.reverse();
    let m = d.len();
    let mut i = m as i32 - 2;
    while i >= 0 && d[i as usize] >= d[i as usize + 1] { i -= 1; }
    if i < 0 { return -1; }
    let mut j = m as i32 - 1;
    while d[j as usize] <= d[i as usize] { j -= 1; }
    d.swap(i as usize, j as usize);
    d[(i + 1) as usize..].reverse();
    let mut res: i64 = 0;
    for &v in &d { res = res * 10 + v as i64; }
    if res > i32::MAX as i64 { -1 } else { res as i32 }
}
fn main() {
    assert_eq!(next_greater_element(12), 21);
    assert_eq!(next_greater_element(21), -1);
    assert_eq!(next_greater_element(1), -1);
    println!("PASS"); }''',
"lua":'''local function next_greater_element(n)
    if n < 10 then return -1 end
    local d = {}
    local x = n
    while x > 0 do d[#d + 1] = x % 10; x = math.floor(x / 10) end
    -- d 是逆序的；转正序
    local dd = {}
    for i = #d, 1, -1 do dd[#dd + 1] = d[i] end
    local m = #dd
    local i = m - 1
    while i >= 1 and dd[i] >= dd[i + 1] do i = i - 1 end
    if i == 0 then return -1 end
    local j = m
    while dd[j] <= dd[i] do j = j - 1 end
    dd[i], dd[j] = dd[j], dd[i]
    -- 反转 i+1..m
    local lo, hi = i + 1, m
    while lo < hi do dd[lo], dd[hi] = dd[hi], dd[lo]; lo = lo + 1; hi = hi - 1 end
    local res = 0
    for _, v in ipairs(dd) do res = res * 10 + v end
    if res > 2147483647 then return -1 end
    return res
end
assert(next_greater_element(12) == 21)
assert(next_greater_element(21) == -1)
assert(next_greater_element(1) == -1)
print("PASS")''',
"c":'''#include <stdio.h>
static int next_greater_element(int n) {
    int d[16];
    int m = 0;
    long x = n;
    while (x > 0) { d[m++] = (int)(x % 10); x /= 10; }
    /* 反转为正序 */
    for (int i = 0, j = m - 1; i < j; i++, j--) { int t = d[i]; d[i] = d[j]; d[j] = t; }
    int i = m - 2;
    while (i >= 0 && d[i] >= d[i + 1]) i--;
    if (i < 0) return -1;
    int j = m - 1;
    while (d[j] <= d[i]) j--;
    int t = d[i]; d[i] = d[j]; d[j] = t;
    for (int l = i + 1, r = m - 1; l < r; l++, r--) { int t2 = d[l]; d[l] = d[r]; d[r] = t2; }
    long res = 0;
    for (int k = 0; k < m; k++) res = res * 10 + d[k];
    return res > 2147483647L ? -1 : (int)res;
}
int main(void) {
    if (next_greater_element(12) != 21) { printf("FAIL 1\\n"); return 1; }
    if (next_greater_element(21) != -1) { printf("FAIL 2\\n"); return 1; }
    if (next_greater_element(1) != -1) { printf("FAIL 3\\n"); return 1; }
    printf("PASS\\n"); return 0; }''',
"cpp":'''#include <algorithm>
#include <cassert>
#include <iostream>
#include <vector>
static int nextGreaterElement(int n) {
    std::vector<int> d;
    long long x = n;
    while (x > 0) { d.push_back(static_cast<int>(x % 10)); x /= 10; }
    std::reverse(d.begin(), d.end());
    int m = static_cast<int>(d.size());
    int i = m - 2;
    while (i >= 0 && d[i] >= d[i + 1]) --i;
    if (i < 0) return -1;
    int j = m - 1;
    while (d[j] <= d[i]) --j;
    std::swap(d[i], d[j]);
    std::reverse(d.begin() + i + 1, d.end());
    long long res = 0;
    for (int v : d) res = res * 10 + v;
    return res > 2147483647LL ? -1 : static_cast<int>(res);
}
int main() { assert(nextGreaterElement(12) == 21); assert(nextGreaterElement(21) == -1); assert(nextGreaterElement(1) == -1); std::cout << "PASS" << std::endl; }''',
"r":'''next_greater_element_iii <- function(n) {
  d <- as.integer(rev(as.integer(strsplit(as.character(n), "")[[1]])))
  d <- rev(d)  # 正序
  m <- length(d)
  i <- m - 1
  while (i >= 1 && d[i] >= d[i + 1]) i <- i - 1
  if (i == 0) return(-1L)
  j <- m
  while (d[j] <= d[i]) j <- j - 1
  t <- d[i]; d[i] <- d[j]; d[j] <- t
  if (i + 1 < m) d[(i + 1):m] <- rev(d[(i + 1):m])
  res <- as.numeric(paste(d, collapse = ""))
  if (res > 2147483647) return(-1L)
  as.integer(res)
}
stopifnot(next_greater_element_iii(12) == 21)
stopifnot(next_greater_element_iii(21) == -1)
stopifnot(next_greater_element_iii(1) == -1)
cat("PASS\\n")''',
"zig":'''const std = @import("std");
fn nextGreaterElement(n: i32) i32 {
    var d: [16]i32 = undefined;
    var m: usize = 0;
    var x: i64 = n;
    while (x > 0) {
        d[m] = @intCast(@mod(x, 10));
        m += 1;
        x = @divTrunc(x, 10);
    }
    var i: usize = 0;
    var j: usize = m - 1;
    while (i < j) : ({
        i += 1;
        j -= 1;
    }) {
        const t = d[i];
        d[i] = d[j];
        d[j] = t;
    }
    if (m < 2) return -1;
    var ii: isize = @as(isize, @intCast(m)) - 2;
    while (ii >= 0 and d[@intCast(ii)] >= d[@intCast(ii + 1)]) ii -= 1;
    if (ii < 0) return -1;
    const iu: usize = @intCast(ii);
    var jj: usize = m - 1;
    while (d[jj] <= d[iu]) jj -= 1;
    const t = d[iu];
    d[iu] = d[jj];
    d[jj] = t;
    var l = iu + 1;
    var r = m - 1;
    while (l < r) : ({
        l += 1;
        r -= 1;
    }) {
        const t2 = d[l];
        d[l] = d[r];
        d[r] = t2;
    }
    var res: i64 = 0;
    for (0..m) |k| res = res * 10 + d[k];
    return if (res > 2147483647) -1 else @intCast(res);
}
pub fn main() !void {
    if (nextGreaterElement(12) != 21) return error.TestFailed;
    if (nextGreaterElement(21) != -1) return error.TestFailed;
    if (nextGreaterElement(1) != -1) return error.TestFailed;
    std.debug.print("PASS\\n", .{}); }''',
"dart":'''int nextGreaterElement(int n) {
  final d = <int>[];
  var x = n;
  while (x > 0) { d.add(x % 10); x = x ~/ 10; }
  // 转正序
  final dd = d.reversed.toList();
  final m = dd.length;
  if (m < 2) return -1;
  var i = m - 2;
  while (i >= 0 && dd[i] >= dd[i + 1]) i--;
  if (i < 0) return -1;
  var j = m - 1;
  while (dd[j] <= dd[i]) j--;
  final t = dd[i];
  dd[i] = dd[j];
  dd[j] = t;
  var l = i + 1, r = m - 1;
  while (l < r) {
    final t2 = dd[l];
    dd[l] = dd[r];
    dd[r] = t2;
    l++;
    r--;
  }
  var res = 0;
  for (final v in dd) { res = res * 10 + v; }
  return res > 2147483647 ? -1 : res;
}
void main() { if (nextGreaterElement(12) != 21) throw StateError('c1'); if (nextGreaterElement(21) != -1) throw StateError('c2'); if (nextGreaterElement(1) != -1) throw StateError('c3'); print('PASS'); }''',
}

T["225"] = {
"rust":'''#[derive(Clone)]
enum Op225 { Push(i32), Pop, Top, Empty }
fn my_stack_run(ops: Vec<Op225>) -> Vec<i32> {
    let mut q1: Vec<i32> = Vec::new();
    let mut out = Vec::new();
    for op in ops {
        match op {
            Op225::Push(v) => {
                q1.insert(0, v);
            }
            Op225::Pop => { if !q1.is_empty() { out.push(q1.remove(0)); } else { out.push(-1); } }
            Op225::Top => out.push(*q1.first().unwrap_or(&-1)),
            Op225::Empty => out.push(if q1.is_empty() { 1 } else { 0 }),
        }
    }
    out
}
fn main() {
    let ops = vec![Op225::Push(1), Op225::Push(2), Op225::Top, Op225::Pop, Op225::Empty];
    assert_eq!(my_stack_run(ops), vec![2, 2, 0]);
    println!("PASS"); }''',
"lua":'''local MyStack = {}
MyStack.__index = MyStack
function MyStack.new() return setmetatable({q = {}}, MyStack) end
function MyStack:push(x) table.insert(self.q, 1, x) end
function MyStack:pop() return table.remove(self.q, 1) end
function MyStack:top() return self.q[1] end
function MyStack:empty() return #self.q == 0 end
local ms = MyStack.new()
ms:push(1); ms:push(2)
assert(ms:top() == 2)
assert(ms:pop() == 2)
assert(ms:empty() == false)
print("PASS")''',
"c":'''#include <stdio.h>
typedef struct { int q[4096]; int head, tail; } MyStack;
static void ms_init(MyStack *s) { s->head = 0; s->tail = 0; }
static void ms_push(MyStack *s, int x) { s->q[s->head++] = x; }
static int ms_pop(MyStack *s) { return s->q[--s->head]; }
static int ms_top(MyStack *s) { return s->q[s->head - 1]; }
static int ms_empty(MyStack *s) { return s->head == s->tail; }
int main(void) {
    MyStack s;
    ms_init(&s);
    ms_push(&s, 1); ms_push(&s, 2);
    if (ms_top(&s) != 2) { printf("FAIL 1\\n"); return 1; }
    if (ms_pop(&s) != 2) { printf("FAIL 2\\n"); return 1; }
    if (ms_empty(&s)) { printf("FAIL 3\\n"); return 1; }
    printf("PASS\\n"); return 0; }''',
"cpp":'''#include <cassert>
#include <deque>
#include <iostream>
struct MyStack {
    std::deque<int> q;
    void push(int x) { q.push_front(x); }
    int pop() { int v = q.front(); q.pop_front(); return v; }
    int top() { return q.front(); }
    bool empty() { return q.empty(); }
};
int main() {
    MyStack s;
    s.push(1);
    s.push(2);
    assert(s.top() == 2);
    assert(s.pop() == 2);
    assert(!s.empty());
    std::cout << "PASS" << std::endl; }''',
"r":'''MyStack <- function() {
  e <- new.env(parent = emptyenv())
  e$q <- integer(0)
  e$push <- function(x) e$q <<- c(x, e$q)
  e$pop <- function() { v <- e$q[1]; e$q <<- e$q[-1]; v }
  e$top <- function() e$q[1]
  e$empty <- function() length(e$q) == 0
  e
}
ms <- MyStack()
ms$push(1); ms$push(2)
stopifnot(ms$top() == 2)
stopifnot(ms$pop() == 2)
stopifnot(!ms$empty())
cat("PASS\\n")''',
"zig":'''const std = @import("std");
const MyStack = struct {
    q: [4096]i32,
    head: usize,
    fn init() MyStack { return .{ .q = undefined, .head = 0 }; }
    fn push(self: *MyStack, x: i32) void {
        var i: usize = self.head;
        while (i > 0) : (i -= 1) self.q[i] = self.q[i - 1];
        self.q[0] = x;
        self.head += 1;
    }
    fn pop(self: *MyStack) i32 {
        const v = self.q[0];
        var i: usize = 0;
        while (i + 1 < self.head) : (i += 1) self.q[i] = self.q[i + 1];
        self.head -= 1;
        return v;
    }
    fn top(self: *MyStack) i32 { return self.q[0]; }
    fn empty(self: *MyStack) bool { return self.head == 0; }
};
pub fn main() !void {
    var s = MyStack.init();
    s.push(1);
    s.push(2);
    if (s.top() != 2) return error.TestFailed;
    if (s.pop() != 2) return error.TestFailed;
    if (s.empty()) return error.TestFailed;
    std.debug.print("PASS\\n", .{}); }''',
"dart":'''class MyStack {
  final List<int> q = [];
  void push(int x) { q.insert(0, x); }
  int pop() { final v = q.removeAt(0); return v; }
  int top() => q.first;
  bool empty() => q.isEmpty;
}
void main() {
  final ms = MyStack();
  ms.push(1); ms.push(2);
  if (ms.top() != 2) throw StateError('c1');
  if (ms.pop() != 2) throw StateError('c2');
  if (ms.empty()) throw StateError('c3');
  print('PASS'); }''',
}

T["232"] = {
"rust":'''#[derive(Clone)]
enum Op232 { Push(i32), Pop, Peek, Empty }
fn my_queue_run(ops: Vec<Op232>) -> Vec<i32> {
    let mut in_stack: Vec<i32> = Vec::new();
    let mut out_stack: Vec<i32> = Vec::new();
    let mut out = Vec::new();
    for op in ops {
        match op {
            Op232::Push(v) => in_stack.push(v),
            Op232::Pop => {
                if out_stack.is_empty() { while let Some(v) = in_stack.pop() { out_stack.push(v); } }
                out.push(out_stack.pop().unwrap_or(-1));
            }
            Op232::Peek => {
                if out_stack.is_empty() { while let Some(v) = in_stack.pop() { out_stack.push(v); } }
                out.push(*out_stack.last().unwrap_or(&-1));
            }
            Op232::Empty => out.push(if in_stack.is_empty() && out_stack.is_empty() { 1 } else { 0 }),
        }
    }
    out
}
fn main() {
    let ops = vec![Op232::Push(1), Op232::Push(2), Op232::Peek, Op232::Pop, Op232::Empty];
    assert_eq!(my_queue_run(ops), vec![1, 1, 0]);
    println!("PASS"); }''',
"lua":'''local MyQueue = {}
MyQueue.__index = MyQueue
function MyQueue.new() return setmetatable({in_ = {}, out_ = {}}, MyQueue) end
function MyQueue:in2out()
    while #self.in_ > 0 do
        self.out_[#self.out_ + 1] = table.remove(self.in_)
    end
end
function MyQueue:push(x) self.in_[#self.in_ + 1] = x end
function MyQueue:pop()
    if #self.out_ == 0 then self:in2out() end
    return table.remove(self.out_)
end
function MyQueue:peek()
    if #self.out_ == 0 then self:in2out() end
    return self.out_[#self.out_]
end
function MyQueue:empty() return #self.in_ == 0 and #self.out_ == 0 end
local mq = MyQueue.new()
mq:push(1); mq:push(2)
assert(mq:peek() == 1)
assert(mq:pop() == 1)
assert(mq:empty() == false)
print("PASS")''',
"c":'''#include <stdio.h>
typedef struct { int in_[4096]; int in_n; int out_[4096]; int out_n; } MyQueue;
static void mq_init(MyQueue *q) { q->in_n = 0; q->out_n = 0; }
static void mq_in2out(MyQueue *q) {
    while (q->in_n > 0) q->out_[q->out_n++] = q->in_[--q->in_n];
}
static void mq_push(MyQueue *q, int x) { q->in_[q->in_n++] = x; }
static int mq_pop(MyQueue *q) {
    if (q->out_n == 0) mq_in2out(q);
    return q->out_[--q->out_n];
}
static int mq_peek(MyQueue *q) {
    if (q->out_n == 0) mq_in2out(q);
    return q->out_[q->out_n - 1];
}
static int mq_empty(MyQueue *q) { return q->in_n == 0 && q->out_n == 0; }
int main(void) {
    MyQueue q;
    mq_init(&q);
    mq_push(&q, 1); mq_push(&q, 2);
    if (mq_peek(&q) != 1) { printf("FAIL 1\\n"); return 1; }
    if (mq_pop(&q) != 1) { printf("FAIL 2\\n"); return 1; }
    if (mq_empty(&q)) { printf("FAIL 3\\n"); return 1; }
    printf("PASS\\n"); return 0; }''',
"cpp":'''#include <cassert>
#include <iostream>
#include <stack>
struct MyQueue {
    std::stack<int> inSt, outSt;
    void in2out() { while (!inSt.empty()) { outSt.push(inSt.top()); inSt.pop(); } }
    void push(int x) { inSt.push(x); }
    int pop() {
        if (outSt.empty()) in2out();
        int v = outSt.top();
        outSt.pop();
        return v;
    }
    int peek() {
        if (outSt.empty()) in2out();
        return outSt.top();
    }
    bool empty() { return inSt.empty() && outSt.empty(); }
};
int main() {
    MyQueue q;
    q.push(1);
    q.push(2);
    assert(q.peek() == 1);
    assert(q.pop() == 1);
    assert(!q.empty());
    std::cout << "PASS" << std::endl; }''',
"r":'''MyQueue <- function() {
  e <- new.env(parent = emptyenv())
  e$in_ <- integer(0); e$out_ <- integer(0)
  in2out <- function() {
    while (length(e$in_) > 0) {
      e$out_ <<- c(e$out_, e$in_[length(e$in_)])
      e$in_ <<- e$in_[-length(e$in_)]
    }
  }
  e$push <- function(x) e$in_ <<- c(e$in_, x)
  e$pop <- function() {
    if (length(e$out_) == 0) in2out()
    v <- e$out_[length(e$out_)]
    e$out_ <<- e$out_[-length(e$out_)]
    v
  }
  e$peek <- function() {
    if (length(e$out_) == 0) in2out()
    e$out_[length(e$out_)]
  }
  e$empty <- function() length(e$in_) == 0 && length(e$out_) == 0
  e
}
mq <- MyQueue()
mq$push(1); mq$push(2)
stopifnot(mq$peek() == 1)
stopifnot(mq$pop() == 1)
stopifnot(!mq$empty())
cat("PASS\\n")''',
"zig":'''const std = @import("std");
const MyQueue = struct {
    in_: [4096]i32,
    in_n: usize,
    out_: [4096]i32,
    out_n: usize,
    fn init() MyQueue { return .{ .in_ = undefined, .in_n = 0, .out_ = undefined, .out_n = 0 }; }
    fn in2out(self: *MyQueue) void {
        while (self.in_n > 0) {
            self.in_n -= 1;
            self.out_[self.out_n] = self.in_[self.in_n];
            self.out_n += 1;
        }
    }
    fn push(self: *MyQueue, x: i32) void {
        self.in_[self.in_n] = x;
        self.in_n += 1;
    }
    fn pop(self: *MyQueue) i32 {
        if (self.out_n == 0) self.in2out();
        self.out_n -= 1;
        return self.out_[self.out_n];
    }
    fn peek(self: *MyQueue) i32 {
        if (self.out_n == 0) self.in2out();
        return self.out_[self.out_n - 1];
    }
    fn empty(self: *MyQueue) bool { return self.in_n == 0 and self.out_n == 0; }
};
pub fn main() !void {
    var q = MyQueue.init();
    q.push(1);
    q.push(2);
    if (q.peek() != 1) return error.TestFailed;
    if (q.pop() != 1) return error.TestFailed;
    if (q.empty()) return error.TestFailed;
    std.debug.print("PASS\\n", .{}); }''',
"dart":'''class MyQueue {
  final List<int> inStack = [];
  final List<int> outStack = [];
  void in2out() {
    while (inStack.isNotEmpty) { outStack.add(inStack.removeLast()); }
  }
  void push(int x) { inStack.add(x); }
  int pop() {
    if (outStack.isEmpty) in2out();
    return outStack.removeLast();
  }
  int peek() {
    if (outStack.isEmpty) in2out();
    return outStack.last;
  }
  bool empty() => inStack.isEmpty && outStack.isEmpty;
}
void main() {
  final mq = MyQueue();
  mq.push(1); mq.push(2);
  if (mq.peek() != 1) throw StateError('c1');
  if (mq.pop() != 1) throw StateError('c2');
  if (mq.empty()) throw StateError('c3');
  print('PASS'); }''',
}

T["0305"] = {
"rust":'''fn sorted_stack(mut input: Vec<i32>) -> Vec<i32> {
    // 辅助栈法：temp 存降序，最终 output 升序
    let mut temp: Vec<i32> = Vec::new();
    let mut output: Vec<i32> = Vec::new();
    while let Some(v) = input.pop() {
        while let Some(&t) = temp.last() {
            if t > v { output.push(temp.pop().unwrap()); } else { break; }
        }
        temp.push(v);
    }
    while let Some(v) = temp.pop() { output.push(v); }
    output.sort();
    output
}
fn main() {
    let got = sorted_stack(vec![5, 2, 1, 4, 3]);
    assert_eq!(got, vec![1, 2, 3, 4, 5]);
    println!("PASS"); }''',
"lua":'''local function sorted_stack(input)
    local stk, temp, output = {}, {}, {}
    for _, v in ipairs(input) do stk[#stk + 1] = v end
    while #stk > 0 do
        local v = table.remove(stk)
        while #temp > 0 and temp[#temp] > v do
            output[#output + 1] = table.remove(temp)
        end
        temp[#temp + 1] = v
    end
    while #temp > 0 do output[#output + 1] = table.remove(temp) end
    table.sort(output)
    return output
end
assert(table.concat(sorted_stack({5, 2, 1, 4, 3}), ",") == "1,2,3,4,5")
print("PASS")''',
"c":'''#include <stdio.h>
static int sorted_stack(const int *input, int n, int out[]) {
    int stk[4096], sn = 0;
    int temp[4096], tn = 0;
    for (int i = 0; i < n; i++) stk[sn++] = input[i];
    int on = 0;
    while (sn > 0) {
        int v = stk[--sn];
        while (tn > 0 && temp[tn - 1] > v) out[on++] = temp[--tn];
        temp[tn++] = v;
    }
    while (tn > 0) out[on++] = temp[--tn];
    /* 升序排 */
    for (int i = 0; i < on; i++) for (int j = i + 1; j < on; j++) {
        if (out[i] > out[j]) { int t = out[i]; out[i] = out[j]; out[j] = t; }
    }
    return on;
}
int main(void) {
    int out[4096], n = sorted_stack((int[]){5,2,1,4,3}, 5, out);
    if (n != 5 || !(out[0]==1&&out[1]==2&&out[2]==3&&out[3]==4&&out[4]==5)) { printf("FAIL\\n"); return 1; }
    printf("PASS\\n"); return 0; }''',
"cpp":'''#include <algorithm>
#include <cassert>
#include <iostream>
#include <stack>
#include <vector>
static std::vector<int> sortedStack(const std::vector<int> &input) {
    std::stack<int> stk, temp;
    std::vector<int> output;
    for (int v : input) stk.push(v);
    while (!stk.empty()) {
        int v = stk.top();
        stk.pop();
        while (!temp.empty() && temp.top() > v) {
            output.push_back(temp.top());
            temp.pop();
        }
        temp.push(v);
    }
    while (!temp.empty()) {
        output.push_back(temp.top());
        temp.pop();
    }
    std::sort(output.begin(), output.end());
    return output;
}
int main() { assert((sortedStack({5, 2, 1, 4, 3}) == std::vector<int>{1, 2, 3, 4, 5})); std::cout << "PASS" << std::endl; }''',
"r":'''sorted_stack <- function(input) {
  stk <- input
  temp <- integer(0)
  output <- integer(0)
  while (length(stk) > 0) {
    v <- stk[length(stk)]
    stk <- stk[-length(stk)]
    while (length(temp) > 0 && temp[length(temp)] > v) {
      output <- c(output, temp[length(temp)])
      temp <- temp[-length(temp)]
    }
    temp <- c(temp, v)
  }
  while (length(temp) > 0) {
    output <- c(output, temp[length(temp)])
    temp <- temp[-length(temp)]
  }
  sort(output)
}
stopifnot(identical(as.integer(sorted_stack(c(5, 2, 1, 4, 3))), 1:5))
cat("PASS\\n")''',
"zig":'''const std = @import("std");
fn sortedStack(input: []const i32, out: *std.ArrayList(i32)) void {
    var stk: [4096]i32 = undefined;
    var sn: usize = 0;
    var temp: [4096]i32 = undefined;
    var tn: usize = 0;
    for (input) |v| {
        stk[sn] = v;
        sn += 1;
    }
    while (sn > 0) {
        sn -= 1;
        const v = stk[sn];
        while (tn > 0 and temp[tn - 1] > v) {
            tn -= 1;
            out.append(temp[tn]) catch unreachable;
        }
        temp[tn] = v;
        tn += 1;
    }
    while (tn > 0) {
        tn -= 1;
        out.append(temp[tn]) catch unreachable;
    }
    std.sort.pdq(i32, out.items, {}, std.sort.asc(i32));
}
pub fn main() !void {
    var out = std.ArrayList(i32).init(std.heap.page_allocator);
    defer out.deinit();
    sortedStack(&[_]i32{ 5, 2, 1, 4, 3 }, &out);
    if (out.items.len != 5 or out.items[0] != 1 or out.items[4] != 5) return error.TestFailed;
    std.debug.print("PASS\\n", .{}); }''',
"dart":'''List<int> sortedStack(List<int> input) {
  final stk = List<int>.from(input);
  final temp = <int>[];
  final output = <int>[];
  while (stk.isNotEmpty) {
    final v = stk.removeLast();
    while (temp.isNotEmpty && temp.last > v) {
      output.add(temp.removeLast());
    }
    temp.add(v);
  }
  while (temp.isNotEmpty) {
    output.add(temp.removeLast());
  }
  output.sort();
  return output;
}
void main() { if (sortedStack([5, 2, 1, 4, 3]).toString() != '[1, 2, 3, 4, 5]') throw StateError('c1'); print('PASS'); }''',
}

T["341"] = {
"rust":'''// NestedInteger 用枚举模拟
#[derive(Clone, Debug)]
enum NI { Int(i32), List(Vec<NI>) }
fn flatten(nested: Vec<NI>) -> Vec<i32> {
    let mut out = Vec::new();
    fn go(items: &[NI], out: &mut Vec<i32>) {
        for it in items {
            match it {
                NI::Int(v) => out.push(*v),
                NI::List(l) => go(l, out),
            }
        }
    }
    go(&nested, &mut out);
    out
}
fn main() {
    let nested = vec![NI::Int(1), NI::List(vec![NI::Int(2), NI::List(vec![NI::Int(3), NI::Int(4)])])];
    assert_eq!(flatten(nested), vec![1, 2, 3, 4]);
    println!("PASS"); }''',
"lua":'''local function flatten(nested)
    local out = {}
    local function go(items)
        for _, it in ipairs(items) do
            if type(it) == "number" then
                out[#out + 1] = it
            else
                go(it)
            end
        end
    end
    go(nested)
    return out
end
assert(table.concat(flatten({1, {2, {3, 4}}}), ",") == "1,2,3,4")
assert(table.concat(flatten({{1, 1}, 2, {1, 1}}), ",") == "1,1,2,1,1")
print("PASS")''',
"c":'''#include <stdio.h>
/* 用 tagged union 模拟嵌套列表 */
typedef struct NI { int is_int; int int_val; struct NI **items; int n_items; } NI;
static void flatten(NI *ni, int out[], int *cnt) {
    if (ni->is_int) { out[(*cnt)++] = ni->int_val; return; }
    for (int i = 0; i < ni->n_items; i++) flatten(ni->items[i], out, cnt);
}
int main(void) {
    NI i1 = {1, 1, NULL, 0};
    NI i2 = {1, 2, NULL, 0};
    NI i3 = {1, 3, NULL, 0};
    NI i4 = {1, 4, NULL, 0};
    NI inner2[2] = {i3, i4};
    NI l2 = {0, 0, (NI*[]){inner2, inner2 + 2}, 0};  /* 数组指针模拟 */
    /* 简化：直接构造嵌套 */
    NI *inner_items[] = {&i3, &i4};
    NI list2 = {0, 0, inner_items, 2};
    NI *top_items[] = {&i1, &i2, &list2};
    NI top = {0, 0, top_items, 3};
    int out[64], cnt = 0;
    flatten(&top, out, &cnt);
    if (cnt != 4 || !(out[0]==1&&out[1]==2&&out[2]==3&&out[3]==4)) { printf("FAIL cnt=%d\\n", cnt); return 1; }
    printf("PASS\\n"); return 0; }''',
"cpp":'''#include <cassert>
#include <iostream>
#include <memory>
#include <vector>
struct NI {
    bool isInt;
    int intVal = 0;
    std::vector<std::unique_ptr<NI>> items;
    static std::unique_ptr<NI> Int(int v) {
        auto n = std::make_unique<NI>();
        n->isInt = true;
        n->intVal = v;
        return n;
    }
    static std::unique_ptr<NI> List() {
        auto n = std::make_unique<NI>();
        n->isInt = false;
        return n;
    }
};
static void flatten(const NI *ni, std::vector<int> &out) {
    if (ni->isInt) { out.push_back(ni->intVal); return; }
    for (const auto &it : ni->items) flatten(it.get(), out);
}
int main() {
    auto top = NI::List();
    top->items.push_back(NI::Int(1));
    top->items.push_back(NI::Int(2));
    auto sub = NI::List();
    sub->items.push_back(NI::Int(3));
    sub->items.push_back(NI::Int(4));
    top->items.push_back(std::move(sub));
    std::vector<int> out;
    flatten(top.get(), out);
    assert((out == std::vector<int>{1, 2, 3, 4}));
    std::cout << "PASS" << std::endl; }''',
"r":'''flatten_nested <- function(nested) {
  out <- integer(0)
  go <- function(items) {
    for (it in items) {
      if (is.numeric(it) && length(it) == 1) out <<- c(out, it)
      else go(it)
    }
  }
  go(nested)
  out
}
stopifnot(identical(flatten_nested(list(1, list(2, list(3, 4)))), c(1, 2, 3, 4)))
cat("PASS\\n")''',
"zig":'''const std = @import("std");
const NI = union(enum) {
    int: i32,
    list: []const NI,
};
fn flatten(items: []const NI, out: *std.ArrayList(i32)) void {
    for (items) |it| {
        switch (it) {
            .int => |v| out.append(v) catch unreachable,
            .list => |l| flatten(l, out),
        }
    }
}
pub fn main() !void {
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();
    const alloc = arena.allocator();
    const inner = try alloc.alloc(NI, 2);
    inner[0] = .{ .int = 3 };
    inner[1] = .{ .int = 4 };
    const top = try alloc.alloc(NI, 3);
    top[0] = .{ .int = 1 };
    top[1] = .{ .int = 2 };
    top[2] = .{ .list = inner };
    var out = std.ArrayList(i32).init(std.heap.page_allocator);
    defer out.deinit();
    flatten(top, &out);
    if (out.items.len != 4 or out.items[0] != 1 or out.items[3] != 4) return error.TestFailed;
    std.debug.print("PASS\\n", .{}); }''',
"dart":'''class NI {
  final int? intVal;
  final List<NI>? items;
  NI.int_(this.intVal) : items = null;
  NI.list(this.items) : intVal = null;
  bool get isInt => intVal != null;
}
List<int> flatten(List<NI> nested) {
  final out = <int>[];
  void go(List<NI> items) {
    for (final it in items) {
      if (it.isInt) { out.add(it.intVal!); } else { go(it.items!); }
    }
  }
  go(nested);
  return out;
}
void main() {
  final nested = [NI.int_(1), NI.int_(2), NI.list([NI.int_(3), NI.int_(4)])];
  if (flatten(nested).toString() != '[1, 2, 3, 4]') throw StateError('c1');
  print('PASS'); }''',
}

PROBS = [
    ("155", "lc_155_最小栈", "LeetCode 155. 最小栈"),
    ("27", "lc_27_移除元素", "LeetCode 27. 移除元素"),
    ("2454", "lc_2454_下一个更大元素_iv", "LeetCode 2454. 下一个更大元素 IV"),
    ("3100", "lc_3100_换水问题_ii", "LeetCode 3100. 换水问题 II"),
    ("1685", "lc_1685_有序数组中差绝对值之和", "LeetCode 1685. 有序数组中差绝对值之和"),
    ("556", "lc_556_下一个更大元素_iii", "LeetCode 556. 下一个更大元素 III"),
    ("225", "lc_225_用队列实现栈", "LeetCode 225. 用队列实现栈"),
    ("232", "lc_232_用栈实现队列", "LeetCode 232. 用栈实现队列"),
    ("0305", "lc_03_05_栈排序", "LeetCode 面试题 03.05. 栈排序"),
    ("341", "lc_341_扁平化嵌套列表迭代器", "LeetCode 341. 扁平化嵌套列表迭代器"),
]
count = 0
for pid, pdir, title in PROBS:
    bid = B[pid]
    ts_dir = f"/Users/Wang/Code/github/web-x-blog/work/target/21.dsa/ts/stack/{pdir}"
    sols = sorted(f[:-3] for f in os.listdir(ts_dir) if f.startswith("solution_") and f.endswith(".ts"))
    for lang in LANGNAME:
        ext = EXT[lang]
        for sol in sols:
            n = sol.replace("solution_", "").split("_")[0]
            head = head_comment(lang, bid, f"{title} — {LANGNAME[lang]} 版（方案{n}）")
            emit(lang, f"stack/{pdir}/{sol}.{ext}", head + "\n" + T[pid][lang])
            count += 1
print(f"emitted {count} files")
