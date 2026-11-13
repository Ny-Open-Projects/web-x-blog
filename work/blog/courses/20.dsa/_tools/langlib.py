#!/usr/bin/env python3
# langlib.py — 7 语言共享 harness 库（tree/linked_list）+ 文件发射器
# 用法：from langlib import emit, TREE_HARNESS, LL_HARNESS, wrap_main ...
import os
DSA = "/Users/Wang/Code/github/web-x-blog/work/blog/courses/20.dsa"
EXT = {"rust": "rs", "lua": "lua", "c": "c", "cpp": "cpp", "r": "R", "zig": "zig", "dart": "dart"}

def emit(lang, relpath, content):
    """写文件到 dsa/{lang}/{relpath}，自动创建目录"""
    path = os.path.join(DSA, lang, relpath)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(content)
    return path

# ============ 树 harness（每语言一段：TreeNode + build_tree [+ free]） ============
TREE_H = {}
TREE_H["rust"] = '''use std::rc::Rc;
use std::cell::RefCell;

#[derive(Debug)]
struct TreeNode {
    val: i32,
    left: Option<Rc<RefCell<TreeNode>>>,
    right: Option<Rc<RefCell<TreeNode>>>,
}

impl TreeNode {
    fn new(val: i32) -> Rc<RefCell<TreeNode>> {
        Rc::new(RefCell::new(TreeNode { val, left: None, right: None }))
    }
}

fn build_tree(vals: &[Option<i32>]) -> Option<Rc<RefCell<TreeNode>>> {
    if vals.is_empty() || vals[0].is_none() {
        return None;
    }
    let root = TreeNode::new(vals[0].unwrap());
    let mut queue: Vec<Rc<RefCell<TreeNode>>> = vec![root.clone()];
    let mut i = 1;
    while !queue.is_empty() && i < vals.len() {
        let node = queue.remove(0);
        if i < vals.len() {
            if let Some(v) = vals[i] {
                let child = TreeNode::new(v);
                node.borrow_mut().left = Some(child.clone());
                queue.push(child);
            }
            i += 1;
        }
        if i < vals.len() {
            if let Some(v) = vals[i] {
                let child = TreeNode::new(v);
                node.borrow_mut().right = Some(child.clone());
                queue.push(child);
            }
            i += 1;
        }
    }
    Some(root)
}
'''
TREE_H["lua"] = '''local TreeNode = {}
TreeNode.__index = TreeNode
function TreeNode.new(val)
    return setmetatable({val = val, left = nil, right = nil}, TreeNode)
end

local function build_tree(vals)
    if not vals or #vals == 0 or vals[1] == "null" then return nil end
    local root = TreeNode.new(vals[1])
    local queue = {root}
    local head = 1
    local i = 2
    while head <= #queue and i <= #vals do
        local node = queue[head]
        head = head + 1
        if i <= #vals then
            if vals[i] ~= "null" then
                node.left = TreeNode.new(vals[i])
                queue[#queue + 1] = node.left
            end
            i = i + 1
        end
        if i <= #vals then
            if vals[i] ~= "null" then
                node.right = TreeNode.new(vals[i])
                queue[#queue + 1] = node.right
            end
            i = i + 1
        end
    end
    return root
end
'''
TREE_H["c"] = '''#include <stdio.h>
#include <stdlib.h>
#define INT_MIN_SN (-2147483647 - 1)

typedef struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
} TreeNode;

static TreeNode *build_tree(const int *vals, int n) {
    if (n == 0 || vals[0] == INT_MIN_SN) return NULL;
    TreeNode *root = malloc(sizeof(TreeNode));
    root->val = vals[0]; root->left = root->right = NULL;
    TreeNode **queue = malloc(sizeof(TreeNode *) * n);
    int head = 0, tail = 0, i = 1;
    queue[tail++] = root;
    while (head < tail && i < n) {
        TreeNode *node = queue[head++];
        if (i < n) {
            if (vals[i] != INT_MIN_SN) {
                node->left = malloc(sizeof(TreeNode));
                node->left->val = vals[i]; node->left->left = node->left->right = NULL;
                queue[tail++] = node->left;
            }
            i++;
        }
        if (i < n) {
            if (vals[i] != INT_MIN_SN) {
                node->right = malloc(sizeof(TreeNode));
                node->right->val = vals[i]; node->right->left = node->right->right = NULL;
                queue[tail++] = node->right;
            }
            i++;
        }
    }
    free(queue);
    return root;
}

static void free_tree(TreeNode *n) {
    if (!n) return;
    free_tree(n->left);
    free_tree(n->right);
    free(n);
}
'''
TREE_H["cpp"] = '''#include <cassert>
#include <cstdint>
#include <iostream>
#include <optional>
#include <queue>
#include <vector>

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    explicit TreeNode(int v) : val(v), left(nullptr), right(nullptr) {}
};

static TreeNode *build_tree(const std::vector<std::optional<int>> &vals) {
    if (vals.empty() || !vals[0].has_value()) return nullptr;
    auto *root = new TreeNode(*vals[0]);
    std::queue<TreeNode *> q;
    q.push(root);
    size_t i = 1;
    while (!q.empty() && i < vals.size()) {
        TreeNode *node = q.front();
        q.pop();
        if (i < vals.size()) {
            if (vals[i].has_value()) {
                node->left = new TreeNode(*vals[i]);
                q.push(node->left);
            }
            ++i;
        }
        if (i < vals.size()) {
            if (vals[i].has_value()) {
                node->right = new TreeNode(*vals[i]);
                q.push(node->right);
            }
            ++i;
        }
    }
    return root;
}

static void free_tree(TreeNode *n) {
    if (!n) return;
    free_tree(n->left);
    free_tree(n->right);
    delete n;
}
'''
TREE_H["r"] = '''# 树节点：R 必须 environment 引用语义（list 是值语义）
TreeNode <- function(val, left = NULL, right = NULL) {
  e <- new.env(parent = emptyenv())
  e$val <- val; e$left <- left; e$right <- right
  class(e) <- "TreeNode"
  e
}

build_tree <- function(vals) {
  if (length(vals) == 0 || is.na(vals[[1]])) return(NULL)
  root <- TreeNode(vals[[1]])
  queue <- list(root)
  head <- 1L
  i <- 2L
  while (head <= length(queue) && i <= length(vals)) {
    node <- queue[[head]]
    head <- head + 1L
    if (i <= length(vals)) {
      if (!is.na(vals[[i]])) {
        node$left <- TreeNode(vals[[i]])
        queue[[length(queue) + 1L]] <- node$left
      }
      i <- i + 1L
    }
    if (i <= length(vals)) {
      if (!is.na(vals[[i]])) {
        node$right <- TreeNode(vals[[i]])
        queue[[length(queue) + 1L]] <- node$right
      }
      i <- i + 1L
    }
  }
  root
}

# 层序转列表（用于断言输出）
tree_to_levels <- function(root) {
  if (is.null(root)) return(list())
  res <- list()
  level <- list(root)
  while (length(level) > 0) {
    vals <- list(); nxt <- list()
    for (nd in level) {
      vals[[length(vals) + 1L]] <- nd$val
      if (!is.null(nd$left)) nxt[[length(nxt) + 1L]] <- nd$left
      if (!is.null(nd$right)) nxt[[length(nxt) + 1L]] <- nd$right
    }
    res[[length(res) + 1L]] <- unlist(vals)
    level <- nxt
  }
  res
}
'''
TREE_H["zig"] = '''const std = @import("std");

const TreeNode = struct {
    val: i32,
    left: ?*TreeNode,
    right: ?*TreeNode,
};

fn buildTree(allocator: std.mem.Allocator, vals: []const i32) !?*TreeNode {
    if (vals.len == 0 or vals[0] == -1) return null;
    const root = try allocator.create(TreeNode);
    root.* = .{ .val = vals[0], .left = null, .right = null };
    var queue = std.ArrayList(*TreeNode).init(allocator);
    defer queue.deinit();
    try queue.append(root);
    var head: usize = 0;
    var i: usize = 1;
    while (head < queue.items.len and i < vals.len) {
        const node = queue.items[head];
        head += 1;
        if (i < vals.len) {
            if (vals[i] != -1) {
                const child = try allocator.create(TreeNode);
                child.* = .{ .val = vals[i], .left = null, .right = null };
                node.left = child;
                try queue.append(child);
            }
            i += 1;
        }
        if (i < vals.len) {
            if (vals[i] != -1) {
                const child = try allocator.create(TreeNode);
                child.* = .{ .val = vals[i], .left = null, .right = null };
                node.right = child;
                try queue.append(child);
            }
            i += 1;
        }
    }
    return root;
}
'''
TREE_H["dart"] = '''class TreeNode {
  int val;
  TreeNode? left;
  TreeNode? right;
  TreeNode(this.val);
}

TreeNode? buildTree(List<int?> vals) {
  if (vals.isEmpty || vals[0] == null) return null;
  final root = TreeNode(vals[0]!);
  final queue = <TreeNode>[root];
  var head = 0;
  var i = 1;
  while (head < queue.length && i < vals.length) {
    final node = queue[head++];
    if (i < vals.length) {
      if (vals[i] != null) {
        node.left = TreeNode(vals[i]!);
        queue.add(node.left!);
      }
      i++;
    }
    if (i < vals.length) {
      if (vals[i] != null) {
        node.right = TreeNode(vals[i]!);
        queue.add(node.right!);
      }
      i++;
    }
  }
  return root;
}

List<List<int>> treeToLevels(TreeNode? root) {
  if (root == null) return [];
  final res = <List<int>>[];
  var level = <TreeNode>[root];
  while (level.isNotEmpty) {
    final vals = <int>[];
    final nxt = <TreeNode>[];
    for (final n in level) {
      vals.add(n.val);
      if (n.left != null) nxt.add(n.left!);
      if (n.right != null) nxt.add(n.right!);
    }
    res.add(vals);
    level = nxt;
  }
  return res;
}
'''

# ============ 每语言 main/PASS 包装 ============
PASS_TAIL = {}
PASS_TAIL["rust"] = '    println!("PASS");\n}\n'
PASS_TAIL["lua"] = 'print("PASS")\n'
PASS_TAIL["c"] = '    printf("PASS\\n");\n    return 0;\n}\n'
PASS_TAIL["cpp"] = '    std::cout << "PASS" << std::endl;\n    return 0;\n}\n'
PASS_TAIL["r"] = 'cat("PASS\\n")\n'
PASS_TAIL["zig"] = '    std.debug.print("PASS\\n", .{});\n}\n'
PASS_TAIL["dart"] = "  print('PASS');\n}\n"

def head_comment(lang, src, title):
    c = {"rust": "//", "lua": "--", "c": "/*", "cpp": "//", "r": "#", "zig": "//", "dart": "//"}[lang]
    t = f"{c} 来源（blog）：https://blog.csdn.net/tyro_java/article/details/{src}"
    if lang == "c":
        return f"{t}\n{c} {title} */"
    return f"{t}\n{c} {title}"

def vals_r(vals):  # python list -> R 语法
    if not vals: return "list()"
    return "list(" + ", ".join("NA" if v is None else f"{v}L" for v in vals) + ")"

def vals_zig(vals):
    if not vals:
        return "&[_]i32{}"
    return "&[_]i32{ " + ", ".join("-1" if v is None else str(v) for v in vals) + " }"
