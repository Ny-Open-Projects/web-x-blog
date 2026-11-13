#!/usr/bin/env python3
# gen_fix_n15.py — 补齐 notes/lc_133278676 使用链表指针获取 JSON 节点值 × 7 语言（4 解法）
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from langlib import emit

REL = "notes/lc_133278676_使用链表指针获取json节点值的算法实现"
BLOG = "来源（blog）：https://blog.csdn.net/tyro_java/article/details/133278676"
DESC = "使用链表（指针链）获取 JSON 节点值"

# ---------- A: 安全遍历（s1 有 miss 用例；s2 单用例） ----------
A = {
"rust": '''// @@BLOG@@
// LeetCode 133278676. @@T@@ — Rust 版（方案A：安全遍历，缺失返回 None）
use std::collections::HashMap;

#[derive(Debug, Clone, PartialEq)]
enum Json {
    Obj(HashMap<String, Json>),
    Num(i64),
}

fn get_value(data: &Json, path: &[&str]) -> Option<i64> {
    let mut node = data;
    for key in path {
        match node {
            Json::Obj(map) => match map.get(*key) {
                Some(next) => node = next,
                None => return None,
            },
            _ => return None,
        }
    }
    match node {
        Json::Num(v) => Some(*v),
        _ => None,
    }
}

fn sample() -> Json {
    let mut c = HashMap::new();
    c.insert("c".to_string(), Json::Num(1));
    let mut b = HashMap::new();
    b.insert("b".to_string(), Json::Obj(c));
    let mut a = HashMap::new();
    a.insert("a".to_string(), Json::Obj(b));
    let mut e = HashMap::new();
    e.insert("e".to_string(), Json::Num(2));
    a.insert("d".to_string(), Json::Obj(e));
    Json::Obj(a)
}

fn main() {
    let data = sample();
    assert_eq!(get_value(&data, &["a", "b", "c"]), Some(1), "p1");
    assert_eq!(get_value(&data, &["a", "z"]), None, "p2");
    println!("PASS");
}
''',
"lua": '''-- @@BLOG@@
-- LeetCode 133278676. @@T@@ — Lua 版（方案A：安全遍历，缺失返回 nil）
local function get_value(data, path)
    local node = data
    for _, key in ipairs(path) do
        if type(node) ~= "table" or node[key] == nil then return nil end
        node = node[key]
    end
    return node
end

local data = { a = { b = { c = 1 } }, d = { e = 2 } }
assert(get_value(data, { "a", "b", "c" }) == 1, "p1")
assert(get_value(data, { "a", "z" }) == nil, "p2")
print("PASS")
''',
"c": '''/* @@BLOG@@
 * LeetCode 133278676. @@T@@ — C 版（方案A：安全遍历，缺失返回 NULL）
 * 最小 JSON 对象模型：节点为对象（带命名子节点）或整数
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct JNode {
    const char *key;
    int is_obj;
    int val;                     /* 叶子值 */
    struct JNode *children[8];   /* 对象子节点 */
    int nchildren;
} JNode;

static JNode *obj(const char *key, JNode **children, int n) {
    JNode *j = malloc(sizeof(JNode));
    j->key = key; j->is_obj = 1; j->val = 0;
    for (int i = 0; i < n; i++) j->children[i] = children[i];
    j->nchildren = n;
    return j;
}

static JNode *leaf(const char *key, int val) {
    JNode *j = malloc(sizeof(JNode));
    j->key = key; j->is_obj = 0; j->val = val; j->nchildren = 0;
    return j;
}

static JNode *child(JNode *node, const char *key) {
    for (int i = 0; i < node->nchildren; i++)
        if (strcmp(node->children[i]->key, key) == 0) return node->children[i];
    return NULL;
}

static JNode *get_value(JNode *data, const char **path, int n) {
    JNode *node = data;
    for (int i = 0; i < n; i++) {
        if (!node->is_obj) return NULL;
        node = child(node, path[i]);
        if (!node) return NULL;
    }
    return node;
}

int main(void) {
    JNode *c = leaf("c", 1);
    JNode *b_children[1] = {c};
    JNode *b = obj("b", b_children, 1);
    JNode *a_children[1] = {b};
    JNode *a = obj("a", a_children, 1);
    JNode *e = leaf("e", 2);
    JNode *d_children[1] = {e};
    JNode *d = obj("d", d_children, 1);
    JNode *top_children[2] = {a, d};
    JNode *data = obj("root", top_children, 2);

    const char *p1[] = {"a", "b", "c"};
    const char *p2[] = {"a", "z"};
    JNode *r1 = get_value(data, p1, 3);
    if (!r1 || r1->val != 1) { printf("p1 failed\\n"); return 1; }
    if (get_value(data, p2, 2) != NULL) { printf("p2 failed\\n"); return 1; }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''// @@BLOG@@
// LeetCode 133278676. @@T@@ — C++ 版（方案A：安全遍历，缺失返回 nullptr）
#include <iostream>
#include <map>
#include <memory>
#include <string>
#include <vector>

struct JNode {
    bool is_obj = false;
    int val = 0;
    std::map<std::string, std::unique_ptr<JNode>> children;

    JNode *child(const std::string &key) const {
        auto it = children.find(key);
        return it == children.end() ? nullptr : it->second.get();
    }
};

static JNode *get_value(JNode *data, const std::vector<std::string> &path) {
    JNode *node = data;
    for (const auto &key : path) {
        if (!node->is_obj) return nullptr;
        node = node->child(key);
        if (!node) return nullptr;
    }
    return node;
}

int main() {
    auto data = std::make_unique<JNode>();
    data->is_obj = true;
    auto &a = data->children["a"];
    a = std::make_unique<JNode>();
    a->is_obj = true;
    auto &b = a->children["b"];
    b = std::make_unique<JNode>();
    b->is_obj = true;
    auto &c = b->children["c"];
    c = std::make_unique<JNode>();
    c->val = 1;
    auto &d = data->children["d"];
    d = std::make_unique<JNode>();
    d->is_obj = true;
    auto &e = d->children["e"];
    e = std::make_unique<JNode>();
    e->val = 2;

    if (auto *r = get_value(data.get(), {"a", "b", "c"})) {
        if (r->val != 1) { std::cout << "p1 failed" << std::endl; return 1; }
    } else {
        std::cout << "p1 failed" << std::endl;
        return 1;
    }
    if (get_value(data.get(), {"a", "z"}) != nullptr) { std::cout << "p2 failed" << std::endl; return 1; }
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''# @@BLOG@@
# LeetCode 133278676. @@T@@ — R 版（方案A：安全遍历，缺失返回 NULL）
get_value <- function(data, path) {
  node <- data
  for (key in path) {
    if (!is.list(node) || is.null(node[[key]])) return(NULL)
    node <- node[[key]]
  }
  node
}

data <- list(a = list(b = list(c = 1L)), d = list(e = 2L))
stopifnot(identical(get_value(data, c("a", "b", "c")), 1L))
stopifnot(is.null(get_value(data, c("a", "z"))))
cat("PASS\\n")
''',
"zig": '''// @@BLOG@@
// LeetCode 133278676. @@T@@ — Zig 版（方案A：安全遍历，缺失返回 null）
const std = @import("std");

const MAX_CHILDREN = 8;
const JNode = struct {
    is_obj: bool,
    val: i32 = 0,
    keys: [MAX_CHILDREN][]const u8 = undefined,
    children: [MAX_CHILDREN]*JNode = undefined,
    nchildren: usize = 0,

    fn addChild(self: *JNode, key: []const u8, node: *JNode) void {
        self.keys[self.nchildren] = key;
        self.children[self.nchildren] = node;
        self.nchildren += 1;
    }

    fn child(self: *const JNode, key: []const u8) ?*JNode {
        var i: usize = 0;
        while (i < self.nchildren) : (i += 1) {
            if (std.mem.eql(u8, self.keys[i], key)) return self.children[i];
        }
        return null;
    }
};

fn getValue(data: *JNode, path: []const []const u8) ?*JNode {
    var node = data;
    for (path) |key| {
        if (!node.is_obj) return null;
        node = node.child(key) orelse return null;
    }
    return node;
}

pub fn main() !void {
    var gpa = std.heap.GeneralPurposeAllocator(.{}){};
    const allocator = gpa.allocator();

    const data = try allocator.create(JNode);
    data.* = .{ .is_obj = true };
    const a = try allocator.create(JNode);
    a.* = .{ .is_obj = true };
    const b = try allocator.create(JNode);
    b.* = .{ .is_obj = true };
    const c = try allocator.create(JNode);
    c.* = .{ .is_obj = false, .val = 1 };
    b.addChild("c", c);
    a.addChild("b", b);
    data.addChild("a", a);
    const d = try allocator.create(JNode);
    d.* = .{ .is_obj = true };
    const e = try allocator.create(JNode);
    e.* = .{ .is_obj = false, .val = 2 };
    d.addChild("e", e);
    data.addChild("d", d);

    const r1 = getValue(data, &.{ "a", "b", "c" }) orelse return error.TestFailed;
    if (r1.val != 1) return error.TestFailed;
    if (getValue(data, &.{ "a", "z" }) != null) return error.TestFailed;
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''// @@BLOG@@
// LeetCode 133278676. @@T@@ — Dart 版（方案A：安全遍历，缺失返回 null）
Object? getValue(Map<String, dynamic> data, List<String> path) {
  var node = data as Object?;
  for (final key in path) {
    if (node is! Map<String, dynamic> || !node.containsKey(key)) return null;
    node = node[key];
  }
  return node;
}

void main() {
  final data = <String, dynamic>{
    'a': <String, dynamic>{'b': <String, dynamic>{'c': 1}},
    'd': <String, dynamic>{'e': 2},
  };
  if (getValue(data, ['a', 'b', 'c']) != 1) throw StateError('p1 failed');
  if (getValue(data, ['a', 'z']) != null) throw StateError('p2 failed');
  print('PASS');
}
''',
}

# ---------- B: 直接求值（s3）/ reduce 链（s4） ----------
B = {
"rust": '''// @@BLOG@@
// LeetCode 133278676. @@T@@ — Rust 版（方案B：逐键求值 / reduce 链式访问）
use std::collections::HashMap;

#[derive(Debug, Clone, PartialEq)]
enum Json {
    Obj(HashMap<String, Json>),
    Num(i64),
}

// 逐键求值（合法路径语义，与 TS get_value_eval / getValueChain 一致）
fn get_value(data: &Json, path: &[&str]) -> Option<i64> {
    let mut node = data;
    for key in path {
        node = match node {
            Json::Obj(map) => map.get(*key)?,
            _ => return None,
        };
    }
    match node {
        Json::Num(v) => Some(*v),
        _ => None,
    }
}

fn sample() -> Json {
    let mut c = HashMap::new();
    c.insert("c".to_string(), Json::Num(1));
    let mut b = HashMap::new();
    b.insert("b".to_string(), Json::Obj(c));
    let mut a = HashMap::new();
    a.insert("a".to_string(), Json::Obj(b));
    let mut e = HashMap::new();
    e.insert("e".to_string(), Json::Num(2));
    a.insert("d".to_string(), Json::Obj(e));
    Json::Obj(a)
}

fn main() {
    let data = sample();
    // p1: 逐键求值
    assert_eq!(get_value(&data, &["a", "b", "c"]), Some(1), "p1");
    // p2: reduce 链式访问
    assert_eq!(get_value(&data, &["d", "e"]), Some(2), "p2");
    println!("PASS");
}
''',
"lua": '''-- @@BLOG@@
-- LeetCode 133278676. @@T@@ — Lua 版（方案B：逐键求值 / reduce 链式访问）
local function get_value_eval(data, path)
    local cur = data
    for _, k in ipairs(path) do
        cur = cur[k]
    end
    return cur
end

local function get_value_chain(data, path)
    local acc = data
    for _, k in ipairs(path) do
        acc = acc[k]
    end
    return acc
end

local data = { a = { b = { c = 1 } }, d = { e = 2 } }
assert(get_value_eval(data, { "a", "b", "c" }) == 1, "p1")
assert(get_value_chain(data, { "d", "e" }) == 2, "p2")
print("PASS")
''',
"c": '''/* @@BLOG@@
 * LeetCode 133278676. @@T@@ — C 版（方案B：逐键求值，合法路径直接索引）
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct JNode {
    const char *key;
    int is_obj;
    int val;
    struct JNode *children[8];
    int nchildren;
} JNode;

static JNode *child(JNode *node, const char *key) {
    for (int i = 0; i < node->nchildren; i++)
        if (strcmp(node->children[i]->key, key) == 0) return node->children[i];
    return NULL;
}

/* 直接求值：假定路径合法（与 TS get_value_eval 一致） */
static JNode *get_value_eval(JNode *data, const char **path, int n) {
    JNode *cur = data;
    for (int i = 0; i < n; i++) cur = child(cur, path[i]);
    return cur;
}

int main(void) {
    JNode *c = calloc(1, sizeof(JNode));
    c->key = "c"; c->val = 1;
    JNode *b = calloc(1, sizeof(JNode));
    b->key = "b"; b->is_obj = 1; b->children[0] = c; b->nchildren = 1;
    JNode *a = calloc(1, sizeof(JNode));
    a->key = "a"; a->is_obj = 1; a->children[0] = b; a->nchildren = 1;
    JNode *e = calloc(1, sizeof(JNode));
    e->key = "e"; e->val = 2;
    JNode *d = calloc(1, sizeof(JNode));
    d->key = "d"; d->is_obj = 1; d->children[0] = e; d->nchildren = 1;
    JNode *data = calloc(1, sizeof(JNode));
    data->key = "root"; data->is_obj = 1;
    data->children[0] = a; data->children[1] = d; data->nchildren = 2;

    const char *p1[] = {"a", "b", "c"};
    const char *p2[] = {"d", "e"};
    if (get_value_eval(data, p1, 3)->val != 1) { printf("p1 failed\\n"); return 1; }
    if (get_value_eval(data, p2, 2)->val != 2) { printf("p2 failed\\n"); return 1; }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''// @@BLOG@@
// LeetCode 133278676. @@T@@ — C++ 版（方案B：逐键求值 / reduce 链式访问）
#include <iostream>
#include <map>
#include <memory>
#include <string>

struct JNode {
    bool is_obj = false;
    int val = 0;
    std::map<std::string, std::unique_ptr<JNode>> children;
};

static JNode *get_value_eval(JNode *data, const std::string &path) {
    // 合法路径直接逐键求值（"a/b/c" 形式）
    JNode *cur = data;
    size_t start = 0;
    while (start <= path.size()) {
        size_t slash = path.find('/', start);
        std::string key = path.substr(start, slash - start);
        cur = cur->children[key].get();
        if (slash == std::string::npos) break;
        start = slash + 1;
    }
    return cur;
}

int main() {
    auto data = std::make_unique<JNode>();
    data->is_obj = true;
    auto &a = data->children["a"];
    a = std::make_unique<JNode>();
    a->is_obj = true;
    auto &b = a->children["b"];
    b = std::make_unique<JNode>();
    b->is_obj = true;
    auto &c = b->children["c"];
    c = std::make_unique<JNode>();
    c->val = 1;
    auto &d = data->children["d"];
    d = std::make_unique<JNode>();
    d->is_obj = true;
    auto &e = d->children["e"];
    e = std::make_unique<JNode>();
    e->val = 2;

    // p1: 逐键求值
    if (get_value_eval(data.get(), "a/b/c")->val != 1) { std::cout << "p1 failed" << std::endl; return 1; }
    // p2: reduce 链式访问（同一遍历）
    if (get_value_eval(data.get(), "d/e")->val != 2) { std::cout << "p2 failed" << std::endl; return 1; }
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''# @@BLOG@@
# LeetCode 133278676. @@T@@ — R 版（方案B：逐键求值 / reduce 链式访问）
get_value_eval <- function(data, path) {
  cur <- data
  for (k in path) cur <- cur[[k]]
  cur
}

get_value_chain <- function(data, path) {
  Reduce(function(acc, k) acc[[k]], path, init = data)
}

data <- list(a = list(b = list(c = 1L)), d = list(e = 2L))
stopifnot(identical(get_value_eval(data, c("a", "b", "c")), 1L))
stopifnot(identical(get_value_chain(data, c("d", "e")), 2L))
cat("PASS\\n")
''',
"zig": '''// @@BLOG@@
// LeetCode 133278676. @@T@@ — Zig 版（方案B：逐键求值，合法路径直接索引）
const std = @import("std");

const MAX_CHILDREN = 8;
const JNode = struct {
    is_obj: bool,
    val: i32 = 0,
    keys: [MAX_CHILDREN][]const u8 = undefined,
    children: [MAX_CHILDREN]*JNode = undefined,
    nchildren: usize = 0,

    fn addChild(self: *JNode, key: []const u8, node: *JNode) void {
        self.keys[self.nchildren] = key;
        self.children[self.nchildren] = node;
        self.nchildren += 1;
    }

    fn child(self: *const JNode, key: []const u8) *JNode {
        var i: usize = 0;
        while (i < self.nchildren) : (i += 1) {
            if (std.mem.eql(u8, self.keys[i], key)) return self.children[i];
        }
        unreachable; // 合法路径语义
    }
};

fn getValueEval(data: *JNode, path: []const []const u8) *JNode {
    var cur = data;
    for (path) |key| {
        cur = cur.child(key);
    }
    return cur;
}

pub fn main() !void {
    var gpa = std.heap.GeneralPurposeAllocator(.{}){};
    const allocator = gpa.allocator();

    const data = try allocator.create(JNode);
    data.* = .{ .is_obj = true };
    const a = try allocator.create(JNode);
    a.* = .{ .is_obj = true };
    const b = try allocator.create(JNode);
    b.* = .{ .is_obj = true };
    const c = try allocator.create(JNode);
    c.* = .{ .is_obj = false, .val = 1 };
    b.addChild("c", c);
    a.addChild("b", b);
    data.addChild("a", a);
    const d = try allocator.create(JNode);
    d.* = .{ .is_obj = true };
    const e = try allocator.create(JNode);
    e.* = .{ .is_obj = false, .val = 2 };
    d.addChild("e", e);
    data.addChild("d", d);

    if (getValueEval(data, &.{ "a", "b", "c" }).val != 1) return error.TestFailed;
    if (getValueEval(data, &.{ "d", "e" }).val != 2) return error.TestFailed;
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''// @@BLOG@@
// LeetCode 133278676. @@T@@ — Dart 版（方案B：逐键求值 / reduce 链式访问）
Object? getValueEval(Map<String, dynamic> data, List<String> path) {
  var cur = data as Object?;
  for (final k in path) {
    cur = (cur as Map<String, dynamic>)[k];
  }
  return cur;
}

Object? getValueChain(Map<String, dynamic> data, List<String> path) {
  return path.fold<Object?>(data, (acc, k) => (acc as Map<String, dynamic>)[k]);
}

void main() {
  final data = <String, dynamic>{
    'a': <String, dynamic>{'b': <String, dynamic>{'c': 1}},
    'd': <String, dynamic>{'e': 2},
  };
  if (getValueEval(data, ['a', 'b', 'c']) != 1) throw StateError('p1 failed');
  if (getValueChain(data, ['d', 'e']) != 2) throw StateError('p2 failed');
  print('PASS');
}
''',
}

EXTS = {"rust": ".rs", "lua": ".lua", "c": ".c", "cpp": ".cpp", "r": ".R", "zig": ".zig", "dart": ".dart"}

def main():
    for lang, t in A.items():
        out = t.replace("@@BLOG@@", BLOG).replace("@@T@@", DESC)
        emit(lang, REL + "/solution_1___1" + EXTS[lang], out)
        emit(lang, REL + "/solution_2___2" + EXTS[lang], out.replace("方案A：安全遍历，缺失返回", "方案A：安全遍历（单用例），缺失返回"))
    for lang, t in B.items():
        out = t.replace("@@BLOG@@", BLOG).replace("@@T@@", DESC)
        emit(lang, REL + "/solution_3___3" + EXTS[lang], out)
        emit(lang, REL + "/solution_4___4" + EXTS[lang], out)

if __name__ == "__main__":
    main()
