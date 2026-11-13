#!/usr/bin/env python3
# gen_stack1.py — stack 第一批：1047/150/151/496/503/739/71/682 × 7语言
# 纯单括号模板（无反转义）
import sys, os; sys.path.insert(0, "/Users/Wang/Code/github/web-x-blog/work/blog/courses/21.dsa/_tools")
from langlib import emit, head_comment, EXT

B = {"1047":"145295630","150":"130726302","151":"130846022","496":"145012016","503":"145045460","739":"145233913","71":"134368624","682":"130734875"}
LANGNAME = {"rust": "Rust", "lua": "Lua", "c": "C", "cpp": "C++", "r": "R", "zig": "Zig", "dart": "Dart"}

T = {}
T["1047"] = {
"rust":'''fn remove_duplicates(s: String) -> String {
    let mut st: Vec<char> = Vec::new();
    for c in s.chars() {
        if st.last() == Some(&c) { st.pop(); } else { st.push(c); }
    }
    st.into_iter().collect()
}
fn main() {
    assert_eq!(remove_duplicates("abbaca".into()), "ca");
    assert_eq!(remove_duplicates("azxxzy".into()), "ay");
    assert_eq!(remove_duplicates("".into()), "");
    println!("PASS"); }''',
"lua":'''local function remove_duplicates(s)
    local st = {}
    for i = 1, #s do
        local c = s:sub(i, i)
        if #st > 0 and st[#st] == c then
            st[#st] = nil
        else
            st[#st + 1] = c
        end
    end
    return table.concat(st)
end
assert(remove_duplicates("abbaca") == "ca")
assert(remove_duplicates("azxxzy") == "ay")
assert(remove_duplicates("") == "")
print("PASS")''',
"c":'''#include <stdio.h>
#include <string.h>
static void remove_duplicates(const char *s, char out[]) {
    int top = 0;
    for (const char *p = s; *p; p++) {
        if (top > 0 && out[top - 1] == *p) top--;
        else out[top++] = *p;
    }
    out[top] = '\\0';
}
int main(void) {
    char out[8192];
    remove_duplicates("abbaca", out);
    if (strcmp(out, "ca") != 0) { printf("FAIL 1\\n"); return 1; }
    remove_duplicates("azxxzy", out);
    if (strcmp(out, "ay") != 0) { printf("FAIL 2\\n"); return 1; }
    remove_duplicates("", out);
    if (strcmp(out, "") != 0) { printf("FAIL 3\\n"); return 1; }
    printf("PASS\\n"); return 0; }''',
"cpp":'''#include <cassert>
#include <iostream>
#include <string>
static std::string removeDuplicates(const std::string &s) {
    std::string st;
    for (char c : s) {
        if (!st.empty() && st.back() == c) st.pop_back();
        else st.push_back(c);
    }
    return st;
}
int main() { assert(removeDuplicates("abbaca") == "ca"); assert(removeDuplicates("azxxzy") == "ay"); assert(removeDuplicates("") == ""); std::cout << "PASS" << std::endl; }''',
"r":'''remove_duplicates_str <- function(s) {
  chars <- strsplit(s, "")[[1]]
  st <- character(0)
  for (c in chars) {
    if (length(st) > 0 && st[length(st)] == c) st <- st[-length(st)]
    else st <- c(st, c)
  }
  paste(st, collapse = "")
}
stopifnot(remove_duplicates_str("abbaca") == "ca")
stopifnot(remove_duplicates_str("azxxzy") == "ay")
stopifnot(remove_duplicates_str("") == "")
cat("PASS\\n")''',
"zig":'''const std = @import("std");
fn removeDuplicates(s: []const u8, out: *std.ArrayList(u8)) void {
    var st: [8192]u8 = undefined;
    var top: usize = 0;
    for (s) |c| {
        if (top > 0 and st[top - 1] == c) top -= 1 else {
            st[top] = c;
            top += 1;
        }
    }
    out.appendSlice(st[0..top]) catch unreachable;
}
pub fn main() !void {
    var out = std.ArrayList(u8).init(std.heap.page_allocator);
    defer out.deinit();
    removeDuplicates("abbaca", &out);
    if (!std.mem.eql(u8, out.items, "ca")) return error.TestFailed;
    out.clearRetainingCapacity();
    removeDuplicates("azxxzy", &out);
    if (!std.mem.eql(u8, out.items, "ay")) return error.TestFailed;
    out.clearRetainingCapacity();
    removeDuplicates("", &out);
    if (out.items.len != 0) return error.TestFailed;
    std.debug.print("PASS\\n", .{}); }''',
"dart":'''String removeDuplicates(String s) {
  final st = <String>[];
  for (final c in s.split('')) {
    if (st.isNotEmpty && st.last == c) { st.removeLast(); } else { st.add(c); }
  }
  return st.join();
}
void main() { if (removeDuplicates('abbaca') != 'ca') throw StateError('c1'); if (removeDuplicates('azxxzy') != 'ay') throw StateError('c2'); if (removeDuplicates('') != '') throw StateError('c3'); print('PASS'); }''',
}

T["150"] = {
"rust":'''fn eval_rpn(tokens: Vec<&str>) -> i32 {
    let mut st: Vec<i64> = Vec::new();
    for t in tokens {
        match t {
            "+" => { let b = st.pop().unwrap(); let a = st.pop().unwrap(); st.push(a + b); }
            "-" => { let b = st.pop().unwrap(); let a = st.pop().unwrap(); st.push(a - b); }
            "*" => { let b = st.pop().unwrap(); let a = st.pop().unwrap(); st.push(a * b); }
            "/" => { let b = st.pop().unwrap(); let a = st.pop().unwrap(); st.push(a / b); }
            _ => st.push(t.parse::<i64>().unwrap()),
        }
    }
    st[0] as i32
}
fn main() {
    assert_eq!(eval_rpn(vec!["2","1","+","3","*"]), 9);
    assert_eq!(eval_rpn(vec!["4","13","5","/","+"]), 6);
    assert_eq!(eval_rpn(vec!["10","6","9","3","+","-11","*","/","*","17","+","5","+"]), 22);
    println!("PASS"); }''',
"lua":'''local function eval_rpn(tokens)
    local st = {}
    for _, t in ipairs(tokens) do
        if t == "+" then
            local b = table.remove(st); local a = table.remove(st)
            st[#st + 1] = a + b
        elseif t == "-" then
            local b = table.remove(st); local a = table.remove(st)
            st[#st + 1] = a - b
        elseif t == "*" then
            local b = table.remove(st); local a = table.remove(st)
            st[#st + 1] = a * b
        elseif t == "/" then
            local b = table.remove(st); local a = table.remove(st)
            st[#st + 1] = math.floor(a / b + 0.5) * ((a * b < 0) and -1 or 1) * -1  -- 截断除法
            -- 简化：C 风格截断
            local q = a / b
            st[#st] = (q >= 0) and math.floor(q) or math.ceil(q)
        else
            st[#st + 1] = tonumber(t)
        end
    end
    return st[1]
end
assert(eval_rpn({"2","1","+","3","*"}) == 9)
assert(eval_rpn({"4","13","5","/","+"}) == 6)
assert(eval_rpn({"10","6","9","3","+","-11","*","/","*","17","+","5","+"}) == 22)
print("PASS")''',
"c":'''#include <stdio.h>
#include <stdlib.h>
#include <string.h>
static long eval_rpn(const char **tokens, int n) {
    long st[4096];
    int top = 0;
    for (int i = 0; i < n; i++) {
        const char *t = tokens[i];
        if (strcmp(t, "+") == 0 || strcmp(t, "-") == 0 || strcmp(t, "*") == 0 || strcmp(t, "/") == 0) {
            long b = st[--top];
            long a = st[--top];
            long r = 0;
            if (t[0] == '+') r = a + b;
            else if (t[0] == '-') r = a - b;
            else if (t[0] == '*') r = a * b;
            else r = a / b;
            st[top++] = r;
        } else {
            st[top++] = atol(t);
        }
    }
    return st[0];
}
int main(void) {
    const char *t1[] = {"2","1","+","3","*"};
    const char *t2[] = {"4","13","5","/","+"};
    const char *t3[] = {"10","6","9","3","+","-11","*","/","*","17","+","5","+"};
    if (eval_rpn(t1, 5) != 9) { printf("FAIL 1\\n"); return 1; }
    if (eval_rpn(t2, 5) != 6) { printf("FAIL 2\\n"); return 1; }
    if (eval_rpn(t3, 13) != 22) { printf("FAIL 3\\n"); return 1; }
    printf("PASS\\n"); return 0; }''',
"cpp":'''#include <cassert>
#include <cstdlib>
#include <iostream>
#include <string>
#include <vector>
static int evalRPN(const std::vector<std::string> &tokens) {
    std::vector<long long> st;
    for (const auto &t : tokens) {
        if (t == "+" || t == "-" || t == "*" || t == "/") {
            long long b = st.back(); st.pop_back();
            long long a = st.back(); st.pop_back();
            if (t == "+") st.push_back(a + b);
            else if (t == "-") st.push_back(a - b);
            else if (t == "*") st.push_back(a * b);
            else st.push_back(a / b);
        } else {
            st.push_back(std::stoll(t));
        }
    }
    return static_cast<int>(st[0]);
}
int main() {
    assert(evalRPN({"2","1","+","3","*"}) == 9);
    assert(evalRPN({"4","13","5","/","+"}) == 6);
    assert(evalRPN({"10","6","9","3","+","-11","*","/","*","17","+","5","+"}) == 22);
    std::cout << "PASS" << std::endl; }''',
"r":'''eval_rpn <- function(tokens) {
  st <- numeric(0)
  for (t in tokens) {
    if (t %in% c("+", "-", "*", "/")) {
      b <- st[length(st)]; st <- st[-length(st)]
      a <- st[length(st)]; st <- st[-length(st)]
      if (t == "+") r <- a + b
      else if (t == "-") r <- a - b
      else if (t == "*") r <- a * b
      else {
        q <- a / b
        r <- if (q >= 0) floor(q) else ceiling(q)
      }
      st <- c(st, r)
    } else {
      st <- c(st, as.numeric(t))
    }
  }
  st[1]
}
stopifnot(eval_rpn(c("2","1","+","3","*")) == 9)
stopifnot(eval_rpn(c("4","13","5","/","+")) == 6)
stopifnot(eval_rpn(c("10","6","9","3","+","-11","*","/","*","17","+","5","+")) == 22)
cat("PASS\\n")''',
"zig":'''const std = @import("std");
fn evalRPN(tokens: []const []const u8) i64 {
    var st: [4096]i64 = undefined;
    var top: usize = 0;
    for (tokens) |t| {
        if (t.len == 1 and (t[0] == '+' or t[0] == '-' or t[0] == '*' or t[0] == '/') and t.len == 1) {
            if (std.mem.eql(u8, t, "+") or std.mem.eql(u8, t, "-") or std.mem.eql(u8, t, "*") or std.mem.eql(u8, t, "/")) {
                const b = st[top - 1];
                top -= 1;
                const a = st[top - 1];
                top -= 1;
                var r: i64 = 0;
                if (t[0] == '+') r = a + b
                else if (t[0] == '-') r = a - b
                else if (t[0] == '*') r = a * b
                else r = @divTrunc(a, b);
                st[top] = r;
                top += 1;
            }
        } else {
            st[top] = std.fmt.parseInt(i64, t, 10) catch unreachable;
            top += 1;
        }
    }
    return st[0];
}
pub fn main() !void {
    if (evalRPN(&[_][]const u8{ "2", "1", "+", "3", "*" }) != 9) return error.TestFailed;
    if (evalRPN(&[_][]const u8{ "4", "13", "5", "/", "+" }) != 6) return error.TestFailed;
    if (evalRPN(&[_][]const u8{ "10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+" }) != 22) return error.TestFailed;
    std.debug.print("PASS\\n", .{}); }''',
"dart":'''int evalRPN(List<String> tokens) {
  final st = <int>[];
  for (final t in tokens) {
    if (t == '+' || t == '-' || t == '*' || t == '/') {
      final b = st.removeLast();
      final a = st.removeLast();
      if (t == '+') { st.add(a + b); }
      else if (t == '-') { st.add(a - b); }
      else if (t == '*') { st.add(a * b); }
      else {
        final q = a / b;
        st.add(q >= 0 ? q.floor() : q.ceil());
      }
    } else {
      st.add(int.parse(t));
    }
  }
  return st[0];
}
void main() {
  if (evalRPN(['2','1','+','3','*']) != 9) throw StateError('c1');
  if (evalRPN(['4','13','5','/','+']) != 6) throw StateError('c2');
  if (evalRPN(['10','6','9','3','+','-11','*','/','*','17','+','5','+']) != 22) throw StateError('c3');
  print('PASS'); }''',
}

T["151"] = {
"rust":'''fn reverse_words(s: String) -> String {
    s.split_whitespace().rev().collect::<Vec<_>>().join(" ")
}
fn main() {
    assert_eq!(reverse_words("the sky is blue".into()), "blue is sky the");
    assert_eq!(reverse_words("  hello world  ".into()), "world hello");
    assert_eq!(reverse_words("a good   example".into()), "example good a");
    println!("PASS"); }''',
"lua":'''local function reverse_words(s)
    local words = {}
    for w in s:gmatch("%S+") do words[#words + 1] = w end
    local out = {}
    for i = #words, 1, -1 do out[#out + 1] = words[i] end
    return table.concat(out, " ")
end
assert(reverse_words("the sky is blue") == "blue is sky the")
assert(reverse_words("  hello world  ") == "world hello")
assert(reverse_words("a good   example") == "example good a")
print("PASS")''',
"c":'''#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
static void reverse_words(const char *s, char out[]) {
    char *words[8192];
    int wn = 0;
    const char *p = s;
    while (*p) {
        while (*p && isspace((unsigned char)*p)) p++;
        if (!*p) break;
        const char *start = p;
        while (*p && !isspace((unsigned char)*p)) p++;
        size_t len = p - start;
        words[wn] = malloc(len + 1);
        strncpy(words[wn], start, len);
        words[wn][len] = '\\0';
        wn++;
    }
    int pos = 0;
    for (int i = wn - 1; i >= 0; i--) {
        if (pos > 0) out[pos++] = ' ';
        strcpy(out + pos, words[i]);
        pos += strlen(words[i]);
        free(words[i]);
    }
    out[pos] = '\\0';
}
int main(void) {
    char out[8192];
    reverse_words("the sky is blue", out);
    if (strcmp(out, "blue is sky the") != 0) { printf("FAIL 1\\n"); return 1; }
    reverse_words("  hello world  ", out);
    if (strcmp(out, "world hello") != 0) { printf("FAIL 2\\n"); return 1; }
    reverse_words("a good   example", out);
    if (strcmp(out, "example good a") != 0) { printf("FAIL 3\\n"); return 1; }
    printf("PASS\\n"); return 0; }''',
"cpp":'''#include <algorithm>
#include <cassert>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
static std::string reverseWords(const std::string &s) {
    std::istringstream iss(s);
    std::vector<std::string> words;
    std::string w;
    while (iss >> w) words.push_back(w);
    std::reverse(words.begin(), words.end());
    std::string out;
    for (size_t i = 0; i < words.size(); ++i) {
        if (i) out += " ";
        out += words[i];
    }
    return out;
}
int main() { assert(reverseWords("the sky is blue") == "blue is sky the"); assert(reverseWords("  hello world  ") == "world hello"); assert(reverseWords("a good   example") == "example good a"); std::cout << "PASS" << std::endl; }''',
"r":'''reverse_words <- function(s) {
  words <- strsplit(trimws(s), "\\\\s+")[[1]]
  paste(rev(words), collapse = " ")
}
stopifnot(reverse_words("the sky is blue") == "blue is sky the")
stopifnot(reverse_words("  hello world  ") == "world hello")
stopifnot(reverse_words("a good   example") == "example good a")
cat("PASS\\n")''',
"zig":'''const std = @import("std");
fn reverseWords(s: []const u8, out: *std.ArrayList(u8)) void {
    var words: [8192][]const u8 = undefined;
    var wn: usize = 0;
    var it = std.mem.tokenizeAny(u8, s, " \\t");
    while (it.next()) |w| {
        words[wn] = w;
        wn += 1;
    }
    var first = true;
    var i: usize = wn;
    while (i > 0) {
        i -= 1;
        if (!first) out.append(' ') catch unreachable;
        first = false;
        out.appendSlice(words[i]) catch unreachable;
    }
}
pub fn main() !void {
    var out = std.ArrayList(u8).init(std.heap.page_allocator);
    defer out.deinit();
    reverseWords("the sky is blue", &out);
    if (!std.mem.eql(u8, out.items, "blue is sky the")) return error.TestFailed;
    out.clearRetainingCapacity();
    reverseWords("  hello world  ", &out);
    if (!std.mem.eql(u8, out.items, "world hello")) return error.TestFailed;
    out.clearRetainingCapacity();
    reverseWords("a good   example", &out);
    if (!std.mem.eql(u8, out.items, "example good a")) return error.TestFailed;
    std.debug.print("PASS\\n", .{}); }''',
"dart":'''String reverseWords(String s) {
  final words = s.trim().split(RegExp(r'\\s+')).where((w) => w.isNotEmpty).toList();
  return words.reversed.join(' ');
}
void main() { if (reverseWords('the sky is blue') != 'blue is sky the') throw StateError('c1'); if (reverseWords('  hello world  ') != 'world hello') throw StateError('c2'); if (reverseWords('a good   example') != 'example good a') throw StateError('c3'); print('PASS'); }''',
}

T["496"] = {
"rust":'''use std::collections::HashMap;
fn next_greater_element(nums1: Vec<i32>, nums2: Vec<i32>) -> Vec<i32> {
    let mut next: HashMap<i32, i32> = HashMap::new();
    let mut st: Vec<i32> = Vec::new();
    for &v in &nums2 {
        while let Some(&top) = st.last() {
            if top < v { next.insert(top, v); st.pop(); } else { break; }
        }
        st.push(v);
    }
    nums1.iter().map(|&v| *next.get(&v).unwrap_or(&-1)).collect()
}
fn main() {
    assert_eq!(next_greater_element(vec![4,1,2], vec![1,3,4,2]), vec![-1,3,-1]);
    assert_eq!(next_greater_element(vec![2,4], vec![1,2,3,4]), vec![3,-1]);
    println!("PASS"); }''',
"lua":'''local function next_greater_element(nums1, nums2)
    local next_ = {}
    local st = {}
    for _, v in ipairs(nums2) do
        while #st > 0 and st[#st] < v do
            next_[st[#st]] = v
            st[#st] = nil
        end
        st[#st + 1] = v
    end
    local out = {}
    for i, v in ipairs(nums1) do
        out[i] = next_[v] or -1
    end
    return out
end
assert(table.concat(next_greater_element({4,1,2}, {1,3,4,2}), ",") == "-1,3,-1")
assert(table.concat(next_greater_element({2,4}, {1,2,3,4}), ",") == "3,-1")
print("PASS")''',
"c":'''#include <stdio.h>
static int next_greater_element(const int *n1, int l1, const int *n2, int l2, int out[]) {
    int next[65536];
    for (int i = 0; i < 65536; i++) next[i] = -1;
    int st[8192], top = 0;
    for (int i = 0; i < l2; i++) {
        while (top > 0 && st[top - 1] < n2[i]) {
            next[st[top - 1] + 32768] = n2[i];
            top--;
        }
        st[top++] = n2[i];
    }
    for (int i = 0; i < l1; i++) out[i] = next[n1[i] + 32768];
    return l1;
}
int main(void) {
    int out[64];
    next_greater_element((int[]){4,1,2}, 3, (int[]){1,3,4,2}, 4, out);
    if (!(out[0]==-1&&out[1]==3&&out[2]==-1)) { printf("FAIL 1\\n"); return 1; }
    next_greater_element((int[]){2,4}, 2, (int[]){1,2,3,4}, 4, out);
    if (!(out[0]==3&&out[1]==-1)) { printf("FAIL 2\\n"); return 1; }
    printf("PASS\\n"); return 0; }''',
"cpp":'''#include <cassert>
#include <iostream>
#include <stack>
#include <unordered_map>
#include <vector>
static std::vector<int> nextGreaterElement(const std::vector<int> &nums1, const std::vector<int> &nums2) {
    std::unordered_map<int, int> next;
    std::stack<int> st;
    for (int v : nums2) {
        while (!st.empty() && st.top() < v) {
            next[st.top()] = v;
            st.pop();
        }
        st.push(v);
    }
    std::vector<int> out;
    for (int v : nums1) {
        auto it = next.find(v);
        out.push_back(it != next.end() ? it->second : -1);
    }
    return out;
}
int main() { assert((nextGreaterElement({4,1,2}, {1,3,4,2}) == std::vector<int>{-1,3,-1})); assert((nextGreaterElement({2,4}, {1,2,3,4}) == std::vector<int>{3,-1})); std::cout << "PASS" << std::endl; }''',
"r":'''next_greater_element <- function(nums1, nums2) {
  nxt <- new.env(parent = emptyenv())
  st <- integer(0)
  for (v in nums2) {
    while (length(st) > 0 && st[length(st)] < v) {
      nxt[[as.character(st[length(st)])]] <- v
      st <- st[-length(st)]
    }
    st <- c(st, v)
  }
  sapply(nums1, function(v) {
    key <- as.character(v)
    if (!is.null(nxt[[key]])) nxt[[key]] else -1L
  })
}
stopifnot(identical(as.integer(next_greater_element(c(4, 1, 2), c(1, 3, 4, 2))), c(-1L, 3L, -1L)))
stopifnot(identical(as.integer(next_greater_element(c(2, 4), c(1, 2, 3, 4))), c(3L, -1L)))
cat("PASS\\n")''',
"zig":'''const std = @import("std");
fn nextGreaterElement(n1: []const i32, n2: []const i32, alloc: std.mem.Allocator, out: []i32) void {
    var next = std.AutoHashMap(i32, i32).init(alloc);
    var st: [8192]i32 = undefined;
    var top: usize = 0;
    for (n2) |v| {
        while (top > 0 and st[top - 1] < v) {
            next.put(st[top - 1], v) catch unreachable;
            top -= 1;
        }
        st[top] = v;
        top += 1;
    }
    for (n1, 0..) |v, i| {
        out[i] = next.get(v) orelse -1;
    }
}
pub fn main() !void {
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();
    const alloc = arena.allocator();
    var out: [8]i32 = undefined;
    nextGreaterElement(&[_]i32{ 4, 1, 2 }, &[_]i32{ 1, 3, 4, 2 }, alloc, &out);
    if (out[0] != -1 or out[1] != 3 or out[2] != -1) return error.TestFailed;
    nextGreaterElement(&[_]i32{ 2, 4 }, &[_]i32{ 1, 2, 3, 4 }, alloc, &out);
    if (out[0] != 3 or out[1] != -1) return error.TestFailed;
    std.debug.print("PASS\\n", .{}); }''',
"dart":'''List<int> nextGreaterElement(List<int> nums1, List<int> nums2) {
  final next = <int, int>{};
  final st = <int>[];
  for (final v in nums2) {
    while (st.isNotEmpty && st.last < v) {
      next[st.removeLast()] = v;
    }
    st.add(v);
  }
  return nums1.map((v) => next[v] ?? -1).toList();
}
void main() { if (nextGreaterElement([4,1,2], [1,3,4,2]).toString() != '[-1, 3, -1]') throw StateError('c1'); if (nextGreaterElement([2,4], [1,2,3,4]).toString() != '[3, -1]') throw StateError('c2'); print('PASS'); }''',
}

T["503"] = {
"rust":'''fn next_greater_elements(nums: Vec<i32>) -> Vec<i32> {
    let n = nums.len();
    let mut res = vec![-1; n];
    let mut st: Vec<usize> = Vec::new();
    for i in 0..n * 2 {
        let ii = i % n;
        while let Some(&top) = st.last() {
            if nums[top] < nums[ii] { res[top] = nums[ii]; st.pop(); } else { break; }
        }
        if i < n { st.push(ii); }
    }
    res
}
fn main() {
    assert_eq!(next_greater_elements(vec![1,2,1]), vec![2,-1,2]);
    assert_eq!(next_greater_elements(vec![3,2,1]), vec![-1,3,3]);
    println!("PASS"); }''',
"lua":'''local function next_greater_elements(nums)
    local n = #nums
    local res = {}
    for i = 1, n do res[i] = -1 end
    local st = {}
    for i = 1, 2 * n do
        local ii = (i - 1) % n + 1
        while #st > 0 and nums[st[#st]] < nums[ii] do
            res[st[#st]] = nums[ii]
            st[#st] = nil
        end
        if i <= n then st[#st + 1] = ii end
    end
    return res
end
assert(table.concat(next_greater_elements({1,2,1}), ",") == "2,-1,2")
assert(table.concat(next_greater_elements({3,2,1}), ",") == "-1,3,3")
print("PASS")''',
"c":'''#include <stdio.h>
static void next_greater_elements(const int *nums, int n, int out[]) {
    for (int i = 0; i < n; i++) out[i] = -1;
    int st[8192], top = 0;
    for (int i = 0; i < 2 * n; i++) {
        int ii = i % n;
        while (top > 0 && nums[st[top - 1]] < nums[ii]) {
            out[st[top - 1]] = nums[ii];
            top--;
        }
        if (i < n) st[top++] = ii;
    }
}
int main(void) {
    int out[8192];
    next_greater_elements((int[]){1,2,1}, 3, out);
    if (!(out[0]==2&&out[1]==-1&&out[2]==2)) { printf("FAIL 1\\n"); return 1; }
    next_greater_elements((int[]){3,2,1}, 3, out);
    if (!(out[0]==-1&&out[1]==3&&out[2]==3)) { printf("FAIL 2\\n"); return 1; }
    printf("PASS\\n"); return 0; }''',
"cpp":'''#include <cassert>
#include <iostream>
#include <vector>
static std::vector<int> nextGreaterElements(const std::vector<int> &nums) {
    size_t n = nums.size();
    std::vector<int> res(n, -1);
    std::vector<size_t> st;
    for (size_t i = 0; i < 2 * n; ++i) {
        size_t ii = i % n;
        while (!st.empty() && nums[st.back()] < nums[ii]) {
            res[st.back()] = nums[ii];
            st.pop_back();
        }
        if (i < n) st.push_back(ii);
    }
    return res;
}
int main() { assert((nextGreaterElements({1,2,1}) == std::vector<int>{2,-1,2})); assert((nextGreaterElements({3,2,1}) == std::vector<int>{-1,3,3})); std::cout << "PASS" << std::endl; }''',
"r":'''next_greater_elements <- function(nums) {
  n <- length(nums)
  res <- rep(-1L, n)
  st <- integer(0)
  for (i in 1:(2 * n)) {
    ii <- (i - 1) %% n + 1
    while (length(st) > 0 && nums[st[length(st)]] < nums[ii]) {
      res[st[length(st)]] <- nums[ii]
      st <- st[-length(st)]
    }
    if (i <= n) st <- c(st, ii)
  }
  res
}
stopifnot(identical(as.integer(next_greater_elements(c(1, 2, 1))), c(2L, -1L, 2L)))
stopifnot(identical(as.integer(next_greater_elements(c(3, 2, 1))), c(-1L, 3L, 3L)))
cat("PASS\\n")''',
"zig":'''const std = @import("std");
fn nextGreaterElements(nums: []const i32, out: []i32) void {
    const n = nums.len;
    for (0..n) |i| out[i] = -1;
    var st: [8192]usize = undefined;
    var top: usize = 0;
    for (0..2 * n) |i| {
        const ii = i % n;
        while (top > 0 and nums[st[top - 1]] < nums[ii]) {
            out[st[top - 1]] = nums[ii];
            top -= 1;
        }
        if (i < n) {
            st[top] = ii;
            top += 1;
        }
    }
}
pub fn main() !void {
    var out: [8]i32 = undefined;
    nextGreaterElements(&[_]i32{ 1, 2, 1 }, &out);
    if (out[0] != 2 or out[1] != -1 or out[2] != 2) return error.TestFailed;
    nextGreaterElements(&[_]i32{ 3, 2, 1 }, &out);
    if (out[0] != -1 or out[1] != 3 or out[2] != 3) return error.TestFailed;
    std.debug.print("PASS\\n", .{}); }''',
"dart":'''List<int> nextGreaterElements(List<int> nums) {
  final n = nums.length;
  final res = List<int>.filled(n, -1);
  final st = <int>[];
  for (var i = 0; i < 2 * n; i++) {
    final ii = i % n;
    while (st.isNotEmpty && nums[st.last] < nums[ii]) {
      res[st.removeLast()] = nums[ii];
    }
    if (i < n) st.add(ii);
  }
  return res;
}
void main() { if (nextGreaterElements([1,2,1]).toString() != '[2, -1, 2]') throw StateError('c1'); if (nextGreaterElements([3,2,1]).toString() != '[-1, 3, 3]') throw StateError('c2'); print('PASS'); }''',
}

T["739"] = {
"rust":'''fn daily_temperatures(temps: Vec<i32>) -> Vec<i32> {
    let n = temps.len();
    let mut res = vec![0i32; n];
    let mut st: Vec<usize> = Vec::new();
    for i in 0..n {
        while let Some(&top) = st.last() {
            if temps[top] < temps[i] { res[top] = (i - top) as i32; st.pop(); } else { break; }
        }
        st.push(i);
    }
    res
}
fn main() {
    assert_eq!(daily_temperatures(vec![73,74,75,71,69,72,76,73]), vec![1,1,4,2,1,1,0,0]);
    assert_eq!(daily_temperatures(vec![30,40,50,60]), vec![1,1,1,0]);
    assert_eq!(daily_temperatures(vec![30,60,90]), vec![1,1,0]);
    println!("PASS"); }''',
"lua":'''local function daily_temperatures(temps)
    local n = #temps
    local res = {}
    for i = 1, n do res[i] = 0 end
    local st = {}
    for i = 1, n do
        while #st > 0 and temps[st[#st]] < temps[i] do
            res[st[#st]] = i - st[#st]
            st[#st] = nil
        end
        st[#st + 1] = i
    end
    return res
end
assert(table.concat(daily_temperatures({73,74,75,71,69,72,76,73}), ",") == "1,1,4,2,1,1,0,0")
assert(table.concat(daily_temperatures({30,40,50,60}), ",") == "1,1,1,0")
assert(table.concat(daily_temperatures({30,60,90}), ",") == "1,1,0")
print("PASS")''',
"c":'''#include <stdio.h>
static void daily_temperatures(const int *t, int n, int out[]) {
    for (int i = 0; i < n; i++) out[i] = 0;
    int st[8192], top = 0;
    for (int i = 0; i < n; i++) {
        while (top > 0 && t[st[top - 1]] < t[i]) {
            out[st[top - 1]] = i - st[top - 1];
            top--;
        }
        st[top++] = i;
    }
}
int main(void) {
    int out[8192];
    daily_temperatures((int[]){73,74,75,71,69,72,76,73}, 8, out);
    if (!(out[0]==1&&out[2]==4&&out[7]==0)) { printf("FAIL 1\\n"); return 1; }
    daily_temperatures((int[]){30,40,50,60}, 4, out);
    if (!(out[0]==1&&out[3]==0)) { printf("FAIL 2\\n"); return 1; }
    daily_temperatures((int[]){30,60,90}, 3, out);
    if (!(out[0]==1&&out[2]==0)) { printf("FAIL 3\\n"); return 1; }
    printf("PASS\\n"); return 0; }''',
"cpp":'''#include <cassert>
#include <iostream>
#include <vector>
static std::vector<int> dailyTemperatures(const std::vector<int> &temps) {
    size_t n = temps.size();
    std::vector<int> res(n, 0);
    std::vector<size_t> st;
    for (size_t i = 0; i < n; ++i) {
        while (!st.empty() && temps[st.back()] < temps[i]) {
            res[st.back()] = static_cast<int>(i - st.back());
            st.pop_back();
        }
        st.push_back(i);
    }
    return res;
}
int main() { assert((dailyTemperatures({73,74,75,71,69,72,76,73}) == std::vector<int>{1,1,4,2,1,1,0,0})); assert((dailyTemperatures({30,40,50,60}) == std::vector<int>{1,1,1,0})); assert((dailyTemperatures({30,60,90}) == std::vector<int>{1,1,0})); std::cout << "PASS" << std::endl; }''',
"r":'''daily_temperatures <- function(temps) {
  n <- length(temps)
  res <- rep(0L, n)
  st <- integer(0)
  for (i in seq_len(n)) {
    while (length(st) > 0 && temps[st[length(st)]] < temps[i]) {
      res[st[length(st)]] <- i - st[length(st)]
      st <- st[-length(st)]
    }
    st <- c(st, i)
  }
  res
}
stopifnot(identical(daily_temperatures(c(73,74,75,71,69,72,76,73)), c(1L,1L,4L,2L,1L,1L,0L,0L)))
stopifnot(identical(daily_temperatures(c(30,40,50,60)), c(1L,1L,1L,0L)))
stopifnot(identical(daily_temperatures(c(30,60,90)), c(1L,1L,0L)))
cat("PASS\\n")''',
"zig":'''const std = @import("std");
fn dailyTemperatures(t: []const i32, out: []i32) void {
    const n = t.len;
    for (0..n) |i| out[i] = 0;
    var st: [8192]usize = undefined;
    var top: usize = 0;
    for (0..n) |i| {
        while (top > 0 and t[st[top - 1]] < t[i]) {
            out[st[top - 1]] = @intCast(i - st[top - 1]);
            top -= 1;
        }
        st[top] = i;
        top += 1;
    }
}
pub fn main() !void {
    var out: [8]i32 = undefined;
    dailyTemperatures(&[_]i32{ 73, 74, 75, 71, 69, 72, 76, 73 }, &out);
    if (out[0] != 1 or out[2] != 4 or out[7] != 0) return error.TestFailed;
    dailyTemperatures(&[_]i32{ 30, 40, 50, 60 }, &out);
    if (out[0] != 1 or out[3] != 0) return error.TestFailed;
    dailyTemperatures(&[_]i32{ 30, 60, 90 }, &out);
    if (out[0] != 1 or out[2] != 0) return error.TestFailed;
    std.debug.print("PASS\\n", .{}); }''',
"dart":'''List<int> dailyTemperatures(List<int> temps) {
  final n = temps.length;
  final res = List<int>.filled(n, 0);
  final st = <int>[];
  for (var i = 0; i < n; i++) {
    while (st.isNotEmpty && temps[st.last] < temps[i]) {
      final idx = st.removeLast();
      res[idx] = i - idx;
    }
    st.add(i);
  }
  return res;
}
void main() { if (dailyTemperatures([73,74,75,71,69,72,76,73]).toString() != '[1, 1, 4, 2, 1, 1, 0, 0]') throw StateError('c1'); if (dailyTemperatures([30,40,50,60]).toString() != '[1, 1, 1, 0]') throw StateError('c2'); if (dailyTemperatures([30,60,90]).toString() != '[1, 1, 0]') throw StateError('c3'); print('PASS'); }''',
}

T["71"] = {
"rust":'''fn simplify_path(path: String) -> String {
    let mut st: Vec<&str> = Vec::new();
    for part in path.split('/') {
        match part {
            "" | "." => {}
            ".." => { st.pop(); }
            _ => st.push(part),
        }
    }
    format!("/{}", st.join("/"))
}
fn main() {
    assert_eq!(simplify_path("/home/".into()), "/home");
    assert_eq!(simplify_path("/../".into()), "/");
    assert_eq!(simplify_path("/home//foo/".into()), "/home/foo");
    assert_eq!(simplify_path("/a/./b/../../c/".into()), "/c");
    println!("PASS"); }''',
"lua":'''local function simplify_path(path)
    local st = {}
    for part in path:gmatch("[^/]+") do
        if part == ".." then
            if #st > 0 then st[#st] = nil end
        elseif part ~= "." then
            st[#st + 1] = part
        end
    end
    if #st == 0 then return "/" end
    return "/" .. table.concat(st, "/")
end
assert(simplify_path("/home/") == "/home")
assert(simplify_path("/../") == "/")
assert(simplify_path("/home//foo/") == "/home/foo")
assert(simplify_path("/a/./b/../../c/") == "/c")
print("PASS")''',
"c":'''#include <stdio.h>
#include <string.h>
static void simplify_path(const char *path, char out[]) {
    char *parts[1024];
    int pn = 0;
    char buf[8192];
    strncpy(buf, path, sizeof(buf) - 1);
    buf[sizeof(buf) - 1] = '\\0';
    char *tok = strtok(buf, "/");
    while (tok) {
        if (strcmp(tok, "..") == 0) { if (pn > 0) pn--; }
        else if (strcmp(tok, ".") != 0) parts[pn++] = tok;
        tok = strtok(NULL, "/");
    }
    int pos = 0;
    if (pn == 0) { out[pos++] = '/'; }
    else for (int i = 0; i < pn; i++) {
        out[pos++] = '/';
        strcpy(out + pos, parts[i]);
        pos += strlen(parts[i]);
    }
    out[pos] = '\\0';
}
int main(void) {
    char out[8192];
    simplify_path("/home/", out);
    if (strcmp(out, "/home") != 0) { printf("FAIL 1\\n"); return 1; }
    simplify_path("/../", out);
    if (strcmp(out, "/") != 0) { printf("FAIL 2\\n"); return 1; }
    simplify_path("/home//foo/", out);
    if (strcmp(out, "/home/foo") != 0) { printf("FAIL 3\\n"); return 1; }
    simplify_path("/a/./b/../../c/", out);
    if (strcmp(out, "/c") != 0) { printf("FAIL 4\\n"); return 1; }
    printf("PASS\\n"); return 0; }''',
"cpp":'''#include <cassert>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
static std::string simplifyPath(const std::string &path) {
    std::vector<std::string> st;
    std::istringstream iss(path);
    std::string part;
    while (std::getline(iss, part, '/')) {
        if (part.empty() || part == ".") continue;
        if (part == "..") { if (!st.empty()) st.pop_back(); }
        else st.push_back(part);
    }
    std::string out = "/";
    for (size_t i = 0; i < st.size(); ++i) {
        if (i) out += "/";
        out += st[i];
    }
    return out;
}
int main() { assert(simplifyPath("/home/") == "/home"); assert(simplifyPath("/../") == "/"); assert(simplifyPath("/home//foo/") == "/home/foo"); assert(simplifyPath("/a/./b/../../c/") == "/c"); std::cout << "PASS" << std::endl; }''',
"r":'''simplify_path <- function(path) {
  parts <- strsplit(path, "/")[[1]]
  st <- character(0)
  for (p in parts) {
    if (p == "" || p == ".") next
    if (p == "..") { if (length(st) > 0) st <- st[-length(st)] }
    else st <- c(st, p)
  }
  if (length(st) == 0) return("/")
  paste0("/", paste(st, collapse = "/"))
}
stopifnot(simplify_path("/home/") == "/home")
stopifnot(simplify_path("/../") == "/")
stopifnot(simplify_path("/home//foo/") == "/home/foo")
stopifnot(simplify_path("/a/./b/../../c/") == "/c")
cat("PASS\\n")''',
"zig":'''const std = @import("std");
fn simplifyPath(path: []const u8, out: *std.ArrayList(u8)) void {
    var parts: [1024][]const u8 = undefined;
    var pn: usize = 0;
    var it = std.mem.splitScalar(u8, path, '/');
    while (it.next()) |part| {
        if (part.len == 0 or std.mem.eql(u8, part, ".")) continue;
        if (std.mem.eql(u8, part, "..")) {
            if (pn > 0) pn -= 1;
        } else {
            parts[pn] = part;
            pn += 1;
        }
    }
    if (pn == 0) {
        out.append('/') catch unreachable;
        return;
    }
    for (0..pn) |i| {
        out.append('/') catch unreachable;
        out.appendSlice(parts[i]) catch unreachable;
    }
}
pub fn main() !void {
    var out = std.ArrayList(u8).init(std.heap.page_allocator);
    defer out.deinit();
    simplifyPath("/home/", &out);
    if (!std.mem.eql(u8, out.items, "/home")) return error.TestFailed;
    out.clearRetainingCapacity();
    simplifyPath("/../", &out);
    if (!std.mem.eql(u8, out.items, "/")) return error.TestFailed;
    out.clearRetainingCapacity();
    simplifyPath("/home//foo/", &out);
    if (!std.mem.eql(u8, out.items, "/home/foo")) return error.TestFailed;
    out.clearRetainingCapacity();
    simplifyPath("/a/./b/../../c/", &out);
    if (!std.mem.eql(u8, out.items, "/c")) return error.TestFailed;
    std.debug.print("PASS\\n", .{}); }''',
"dart":'''String simplifyPath(String path) {
  final st = <String>[];
  for (final part in path.split('/')) {
    if (part.isEmpty || part == '.') continue;
    if (part == '..') {
      if (st.isNotEmpty) st.removeLast();
    } else {
      st.add(part);
    }
  }
  return st.isEmpty ? '/' : '/' + st.join('/');
}
void main() { if (simplifyPath('/home/') != '/home') throw StateError('c1'); if (simplifyPath('/../') != '/') throw StateError('c2'); if (simplifyPath('/home//foo/') != '/home/foo') throw StateError('c3'); if (simplifyPath('/a/./b/../../c/') != '/c') throw StateError('c4'); print('PASS'); }''',
}

T["682"] = {
"rust":'''fn cal_points(ops: Vec<&str>) -> i32 {
    let mut st: Vec<i32> = Vec::new();
    for op in ops {
        match op {
            "+" => { let b = *st.last().unwrap(); let a = st[st.len() - 2]; st.push(a + b); }
            "D" => { st.push(2 * st.last().unwrap()); }
            "C" => { st.pop(); }
            _ => st.push(op.parse().unwrap()),
        }
    }
    st.iter().sum()
}
fn main() {
    assert_eq!(cal_points(vec!["5","2","C","D","+"]), 30);
    assert_eq!(cal_points(vec!["5","-2","4","C","D","9","+","+"]), 27);
    assert_eq!(cal_points(vec!["1","C"]), 0);
    println!("PASS"); }''',
"lua":'''local function cal_points(ops)
    local st = {}
    for _, op in ipairs(ops) do
        if op == "+" then
            st[#st + 1] = st[#st] + st[#st - 1]
        elseif op == "D" then
            st[#st + 1] = st[#st] * 2
        elseif op == "C" then
            st[#st] = nil
        else
            st[#st + 1] = tonumber(op)
        end
    end
    local sum = 0
    for _, v in ipairs(st) do sum = sum + v end
    return sum
end
assert(cal_points({"5","2","C","D","+"}) == 30)
assert(cal_points({"5","-2","4","C","D","9","+","+"}) == 27)
assert(cal_points({"1","C"}) == 0)
print("PASS")''',
"c":'''#include <stdio.h>
#include <string.h>
#include <stdlib.h>
static int cal_points(const char **ops, int n) {
    int st[4096];
    int top = 0;
    for (int i = 0; i < n; i++) {
        if (strcmp(ops[i], "+") == 0) {
            st[top] = st[top - 1] + st[top - 2];
            top++;
        } else if (strcmp(ops[i], "D") == 0) {
            st[top] = st[top - 1] * 2;
            top++;
        } else if (strcmp(ops[i], "C") == 0) {
            top--;
        } else {
            st[top++] = atoi(ops[i]);
        }
    }
    int sum = 0;
    for (int i = 0; i < top; i++) sum += st[i];
    return sum;
}
int main(void) {
    const char *t1[] = {"5","2","C","D","+"};
    const char *t2[] = {"5","-2","4","C","D","9","+","+"};
    const char *t3[] = {"1","C"};
    if (cal_points(t1, 5) != 30) { printf("FAIL 1\\n"); return 1; }
    if (cal_points(t2, 8) != 27) { printf("FAIL 2\\n"); return 1; }
    if (cal_points(t3, 2) != 0) { printf("FAIL 3\\n"); return 1; }
    printf("PASS\\n"); return 0; }''',
"cpp":'''#include <cassert>
#include <iostream>
#include <string>
#include <vector>
static int calPoints(const std::vector<std::string> &ops) {
    std::vector<int> st;
    for (const auto &op : ops) {
        if (op == "+") st.push_back(st[st.size() - 1] + st[st.size() - 2]);
        else if (op == "D") st.push_back(2 * st.back());
        else if (op == "C") st.pop_back();
        else st.push_back(std::stoi(op));
    }
    int sum = 0;
    for (int v : st) sum += v;
    return sum;
}
int main() { assert(calPoints({"5","2","C","D","+"}) == 30); assert(calPoints({"5","-2","4","C","D","9","+","+"}) == 27); assert(calPoints({"1","C"}) == 0); std::cout << "PASS" << std::endl; }''',
"r":'''cal_points <- function(ops) {
  st <- integer(0)
  for (op in ops) {
    if (op == "+") st <- c(st, st[length(st)] + st[length(st) - 1])
    else if (op == "D") st <- c(st, st[length(st)] * 2)
    else if (op == "C") st <- st[-length(st)]
    else st <- c(st, as.integer(op))
  }
  sum(st)
}
stopifnot(cal_points(c("5","2","C","D","+")) == 30)
stopifnot(cal_points(c("5","-2","4","C","D","9","+","+")) == 27)
stopifnot(cal_points(c("1","C")) == 0)
cat("PASS\\n")''',
"zig":'''const std = @import("std");
fn calPoints(ops: []const []const u8) i32 {
    var st: [4096]i32 = undefined;
    var top: usize = 0;
    for (ops) |op| {
        if (std.mem.eql(u8, op, "+")) {
            st[top] = st[top - 1] + st[top - 2];
            top += 1;
        } else if (std.mem.eql(u8, op, "D")) {
            st[top] = st[top - 1] * 2;
            top += 1;
        } else if (std.mem.eql(u8, op, "C")) {
            top -= 1;
        } else {
            st[top] = std.fmt.parseInt(i32, op, 10) catch unreachable;
            top += 1;
        }
    }
    var sum: i32 = 0;
    for (0..top) |i| sum += st[i];
    return sum;
}
pub fn main() !void {
    if (calPoints(&[_][]const u8{ "5", "2", "C", "D", "+" }) != 30) return error.TestFailed;
    if (calPoints(&[_][]const u8{ "5", "-2", "4", "C", "D", "9", "+", "+" }) != 27) return error.TestFailed;
    if (calPoints(&[_][]const u8{ "1", "C" }) != 0) return error.TestFailed;
    std.debug.print("PASS\\n", .{}); }''',
"dart":'''int calPoints(List<String> ops) {
  final st = <int>[];
  for (final op in ops) {
    if (op == '+') {
      st.add(st[st.length - 1] + st[st.length - 2]);
    } else if (op == 'D') {
      st.add(st.last * 2);
    } else if (op == 'C') {
      st.removeLast();
    } else {
      st.add(int.parse(op));
    }
  }
  var sum = 0;
  for (final v in st) { sum += v; }
  return sum;
}
void main() { if (calPoints(['5','2','C','D','+']) != 30) throw StateError('c1'); if (calPoints(['5','-2','4','C','D','9','+','+']) != 27) throw StateError('c2'); if (calPoints(['1','C']) != 0) throw StateError('c3'); print('PASS'); }''',
}

PROBS = [
    ("1047", "lc_1047_删除字符串中的所有相邻重复项", "LeetCode 1047. 删除字符串中的所有相邻重复项"),
    ("150", "lc_150_逆波兰表达式求值", "LeetCode 150. 逆波兰表达式求值"),
    ("151", "lc_151_反转字符串中的单词", "LeetCode 151. 反转字符串中的单词"),
    ("496", "lc_496_下一个更大元素_i", "LeetCode 496. 下一个更大元素 I"),
    ("503", "lc_503_下一个更大元素_ii", "LeetCode 503. 下一个更大元素 II"),
    ("739", "lc_739_每日温度", "LeetCode 739. 每日温度"),
    ("71", "lc_71_简化路径", "LeetCode 71. 简化路径"),
    ("682", "lc_682_棒球比赛", "LeetCode 682. 棒球比赛"),
]
count = 0
for pid, pdir, title in PROBS:
    bid = B[pid]
    ts_dir = f"/Users/Wang/Code/github/web-x-blog/work/blog/courses/21.dsa/ts/stack/{pdir}"
    sols = sorted(f[:-3] for f in os.listdir(ts_dir) if f.startswith("solution_") and f.endswith(".ts"))
    for lang in LANGNAME:
        ext = EXT[lang]
        for sol in sols:
            n = sol.replace("solution_", "").split("_")[0]
            head = head_comment(lang, bid, f"{title} — {LANGNAME[lang]} 版（方案{n}）")
            emit(lang, f"stack/{pdir}/{sol}.{ext}", head + "\n" + T[pid][lang])
            count += 1
print(f"emitted {count} files")
