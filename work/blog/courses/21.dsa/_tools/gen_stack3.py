#!/usr/bin/env python3
# gen_stack3.py — stack 收官：1472/641 × 7语言
import sys, os; sys.path.insert(0, "/Users/Wang/Code/github/web-x-blog/work/blog/courses/21.dsa/_tools")
from langlib import emit, head_comment, EXT

B = {"1472":"145338856","641":"145361774"}
LANGNAME = {"rust": "Rust", "lua": "Lua", "c": "C", "cpp": "C++", "r": "R", "zig": "Zig", "dart": "Dart"}

T = {}
T["1472"] = {
"rust":'''struct BrowserHistory { history: Vec<String>, cur: usize }
impl BrowserHistory {
    fn new(homepage: &str) -> Self { BrowserHistory { history: vec![homepage.to_string()], cur: 0 } }
    fn visit(&mut self, url: &str) {
        self.history.truncate(self.cur + 1);
        self.history.push(url.to_string());
        self.cur = self.history.len() - 1;
    }
    fn back(&mut self, steps: i32) -> String {
        self.cur = self.cur.saturating_sub(steps as usize);
        self.history[self.cur].clone()
    }
    fn forward(&mut self, steps: i32) -> String {
        self.cur = (self.cur + steps as usize).min(self.history.len() - 1);
        self.history[self.cur].clone()
    }
}
fn main() {
    let mut b = BrowserHistory::new("leetcode.com");
    b.visit("google.com");
    b.visit("facebook.com");
    b.visit("youtube.com");
    assert_eq!(b.back(1), "facebook.com".to_string());
    assert_eq!(b.back(1), "google.com".to_string());
    assert_eq!(b.forward(1), "facebook.com".to_string());
    b.visit("linkedin.com");
    assert_eq!(b.forward(2), "linkedin.com".to_string());
    assert_eq!(b.back(2), "google.com".to_string());
    assert_eq!(b.back(7), "leetcode.com".to_string());
    println!("PASS"); }''',
"lua":'''local BrowserHistory = {}
BrowserHistory.__index = BrowserHistory
function BrowserHistory.new(homepage)
    return setmetatable({history = {homepage}, cur = 1}, BrowserHistory)
end
function BrowserHistory:visit(url)
    for i = #self.history, self.cur + 1, -1 do self.history[i] = nil end
    self.history[#self.history + 1] = url
    self.cur = #self.history
end
function BrowserHistory:back(steps)
    self.cur = math.max(1, self.cur - steps)
    return self.history[self.cur]
end
function BrowserHistory:forward(steps)
    self.cur = math.min(#self.history, self.cur + steps)
    return self.history[self.cur]
end
local b = BrowserHistory.new("leetcode.com")
b:visit("google.com"); b:visit("facebook.com"); b:visit("youtube.com")
assert(b:back(1) == "facebook.com")
assert(b:back(1) == "google.com")
assert(b:forward(1) == "facebook.com")
b:visit("linkedin.com")
assert(b:forward(2) == "linkedin.com")
assert(b:back(2) == "google.com")
assert(b:back(7) == "leetcode.com")
print("PASS")''',
"c":'''#include <stdio.h>
#include <string.h>
typedef struct { char history[64][64]; int n; int cur; } BrowserHistory;
static void bh_init(BrowserHistory *b, const char *homepage) {
    strcpy(b->history[0], homepage);
    b->n = 1;
    b->cur = 0;
}
static void bh_visit(BrowserHistory *b, const char *url) {
    b->n = b->cur + 1;
    strcpy(b->history[b->n++], url);
    b->cur = b->n - 1;
}
static const char *bh_back(BrowserHistory *b, int steps) {
    b->cur = b->cur - steps < 0 ? 0 : b->cur - steps;
    return b->history[b->cur];
}
static const char *bh_forward(BrowserHistory *b, int steps) {
    b->cur = b->cur + steps > b->n - 1 ? b->n - 1 : b->cur + steps;
    return b->history[b->cur];
}
int main(void) {
    BrowserHistory b;
    bh_init(&b, "leetcode.com");
    bh_visit(&b, "google.com");
    bh_visit(&b, "facebook.com");
    bh_visit(&b, "youtube.com");
    if (strcmp(bh_back(&b, 1), "facebook.com") != 0) { printf("FAIL 1\\n"); return 1; }
    if (strcmp(bh_back(&b, 1), "google.com") != 0) { printf("FAIL 2\\n"); return 1; }
    if (strcmp(bh_forward(&b, 1), "facebook.com") != 0) { printf("FAIL 3\\n"); return 1; }
    bh_visit(&b, "linkedin.com");
    if (strcmp(bh_forward(&b, 2), "linkedin.com") != 0) { printf("FAIL 4\\n"); return 1; }
    if (strcmp(bh_back(&b, 2), "google.com") != 0) { printf("FAIL 5\\n"); return 1; }
    if (strcmp(bh_back(&b, 7), "leetcode.com") != 0) { printf("FAIL 6\\n"); return 1; }
    printf("PASS\\n"); return 0; }''',
"cpp":'''#include <cassert>
#include <iostream>
#include <string>
#include <vector>
struct BrowserHistory {
    std::vector<std::string> history;
    size_t cur;
    explicit BrowserHistory(const std::string &homepage) : history{homepage}, cur(0) {}
    void visit(const std::string &url) {
        history.resize(cur + 1);
        history.push_back(url);
        cur = history.size() - 1;
    }
    std::string back(int steps) {
        cur = cur >= static_cast<size_t>(steps) ? cur - steps : 0;
        return history[cur];
    }
    std::string forward(int steps) {
        cur = std::min(cur + static_cast<size_t>(steps), history.size() - 1);
        return history[cur];
    }
};
int main() {
    BrowserHistory b("leetcode.com");
    b.visit("google.com");
    b.visit("facebook.com");
    b.visit("youtube.com");
    assert(b.back(1) == "facebook.com");
    assert(b.back(1) == "google.com");
    assert(b.forward(1) == "facebook.com");
    b.visit("linkedin.com");
    assert(b.forward(2) == "linkedin.com");
    assert(b.back(2) == "google.com");
    assert(b.back(7) == "leetcode.com");
    std::cout << "PASS" << std::endl; }''',
"r":'''BrowserHistory <- function(homepage) {
  e <- new.env(parent = emptyenv())
  e$history <- homepage; e$cur <- 1L
  e$visit <- function(url) {
    e$history <<- c(e$history[seq_len(e$cur)], url)
    e$cur <<- length(e$history)
  }
  e$back <- function(steps) {
    e$cur <<- max(1L, e$cur - steps)
    e$history[e$cur]
  }
  e$forward <- function(steps) {
    e$cur <<- min(length(e$history), e$cur + steps)
    e$history[e$cur]
  }
  e
}
b <- BrowserHistory("leetcode.com")
b$visit("google.com"); b$visit("facebook.com"); b$visit("youtube.com")
stopifnot(b$back(1) == "facebook.com")
stopifnot(b$back(1) == "google.com")
stopifnot(b$forward(1) == "facebook.com")
b$visit("linkedin.com")
stopifnot(b$forward(2) == "linkedin.com")
stopifnot(b$back(2) == "google.com")
stopifnot(b$back(7) == "leetcode.com")
cat("PASS\\n")''',
"zig":'''const std = @import("std");
const BrowserHistory = struct {
    history: [64][64]u8,
    lens: [64]usize,
    n: usize,
    cur: usize,
    fn init(homepage: []const u8) BrowserHistory {
        var b = BrowserHistory{ .history = undefined, .lens = undefined, .n = 1, .cur = 0 };
        @memcpy(b.history[0][0..homepage.len], homepage);
        b.lens[0] = homepage.len;
        return b;
    }
    fn visit(self: *BrowserHistory, url: []const u8) void {
        self.n = self.cur + 1;
        @memcpy(self.history[self.n][0..url.len], url);
        self.lens[self.n] = url.len;
        self.n += 1;
        self.cur = self.n - 1;
    }
    fn back(self: *BrowserHistory, steps: usize) []const u8 {
        self.cur = if (self.cur >= steps) self.cur - steps else 0;
        return self.history[self.cur][0..self.lens[self.cur]];
    }
    fn forward(self: *BrowserHistory, steps: usize) []const u8 {
        self.cur = @min(self.cur + steps, self.n - 1);
        return self.history[self.cur][0..self.lens[self.cur]];
    }
};
pub fn main() !void {
    var b = BrowserHistory.init("leetcode.com");
    b.visit("google.com");
    b.visit("facebook.com");
    b.visit("youtube.com");
    if (!std.mem.eql(u8, b.back(1), "facebook.com")) return error.TestFailed;
    if (!std.mem.eql(u8, b.back(1), "google.com")) return error.TestFailed;
    if (!std.mem.eql(u8, b.forward(1), "facebook.com")) return error.TestFailed;
    b.visit("linkedin.com");
    if (!std.mem.eql(u8, b.forward(2), "linkedin.com")) return error.TestFailed;
    if (!std.mem.eql(u8, b.back(2), "google.com")) return error.TestFailed;
    if (!std.mem.eql(u8, b.back(7), "leetcode.com")) return error.TestFailed;
    std.debug.print("PASS\\n", .{}); }''',
"dart":'''class BrowserHistory {
  final List<String> history;
  int cur = 0;
  BrowserHistory(String homepage) : history = [homepage];
  void visit(String url) {
    history.removeRange(cur + 1, history.length);
    history.add(url);
    cur = history.length - 1;
  }
  String back(int steps) {
    cur = cur - steps < 0 ? 0 : cur - steps;
    return history[cur];
  }
  String forward(int steps) {
    cur = (cur + steps > history.length - 1) ? history.length - 1 : cur + steps;
    return history[cur];
  }
}
void main() {
  final b = BrowserHistory('leetcode.com');
  b.visit('google.com');
  b.visit('facebook.com');
  b.visit('youtube.com');
  if (b.back(1) != 'facebook.com') throw StateError('c1');
  if (b.back(1) != 'google.com') throw StateError('c2');
  if (b.forward(1) != 'facebook.com') throw StateError('c3');
  b.visit('linkedin.com');
  if (b.forward(2) != 'linkedin.com') throw StateError('c4');
  if (b.back(2) != 'google.com') throw StateError('c5');
  if (b.back(7) != 'leetcode.com') throw StateError('c6');
  print('PASS'); }''',
}

T["641"] = {
"rust":'''struct MyCircularDeque { data: Vec<i32>, head: usize, tail: usize, cap: usize, size: usize }
impl MyCircularDeque {
    fn new(k: i32) -> Self { MyCircularDeque { data: vec![0; k as usize + 1], head: 0, tail: 0, cap: k as usize + 1, size: 0 } }
    fn capacity(&self) -> usize { self.cap - 1 }
    fn insert_front(&mut self, v: i32) -> bool {
        if self.size == self.cap - 1 { return false; }
        self.head = (self.head + self.cap - 1) % self.cap;
        self.data[self.head] = v;
        self.size += 1;
        true
    }
    fn insert_last(&mut self, v: i32) -> bool {
        if self.size == self.cap - 1 { return false; }
        self.data[self.tail] = v;
        self.tail = (self.tail + 1) % self.cap;
        self.size += 1;
        true
    }
    fn delete_front(&mut self) -> bool {
        if self.size == 0 { return false; }
        self.head = (self.head + 1) % self.cap;
        self.size -= 1;
        true
    }
    fn delete_last(&mut self) -> bool {
        if self.size == 0 { return false; }
        self.tail = (self.tail + self.cap - 1) % self.cap;
        self.size -= 1;
        true
    }
    fn get_front(&self) -> i32 { if self.size == 0 { -1 } else { self.data[self.head] } }
    fn get_rear(&self) -> i32 { if self.size == 0 { -1 } else { self.data[(self.tail + self.cap - 1) % self.cap] } }
    fn is_empty(&self) -> bool { self.size == 0 }
    fn is_full(&self) -> bool { self.size == self.cap - 1 }
}
fn main() {
    let mut d = MyCircularDeque::new(3);
    assert!(d.insert_last(1));
    assert!(d.insert_last(2));
    assert!(d.insert_front(3));
    assert!(!d.insert_front(4));
    assert_eq!(d.get_rear(), 2);
    assert!(d.is_full());
    assert!(d.delete_last());
    assert!(d.insert_front(4));
    assert_eq!(d.get_front(), 4);
    println!("PASS"); }''',
"lua":'''local MyCircularDeque = {}
MyCircularDeque.__index = MyCircularDeque
function MyCircularDeque.new(k)
    return setmetatable({data = {}, head = 1, tail = 1, cap = k, size = 0}, MyCircularDeque)
end
function MyCircularDeque:insertFront(v)
    if self.size == self.cap then return false end
    self.head = (self.head - 2) % self.cap + 1
    self.data[self.head] = v
    self.size = self.size + 1
    return true
end
function MyCircularDeque:insertLast(v)
    if self.size == self.cap then return false end
    self.data[self.tail] = v
    self.tail = self.tail % self.cap + 1
    self.size = self.size + 1
    return true
end
function MyCircularDeque:deleteFront()
    if self.size == 0 then return false end
    self.head = self.head % self.cap + 1
    self.size = self.size - 1
    return true
end
function MyCircularDeque:deleteLast()
    if self.size == 0 then return false end
    self.tail = (self.tail - 2) % self.cap + 1
    self.size = self.size - 1
    return true
end
function MyCircularDeque:getFront() if self.size == 0 then return -1 end return self.data[self.head] end
function MyCircularDeque:getRear() if self.size == 0 then return -1 end return self.data[(self.tail - 2) % self.cap + 1] end
function MyCircularDeque:isEmpty() return self.size == 0 end
function MyCircularDeque:isFull() return self.size == self.cap end
local d = MyCircularDeque.new(3)
assert(d:insertLast(1) == true)
assert(d:insertLast(2) == true)
assert(d:insertFront(3) == true)
assert(d:insertFront(4) == false)
assert(d:getRear() == 2)
assert(d:isFull() == true)
assert(d:deleteLast() == true)
assert(d:insertFront(4) == true)
assert(d:getFront() == 4)
print("PASS")''',
"c":'''#include <stdio.h>
#include <stdlib.h>
typedef struct { int *data; int head, tail, cap, size; } MyCircularDeque;
static MyCircularDeque *cdq_new(int k) {
    MyCircularDeque *d = malloc(sizeof(MyCircularDeque));
    d->cap = k;
    d->data = malloc(sizeof(int) * k);
    d->head = 0; d->tail = 0; d->size = 0;
    return d;
}
static int cdq_insert_front(MyCircularDeque *d, int v) {
    if (d->size == d->cap) return 0;
    d->head = (d->head + d->cap - 1) % d->cap;
    d->data[d->head] = v;
    d->size++;
    return 1;
}
static int cdq_insert_last(MyCircularDeque *d, int v) {
    if (d->size == d->cap) return 0;
    d->data[d->tail] = v;
    d->tail = (d->tail + 1) % d->cap;
    d->size++;
    return 1;
}
static int cdq_delete_front(MyCircularDeque *d) {
    if (d->size == 0) return 0;
    d->head = (d->head + 1) % d->cap;
    d->size--;
    return 1;
}
static int cdq_delete_last(MyCircularDeque *d) {
    if (d->size == 0) return 0;
    d->tail = (d->tail + d->cap - 1) % d->cap;
    d->size--;
    return 1;
}
static int cdq_get_front(MyCircularDeque *d) { return d->size == 0 ? -1 : d->data[d->head]; }
static int cdq_get_rear(MyCircularDeque *d) { return d->size == 0 ? -1 : d->data[(d->tail + d->cap - 1) % d->cap]; }
static int cdq_is_empty(MyCircularDeque *d) { return d->size == 0; }
static int cdq_is_full(MyCircularDeque *d) { return d->size == d->cap; }
int main(void) {
    MyCircularDeque *d = cdq_new(3);
    if (!cdq_insert_last(d, 1)) { printf("FAIL 1\\n"); return 1; }
    if (!cdq_insert_last(d, 2)) { printf("FAIL 2\\n"); return 1; }
    if (!cdq_insert_front(d, 3)) { printf("FAIL 3\\n"); return 1; }
    if (cdq_insert_front(d, 4)) { printf("FAIL 4\\n"); return 1; }
    if (cdq_get_rear(d) != 2) { printf("FAIL 5\\n"); return 1; }
    if (!cdq_is_full(d)) { printf("FAIL 6\\n"); return 1; }
    if (!cdq_delete_last(d)) { printf("FAIL 7\\n"); return 1; }
    if (!cdq_insert_front(d, 4)) { printf("FAIL 8\\n"); return 1; }
    if (cdq_get_front(d) != 4) { printf("FAIL 9\\n"); return 1; }
    free(d->data); free(d);
    printf("PASS\\n"); return 0; }''',
"cpp":'''#include <cassert>
#include <iostream>
#include <vector>
struct MyCircularDeque {
    std::vector<int> data;
    size_t head = 0, tail = 0, size_ = 0;
    explicit MyCircularDeque(int k) : data(static_cast<size_t>(k)) {}
    bool insertFront(int v) {
        if (size_ == data.size()) return false;
        head = (head + data.size() - 1) % data.size();
        data[head] = v;
        ++size_;
        return true;
    }
    bool insertLast(int v) {
        if (size_ == data.size()) return false;
        data[tail] = v;
        tail = (tail + 1) % data.size();
        ++size_;
        return true;
    }
    bool deleteFront() {
        if (size_ == 0) return false;
        head = (head + 1) % data.size();
        --size_;
        return true;
    }
    bool deleteLast() {
        if (size_ == 0) return false;
        tail = (tail + data.size() - 1) % data.size();
        --size_;
        return true;
    }
    int getFront() { return size_ == 0 ? -1 : data[head]; }
    int getRear() { return size_ == 0 ? -1 : data[(tail + data.size() - 1) % data.size()]; }
    bool isEmpty() { return size_ == 0; }
    bool isFull() { return size_ == data.size(); }
};
int main() {
    MyCircularDeque d(3);
    assert(d.insertLast(1));
    assert(d.insertLast(2));
    assert(d.insertFront(3));
    assert(!d.insertFront(4));
    assert(d.getRear() == 2);
    assert(d.isFull());
    assert(d.deleteLast());
    assert(d.insertFront(4));
    assert(d.getFront() == 4);
    std::cout << "PASS" << std::endl; }''',
"r":'''MyCircularDeque <- function(k) {
  e <- new.env(parent = emptyenv())
  e$data <- rep(0L, k); e$head <- 1L; e$tail <- 1L; e$cap <- k; e$size <- 0L
  e$insertFront <- function(v) {
    if (e$size == e$cap) return(FALSE)
    e$head <<- ((e$head - 2) %% e$cap) + 1L
    e$data[e$head] <<- v
    e$size <<- e$size + 1L
    TRUE
  }
  e$insertLast <- function(v) {
    if (e$size == e$cap) return(FALSE)
    e$data[e$tail] <<- v
    e$tail <<- (e$tail %% e$cap) + 1L
    e$size <<- e$size + 1L
    TRUE
  }
  e$deleteFront <- function() {
    if (e$size == 0) return(FALSE)
    e$head <<- (e$head %% e$cap) + 1L
    e$size <<- e$size - 1L
    TRUE
  }
  e$deleteLast <- function() {
    if (e$size == 0) return(FALSE)
    e$tail <<- ((e$tail - 2) %% e$cap) + 1L
    e$size <<- e$size - 1L
    TRUE
  }
  e$getFront <- function() if (e$size == 0) -1L else e$data[e$head]
  e$getRear <- function() if (e$size == 0) -1L else e$data[((e$tail - 2) %% e$cap) + 1L]
  e$isEmpty <- function() e$size == 0
  e$isFull <- function() e$size == e$cap
  e
}
d <- MyCircularDeque(3)
stopifnot(d$insertLast(1), d$insertLast(2), d$insertFront(3))
stopifnot(!d$insertFront(4))
stopifnot(d$getRear() == 2, d$isFull())
stopifnot(d$deleteLast())
stopifnot(d$insertFront(4), d$getFront() == 4)
cat("PASS\\n")''',
"zig":'''const std = @import("std");
const MyCircularDeque = struct {
    data: [4096]i32,
    head: usize,
    tail: usize,
    cap: usize,
    size: usize,
    fn new(k: usize) MyCircularDeque {
        return .{ .data = undefined, .head = 0, .tail = 0, .cap = k, .size = 0 };
    }
    fn insertFront(self: *MyCircularDeque, v: i32) bool {
        if (self.size == self.cap) return false;
        self.head = (self.head + self.cap - 1) % self.cap;
        self.data[self.head] = v;
        self.size += 1;
        return true;
    }
    fn insertLast(self: *MyCircularDeque, v: i32) bool {
        if (self.size == self.cap) return false;
        self.data[self.tail] = v;
        self.tail = (self.tail + 1) % self.cap;
        self.size += 1;
        return true;
    }
    fn deleteFront(self: *MyCircularDeque) bool {
        if (self.size == 0) return false;
        self.head = (self.head + 1) % self.cap;
        self.size -= 1;
        return true;
    }
    fn deleteLast(self: *MyCircularDeque) bool {
        if (self.size == 0) return false;
        self.tail = (self.tail + self.cap - 1) % self.cap;
        self.size -= 1;
        return true;
    }
    fn getFront(self: *MyCircularDeque) i32 { return if (self.size == 0) -1 else self.data[self.head]; }
    fn getRear(self: *MyCircularDeque) i32 { return if (self.size == 0) -1 else self.data[(self.tail + self.cap - 1) % self.cap]; }
    fn isEmpty(self: *MyCircularDeque) bool { return self.size == 0; }
    fn isFull(self: *MyCircularDeque) bool { return self.size == self.cap; }
};
pub fn main() !void {
    var d = MyCircularDeque.new(3);
    if (!d.insertLast(1)) return error.TestFailed;
    if (!d.insertLast(2)) return error.TestFailed;
    if (!d.insertFront(3)) return error.TestFailed;
    if (d.insertFront(4)) return error.TestFailed;
    if (d.getRear() != 2) return error.TestFailed;
    if (!d.isFull()) return error.TestFailed;
    if (!d.deleteLast()) return error.TestFailed;
    if (!d.insertFront(4)) return error.TestFailed;
    if (d.getFront() != 4) return error.TestFailed;
    std.debug.print("PASS\\n", .{}); }''',
"dart":'''class MyCircularDeque {
  final List<int> data;
  int head = 0, tail = 0, size = 0;
  final int cap;
  MyCircularDeque(this.cap) : data = List<int>.filled(cap, 0);
  bool insertFront(int v) {
    if (size == cap) return false;
    head = (head + cap - 1) % cap;
    data[head] = v;
    size++;
    return true;
  }
  bool insertLast(int v) {
    if (size == cap) return false;
    data[tail] = v;
    tail = (tail + 1) % cap;
    size++;
    return true;
  }
  bool deleteFront() {
    if (size == 0) return false;
    head = (head + 1) % cap;
    size--;
    return true;
  }
  bool deleteLast() {
    if (size == 0) return false;
    tail = (tail + cap - 1) % cap;
    size--;
    return true;
  }
  int getFront() => size == 0 ? -1 : data[head];
  int getRear() => size == 0 ? -1 : data[(tail + cap - 1) % cap];
  bool isEmpty() => size == 0;
  bool isFull() => size == cap;
}
void main() {
  final d = MyCircularDeque(3);
  if (!d.insertLast(1)) throw StateError('c1');
  if (!d.insertLast(2)) throw StateError('c2');
  if (!d.insertFront(3)) throw StateError('c3');
  if (d.insertFront(4)) throw StateError('c4');
  if (d.getRear() != 2) throw StateError('c5');
  if (!d.isFull()) throw StateError('c6');
  if (!d.deleteLast()) throw StateError('c7');
  if (!d.insertFront(4)) throw StateError('c8');
  if (d.getFront() != 4) throw StateError('c9');
  print('PASS'); }''',
}

PROBS = [
    ("1472", "lc_1472_设计浏览器历史记录", "LeetCode 1472. 设计浏览器历史记录"),
    ("641", "lc_641_设计循环双端队列", "LeetCode 641. 设计循环双端队列"),
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
