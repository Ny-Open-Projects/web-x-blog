#!/usr/bin/env python3
# gen_ll2.py — linked_list 第二批：206/876/83/237/203/19 × 7语言
# 均为纯值操作（无环无共享），用值数组验证
import sys, os; sys.path.insert(0, "/Users/Wang/Code/webfault-ai/dsa/_tools")
from langlib import emit, head_comment, EXT

B = {"206": "133785568", "876": "133867938", "83": "133874590", "237": "133886377", "203": "133813394", "19": "133746567"}
LANGNAME = {"rust": "Rust", "lua": "Lua", "c": "C", "cpp": "C++", "r": "R", "zig": "Zig", "dart": "Dart"}

# 每 (lang) 一个模板。R 用 env 节点；C 用 malloc；rust 用 Box。
A206 = {
"rust": '''#[derive(Debug)]
struct ListNode {{ val: i32, next: Option<Box<ListNode>> }}
fn build_list(vals: &[i32]) -> Option<Box<ListNode>> {{
    let mut head: Option<Box<ListNode>> = None;
    for &v in vals.iter().rev() {{ head = Some(Box::new(ListNode {{ val: v, next: head }})); }}
    head
}}
fn to_vec(h: &Option<Box<ListNode>>) -> Vec<i32> {{
    let mut out = Vec::new();
    let mut cur = h;
    while let Some(n) = cur {{ out.push(n.val); cur = &n.next; }}
    out
}}
fn reverse_list(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {{
    let mut prev: Option<Box<ListNode>> = None;
    let mut cur = head;
    while let Some(mut node) = cur {{
        cur = node.next.take();
        node.next = prev;
        prev = Some(node);
    }}
    prev
}}
fn main() {{
    let got = to_vec(&reverse_list(build_list(&[1, 2, 3, 4, 5])));
    assert_eq!(got, vec![5, 4, 3, 2, 1]);
    assert_eq!(to_vec(&reverse_list(build_list(&[]))), Vec::<i32>::new());
    assert_eq!(to_vec(&reverse_list(build_list(&[1]))), vec![1]);
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
local function to_vec(h)
    local out = {}
    while h do out[#out + 1] = h.val; h = h.next end
    return out
end
local function reverse_list(head)
    local prev = nil
    local cur = head
    while cur do
        local nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    end
    return prev
end
assert(table.concat(to_vec(reverse_list(build_list({1, 2, 3, 4, 5}))), ",") == "5,4,3,2,1")
assert(#to_vec(reverse_list(build_list({}))) == 0)
assert(table.concat(to_vec(reverse_list(build_list({1}))), ",") == "1")
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
    while (h) {{ if (i >= wn || h->val != want[i]) return 0; i++; h = h->next; }}
    return i == wn;
}}
static LNode *reverse_list(LNode *head) {{
    LNode *prev = NULL, *cur = head;
    while (cur) {{
        LNode *nxt = cur->next;
        cur->next = prev;
        prev = cur;
        cur = nxt;
    }}
    return prev;
}}
int main(void) {{
    LNode *r = reverse_list(build_list((int[]){{1,2,3,4,5}}, 5));
    int w1[] = {{5,4,3,2,1}};
    if (!list_check(r, w1, 5)) {{ printf("FAIL 1\\n"); return 1; }}
    free_list(r);
    if (reverse_list(NULL) != NULL) {{ printf("FAIL 2\\n"); return 1; }}
    LNode *r3 = reverse_list(build_list((int[]){{1}}, 1));
    int w3[] = {{1}};
    if (!list_check(r3, w3, 1)) {{ printf("FAIL 3\\n"); return 1; }}
    free_list(r3);
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
static std::vector<int> toVec(ListNode *h) {
    std::vector<int> out;
    while (h) { out.push_back(h->val); h = h->next.get(); }
    return out;
}
static std::unique_ptr<ListNode> reverseList(std::unique_ptr<ListNode> head) {
    std::unique_ptr<ListNode> prev;
    while (head) {
        auto nxt = std::move(head->next);
        head->next = std::move(prev);
        prev = std::move(head);
        head = std::move(nxt);
    }
    return prev;
}
int main() {
    assert((toVec(reverseList(buildList({1, 2, 3, 4, 5})).get()) == std::vector<int>{5, 4, 3, 2, 1}));
    assert(toVec(reverseList(nullptr).get()).empty());
    assert((toVec(reverseList(buildList({1})).get()) == std::vector<int>{1}));
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''ListNode <- function(val, nxt = NULL) {{ e <- new.env(parent = emptyenv()); e$val <- val; e$nxt <- nxt; class(e) <- "ListNode"; e }}
build_list <- function(vals) {{
  head <- NULL; cur <- NULL
  for (v in vals) {{
    n <- ListNode(v)
    if (is.null(head)) { head <- n; cur <- n } else { cur$nxt <- n; cur <- n }
  }}
  head
}}
to_vec <- function(h) {{ out <- integer(0); while (!is.null(h)) { out <- c(out, h$val); h <- h$nxt }; out }}
reverse_list <- function(head) {
  prev <- NULL; cur <- head
  while (!is.null(cur)) {
    nxt <- cur$nxt
    cur$nxt <- prev
    prev <- cur
    cur <- nxt
  }
  prev
}
stopifnot(identical(to_vec(reverse_list(build_list(1:5))), 5:1))
stopifnot(length(to_vec(reverse_list(build_list(integer(0))))) == 0)
stopifnot(identical(to_vec(reverse_list(build_list(1L))), 1L))
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
fn toVec(h: ?*LNode, out: *std.ArrayList(i32)) void {
    var cur = h;
    while (cur) |n| { out.append(n.val) catch unreachable; cur = n.next; }
}
fn reverseList(head: ?*LNode) ?*LNode {
    var prev: ?*LNode = null;
    var cur = head;
    while (cur) |node| {
        const nxt = node.next;
        node.next = prev;
        prev = node;
        cur = nxt;
    }
    return prev;
}
pub fn main() !void {
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();
    const alloc = arena.allocator();
    var out = std.ArrayList(i32).init(std.heap.page_allocator);
    defer out.deinit();
    toVec(reverseList(buildList(alloc, &[_]i32{ 1, 2, 3, 4, 5 })), &out);
    const want = [_]i32{ 5, 4, 3, 2, 1 };
    if (out.items.len != want.len) return error.TestFailed;
    for (want, 0..) |w, i| if (out.items[i] != w) return error.TestFailed;
    out.clearRetainingCapacity();
    toVec(reverseList(null), &out);
    if (out.items.len != 0) return error.TestFailed;
    out.clearRetainingCapacity();
    toVec(reverseList(buildList(alloc, &[_]i32{1})), &out);
    if (out.items.len != 1 or out.items[0] != 1) return error.TestFailed;
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
List<int> toVec(LNode? h) {
  final out = <int>[];
  while (h != null) {
    out.add(h.val);
    h = h.next;
  }
  return out;
}
LNode? reverseList(LNode? head) {
  LNode? prev;
  var cur = head;
  while (cur != null) {
    final nxt = cur.next;
    cur.next = prev;
    prev = cur;
    cur = nxt;
  }
  return prev;
}
void main() {
  if (toVec(reverseList(buildList([1, 2, 3, 4, 5]))).toString() != '[5, 4, 3, 2, 1]') throw StateError('c1');
  if (toVec(reverseList(null)).isNotEmpty) throw StateError('c2');
  if (toVec(reverseList(buildList([1]))).toString() != '[1]') throw StateError('c3');
  print('PASS');
}
''',
}

A876 = {
"rust": '''#[derive(Debug)]
struct ListNode {{ val: i32, next: Option<Box<ListNode>> }}
fn build_list(vals: &[i32]) -> Option<Box<ListNode>> {{
    let mut head: Option<Box<ListNode>> = None;
    for &v in vals.iter().rev() {{ head = Some(Box::new(ListNode {{ val: v, next: head }})); }}
    head
}}
fn to_vec(h: &Option<Box<ListNode>>) -> Vec<i32> {{
    let mut out = Vec::new();
    let mut cur = h;
    while let Some(n) = cur {{ out.push(n.val); cur = &n.next; }}
    out
}}
fn middle_node(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {{
    // 快慢指针找中间：返回后半段起点（转移所有权：重建后半段）
    let mut vals = Vec::new();
    let mut cur = &head;
    while let Some(n) = cur {{ vals.push(n.val); cur = &n.next; }}
    let mid = vals.len() / 2;
    let mut out: Option<Box<ListNode>> = None;
    for &v in vals[mid..].iter().rev() {{ out = Some(Box::new(ListNode {{ val: v, next: out }})); }}
    out
}}
fn main() {{
    assert_eq!(to_vec(&middle_node(build_list(&[1, 2, 3, 4, 5]))), vec![3, 4, 5]);
    assert_eq!(to_vec(&middle_node(build_list(&[1, 2, 3, 4, 5, 6]))), vec![4, 5, 6]);
    assert_eq!(to_vec(&middle_node(build_list(&[1]))), vec![1]);
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
local function to_vec(h)
    local out = {}
    while h do out[#out + 1] = h.val; h = h.next end
    return out
end
local function middle_node(head)
    local slow, fast = head, head
    while fast and fast.next do
        slow = slow.next
        fast = fast.next.next
    end
    return slow
end
assert(table.concat(to_vec(middle_node(build_list({1,2,3,4,5}))), ",") == "3,4,5")
assert(table.concat(to_vec(middle_node(build_list({1,2,3,4,5,6}))), ",") == "4,5,6")
assert(table.concat(to_vec(middle_node(build_list({1}))), ",") == "1")
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
    while (h) {{ if (i >= wn || h->val != want[i]) return 0; i++; h = h->next; }}
    return i == wn;
}}
static LNode *middle_node(LNode *head) {{
    LNode *slow = head, *fast = head;
    while (fast && fast->next) {{
        slow = slow->next;
        fast = fast->next->next;
    }}
    return slow;
}}
int main(void) {{
    int w1[] = {{3,4,5}}, w2[] = {{4,5,6}}, w3[] = {{1}};
    LNode *m = middle_node(build_list((int[]){{1,2,3,4,5}}, 5));
    if (!list_check(m, w1, 3)) {{ printf("FAIL 1\\n"); return 1; }}
    free_list(m);
    LNode *m2 = middle_node(build_list((int[]){{1,2,3,4,5,6}}, 6));
    if (!list_check(m2, w2, 3)) {{ printf("FAIL 2\\n"); return 1; }}
    free_list(m2);
    LNode *m3 = middle_node(build_list((int[]){{1}}, 1));
    if (!list_check(m3, w3, 1)) {{ printf("FAIL 3\\n"); return 1; }}
    free_list(m3);
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
    ListNode *next = nullptr;
    explicit ListNode(int v) : val(v) {}
};
static ListNode *buildList(const std::vector<int> &vals) {
    ListNode dummy(0);
    ListNode *cur = &dummy;
    for (int v : vals) {
        cur->next = new ListNode(v);
        cur = cur->next;
    }
    return dummy.next;
}
static void freeList(ListNode *h) { while (h) { ListNode *n = h->next; delete h; h = n; } }
static std::vector<int> toVec(ListNode *h) {
    std::vector<int> out;
    while (h) { out.push_back(h->val); h = h->next; }
    return out;
}
static ListNode *middleNode(ListNode *head) {
    ListNode *slow = head, *fast = head;
    while (fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
    }
    return slow;
}
int main() {
    ListNode *m = middleNode(buildList({1, 2, 3, 4, 5}));
    assert((toVec(m) == std::vector<int>{3, 4, 5}));
    freeList(m);
    ListNode *m2 = middleNode(buildList({1, 2, 3, 4, 5, 6}));
    assert((toVec(m2) == std::vector<int>{4, 5, 6}));
    freeList(m2);
    ListNode *m3 = middleNode(buildList({1}));
    assert((toVec(m3) == std::vector<int>{1}));
    freeList(m3);
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''ListNode <- function(val, nxt = NULL) {{ e <- new.env(parent = emptyenv()); e$val <- val; e$nxt <- nxt; class(e) <- "ListNode"; e }}
build_list <- function(vals) {{
  head <- NULL; cur <- NULL
  for (v in vals) {{
    n <- ListNode(v)
    if (is.null(head)) { head <- n; cur <- n } else { cur$nxt <- n; cur <- n }
  }}
  head
}}
to_vec <- function(h) {{ out <- integer(0); while (!is.null(h)) { out <- c(out, h$val); h <- h$nxt }; out }}
middle_node <- function(head) {
  slow <- head; fast <- head
  while (!is.null(fast) && !is.null(fast$nxt)) {
    slow <- slow$nxt
    fast <- fast$nxt$nxt
  }
  slow
}
stopifnot(identical(to_vec(middle_node(build_list(1:5))), 3:5))
stopifnot(identical(to_vec(middle_node(build_list(1:6))), 4:6))
stopifnot(identical(to_vec(middle_node(build_list(1L))), 1L))
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
fn toVec(h: ?*LNode, out: *std.ArrayList(i32)) void {
    var cur = h;
    while (cur) |n| { out.append(n.val) catch unreachable; cur = n.next; }
}
fn middleNode(head: ?*LNode) ?*LNode {
    var slow = head;
    var fast = head;
    while (fast != null and fast.?.next != null) {
        slow = slow.?.next;
        fast = fast.?.next.?.next;
    }
    return slow;
}
pub fn main() !void {
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();
    const alloc = arena.allocator();
    var out = std.ArrayList(i32).init(std.heap.page_allocator);
    defer out.deinit();
    toVec(middleNode(buildList(alloc, &[_]i32{ 1, 2, 3, 4, 5 })), &out);
    if (out.items.len != 3 or out.items[0] != 3) return error.TestFailed;
    out.clearRetainingCapacity();
    toVec(middleNode(buildList(alloc, &[_]i32{ 1, 2, 3, 4, 5, 6 })), &out);
    if (out.items.len != 3 or out.items[0] != 4) return error.TestFailed;
    out.clearRetainingCapacity();
    toVec(middleNode(buildList(alloc, &[_]i32{1})), &out);
    if (out.items.len != 1 or out.items[0] != 1) return error.TestFailed;
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
List<int> toVec(LNode? h) {
  final out = <int>[];
  while (h != null) {
    out.add(h.val);
    h = h.next;
  }
  return out;
}
LNode? middleNode(LNode? head) {
  LNode? slow = head, fast = head;
  while (fast != null && fast.next != null) {
    slow = slow!.next;
    fast = fast.next!.next;
  }
  return slow;
}
void main() {
  if (toVec(middleNode(buildList([1, 2, 3, 4, 5]))).toString() != '[3, 4, 5]') throw StateError('c1');
  if (toVec(middleNode(buildList([1, 2, 3, 4, 5, 6]))).toString() != '[4, 5, 6]') throw StateError('c2');
  if (toVec(middleNode(buildList([1]))).toString() != '[1]') throw StateError('c3');
  print('PASS');
}
''',
}

A83 = {
"rust": '''#[derive(Debug)]
struct ListNode {{ val: i32, next: Option<Box<ListNode>> }}
fn build_list(vals: &[i32]) -> Option<Box<ListNode>> {{
    let mut head: Option<Box<ListNode>> = None;
    for &v in vals.iter().rev() {{ head = Some(Box::new(ListNode {{ val: v, next: head }})); }}
    head
}}
fn to_vec(h: &Option<Box<ListNode>>) -> Vec<i32> {{
    let mut out = Vec::new();
    let mut cur = h;
    while let Some(n) = cur {{ out.push(n.val); cur = &n.next; }}
    out
}}
fn delete_duplicates(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {{
    let mut vals = to_vec(&head);
    vals.dedup();
    let mut out: Option<Box<ListNode>> = None;
    for &v in vals.iter().rev() {{ out = Some(Box::new(ListNode {{ val: v, next: out }})); }}
    out
}}
fn main() {{
    assert_eq!(to_vec(&delete_duplicates(build_list(&[1, 1, 2]))), vec![1, 2]);
    assert_eq!(to_vec(&delete_duplicates(build_list(&[1, 1, 2, 3, 3]))), vec![1, 2, 3]);
    assert_eq!(to_vec(&delete_duplicates(build_list(&[1, 1, 1]))), vec![1]);
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
local function to_vec(h)
    local out = {}
    while h do out[#out + 1] = h.val; h = h.next end
    return out
end
local function delete_duplicates(head)
    local cur = head
    while cur and cur.next do
        if cur.val == cur.next.val then
            cur.next = cur.next.next
        else
            cur = cur.next
        end
    end
    return head
end
assert(table.concat(to_vec(delete_duplicates(build_list({1,1,2}))), ",") == "1,2")
assert(table.concat(to_vec(delete_duplicates(build_list({1,1,2,3,3}))), ",") == "1,2,3")
assert(table.concat(to_vec(delete_duplicates(build_list({1,1,1}))), ",") == "1")
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
    while (h) {{ if (i >= wn || h->val != want[i]) return 0; i++; h = h->next; }}
    return i == wn;
}}
static LNode *delete_duplicates(LNode *head) {{
    LNode *cur = head;
    while (cur && cur->next) {{
        if (cur->val == cur->next->val) {{
            LNode *dup = cur->next;
            cur->next = dup->next;
            free(dup);
        } else {
            cur = cur->next;
        }
    }}
    return head;
}}
int main(void) {{
    int w1[] = {{1,2}}, w2[] = {{1,2,3}}, w3[] = {{1}};
    LNode *r = delete_duplicates(build_list((int[]){{1,1,2}}, 3));
    if (!list_check(r, w1, 2)) {{ printf("FAIL 1\\n"); return 1; }}
    free_list(r);
    LNode *r2 = delete_duplicates(build_list((int[]){{1,1,2,3,3}}, 5));
    if (!list_check(r2, w2, 3)) {{ printf("FAIL 2\\n"); return 1; }}
    free_list(r2);
    LNode *r3 = delete_duplicates(build_list((int[]){{1,1,1}}, 3));
    if (!list_check(r3, w3, 1)) {{ printf("FAIL 3\\n"); return 1; }}
    free_list(r3);
    printf("PASS\\n");
    return 0;
}}
''',
"cpp": '''#include <cassert>
#include <iostream>
#include <vector>
struct ListNode {
    int val;
    ListNode *next = nullptr;
    explicit ListNode(int v) : val(v) {}
};
static ListNode *buildList(const std::vector<int> &vals) {
    ListNode dummy(0);
    ListNode *cur = &dummy;
    for (int v : vals) {
        cur->next = new ListNode(v);
        cur = cur->next;
    }
    return dummy.next;
}
static void freeList(ListNode *h) { while (h) { ListNode *n = h->next; delete h; h = n; } }
static std::vector<int> toVec(ListNode *h) {
    std::vector<int> out;
    while (h) { out.push_back(h->val); h = h->next; }
    return out;
}
static ListNode *deleteDuplicates(ListNode *head) {
    ListNode *cur = head;
    while (cur && cur->next) {
        if (cur->val == cur->next->val) {
            ListNode *dup = cur->next;
            cur->next = dup->next;
            delete dup;
        } else {
            cur = cur->next;
        }
    }
    return head;
}
int main() {
    ListNode *r = deleteDuplicates(buildList({1, 1, 2}));
    assert((toVec(r) == std::vector<int>{1, 2}));
    freeList(r);
    ListNode *r2 = deleteDuplicates(buildList({1, 1, 2, 3, 3}));
    assert((toVec(r2) == std::vector<int>{1, 2, 3}));
    freeList(r2);
    ListNode *r3 = deleteDuplicates(buildList({1, 1, 1}));
    assert((toVec(r3) == std::vector<int>{1}));
    freeList(r3);
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''ListNode <- function(val, nxt = NULL) {{ e <- new.env(parent = emptyenv()); e$val <- val; e$nxt <- nxt; class(e) <- "ListNode"; e }}
build_list <- function(vals) {{
  head <- NULL; cur <- NULL
  for (v in vals) {{
    n <- ListNode(v)
    if (is.null(head)) { head <- n; cur <- n } else { cur$nxt <- n; cur <- n }
  }}
  head
}}
to_vec <- function(h) {{ out <- integer(0); while (!is.null(h)) { out <- c(out, h$val); h <- h$nxt }; out }}
delete_duplicates <- function(head) {
  if (is.null(head)) return(NULL)
  vals <- to_vec(head)
  vals <- vals[c(TRUE, vals[-1] != vals[-length(vals)])]
  out <- NULL; cur <- NULL
  for (v in vals) {
    n <- ListNode(v)
    if (is.null(out)) { out <- n; cur <- n } else { cur$nxt <- n; cur <- n }
  }
  out
}
stopifnot(identical(to_vec(delete_duplicates(build_list(c(1, 1, 2)))), c(1, 2)))
stopifnot(identical(to_vec(delete_duplicates(build_list(c(1, 1, 2, 3, 3)))), c(1, 2, 3)))
stopifnot(identical(to_vec(delete_duplicates(build_list(c(1, 1, 1)))), 1))
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
fn toVec(h: ?*LNode, out: *std.ArrayList(i32)) void {
    var cur = h;
    while (cur) |n| { out.append(n.val) catch unreachable; cur = n.next; }
}
fn deleteDuplicates(head: ?*LNode) ?*LNode {
    var cur = head;
    while (cur) |node| {
        if (node.next) |nxt| {
            if (nxt.val == node.val) {
                node.next = nxt.next;
                continue;
            }
        }
        cur = node.next;
    }
    return head;
}
pub fn main() !void {
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();
    const alloc = arena.allocator();
    var out = std.ArrayList(i32).init(std.heap.page_allocator);
    defer out.deinit();
    toVec(deleteDuplicates(buildList(alloc, &[_]i32{ 1, 1, 2 })), &out);
    if (out.items.len != 2 or out.items[0] != 1 or out.items[1] != 2) return error.TestFailed;
    out.clearRetainingCapacity();
    toVec(deleteDuplicates(buildList(alloc, &[_]i32{ 1, 1, 2, 3, 3 })), &out);
    if (out.items.len != 3 or out.items[2] != 3) return error.TestFailed;
    out.clearRetainingCapacity();
    toVec(deleteDuplicates(buildList(alloc, &[_]i32{ 1, 1, 1 })), &out);
    if (out.items.len != 1) return error.TestFailed;
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
List<int> toVec(LNode? h) {
  final out = <int>[];
  while (h != null) {
    out.add(h.val);
    h = h.next;
  }
  return out;
}
LNode? deleteDuplicates(LNode? head) {
  var cur = head;
  while (cur != null && cur.next != null) {
    if (cur.val == cur.next!.val) {
      cur.next = cur.next!.next;
    } else {
      cur = cur.next;
    }
  }
  return head;
}
void main() {
  if (toVec(deleteDuplicates(buildList([1, 1, 2]))).toString() != '[1, 2]') throw StateError('c1');
  if (toVec(deleteDuplicates(buildList([1, 1, 2, 3, 3]))).toString() != '[1, 2, 3]') throw StateError('c2');
  if (toVec(deleteDuplicates(buildList([1, 1, 1]))).toString() != '[1]') throw StateError('c3');
  print('PASS');
}
''',
}

A237 = {
"rust": '''#[derive(Debug)]
struct ListNode {{ val: i32, next: Option<Box<ListNode>> }}
fn build_list(vals: &[i32]) -> Option<Box<ListNode>> {{
    let mut head: Option<Box<ListNode>> = None;
    for &v in vals.iter().rev() {{ head = Some(Box::new(ListNode {{ val: v, next: head }})); }}
    head
}}
fn to_vec(h: &Option<Box<ListNode>>) -> Vec<i32> {{
    let mut out = Vec::new();
    let mut cur = h;
    while let Some(n) = cur {{ out.push(n.val); cur = &n.next; }}
    out
}}
fn delete_node_by_val(head: &mut Option<Box<ListNode>>, target: i32) {{
    // LeetCode 237 语义：复制下一节点值后删除下一节点。
    // Rust 的 Box 所有权模型下等价实现：按值删除首个匹配节点（重建法）。
    let vals = to_vec(head);
    let mut kept: Vec<i32> = Vec::new();
    let mut skipped = false;
    for &v in &vals {{
        if !skipped && v == target {{ skipped = true; continue; }}
        kept.push(v);
    }}
    let mut out: Option<Box<ListNode>> = None;
    for &v in kept.iter().rev() {{ out = Some(Box::new(ListNode {{ val: v, next: out }})); }}
    *head = out;
}}
fn main() {{
    let mut l = build_list(&[4, 5, 1, 9]);
    delete_node_by_val(&mut l, 5);
    assert_eq!(to_vec(&l), vec![4, 1, 9]);
    let mut l2 = build_list(&[1, 2, 3]);
    delete_node_by_val(&mut l2, 2);
    assert_eq!(to_vec(&l2), vec![1, 3]);
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
local function to_vec(h)
    local out = {}
    while h do out[#out + 1] = h.val; h = h.next end
    return out
end
local function delete_node(node)
    node.val = node.next.val
    node.next = node.next.next
end
local l = build_list({4, 5, 1, 9})
delete_node(l.next)  -- 删除节点 5
assert(table.concat(to_vec(l), ",") == "4,1,9")
local l2 = build_list({1, 2, 3})
delete_node(l2.next)  -- 删除节点 2
assert(table.concat(to_vec(l2), ",") == "1,3")
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
    while (h) {{ if (i >= wn || h->val != want[i]) return 0; i++; h = h->next; }}
    return i == wn;
}}
static void delete_node(LNode *node) {{
    LNode *next = node->next;
    node->val = next->val;
    node->next = next->next;
    free(next);
}}
int main(void) {{
    LNode *l = build_list((int[]){{4,5,1,9}}, 4);
    delete_node(l->next);
    int w1[] = {{4,1,9}};
    if (!list_check(l, w1, 3)) {{ printf("FAIL 1\\n"); return 1; }}
    free_list(l);
    LNode *l2 = build_list((int[]){{1,2,3}}, 3);
    delete_node(l2->next);
    int w2[] = {{1,3}};
    if (!list_check(l2, w2, 2)) {{ printf("FAIL 2\\n"); return 1; }}
    free_list(l2);
    printf("PASS\\n");
    return 0;
}}
''',
"cpp": '''#include <cassert>
#include <iostream>
#include <vector>
struct ListNode {
    int val;
    ListNode *next = nullptr;
    explicit ListNode(int v) : val(v) {}
};
static ListNode *buildList(const std::vector<int> &vals) {
    ListNode dummy(0);
    ListNode *cur = &dummy;
    for (int v : vals) {
        cur->next = new ListNode(v);
        cur = cur->next;
    }
    return dummy.next;
}
static void freeList(ListNode *h) { while (h) { ListNode *n = h->next; delete h; h = n; } }
static std::vector<int> toVec(ListNode *h) {
    std::vector<int> out;
    while (h) { out.push_back(h->val); h = h->next; }
    return out;
}
static void deleteNode(ListNode *node) {
    ListNode *next = node->next;
    node->val = next->val;
    node->next = next->next;
    delete next;
}
int main() {
    ListNode *l = buildList({4, 5, 1, 9});
    deleteNode(l->next);
    assert((toVec(l) == std::vector<int>{4, 1, 9}));
    freeList(l);
    ListNode *l2 = buildList({1, 2, 3});
    deleteNode(l2->next);
    assert((toVec(l2) == std::vector<int>{1, 3}));
    freeList(l2);
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''ListNode <- function(val, nxt = NULL) {{ e <- new.env(parent = emptyenv()); e$val <- val; e$nxt <- nxt; class(e) <- "ListNode"; e }}
build_list <- function(vals) {{
  head <- NULL; cur <- NULL
  for (v in vals) {{
    n <- ListNode(v)
    if (is.null(head)) { head <- n; cur <- n } else { cur$nxt <- n; cur <- n }
  }}
  head
}}
to_vec <- function(h) {{ out <- integer(0); while (!is.null(h)) { out <- c(out, h$val); h <- h$nxt }; out }}
delete_node <- function(node) {
  nxt <- node$nxt
  node$val <- nxt$val
  node$nxt <- nxt$nxt
}
l <- build_list(c(4, 5, 1, 9))
delete_node(l$nxt)
stopifnot(identical(to_vec(l), c(4, 1, 9)))
l2 <- build_list(c(1, 2, 3))
delete_node(l2$nxt)
stopifnot(identical(to_vec(l2), c(1, 3)))
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
fn toVec(h: ?*LNode, out: *std.ArrayList(i32)) void {
    var cur = h;
    while (cur) |n| { out.append(n.val) catch unreachable; cur = n.next; }
}
fn deleteNode(node: *LNode) void {
    const next = node.next.?;
    node.val = next.val;
    node.next = next.next;
}
pub fn main() !void {
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();
    const alloc = arena.allocator();
    var out = std.ArrayList(i32).init(std.heap.page_allocator);
    defer out.deinit();
    const l = buildList(alloc, &[_]i32{ 4, 5, 1, 9 }).?;
    deleteNode(l.next.?);
    toVec(l, &out);
    if (out.items.len != 3 or out.items[0] != 4 or out.items[1] != 1 or out.items[2] != 9) return error.TestFailed;
    out.clearRetainingCapacity();
    const l2 = buildList(alloc, &[_]i32{ 1, 2, 3 }).?;
    deleteNode(l2.next.?);
    toVec(l2, &out);
    if (out.items.len != 2 or out.items[0] != 1 or out.items[1] != 3) return error.TestFailed;
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''class LNode {
  int val;
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
List<int> toVec(LNode? h) {
  final out = <int>[];
  while (h != null) {
    out.add(h.val);
    h = h.next;
  }
  return out;
}
void deleteNode(LNode node) {
  final next = node.next!;
  node.val = next.val;
  node.next = next.next;
}
void main() {
  final l = buildList([4, 5, 1, 9])!;
  deleteNode(l.next!);
  if (toVec(l).toString() != '[4, 1, 9]') throw StateError('c1');
  final l2 = buildList([1, 2, 3])!;
  deleteNode(l2.next!);
  if (toVec(l2).toString() != '[1, 3]') throw StateError('c2');
  print('PASS');
}
''',
}

A203 = {
"rust": '''#[derive(Debug)]
struct ListNode {{ val: i32, next: Option<Box<ListNode>> }}
fn build_list(vals: &[i32]) -> Option<Box<ListNode>> {{
    let mut head: Option<Box<ListNode>> = None;
    for &v in vals.iter().rev() {{ head = Some(Box::new(ListNode {{ val: v, next: head }})); }}
    head
}}
fn to_vec(h: &Option<Box<ListNode>>) -> Vec<i32> {{
    let mut out = Vec::new();
    let mut cur = h;
    while let Some(n) = cur {{ out.push(n.val); cur = &n.next; }}
    out
}}
fn remove_elements(head: Option<Box<ListNode>>, val: i32) -> Option<Box<ListNode>> {{
    // 重建法（Rust 所有权友好）
    let vals = to_vec(&head);
    let kept: Vec<i32> = vals.into_iter().filter(|&v| v != val).collect();
    let mut out: Option<Box<ListNode>> = None;
    for &v in kept.iter().rev() {{ out = Some(Box::new(ListNode {{ val: v, next: out }})); }}
    out
}}
fn main() {{
    assert_eq!(to_vec(&remove_elements(build_list(&[1,2,3,4,5,6]), 6)), vec![1, 2, 3, 4, 5]);
    assert_eq!(to_vec(&remove_elements(build_list(&[7,7,7,7]), 7)), Vec::<i32>::new());
    assert_eq!(to_vec(&remove_elements(build_list(&[1,2,2,1]), 2)), vec![1, 1]);
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
local function to_vec(h)
    local out = {}
    while h do out[#out + 1] = h.val; h = h.next end
    return out
end
local function remove_elements(head, val)
    local dummy = ListNode.new(0)
    dummy.next = head
    local cur = dummy
    while cur.next do
        if cur.next.val == val then
            cur.next = cur.next.next
        else
            cur = cur.next
        end
    end
    return dummy.next
end
assert(table.concat(to_vec(remove_elements(build_list({1,2,3,4,5,6}), 6)), ",") == "1,2,3,4,5")
assert(remove_elements(build_list({7,7,7,7}), 7) == nil)
assert(table.concat(to_vec(remove_elements(build_list({1,2,2,1}), 2)), ",") == "1,1")
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
    while (h) {{ if (i >= wn || h->val != want[i]) return 0; i++; h = h->next; }}
    return i == wn;
}}
static LNode *remove_elements(LNode *head, int val) {{
    LNode dummy = {{0, NULL}};
    dummy.next = head;
    LNode *cur = &dummy;
    while (cur->next) {{
        if (cur->next->val == val) {{
            LNode *rm = cur->next;
            cur->next = rm->next;
            free(rm);
        }} else {
            cur = cur->next;
        }}
    }}
    return dummy.next;
}}
int main(void) {{
    int w1[] = {{1,2,3,4,5}}, w3[] = {{1,1}};
    LNode *r = remove_elements(build_list((int[]){{1,2,3,4,5,6}}, 6), 6);
    if (!list_check(r, w1, 5)) {{ printf("FAIL 1\\n"); return 1; }}
    free_list(r);
    if (remove_elements(build_list((int[]){{7,7,7,7}}, 4), 7) != NULL) {{ printf("FAIL 2\\n"); return 1; }}
    LNode *r3 = remove_elements(build_list((int[]){{1,2,2,1}}, 4), 2);
    if (!list_check(r3, w3, 2)) {{ printf("FAIL 3\\n"); return 1; }}
    free_list(r3);
    printf("PASS\\n");
    return 0;
}}
''',
"cpp": '''#include <cassert>
#include <iostream>
#include <vector>
struct ListNode {
    int val;
    ListNode *next = nullptr;
    explicit ListNode(int v) : val(v) {}
};
static ListNode *buildList(const std::vector<int> &vals) {
    ListNode dummy(0);
    ListNode *cur = &dummy;
    for (int v : vals) {
        cur->next = new ListNode(v);
        cur = cur->next;
    }
    return dummy.next;
}
static void freeList(ListNode *h) { while (h) { ListNode *n = h->next; delete h; h = n; } }
static std::vector<int> toVec(ListNode *h) {
    std::vector<int> out;
    while (h) { out.push_back(h->val); h = h->next; }
    return out;
}
static ListNode *removeElements(ListNode *head, int val) {
    ListNode dummy(0);
    dummy.next = head;
    ListNode *cur = &dummy;
    while (cur->next) {
        if (cur->next->val == val) {
            ListNode *rm = cur->next;
            cur->next = rm->next;
            delete rm;
        } else {
            cur = cur->next;
        }
    }
    return dummy.next;
}
int main() {
    ListNode *r = removeElements(buildList({1, 2, 3, 4, 5, 6}), 6);
    assert((toVec(r) == std::vector<int>{1, 2, 3, 4, 5}));
    freeList(r);
    assert(removeElements(buildList({7, 7, 7, 7}), 7) == nullptr);
    ListNode *r3 = removeElements(buildList({1, 2, 2, 1}), 2);
    assert((toVec(r3) == std::vector<int>{1, 1}));
    freeList(r3);
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''ListNode <- function(val, nxt = NULL) {{ e <- new.env(parent = emptyenv()); e$val <- val; e$nxt <- nxt; class(e) <- "ListNode"; e }}
build_list <- function(vals) {{
  head <- NULL; cur <- NULL
  for (v in vals) {{
    n <- ListNode(v)
    if (is.null(head)) { head <- n; cur <- n } else { cur$nxt <- n; cur <- n }
  }}
  head
}}
to_vec <- function(h) {{ out <- integer(0); while (!is.null(h)) { out <- c(out, h$val); h <- h$nxt }; out }}
remove_elements <- function(head, val) {
  dummy <- ListNode(0, head)
  cur <- dummy
  while (!is.null(cur$nxt)) {
    if (cur$nxt$val == val) {
      cur$nxt <- cur$nxt$nxt
    } else {
      cur <- cur$nxt
    }
  }
  dummy$nxt
}
stopifnot(identical(to_vec(remove_elements(build_list(1:6), 6)), 1:5))
stopifnot(is.null(remove_elements(build_list(rep(7, 4)), 7)))
stopifnot(identical(to_vec(remove_elements(build_list(c(1, 2, 2, 1)), 2)), c(1, 1)))
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
fn toVec(h: ?*LNode, out: *std.ArrayList(i32)) void {
    var cur = h;
    while (cur) |n| { out.append(n.val) catch unreachable; cur = n.next; }
}
fn removeElements(alloc: std.mem.Allocator, head: ?*LNode, val: i32) ?*LNode {
    const dummy = alloc.create(LNode) catch unreachable;
    dummy.* = .{ .val = 0, .next = head };
    var cur = dummy;
    while (cur.next) |nxt| {
        if (nxt.val == val) {
            cur.next = nxt.next;
        } else {
            cur = nxt;
        }
    }
    return dummy.next;
}
pub fn main() !void {
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();
    const alloc = arena.allocator();
    var out = std.ArrayList(i32).init(std.heap.page_allocator);
    defer out.deinit();
    toVec(removeElements(alloc, buildList(alloc, &[_]i32{ 1, 2, 3, 4, 5, 6 }), 6), &out);
    if (out.items.len != 5 or out.items[4] != 5) return error.TestFailed;
    out.clearRetainingCapacity();
    if (removeElements(alloc, buildList(alloc, &[_]i32{ 7, 7, 7, 7 }), 7) != null) return error.TestFailed;
    toVec(removeElements(alloc, buildList(alloc, &[_]i32{ 1, 2, 2, 1 }), 2), &out);
    if (out.items.len != 2 or out.items[0] != 1 or out.items[1] != 1) return error.TestFailed;
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
List<int> toVec(LNode? h) {
  final out = <int>[];
  while (h != null) {
    out.add(h.val);
    h = h.next;
  }
  return out;
}
LNode? removeElements(LNode? head, int val) {
  final dummy = LNode(0);
  dummy.next = head;
  var cur = dummy;
  while (cur.next != null) {
    if (cur.next!.val == val) {
      cur.next = cur.next!.next;
    } else {
      cur = cur.next!;
    }
  }
  return dummy.next;
}
void main() {
  if (toVec(removeElements(buildList([1, 2, 3, 4, 5, 6]), 6)).toString() != '[1, 2, 3, 4, 5]') throw StateError('c1');
  if (removeElements(buildList([7, 7, 7, 7]), 7) != null) throw StateError('c2');
  if (toVec(removeElements(buildList([1, 2, 2, 1]), 2)).toString() != '[1, 1]') throw StateError('c3');
  print('PASS');
}
''',
}

A19 = {
"rust": '''#[derive(Debug)]
struct ListNode {{ val: i32, next: Option<Box<ListNode>> }}
fn build_list(vals: &[i32]) -> Option<Box<ListNode>> {{
    let mut head: Option<Box<ListNode>> = None;
    for &v in vals.iter().rev() {{ head = Some(Box::new(ListNode {{ val: v, next: head }})); }}
    head
}}
fn to_vec(h: &Option<Box<ListNode>>) -> Vec<i32> {{
    let mut out = Vec::new();
    let mut cur = h;
    while let Some(n) = cur {{ out.push(n.val); cur = &n.next; }}
    out
}}
fn remove_nth_from_end(head: Option<Box<ListNode>>, n: i32) -> Option<Box<ListNode>> {{
    let vals = to_vec(&head);
    let len = vals.len();
    let idx = len as i32 - n;  // 要删除的下标
    let mut out: Option<Box<ListNode>> = None;
    for (i, &v) in vals.iter().enumerate().rev() {{
        if i as i32 == idx {{ continue; }}
        out = Some(Box::new(ListNode {{ val: v, next: out }}));
    }}
    out
}}
fn main() {{
    assert_eq!(to_vec(&remove_nth_from_end(build_list(&[1,2,3,4,5]), 2)), vec![1,2,3,5]);
    assert_eq!(to_vec(&remove_nth_from_end(build_list(&[1]), 1)), Vec::<i32>::new());
    assert_eq!(to_vec(&remove_nth_from_end(build_list(&[1,2]), 2)), vec![2]);
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
local function to_vec(h)
    local out = {}
    while h do out[#out + 1] = h.val; h = h.next end
    return out
end
local function remove_nth_from_end(head, n)
    local dummy = ListNode.new(0)
    dummy.next = head
    local fast, slow = dummy, dummy
    for _ = 1, n + 1 do fast = fast.next end
    while fast do
        fast = fast.next
        slow = slow.next
    end
    slow.next = slow.next.next
    return dummy.next
end
assert(table.concat(to_vec(remove_nth_from_end(build_list({1,2,3,4,5}), 2)), ",") == "1,2,3,5")
assert(#to_vec(remove_nth_from_end(build_list({1}), 1)) == 0)
assert(table.concat(to_vec(remove_nth_from_end(build_list({1,2}), 2)), ",") == "2")
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
    while (h) {{ if (i >= wn || h->val != want[i]) return 0; i++; h = h->next; }}
    return i == wn;
}}
static LNode *remove_nth_from_end(LNode *head, int n) {{
    LNode dummy = {{0, NULL}};
    dummy.next = head;
    LNode *fast = &dummy, *slow = &dummy;
    for (int i = 0; i <= n; i++) fast = fast->next;
    while (fast) {{ fast = fast->next; slow = slow->next; }}
    LNode *rm = slow->next;
    slow->next = rm->next;
    free(rm);
    return dummy.next;
}}
int main(void) {{
    int w1[] = {{1,2,3,5}}, w3[] = {{2}};
    LNode *r = remove_nth_from_end(build_list((int[]){{1,2,3,4,5}}, 5), 2);
    if (!list_check(r, w1, 4)) {{ printf("FAIL 1\\n"); return 1; }}
    free_list(r);
    LNode *r2 = remove_nth_from_end(build_list((int[]){{1}}, 1), 1);
    if (r2 != NULL) {{ printf("FAIL 2\\n"); return 1; }}
    LNode *r3 = remove_nth_from_end(build_list((int[]){{1,2}}, 2), 2);
    if (!list_check(r3, w3, 1)) {{ printf("FAIL 3\\n"); return 1; }}
    free_list(r3);
    printf("PASS\\n");
    return 0;
}}
''',
"cpp": '''#include <cassert>
#include <iostream>
#include <vector>
struct ListNode {
    int val;
    ListNode *next = nullptr;
    explicit ListNode(int v) : val(v) {}
};
static ListNode *buildList(const std::vector<int> &vals) {
    ListNode dummy(0);
    ListNode *cur = &dummy;
    for (int v : vals) {
        cur->next = new ListNode(v);
        cur = cur->next;
    }
    return dummy.next;
}
static void freeList(ListNode *h) { while (h) { ListNode *n = h->next; delete h; h = n; } }
static std::vector<int> toVec(ListNode *h) {
    std::vector<int> out;
    while (h) { out.push_back(h->val); h = h->next; }
    return out;
}
static ListNode *removeNthFromEnd(ListNode *head, int n) {
    ListNode dummy(0);
    dummy.next = head;
    ListNode *fast = &dummy, *slow = &dummy;
    for (int i = 0; i <= n; ++i) fast = fast->next;
    while (fast) { fast = fast->next; slow = slow->next; }
    ListNode *rm = slow->next;
    slow->next = rm->next;
    delete rm;
    return dummy.next;
}
int main() {
    ListNode *r = removeNthFromEnd(buildList({1, 2, 3, 4, 5}), 2);
    assert((toVec(r) == std::vector<int>{1, 2, 3, 5}));
    freeList(r);
    ListNode *r2 = removeNthFromEnd(buildList({1}), 1);
    assert(r2 == nullptr);
    ListNode *r3 = removeNthFromEnd(buildList({1, 2}), 2);
    assert((toVec(r3) == std::vector<int>{2}));
    freeList(r3);
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''ListNode <- function(val, nxt = NULL) {{ e <- new.env(parent = emptyenv()); e$val <- val; e$nxt <- nxt; class(e) <- "ListNode"; e }}
build_list <- function(vals) {{
  head <- NULL; cur <- NULL
  for (v in vals) {{
    n <- ListNode(v)
    if (is.null(head)) { head <- n; cur <- n } else { cur$nxt <- n; cur <- n }
  }}
  head
}}
to_vec <- function(h) {{ out <- integer(0); while (!is.null(h)) { out <- c(out, h$val); h <- h$nxt }; out }}
remove_nth_from_end <- function(head, n) {
  vals <- to_vec(head)
  idx <- length(vals) - n + 1
  if (idx >= 1) vals <- vals[-idx]
  out <- NULL; cur <- NULL
  for (v in vals) {
    nd <- ListNode(v)
    if (is.null(out)) { out <- nd; cur <- nd } else { cur$nxt <- nd; cur <- nd }
  }
  out
}
stopifnot(identical(to_vec(remove_nth_from_end(build_list(1:5), 2)), c(1L, 2L, 3L, 5L)))
stopifnot(length(to_vec(remove_nth_from_end(build_list(1L), 1L))) == 0)
stopifnot(identical(to_vec(remove_nth_from_end(build_list(c(1L, 2L)), 2L)), 2L))
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
fn toVec(h: ?*LNode, out: *std.ArrayList(i32)) void {
    var cur = h;
    while (cur) |n| { out.append(n.val) catch unreachable; cur = n.next; }
}
fn removeNthFromEnd(head: ?*LNode, n: i32) ?*LNode {
    // 重建法：zig 指针操作安全
    var vals: [4096]i32 = undefined;
    var len: usize = 0;
    var cur = head;
    while (cur) |node| {
        vals[len] = node.val;
        len += 1;
        cur = node.next;
    }
    const idx = len - @as(usize, @intCast(n));
    var out: ?*LNode = null;
    var tail: ?*LNode = null;
    for (0..len) |i| {
        if (i == idx) continue;
        const nd = std.heap.page_allocator.create(LNode) catch unreachable;
        nd.* = .{ .val = vals[i], .next = null };
        if (tail) |t| t.next = nd else out = nd;
        tail = nd;
    }
    return out;
}
pub fn main() !void {
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();
    const alloc = arena.allocator();
    var out = std.ArrayList(i32).init(std.heap.page_allocator);
    defer out.deinit();
    toVec(removeNthFromEnd(buildList(alloc, &[_]i32{ 1, 2, 3, 4, 5 }), 2), &out);
    if (out.items.len != 4 or out.items[3] != 5) return error.TestFailed;
    out.clearRetainingCapacity();
    if (removeNthFromEnd(buildList(alloc, &[_]i32{1}), 1) != null) return error.TestFailed;
    toVec(removeNthFromEnd(buildList(alloc, &[_]i32{ 1, 2 }), 2), &out);
    if (out.items.len != 1 or out.items[0] != 2) return error.TestFailed;
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
List<int> toVec(LNode? h) {
  final out = <int>[];
  while (h != null) {
    out.add(h.val);
    h = h.next;
  }
  return out;
}
LNode? removeNthFromEnd(LNode? head, int n) {
  final dummy = LNode(0);
  dummy.next = head;
  LNode? fast = dummy, slow = dummy;
  for (var i = 0; i <= n; i++) {
    fast = fast!.next;
  }
  while (fast != null) {
    fast = fast.next;
    slow = slow!.next;
  }
  slow!.next = slow.next!.next;
  return dummy.next;
}
void main() {
  if (toVec(removeNthFromEnd(buildList([1, 2, 3, 4, 5]), 2)).toString() != '[1, 2, 3, 5]') throw StateError('c1');
  if (removeNthFromEnd(buildList([1]), 1) != null) throw StateError('c2');
  if (toVec(removeNthFromEnd(buildList([1, 2]), 2)).toString() != '[2]') throw StateError('c3');
  print('PASS');
}
''',
}

PROBS = [
    ("lc_206_反转链表", A206, "LeetCode 206. 反转链表"),
    ("lc_876_链表的中间结点", A876, "LeetCode 876. 链表的中间结点"),
    ("lc_83_删除排序链表中的重复元素", A83, "LeetCode 83. 删除排序链表中的重复元素"),
    ("lc_237_删除链表中的节点", A237, "LeetCode 237. 删除链表中的节点"),
    ("lc_203_移除链表元素", A203, "LeetCode 203. 移除链表元素"),
    ("lc_19_删除链表的倒数第_n_个结点", A19, "LeetCode 19. 删除链表的倒数第N个结点"),
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
            body = algo[lang].replace("{{", "{").replace("}}", "}")
            emit(lang, f"linked_list/{prob}/{sol}.{ext}", head + "\n" + body)
            count += 1
print(f"emitted {count} files")
