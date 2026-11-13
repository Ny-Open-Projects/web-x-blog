#!/usr/bin/env python3
# gen_ll1.py — linked_list 第一批：141/142/160/19/203/206 × 7语言
import sys, os; sys.path.insert(0, "/Users/Wang/Code/github/web-x-blog/work/blog/courses/20.dsa/_tools")
from langlib import emit, head_comment, EXT

B = {"141": "133816714", "142": "133874671", "160": "133922762", "19": "133746567", "203": "133813394", "206": "133785568"}
LANGNAME = {"rust": "Rust", "lua": "Lua", "c": "C", "cpp": "C++", "r": "R", "zig": "Zig", "dart": "Dart"}

A141 = {
"rust": '''#[derive(Debug)]
struct ListNode {{ val: i32, next: Option<Box<ListNode>> }}
fn build_list(vals: &[i32]) -> Option<Box<ListNode>> {{
    let mut head: Option<Box<ListNode>> = None;
    for &v in vals.iter().rev() {{
        head = Some(Box::new(ListNode {{ val: v, next: head }}));
    }}
    head
}}
fn has_cycle(head: Option<&ListNode>) -> bool {{
    let mut slow = head;
    let mut fast = head;
    while let (Some(s), Some(f)) = (slow, fast) {{
        slow = s.next.as_deref();
        let f2 = match f.next.as_deref() {{ Some(x) => x, None => return false }};
        fast = match f2.next.as_deref() {{ Some(x) => Some(x), None => return false }};
        if let (Some(a), Some(b)) = (slow, fast) {{
            if std::ptr::eq(a, b) {{ return true; }}
        }}
    }}
    false
}}
fn main() {{
    let lst = build_list(&[3, 2, 0, -4]);
    let head = lst.as_deref();
    assert!(!has_cycle(head));
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
local function has_cycle(head)
    local slow, fast = head, head
    while fast and fast.next do
        slow = slow.next
        fast = fast.next.next
        if slow == fast then return true end
    end
    return false
end
assert(has_cycle(build_list({3, 2, 0, -4})) == false)
local h = build_list({1})
h.next = h
assert(has_cycle(h) == true)
assert(has_cycle(nil) == false)
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
static int has_cycle(LNode *head) {{
    LNode *slow = head, *fast = head;
    while (fast && fast->next) {{
        slow = slow->next;
        fast = fast->next->next;
        if (slow == fast) return 1;
    }}
    return 0;
}}
int main(void) {{
    LNode *l = build_list((int[]){{3,2,0,-4}}, 4);
    if (has_cycle(l)) {{ printf("FAIL 1\\n"); return 1; }}
    free_list(l);
    LNode *h = build_list((int[]){{1}}, 1);
    h->next = h;
    if (!has_cycle(h)) {{ printf("FAIL 2\\n"); return 1; }}
    free(h);
    if (has_cycle(NULL)) {{ printf("FAIL 3\\n"); return 1; }}
    printf("PASS\\n");
    return 0;
}}
''',
"cpp": '''#include <cassert>
#include <iostream>
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
static void freeList(ListNode *h) {
    while (h) { ListNode *n = h->next; delete h; h = n; }
}
static bool hasCycle(ListNode *head) {
    ListNode *slow = head, *fast = head;
    while (fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
        if (slow == fast) return true;
    }
    return false;
}
int main() {
    ListNode *l = buildList({3, 2, 0, -4});
    assert(!hasCycle(l));
    freeList(l);
    ListNode *h = buildList({1});
    h->next = h;
    assert(hasCycle(h));
    free(h);
    assert(!hasCycle(nullptr));
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
has_cycle <- function(head) {
  slow <- head; fast <- head
  while (!is.null(fast) && !is.null(fast$nxt)) {
    slow <- slow$nxt
    fast <- fast$nxt$nxt
    if (!is.null(slow) && identical(slow, fast)) return(TRUE)
  }
  FALSE
}
stopifnot(!has_cycle(build_list(c(3, 2, 0, -4))))
h <- build_list(c(1))
h$nxt <- h
stopifnot(has_cycle(h))
stopifnot(!has_cycle(NULL))
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
fn hasCycle(head: ?*LNode) bool {
    var slow = head;
    var fast = head;
    while (fast != null and fast.?.next != null) {
        slow = slow.?.next;
        fast = fast.?.next.?.next;
        if (slow != null and fast != null and slow.? == fast.?) return true;
    }
    return false;
}
pub fn main() !void {
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();
    const alloc = arena.allocator();
    if (hasCycle(buildList(alloc, &[_]i32{ 3, 2, 0, -4 }))) return error.TestFailed;
    const h = buildList(alloc, &[_]i32{1}).?;
    h.next = h;
    if (!hasCycle(h)) return error.TestFailed;
    if (hasCycle(null)) return error.TestFailed;
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
bool hasCycle(LNode? head) {
  LNode? slow = head, fast = head;
  while (fast != null && fast.next != null) {
    slow = slow!.next;
    fast = fast.next!.next;
    if (identical(slow, fast)) return true;
  }
  return false;
}
void main() {
  if (hasCycle(buildList([3, 2, 0, -4]))) throw StateError('c1');
  final h = buildList([1])!;
  h.next = h;
  if (!hasCycle(h)) throw StateError('c2');
  if (hasCycle(null)) throw StateError('c3');
  print('PASS');
}
''',
}

A142 = {
"rust": '''#[derive(Debug)]
struct ListNode {{ val: i32, next: Option<Box<ListNode>> }}
fn detect_cycle(mut head: Option<&ListNode>) -> Option<i32> {{
    let mut slow = head;
    let mut fast = head;
    while let (Some(s), Some(f)) = (slow, fast) {{
        slow = s.next.as_deref();
        let f2 = f.next.as_deref()?;
        fast = f2.next.as_deref();
        if let (Some(a), Some(b)) = (slow, fast) {{
            if std::ptr::eq(a, b) {{
                let mut p1 = head;
                let mut p2 = slow;
                loop {{
                    let (x, y) = (p1?, p2?);
                    if std::ptr::eq(x, y) {{ return Some(x.val); }}
                    p1 = x.next.as_deref();
                    p2 = y.next.as_deref();
                }}
            }}
        }}
    }}
    None
}}
fn main() {{
    assert_eq!(detect_cycle(None), None);
    println!("PASS");
}}
''',
"lua": '''local ListNode = {}
ListNode.__index = ListNode
function ListNode.new(val, next) return setmetatable({val = val, next = next}, ListNode) end
local function detect_cycle(head)
    local slow, fast = head, head
    while fast and fast.next do
        slow = slow.next
        fast = fast.next.next
        if slow == fast then
            local p1, p2 = head, slow
            while p1 ~= p2 do
                p1 = p1.next
                p2 = p2.next
            end
            return p1
        end
    end
    return nil
end
local function build_with_cycle(vals, pos)
    local head, cur, tail_at = nil, nil, nil
    for i, v in ipairs(vals) do
        local n = ListNode.new(v)
        if not head then head, cur = n, n else cur.next, cur = n, n end
        if i == pos then tail_at = n end
    end
    if cur and tail_at then cur.next = tail_at end
    return head
end
local h = build_with_cycle({3, 2, 0, -4}, 2)
assert(detect_cycle(h) ~= nil and detect_cycle(h).val == 2)
assert(detect_cycle(ListNode.new(1)) == nil)
print("PASS")
''',
"c": '''#include <stdio.h>
#include <stdlib.h>
typedef struct LNode {{ int val; struct LNode *next; }} LNode;
static LNode *build_with_cycle(const int *vals, int n, int pos) {{
    LNode *head = NULL, **cur = &head, *tail_at = NULL;
    for (int i = 0; i < n; i++) {{
        LNode *node = malloc(sizeof(LNode));
        node->val = vals[i]; node->next = NULL;
        *cur = node; cur = &node->next;
        if (i + 1 == pos) tail_at = node;
    }}
    if (*cur == NULL) {}
    LNode *tail = head;
    while (tail && tail->next) tail = tail->next;
    if (tail && tail_at) tail->next = tail_at;
    return head;
}}
static LNode *detect_cycle(LNode *head) {{
    LNode *slow = head, *fast = head;
    while (fast && fast->next) {{
        slow = slow->next;
        fast = fast->next->next;
        if (slow == fast) {{
            LNode *p1 = head, *p2 = slow;
            while (p1 != p2) { p1 = p1->next; p2 = p2->next; }
            return p1;
        }}
    }}
    return NULL;
}}
int main(void) {{
    LNode *h = build_with_cycle((int[]){{3,2,0,-4}}, 4, 2);
    LNode *e = detect_cycle(h);
    if (!e || e->val != 2) {{ printf("FAIL 1\\n"); return 1; }}
    LNode *s = malloc(sizeof(LNode)); s->val = 1; s->next = NULL;
    if (detect_cycle(s)) {{ printf("FAIL 2\\n"); return 1; }}
    printf("PASS\\n");
    return 0;
}}
''',
"cpp": '''#include <cassert>
#include <iostream>
struct ListNode {
    int val;
    ListNode *next = nullptr;
    explicit ListNode(int v) : val(v) {}
};
static ListNode *buildWithCycle(const std::vector<int> &vals, int pos) {
    ListNode dummy(0);
    ListNode *cur = &dummy;
    ListNode *tailAt = nullptr;
    for (size_t i = 0; i < vals.size(); ++i) {
        cur->next = new ListNode(vals[i]);
        cur = cur->next;
        if (static_cast<int>(i) + 1 == pos) tailAt = cur;
    }
    if (tailAt) cur->next = tailAt;
    return dummy.next;
}
static ListNode *detectCycle(ListNode *head) {
    ListNode *slow = head, *fast = head;
    while (fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
        if (slow == fast) {
            ListNode *p1 = head, *p2 = slow;
            while (p1 != p2) { p1 = p1->next; p2 = p2->next; }
            return p1;
        }
    }
    return nullptr;
}
int main() {
    ListNode *h = buildWithCycle({3, 2, 0, -4}, 2);
    ListNode *e = detectCycle(h);
    assert(e != nullptr && e->val == 2);
    ListNode *s = new ListNode(1);
    assert(detectCycle(s) == nullptr);
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''ListNode <- function(val, nxt = NULL) {{ e <- new.env(parent = emptyenv()); e$val <- val; e$nxt <- nxt; class(e) <- "ListNode"; e }}
build_with_cycle <- function(vals, pos) {
  head <- NULL; cur <- NULL; tail_at <- NULL
  for (i in seq_along(vals)) {
    n <- ListNode(vals[i])
    if (is.null(head)) { head <- n; cur <- n } else { cur$nxt <- n; cur <- n }
    if (i == pos) tail_at <- n
  }
  if (!is.null(tail_at)) cur$nxt <- tail_at
  head
}
detect_cycle <- function(head) {
  slow <- head; fast <- head
  while (!is.null(fast) && !is.null(fast$nxt)) {
    slow <- slow$nxt
    fast <- fast$nxt$nxt
    if (!is.null(slow) && identical(slow, fast)) {
      p1 <- head; p2 <- slow
      while (!identical(p1, p2)) { p1 <- p1$nxt; p2 <- p2$nxt }
      return(p1)
    }
  }
  NULL
}
h <- build_with_cycle(c(3, 2, 0, -4), 2)
stopifnot(!is.null(detect_cycle(h)), detect_cycle(h)$val == 2)
stopifnot(is.null(detect_cycle(ListNode(1))))
cat("PASS\\n")
''',
"zig": '''const std = @import("std");
const LNode = struct { val: i32, next: ?*LNode };
fn buildWithCycle(alloc: std.mem.Allocator, vals: []const i32, pos: usize) ?*LNode {
    var head: ?*LNode = null;
    var tail: ?*LNode = null;
    var tailAt: ?*LNode = null;
    for (vals, 0..) |v, i| {
        const n = alloc.create(LNode) catch unreachable;
        n.* = .{ .val = v, .next = null };
        if (tail) |t| t.next = n else head = n;
        tail = n;
        if (i + 1 == pos) tailAt = n;
    }
    if (tail) |t| t.next = tailAt;
    return head;
}
fn detectCycle(head: ?*LNode) ?*LNode {
    var slow = head;
    var fast = head;
    while (fast != null and fast.?.next != null) {
        slow = slow.?.next;
        fast = fast.?.next.?.next;
        if (slow != null and fast != null and slow.? == fast.?) {
            var p1 = head;
            var p2 = slow;
            while (p1 != null and p2 != null and p1.? != p2.?) {
                p1 = p1.?.next;
                p2 = p2.?.next;
            }
            return p1;
        }
    }
    return null;
}
pub fn main() !void {
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();
    const alloc = arena.allocator();
    const h = buildWithCycle(alloc, &[_]i32{ 3, 2, 0, -4 }, 2);
    const e = detectCycle(h);
    if (e == null or e.?.val != 2) return error.TestFailed;
    const s = try alloc.create(LNode);
    s.* = .{ .val = 1, .next = null };
    if (detectCycle(s) != null) return error.TestFailed;
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''class LNode {
  final int val;
  LNode? next;
  LNode(this.val);
}
LNode? buildWithCycle(List<int> vals, int pos) {
  LNode? head;
  LNode? cur;
  LNode? tailAt;
  for (var i = 0; i < vals.length; i++) {
    final n = LNode(vals[i]);
    if (head == null) {
      head = n;
    } else {
      cur!.next = n;
    }
    cur = n;
    if (i + 1 == pos) tailAt = n;
  }
  if (tailAt != null) cur!.next = tailAt;
  return head;
}
LNode? detectCycle(LNode? head) {
  LNode? slow = head, fast = head;
  while (fast != null && fast.next != null) {
    slow = slow!.next;
    fast = fast.next!.next;
    if (identical(slow, fast)) {
      LNode? p1 = head;
      LNode? p2 = slow;
      while (!identical(p1, p2)) {
        p1 = p1!.next;
        p2 = p2!.next;
      }
      return p1;
    }
  }
  return null;
}
void main() {
  final h = buildWithCycle([3, 2, 0, -4], 2);
  final e = detectCycle(h);
  if (e == null || e.val != 2) throw StateError('c1');
  if (detectCycle(LNode(1)) != null) throw StateError('c2');
  print('PASS');
}
''',
}

A160 = {
"rust": '''#[derive(Debug)]
struct ListNode {{ val: i32, next: Option<Box<ListNode>> }}
fn get_intersection_node<'a>(a: Option<&'a ListNode>, b: Option<&'a ListNode>) -> Option<&'a ListNode> {{
    let (mut p1, mut p2) = (a, b);
    loop {{
        match (p1, p2) {{
            (None, None) => return None,
            (Some(x), Some(y)) if std::ptr::eq(x, y) => return Some(x),
            _ => {{
                p1 = match p1 {{ Some(x) => x.next.as_deref(), None => b }};
                p2 = match p2 {{ Some(y) => y.next.as_deref(), None => a }};
            }}
        }}
    }}
}}
fn main() {{
    assert!(get_intersection_node(None, None).is_none());
    println!("PASS");
}}
''',
"lua": '''local ListNode = {}
ListNode.__index = ListNode
function ListNode.new(val, next) return setmetatable({val = val, next = next}, ListNode) end
local function get_intersection_node(headA, headB)
    if not headA or not headB then return nil end
    local p1, p2 = headA, headB
    while p1 ~= p2 do
        if p1 then p1 = p1.next else p1 = headB end
        if p2 then p2 = p2.next else p2 = headA end
    end
    return p1
end
local shared = ListNode.new(8, ListNode.new(4, ListNode.new(5)))
local a = ListNode.new(4, ListNode.new(1, shared))
local b = ListNode.new(5, ListNode.new(6, ListNode.new(1, shared)))
assert(get_intersection_node(a, b) == shared)
assert(get_intersection_node(ListNode.new(1), ListNode.new(1)) == nil)
assert(get_intersection_node(nil, nil) == nil)
print("PASS")
''',
"c": '''#include <stdio.h>
#include <stdlib.h>
typedef struct LNode {{ int val; struct LNode *next; }} LNode;
static LNode *nnew(int v) {{ LNode *n = malloc(sizeof(LNode)); n->val = v; n->next = NULL; return n; }}
static LNode *get_intersection_node(LNode *a, LNode *b) {{
    if (!a || !b) return NULL;
    LNode *p1 = a, *p2 = b;
    while (p1 != p2) {{
        p1 = p1 ? p1->next : b;
        p2 = p2 ? p2->next : a;
    }}
    return p1;
}}
int main(void) {{
    LNode *shared = nnew(8);
    shared->next = nnew(4);
    shared->next->next = nnew(5);
    LNode *a = nnew(4);
    a->next = nnew(1);
    a->next->next = shared;
    LNode *b = nnew(5);
    b->next = nnew(6);
    b->next->next = nnew(1);
    b->next->next->next = shared;
    if (get_intersection_node(a, b) != shared) {{ printf("FAIL 1\\n"); return 1; }}
    if (get_intersection_node(nnew(1), nnew(1)) != NULL) {{ printf("FAIL 2\\n"); return 1; }}
    if (get_intersection_node(NULL, NULL) != NULL) {{ printf("FAIL 3\\n"); return 1; }}
    printf("PASS\\n");
    return 0;
}}
''',
"cpp": '''#include <cassert>
#include <iostream>
struct ListNode {
    int val;
    ListNode *next = nullptr;
    explicit ListNode(int v) : val(v) {}
};
static ListNode *getIntersectionNode(ListNode *a, ListNode *b) {
    if (!a || !b) return nullptr;
    ListNode *p1 = a, *p2 = b;
    while (p1 != p2) {
        p1 = p1 ? p1->next : b;
        p2 = p2 ? p2->next : a;
    }
    return p1;
}
int main() {
    ListNode *shared = new ListNode(8);
    shared->next = new ListNode(4);
    shared->next->next = new ListNode(5);
    ListNode *a = new ListNode(4);
    a->next = new ListNode(1);
    a->next->next = shared;
    ListNode *b = new ListNode(5);
    b->next = new ListNode(6);
    b->next->next = new ListNode(1);
    b->next->next->next = shared;
    assert(getIntersectionNode(a, b) == shared);
    assert(getIntersectionNode(new ListNode(1), new ListNode(1)) == nullptr);
    assert(getIntersectionNode(nullptr, nullptr) == nullptr);
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''ListNode <- function(val, nxt = NULL) {{ e <- new.env(parent = emptyenv()); e$val <- val; e$nxt <- nxt; class(e) <- "ListNode"; e }}
get_intersection_node <- function(headA, headB) {
  if (is.null(headA) || is.null(headB)) return(NULL)
  p1 <- headA; p2 <- headB
  while (!identical(p1, p2)) {
    p1 <- if (!is.null(p1)) p1$nxt else headB
    p2 <- if (!is.null(p2)) p2$nxt else headA
  }
  p1
}
shared <- ListNode(8, ListNode(4, ListNode(5)))
a <- ListNode(4, ListNode(1, shared))
b <- ListNode(5, ListNode(6, ListNode(1, shared)))
stopifnot(identical(get_intersection_node(a, b), shared))
stopifnot(is.null(get_intersection_node(ListNode(1), ListNode(1))))
stopifnot(is.null(get_intersection_node(NULL, NULL)))
cat("PASS\\n")
''',
"zig": '''const std = @import("std");
const LNode = struct { val: i32, next: ?*LNode };
fn getIntersectionNode(a: ?*LNode, b: ?*LNode) ?*LNode {
    if (a == null or b == null) return null;
    var p1 = a;
    var p2 = b;
    while (p1 != p2) {
        p1 = if (p1) |x| x.next else b;
        p2 = if (p2) |y| y.next else a;
    }
    return p1;
}
pub fn main() !void {
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();
    const alloc = arena.allocator();
    const shared = try alloc.create(LNode);
    shared.* = .{ .val = 8, .next = null };
    const n4 = try alloc.create(LNode);
    n4.* = .{ .val = 4, .next = null };
    shared.next = n4;
    const n5 = try alloc.create(LNode);
    n5.* = .{ .val = 5, .next = null };
    n4.next = n5;
    const a1 = try alloc.create(LNode);
    a1.* = .{ .val = 4, .next = null };
    const a2 = try alloc.create(LNode);
    a2.* = .{ .val = 1, .next = shared };
    a1.next = a2;
    const b1 = try alloc.create(LNode);
    b1.* = .{ .val = 5, .next = null };
    const b2 = try alloc.create(LNode);
    b2.* = .{ .val = 6, .next = null };
    b1.next = b2;
    const b3 = try alloc.create(LNode);
    b3.* = .{ .val = 1, .next = shared };
    b2.next = b3;
    if (getIntersectionNode(a1, b1) != shared) return error.TestFailed;
    const x = try alloc.create(LNode);
    x.* = .{ .val = 1, .next = null };
    const y = try alloc.create(LNode);
    y.* = .{ .val = 1, .next = null };
    if (getIntersectionNode(x, y) != null) return error.TestFailed;
    if (getIntersectionNode(null, null) != null) return error.TestFailed;
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''class LNode {
  final int val;
  LNode? next;
  LNode(this.val);
}
LNode? getIntersectionNode(LNode? a, LNode? b) {
  if (a == null || b == null) return null;
  LNode? p1 = a, p2 = b;
  while (!identical(p1, p2)) {
    p1 = p1 != null ? p1.next : b;
    p2 = p2 != null ? p2.next : a;
  }
  return p1;
}
void main() {
  final shared = LNode(8);
  shared.next = LNode(4)..next = LNode(5);
  final a = LNode(4)..next = LNode(1)..next = shared;
  final b = LNode(5)..next = LNode(6)..next = LNode(1)..next = shared;
  if (!identical(getIntersectionNode(a, b), shared)) throw StateError('c1');
  if (getIntersectionNode(LNode(1), LNode(1)) != null) throw StateError('c2');
  if (getIntersectionNode(null, null) != null) throw StateError('c3');
  print('PASS');
}
''',
}

PROBS = [
    ("lc_141_环形链表", A141, "LeetCode 141. 环形链表"),
    ("lc_142_环形链表_ii", A142, "LeetCode 142. 环形链表II"),
    ("lc_160_相交链表", A160, "LeetCode 160. 相交链表"),
]
count = 0
for prob, algo, title in PROBS:
    bid = B[prob.split("_")[1]]
    ts_dir = f"/Users/Wang/Code/github/web-x-blog/work/blog/courses/20.dsa/ts/linked_list/{prob}"
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
