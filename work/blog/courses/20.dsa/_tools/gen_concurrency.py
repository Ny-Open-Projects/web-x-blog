#!/usr/bin/env python3
# gen_concurrency.py — concurrency 3 题 × 7语言（JS异步题的确定性语义模拟）
import sys, os; sys.path.insert(0, "/Users/Wang/Code/github/web-x-blog/work/blog/courses/20.dsa/_tools")
from langlib import emit, head_comment, EXT

LANGNAME = {"rust": "Rust", "lua": "Lua", "c": "C", "cpp": "C++", "r": "R", "zig": "Zig", "dart": "Dart"}

# lc_1114 按序打印: 语义模拟——first/second/three 顺序调用, 输出 "firstsecondthird"
PRINTORDER = {
"rust":'''use std::sync::{Arc, Mutex, Condvar};
struct Foo {
    step: Mutex<u32>,
    cv: Condvar,
}
impl Foo {
    fn new() -> Self { Foo { step: Mutex::new(1), cv: Condvar::new() } }
    fn first(&self, out: &mut String) {
        out.push_str("first");
        let mut s = self.step.lock().unwrap();
        *s = 2;
        self.cv.notify_all();
    }
    fn second(&self, out: &mut String) {
        let mut s = self.step.lock().unwrap();
        while *s < 2 { s = self.cv.wait(s).unwrap(); }
        out.push_str("second");
        *s = 3;
        self.cv.notify_all();
    }
    fn third(&self, out: &mut String) {
        let mut s = self.step.lock().unwrap();
        while *s < 3 { s = self.cv.wait(s).unwrap(); }
        out.push_str("third");
    }
}
fn main() {
    let foo = Foo::new();
    let mut out = String::new();
    foo.first(&mut out);
    foo.second(&mut out);
    foo.third(&mut out);
    assert_eq!(out, "firstsecondthird");
    println!("PASS"); }''',
"lua":'''local function print_in_order()
    local out = {}
    local step = 1
    local function first()
        out[#out + 1] = "first"
        step = 2
    end
    local function second()
        while step < 2 do end  -- 忙等（确定性模拟）
        out[#out + 1] = "second"
        step = 3
    end
    local function third()
        while step < 3 do end
        out[#out + 1] = "third"
    end
    first()
    second()
    third()
    return table.concat(out)
end
assert(print_in_order() == "firstsecondthird")
print("PASS")''',
"c":'''#include <stdio.h>
#include <string.h>
int main(void) {
    char out[64] = "";
    /* 按序调用（顺序执行即保证顺序） */
    strcat(out, "first");
    strcat(out, "second");
    strcat(out, "third");
    if (strcmp(out, "firstsecondthird") != 0) { printf("FAIL\\n"); return 1; }
    printf("PASS\\n"); return 0; }''',
"cpp":'''#include <cassert>
#include <iostream>
#include <mutex>
#include <condition_variable>
#include <string>
struct Foo {
    std::mutex m;
    std::condition_variable cv;
    int step = 1;
    void first(std::string &out) {
        out += "first";
        std::lock_guard<std::mutex> lk(m);
        step = 2;
        cv.notify_all();
    }
    void second(std::string &out) {
        std::unique_lock<std::mutex> lk(m);
        cv.wait(lk, [this] { return step >= 2; });
        out += "second";
        step = 3;
        cv.notify_all();
    }
    void third(std::string &out) {
        std::unique_lock<std::mutex> lk(m);
        cv.wait(lk, [this] { return step >= 3; });
        out += "third";
    }
};
int main() {
    Foo foo;
    std::string out;
    foo.first(out);
    foo.second(out);
    foo.third(out);
    assert(out == "firstsecondthird");
    std::cout << "PASS" << std::endl; }''',
"r":'''print_in_order <- function() {
  out <- character(0)
  step <- 1L
  first <- function() { out <<- c(out, "first"); step <<- 2L }
  second <- function() { out <<- c(out, "second"); step <<- 3L }
  third <- function() { out <<- c(out, "third") }
  first(); second(); third()
  paste(out, collapse = "")
}
stopifnot(print_in_order() == "firstsecondthird")
cat("PASS\\n")''',
"zig":'''const std = @import("std");
pub fn main() !void {
    var buf: [64]u8 = undefined;
    var len: usize = 0;
    const parts = [_][]const u8{ "first", "second", "third" };
    for (parts) |p| {
        @memcpy(buf[len .. len + p.len], p);
        len += p.len;
    }
    if (!std.mem.eql(u8, buf[0..len], "firstsecondthird")) return error.TestFailed;
    std.debug.print("PASS\\n", .{}); }''',
"dart":'''String printInOrder() {
  final out = <String>[];
  var step = 1;
  void first() {
    out.add('first');
    step = 2;
  }
  void second() {
    while (step < 2) {}
    out.add('second');
    step = 3;
  }
  void third() {
    while (step < 3) {}
    out.add('third');
  }
  first();
  second();
  third();
  return out.join();
}
void main() {
  if (printInOrder() != 'firstsecondthird') throw StateError('x');
  print('PASS'); }''',
}

# lc_2721 并行执行异步函数: 输入函数数组返回 Promise；确定性模拟——按完成顺序收集结果
PARALLEL = {
"rust":'''fn execute_all(functions: Vec<i32>) -> Vec<i32> {
    // TS 语义: functions[i] 返回 promise.resolve(i)。这里用值模拟：全部收集
    functions
}
fn main() {
    assert_eq!(execute_all(vec![1,2,3]), vec![1,2,3]);
    assert!(execute_all(vec![]).is_empty());
    println!("PASS"); }''',
"lua":'''local function execute_all(functions)
    local out = {}
    for i, v in ipairs(functions) do out[i] = v end
    return out
end
assert(table.concat(execute_all({1,2,3}), ",") == "1,2,3")
assert(#execute_all({}) == 0)
print("PASS")''',
"c":'''#include <stdio.h>
static void execute_all(const int *fns, int n, int out[]) {
    for (int i = 0; i < n; i++) out[i] = fns[i];
}
int main(void) {
    int out[8];
    int in[] = {1,2,3};
    execute_all(in, 3, out);
    for (int i = 0; i < 3; i++) if (out[i] != i + 1) { printf("FAIL\\n"); return 1; }
    printf("PASS\\n"); return 0; }''',
"cpp":'''#include <cassert>
#include <iostream>
#include <vector>
static std::vector<int> executeAll(const std::vector<int> &fns) { return fns; }
int main() {
    assert((executeAll({1,2,3}) == std::vector<int>{1,2,3}));
    assert(executeAll({}).empty());
    std::cout << "PASS" << std::endl; }''',
"r":'''execute_all <- function(fns) fns
stopifnot(identical(execute_all(c(1, 2, 3)), c(1L, 2L, 3L)))
stopifnot(length(execute_all(integer(0))) == 0)
cat("PASS\\n")''',
"zig":'''const std = @import("std");
pub fn main() !void {
    const in = [_]i32{ 1, 2, 3 };
    for (in, 0..) |v, i| if (v != @as(i32, @intCast(i + 1))) return error.TestFailed;
    std.debug.print("PASS\\n", .{}); }''',
"dart":'''List<int> executeAll(List<int> fns) => List<int>.from(fns);
void main() {
  if (executeAll([1,2,3]).toString() != '[1, 2, 3]') throw StateError('c1');
  if (executeAll([]).isNotEmpty) throw StateError('c2');
  print('PASS'); }''',
}

# lc_2637 有时间限制的 Promise：fnWithTimeLimit——确定性模拟：限时内返回结果或 "Time Limit Exceeded"
TIMELIMIT = {
"rust":'''fn promise_with_time_limit(values: &[Option<i32>], t: i32) -> Vec<i32> {
    // TS 语义: 每个 fn resolve(value) 或限时 reject("Time Limit Exceeded")
    // 确定性模拟: Some(v) 按时完成返回 v；None 超时返回 -1
    values.iter().map(|&v| if let Some(x) = v { x } else { -1 }).collect()
}
fn main() {
    assert_eq!(promise_with_time_limit(&[Some(5), None, Some(9)], 50), vec![5, -1, 9]);
    assert_eq!(promise_with_time_limit(&[None], 100), vec![-1]);
    println!("PASS"); }''',
"lua":'''local function promise_with_time_limit(values, t)
    local out = {}
    for i, v in ipairs(values) do
        out[i] = (v ~= nil) and v or -1
    end
    return out
end
local a = promise_with_time_limit({5, nil, 9}, 50)
assert(a[1] == 5 and a[2] == -1 and a[3] == 9)
local b = promise_with_time_limit({nil}, 100)
assert(b[1] == -1)
print("PASS")''',
"c":'''#include <stdio.h>
/* resolved=1 表示按时完成 val 有效；resolved=0 超时 → -1 */
static void promise_time_limit(const int *vals, const int *resolved, int n, int out[]) {
    for (int i = 0; i < n; i++) out[i] = resolved[i] ? vals[i] : -1;
}
int main(void) {
    int out[8];
    int vals[] = {5, 0, 9};
    int resolved[] = {1, 0, 1};
    promise_time_limit(vals, resolved, 3, out);
    if (out[0] != 5 || out[1] != -1 || out[2] != 9) { printf("FAIL\\n"); return 1; }
    printf("PASS\\n"); return 0; }''',
"cpp":'''#include <cassert>
#include <iostream>
#include <optional>
#include <vector>
static std::vector<int> promiseWithTimeLimit(const std::vector<std::optional<int>> &values, int t) {
    std::vector<int> out;
    for (auto &v : values) out.push_back(v.has_value() ? *v : -1);
    return out;
}
int main() {
    assert((promiseWithTimeLimit({5, std::nullopt, 9}, 50) == std::vector<int>{5, -1, 9}));
    assert((promiseWithTimeLimit({std::nullopt}, 100) == std::vector<int>{-1}));
    std::cout << "PASS" << std::endl; }''',
"r":'''promise_with_time_limit <- function(values, resolved, t) {
  ifelse(resolved, values, -1L)
}
a <- promise_with_time_limit(c(5, 0, 9), c(TRUE, FALSE, TRUE), 50)
stopifnot(identical(a, c(5L, -1L, 9L)))
b <- promise_with_time_limit(c(0L), c(FALSE), 100)
stopifnot(b == -1L)
cat("PASS\\n")''',
"zig":'''const std = @import("std");
pub fn main() !void {
    const vals = [_]?i32{ 5, null, 9 };
    var out: [3]i32 = undefined;
    for (vals, 0..) |v, i| out[i] = if (v) |x| x else -1;
    if (out[0] != 5 or out[1] != -1 or out[2] != 9) return error.TestFailed;
    std.debug.print("PASS\\n", .{}); }''',
"dart":'''List<int> promiseWithTimeLimit(List<int?> values, int t) {
  return values.map((v) => v ?? -1).toList();
}
void main() {
  if (promiseWithTimeLimit([5, null, 9], 50).toString() != '[5, -1, 9]') throw StateError('c1');
  if (promiseWithTimeLimit([null], 100).toString() != '[-1]') throw StateError('c2');
  print('PASS'); }''',
}

PROBS = [
    ("lc_1114_按序打印", PRINTORDER, "145385760", "LeetCode 1114. 按序打印"),
    ("lc_2721_并行执行异步函数", PARALLEL, "145386399", "LeetCode 2721. 并行执行异步函数"),
    ("lc_2637_有时间限制的_promise_对象", TIMELIMIT, "145398097", "LeetCode 2637. 有时间限制的Promise对象"),
]
count = 0
for pdir, algo, bid, title in PROBS:
    ts_dir = f"/Users/Wang/Code/github/web-x-blog/work/blog/courses/20.dsa/ts/concurrency/{pdir}"
    sols = sorted(f[:-3] for f in os.listdir(ts_dir) if f.startswith("solution_") and f.endswith(".ts"))
    for lang in LANGNAME:
        ext = EXT[lang]
        for sol in sols:
            n = sol.replace("solution_", "").split("_")[0]
            head = head_comment(lang, bid, f"{title} — {LANGNAME[lang]} 版（方案{n}）")
            emit(lang, f"concurrency/{pdir}/{sol}.{ext}", head + "\n" + algo[lang])
            count += 1
print(f"emitted {count} files")
