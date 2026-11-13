#!/usr/bin/env python3
# gen_string1.py — string 第一批：58/67/125/165/2042/415/43/482/791/8 × 7语言
# 模板约定：所有 { } 双写（{{ }}），emit 时反转义
import sys, os; sys.path.insert(0, "/Users/Wang/Code/github/web-x-blog/work/blog/courses/21.dsa/_tools")
from langlib import emit, head_comment, EXT

B = {"58": "130668538", "67": "130724108", "125": "130778527", "165": "135004886", "2042": "138481618", "415": "130736023", "43": "130701795", "482": "138290964", "791": "136838836", "8": "135129920"}
LANGNAME = {"rust": "Rust", "lua": "Lua", "c": "C", "cpp": "C++", "r": "R", "zig": "Zig", "dart": "Dart"}

A58 = {
"rust": '''fn length_of_last_word(s: String) -> i32 {
    let t = s.trim();
    if t.is_empty() { return 0; }
    t.split_whitespace().last().map(|w| w.len() as i32).unwrap_or(0)
}
fn main() {
    assert_eq!(length_of_last_word("Hello World".to_string()), 5);
    assert_eq!(length_of_last_word(" ".to_string()), 0);
    assert_eq!(length_of_last_word("a".to_string()), 1);
    assert_eq!(length_of_last_word(" fly me to the moon ".to_string()), 4);
    println!("PASS");
}
''',
"lua": '''local function length_of_last_word(s)
    local t = s:gsub("^%s+", ""):gsub("%s+$", "")
    if t == "" then return 0 end
    local last = t:match("([%w]+)%s*$")
    return last and #last or 0
end
assert(length_of_last_word("Hello World") == 5)
assert(length_of_last_word(" ") == 0)
assert(length_of_last_word("a") == 1)
assert(length_of_last_word(" fly me to the moon ") == 4)
print("PASS")
''',
"c": '''#include <stdio.h>
#include <string.h>
static int length_of_last_word(const char *s) {
    int n = (int)strlen(s);
    int end = n - 1;
    while (end >= 0 && s[end] == ' ') end--;
    if (end < 0) return 0;
    int start = end;
    while (start >= 0 && s[start] != ' ') start--;
    return end - start;
}
int main(void) {
    if (length_of_last_word("Hello World") != 5) { printf("FAIL 1\\n"); return 1; }
    if (length_of_last_word(" ") != 0) { printf("FAIL 2\\n"); return 1; }
    if (length_of_last_word("a") != 1) { printf("FAIL 3\\n"); return 1; }
    if (length_of_last_word(" fly me to the moon ") != 4) { printf("FAIL 4\\n"); return 1; }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''#include <cassert>
#include <iostream>
#include <string>
static int lengthOfLastWord(std::string s) {
    int end = static_cast<int>(s.size()) - 1;
    while (end >= 0 && s[end] == ' ') --end;
    if (end < 0) return 0;
    int start = end;
    while (start >= 0 && s[start] != ' ') --start;
    return end - start;
}
int main() {
    assert(lengthOfLastWord("Hello World") == 5);
    assert(lengthOfLastWord(" ") == 0);
    assert(lengthOfLastWord("a") == 1);
    assert(lengthOfLastWord(" fly me to the moon ") == 4);
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''length_of_last_word <- function(s) {
  t <- trimws(s)
  if (nchar(t) == 0) return(0L)
  words <- strsplit(t, " ")[[1]]
  nchar(words[length(words)])
}
stopifnot(length_of_last_word("Hello World") == 5)
stopifnot(length_of_last_word(" ") == 0)
stopifnot(length_of_last_word("a") == 1)
stopifnot(length_of_last_word(" fly me to the moon ") == 4)
cat("PASS\\n")
''',
"zig": '''const std = @import("std");
fn lengthOfLastWord(s: []const u8) i32 {
    var end: isize = @intCast(s.len - 1);
    while (end >= 0 and s[@intCast(end)] == ' ') end -= 1;
    if (end < 0) return 0;
    var start = end;
    while (start >= 0 and s[@intCast(start)] != ' ') start -= 1;
    return @intCast(end - start);
}
pub fn main() !void {
    if (lengthOfLastWord("Hello World") != 5) return error.TestFailed;
    if (lengthOfLastWord(" ") != 0) return error.TestFailed;
    if (lengthOfLastWord("a") != 1) return error.TestFailed;
    if (lengthOfLastWord(" fly me to the moon ") != 4) return error.TestFailed;
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''int lengthOfLastWord(String s) {
  var end = s.length - 1;
  while (end >= 0 && s[end] == ' ') end--;
  if (end < 0) return 0;
  var start = end;
  while (start >= 0 && s[start] != ' ') start--;
  return end - start;
}
void main() {
  if (lengthOfLastWord('Hello World') != 5) throw StateError('c1');
  if (lengthOfLastWord(' ') != 0) throw StateError('c2');
  if (lengthOfLastWord('a') != 1) throw StateError('c3');
  if (lengthOfLastWord(' fly me to the moon ') != 4) throw StateError('c4');
  print('PASS');
}
''',
}

A67 = {
"rust": '''fn add_binary(a: String, b: String) -> String {
    let (a, b) = (a.as_bytes(), b.as_bytes());
    let (mut i, mut j) = (a.len() as i32 - 1, b.len() as i32 - 1);
    let mut carry = 0u8;
    let mut out: Vec<u8> = Vec::new();
    while i >= 0 || j >= 0 || carry > 0 {
        let mut total = carry;
        if i >= 0 { total += a[i as usize] - b'0'; i -= 1; }
        if j >= 0 { total += b[j as usize] - b'0'; j -= 1; }
        out.push(b'0' + total % 2);
        carry = total / 2;
    }
    out.reverse();
    String::from_utf8(out).unwrap()
}
fn main() {
    assert_eq!(add_binary("11".to_string(), "1".to_string()), "100");
    assert_eq!(add_binary("1010".to_string(), "1011".to_string()), "10101");
    println!("PASS");
}
''',
"lua": '''local function add_binary(a, b)
    local i, j = #a, #b
    local carry = 0
    local out = {}
    while i >= 1 or j >= 1 or carry > 0 do
        local total = carry
        if i >= 1 then total = total + (a:byte(i) - 48); i = i - 1 end
        if j >= 1 then total = total + (b:byte(j) - 48); j = j - 1 end
        out[#out + 1] = tostring(total % 2)
        carry = math.floor(total / 2)
    end
    return table.concat(out):reverse()
end
assert(add_binary("11", "1") == "100")
assert(add_binary("1010", "1011") == "10101")
print("PASS")
''',
"c": '''#include <stdio.h>
#include <string.h>
static void add_binary(const char *a, const char *b, char out[]) {
    int i = (int)strlen(a) - 1, j = (int)strlen(b) - 1, carry = 0, n = 0;
    while (i >= 0 || j >= 0 || carry) {
        int total = carry;
        if (i >= 0) { total += a[i] - '0'; i--; }
        if (j >= 0) { total += b[j] - '0'; j--; }
        out[n++] = '0' + total % 2;
        carry = total / 2;
    }
    if (n == 0) out[n++] = '0';
    out[n] = '\\0';
    for (int l = 0, r = n - 1; l < r; l++, r--) { char t = out[l]; out[l] = out[r]; out[r] = t; }
}
int main(void) {
    char out[8192];
    add_binary("11", "1", out);
    if (strcmp(out, "100") != 0) { printf("FAIL 1\\n"); return 1; }
    add_binary("1010", "1011", out);
    if (strcmp(out, "10101") != 0) { printf("FAIL 2\\n"); return 1; }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''#include <algorithm>
#include <cassert>
#include <iostream>
#include <string>
static std::string addBinary(const std::string &a, const std::string &b) {
    int i = static_cast<int>(a.size()) - 1, j = static_cast<int>(b.size()) - 1, carry = 0;
    std::string out;
    while (i >= 0 || j >= 0 || carry) {
        int total = carry;
        if (i >= 0) total += a[i--] - '0';
        if (j >= 0) total += b[j--] - '0';
        out.push_back('0' + total % 2);
        carry = total / 2;
    }
    if (out.empty()) out = "0";
    std::reverse(out.begin(), out.end());
    return out;
}
int main() {
    assert(addBinary("11", "1") == "100");
    assert(addBinary("1010", "1011") == "10101");
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''add_binary <- function(a, b) {
  ca <- strsplit(a, "")[[1]]; cb <- strsplit(b, "")[[1]]
  i <- length(ca); j <- length(cb); carry <- 0
  out <- character(0)
  while (i >= 1 || j >= 1 || carry > 0) {
    total <- carry
    if (i >= 1) { total <- total + as.integer(ca[i]); i <- i - 1 }
    if (j >= 1) { total <- total + as.integer(cb[j]); j <- j - 1 }
    out <- c(out, as.character(total %% 2))
    carry <- total %/% 2
  }
  if (length(out) == 0) out <- "0"
  paste(rev(out), collapse = "")
}
stopifnot(add_binary("11", "1") == "100")
stopifnot(add_binary("1010", "1011") == "10101")
cat("PASS\\n")
''',
"zig": '''const std = @import("std");
fn addBinary(a: []const u8, b: []const u8, out: *std.ArrayList(u8)) void {
    var i: isize = @as(isize, @intCast(a.len)) - 1;
    var j: isize = @as(isize, @intCast(b.len)) - 1;
    var carry: u8 = 0;
    while (i >= 0 or j >= 0 or carry > 0) {
        var total: u8 = carry;
        if (i >= 0) { total += a[@intCast(i)] - '0'; i -= 1; }
        if (j >= 0) { total += b[@intCast(j)] - '0'; j -= 1; }
        out.append('0' + total % 2) catch unreachable;
        carry = total / 2;
    }
    if (out.items.len == 0) out.append('0') catch unreachable;
    std.mem.reverse(u8, out.items);
}
pub fn main() !void {
    var out = std.ArrayList(u8).init(std.heap.page_allocator);
    defer out.deinit();
    addBinary("11", "1", &out);
    if (!std.mem.eql(u8, out.items, "100")) return error.TestFailed;
    out.clearRetainingCapacity();
    addBinary("1010", "1011", &out);
    if (!std.mem.eql(u8, out.items, "10101")) return error.TestFailed;
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''String addBinary(String a, String b) {
  var i = a.length - 1, j = b.length - 1, carry = 0;
  final out = <String>[];
  while (i >= 0 || j >= 0 || carry > 0) {
    var total = carry;
    if (i >= 0) {
      total += a.codeUnitAt(i--) - 0x30;
    }
    if (j >= 0) {
      total += b.codeUnitAt(j--) - 0x30;
    }
    out.add((total % 2).toString());
    carry = total ~/ 2;
  }
  if (out.isEmpty) out.add('0');
  return out.reversed.join();
}
void main() {
  if (addBinary('11', '1') != '100') throw StateError('c1');
  if (addBinary('1010', '1011') != '10101') throw StateError('c2');
  print('PASS');
}
''',
}

A125 = {
"rust": '''fn is_palindrome(s: String) -> bool {
    let f: Vec<char> = s.chars().filter(|c| c.is_ascii_alphanumeric()).map(|c| c.to_ascii_lowercase()).collect();
    let (mut i, mut j) = (0usize, f.len());
    if j == 0 { return true; }
    j -= 1;
    while i < j {
        if f[i] != f[j] { return false; }
        i += 1;
        if j == 0 { break; }
        j -= 1;
    }
    true
}
fn main() {
    assert!(is_palindrome("A man, a plan, a canal: Panama".to_string()));
    assert!(!is_palindrome("race a car".to_string()));
    assert!(is_palindrome(" ".to_string()));
    println!("PASS");
}
''',
"lua": '''local function is_palindrome(s)
    local f = {}
    for c in s:gmatch("[%a%d]") do
        f[#f + 1] = c:lower()
    end
    local i, j = 1, #f
    while i < j do
        if f[i] ~= f[j] then return false end
        i = i + 1
        j = j - 1
    end
    return true
end
assert(is_palindrome("A man, a plan, a canal: Panama") == true)
assert(is_palindrome("race a car") == false)
assert(is_palindrome(" ") == true)
print("PASS")
''',
"c": '''#include <stdio.h>
#include <string.h>
#include <ctype.h>
static int is_palindrome(const char *s) {
    char f[8192];
    int n = 0;
    for (const char *p = s; *p; p++) {
        if (isalnum((unsigned char)*p)) f[n++] = tolower((unsigned char)*p);
    }
    int i = 0, j = n - 1;
    while (i < j) {
        if (f[i] != f[j]) return 0;
        i++; j--;
    }
    return 1;
}
int main(void) {
    if (!is_palindrome("A man, a plan, a canal: Panama")) { printf("FAIL 1\\n"); return 1; }
    if (is_palindrome("race a car")) { printf("FAIL 2\\n"); return 1; }
    if (!is_palindrome(" ")) { printf("FAIL 3\\n"); return 1; }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''#include <cctype>
#include <cassert>
#include <iostream>
#include <string>
static bool isPalindrome(const std::string &s) {
    std::string f;
    for (char c : s) {
        if (std::isalnum(static_cast<unsigned char>(c))) f.push_back(static_cast<char>(std::tolower(static_cast<unsigned char>(c))));
    }
    size_t i = 0, j = f.size();
    if (j == 0) return true;
    --j;
    while (i < j) {
        if (f[i] != f[j]) return false;
        ++i; --j;
    }
    return true;
}
int main() {
    assert(isPalindrome("A man, a plan, a canal: Panama"));
    assert(!isPalindrome("race a car"));
    assert(isPalindrome(" "));
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''is_palindrome <- function(s) {
  f <- tolower(gsub("[^[:alnum:]]", "", s))
  chars <- strsplit(f, "")[[1]]
  identical(chars, rev(chars))
}
stopifnot(is_palindrome("A man, a plan, a canal: Panama"))
stopifnot(!is_palindrome("race a car"))
stopifnot(is_palindrome(" "))
cat("PASS\\n")
''',
"zig": '''const std = @import("std");
fn isPalindrome(s: []const u8) bool {
    var fbuf: [8192]u8 = undefined;
    var n: usize = 0;
    for (s) |c| {
        if (std.ascii.isAlphanumeric(c)) {
            fbuf[n] = std.ascii.toLower(c);
            n += 1;
        }
    }
    if (n == 0) return true;
    var i: usize = 0;
    var j: usize = n - 1;
    while (i < j) {
        if (fbuf[i] != fbuf[j]) return false;
        i += 1;
        j -= 1;
    }
    return true;
}
pub fn main() !void {
    if (!isPalindrome("A man, a plan, a canal: Panama")) return error.TestFailed;
    if (isPalindrome("race a car")) return error.TestFailed;
    if (!isPalindrome(" ")) return error.TestFailed;
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''bool isPalindrome(String s) {
  final f = s.replaceAll(RegExp('[^a-zA-Z0-9]'), '').toLowerCase();
  var i = 0, j = f.length - 1;
  while (i < j) {
    if (f[i] != f[j]) return false;
    i++;
    j--;
  }
  return true;
}
void main() {
  if (!isPalindrome('A man, a plan, a canal: Panama')) throw StateError('c1');
  if (isPalindrome('race a car')) throw StateError('c2');
  if (!isPalindrome(' ')) throw StateError('c3');
  print('PASS');
}
''',
}

A165 = {
"rust": '''fn compare_version(v1: String, v2: String) -> i32 {
    let p1: Vec<i64> = v1.split('.').map(|x| x.parse::<i64>().unwrap_or(0)).collect();
    let p2: Vec<i64> = v2.split('.').map(|x| x.parse::<i64>().unwrap_or(0)).collect();
    let n = p1.len().max(p2.len());
    for i in 0..n {
        let a = if i < p1.len() { p1[i] } else { 0 };
        let b = if i < p2.len() { p2[i] } else { 0 };
        if a < b { return -1; }
        if a > b { return 1; }
    }
    0
}
fn main() {
    assert_eq!(compare_version("1.01".into(), "1.001".into()), 0);
    assert_eq!(compare_version("1.0".into(), "1.0.0".into()), 0);
    assert_eq!(compare_version("0.1".into(), "1.1".into()), -1);
    println!("PASS");
}
''',
"lua": '''local function compare_version(v1, v2)
    local p1, p2 = {}, {}
    v1:gsub("([^.]+)", function(x) p1[#p1 + 1] = tonumber(x) end)
    v2:gsub("([^.]+)", function(x) p2[#p2 + 1] = tonumber(x) end)
    local n = math.max(#p1, #p2)
    for i = 1, n do
        local a = p1[i] or 0
        local b = p2[i] or 0
        if a < b then return -1 end
        if a > b then return 1 end
    end
    return 0
end
assert(compare_version("1.01", "1.001") == 0)
assert(compare_version("1.0", "1.0.0") == 0)
assert(compare_version("0.1", "1.1") == -1)
print("PASS")
''',
"c": '''#include <stdio.h>
#include <string.h>
#include <stdlib.h>
static long parse_seg(const char *s, int len) {
    char buf[32];
    if (len >= 32) len = 31;
    strncpy(buf, s, len);
    buf[len] = '\\0';
    return atol(buf);
}
static int compare_version(const char *v1, const char *v2) {
    const char *p1 = v1, *p2 = v2;
    while (*p1 || *p2) {
        long a = 0, b = 0;
        if (*p1) {
            const char *d1 = strchr(p1, '.');
            int len = d1 ? (int)(d1 - p1) : (int)strlen(p1);
            a = parse_seg(p1, len);
            p1 = d1 ? d1 + 1 : p1 + strlen(p1);
        }
        if (*p2) {
            const char *d2 = strchr(p2, '.');
            int len = d2 ? (int)(d2 - p2) : (int)strlen(p2);
            b = parse_seg(p2, len);
            p2 = d2 ? d2 + 1 : p2 + strlen(p2);
        }
        if (a < b) return -1;
        if (a > b) return 1;
    }
    return 0;
}
int main(void) {
    if (compare_version("1.01", "1.001") != 0) { printf("FAIL 1\\n"); return 1; }
    if (compare_version("1.0", "1.0.0") != 0) { printf("FAIL 2\\n"); return 1; }
    if (compare_version("0.1", "1.1") != -1) { printf("FAIL 3\\n"); return 1; }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''#include <cstdlib>
#include <cassert>
#include <iostream>
#include <string>
#include <vector>
static int compareVersion(const std::string &version1, const std::string &version2) {
    std::vector<long long> p1, p2;
    size_t start = 0;
    for (size_t i = 0; i <= version1.size(); ++i) {
        if (i == version1.size() || version1[i] == '.') {
            p1.push_back(std::atoll(version1.substr(start, i - start).c_str()));
            start = i + 1;
        }
    }
    start = 0;
    for (size_t i = 0; i <= version2.size(); ++i) {
        if (i == version2.size() || version2[i] == '.') {
            p2.push_back(std::atoll(version2.substr(start, i - start).c_str()));
            start = i + 1;
        }
    }
    size_t n = std::max(p1.size(), p2.size());
    for (size_t i = 0; i < n; ++i) {
        long long a = i < p1.size() ? p1[i] : 0;
        long long b = i < p2.size() ? p2[i] : 0;
        if (a < b) return -1;
        if (a > b) return 1;
    }
    return 0;
}
int main() {
    assert(compareVersion("1.01", "1.001") == 0);
    assert(compareVersion("1.0", "1.0.0") == 0);
    assert(compareVersion("0.1", "1.1") == -1);
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''compare_version <- function(v1, v2) {
  p1 <- as.numeric(strsplit(v1, "\\\\.")[[1]])
  p2 <- as.numeric(strsplit(v2, "\\\\.")[[1]])
  n <- max(length(p1), length(p2))
  for (i in seq_len(n)) {
    a <- if (i <= length(p1)) p1[i] else 0
    b <- if (i <= length(p2)) p2[i] else 0
    if (a < b) return(-1)
    if (a > b) return(1)
  }
  0
}
stopifnot(compare_version("1.01", "1.001") == 0)
stopifnot(compare_version("1.0", "1.0.0") == 0)
stopifnot(compare_version("0.1", "1.1") == -1)
cat("PASS\\n")
''',
"zig": '''const std = @import("std");
fn segVal(s: []const u8) i64 {
    if (s.len == 0) return 0;
    return std.fmt.parseInt(i64, s, 10) catch 0;
}
fn compareVersion(v1: []const u8, v2: []const u8) i32 {
    var it1 = std.mem.splitScalar(u8, v1, '.');
    var it2 = std.mem.splitScalar(u8, v2, '.');
    while (true) {
        const s1 = it1.next();
        const s2 = it2.next();
        if (s1 == null and s2 == null) break;
        const a = if (s1) |x| segVal(x) else 0;
        const b = if (s2) |x| segVal(x) else 0;
        if (a < b) return -1;
        if (a > b) return 1;
    }
    return 0;
}
pub fn main() !void {
    if (compareVersion("1.01", "1.001") != 0) return error.TestFailed;
    if (compareVersion("1.0", "1.0.0") != 0) return error.TestFailed;
    if (compareVersion("0.1", "1.1") != -1) return error.TestFailed;
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''int compareVersion(String v1, String v2) {
  final p1 = v1.split('.').map(int.parse).toList();
  final p2 = v2.split('.').map(int.parse).toList();
  final n = p1.length > p2.length ? p1.length : p2.length;
  for (var i = 0; i < n; i++) {
    final a = i < p1.length ? p1[i] : 0;
    final b = i < p2.length ? p2[i] : 0;
    if (a < b) return -1;
    if (a > b) return 1;
  }
  return 0;
}
void main() {
  if (compareVersion('1.01', '1.001') != 0) throw StateError('c1');
  if (compareVersion('1.0', '1.0.0') != 0) throw StateError('c2');
  if (compareVersion('0.1', '1.1') != -1) throw StateError('c3');
  print('PASS');
}
''',
}

A2042 = {
"rust": '''fn are_numbers_ascending(s: String) -> bool {
    let mut prev: i64 = 0;
    for tok in s.split_whitespace() {
        if tok.chars().next().map(|c| c.is_ascii_digit()).unwrap_or(false) {
            let num: i64 = tok.parse().unwrap_or(0);
            if num <= prev { return false; }
            prev = num;
        }
    }
    true
}
fn main() {
    assert!(are_numbers_ascending("1 box has 3 blue 4 red 6 green and 12 yellow marbles".to_string()));
    assert!(!are_numbers_ascending("hello world 5 x 5".to_string()));
    println!("PASS");
}
''',
"lua": '''local function are_numbers_ascending(s)
    local prev = -1
    for tok in s:gmatch("%S+") do
        local c = tok:sub(1, 1)
        if c >= "0" and c <= "9" then
            local num = tonumber(tok)
            if num <= prev then return false end
            prev = num
        end
    end
    return true
end
assert(are_numbers_ascending("1 box has 3 blue 4 red 6 green and 12 yellow marbles") == true)
assert(are_numbers_ascending("hello world 5 x 5") == false)
print("PASS")
''',
"c": '''#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>
static int are_numbers_ascending(const char *s) {
    long prev = -1;
    char tok[256];
    int ti = 0;
    const char *p = s;
    while (1) {
        if (*p == ' ' || *p == '\\0') {
            if (ti > 0) {
                tok[ti] = '\\0';
                if (isdigit((unsigned char)tok[0])) {
                    long num = atol(tok);
                    if (num <= prev) return 0;
                    prev = num;
                }
                ti = 0;
            }
            if (*p == '\\0') break;
        } else if (ti < 255) {
            tok[ti++] = *p;
        }
        p++;
    }
    return 1;
}
int main(void) {
    if (!are_numbers_ascending("1 box has 3 blue 4 red 6 green and 12 yellow marbles")) { printf("FAIL 1\\n"); return 1; }
    if (are_numbers_ascending("hello world 5 x 5")) { printf("FAIL 2\\n"); return 1; }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''#include <cctype>
#include <cassert>
#include <iostream>
#include <sstream>
#include <string>
static bool areNumbersAscending(const std::string &s) {
    long long prev = -1;
    std::istringstream iss(s);
    std::string tok;
    while (iss >> tok) {
        if (std::isdigit(static_cast<unsigned char>(tok[0]))) {
            long long num = std::stoll(tok);
            if (num <= prev) return false;
            prev = num;
        }
    }
    return true;
}
int main() {
    assert(areNumbersAscending("1 box has 3 blue 4 red 6 green and 12 yellow marbles"));
    assert(!areNumbersAscending("hello world 5 x 5"));
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''are_numbers_ascending <- function(s) {
  prev <- -1
  for (tok in strsplit(trimws(s), " ")[[1]]) {
    if (nchar(tok) > 0 && grepl("^[0-9]", tok)) {
      num <- as.numeric(tok)
      if (num <= prev) return(FALSE)
      prev <- num
    }
  }
  TRUE
}
stopifnot(are_numbers_ascending("1 box has 3 blue 4 red 6 green and 12 yellow marbles"))
stopifnot(!are_numbers_ascending("hello world 5 x 5"))
cat("PASS\\n")
''',
"zig": '''const std = @import("std");
fn areNumbersAscending(s: []const u8) bool {
    var it = std.mem.tokenizeScalar(u8, s, ' ');
    var prev: i64 = -1;
    while (it.next()) |tok| {
        if (tok.len > 0 and std.ascii.isDigit(tok[0])) {
            const num = std.fmt.parseInt(i64, tok, 10) catch 0;
            if (num <= prev) return false;
            prev = num;
        }
    }
    return true;
}
pub fn main() !void {
    if (!areNumbersAscending("1 box has 3 blue 4 red 6 green and 12 yellow marbles")) return error.TestFailed;
    if (areNumbersAscending("hello world 5 x 5")) return error.TestFailed;
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''bool areNumbersAscending(String s) {
  var prev = -1;
  for (final tok in s.split(' ')) {
    if (tok.isNotEmpty && tok[0].codeUnitAt(0) >= 0x30 && tok[0].codeUnitAt(0) <= 0x39) {
      final num = int.parse(tok);
      if (num <= prev) return false;
      prev = num;
    }
  }
  return true;
}
void main() {
  if (!areNumbersAscending('1 box has 3 blue 4 red 6 green and 12 yellow marbles')) throw StateError('c1');
  if (areNumbersAscending('hello world 5 x 5')) throw StateError('c2');
  print('PASS');
}
''',
}

A415 = {
"rust": '''fn add_strings(num1: String, num2: String) -> String {
    let (a, b) = (num1.as_bytes(), num2.as_bytes());
    let (mut i, mut j) = (a.len() as i32 - 1, b.len() as i32 - 1);
    let mut carry = 0u8;
    let mut out: Vec<u8> = Vec::new();
    while i >= 0 || j >= 0 || carry > 0 {
        let mut total = carry;
        if i >= 0 { total += a[i as usize] - b'0'; i -= 1; }
        if j >= 0 { total += b[j as usize] - b'0'; j -= 1; }
        out.push(b'0' + total % 10);
        carry = total / 10;
    }
    out.reverse();
    String::from_utf8(out).unwrap()
}
fn main() {
    assert_eq!(add_strings("11".into(), "123".into()), "134");
    assert_eq!(add_strings("456".into(), "77".into()), "533");
    assert_eq!(add_strings("0".into(), "0".into()), "0");
    println!("PASS");
}
''',
"lua": '''local function add_strings(num1, num2)
    local i, j = #num1, #num2
    local carry = 0
    local out = {}
    while i >= 1 or j >= 1 or carry > 0 do
        local total = carry
        if i >= 1 then total = total + (num1:byte(i) - 48); i = i - 1 end
        if j >= 1 then total = total + (num2:byte(j) - 48); j = j - 1 end
        out[#out + 1] = tostring(total % 10)
        carry = math.floor(total / 10)
    end
    if #out == 0 then return "0" end
    return table.concat(out):reverse()
end
assert(add_strings("11", "123") == "134")
assert(add_strings("456", "77") == "533")
assert(add_strings("0", "0") == "0")
print("PASS")
''',
"c": '''#include <stdio.h>
#include <string.h>
static void add_strings(const char *a, const char *b, char out[]) {
    int i = (int)strlen(a) - 1, j = (int)strlen(b) - 1, carry = 0, n = 0;
    while (i >= 0 || j >= 0 || carry) {
        int total = carry;
        if (i >= 0) { total += a[i] - '0'; i--; }
        if (j >= 0) { total += b[j] - '0'; j--; }
        out[n++] = '0' + total % 10;
        carry = total / 10;
    }
    if (n == 0) out[n++] = '0';
    out[n] = '\\0';
    for (int l = 0, r = n - 1; l < r; l++, r--) { char t = out[l]; out[l] = out[r]; out[r] = t; }
}
int main(void) {
    char out[9000];
    add_strings("11", "123", out);
    if (strcmp(out, "134") != 0) { printf("FAIL 1\\n"); return 1; }
    add_strings("456", "77", out);
    if (strcmp(out, "533") != 0) { printf("FAIL 2\\n"); return 1; }
    add_strings("0", "0", out);
    if (strcmp(out, "0") != 0) { printf("FAIL 3\\n"); return 1; }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''#include <algorithm>
#include <cassert>
#include <iostream>
#include <string>
static std::string addStrings(const std::string &a, const std::string &b) {
    int i = static_cast<int>(a.size()) - 1, j = static_cast<int>(b.size()) - 1, carry = 0;
    std::string out;
    while (i >= 0 || j >= 0 || carry) {
        int total = carry;
        if (i >= 0) total += a[i--] - '0';
        if (j >= 0) total += b[j--] - '0';
        out.push_back('0' + total % 10);
        carry = total / 10;
    }
    if (out.empty()) out = "0";
    std::reverse(out.begin(), out.end());
    return out;
}
int main() {
    assert(addStrings("11", "123") == "134");
    assert(addStrings("456", "77") == "533");
    assert(addStrings("0", "0") == "0");
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''add_strings <- function(num1, num2) {
  ca <- strsplit(num1, "")[[1]]; cb <- strsplit(num2, "")[[1]]
  i <- length(ca); j <- length(cb); carry <- 0
  out <- character(0)
  while (i >= 1 || j >= 1 || carry > 0) {
    total <- carry
    if (i >= 1) { total <- total + as.integer(ca[i]); i <- i - 1 }
    if (j >= 1) { total <- total + as.integer(cb[j]); j <- j - 1 }
    out <- c(out, as.character(total %% 10))
    carry <- total %/% 10
  }
  if (length(out) == 0) out <- "0"
  paste(rev(out), collapse = "")
}
stopifnot(add_strings("11", "123") == "134")
stopifnot(add_strings("456", "77") == "533")
stopifnot(add_strings("0", "0") == "0")
cat("PASS\\n")
''',
"zig": '''const std = @import("std");
fn addStrings(a: []const u8, b: []const u8, out: *std.ArrayList(u8)) void {
    var i: isize = @as(isize, @intCast(a.len)) - 1;
    var j: isize = @as(isize, @intCast(b.len)) - 1;
    var carry: u8 = 0;
    while (i >= 0 or j >= 0 or carry > 0) {
        var total: u16 = carry;
        if (i >= 0) { total += a[@intCast(i)] - '0'; i -= 1; }
        if (j >= 0) { total += b[@intCast(j)] - '0'; j -= 1; }
        out.append('0' + @as(u8, @intCast(total % 10))) catch unreachable;
        carry = @intCast(total / 10);
    }
    if (out.items.len == 0) out.append('0') catch unreachable;
    std.mem.reverse(u8, out.items);
}
pub fn main() !void {
    var out = std.ArrayList(u8).init(std.heap.page_allocator);
    defer out.deinit();
    addStrings("11", "123", &out);
    if (!std.mem.eql(u8, out.items, "134")) return error.TestFailed;
    out.clearRetainingCapacity();
    addStrings("456", "77", &out);
    if (!std.mem.eql(u8, out.items, "533")) return error.TestFailed;
    out.clearRetainingCapacity();
    addStrings("0", "0", &out);
    if (!std.mem.eql(u8, out.items, "0")) return error.TestFailed;
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''String addStrings(String a, String b) {
  var i = a.length - 1, j = b.length - 1, carry = 0;
  final out = <String>[];
  while (i >= 0 || j >= 0 || carry > 0) {
    var total = carry;
    if (i >= 0) {
      total += a.codeUnitAt(i--) - 0x30;
    }
    if (j >= 0) {
      total += b.codeUnitAt(j--) - 0x30;
    }
    out.add((total % 10).toString());
    carry = total ~/ 10;
  }
  if (out.isEmpty) out.add('0');
  return out.reversed.join();
}
void main() {
  if (addStrings('11', '123') != '134') throw StateError('c1');
  if (addStrings('456', '77') != '533') throw StateError('c2');
  if (addStrings('0', '0') != '0') throw StateError('c3');
  print('PASS');
}
''',
}

A43 = {
"rust": '''fn multiply(num1: String, num2: String) -> String {
    if num1 == "0" || num2 == "0" { return "0".to_string(); }
    let (a, b) = (num1.as_bytes(), num2.as_bytes());
    let (m, n) = (a.len(), b.len());
    let mut result = vec![0u8; m + n];
    for i in (0..m).rev() {
        for j in (0..n).rev() {
            let mul = (a[i] - b'0') * (b[j] - b'0');
            let (p1, p2) = (i + j, i + j + 1);
            let total = mul + result[p2];
            result[p2] = total % 10;
            result[p1] += total / 10;
        }
    }
    let mut out = String::new();
    let mut started = false;
    for &d in &result {
        if d != 0 || started { out.push((b'0' + d) as char); started = true; }
    }
    if out.is_empty() { out.push('0'); }
    out
}
fn main() {
    assert_eq!(multiply("2".into(), "3".into()), "6");
    assert_eq!(multiply("123".into(), "456".into()), "56088");
    println!("PASS");
}
''',
"lua": '''local function multiply(num1, num2)
    if num1 == "0" or num2 == "0" then return "0" end
    local m, n = #num1, #num2
    local result = {}
    for i = 1, m + n do result[i] = 0 end
    for i = m, 1, -1 do
        for j = n, 1, -1 do
            local mul = (num1:byte(i) - 48) * (num2:byte(j) - 48)
            local p1, p2 = i + j - 1, i + j
            local total = mul + result[p2]
            result[p2] = total % 10
            result[p1] = result[p1] + math.floor(total / 10)
        end
    end
    local out = {}
    local started = false
    for _, d in ipairs(result) do
        if d ~= 0 or started then
            out[#out + 1] = tostring(d)
            started = true
        end
    end
    if #out == 0 then return "0" end
    return table.concat(out)
end
assert(multiply("2", "3") == "6")
assert(multiply("123", "456") == "56088")
print("PASS")
''',
"c": '''#include <stdio.h>
#include <string.h>
static void multiply(const char *num1, const char *num2, char out[]) {
    if (strcmp(num1, "0") == 0 || strcmp(num2, "0") == 0) { strcpy(out, "0"); return; }
    int m = (int)strlen(num1), n = (int)strlen(num2);
    int result[512] = {0};
    for (int i = m - 1; i >= 0; i--) {
        for (int j = n - 1; j >= 0; j--) {
            int mul = (num1[i] - '0') * (num2[j] - '0');
            int p1 = i + j, p2 = i + j + 1;
            int total = mul + result[p2];
            result[p2] = total % 10;
            result[p1] += total / 10;
        }
    }
    int pos = 0, started = 0;
    for (int i = 0; i < m + n; i++) {
        if (result[i] != 0 || started) { out[pos++] = '0' + result[i]; started = 1; }
    }
    if (pos == 0) out[pos++] = '0';
    out[pos] = '\\0';
}
int main(void) {
    char out[1024];
    multiply("2", "3", out);
    if (strcmp(out, "6") != 0) { printf("FAIL 1\\n"); return 1; }
    multiply("123", "456", out);
    if (strcmp(out, "56088") != 0) { printf("FAIL 2\\n"); return 1; }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''#include <cassert>
#include <iostream>
#include <string>
#include <vector>
static std::string multiply(const std::string &num1, const std::string &num2) {
    if (num1 == "0" || num2 == "0") return "0";
    int m = static_cast<int>(num1.size()), n = static_cast<int>(num2.size());
    std::vector<int> result(m + n, 0);
    for (int i = m - 1; i >= 0; --i) {
        for (int j = n - 1; j >= 0; --j) {
            int mul = (num1[i] - '0') * (num2[j] - '0');
            int p1 = i + j, p2 = i + j + 1;
            int total = mul + result[p2];
            result[p2] = total % 10;
            result[p1] += total / 10;
        }
    }
    std::string out;
    bool started = false;
    for (int d : result) {
        if (d != 0 || started) { out.push_back('0' + d); started = true; }
    }
    if (out.empty()) out = "0";
    return out;
}
int main() {
    assert(multiply("2", "3") == "6");
    assert(multiply("123", "456") == "56088");
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''multiply_str <- function(num1, num2) {
  if (num1 == "0" || num2 == "0") return("0")
  ca <- strsplit(num1, "")[[1]]; cb <- strsplit(num2, "")[[1]]
  m <- length(ca); n <- length(cb)
  result <- rep(0L, m + n)
  for (i in m:1) {
    for (j in n:1) {
      mul <- (as.integer(ca[i])) * (as.integer(cb[j]))
      p1 <- i + j - 1; p2 <- i + j
      total <- mul + result[p2]
      result[p2] <- total %% 10
      result[p1] <- result[p1] + total %/% 10
    }
  }
  digits <- result[result != 0 | cumsum(result != 0) > 0 | seq_along(result) == length(result)]
  # 简化：拼接后去前导零
  s <- paste(result, collapse = "")
  s <- sub("^0+", "", s)
  if (nchar(s) == 0) "0" else s
}
stopifnot(multiply_str("2", "3") == "6")
stopifnot(multiply_str("123", "456") == "56088")
cat("PASS\\n")
''',
"zig": '''const std = @import("std");
fn multiply(num1: []const u8, num2: []const u8, out: *std.ArrayList(u8)) void {
    if (std.mem.eql(u8, num1, "0") or std.mem.eql(u8, num2, "0")) {
        out.append('0') catch unreachable;
        return;
    }
    const m = num1.len;
    const n = num2.len;
    var result = [_]i32{0} ** 512;
    var i: usize = m;
    while (i > 0) {
        i -= 1;
        var j: usize = n;
        while (j > 0) {
            j -= 1;
            const mul = @as(i32, num1[i] - '0') * @as(i32, num2[j] - '0');
            const p1 = i + j;
            const p2 = i + j + 1;
            const total = mul + result[p2];
            result[p2] = @mod(total, 10);
            result[p1] += @divTrunc(total, 10);
        }
    }
    var started = false;
    for (result[0 .. m + n]) |d| {
        if (d != 0 or started) {
            out.append('0' + @as(u8, @intCast(d))) catch unreachable;
            started = true;
        }
    }
    if (out.items.len == 0) out.append('0') catch unreachable;
}
pub fn main() !void {
    var out = std.ArrayList(u8).init(std.heap.page_allocator);
    defer out.deinit();
    multiply("2", "3", &out);
    if (!std.mem.eql(u8, out.items, "6")) return error.TestFailed;
    out.clearRetainingCapacity();
    multiply("123", "456", &out);
    if (!std.mem.eql(u8, out.items, "56088")) return error.TestFailed;
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''String multiply(String num1, String num2) {
  if (num1 == '0' || num2 == '0') return '0';
  final m = num1.length, n = num2.length;
  final result = List<int>.filled(m + n, 0);
  for (var i = m - 1; i >= 0; i--) {
    for (var j = n - 1; j >= 0; j--) {
      final mul = (num1.codeUnitAt(i) - 0x30) * (num2.codeUnitAt(j) - 0x30);
      final p1 = i + j, p2 = i + j + 1;
      final total = mul + result[p2];
      result[p2] = total % 10;
      result[p1] += total ~/ 10;
    }
  }
  final sb = StringBuffer();
  var started = false;
  for (final d in result) {
    if (d != 0 || started) {
      sb.write(d);
      started = true;
    }
  }
  final s = sb.toString();
  return s.isEmpty ? '0' : s;
}
void main() {
  if (multiply('2', '3') != '6') throw StateError('c1');
  if (multiply('123', '456') != '56088') throw StateError('c2');
  print('PASS');
}
''',
}

A482 = {
"rust": '''fn license_key_formatting(s: String, k: i32) -> String {
    let cleaned: Vec<u8> = s.bytes().filter(|&c| c != b'-').map(|c| c.to_ascii_uppercase()).collect();
    let mut out: Vec<u8> = Vec::new();
    let n = cleaned.len();
    let k = k as usize;
    if n == 0 { return String::new(); }
    let first = n % k;
    let mut idx = 0usize;
    if first > 0 {
        for _ in 0..first { out.push(cleaned[idx]); idx += 1; }
        if idx < n { out.push(b'-'); }
    }
    while idx < n {
        for _ in 0..k { out.push(cleaned[idx]); idx += 1; }
        if idx < n { out.push(b'-'); }
    }
    String::from_utf8(out).unwrap()
}
fn main() {
    assert_eq!(license_key_formatting("5F3Z-2e-9-w".into(), 4), "5F3Z-2E9W");
    assert_eq!(license_key_formatting("2-5g-3-J".into(), 2), "2-5G-3J");
    println!("PASS");
}
''',
"lua": '''local function license_key_formatting(s, k)
    local cleaned = {}
    s:gsub("[^-]", function(c) cleaned[#cleaned + 1] = c:upper() end)
    local n = #cleaned
    if n == 0 then return "" end
    local out = {}
    local first = n % k
    local idx = 1
    if first > 0 then
        for _ = 1, first do
            out[#out + 1] = cleaned[idx]
            idx = idx + 1
        end
        if idx <= n then out[#out + 1] = "-" end
    end
    while idx <= n do
        for _ = 1, k do
            out[#out + 1] = cleaned[idx]
            idx = idx + 1
        end
        if idx <= n then out[#out + 1] = "-" end
    end
    return table.concat(out)
end
assert(license_key_formatting("5F3Z-2e-9-w", 4) == "5F3Z-2E9W")
assert(license_key_formatting("2-5g-3-J", 2) == "2-5G-3J")
print("PASS")
''',
"c": '''#include <stdio.h>
#include <string.h>
#include <ctype.h>
static void license_key_formatting(const char *s, int k, char out[]) {
    char cleaned[8192];
    int n = 0;
    for (const char *p = s; *p; p++) {
        if (*p != '-') cleaned[n++] = (char)toupper((unsigned char)*p);
    }
    int pos = 0;
    if (n == 0) { out[0] = '\\0'; return; }
    int first = n % k;
    int idx = 0;
    if (first > 0) {
        for (int i = 0; i < first; i++) out[pos++] = cleaned[idx++];
        if (idx < n) out[pos++] = '-';
    }
    while (idx < n) {
        for (int i = 0; i < k; i++) out[pos++] = cleaned[idx++];
        if (idx < n) out[pos++] = '-';
    }
    out[pos] = '\\0';
}
int main(void) {
    char out[8192];
    license_key_formatting("5F3Z-2e-9-w", 4, out);
    if (strcmp(out, "5F3Z-2E9W") != 0) { printf("FAIL 1 %s\\n", out); return 1; }
    license_key_formatting("2-5g-3-J", 2, out);
    if (strcmp(out, "2-5G-3J") != 0) { printf("FAIL 2 %s\\n", out); return 1; }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''#include <algorithm>
#include <cctype>
#include <cassert>
#include <iostream>
#include <string>
static std::string licenseKeyFormatting(const std::string &s, int k) {
    std::string cleaned;
    for (char c : s) {
        if (c != '-') cleaned.push_back(static_cast<char>(std::toupper(static_cast<unsigned char>(c))));
    }
    int n = static_cast<int>(cleaned.size());
    if (n == 0) return "";
    std::string out;
    int first = n % k;
    int idx = 0;
    if (first > 0) {
        for (int i = 0; i < first; ++i) out.push_back(cleaned[idx++]);
        if (idx < n) out.push_back('-');
    }
    while (idx < n) {
        for (int i = 0; i < k; ++i) out.push_back(cleaned[idx++]);
        if (idx < n) out.push_back('-');
    }
    return out;
}
int main() {
    assert(licenseKeyFormatting("5F3Z-2e-9-w", 4) == "5F3Z-2E9W");
    assert(licenseKeyFormatting("2-5g-3-J", 2) == "2-5G-3J");
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''license_key_formatting <- function(s, k) {
  cleaned <- toupper(gsub("-", "", s))
  chars <- strsplit(cleaned, "")[[1]]
  n <- length(chars)
  if (n == 0) return("")
  first <- n %% k
  out <- character(0)
  idx <- 1
  if (first > 0) {
    out <- c(out, chars[idx:(idx + first - 1)])
    idx <- idx + first
    if (idx <= n) out <- c(out, "-")
  }
  while (idx <= n) {
    out <- c(out, chars[idx:(idx + k - 1)])
    idx <- idx + k
    if (idx <= n) out <- c(out, "-")
  }
  paste(out, collapse = "")
}
stopifnot(license_key_formatting("5F3Z-2e-9-w", 4) == "5F3Z-2E9W")
stopifnot(license_key_formatting("2-5g-3-J", 2) == "2-5G-3J")
cat("PASS\\n")
''',
"zig": '''const std = @import("std");
fn licenseKeyFormatting(s: []const u8, k: usize, out: *std.ArrayList(u8)) void {
    var cleaned: [8192]u8 = undefined;
    var n: usize = 0;
    for (s) |c| {
        if (c != '-') {
            cleaned[n] = std.ascii.toUpper(c);
            n += 1;
        }
    }
    if (n == 0) return;
    const first = n % k;
    var idx: usize = 0;
    if (first > 0) {
        for (0..first) |_| {
            out.append(cleaned[idx]) catch unreachable;
            idx += 1;
        }
        if (idx < n) out.append('-') catch unreachable;
    }
    while (idx < n) {
        for (0..k) |_| {
            out.append(cleaned[idx]) catch unreachable;
            idx += 1;
        }
        if (idx < n) out.append('-') catch unreachable;
    }
}
pub fn main() !void {
    var out = std.ArrayList(u8).init(std.heap.page_allocator);
    defer out.deinit();
    licenseKeyFormatting("5F3Z-2e-9-w", 4, &out);
    if (!std.mem.eql(u8, out.items, "5F3Z-2E9W")) return error.TestFailed;
    out.clearRetainingCapacity();
    licenseKeyFormatting("2-5g-3-J", 2, &out);
    if (!std.mem.eql(u8, out.items, "2-5G-3J")) return error.TestFailed;
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''String licenseKeyFormatting(String s, int k) {
  final cleaned = s.replaceAll('-', '').toUpperCase();
  final n = cleaned.length;
  if (n == 0) return '';
  final out = <String>[];
  final first = n % k;
  var idx = 0;
  if (first > 0) {
    for (var i = 0; i < first; i++) {
      out.add(cleaned[idx++]);
    }
    if (idx < n) out.add('-');
  }
  while (idx < n) {
    for (var i = 0; i < k; i++) {
      out.add(cleaned[idx++]);
    }
    if (idx < n) out.add('-');
  }
  return out.join();
}
void main() {
  if (licenseKeyFormatting('5F3Z-2e-9-w', 4) != '5F3Z-2E9W') throw StateError('c1');
  if (licenseKeyFormatting('2-5g-3-J', 2) != '2-5G-3J') throw StateError('c2');
  print('PASS');
}
''',
}

A791 = {
"rust": '''fn custom_sort_string(order: String, s: String) -> String {
    let mut count = [0usize; 26];
    for b in s.bytes() { count[(b - b'a') as usize] += 1; }
    let mut out = String::new();
    for b in order.bytes() {
        let idx = (b - b'a') as usize;
        for _ in 0..count[idx] { out.push(b as char); }
        count[idx] = 0;
    }
    for (i, &c) in count.iter().enumerate() {
        for _ in 0..c { out.push((b'a' + i as u8) as char); }
    }
    out
}
fn main() {
    assert_eq!(custom_sort_string("cba".into(), "abcd".into()), "cbad");
    assert_eq!(custom_sort_string("bcafg".into(), "abcd".into()), "bcad");
    println!("PASS");
}
''',
"lua": '''local function custom_sort_string(order, s)
    local count = {}
    for c in s:gmatch("[%a]") do
        count[c] = (count[c] or 0) + 1
    end
    local out = {}
    for c in order:gmatch("[%a]") do
        if count[c] then
            for _ = 1, count[c] do out[#out + 1] = c end
            count[c] = nil
        end
    end
    local rest = {}
    for c, n in pairs(count) do
        for _ = 1, n do rest[#rest + 1] = c end
    end
    table.sort(rest)
    for _, c in ipairs(rest) do out[#out + 1] = c end
    return table.concat(out)
end
assert(custom_sort_string("cba", "abcd") == "cbad")
assert(custom_sort_string("bcafg", "abcd") == "bcad")
print("PASS")
''',
"c": '''#include <stdio.h>
#include <string.h>
static void custom_sort_string(const char *order, const char *s, char out[]) {
    int count[26] = {0};
    for (const char *p = s; *p; p++) count[*p - 'a']++;
    int pos = 0;
    for (const char *p = order; *p; p++) {
        int idx = *p - 'a';
        for (int i = 0; i < count[idx]; i++) out[pos++] = *p;
        count[idx] = 0;
    }
    for (int i = 0; i < 26; i++) {
        for (int j = 0; j < count[i]; j++) out[pos++] = 'a' + i;
    }
    out[pos] = '\\0';
}
int main(void) {
    char out[8192];
    custom_sort_string("cba", "abcd", out);
    if (strcmp(out, "cbad") != 0) { printf("FAIL 1 %s\\n", out); return 1; }
    custom_sort_string("bcafg", "abcd", out);
    if (strcmp(out, "bcad") != 0) { printf("FAIL 2 %s\\n", out); return 1; }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''#include <cassert>
#include <iostream>
#include <string>
static std::string customSortString(const std::string &order, const std::string &s) {
    int count[26] = {0};
    for (char c : s) ++count[c - 'a'];
    std::string out;
    for (char c : order) {
        out.append(static_cast<size_t>(count[c - 'a']), c);
        count[c - 'a'] = 0;
    }
    for (int i = 0; i < 26; ++i) {
        out.append(static_cast<size_t>(count[i]), static_cast<char>('a' + i));
    }
    return out;
}
int main() {
    assert(customSortString("cba", "abcd") == "cbad");
    assert(customSortString("bcafg", "abcd") == "bcad");
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''custom_sort_string <- function(order, s) {
  count <- table(strsplit(s, "")[[1]])
  out <- character(0)
  for (c in strsplit(order, "")[[1]]) {
    if (!is.na(count[c]) && count[[c]] > 0) {
      out <- c(out, rep(c, count[[c]]))
      count[[c]] <- 0
    }
  }
  rest <- character(0)
  for (c in names(count)) {
    if (count[[c]] > 0) rest <- c(rest, rep(c, count[[c]]))
  }
  paste(c(out, rest), collapse = "")
}
stopifnot(custom_sort_string("cba", "abcd") == "cbad")
stopifnot(custom_sort_string("bcafg", "abcd") == "bcad")
cat("PASS\\n")
''',
"zig": '''const std = @import("std");
fn customSortString(order: []const u8, s: []const u8, out: *std.ArrayList(u8)) void {
    var count = [_]usize{0} ** 26;
    for (s) |c| count[c - 'a'] += 1;
    for (order) |c| {
        const idx = c - 'a';
        for (0..count[idx]) |_| out.append(c) catch unreachable;
        count[idx] = 0;
    }
    for (count, 0..) |cnt, i| {
        for (0..cnt) |_| out.append('a' + @as(u8, @intCast(i))) catch unreachable;
    }
}
pub fn main() !void {
    var out = std.ArrayList(u8).init(std.heap.page_allocator);
    defer out.deinit();
    customSortString("cba", "abcd", &out);
    if (!std.mem.eql(u8, out.items, "cbad")) return error.TestFailed;
    out.clearRetainingCapacity();
    customSortString("bcafg", "abcd", &out);
    if (!std.mem.eql(u8, out.items, "bcad")) return error.TestFailed;
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''String customSortString(String order, String s) {
  final count = <String, int>{};
  for (final c in s.split('')) {
    count[c] = (count[c] ?? 0) + 1;
  }
  final out = <String>[];
  for (final c in order.split('')) {
    final n = count[c] ?? 0;
    for (var i = 0; i < n; i++) {
      out.add(c);
    }
    count[c] = 0;
  }
  final rest = <String>[];
  for (final e in count.entries) {
    for (var i = 0; i < e.value; i++) {
      rest.add(e.key);
    }
  }
  rest.sort();
  return (out..addAll(rest)).join();
}
void main() {
  if (customSortString('cba', 'abcd') != 'cbad') throw StateError('c1');
  if (customSortString('bcafg', 'abcd') != 'bcad') throw StateError('c2');
  print('PASS');
}
''',
}

A8 = {
"rust": '''fn my_atoi(s: String) -> i32 {
    let b = s.as_bytes();
    let mut i = 0usize;
    let n = b.len();
    while i < n && (b[i] == b' ') { i += 1; }
    let mut sign = 1i64;
    if i < n && (b[i] == b'+' || b[i] == b'-') {
        if b[i] == b'-' { sign = -1; }
        i += 1;
    }
    let mut ans: i64 = 0;
    while i < n && b[i].is_ascii_digit() {
        ans = ans * 10 + (b[i] - b'0') as i64;
        if ans > i32::MAX as i64 + 1 { ans = i32::MAX as i64 + 1; }
        i += 1;
    }
    ans *= sign;
    if ans > i32::MAX as i64 { return i32::MAX; }
    if ans < i32::MIN as i64 { return i32::MIN; }
    ans as i32
}
fn main() {
    assert_eq!(my_atoi("42".to_string()), 42);
    assert_eq!(my_atoi(" -42".to_string()), -42);
    assert_eq!(my_atoi("4193 with words".to_string()), 4193);
    assert_eq!(my_atoi("-91283472332".to_string()), -2147483648);
    assert_eq!(my_atoi("words and 987".to_string()), 0);
    println!("PASS");
}
''',
"lua": '''local function my_atoi(s)
    local i = 1
    local n = #s
    while i <= n and s:sub(i, i) == " " do i = i + 1 end
    local sign = 1
    if i <= n and (s:sub(i, i) == "+" or s:sub(i, i) == "-") then
        if s:sub(i, i) == "-" then sign = -1 end
        i = i + 1
    end
    local ans = 0
    while i <= n and s:sub(i, i):match("%d") do
        ans = ans * 10 + tonumber(s:sub(i, i))
        if ans > 2147483648 then ans = 2147483648 end
        i = i + 1
    end
    ans = ans * sign
    if ans > 2147483647 then return 2147483647 end
    if ans < -2147483648 then return -2147483648 end
    return ans
end
assert(my_atoi("42") == 42)
assert(my_atoi(" -42") == -42)
assert(my_atoi("4193 with words") == 4193)
assert(my_atoi("-91283472332") == -2147483648)
assert(my_atoi("words and 987") == 0)
print("PASS")
''',
"c": '''#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <limits.h>
static int my_atoi(const char *s) {
    int i = 0, n = (int)strlen(s);
    while (i < n && s[i] == ' ') i++;
    int sign = 1;
    if (i < n && (s[i] == '+' || s[i] == '-')) {
        if (s[i] == '-') sign = -1;
        i++;
    }
    long ans = 0;
    while (i < n && isdigit((unsigned char)s[i])) {
        ans = ans * 10 + (s[i] - '0');
        if (ans > 2147483648L) ans = 2147483648L;
        i++;
    }
    ans *= sign;
    if (ans > INT_MAX) return INT_MAX;
    if (ans < INT_MIN) return INT_MIN;
    return (int)ans;
}
int main(void) {
    if (my_atoi("42") != 42) { printf("FAIL 1\\n"); return 1; }
    if (my_atoi(" -42") != -42) { printf("FAIL 2\\n"); return 1; }
    if (my_atoi("4193 with words") != 4193) { printf("FAIL 3\\n"); return 1; }
    if (my_atoi("-91283472332") != INT_MIN) { printf("FAIL 4\\n"); return 1; }
    if (my_atoi("words and 987") != 0) { printf("FAIL 5\\n"); return 1; }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''#include <cctype>
#include <climits>
#include <cassert>
#include <iostream>
#include <string>
static int myAtoi(const std::string &s) {
    size_t i = 0, n = s.size();
    while (i < n && s[i] == ' ') ++i;
    long long sign = 1;
    if (i < n && (s[i] == '+' || s[i] == '-')) {
        if (s[i] == '-') sign = -1;
        ++i;
    }
    long long ans = 0;
    while (i < n && std::isdigit(static_cast<unsigned char>(s[i]))) {
        ans = ans * 10 + (s[i] - '0');
        if (ans > 2147483648LL) ans = 2147483648LL;
        ++i;
    }
    ans *= sign;
    if (ans > INT_MAX) return INT_MAX;
    if (ans < INT_MIN) return INT_MIN;
    return static_cast<int>(ans);
}
int main() {
    assert(myAtoi("42") == 42);
    assert(myAtoi(" -42") == -42);
    assert(myAtoi("4193 with words") == 4193);
    assert(myAtoi("-91283472332") == INT_MIN);
    assert(myAtoi("words and 987") == 0);
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''my_atoi <- function(s) {
  i <- 1; n <- nchar(s)
  chars <- strsplit(s, "")[[1]]
  while (i <= n && chars[i] == " ") i <- i + 1L
  sign <- 1
  if (i <= n && (chars[i] == "+" || chars[i] == "-")) {
    if (chars[i] == "-") sign <- -1
    i <- i + 1L
  }
  ans <- 0
  while (i <= n && grepl("[0-9]", chars[i])) {
    ans <- ans * 10 + as.integer(chars[i])
    if (ans > 2147483648) ans <- 2147483648
    i <- i + 1L
  }
  ans <- ans * sign
  if (ans >= 2147483648) return(2147483647L)
  if (ans <= -2147483648) return(-2147483648L)
  as.integer(ans)
}
stopifnot(my_atoi("42") == 42)
stopifnot(my_atoi(" -42") == -42)
stopifnot(my_atoi("4193 with words") == 4193)
stopifnot(my_atoi("-91283472332") == -2147483648)
stopifnot(my_atoi("words and 987") == 0)
cat("PASS\\n")
''',
"zig": '''const std = @import("std");
fn myAtoi(s: []const u8) i32 {
    var i: usize = 0;
    const n = s.len;
    while (i < n and s[i] == ' ') i += 1;
    var sign: i64 = 1;
    if (i < n and (s[i] == '+' or s[i] == '-')) {
        if (s[i] == '-') sign = -1;
        i += 1;
    }
    var ans: i64 = 0;
    while (i < n and std.ascii.isDigit(s[i])) {
        ans = ans * 10 + @as(i64, s[i] - '0');
        if (ans > 2147483648) ans = 2147483648;
        i += 1;
    }
    ans *= sign;
    if (ans > 2147483647) return 2147483647;
    if (ans < -2147483648) return -2147483648;
    return @intCast(ans);
}
pub fn main() !void {
    if (myAtoi("42") != 42) return error.TestFailed;
    if (myAtoi(" -42") != -42) return error.TestFailed;
    if (myAtoi("4193 with words") != 4193) return error.TestFailed;
    if (myAtoi("-91283472332") != -2147483648) return error.TestFailed;
    if (myAtoi("words and 987") != 0) return error.TestFailed;
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''int myAtoi(String s) {
  var i = 0;
  final n = s.length;
  while (i < n && s[i] == ' ') i++;
  var sign = 1;
  if (i < n && (s[i] == '+' || s[i] == '-')) {
    if (s[i] == '-') sign = -1;
    i++;
  }
  var ans = 0;
  while (i < n && s.codeUnitAt(i) >= 0x30 && s.codeUnitAt(i) <= 0x39) {
    ans = ans * 10 + (s.codeUnitAt(i) - 0x30);
    if (ans > 2147483648) ans = 2147483648;
    i++;
  }
  ans *= sign;
  if (ans > 2147483647) return 2147483647;
  if (ans < -2147483648) return -2147483648;
  return ans;
}
void main() {
  if (myAtoi('42') != 42) throw StateError('c1');
  if (myAtoi(' -42') != -42) throw StateError('c2');
  if (myAtoi('4193 with words') != 4193) throw StateError('c3');
  if (myAtoi('-91283472332') != -2147483648) throw StateError('c4');
  if (myAtoi('words and 987') != 0) throw StateError('c5');
  print('PASS');
}
''',
}

PROBS = [
    ("lc_58_最后一个单词的长度", A58, "LeetCode 58. 最后一个单词的长度"),
    ("lc_67_二进制求和", A67, "LeetCode 67. 二进制求和"),
    ("lc_125_验证回文串", A125, "LeetCode 125. 验证回文串"),
    ("lc_165_比较版本号", A165, "LeetCode 165. 比较版本号"),
    ("lc_2042_检查句子中的数字是否递增", A2042, "LeetCode 2042. 检查句子中的数字是否递增"),
    ("lc_415_字符串相加", A415, "LeetCode 415. 字符串相加"),
    ("lc_43_字符串相乘", A43, "LeetCode 43. 字符串相乘"),
    ("lc_482_密钥格式化", A482, "LeetCode 482. 密钥格式化"),
    ("lc_791_自定义字符串排序", A791, "LeetCode 791. 自定义字符串排序"),
    ("lc_8_字符串转换整数_(atoi)", A8, "LeetCode 8. 字符串转换整数 (atoi)"),
]
count = 0
for prob, algo, title in PROBS:
    bid = B[prob.split("_")[1]]
    ts_dir = f"/Users/Wang/Code/github/web-x-blog/work/blog/courses/21.dsa/ts/string/{prob}"
    sols = sorted(f[:-3] for f in os.listdir(ts_dir) if f.startswith("solution_") and f.endswith(".ts"))
    for lang in EXT:
        ext = EXT[lang]
        for sol in sols:
            n = sol.replace("solution_", "").split("_")[0]
            head = head_comment(lang, bid, f"{title} — {LANGNAME[lang]} 版（方案{n}）")
            emit(lang, f"string/{prob}/{sol}.{ext}", head + "\n" + algo[lang])
            count += 1
print(f"emitted {count} files")
