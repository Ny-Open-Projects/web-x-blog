#!/usr/bin/env python3
# gen_fix_n08.py — 补齐 notes/lc_133270489 原型链原理 × 7 语言（4 解法）
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from langlib import emit

REL = "notes/lc_133270489_基于链表实现js中的原型链原理与算法实现"
BLOG = "来源（blog）：https://blog.csdn.net/tyro_java/article/details/133270489"

# ---------- s1: instanceOf ----------
S1 = {
"rust": '''// @@BLOG@@
// LeetCode 133270489. 原型链原理 — Rust 版（方案1：instanceOf 沿原型链判定）
use std::cell::RefCell;
use std::collections::HashMap;
use std::rc::Rc;

struct Proto {
    name: String,
    props: RefCell<HashMap<String, String>>,
    parent: Option<Rc<Proto>>,
}

impl Proto {
    fn new(name: &str, parent: Option<Rc<Proto>>) -> Rc<Proto> {
        Rc::new(Proto {
            name: name.to_string(),
            props: RefCell::new(HashMap::new()),
            parent,
        })
    }
}

fn instance_of(obj: &Rc<Proto>, prototype: &Rc<Proto>) -> bool {
    let mut p: Option<&Rc<Proto>> = Some(obj);
    while let Some(cur) = p {
        if std::ptr::eq(cur.as_ref(), prototype.as_ref()) {
            return true;
        }
        p = cur.parent.as_ref();
    }
    false
}

fn main() {
    let object_proto = Proto::new("Object.prototype", None);
    let function_proto = Proto::new("Function.prototype", Some(object_proto.clone()));
    let array_proto = Proto::new("Array.prototype", Some(object_proto.clone()));
    let obj = Proto::new("obj", Some(object_proto.clone()));
    let func = Proto::new("func", Some(function_proto.clone()));
    let arr = Proto::new("arr", Some(array_proto.clone()));

    let cases = [
        (instance_of(&obj, &object_proto), true),
        (instance_of(&func, &function_proto), true),
        (instance_of(&func, &object_proto), true),
        (instance_of(&arr, &array_proto), true),
        (instance_of(&arr, &object_proto), true),
    ];
    for (idx, (got, want)) in cases.iter().enumerate() {
        assert_eq!(got, want, "case {} failed", idx);
    }
    println!("PASS");
}
''',
"lua": '''-- @@BLOG@@
-- LeetCode 133270489. 原型链原理 — Lua 版（方案1：instanceOf 沿原型链判定）
local Proto = {}
Proto.__index = Proto
function Proto.new(name, parent)
    return setmetatable({ name = name, props = {}, parent = parent }, Proto)
end

local function instance_of(obj, prototype)
    local p = obj
    while p ~= nil do
        if p == prototype then return true end
        p = p.parent
    end
    return false
end

local object_proto = Proto.new("Object.prototype", nil)
local function_proto = Proto.new("Function.prototype", object_proto)
local array_proto = Proto.new("Array.prototype", object_proto)
local obj = Proto.new("obj", object_proto)
local func = Proto.new("func", function_proto)
local arr = Proto.new("arr", array_proto)

local cases = {
    {instance_of(obj, object_proto), true},
    {instance_of(func, function_proto), true},
    {instance_of(func, object_proto), true},
    {instance_of(arr, array_proto), true},
    {instance_of(arr, object_proto), true},
}
for idx, c in ipairs(cases) do
    assert(c[1] == c[2], "case " .. idx .. " failed")
end
print("PASS")
''',
"c": '''/* @@BLOG@@
 * LeetCode 133270489. 原型链原理 — C 版（方案1：instanceOf 沿原型链判定）
 */
#include <stdio.h>
#include <string.h>

typedef struct Proto {
    const char *name;
    struct Proto *parent;
} Proto;

static int instance_of(const Proto *obj, const Proto *prototype) {
    const Proto *p = obj;
    while (p != NULL) {
        if (p == prototype) return 1;
        p = p->parent;
    }
    return 0;
}

int main(void) {
    Proto object_proto = {"Object.prototype", NULL};
    Proto function_proto = {"Function.prototype", &object_proto};
    Proto array_proto = {"Array.prototype", &object_proto};
    Proto obj = {"obj", &object_proto};
    Proto func = {"func", &function_proto};
    Proto arr = {"arr", &array_proto};

    int g0 = instance_of(&obj, &object_proto);
    int g1 = instance_of(&func, &function_proto);
    int g2 = instance_of(&func, &object_proto);
    int g3 = instance_of(&arr, &array_proto);
    int g4 = instance_of(&arr, &object_proto);
    if (!g0 || !g1 || !g2 || !g3 || !g4) { printf("FAIL\\n"); return 1; }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''// @@BLOG@@
// LeetCode 133270489. 原型链原理 — C++ 版（方案1：instanceOf 沿原型链判定）
#include <iostream>
#include <string>
#include <unordered_map>

struct Proto {
    std::string name;
    std::unordered_map<std::string, std::string> props;
    Proto *parent;
    Proto(const std::string &n, Proto *p = nullptr) : name(n), parent(p) {}
};

static bool instance_of(const Proto *obj, const Proto *prototype) {
    const Proto *p = obj;
    while (p != nullptr) {
        if (p == prototype) return true;
        p = p->parent;
    }
    return false;
}

int main() {
    Proto object_proto("Object.prototype");
    Proto function_proto("Function.prototype", &object_proto);
    Proto array_proto("Array.prototype", &object_proto);
    Proto obj("obj", &object_proto);
    Proto func("func", &function_proto);
    Proto arr("arr", &array_proto);

    bool g0 = instance_of(&obj, &object_proto);
    bool g1 = instance_of(&func, &function_proto);
    bool g2 = instance_of(&func, &object_proto);
    bool g3 = instance_of(&arr, &array_proto);
    bool g4 = instance_of(&arr, &object_proto);
    if (!g0 || !g1 || !g2 || !g3 || !g4) { std::cout << "FAIL" << std::endl; return 1; }
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''# @@BLOG@@
# LeetCode 133270489. 原型链原理 — R 版（方案1：instanceOf 沿原型链判定）
# 节点用 environment 引用语义
Proto <- function(name, parent = NULL) {
  e <- new.env(parent = emptyenv())
  e$name <- name
  e$props <- new.env(parent = emptyenv())
  e$parent <- parent
  e
}

instance_of <- function(obj, prototype) {
  p <- obj
  while (!is.null(p)) {
    if (identical(p, prototype)) return(TRUE)
    p <- p$parent
  }
  FALSE
}

object_proto <- Proto("Object.prototype")
function_proto <- Proto("Function.prototype", object_proto)
array_proto <- Proto("Array.prototype", object_proto)
obj <- Proto("obj", object_proto)
func <- Proto("func", function_proto)
arr <- Proto("arr", array_proto)

stopifnot(instance_of(obj, object_proto))
stopifnot(instance_of(func, function_proto))
stopifnot(instance_of(func, object_proto))
stopifnot(instance_of(arr, array_proto))
stopifnot(instance_of(arr, object_proto))
cat("PASS\\n")
''',
"zig": '''// @@BLOG@@
// LeetCode 133270489. 原型链原理 — Zig 版（方案1：instanceOf 沿原型链判定）
const std = @import("std");

const Proto = struct {
    name: []const u8,
    parent: ?*Proto,
};

fn instanceOf(obj: *const Proto, prototype: *const Proto) bool {
    var p: ?*const Proto = obj;
    while (p) |cur| {
        if (cur == prototype) return true;
        p = cur.parent;
    }
    return false;
}

pub fn main() !void {
    var gpa = std.heap.GeneralPurposeAllocator(.{}){};
    const allocator = gpa.allocator();

    const object_proto = try allocator.create(Proto);
    object_proto.* = .{ .name = "Object.prototype", .parent = null };
    const function_proto = try allocator.create(Proto);
    function_proto.* = .{ .name = "Function.prototype", .parent = object_proto };
    const array_proto = try allocator.create(Proto);
    array_proto.* = .{ .name = "Array.prototype", .parent = object_proto };
    const obj = try allocator.create(Proto);
    obj.* = .{ .name = "obj", .parent = object_proto };
    const func = try allocator.create(Proto);
    func.* = .{ .name = "func", .parent = function_proto };
    const arr = try allocator.create(Proto);
    arr.* = .{ .name = "arr", .parent = array_proto };

    if (!instanceOf(obj, object_proto)) return error.TestFailed;
    if (!instanceOf(func, function_proto)) return error.TestFailed;
    if (!instanceOf(func, object_proto)) return error.TestFailed;
    if (!instanceOf(arr, array_proto)) return error.TestFailed;
    if (!instanceOf(arr, object_proto)) return error.TestFailed;
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''// @@BLOG@@
// LeetCode 133270489. 原型链原理 — Dart 版（方案1：instanceOf 沿原型链判定）
class Proto {
  String name;
  Map<String, String> props = {};
  Proto? parent;
  Proto(this.name, [this.parent]);
}

bool instanceOf(Proto obj, Proto prototype) {
  Proto? p = obj;
  while (p != null) {
    if (identical(p, prototype)) return true;
    p = p.parent;
  }
  return false;
}

void main() {
  final objectProto = Proto('Object.prototype');
  final functionProto = Proto('Function.prototype', objectProto);
  final arrayProto = Proto('Array.prototype', objectProto);
  final obj = Proto('obj', objectProto);
  final func = Proto('func', functionProto);
  final arr = Proto('arr', arrayProto);

  assert(instanceOf(obj, objectProto), 'case 0 failed');
  assert(instanceOf(func, functionProto), 'case 1 failed');
  assert(instanceOf(func, objectProto), 'case 2 failed');
  assert(instanceOf(arr, arrayProto), 'case 3 failed');
  assert(instanceOf(arr, objectProto), 'case 4 failed');
  print('PASS');
}
''',
}

# ---------- s2: get 沿链查找 ----------
S2 = {
"rust": '''// @@BLOG@@
// LeetCode 133270489. 原型链原理 — Rust 版（方案2：get 沿原型链查找属性）
use std::cell::RefCell;
use std::collections::HashMap;
use std::rc::Rc;

struct Proto {
    name: String,
    props: RefCell<HashMap<String, String>>,
    parent: Option<Rc<Proto>>,
}

impl Proto {
    fn new(name: &str, parent: Option<Rc<Proto>>) -> Rc<Proto> {
        Rc::new(Proto {
            name: name.to_string(),
            props: RefCell::new(HashMap::new()),
            parent,
        })
    }
    fn set(&self, key: &str, value: &str) {
        self.props.borrow_mut().insert(key.to_string(), value.to_string());
    }
    fn get(&self, key: &str) -> Option<String> {
        // 从自身开始沿链查找
        if let Some(v) = self.props.borrow().get(key) {
            return Some(v.clone());
        }
        let mut cur = self.parent.as_ref();
        while let Some(node) = cur {
            if let Some(v) = node.props.borrow().get(key) {
                return Some(v.clone());
            }
            cur = node.parent.as_ref();
        }
        None
    }
}

fn main() {
    let object_proto = Proto::new("Object.prototype", None);
    object_proto.set("x", "x");
    let function_proto = Proto::new("Function.prototype", Some(object_proto.clone()));
    function_proto.set("y", "y");
    let array_proto = Proto::new("Array.prototype", Some(object_proto.clone()));
    array_proto.set("z", "z");
    let obj = Proto::new("obj", Some(object_proto.clone()));
    let func = Proto::new("func", Some(function_proto.clone()));
    let arr = Proto::new("arr", Some(array_proto.clone()));

    assert_eq!(obj.get("x").as_deref(), Some("x"), "case 0 failed");
    assert_eq!(func.get("y").as_deref(), Some("y"), "case 1 failed");
    assert_eq!(arr.get("z").as_deref(), Some("z"), "case 2 failed");
    println!("PASS");
}
''',
"lua": '''-- @@BLOG@@
-- LeetCode 133270489. 原型链原理 — Lua 版（方案2：get 沿原型链查找属性）
local Proto = {}
Proto.__index = Proto
function Proto.new(name, parent)
    return setmetatable({ name = name, props = {}, parent = parent }, Proto)
end
function Proto:set(key, value)
    self.props[key] = value
end
function Proto:get(key)
    local cur = self
    while cur ~= nil do
        if cur.props[key] ~= nil then return cur.props[key] end
        cur = cur.parent
    end
    return nil
end

local object_proto = Proto.new("Object.prototype")
object_proto:set("x", "x")
local function_proto = Proto.new("Function.prototype", object_proto)
function_proto:set("y", "y")
local array_proto = Proto.new("Array.prototype", object_proto)
array_proto:set("z", "z")
local obj = Proto.new("obj", object_proto)
local func = Proto.new("func", function_proto)
local arr = Proto.new("arr", array_proto)

assert(obj:get("x") == "x", "case 0 failed")
assert(func:get("y") == "y", "case 1 failed")
assert(arr:get("z") == "z", "case 2 failed")
print("PASS")
''',
"c": '''/* @@BLOG@@
 * LeetCode 133270489. 原型链原理 — C 版（方案2：get 沿原型链查找属性）
 */
#include <stdio.h>
#include <string.h>

#define MAX_PROPS 8
typedef struct Proto {
    const char *name;
    char keys[MAX_PROPS][16];
    char vals[MAX_PROPS][32];
    int nprops;
    struct Proto *parent;
} Proto;

static void set_prop(Proto *p, const char *key, const char *value) {
    strcpy(p->keys[p->nprops], key);
    strcpy(p->vals[p->nprops], value);
    p->nprops++;
}

static const char *get_prop(const Proto *p, const char *key) {
    const Proto *cur = p;
    while (cur != NULL) {
        for (int i = 0; i < cur->nprops; i++)
            if (strcmp(cur->keys[i], key) == 0) return cur->vals[i];
        cur = cur->parent;
    }
    return NULL;
}

int main(void) {
    Proto object_proto = {"Object.prototype", {}, {}, 0, NULL};
    set_prop(&object_proto, "x", "x");
    Proto function_proto = {"Function.prototype", {}, {}, 0, &object_proto};
    set_prop(&function_proto, "y", "y");
    Proto array_proto = {"Array.prototype", {}, {}, 0, &object_proto};
    set_prop(&array_proto, "z", "z");
    Proto obj = {"obj", {}, {}, 0, &object_proto};
    Proto func = {"func", {}, {}, 0, &function_proto};
    Proto arr = {"arr", {}, {}, 0, &array_proto};

    if (strcmp(get_prop(&obj, "x"), "x") != 0) { printf("case 0 failed\\n"); return 1; }
    if (strcmp(get_prop(&func, "y"), "y") != 0) { printf("case 1 failed\\n"); return 1; }
    if (strcmp(get_prop(&arr, "z"), "z") != 0) { printf("case 2 failed\\n"); return 1; }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''// @@BLOG@@
// LeetCode 133270489. 原型链原理 — C++ 版（方案2：get 沿原型链查找属性）
#include <iostream>
#include <string>
#include <unordered_map>

struct Proto {
    std::string name;
    std::unordered_map<std::string, std::string> props;
    Proto *parent;
    explicit Proto(const std::string &n, Proto *p = nullptr) : name(n), parent(p) {}
    void set(const std::string &key, const std::string &value) { props[key] = value; }
    std::string get(const std::string &key) const {
        const Proto *cur = this;
        while (cur != nullptr) {
            auto it = cur->props.find(key);
            if (it != cur->props.end()) return it->second;
            cur = cur->parent;
        }
        return "";
    }
};

int main() {
    Proto object_proto("Object.prototype");
    object_proto.set("x", "x");
    Proto function_proto("Function.prototype", &object_proto);
    function_proto.set("y", "y");
    Proto array_proto("Array.prototype", &object_proto);
    array_proto.set("z", "z");
    Proto obj("obj", &object_proto);
    Proto func("func", &function_proto);
    Proto arr("arr", &array_proto);

    if (obj.get("x") != "x") { std::cout << "case 0 failed" << std::endl; return 1; }
    if (func.get("y") != "y") { std::cout << "case 1 failed" << std::endl; return 1; }
    if (arr.get("z") != "z") { std::cout << "case 2 failed" << std::endl; return 1; }
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''# @@BLOG@@
# LeetCode 133270489. 原型链原理 — R 版（方案2：get 沿原型链查找属性）
Proto <- function(name, parent = NULL) {
  e <- new.env(parent = emptyenv())
  e$name <- name
  e$props <- new.env(parent = emptyenv())
  e$parent <- parent
  e
}
set_prop <- function(p, key, value) p$props[[key]] <- value
get_prop <- function(p, key) {
  cur <- p
  while (!is.null(cur)) {
    if (!is.null(cur$props[[key]])) return(cur$props[[key]])
    cur <- cur$parent
  }
  NULL
}

object_proto <- Proto("Object.prototype")
set_prop(object_proto, "x", "x")
function_proto <- Proto("Function.prototype", object_proto)
set_prop(function_proto, "y", "y")
array_proto <- Proto("Array.prototype", object_proto)
set_prop(array_proto, "z", "z")
obj <- Proto("obj", object_proto)
func <- Proto("func", function_proto)
arr <- Proto("arr", array_proto)

stopifnot(identical(get_prop(obj, "x"), "x"))
stopifnot(identical(get_prop(func, "y"), "y"))
stopifnot(identical(get_prop(arr, "z"), "z"))
cat("PASS\\n")
''',
"zig": '''// @@BLOG@@
// LeetCode 133270489. 原型链原理 — Zig 版（方案2：get 沿原型链查找属性）
const std = @import("std");

const MAX_PROPS = 8;
const Prop = struct { key: []const u8, val: []const u8 };
const Proto = struct {
    name: []const u8,
    props: [MAX_PROPS]Prop = undefined,
    nprops: usize = 0,
    parent: ?*Proto = null,

    fn set(self: *Proto, key: []const u8, val: []const u8) void {
        self.props[self.nprops] = .{ .key = key, .val = val };
        self.nprops += 1;
    }
    fn get(self: *const Proto, key: []const u8) ?[]const u8 {
        var cur: ?*const Proto = self;
        while (cur) |node| {
            var i: usize = 0;
            while (i < node.nprops) : (i += 1) {
                if (std.mem.eql(u8, node.props[i].key, key)) return node.props[i].val;
            }
            cur = node.parent;
        }
        return null;
    }
};

pub fn main() !void {
    var gpa = std.heap.GeneralPurposeAllocator(.{}){};
    const allocator = gpa.allocator();

    const object_proto = try allocator.create(Proto);
    object_proto.* = .{ .name = "Object.prototype" };
    _ = object_proto.set("x", "x");
    const function_proto = try allocator.create(Proto);
    function_proto.* = .{ .name = "Function.prototype", .parent = object_proto };
    _ = function_proto.set("y", "y");
    const array_proto = try allocator.create(Proto);
    array_proto.* = .{ .name = "Array.prototype", .parent = object_proto };
    _ = array_proto.set("z", "z");
    const obj = try allocator.create(Proto);
    obj.* = .{ .name = "obj", .parent = object_proto };
    const func = try allocator.create(Proto);
    func.* = .{ .name = "func", .parent = function_proto };
    const arr = try allocator.create(Proto);
    arr.* = .{ .name = "arr", .parent = array_proto };

    if (!std.mem.eql(u8, obj.get("x").?, "x")) return error.TestFailed;
    if (!std.mem.eql(u8, func.get("y").?, "y")) return error.TestFailed;
    if (!std.mem.eql(u8, arr.get("z").?, "z")) return error.TestFailed;
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''// @@BLOG@@
// LeetCode 133270489. 原型链原理 — Dart 版（方案2：get 沿原型链查找属性）
class Proto {
  String name;
  Map<String, String> props = {};
  Proto? parent;
  Proto(this.name, [this.parent]);

  void set(String key, String value) {
    props[key] = value;
  }

  String? get(String key) {
    Proto? cur = this;
    while (cur != null) {
      if (cur.props.containsKey(key)) return cur.props[key];
      cur = cur.parent;
    }
    return null;
  }
}

void main() {
  final objectProto = Proto('Object.prototype');
  objectProto.set('x', 'x');
  final functionProto = Proto('Function.prototype', objectProto);
  functionProto.set('y', 'y');
  final arrayProto = Proto('Array.prototype', objectProto);
  arrayProto.set('z', 'z');
  final obj = Proto('obj', objectProto);
  final func = Proto('func', functionProto);
  final arr = Proto('arr', arrayProto);

  assert(obj.get('x') == 'x', 'case 0 failed');
  assert(func.get('y') == 'y', 'case 1 failed');
  assert(arr.get('z') == 'z', 'case 2 failed');
  print('PASS');
}
''',
}

# ---------- s3: get + instanceOf ----------
S3 = {
"rust": '''// @@BLOG@@
// LeetCode 133270489. 原型链原理 — Rust 版（方案3：get 查找 + instanceOf 判定）
use std::cell::RefCell;
use std::collections::HashMap;
use std::rc::Rc;

struct Proto {
    name: String,
    props: RefCell<HashMap<String, String>>,
    parent: Option<Rc<Proto>>,
}

impl Proto {
    fn new(name: &str, parent: Option<Rc<Proto>>) -> Rc<Proto> {
        Rc::new(Proto {
            name: name.to_string(),
            props: RefCell::new(HashMap::new()),
            parent,
        })
    }
    fn set(&self, key: &str, value: &str) {
        self.props.borrow_mut().insert(key.to_string(), value.to_string());
    }
    fn get(&self, key: &str) -> Option<String> {
        if let Some(v) = self.props.borrow().get(key) {
            return Some(v.clone());
        }
        let mut cur = self.parent.as_ref();
        while let Some(node) = cur {
            if let Some(v) = node.props.borrow().get(key) {
                return Some(v.clone());
            }
            cur = node.parent.as_ref();
        }
        None
    }
}

fn instance_of(obj: &Rc<Proto>, prototype: &Rc<Proto>) -> bool {
    let mut p: Option<&Rc<Proto>> = Some(obj);
    while let Some(cur) = p {
        if std::ptr::eq(cur.as_ref(), prototype.as_ref()) {
            return true;
        }
        p = cur.parent.as_ref();
    }
    false
}

fn main() {
    let object_proto = Proto::new("Object.prototype", None);
    object_proto.set("a", "aaa");
    let function_proto = Proto::new("Function.prototype", Some(object_proto.clone()));
    function_proto.set("b", "bbb");
    let obj = Proto::new("obj", Some(object_proto.clone()));
    let func = Proto::new("func", Some(function_proto.clone()));

    assert_eq!(obj.get("a").as_deref(), Some("aaa"), "case 0 failed");
    assert_eq!(obj.get("b"), None, "case 1 failed");
    assert_eq!(func.get("a").as_deref(), Some("aaa"), "case 2 failed");
    assert_eq!(func.get("b").as_deref(), Some("bbb"), "case 3 failed");
    assert!(instance_of(&func, &object_proto), "case 4 failed");
    println!("PASS");
}
''',
"lua": '''-- @@BLOG@@
-- LeetCode 133270489. 原型链原理 — Lua 版（方案3：get 查找 + instanceOf 判定）
local Proto = {}
Proto.__index = Proto
function Proto.new(name, parent)
    return setmetatable({ name = name, props = {}, parent = parent }, Proto)
end
function Proto:set(key, value)
    self.props[key] = value
end
function Proto:get(key)
    local cur = self
    while cur ~= nil do
        if cur.props[key] ~= nil then return cur.props[key] end
        cur = cur.parent
    end
    return nil
end

local function instance_of(obj, prototype)
    local p = obj
    while p ~= nil do
        if p == prototype then return true end
        p = p.parent
    end
    return false
end

local object_proto = Proto.new("Object.prototype")
object_proto:set("a", "aaa")
local function_proto = Proto.new("Function.prototype", object_proto)
function_proto:set("b", "bbb")
local obj = Proto.new("obj", object_proto)
local func = Proto.new("func", function_proto)

assert(obj:get("a") == "aaa", "case 0 failed")
assert(obj:get("b") == nil, "case 1 failed")
assert(func:get("a") == "aaa", "case 2 failed")
assert(func:get("b") == "bbb", "case 3 failed")
assert(instance_of(func, object_proto) == true, "case 4 failed")
print("PASS")
''',
"c": '''/* @@BLOG@@
 * LeetCode 133270489. 原型链原理 — C 版（方案3：get 查找 + instanceOf 判定）
 */
#include <stdio.h>
#include <string.h>

#define MAX_PROPS 8
typedef struct Proto {
    const char *name;
    char keys[MAX_PROPS][16];
    char vals[MAX_PROPS][32];
    int nprops;
    struct Proto *parent;
} Proto;

static void set_prop(Proto *p, const char *key, const char *value) {
    strcpy(p->keys[p->nprops], key);
    strcpy(p->vals[p->nprops], value);
    p->nprops++;
}

static const char *get_prop(const Proto *p, const char *key) {
    const Proto *cur = p;
    while (cur != NULL) {
        for (int i = 0; i < cur->nprops; i++)
            if (strcmp(cur->keys[i], key) == 0) return cur->vals[i];
        cur = cur->parent;
    }
    return NULL;
}

static int instance_of(const Proto *obj, const Proto *prototype) {
    const Proto *p = obj;
    while (p != NULL) {
        if (p == prototype) return 1;
        p = p->parent;
    }
    return 0;
}

int main(void) {
    Proto object_proto = {"Object.prototype", {}, {}, 0, NULL};
    set_prop(&object_proto, "a", "aaa");
    Proto function_proto = {"Function.prototype", {}, {}, 0, &object_proto};
    set_prop(&function_proto, "b", "bbb");
    Proto obj = {"obj", {}, {}, 0, &object_proto};
    Proto func = {"func", {}, {}, 0, &function_proto};

    if (strcmp(get_prop(&obj, "a"), "aaa") != 0) { printf("case 0 failed\\n"); return 1; }
    if (get_prop(&obj, "b") != NULL) { printf("case 1 failed\\n"); return 1; }
    if (strcmp(get_prop(&func, "a"), "aaa") != 0) { printf("case 2 failed\\n"); return 1; }
    if (strcmp(get_prop(&func, "b"), "bbb") != 0) { printf("case 3 failed\\n"); return 1; }
    if (!instance_of(&func, &object_proto)) { printf("case 4 failed\\n"); return 1; }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''// @@BLOG@@
// LeetCode 133270489. 原型链原理 — C++ 版（方案3：get 查找 + instanceOf 判定）
#include <iostream>
#include <string>
#include <unordered_map>

struct Proto {
    std::string name;
    std::unordered_map<std::string, std::string> props;
    Proto *parent;
    explicit Proto(const std::string &n, Proto *p = nullptr) : name(n), parent(p) {}
    void set(const std::string &key, const std::string &value) { props[key] = value; }
    bool has(const std::string &key) const {
        const Proto *cur = this;
        while (cur != nullptr) {
            if (cur->props.count(key)) return true;
            cur = cur->parent;
        }
        return false;
    }
    std::string get(const std::string &key) const {
        const Proto *cur = this;
        while (cur != nullptr) {
            auto it = cur->props.find(key);
            if (it != cur->props.end()) return it->second;
            cur = cur->parent;
        }
        return "";
    }
};

static bool instance_of(const Proto *obj, const Proto *prototype) {
    const Proto *p = obj;
    while (p != nullptr) {
        if (p == prototype) return true;
        p = p->parent;
    }
    return false;
}

int main() {
    Proto object_proto("Object.prototype");
    object_proto.set("a", "aaa");
    Proto function_proto("Function.prototype", &object_proto);
    function_proto.set("b", "bbb");
    Proto obj("obj", &object_proto);
    Proto func("func", &function_proto);

    if (obj.get("a") != "aaa") { std::cout << "case 0 failed" << std::endl; return 1; }
    if (obj.has("b")) { std::cout << "case 1 failed" << std::endl; return 1; }
    if (func.get("a") != "aaa") { std::cout << "case 2 failed" << std::endl; return 1; }
    if (func.get("b") != "bbb") { std::cout << "case 3 failed" << std::endl; return 1; }
    if (!instance_of(&func, &object_proto)) { std::cout << "case 4 failed" << std::endl; return 1; }
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''# @@BLOG@@
# LeetCode 133270489. 原型链原理 — R 版（方案3：get 查找 + instanceOf 判定）
Proto <- function(name, parent = NULL) {
  e <- new.env(parent = emptyenv())
  e$name <- name
  e$props <- new.env(parent = emptyenv())
  e$parent <- parent
  e
}
set_prop <- function(p, key, value) p$props[[key]] <- value
get_prop <- function(p, key) {
  cur <- p
  while (!is.null(cur)) {
    if (!is.null(cur$props[[key]])) return(cur$props[[key]])
    cur <- cur$parent
  }
  NULL
}
instance_of <- function(obj, prototype) {
  p <- obj
  while (!is.null(p)) {
    if (identical(p, prototype)) return(TRUE)
    p <- p$parent
  }
  FALSE
}

object_proto <- Proto("Object.prototype")
set_prop(object_proto, "a", "aaa")
function_proto <- Proto("Function.prototype", object_proto)
set_prop(function_proto, "b", "bbb")
obj <- Proto("obj", object_proto)
func <- Proto("func", function_proto)

stopifnot(identical(get_prop(obj, "a"), "aaa"))
stopifnot(is.null(get_prop(obj, "b")))
stopifnot(identical(get_prop(func, "a"), "aaa"))
stopifnot(identical(get_prop(func, "b"), "bbb"))
stopifnot(instance_of(func, object_proto))
cat("PASS\\n")
''',
"zig": '''// @@BLOG@@
// LeetCode 133270489. 原型链原理 — Zig 版（方案3：get 查找 + instanceOf 判定）
const std = @import("std");

const MAX_PROPS = 8;
const Prop = struct { key: []const u8, val: []const u8 };
const Proto = struct {
    name: []const u8,
    props: [MAX_PROPS]Prop = undefined,
    nprops: usize = 0,
    parent: ?*Proto = null,

    fn set(self: *Proto, key: []const u8, val: []const u8) void {
        self.props[self.nprops] = .{ .key = key, .val = val };
        self.nprops += 1;
    }
    fn get(self: *const Proto, key: []const u8) ?[]const u8 {
        var cur: ?*const Proto = self;
        while (cur) |node| {
            var i: usize = 0;
            while (i < node.nprops) : (i += 1) {
                if (std.mem.eql(u8, node.props[i].key, key)) return node.props[i].val;
            }
            cur = node.parent;
        }
        return null;
    }
};

fn instanceOf(obj: *const Proto, prototype: *const Proto) bool {
    var p: ?*const Proto = obj;
    while (p) |cur| {
        if (cur == prototype) return true;
        p = cur.parent;
    }
    return false;
}

pub fn main() !void {
    var gpa = std.heap.GeneralPurposeAllocator(.{}){};
    const allocator = gpa.allocator();

    const object_proto = try allocator.create(Proto);
    object_proto.* = .{ .name = "Object.prototype" };
    _ = object_proto.set("a", "aaa");
    const function_proto = try allocator.create(Proto);
    function_proto.* = .{ .name = "Function.prototype", .parent = object_proto };
    _ = function_proto.set("b", "bbb");
    const obj = try allocator.create(Proto);
    obj.* = .{ .name = "obj", .parent = object_proto };
    const func = try allocator.create(Proto);
    func.* = .{ .name = "func", .parent = function_proto };

    if (!std.mem.eql(u8, obj.get("a").?, "aaa")) return error.TestFailed;
    if (obj.get("b") != null) return error.TestFailed;
    if (!std.mem.eql(u8, func.get("a").?, "aaa")) return error.TestFailed;
    if (!std.mem.eql(u8, func.get("b").?, "bbb")) return error.TestFailed;
    if (!instanceOf(func, object_proto)) return error.TestFailed;
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''// @@BLOG@@
// LeetCode 133270489. 原型链原理 — Dart 版（方案3：get 查找 + instanceOf 判定）
class Proto {
  String name;
  Map<String, String> props = {};
  Proto? parent;
  Proto(this.name, [this.parent]);

  void set(String key, String value) {
    props[key] = value;
  }

  bool has(String key) {
    Proto? cur = this;
    while (cur != null) {
      if (cur.props.containsKey(key)) return true;
      cur = cur.parent;
    }
    return false;
  }

  String? get(String key) {
    Proto? cur = this;
    while (cur != null) {
      if (cur.props.containsKey(key)) return cur.props[key];
      cur = cur.parent;
    }
    return null;
  }
}

bool instanceOf(Proto obj, Proto prototype) {
  Proto? p = obj;
  while (p != null) {
    if (identical(p, prototype)) return true;
    p = p.parent;
  }
  return false;
}

void main() {
  final objectProto = Proto('Object.prototype');
  objectProto.set('a', 'aaa');
  final functionProto = Proto('Function.prototype', objectProto);
  functionProto.set('b', 'bbb');
  final obj = Proto('obj', objectProto);
  final func = Proto('func', functionProto);

  assert(obj.get('a') == 'aaa', 'case 0 failed');
  assert(!obj.has('b'), 'case 1 failed');
  assert(func.get('a') == 'aaa', 'case 2 failed');
  assert(func.get('b') == 'bbb', 'case 3 failed');
  assert(instanceOf(func, objectProto), 'case 4 failed');
  print('PASS');
}
''',
}

# ---------- s4: null/undefined 边界 ----------
S4 = {
"rust": '''// @@BLOG@@
// LeetCode 133270489. 原型链原理 — Rust 版（方案4：null/undefined 边界：instanceOf 均返回 false）
struct FakeObj {
    proto: Option<*const u8>, // 模拟 __proto__ 指针
}

struct FakeCtor {
    prototype: Option<*const u8>,
}

fn instance_of(a: Option<&FakeObj>, b: &FakeCtor) -> bool {
    // 与 JS 语义对齐：null/undefined 沿链必为 false
    let mut p = match a {
        None => return false,
        Some(o) => o.proto,
    };
    while let Some(ptr) = p {
        if Some(ptr) == b.prototype {
            return true;
        }
        // 演示用：无法继续向上（无真实对象头），直接终止
        p = None;
    }
    false
}

fn main() {
    // case: null / undefined 视为 None —— instanceOf 均为 false
    let ctor = FakeCtor { prototype: None };
    assert!(!instance_of(None, &ctor), "null case failed");
    assert!(!instance_of(None, &ctor), "undefined case failed");
    println!("PASS");
}
''',
"lua": '''-- @@BLOG@@
-- LeetCode 133270489. 原型链原理 — Lua 版（方案4：null/undefined 边界：instanceOf 均返回 false）
local function instance_of(a, b)
    local p = a
    while p ~= nil do
        if p == b.prototype then return true end
        p = p.__proto__
    end
    return false
end

local ctor = { prototype = nil }
assert(instance_of(nil, ctor) == false, "null case failed")
assert(instance_of(nil, ctor) == false, "undefined case failed")
print("PASS")
''',
"c": '''/* @@BLOG@@
 * LeetCode 133270489. 原型链原理 — C 版（方案4：null/undefined 边界：instanceOf 均返回 false）
 */
#include <stdio.h>

typedef struct Obj {
    void *__proto__;
} Obj;

typedef struct Ctor {
    void *prototype;
} Ctor;

static int instance_of(const void *a, const Ctor *b) {
    const void *p = a;
    while (p != NULL) {
        if (p == b->prototype) return 1;
        p = ((const Obj *)p)->__proto__;
    }
    return 0;
}

int main(void) {
    Ctor ctor = { NULL };
    if (instance_of(NULL, &ctor)) { printf("null case failed\\n"); return 1; }
    if (instance_of(NULL, &ctor)) { printf("undefined case failed\\n"); return 1; }
    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''// @@BLOG@@
// LeetCode 133270489. 原型链原理 — C++ 版（方案4：null/undefined 边界：instanceOf 均返回 false）
#include <iostream>

struct Obj {
    void *__proto__ = nullptr;
};

struct Ctor {
    void *prototype = nullptr;
};

static bool instance_of(const void *a, const Ctor &b) {
    const void *p = a;
    while (p != nullptr) {
        if (p == b.prototype) return true;
        p = static_cast<const Obj *>(p)->__proto__;
    }
    return false;
}

int main() {
    Ctor ctor;
    if (instance_of(nullptr, ctor)) { std::cout << "null case failed" << std::endl; return 1; }
    if (instance_of(nullptr, ctor)) { std::cout << "undefined case failed" << std::endl; return 1; }
    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''# @@BLOG@@
# LeetCode 133270489. 原型链原理 — R 版（方案4：null/undefined 边界：instanceOf 均返回 false）
instance_of <- function(a, b) {
  p <- a
  while (!is.null(p)) {
    if (identical(p, b$prototype)) return(TRUE)
    p <- p$`__proto__`
  }
  FALSE
}

ctor <- new.env(parent = emptyenv())
ctor$prototype <- NULL
stopifnot(!instance_of(NULL, ctor))
stopifnot(!instance_of(NULL, ctor))
cat("PASS\\n")
''',
"zig": '''// @@BLOG@@
// LeetCode 133270489. 原型链原理 — Zig 版（方案4：null/undefined 边界：instanceOf 均返回 false）
const std = @import("std");

const Obj = struct {
    proto: ?*anyopaque = null,
};

const Ctor = struct {
    prototype: ?*anyopaque = null,
};

fn instanceOf(a: ?*const Obj, b: *const Ctor) bool {
    var p: ?*const Obj = a;
    while (p) |cur| {
        if (cur.proto == b.prototype) return true;
        // 演示用：__proto__ 无法继续解引用，直接终止
        p = null;
    }
    return false;
}

pub fn main() !void {
    const ctor = Ctor{ .prototype = null };
    if (instanceOf(null, &ctor)) return error.TestFailed;
    if (instanceOf(null, &ctor)) return error.TestFailed;
    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''// @@BLOG@@
// LeetCode 133270489. 原型链原理 — Dart 版（方案4：null/undefined 边界：instanceOf 均返回 false）
class Obj {
  Obj? __proto__;
}

class Ctor {
  Obj? prototype;
}

bool instanceOf(Obj? a, Ctor b) {
  Obj? p = a;
  while (p != null) {
    if (identical(p, b.prototype)) return true;
    p = p.__proto__;
  }
  return false;
}

void main() {
  final ctor = Ctor();
  // Dart 中 null 对应 JS 的 null/undefined
  if (instanceOf(null, ctor)) throw StateError('null case failed');
  if (instanceOf(null, ctor)) throw StateError('undefined case failed');
  print('PASS');
}
''',
}

EXTS = {"rust": ".rs", "lua": ".lua", "c": ".c", "cpp": ".cpp", "r": ".R", "zig": ".zig", "dart": ".dart"}

def main():
    for sol, block in ((1, S1), (2, S2), (3, S3), (4, S4)):
        for lang, t in block.items():
            emit(lang, REL + "/solution_%d___%d%s" % (sol, sol, EXTS[lang]), t.replace("@@BLOG@@", BLOG))

if __name__ == "__main__":
    main()
