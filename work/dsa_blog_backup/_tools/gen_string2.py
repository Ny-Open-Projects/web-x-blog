#!/usr/bin/env python3
# gen_string2.py — string 第二批：lc_20/lc_567/lc_117(复用tree模板) × 7语言
import sys, os; sys.path.insert(0, "/Users/Wang/Code/webfault-ai/dsa/_tools")
from langlib import emit, head_comment, EXT

B = {"20": "133759617", "567": "135917076", "117": "145386298"}
LANGNAME = {"rust": "Rust", "lua": "Lua", "c": "C", "cpp": "C++", "r": "R", "zig": "Zig", "dart": "Dart"}

A20 = {
"rust": '''fn is_valid(s: String) -> bool {
    let mut stack: Vec<char> = Vec::new();
    for ch in s.chars() {
        match ch {
            ')' => { if stack.pop() != Some('(') { return false; } }
            ']' => { if stack.pop() != Some('[') { return false; } }
            '}' => { if stack.pop() != Some('{') { return false; } }
            _ => stack.push(ch),
        }
    }
    stack.is_empty()
}
fn main() {
    let tests = ["(", "()", "()[]{}", "(]", "([)]", "abc"];
    let want = [false, true, true, false, false, false];
    for (i, t) in tests.iter().enumerate() {
        assert_eq!(is_valid(t.to_string()), want[i], "case {}", i);
    }
    println!("PASS");
}
''',
"lua": '''local function is_valid(s)
    local stack = {}
    local pairs = {[")"] = "(", ["]"] = "[", ["}"] = "{"}
    for i = 1, #s do
        local ch = s:sub(i, i)
        if pairs[ch] then
            local top = #stack > 0 and table.remove(stack) or "#"
            if top ~= pairs[ch] then return false end
        else
            stack[#stack + 1] = ch
        end
    end
    return #stack == 0
end
local tests = {"(", "()", "()[]{}", "(]", "([)]", "abc"}
local want = {false, true, true, false, false, false}
for i, t in ipairs(tests) do
    assert(is_valid(t) == want[i], "case " .. i)
end
print("PASS")
''',
"c": '''#include <stdio.h>
#include <string.h>
static int is_valid(const char *s) {
    char stack[8192];
    int top = 0;
    for (const char *p = s; *p; p++) {
        if (*p == ')') {
            if (top == 0 || stack[--top] != '(') return 0;
        } else if (*p == ']') {
            if (top == 0 || stack[--top] != '[') return 0;
        } else if (*p == '}') {
            if (top == 0 || stack[--top] != '{') return 0;
        } else {
            stack[top++] = *p;
        }
    }
    return top == 0;
}
int main(void) {
    const char *tests[] = {"(", "()", "()[]{}", "(]", "([)]", "abc"};
    const int want[] = {0, 1, 1, 0, 0, 0};
    for (int i = 0; i < 6; i++) {
        if (is_valid(tests[i]) != want[i]) { printf("FAIL %d\\n", i); return 1; }
    }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''#include <cassert>
#include <iostream>
#include <string>
#include <vector>
static bool isValid(const std::string &s) {
    std::vector<char> stack;
    for (char ch : s) {
        if (ch == ')') {
            if (stack.empty() || stack.back() != '(') return false;
            stack.pop_back();
        } else if (ch == ']') {
            if (stack.empty() || stack.back() != '[') return false;
            stack.pop_back();
        } else if (ch == '}') {
            if (stack.empty() || stack.back() != '{') return false;
            stack.pop_back();
        } else {
            stack.push_back(ch);
        }
    }
    return stack.empty();
}
int main() {
    std::vector<std::string> tests = {"(", "()", "()[]{}", "(]", "([)]", "abc"};
    std::vector<bool> want = {false, true, true, false, false, false};
    for (size_t i = 0; i < tests.size(); ++i) {
        assert(isValid(tests[i]) == want[i]);
    }
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''is_valid <- function(s) {
  chars <- strsplit(s, "")[[1]]
  stack <- character(0)
  pairs <- c(")" = "(", "]" = "[", "}" = "{")
  for (ch in chars) {
    if (ch %in% names(pairs)) {
      top <- if (length(stack) > 0) stack[length(stack)] else "#"
      if (length(stack) > 0) stack <- stack[-length(stack)]
      if (top != pairs[[ch]]) return(FALSE)
    } else {
      stack <- c(stack, ch)
    }
  }
  length(stack) == 0
}
tests <- c("(", "()", "()[]{}", "(]", "([)]", "abc")
want <- c(FALSE, TRUE, TRUE, FALSE, FALSE, FALSE)
for (i in seq_along(tests)) {
  stopifnot(is_valid(tests[i]) == want[i])
}
cat("PASS\\n")
''',
"zig": '''const std = @import("std");
fn isValid(s: []const u8) bool {
    var stack: [8192]u8 = undefined;
    var top: usize = 0;
    for (s) |ch| {
        switch (ch) {
            ')' => {
                if (top == 0 or stack[top - 1] != '(') return false;
                top -= 1;
            },
            ']' => {
                if (top == 0 or stack[top - 1] != '[') return false;
                top -= 1;
            },
            '}' => {
                if (top == 0 or stack[top - 1] != '{') return false;
                top -= 1;
            },
            else => {
                stack[top] = ch;
                top += 1;
            },
        }
    }
    return top == 0;
}
pub fn main() !void {
    const tests = [_][]const u8{ "(", "()", "()[]{}", "(]", "([)]", "abc" };
    const want = [_]bool{ false, true, true, false, false, false };
    for (tests, want) |t, w| {
        if (isValid(t) != w) return error.TestFailed;
    }
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''bool isValid(String s) {
  final stack = <String>[];
  final pairs = {')': '(', ']': '[', '}': '{'};
  for (final ch in s.split('')) {
    if (pairs.containsKey(ch)) {
      final top = stack.isNotEmpty ? stack.removeLast() : '#';
      if (top != pairs[ch]) return false;
    } else {
      stack.add(ch);
    }
  }
  return stack.isEmpty;
}
void main() {
  final tests = ['(', '()', "()[]{}", '(]', '([)]', 'abc'];
  final want = [false, true, true, false, false, false];
  for (var i = 0; i < tests.length; i++) {
    if (isValid(tests[i]) != want[i]) throw StateError('case $i');
  }
  print('PASS');
}
''',
}

A567 = {
"rust": '''fn check_inclusion(s1: String, s2: String) -> bool {
    let (a, b) = (s1.as_bytes(), s2.as_bytes());
    let (m, n) = (a.len(), b.len());
    if m > n { return false; }
    let mut s1c = [0i32; 26];
    let mut s2c = [0i32; 26];
    for i in 0..m {
        s1c[(a[i] - b'a') as usize] += 1;
        s2c[(b[i] - b'a') as usize] += 1;
    }
    if s1c == s2c { return true; }
    for i in m..n {
        s2c[(b[i] - b'a') as usize] += 1;
        s2c[(b[i - m] - b'a') as usize] -= 1;
        if s1c == s2c { return true; }
    }
    false
}
fn main() {
    assert!(check_inclusion("ab".into(), "eidbaooo".into()));
    assert!(!check_inclusion("ab".into(), "eidboaoo".into()));
    println!("PASS");
}
''',
"lua": '''local function check_inclusion(s1, s2)
    local m, n = #s1, #s2
    if m > n then return false end
    local s1c, s2c = {}, {}
    for i = 1, m do
        local c1 = s1:byte(i) - 97
        local c2 = s2:byte(i) - 97
        s1c[c1] = (s1c[c1] or 0) + 1
        s2c[c2] = (s2c[c2] or 0) + 1
    end
    local function eq()
        for k, v in pairs(s1c) do
            if (s2c[k] or 0) ~= v then return false end
        end
        for k, v in pairs(s2c) do
            if (s1c[k] or 0) ~= v then return false end
        end
        return true
    end
    if eq() then return true end
    for i = m + 1, n do
        local c2 = s2:byte(i) - 97
        local c0 = s2:byte(i - m) - 97
        s2c[c2] = (s2c[c2] or 0) + 1
        s2c[c0] = (s2c[c0] or 0) - 1
        if s2c[c0] == 0 then s2c[c0] = nil end
        if eq() then return true end
    end
    return false
end
assert(check_inclusion("ab", "eidbaooo") == true)
assert(check_inclusion("ab", "eidboaoo") == false)
print("PASS")
''',
"c": '''#include <stdio.h>
#include <string.h>
static int cnt_eq(const int a[26], const int b[26]) {
    for (int i = 0; i < 26; i++) if (a[i] != b[i]) return 0;
    return 1;
}
static int check_inclusion(const char *s1, const char *s2) {
    int m = (int)strlen(s1), n = (int)strlen(s2);
    if (m > n) return 0;
    int s1c[26] = {0}, s2c[26] = {0};
    for (int i = 0; i < m; i++) {
        s1c[s1[i] - 'a']++;
        s2c[s2[i] - 'a']++;
    }
    if (cnt_eq(s1c, s2c)) return 1;
    for (int i = m; i < n; i++) {
        s2c[s2[i] - 'a']++;
        s2c[s2[i - m] - 'a']--;
        if (cnt_eq(s1c, s2c)) return 1;
    }
    return 0;
}
int main(void) {
    if (!check_inclusion("ab", "eidbaooo")) { printf("FAIL 1\\n"); return 1; }
    if (check_inclusion("ab", "eidboaoo")) { printf("FAIL 2\\n"); return 1; }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''#include <cassert>
#include <iostream>
#include <string>
#include <vector>
static bool checkInclusion(const std::string &s1, const std::string &s2) {
    int m = static_cast<int>(s1.size()), n = static_cast<int>(s2.size());
    if (m > n) return false;
    std::vector<int> s1c(26, 0), s2c(26, 0);
    for (int i = 0; i < m; ++i) {
        ++s1c[s1[i] - 'a'];
        ++s2c[s2[i] - 'a'];
    }
    if (s1c == s2c) return true;
    for (int i = m; i < n; ++i) {
        ++s2c[s2[i] - 'a'];
        --s2c[s2[i - m] - 'a'];
        if (s1c == s2c) return true;
    }
    return false;
}
int main() {
    assert(checkInclusion("ab", "eidbaooo"));
    assert(!checkInclusion("ab", "eidboaoo"));
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''check_inclusion <- function(s1, s2) {
  a <- strsplit(s1, "")[[1]]
  b <- strsplit(s2, "")[[1]]
  m <- length(a); n <- length(b)
  if (m > n) return(FALSE)
  ci <- function(str, from, to) {
    cnt <- rep(0L, 26)
    for (ch in str[from:to]) cnt[utf8ToInt(ch) - 96] <- cnt[utf8ToInt(ch) - 96] + 1L
    cnt
  }
  s1c <- ci(a, 1, m)
  s2c <- ci(b, 1, m)
  if (identical(s1c, s2c)) return(TRUE)
  for (i in (m + 1):n) {
    s2c <- ci(b, i - m + 1, i)  # 简化重算窗口（正确性优先）
    if (identical(s1c, s2c)) return(TRUE)
  }
  FALSE
}
stopifnot(check_inclusion("ab", "eidbaooo"))
stopifnot(!check_inclusion("ab", "eidboaoo"))
cat("PASS\\n")
''',
"zig": '''const std = @import("std");
fn cntEq(a: *const [26]i32, b: *const [26]i32) bool {
    for (a, b) |x, y| if (x != y) return false;
    return true;
}
fn checkInclusion(s1: []const u8, s2: []const u8) bool {
    const m = s1.len;
    const n = s2.len;
    if (m > n) return false;
    var s1c = [_]i32{0} ** 26;
    var s2c = [_]i32{0} ** 26;
    for (0..m) |i| {
        s1c[s1[i] - 'a'] += 1;
        s2c[s2[i] - 'a'] += 1;
    }
    if (cntEq(&s1c, &s2c)) return true;
    for (m..n) |i| {
        s2c[s2[i] - 'a'] += 1;
        s2c[s2[i - m] - 'a'] -= 1;
        if (cntEq(&s1c, &s2c)) return true;
    }
    return false;
}
pub fn main() !void {
    if (!checkInclusion("ab", "eidbaooo")) return error.TestFailed;
    if (checkInclusion("ab", "eidboaoo")) return error.TestFailed;
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''bool checkInclusion(String s1, String s2) {
  final m = s1.length, n = s2.length;
  if (m > n) return false;
  final s1c = List<int>.filled(26, 0);
  final s2c = List<int>.filled(26, 0);
  for (var i = 0; i < m; i++) {
    s1c[s1.codeUnitAt(i) - 97]++;
    s2c[s2.codeUnitAt(i) - 97]++;
  }
  bool eq() {
    for (var i = 0; i < 26; i++) {
      if (s1c[i] != s2c[i]) return false;
    }
    return true;
  }
  if (eq()) return true;
  for (var i = m; i < n; i++) {
    s2c[s2.codeUnitAt(i) - 97]++;
    s2c[s2.codeUnitAt(i - m) - 97]--;
    if (eq()) return true;
  }
  return false;
}
void main() {
  if (!checkInclusion('ab', 'eidbaooo')) throw StateError('c1');
  if (checkInclusion('ab', 'eidboaoo')) throw StateError('c2');
  print('PASS');
}
''',
}

# 117 复用 tree 的模板（gen_tree7 的 A117）
sys.path.insert(0, "/Users/Wang/Code/webfault-ai/dsa/_tools")
import importlib.util
spec = importlib.util.spec_from_file_location("gt7", "/Users/Wang/Code/webfault-ai/dsa/_tools/gen_tree7.py")
# gen_tree7 顶层会 emit，不能 import；改为直接读 tree 下已生成的 117 文件内容复制
def clone_tree_117(lang, prob_dir_src, sol):
    ext = EXT[lang]
    src = f"/Users/Wang/Code/webfault-ai/dsa/{lang}/tree/lc_117_填充每个节点的下一个右侧节点指针_ii/{sol}.{ext}"
    with open(src) as fh:
        return fh.read()

PROBS = [
    ("lc_20_有效的括号", A20, "LeetCode 20. 有效的括号"),
    ("lc_567_字符串的排列", A567, "LeetCode 567. 字符串的排列"),
]
count = 0
for prob, algo, title in PROBS:
    bid = B[prob.split("_")[1]]
    ts_dir = f"/Users/Wang/Code/webfault-ai/dsa/ts/string/{prob}"
    sols = sorted(f[:-3] for f in os.listdir(ts_dir) if f.startswith("solution_") and f.endswith(".ts"))
    for lang in EXT:
        ext = EXT[lang]
        for sol in sols:
            n = sol.replace("solution_", "").split("_")[0]
            head = head_comment(lang, bid, f"{title} — {LANGNAME[lang]} 版（方案{n}）")
            emit(lang, f"string/{prob}/{sol}.{ext}", head + "\n" + algo[lang])
            count += 1

# 117: 从 tree 目录克隆（同题不同主题目录）
src_dir_name = "lc_117_填充每个节点的下一个右侧节点指针_ii"
ts_dir = f"/Users/Wang/Code/webfault-ai/dsa/ts/string/lc_117_填充每个节点的下一个右侧节点指针_ii"
sols = sorted(f[:-3] for f in os.listdir(ts_dir) if f.startswith("solution_") and f.endswith(".ts"))
for lang in EXT:
    ext = EXT[lang]
    for sol in sols:
        content = clone_tree_117(lang, src_dir_name, sol)
        emit(lang, f"string/lc_117_填充每个节点的下一个右侧节点指针_ii/{sol}.{ext}", content)
        count += 1
print(f"emitted {count} files")
