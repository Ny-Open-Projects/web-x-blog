#!/usr/bin/env python3
# gen_fix_n06.py — 补齐 notes/lc_145370679 LCP 10 二叉树任务调度 × 7 语言
# TS 原文件即为占位 stub：dfs 返回空数组，仅测试 null 输入；忠实翻译
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from langlib import emit

REL = "notes/lc_145370679_leetcode_lcp_10._二叉树任务调度"
BLOG = "来源（blog）：https://blog.csdn.net/tyro_java/article/details/145370679"
DESC = "LCP 10. 二叉树任务调度（TS 原文件为 dfs 占位 stub，忠实翻译：dfs 返回空数组）"

T_RUST = '''// @@BLOG@@
// LeetCode 145370679. LCP 10. 二叉树任务调度 — Rust 版（@@DESC@@）

fn dfs(_root: Option<std::rc::Rc<std::cell::RefCell<TreeNode>>>) -> Vec<i32> {
    vec![]
}

#[derive(Debug)]
struct TreeNode {
    val: i32,
    left: Option<std::rc::Rc<std::cell::RefCell<TreeNode>>>,
    right: Option<std::rc::Rc<std::cell::RefCell<TreeNode>>>,
}

fn main() {
    let got = dfs(None);
    assert!(got.is_empty(), "dfs(null) 应返回空数组");
    println!("PASS");
}
'''

T_LUA = '''-- @@BLOG@@
-- LeetCode 145370679. LCP 10. 二叉树任务调度 — Lua 版（@@DESC@@）
local function dfs(root)
    return {}
end

assert(#dfs(nil) == 0, "dfs(nil) 应返回空数组")
print("PASS")
'''

T_C = '''/* @@BLOG@@
 * LeetCode 145370679. LCP 10. 二叉树任务调度 — C 版（@@DESC@@）
 */
#include <stdio.h>

/* dfs 占位实现（与 TS 原文件一致）：返回结果个数 0 */
static int dfs(const void *root) {
    (void)root;
    return 0;
}

int main(void) {
    if (dfs(NULL) != 0) { printf("FAILED\\n"); return 1; }
    printf("PASS\\n");
    return 0;
}
'''

T_CPP = '''// @@BLOG@@
// LeetCode 145370679. LCP 10. 二叉树任务调度 — C++ 版（@@DESC@@）
#include <iostream>
#include <vector>

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
};

// dfs 占位实现（与 TS 原文件一致）：返回空数组
static std::vector<int> dfs(TreeNode *root) {
    (void)root;
    return {};
}

int main() {
    if (!dfs(nullptr).empty()) { std::cout << "FAILED" << std::endl; return 1; }
    std::cout << "PASS" << std::endl;
    return 0;
}
'''

T_R = '''# @@BLOG@@
# LeetCode 145370679. LCP 10. 二叉树任务调度 — R 版（@@DESC@@）

dfs <- function(root) {
  c()
}

stopifnot(length(dfs(NULL)) == 0)
cat("PASS\\n")
'''

T_ZIG = '''// @@BLOG@@
// LeetCode 145370679. LCP 10. 二叉树任务调度 — Zig 版（@@DESC@@）
const std = @import("std");

// dfs 占位实现（与 TS 原文件一致）：返回空切片
fn dfs(root: ?*anyopaque) []const i32 {
    _ = root;
    return &[_]i32{};
}

pub fn main() !void {
    if (dfs(null).len != 0) {
        std.debug.print("FAILED\\n", .{});
        return error.TestFailed;
    }
    std.debug.print("PASS\\n", .{});
}
'''

T_DART = '''// @@BLOG@@
// LeetCode 145370679. LCP 10. 二叉树任务调度 — Dart 版（@@DESC@@）

class TreeNode {
  int val;
  TreeNode? left;
  TreeNode? right;
  TreeNode(this.val);
}

// dfs 占位实现（与 TS 原文件一致）：返回空数组
List<int> dfs(TreeNode? root) {
  return <int>[];
}

void main() {
  if (dfs(null).isNotEmpty) throw StateError('FAILED');
  print('PASS');
}
'''

GENS = {
    "rust": (T_RUST, ".rs"),
    "lua": (T_LUA, ".lua"),
    "c": (T_C, ".c"),
    "cpp": (T_CPP, ".cpp"),
    "r": (T_R, ".R"),
    "zig": (T_ZIG, ".zig"),
    "dart": (T_DART, ".dart"),
}

def main():
    for lang, (t, ext) in GENS.items():
        out = t.replace("@@BLOG@@", BLOG).replace("@@DESC@@", DESC)
        emit(lang, REL + "/solution_1___1" + ext, out)
    # 方案2 文件名（对应 TS solution_2_2_____2_____-__.ts）
    for lang, (t, ext) in GENS.items():
        out = t.replace("@@BLOG@@", BLOG).replace("@@DESC@@", DESC)
        emit(lang, REL + "/solution_2_2_____2_____-__" + ext, out)

if __name__ == "__main__":
    main()
