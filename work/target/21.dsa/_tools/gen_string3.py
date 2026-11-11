#!/usr/bin/env python3
# gen_string3.py — string 收官：lc_557/lc_696 × 7语言
import sys, os; sys.path.insert(0, "/Users/Wang/Code/github/web-x-blog/work/target/21.dsa/_tools")
from langlib import emit, head_comment, EXT

B = {"557": "145565975", "696": "135756434"}
LANGNAME = {"rust": "Rust", "lua": "Lua", "c": "C", "cpp": "C++", "r": "R", "zig": "Zig", "dart": "Dart"}

A557 = {
"rust": '''fn reverse_words(s: String) -> String {
    s.split(' ').map(|w| w.chars().rev().collect::<String>()).collect::<Vec<_>>().join(" ")
}
fn main() {
    assert_eq!(reverse_words("Let's take LeetCode contest".into()), "s'teL ekat edoCteeL tsetnoc");
    assert_eq!(reverse_words("God Ding".into()), "doG gniD");
    println!("PASS");
}
''',
"lua": '''local function reverse_words(s)
    local out = {}
    for w in s:gmatch("[^ ]+") do
        out[#out + 1] = w:reverse()
    end
    return table.concat(out, " ")
end
assert(reverse_words("Let's take LeetCode contest") == "s'teL ekat edoCteeL tsetnoc")
assert(reverse_words("God Ding") == "doG gniD")
print("PASS")
''',
"c": '''#include <stdio.h>
#include <string.h>
static void reverse_words(const char *s, char out[]) {
    int pos = 0;
    const char *p = s;
    while (*p) {
        while (*p == ' ') p++;
        if (!*p) break;
        const char *start = p;
        while (*p && *p != ' ') p++;
        int len = (int)(p - start);
        for (int i = len - 1; i >= 0; i--) out[pos++] = start[i];
        while (*p == ' ') p++;
        if (*p) out[pos++] = ' ';
    }
    out[pos] = '\\0';
}
int main(void) {
    char out[8192];
    reverse_words("Let's take LeetCode contest", out);
    if (strcmp(out, "s'teL ekat edoCteeL tsetnoc") != 0) { printf("FAIL 1 %s\\n", out); return 1; }
    reverse_words("God Ding", out);
    if (strcmp(out, "doG gniD") != 0) { printf("FAIL 2 %s\\n", out); return 1; }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''#include <algorithm>
#include <cassert>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
static std::string reverseWords(const std::string &s) {
    std::vector<std::string> words;
    std::istringstream iss(s);
    std::string w;
    while (iss >> w) {
        std::reverse(w.begin(), w.end());
        words.push_back(w);
    }
    std::string out;
    for (size_t i = 0; i < words.size(); ++i) {
        if (i) out += " ";
        out += words[i];
    }
    return out;
}
int main() {
    assert(reverseWords("Let's take LeetCode contest") == "s'teL ekat edoCteeL tsetnoc");
    assert(reverseWords("God Ding") == "doG gniD");
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''reverse_words <- function(s) {
  words <- strsplit(s, " ")[[1]]
  paste(vapply(words, function(w) paste(rev(strsplit(w, "")[[1]]), collapse = ""), ""), collapse = " ")
}
stopifnot(reverse_words("Let's take LeetCode contest") == "s'teL ekat edoCteeL tsetnoc")
stopifnot(reverse_words("God Ding") == "doG gniD")
cat("PASS\\n")
''',
"zig": '''const std = @import("std");
fn reverseWords(s: []const u8, out: *std.ArrayList(u8)) void {
    var it = std.mem.tokenizeScalar(u8, s, ' ');
    var first = true;
    while (it.next()) |w| {
        if (!first) out.append(' ') catch unreachable;
        first = false;
        var i: usize = w.len;
        while (i > 0) {
            i -= 1;
            out.append(w[i]) catch unreachable;
        }
    }
}
pub fn main() !void {
    var out = std.ArrayList(u8).init(std.heap.page_allocator);
    defer out.deinit();
    reverseWords("Let's take LeetCode contest", &out);
    if (!std.mem.eql(u8, out.items, "s'teL ekat edoCteeL tsetnoc")) return error.TestFailed;
    out.clearRetainingCapacity();
    reverseWords("God Ding", &out);
    if (!std.mem.eql(u8, out.items, "doG gniD")) return error.TestFailed;
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''String reverseWords(String s) {
  final out = <String>[];
  for (final w in s.split(' ')) {
    if (w.isEmpty) continue;
    out.add(w.split('').reversed.join());
  }
  return out.join(' ');
}
void main() {
  if (reverseWords("Let's take LeetCode contest") != "s'teL ekat edoCteeL tsetnoc") throw StateError('c1');
  if (reverseWords('God Ding') != 'doG gniD') throw StateError('c2');
  print('PASS');
}
''',
}

A696 = {
"rust": '''fn count_binary_substrings(s: String) -> i32 {
    let b = s.as_bytes();
    let n = b.len();
    let mut groups: Vec<i32> = Vec::new();
    let mut i = 0usize;
    while i < n {
        let ch = b[i];
        let mut cnt = 0;
        while i < n && b[i] == ch {
            cnt += 1;
            i += 1;
        }
        groups.push(cnt);
    }
    let mut ans = 0;
    for k in 1..groups.len() {
        ans += groups[k - 1].min(groups[k]);
    }
    ans
}
fn main() {
    assert_eq!(count_binary_substrings("00110011".into()), 6);
    assert_eq!(count_binary_substrings("10101".into()), 4);
    println!("PASS");
}
''',
"lua": '''local function count_binary_substrings(s)
    local groups = {}
    local i, n = 1, #s
    while i <= n do
        local ch = s:sub(i, i)
        local cnt = 0
        while i <= n and s:sub(i, i) == ch do
            cnt = cnt + 1
            i = i + 1
        end
        groups[#groups + 1] = cnt
    end
    local ans = 0
    for k = 2, #groups do
        ans = ans + math.min(groups[k - 1], groups[k])
    end
    return ans
end
assert(count_binary_substrings("00110011") == 6)
assert(count_binary_substrings("10101") == 4)
print("PASS")
''',
"c": '''#include <stdio.h>
#include <string.h>
static int count_binary_substrings(const char *s) {
    int groups[8192], gn = 0;
    int n = (int)strlen(s);
    int i = 0;
    while (i < n) {
        char ch = s[i];
        int cnt = 0;
        while (i < n && s[i] == ch) { cnt++; i++; }
        groups[gn++] = cnt;
    }
    int ans = 0;
    for (int k = 1; k < gn; k++) {
        int m = groups[k - 1] < groups[k] ? groups[k - 1] : groups[k];
        ans += m;
    }
    return ans;
}
int main(void) {
    if (count_binary_substrings("00110011") != 6) { printf("FAIL 1\\n"); return 1; }
    if (count_binary_substrings("10101") != 4) { printf("FAIL 2\\n"); return 1; }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''#include <algorithm>
#include <cassert>
#include <iostream>
#include <string>
#include <vector>
static int countBinarySubstrings(const std::string &s) {
    std::vector<int> groups;
    int n = static_cast<int>(s.size());
    int i = 0;
    while (i < n) {
        char ch = s[i];
        int cnt = 0;
        while (i < n && s[i] == ch) { ++cnt; ++i; }
        groups.push_back(cnt);
    }
    int ans = 0;
    for (size_t k = 1; k < groups.size(); ++k) {
        ans += std::min(groups[k - 1], groups[k]);
    }
    return ans;
}
int main() {
    assert(countBinarySubstrings("00110011") == 6);
    assert(countBinarySubstrings("10101") == 4);
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''count_binary_substrings <- function(s) {
  chars <- strsplit(s, "")[[1]]
  groups <- integer(0)
  i <- 1; n <- length(chars)
  while (i <= n) {
    ch <- chars[i]
    cnt <- 0
    while (i <= n && chars[i] == ch) { cnt <- cnt + 1; i <- i + 1 }
    groups <- c(groups, cnt)
  }
  ans <- 0
  for (k in 2:length(groups)) {
    ans <- ans + min(groups[k - 1], groups[k])
  }
  ans
}
stopifnot(count_binary_substrings("00110011") == 6)
stopifnot(count_binary_substrings("10101") == 4)
cat("PASS\\n")
''',
"zig": '''const std = @import("std");
fn countBinarySubstrings(s: []const u8) i32 {
    var groups: [8192]i32 = undefined;
    var gn: usize = 0;
    var i: usize = 0;
    const n = s.len;
    while (i < n) {
        const ch = s[i];
        var cnt: i32 = 0;
        while (i < n and s[i] == ch) {
            cnt += 1;
            i += 1;
        }
        groups[gn] = cnt;
        gn += 1;
    }
    var ans: i32 = 0;
    for (1..gn) |k| {
        ans += @min(groups[k - 1], groups[k]);
    }
    return ans;
}
pub fn main() !void {
    if (countBinarySubstrings("00110011") != 6) return error.TestFailed;
    if (countBinarySubstrings("10101") != 4) return error.TestFailed;
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''int countBinarySubstrings(String s) {
  final groups = <int>[];
  var i = 0;
  final n = s.length;
  while (i < n) {
    final ch = s[i];
    var cnt = 0;
    while (i < n && s[i] == ch) {
      cnt++;
      i++;
    }
    groups.add(cnt);
  }
  var ans = 0;
  for (var k = 1; k < groups.length; k++) {
    ans += groups[k - 1] < groups[k] ? groups[k - 1] : groups[k];
  }
  return ans;
}
void main() {
  if (countBinarySubstrings('00110011') != 6) throw StateError('c1');
  if (countBinarySubstrings('10101') != 4) throw StateError('c2');
  print('PASS');
}
''',
}

PROBS = [
    ("lc_557_反转字符串中的单词_iii", A557, "LeetCode 557. 反转字符串中的单词III"),
    ("lc_696_计数二进制子串", A696, "LeetCode 696. 计数二进制子串"),
]
count = 0
for prob, algo, title in PROBS:
    bid = B[prob.split("_")[1]]
    ts_dir = f"/Users/Wang/Code/github/web-x-blog/work/target/21.dsa/ts/string/{prob}"
    sols = sorted(f[:-3] for f in os.listdir(ts_dir) if f.startswith("solution_") and f.endswith(".ts"))
    for lang in EXT:
        ext = EXT[lang]
        for sol in sols:
            n = sol.replace("solution_", "").split("_")[0]
            head = head_comment(lang, bid, f"{title} — {LANGNAME[lang]} 版（方案{n}）")
            emit(lang, f"string/{prob}/{sol}.{ext}", head + "\n" + algo[lang])
            count += 1
print(f"emitted {count} files")
