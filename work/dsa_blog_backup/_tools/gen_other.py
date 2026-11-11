#!/usr/bin/env python3
# gen_other.py — other 主题 7 题 × 7语言
import sys, os; sys.path.insert(0, "/Users/Wang/Code/webfault-ai/dsa/_tools")
from langlib import emit, head_comment, EXT

B = {"202": "135124945", "2166": "145556343", "217": "135038527", "242": "135154838", "292": "135424151", "326": "135359346", "1797": "145634738"}
LANGNAME = {"rust": "Rust", "lua": "Lua", "c": "C", "cpp": "C++", "r": "R", "zig": "Zig", "dart": "Dart"}

A202 = {
"rust": '''fn bit_square_sum(mut n: i64) -> i64 {
    let mut s = 0i64;
    while n > 0 { let d = n % 10; s += d * d; n /= 10; }
    s
}
fn is_happy(mut n: i64) -> bool {
    use std::collections::HashSet;
    let mut seen: HashSet<i64> = HashSet::new();
    while n != 1 && !seen.contains(&n) {
        seen.insert(n);
        n = bit_square_sum(n);
    }
    n == 1
}
fn main() {
    assert_eq!(bit_square_sum(1), 1);
    assert_eq!(bit_square_sum(19), 82);
    assert_eq!(bit_square_sum(82), 68);
    assert!(is_happy(19));
    assert!(is_happy(1));
    assert!(!is_happy(2));
    println!("PASS");
}
''',
"lua": '''local function bit_square_sum(n)
    local s = 0
    while n > 0 do
        local d = n % 10
        s = s + d * d
        n = math.floor(n / 10)
    end
    return s
end
local function is_happy(n)
    local seen = {}
    while n ~= 1 and not seen[n] do
        seen[n] = true
        n = bit_square_sum(n)
    end
    return n == 1
end
assert(bit_square_sum(1) == 1)
assert(bit_square_sum(19) == 82)
assert(bit_square_sum(82) == 68)
assert(is_happy(19) == true)
assert(is_happy(1) == true)
assert(is_happy(2) == false)
print("PASS")
''',
"c": '''#include <stdio.h>
static long bit_square_sum(long n) {
    long s = 0;
    while (n > 0) { long d = n % 10; s += d * d; n /= 10; }
    return s;
}
static int is_happy(long n) {
    long seen[1024];
    int cnt = 0;
    while (n != 1) {
        for (int i = 0; i < cnt; i++) if (seen[i] == n) return 0;
        if (cnt < 1024) seen[cnt++] = n;
        n = bit_square_sum(n);
    }
    return 1;
}
int main(void) {
    if (bit_square_sum(1) != 1) { printf("FAIL a1\\n"); return 1; }
    if (bit_square_sum(19) != 82) { printf("FAIL a2\\n"); return 1; }
    if (bit_square_sum(82) != 68) { printf("FAIL a3\\n"); return 1; }
    if (!is_happy(19) || !is_happy(1) || is_happy(2)) { printf("FAIL b\\n"); return 1; }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''#include <cassert>
#include <iostream>
#include <unordered_set>
static long long bitSquareSum(long long n) {
    long long s = 0;
    while (n > 0) { long long d = n % 10; s += d * d; n /= 10; }
    return s;
}
static bool isHappy(long long n) {
    std::unordered_set<long long> seen;
    while (n != 1 && !seen.count(n)) {
        seen.insert(n);
        n = bitSquareSum(n);
    }
    return n == 1;
}
int main() {
    assert(bitSquareSum(1) == 1);
    assert(bitSquareSum(19) == 82);
    assert(bitSquareSum(82) == 68);
    assert(isHappy(19));
    assert(isHappy(1));
    assert(!isHappy(2));
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''bit_square_sum <- function(n) {
  s <- 0
  while (n > 0) {
    d <- n %% 10
    s <- s + d * d
    n <- n %/% 10
  }
  s
}
is_happy <- function(n) {
  seen <- new.env(parent = emptyenv())
  while (n != 1 && is.null(seen[[as.character(n)]])) {
    seen[[as.character(n)]] <- TRUE
    n <- bit_square_sum(n)
  }
  n == 1
}
stopifnot(bit_square_sum(1) == 1, bit_square_sum(19) == 82, bit_square_sum(82) == 68)
stopifnot(is_happy(19), is_happy(1), !is_happy(2))
cat("PASS\\n")
''',
"zig": '''const std = @import("std");
fn bitSquareSum(n0: i64) i64 {
    var s: i64 = 0;
    var n = n0;
    while (n > 0) : (n = @divTrunc(n, 10)) {
        const d = @mod(n, 10);
        s += d * d;
    }
    return s;
}
fn isHappy(n0: i64) bool {
    var seen_buf: [1024]i64 = undefined;
    var cnt: usize = 0;
    var n = n0;
    while (n != 1) {
        for (seen_buf[0..cnt]) |v| if (v == n) return false;
        if (cnt < seen_buf.len) { seen_buf[cnt] = n; cnt += 1; }
        n = bitSquareSum(n);
    }
    return true;
}
pub fn main() !void {
    if (bitSquareSum(1) != 1) return error.TestFailed;
    if (bitSquareSum(19) != 82) return error.TestFailed;
    if (bitSquareSum(82) != 68) return error.TestFailed;
    if (!isHappy(19) or !isHappy(1) or isHappy(2)) return error.TestFailed;
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''int bitSquareSum(int n) {
  var s = 0;
  while (n > 0) {
    final d = n % 10;
    s += d * d;
    n = n ~/ 10;
  }
  return s;
}
bool isHappy(int n) {
  final seen = <int>{};
  while (n != 1 && !seen.contains(n)) {
    seen.add(n);
    n = bitSquareSum(n);
  }
  return n == 1;
}
void main() {
  if (bitSquareSum(1) != 1) throw StateError('a1');
  if (bitSquareSum(19) != 82) throw StateError('a2');
  if (bitSquareSum(82) != 68) throw StateError('a3');
  if (!isHappy(19) || !isHappy(1) || isHappy(2)) throw StateError('b');
  print('PASS');
}
''',
}

A2166 = {
"rust": '''struct Bitset { n: usize, words: Vec<u32>, ones: usize, reverse: u32 }
impl Bitset {
    fn new(size: usize) -> Self { Bitset { n: size, words: vec![0; (size + 31) / 32], ones: 0, reverse: 0 } }
    fn get(&self, idx: usize) -> u32 { ((self.words[idx / 32] >> (idx % 32)) & 1) ^ self.reverse }
    fn fix(&mut self, idx: usize) { if self.get(idx) == 0 { self.words[idx / 32] |= 1 << (idx % 32); self.ones += 1; } }
    fn unfix(&mut self, idx: usize) { if self.get(idx) == 1 { self.words[idx / 32] &= !(1 << (idx % 32)); self.ones -= 1; } }
    fn flip(&mut self) { self.reverse ^= 1; self.ones = self.n - self.ones; }
    fn all(&self) -> bool { self.ones == self.n }
    fn one(&self) -> bool { self.ones > 0 }
    fn count(&self) -> usize { self.ones }
    fn to_string(&self) -> String { (0..self.n).map(|i| char::from(b'0' + self.get(i) as u8)).collect() }
}
fn main() {
    let mut bs = Bitset::new(5);
    bs.fix(0); bs.fix(3);
    assert_eq!(bs.to_string(), "10010");
    assert_eq!(bs.count(), 2);
    bs.flip();
    assert_eq!(bs.to_string(), "01101");
    assert_eq!(bs.count(), 3);
    bs.unfix(0);
    assert_eq!(bs.to_string(), "01101");
    assert!(!bs.all() && bs.one());
    println!("PASS");
}
''',
"lua": '''local Bitset = {}
Bitset.__index = Bitset
function Bitset.new(size)
    return setmetatable({n = size, words = {}, ones = 0, reverse = 0}, Bitset)
end
function Bitset:get(idx)
    local w = self.words[(idx >> 5) + 1] or 0
    return ((w >> (idx & 31)) & 1) ~ self.reverse
end
function Bitset:fix(idx)
    if self:get(idx) == 0 then
        self.words[(idx >> 5) + 1] = (self.words[(idx >> 5) + 1] or 0) | (1 << (idx & 31))
        self.ones = self.ones + 1
    end
end
function Bitset:unfix(idx)
    if self:get(idx) == 1 then
        self.words[(idx >> 5) + 1] = (self.words[(idx >> 5) + 1] or 0) & ~(1 << (idx & 31))
        self.ones = self.ones - 1
    end
end
function Bitset:flip()
    self.reverse = self.reverse ~ 1
    self.ones = self.n - self.ones
end
function Bitset:all() return self.ones == self.n end
function Bitset:one() return self.ones > 0 end
function Bitset:count() return self.ones end
function Bitset:tostring()
    local s = {}
    for i = 0, self.n - 1 do s[#s + 1] = tostring(self:get(i)) end
    return table.concat(s)
end
local bs = Bitset.new(5)
bs:fix(0); bs:fix(3)
assert(bs:tostring() == "10010")
assert(bs:count() == 2)
bs:flip()
assert(bs:tostring() == "01101")
assert(bs:count() == 3)
bs:unfix(0)
assert(bs:tostring() == "01101")
assert(bs:all() == false and bs:one() == true)
print("PASS")
''',
"c": '''#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef struct { int n; unsigned *words; int ones; unsigned reverse; } Bitset;
static Bitset *bs_new(int size) {
    Bitset *b = malloc(sizeof(Bitset));
    b->n = size;
    b->words = calloc((size + 31) / 32, sizeof(unsigned));
    b->ones = 0; b->reverse = 0;
    return b;
}
static unsigned bs_get(Bitset *b, int idx) { return ((b->words[idx >> 5] >> (idx & 31)) & 1u) ^ b->reverse; }
static void bs_fix(Bitset *b, int idx) { if (bs_get(b, idx) == 0) { b->words[idx >> 5] |= 1u << (idx & 31); b->ones++; } }
static void bs_unfix(Bitset *b, int idx) { if (bs_get(b, idx) == 1) { b->words[idx >> 5] &= ~(1u << (idx & 31)); b->ones--; } }
static void bs_flip(Bitset *b) { b->reverse ^= 1; b->ones = b->n - b->ones; }
static int bs_all(Bitset *b) { return b->ones == b->n; }
static int bs_one(Bitset *b) { return b->ones > 0; }
static void bs_str(Bitset *b, char out[]) {
    for (int i = 0; i < b->n; i++) out[i] = '0' + bs_get(b, i);
    out[b->n] = '\\0';
}
int main(void) {
    Bitset *b = bs_new(5);
    char s[64];
    bs_fix(b, 0); bs_fix(b, 3);
    bs_str(b, s);
    if (strcmp(s, "10010") != 0) { printf("FAIL s1 %s\\n", s); return 1; }
    if (b->ones != 2) { printf("FAIL c1\\n"); return 1; }
    bs_flip(b);
    bs_str(b, s);
    if (strcmp(s, "01101") != 0) { printf("FAIL s2 %s\\n", s); return 1; }
    if (b->ones != 3) { printf("FAIL c2\\n"); return 1; }
    bs_unfix(b, 0);
    bs_str(b, s);
    if (strcmp(s, "01101") != 0) { printf("FAIL s3 %s\\n", s); return 1; }
    if (bs_all(b) || !bs_one(b)) { printf("FAIL ao\\n"); return 1; }
    free(b->words); free(b);
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''#include <cassert>
#include <iostream>
#include <string>
#include <vector>
struct Bitset {
    int n;
    std::vector<unsigned> words;
    int ones = 0;
    unsigned reverse = 0;
    explicit Bitset(int size) : n(size), words((size + 31) / 32, 0u) {}
    unsigned get(int idx) const { return ((words[idx >> 5] >> (idx & 31)) & 1u) ^ reverse; }
    void fix(int idx) { if (get(idx) == 0) { words[idx >> 5] |= 1u << (idx & 31); ++ones; } }
    void unfix(int idx) { if (get(idx) == 1) { words[idx >> 5] &= ~(1u << (idx & 31)); --ones; } }
    void flip() { reverse ^= 1; ones = n - ones; }
    bool all() const { return ones == n; }
    bool one() const { return ones > 0; }
    int count() const { return ones; }
    std::string toString() const {
        std::string s;
        for (int i = 0; i < n; ++i) s.push_back('0' + static_cast<char>(get(i)));
        return s;
    }
};
int main() {
    Bitset bs(5);
    bs.fix(0); bs.fix(3);
    assert(bs.toString() == "10010");
    assert(bs.count() == 2);
    bs.flip();
    assert(bs.toString() == "01101");
    assert(bs.count() == 3);
    bs.unfix(0);
    assert(bs.toString() == "01101");
    assert(!bs.all() && bs.one());
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''Bitset <- function(size) {
  e <- new.env(parent = emptyenv())
  e$n <- size; e$words <- rep(0, (size + 31) %/% 32); e$ones <- 0L; e$reverse <- 0L
  e$get <- function(idx) bitwXor(bitwAnd(bitwShiftL(1L, idx %% 32L) == e$words[(idx %/% 32) + 1L], ...) # placeholder
  e
}
''',
"zig": '''const std = @import("std");
const Bitset = struct {
    n: usize,
    words: []u32,
    ones: usize,
    reverse: u32,
    fn init(alloc: std.mem.Allocator, size: usize) !Bitset {
        const words = try alloc.alloc(u32, (size + 31) / 32);
        @memset(words, 0);
        return .{ .n = size, .words = words, .ones = 0, .reverse = 0 };
    }
    fn get(self: *const Bitset, idx: usize) u32 {
        return ((self.words[idx / 32] >> @intCast(idx % 32)) & 1) ^ self.reverse;
    }
    fn fix(self: *Bitset, idx: usize) void {
        if (self.get(idx) == 0) {
            self.words[idx / 32] |= @as(u32, 1) << @intCast(idx % 32);
            self.ones += 1;
        }
    }
    fn unfix(self: *Bitset, idx: usize) void {
        if (self.get(idx) == 1) {
            self.words[idx / 32] &= ~(@as(u32, 1) << @intCast(idx % 32));
            self.ones -= 1;
        }
    }
    fn flip(self: *Bitset) void {
        self.reverse ^= 1;
        self.ones = self.n - self.ones;
    }
    fn all(self: *const Bitset) bool { return self.ones == self.n; }
    fn one(self: *const Bitset) bool { return self.ones > 0; }
    fn toStr(self: *const Bitset, out: []u8) void {
        for (0..self.n) |i| out[i] = '0' + @as(u8, @intCast(self.get(i)));
    }
};
pub fn main() !void {
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();
    var bs = try Bitset.init(arena.allocator(), 5);
    var buf: [64]u8 = undefined;
    bs.fix(0); bs.fix(3);
    bs.toStr(&buf);
    if (!std.mem.eql(u8, buf[0..5], "10010")) return error.TestFailed;
    if (bs.ones != 2) return error.TestFailed;
    bs.flip();
    bs.toStr(&buf);
    if (!std.mem.eql(u8, buf[0..5], "01101")) return error.TestFailed;
    if (bs.ones != 3) return error.TestFailed;
    bs.unfix(0);
    bs.toStr(&buf);
    if (!std.mem.eql(u8, buf[0..5], "01101")) return error.TestFailed;
    if (bs.all() or !bs.one()) return error.TestFailed;
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''class Bitset {
  final int n;
  final List<int> words;
  int ones = 0;
  int reverse = 0;
  Bitset(this.n) : words = List.filled((n + 31) ~/ 32, 0);
  int getBit(int idx) => ((words[idx >> 5] >> (idx & 31)) & 1) ^ reverse;
  void fix(int idx) {
    if (getBit(idx) == 0) {
      words[idx >> 5] |= 1 << (idx & 31);
      ones++;
    }
  }
  void unfix(int idx) {
    if (getBit(idx) == 1) {
      words[idx >> 5] &= ~(1 << (idx & 31));
      ones--;
    }
  }
  void flip() {
    reverse ^= 1;
    ones = n - ones;
  }
  bool all() => ones == n;
  bool one() => ones > 0;
  int count() => ones;
  String toString() {
    final sb = StringBuffer();
    for (var i = 0; i < n; i++) {
      sb.write(getBit(i));
    }
    return sb.toString();
  }
}
void main() {
  final bs = Bitset(5);
  bs.fix(0); bs.fix(3);
  if (bs.toString() != '10010') throw StateError('s1');
  if (bs.count() != 2) throw StateError('c1');
  bs.flip();
  if (bs.toString() != '01101') throw StateError('s2');
  if (bs.count() != 3) throw StateError('c2');
  bs.unfix(0);
  if (bs.toString() != '01101') throw StateError('s3');
  if (bs.all() || !bs.one()) throw StateError('ao');
  print('PASS');
}
''',
}

A217 = {
"rust": '''use std::collections::HashSet;
fn contains_duplicate(nums: &[i32]) -> bool {
    let set: HashSet<i32> = nums.iter().cloned().collect();
    set.len() != nums.len()
}
fn main() {
    assert!(contains_duplicate(&[1, 2, 3, 1]));
    assert!(!contains_duplicate(&[1, 2, 3, 4]));
    println!("PASS");
}
''',
"lua": '''local function contains_duplicate(nums)
    local set = {}
    local cnt = 0
    for _, v in ipairs(nums) do
        if not set[v] then set[v] = true; cnt = cnt + 1 end
    end
    return cnt ~= #nums
end
assert(contains_duplicate({1, 2, 3, 1}) == true)
assert(contains_duplicate({1, 2, 3, 4}) == false)
print("PASS")
''',
"c": '''#include <stdio.h>
#include <stdlib.h>
static int cmp_int(const void *a, const void *b) { return *(const int *)a - *(const int *)b; }
static int contains_duplicate(const int *nums, int n) {
    if (n <= 1) return 0;
    int *sorted = malloc(sizeof(int) * n);
    for (int i = 0; i < n; i++) sorted[i] = nums[i];
    qsort(sorted, n, sizeof(int), cmp_int);
    int dup = 0;
    for (int i = 1; i < n; i++) if (sorted[i] == sorted[i - 1]) { dup = 1; break; }
    free(sorted);
    return dup;
}
int main(void) {
    if (!contains_duplicate((int[]){1,2,3,1}, 4)) { printf("FAIL 1\\n"); return 1; }
    if (contains_duplicate((int[]){1,2,3,4}, 4)) { printf("FAIL 2\\n"); return 1; }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''#include <cassert>
#include <iostream>
#include <unordered_set>
#include <vector>
static bool containsDuplicate(const std::vector<int> &nums) {
    return std::unordered_set<int>(nums.begin(), nums.end()).size() != nums.size();
}
int main() {
    assert(containsDuplicate({1, 2, 3, 1}));
    assert(!containsDuplicate({1, 2, 3, 4}));
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''contains_duplicate <- function(nums) length(unique(nums)) != length(nums)
stopifnot(contains_duplicate(c(1, 2, 3, 1)))
stopifnot(!contains_duplicate(c(1, 2, 3, 4)))
cat("PASS\\n")
''',
"zig": '''const std = @import("std");
fn containsDuplicate(nums: []const i32, alloc: std.mem.Allocator) bool {
    var set = std.AutoHashMap(i32, void).init(alloc);
    defer set.deinit();
    for (nums) |v| {
        if (set.contains(v)) return true;
        set.put(v, {}) catch unreachable;
    }
    return false;
}
pub fn main() !void {
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();
    if (!containsDuplicate(&[_]i32{ 1, 2, 3, 1 }, arena.allocator())) return error.TestFailed;
    if (containsDuplicate(&[_]i32{ 1, 2, 3, 4 }, arena.allocator())) return error.TestFailed;
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''bool containsDuplicate(List<int> nums) => nums.toSet().length != nums.length;
void main() {
  if (!containsDuplicate([1, 2, 3, 1])) throw StateError('c1');
  if (containsDuplicate([1, 2, 3, 4])) throw StateError('c2');
  print('PASS');
}
''',
}

A242 = {
"rust": '''fn is_anagram(s: &str, t: &str) -> bool {
    if s.len() != t.len() { return false; }
    let mut a: Vec<char> = s.chars().collect();
    let mut b: Vec<char> = t.chars().collect();
    a.sort();
    b.sort();
    a == b
}
fn main() {
    assert!(is_anagram("anagram", "nagaram"));
    assert!(!is_anagram("rat", "car"));
    println!("PASS");
}
''',
"lua": '''local function is_anagram(s, t)
    if #s ~= #t then return false end
    local a, b = {}, {}
    s:gsub(".", function(c) a[#a + 1] = c end)
    t:gsub(".", function(c) b[#b + 1] = c end)
    table.sort(a)
    table.sort(b)
    for i = 1, #a do
        if a[i] ~= b[i] then return false end
    end
    return true
end
assert(is_anagram("anagram", "nagaram") == true)
assert(is_anagram("rat", "car") == false)
print("PASS")
''',
"c": '''#include <stdio.h>
#include <string.h>
static int is_anagram(const char *s, const char *t) {
    size_t ls = strlen(s), lt = strlen(t);
    if (ls != lt) return 0;
    int cnt[256] = {0};
    for (size_t i = 0; i < ls; i++) cnt[(unsigned char)s[i]]++;
    for (size_t i = 0; i < lt; i++) cnt[(unsigned char)t[i]]--;
    for (int i = 0; i < 256; i++) if (cnt[i] != 0) return 0;
    return 1;
}
int main(void) {
    if (!is_anagram("anagram", "nagaram")) { printf("FAIL 1\\n"); return 1; }
    if (is_anagram("rat", "car")) { printf("FAIL 2\\n"); return 1; }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''#include <algorithm>
#include <cassert>
#include <iostream>
#include <string>
static bool isAnagram(std::string s, std::string t) {
    if (s.size() != t.size()) return false;
    std::sort(s.begin(), s.end());
    std::sort(t.begin(), t.end());
    return s == t;
}
int main() {
    assert(isAnagram("anagram", "nagaram"));
    assert(!isAnagram("rat", "car"));
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''is_anagram <- function(s, t) {
  if (nchar(s) != nchar(t)) return(FALSE)
  identical(sort(strsplit(s, "")[[1]]), sort(strsplit(t, "")[[1]]))
}
stopifnot(is_anagram("anagram", "nagaram"))
stopifnot(!is_anagram("rat", "car"))
cat("PASS\\n")
''',
"zig": '''const std = @import("std");
fn isAnagram(s: []const u8, t: []const u8) bool {
    if (s.len != t.len) return false;
    var cnt = [_]i32{0} ** 256;
    for (s) |c| cnt[c] += 1;
    for (t) |c| cnt[c] -= 1;
    for (cnt) |v| if (v != 0) return false;
    return true;
}
pub fn main() !void {
    if (!isAnagram("anagram", "nagaram")) return error.TestFailed;
    if (isAnagram("rat", "car")) return error.TestFailed;
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''bool isAnagram(String s, String t) {
  if (s.length != t.length) return false;
  final a = s.split('')..sort();
  final b = t.split('')..sort();
  for (var i = 0; i < a.length; i++) {
    if (a[i] != b[i]) return false;
  }
  return true;
}
void main() {
  if (!isAnagram('anagram', 'nagaram')) throw StateError('c1');
  if (isAnagram('rat', 'car')) throw StateError('c2');
  print('PASS');
}
''',
}

A292 = {
"rust": '''fn can_win_nim(n: i64) -> bool { n % 4 != 0 }
fn main() {
    assert!(!can_win_nim(4));
    assert!(can_win_nim(1));
    assert!(can_win_nim(2));
    assert!(!can_win_nim(8));
    println!("PASS");
}
''',
"lua": '''local function can_win_nim(n) return n % 4 ~= 0 end
assert(can_win_nim(4) == false)
assert(can_win_nim(1) == true)
assert(can_win_nim(2) == true)
assert(can_win_nim(8) == false)
print("PASS")
''',
"c": '''#include <stdio.h>
static int can_win_nim(long n) { return n % 4 != 0; }
int main(void) {
    if (can_win_nim(4)) { printf("FAIL 1\\n"); return 1; }
    if (!can_win_nim(1) || !can_win_nim(2)) { printf("FAIL 2\\n"); return 1; }
    if (can_win_nim(8)) { printf("FAIL 3\\n"); return 1; }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''#include <cassert>
#include <iostream>
static bool canWinNim(long long n) { return n % 4 != 0; }
int main() {
    assert(!canWinNim(4));
    assert(canWinNim(1));
    assert(canWinNim(2));
    assert(!canWinNim(8));
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''can_win_nim <- function(n) n %% 4 != 0
stopifnot(!can_win_nim(4), can_win_nim(1), can_win_nim(2), !can_win_nim(8))
cat("PASS\\n")
''',
"zig": '''const std = @import("std");
fn canWinNim(n: i64) bool { return @mod(n, 4) != 0; }
pub fn main() !void {
    if (canWinNim(4)) return error.TestFailed;
    if (!canWinNim(1) or !canWinNim(2)) return error.TestFailed;
    if (canWinNim(8)) return error.TestFailed;
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''bool canWinNim(int n) => n % 4 != 0;
void main() {
  if (canWinNim(4)) throw StateError('c1');
  if (!canWinNim(1) || !canWinNim(2)) throw StateError('c2');
  if (canWinNim(8)) throw StateError('c3');
  print('PASS');
}
''',
}

A326 = {
"rust": '''fn is_power_of_three(mut n: i64) -> bool {
    while n != 0 && n % 3 == 0 { n /= 3; }
    n == 1
}
fn main() {
    assert!(is_power_of_three(27));
    assert!(!is_power_of_three(0));
    assert!(is_power_of_three(9));
    assert!(!is_power_of_three(-1));
    assert!(is_power_of_three(1));
    println!("PASS");
}
''',
"lua": '''local function is_power_of_three(n)
    while n ~= 0 and n % 3 == 0 do n = math.floor(n / 3) end
    return n == 1
end
assert(is_power_of_three(27) == true)
assert(is_power_of_three(0) == false)
assert(is_power_of_three(9) == true)
assert(is_power_of_three(-1) == false)
assert(is_power_of_three(1) == true)
print("PASS")
''',
"c": '''#include <stdio.h>
static int is_power_of_three(long n) {
    while (n != 0 && n % 3 == 0) n /= 3;
    return n == 1;
}
int main(void) {
    if (!is_power_of_three(27)) { printf("FAIL 1\\n"); return 1; }
    if (is_power_of_three(0)) { printf("FAIL 2\\n"); return 1; }
    if (!is_power_of_three(9)) { printf("FAIL 3\\n"); return 1; }
    if (is_power_of_three(-1)) { printf("FAIL 4\\n"); return 1; }
    if (!is_power_of_three(1)) { printf("FAIL 5\\n"); return 1; }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''#include <cassert>
#include <iostream>
static bool isPowerOfThree(long long n) {
    while (n != 0 && n % 3 == 0) n /= 3;
    return n == 1;
}
int main() {
    assert(isPowerOfThree(27));
    assert(!isPowerOfThree(0));
    assert(isPowerOfThree(9));
    assert(!isPowerOfThree(-1));
    assert(isPowerOfThree(1));
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''is_power_of_three <- function(n) {
  while (n != 0 && n %% 3 == 0) n <- n %/% 3
  n == 1
}
stopifnot(is_power_of_three(27), !is_power_of_three(0), is_power_of_three(9), !is_power_of_three(-1), is_power_of_three(1))
cat("PASS\\n")
''',
"zig": '''const std = @import("std");
fn isPowerOfThree(n0: i64) bool {
    var n = n0;
    while (n != 0 and @mod(n, 3) == 0) n = @divTrunc(n, 3);
    return n == 1;
}
pub fn main() !void {
    if (!isPowerOfThree(27)) return error.TestFailed;
    if (isPowerOfThree(0)) return error.TestFailed;
    if (!isPowerOfThree(9)) return error.TestFailed;
    if (isPowerOfThree(-1)) return error.TestFailed;
    if (!isPowerOfThree(1)) return error.TestFailed;
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''bool isPowerOfThree(int n) {
  while (n != 0 && n % 3 == 0) {
    n = n ~/ 3;
  }
  return n == 1;
}
void main() {
  if (!isPowerOfThree(27)) throw StateError('c1');
  if (isPowerOfThree(0)) throw StateError('c2');
  if (!isPowerOfThree(9)) throw StateError('c3');
  if (isPowerOfThree(-1)) throw StateError('c4');
  if (!isPowerOfThree(1)) throw StateError('c5');
  print('PASS');
}
''',
}

A1797 = {
"rust": '''use std::collections::HashMap;
struct AuthenticationManager { ttl: i64, expires_at: HashMap<String, i64> }
impl AuthenticationManager {
    fn new(time_to_live: i64) -> Self { AuthenticationManager { ttl: time_to_live, expires_at: HashMap::new() } }
    fn generate(&mut self, token_id: &str, current_time: i64) { self.expires_at.insert(token_id.to_string(), current_time + self.ttl); }
    fn renew(&mut self, token_id: &str, current_time: i64) -> usize {
        if let Some(&exp) = self.expires_at.get(token_id) {
            if exp > current_time {
                self.expires_at.insert(token_id.to_string(), current_time + self.ttl);
            }
        }
        self.count_valid_tokens(current_time)
    }
    fn count_valid_tokens(&self, current_time: i64) -> usize {
        self.expires_at.values().filter(|&&e| e > current_time).count()
    }
}
fn main() {
    let mut auth = AuthenticationManager::new(5);
    auth.generate("aaa", 1);
    assert_eq!(auth.count_valid_tokens(3), 1);
    assert_eq!(auth.renew("aaa", 4), 1);
    assert_eq!(auth.count_valid_tokens(6), 1);
    println!("PASS");
}
''',
"lua": '''local AuthenticationManager = {}
AuthenticationManager.__index = AuthenticationManager
function AuthenticationManager.new(ttl)
    return setmetatable({ttl = ttl, expires_at = {}}, AuthenticationManager)
end
function AuthenticationManager:generate(token_id, current_time)
    self.expires_at[token_id] = current_time + self.ttl
end
function AuthenticationManager:renew(token_id, current_time)
    local exp = self.expires_at[token_id]
    if exp and exp > current_time then
        self.expires_at[token_id] = current_time + self.ttl
    end
    return self:count_valid_tokens(current_time)
end
function AuthenticationManager:count_valid_tokens(current_time)
    local cnt = 0
    for _, e in pairs(self.expires_at) do
        if e > current_time then cnt = cnt + 1 end
    end
    return cnt
end
local auth = AuthenticationManager.new(5)
auth:generate("aaa", 1)
assert(auth:count_valid_tokens(3) == 1)
assert(auth:renew("aaa", 4) == 1)
assert(auth:count_valid_tokens(6) == 1)
print("PASS")
''',
"c": '''#include <stdio.h>
#include <string.h>
typedef struct { long ttl; char ids[64][32]; long exps[64]; int n; } AuthManager;
static void am_init(AuthManager *m, long ttl) { m->ttl = ttl; m->n = 0; }
static int am_find(AuthManager *m, const char *id) {
    for (int i = 0; i < m->n; i++) if (strcmp(m->ids[i], id) == 0) return i;
    return -1;
}
static void am_generate(AuthManager *m, const char *id, long t) {
    int i = am_find(m, id);
    if (i < 0) { i = m->n++; strcpy(m->ids[i], id); }
    m->exps[i] = t + m->ttl;
}
static int am_count(AuthManager *m, long t) {
    int cnt = 0;
    for (int i = 0; i < m->n; i++) if (m->exps[i] > t) cnt++;
    return cnt;
}
static int am_renew(AuthManager *m, const char *id, long t) {
    int i = am_find(m, id);
    if (i >= 0 && m->exps[i] > t) m->exps[i] = t + m->ttl;
    return am_count(m, t);
}
int main(void) {
    AuthManager m;
    am_init(&m, 5);
    am_generate(&m, "aaa", 1);
    if (am_count(&m, 3) != 1) { printf("FAIL c1\\n"); return 1; }
    if (am_renew(&m, "aaa", 4) != 1) { printf("FAIL r\\n"); return 1; }
    if (am_count(&m, 6) != 1) { printf("FAIL c2\\n"); return 1; }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''#include <cassert>
#include <iostream>
#include <string>
#include <unordered_map>
struct AuthenticationManager {
    long long ttl;
    std::unordered_map<std::string, long long> expiresAt;
    explicit AuthenticationManager(long long timeToLive) : ttl(timeToLive) {}
    void generate(const std::string &tokenId, long long currentTime) { expiresAt[tokenId] = currentTime + ttl; }
    int renew(const std::string &tokenId, long long currentTime) {
        auto it = expiresAt.find(tokenId);
        if (it != expiresAt.end() && it->second > currentTime) it->second = currentTime + ttl;
        return countValidTokens(currentTime);
    }
    int countValidTokens(long long currentTime) const {
        int cnt = 0;
        for (auto &[_, e] : expiresAt) if (e > currentTime) ++cnt;
        return cnt;
    }
};
int main() {
    AuthenticationManager auth(5);
    auth.generate("aaa", 1);
    assert(auth.countValidTokens(3) == 1);
    assert(auth.renew("aaa", 4) == 1);
    assert(auth.countValidTokens(6) == 1);
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''AuthenticationManager <- function(ttl) {
  e <- new.env(parent = emptyenv())
  e$ttl <- ttl
  e$expires_at <- new.env(parent = emptyenv())
  e$generate <- function(token_id, current_time) {
    e$expires_at[[token_id]] <<- current_time + e$ttl
  }
  e$renew <- function(token_id, current_time) {
    exp <- e$expires_at[[token_id]]
    if (!is.null(exp) && exp > current_time) {
      e$expires_at[[token_id]] <<- current_time + e$ttl
    }
    e$count_valid_tokens(current_time)
  }
  e$count_valid_tokens <- function(current_time) {
    cnt <- 0L
    for (k in ls(e$expires_at)) {
      if (e$expires_at[[k]] > current_time) cnt <- cnt + 1L
    }
    cnt
  }
  e
}
auth <- AuthenticationManager(5)
auth$generate("aaa", 1)
stopifnot(auth$count_valid_tokens(3) == 1)
stopifnot(auth$renew("aaa", 4) == 1)
stopifnot(auth$count_valid_tokens(6) == 1)
cat("PASS\\n")
''',
"zig": '''const std = @import("std");
const AuthManager = struct {
    ttl: i64,
    ids: [64][32]u8,
    id_lens: [64]usize,
    exps: [64]i64,
    n: usize,
    fn init(ttl: i64) AuthManager {
        return .{ .ttl = ttl, .ids = undefined, .id_lens = undefined, .exps = undefined, .n = 0 };
    }
    fn find(self: *AuthManager, id: []const u8) ?usize {
        for (0..self.n) |i| {
            if (std.mem.eql(u8, self.ids[i][0..self.id_lens[i]], id)) return i;
        }
        return null;
    }
    fn generate(self: *AuthManager, id: []const u8, t: i64) void {
        const i = self.find(id) orelse blk: {
            const idx = self.n;
            self.n += 1;
            @memcpy(self.ids[idx][0..id.len], id);
            self.id_lens[idx] = id.len;
            break :blk idx;
        };
        self.exps[i] = t + self.ttl;
    }
    fn countValidTokens(self: *AuthManager, t: i64) usize {
        var cnt: usize = 0;
        for (0..self.n) |i| {
            if (self.exps[i] > t) cnt += 1;
        }
        return cnt;
    }
    fn renew(self: *AuthManager, id: []const u8, t: i64) usize {
        if (self.find(id)) |i| {
            if (self.exps[i] > t) self.exps[i] = t + self.ttl;
        }
        return self.countValidTokens(t);
    }
};
pub fn main() !void {
    var auth = AuthManager.init(5);
    auth.generate("aaa", 1);
    if (auth.countValidTokens(3) != 1) return error.TestFailed;
    if (auth.renew("aaa", 4) != 1) return error.TestFailed;
    if (auth.countValidTokens(6) != 1) return error.TestFailed;
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''class AuthenticationManager {
  final int ttl;
  final Map<String, int> expiresAt = {};
  AuthenticationManager(this.ttl);
  void generate(String tokenId, int currentTime) {
    expiresAt[tokenId] = currentTime + ttl;
  }
  int renew(String tokenId, int currentTime) {
    final exp = expiresAt[tokenId];
    if (exp != null && exp > currentTime) {
      expiresAt[tokenId] = currentTime + ttl;
    }
    return countValidTokens(currentTime);
  }
  int countValidTokens(int currentTime) {
    var cnt = 0;
    for (final e in expiresAt.values) {
      if (e > currentTime) cnt++;
    }
    return cnt;
  }
}
void main() {
  final auth = AuthenticationManager(5);
  auth.generate('aaa', 1);
  if (auth.countValidTokens(3) != 1) throw StateError('c1');
  if (auth.renew('aaa', 4) != 1) throw StateError('r');
  if (auth.countValidTokens(6) != 1) throw StateError('c2');
  print('PASS');
}
''',
}

# R 的 2166 位运算方案（R 5.1+ 有 bitwXor/bitwAnd/bitwShiftL）
A2166["r"] = '''Bitset <- function(size) {
  e <- new.env(parent = emptyenv())
  e$n <- size
  e$words <- rep(0, (size + 31) %/% 32)
  e$ones <- 0L
  e$reverse <- 0L
  e$get <- function(idx) {
    w <- e$words[(idx %/% 32) + 1]
    bitwXor(bitwAnd(bitwShiftR(w, idx %% 32), 1L), e$reverse)
  }
  e$fix <- function(idx) {
    if (e$get(idx) == 0) {
      wi <- (idx %/% 32) + 1
      e$words[wi] <- bitwOr(e$words[wi], bitwShiftL(1, idx %% 32))
      e$ones <- e$ones + 1L
    }
  }
  e$unfix <- function(idx) {
    if (e$get(idx) == 1) {
      wi <- (idx %/% 32) + 1
      e$words[wi] <- bitwAnd(e$words[wi], bitwNot(bitwShiftL(1, idx %% 32)))
      e$ones <- e$ones - 1L
    }
  }
  e$flip <- function() {
    e$reverse <- bitwXor(e$reverse, 1L)
    e$ones <- e$n - e$ones
  }
  e$all <- function() e$ones == e$n
  e$one <- function() e$ones > 0
  e$count <- function() e$ones
  e$tostring <- function() {
    paste(vapply(seq_len(e$n) - 1L, function(i) as.character(e$get(i)), ""), collapse = "")
  }
  e
}
bs <- Bitset(5)
bs$fix(0); bs$fix(3)
stopifnot(bs$tostring() == "10010", bs$count() == 2)
bs$flip()
stopifnot(bs$tostring() == "01101", bs$count() == 3)
bs$unfix(0)
stopifnot(bs$tostring() == "01101")
stopifnot(bs$all() == FALSE, bs$one() == TRUE)
cat("PASS\\n")
'''

PROBS = [
    ("lc_202_快乐数", A202, "LeetCode 202. 快乐数"),
    ("lc_2166_设计位集", A2166, "LeetCode 2166. 设计位集"),
    ("lc_217_存在重复元素", A217, "LeetCode 217. 存在重复元素"),
    ("lc_242_有效的字母异位词", A242, "LeetCode 242. 有效的字母异位词"),
    ("lc_292_nim_游戏", A292, "LeetCode 292. Nim游戏"),
    ("lc_326_3_的幂", A326, "LeetCode 326. 3的幂"),
    ("lc_1797_设计一个验证系统", A1797, "LeetCode 1797. 设计一个验证系统"),
]
count = 0
for prob, algo, title in PROBS:
    bid = B[prob.split("_")[1]]
    ts_dir = f"/Users/Wang/Code/webfault-ai/dsa/ts/other/{prob}"
    sols = sorted(f[:-3] for f in os.listdir(ts_dir) if f.startswith("solution_") and f.endswith(".ts"))
    for lang in EXT:
        ext = EXT[lang]
        for sol in sols:
            n = sol.replace("solution_", "").split("_")[0]
            head = head_comment(lang, bid, f"{title} — {LANGNAME[lang]} 版（方案{n}）")
            emit(lang, f"other/{prob}/{sol}.{ext}", head + "\n" + algo[lang])
            count += 1
print(f"emitted {count} files")
