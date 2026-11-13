#!/usr/bin/env python3
# gen_fix_n17.py — 补齐 notes/lc_133651611 图的 DFS/BFS × 7 语言（8 解法，TS 源码全同）
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from langlib import emit

REL = "notes/lc_133651611_图及其深度和广度优先遍历实现"
BLOG = "来源（blog）：https://blog.csdn.net/tyro_java/article/details/133651611"
DESC = "图及其深度和广度优先遍历实现"

IMPL = {
"rust": '''// @@BLOG@@
// LeetCode 133651611. @@T@@ — Rust 版（方案@@N@@）
use std::collections::{HashMap, HashSet};

#[derive(Default)]
struct Graph {
    adj: HashMap<i32, Vec<i32>>,
}

impl Graph {
    fn add_edge(&mut self, from: i32, to: i32) {
        self.adj.entry(from).or_default().push(to);
        self.adj.entry(to).or_default().push(from);
    }

    fn dfs(&self, start: i32) -> Vec<i32> {
        let mut visited: HashSet<i32> = HashSet::new();
        let mut result: Vec<i32> = vec![];
        self.dfs_helper(start, &mut visited, &mut result);
        result
    }

    fn dfs_helper(&self, node: i32, visited: &mut HashSet<i32>, result: &mut Vec<i32>) {
        if visited.contains(&node) {
            return;
        }
        visited.insert(node);
        result.push(node);
        if let Some(neighbors) = self.adj.get(&node) {
            for &neighbor in neighbors {
                self.dfs_helper(neighbor, visited, result);
            }
        }
    }

    fn bfs(&self, start: i32) -> Vec<i32> {
        let mut visited: HashSet<i32> = HashSet::new();
        let mut result: Vec<i32> = vec![];
        let mut queue: std::collections::VecDeque<i32> = std::collections::VecDeque::new();
        queue.push_back(start);
        visited.insert(start);

        while let Some(node) = queue.pop_front() {
            result.push(node);
            if let Some(neighbors) = self.adj.get(&node) {
                for &neighbor in neighbors {
                    if !visited.contains(&neighbor) {
                        visited.insert(neighbor);
                        queue.push_back(neighbor);
                    }
                }
            }
        }
        result
    }
}

fn eq(a: &[i32], b: &[i32]) -> bool {
    a == b
}

fn main() {
    // case 1: 方形图 0-1-3-2-0
    let mut g1 = Graph::default();
    g1.add_edge(0, 1);
    g1.add_edge(0, 2);
    g1.add_edge(1, 3);
    g1.add_edge(2, 3);
    assert!(eq(&g1.dfs(0), &[0, 1, 3, 2]), "case1 dfs(0)");
    assert!(eq(&g1.bfs(0), &[0, 1, 2, 3]), "case1 bfs(0)");

    // case 2: 从另一节点出发
    assert!(eq(&g1.dfs(2), &[2, 0, 1, 3]), "case2 dfs(2)");
    assert!(eq(&g1.bfs(2), &[2, 0, 3, 1]), "case2 bfs(2)");

    println!("PASS");
}
''',
"lua": '''-- @@BLOG@@
-- LeetCode 133651611. @@T@@ — Lua 版（方案@@N@@）
local Graph = {}
Graph.__index = Graph

function Graph.new()
    return setmetatable({ adj = {} }, Graph)
end

function Graph:addEdge(from, to)
    self.adj[from] = self.adj[from] or {}
    self.adj[to] = self.adj[to] or {}
    self.adj[from][#self.adj[from] + 1] = to
    self.adj[to][#self.adj[to] + 1] = from
end

function Graph:dfs(start)
    local visited = {}
    local result = {}
    local function helper(node)
        if visited[node] then return end
        visited[node] = true
        result[#result + 1] = node
        for _, neighbor in ipairs(self.adj[node] or {}) do
            helper(neighbor)
        end
    end
    helper(start)
    return result
end

function Graph:bfs(start)
    local visited = { [start] = true }
    local result = {}
    local queue = { start }
    local head = 1
    while head <= #queue do
        local node = queue[head]
        head = head + 1
        result[#result + 1] = node
        for _, neighbor in ipairs(self.adj[node] or {}) do
            if not visited[neighbor] then
                visited[neighbor] = true
                queue[#queue + 1] = neighbor
            end
        end
    end
    return result
end

local function eq(a, b)
    if #a ~= #b then return false end
    for i = 1, #a do
        if a[i] ~= b[i] then return false end
    end
    return true
end

-- case 1: 方形图 0-1-3-2-0
local g1 = Graph.new()
g1:addEdge(0, 1)
g1:addEdge(0, 2)
g1:addEdge(1, 3)
g1:addEdge(2, 3)
assert(eq(g1:dfs(0), {0, 1, 3, 2}), "case1 dfs(0)")
assert(eq(g1:bfs(0), {0, 1, 2, 3}), "case1 bfs(0)")

-- case 2: 从另一节点出发
assert(eq(g1:dfs(2), {2, 0, 1, 3}), "case2 dfs(2)")
assert(eq(g1:bfs(2), {2, 0, 3, 1}), "case2 bfs(2)")

print("PASS")
''',
"c": '''/* @@BLOG@@
 * LeetCode 133651611. @@T@@ — C 版（方案@@N@@）
 * 邻接表（保持插入序），最大 16 节点每点 8 邻居
 */
#include <stdio.h>

#define MAXV 16
#define MAXDEG 8

typedef struct {
    int adj[MAXV][MAXDEG];
    int deg[MAXV];
} Graph;

static void graph_init(Graph *g) {
    for (int i = 0; i < MAXV; i++) g->deg[i] = 0;
}

static void add_edge(Graph *g, int from, int to) {
    g->adj[from][g->deg[from]++] = to;
    g->adj[to][g->deg[to]++] = from;
}

static int visited[MAXV];
static int result[MAXV];
static int result_len;

static void dfs_helper(const Graph *g, int node) {
    if (visited[node]) return;
    visited[node] = 1;
    result[result_len++] = node;
    for (int i = 0; i < g->deg[node]; i++) {
        dfs_helper(g, g->adj[node][i]);
    }
}

static int dfs(const Graph *g, int start, int out[]) {
    for (int i = 0; i < MAXV; i++) visited[i] = 0;
    result_len = 0;
    dfs_helper(g, start);
    for (int i = 0; i < result_len; i++) out[i] = result[i];
    return result_len;
}

static int bfs(const Graph *g, int start, int out[]) {
    for (int i = 0; i < MAXV; i++) visited[i] = 0;
    int queue[MAXV], head = 0, tail = 0;
    int len = 0;
    queue[tail++] = start;
    visited[start] = 1;
    while (head < tail) {
        int node = queue[head++];
        out[len++] = node;
        for (int i = 0; i < g->deg[node]; i++) {
            int nb = g->adj[node][i];
            if (!visited[nb]) {
                visited[nb] = 1;
                queue[tail++] = nb;
            }
        }
    }
    return len;
}

static int eq(const int *a, const int *b, int n) {
    for (int i = 0; i < n; i++) if (a[i] != b[i]) return 0;
    return 1;
}

int main(void) {
    /* case 1: 方形图 0-1-3-2-0 */
    Graph g1;
    graph_init(&g1);
    add_edge(&g1, 0, 1);
    add_edge(&g1, 0, 2);
    add_edge(&g1, 1, 3);
    add_edge(&g1, 2, 3);

    int got[8];
    int want[4];

    want[0]=0; want[1]=1; want[2]=3; want[3]=2;
    if (dfs(&g1, 0, got) != 4 || !eq(got, want, 4)) { printf("case1 dfs(0) failed\\n"); return 1; }
    want[0]=0; want[1]=1; want[2]=2; want[3]=3;
    if (bfs(&g1, 0, got) != 4 || !eq(got, want, 4)) { printf("case1 bfs(0) failed\\n"); return 1; }

    /* case 2: 从另一节点出发 */
    want[0]=2; want[1]=0; want[2]=1; want[3]=3;
    if (dfs(&g1, 2, got) != 4 || !eq(got, want, 4)) { printf("case2 dfs(2) failed\\n"); return 1; }
    want[0]=2; want[1]=0; want[2]=3; want[3]=1;
    if (bfs(&g1, 2, got) != 4 || !eq(got, want, 4)) { printf("case2 bfs(2) failed\\n"); return 1; }

    printf("PASS\\n");
    return 0;
}
''',
"cpp": '''// @@BLOG@@
// LeetCode 133651611. @@T@@ — C++ 版（方案@@N@@）
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <vector>

class Graph {
public:
    void addEdge(int from, int to) {
        adj_[from].push_back(to);
        adj_[to].push_back(from);
    }

    std::vector<int> dfs(int start) const {
        std::set<int> visited;
        std::vector<int> result;
        dfsHelper(start, visited, result);
        return result;
    }

    std::vector<int> bfs(int start) const {
        std::set<int> visited;
        std::vector<int> result;
        std::queue<int> q;
        q.push(start);
        visited.insert(start);
        while (!q.empty()) {
            int node = q.front();
            q.pop();
            result.push_back(node);
            auto it = adj_.find(node);
            if (it == adj_.end()) continue;
            for (int neighbor : it->second) {
                if (!visited.count(neighbor)) {
                    visited.insert(neighbor);
                    q.push(neighbor);
                }
            }
        }
        return result;
    }

private:
    void dfsHelper(int node, std::set<int> &visited, std::vector<int> &result) const {
        if (visited.count(node)) return;
        visited.insert(node);
        result.push_back(node);
        auto it = adj_.find(node);
        if (it == adj_.end()) return;
        for (int neighbor : it->second) {
            dfsHelper(neighbor, visited, result);
        }
    }

    std::map<int, std::vector<int>> adj_;
};

static bool eq(const std::vector<int> &a, const std::vector<int> &b) {
    return a == b;
}

int main() {
    // case 1: 方形图 0-1-3-2-0
    Graph g1;
    g1.addEdge(0, 1);
    g1.addEdge(0, 2);
    g1.addEdge(1, 3);
    g1.addEdge(2, 3);
    if (!eq(g1.dfs(0), {0, 1, 3, 2})) { std::cout << "FAILED case1 dfs(0)" << std::endl; return 1; }
    if (!eq(g1.bfs(0), {0, 1, 2, 3})) { std::cout << "FAILED case1 bfs(0)" << std::endl; return 1; }

    // case 2: 从另一节点出发
    if (!eq(g1.dfs(2), {2, 0, 1, 3})) { std::cout << "FAILED case2 dfs(2)" << std::endl; return 1; }
    if (!eq(g1.bfs(2), {2, 0, 3, 1})) { std::cout << "FAILED case2 bfs(2)" << std::endl; return 1; }

    std::cout << "PASS" << std::endl;
    return 0;
}
''',
"r": '''# @@BLOG@@
# LeetCode 133651611. @@T@@ — R 版（方案@@N@@）
# 邻接表用 environment 引用语义
Graph <- function() {
  e <- new.env(parent = emptyenv())
  e$adj <- list()
  class(e) <- "Graph"
  e
}

add_edge <- function(g, from, to) {
  if (is.null(g$adj[[as.character(from)]])) g$adj[[as.character(from)]] <- c()
  if (is.null(g$adj[[as.character(to)]])) g$adj[[as.character(to)]] <- c()
  g$adj[[as.character(from)]] <- c(g$adj[[as.character(from)]], from * 0 + to)
  g$adj[[as.character(to)]] <- c(g$adj[[as.character(to)]], to * 0 + from)
  invisible(NULL)
}

dfs <- function(g, start) {
  visited <- new.env(parent = emptyenv())
  result <- c()
  helper <- function(node) {
    if (!is.null(visited[[as.character(node)]])) return(invisible(NULL))
    visited[[as.character(node)]] <- TRUE
    result <<- c(result, node)
    for (nb in g$adj[[as.character(node)]] %||% c()) helper(nb)
  }
  helper(start)
  as.integer(result)
}

`%||%` <- function(a, b) if (is.null(a)) b else a

bfs <- function(g, start) {
  visited <- new.env(parent = emptyenv())
  visited[[as.character(start)]] <- TRUE
  result <- c()
  queue <- c(start)
  head <- 1L
  while (head <= length(queue)) {
    node <- queue[head]
    head <- head + 1L
    result <- c(result, node)
    nbs <- g$adj[[as.character(node)]] %||% c()
    for (nb in nbs) {
      if (is.null(visited[[as.character(nb)]])) {
        visited[[as.character(nb)]] <- TRUE
        queue <- c(queue, nb)
      }
    }
  }
  as.integer(result)
}

eq <- function(a, b) identical(as.integer(a), as.integer(b))

# case 1: 方形图 0-1-3-2-0
g1 <- Graph()
add_edge(g1, 0L, 1L)
add_edge(g1, 0L, 2L)
add_edge(g1, 1L, 3L)
add_edge(g1, 2L, 3L)
stopifnot(eq(dfs(g1, 0L), c(0L, 1L, 3L, 2L)))
stopifnot(eq(bfs(g1, 0L), c(0L, 1L, 2L, 3L)))

# case 2: 从另一节点出发
stopifnot(eq(dfs(g1, 2L), c(2L, 0L, 1L, 3L)))
stopifnot(eq(bfs(g1, 2L), c(2L, 0L, 3L, 1L)))

cat("PASS\\n")
''',
"zig": '''// @@BLOG@@
// LeetCode 133651611. @@T@@ — Zig 版（方案@@N@@）
const std = @import("std");

const MAXV = 16;
const MAXDEG = 8;

const Graph = struct {
    adj: [MAXV][MAXDEG]i32 = undefined,
    deg: [MAXV]usize = [_]usize{0} ** MAXV,

    fn addEdge(self: *Graph, from: usize, to: usize) void {
        self.adj[from][self.deg[from]] = @intCast(to);
        self.deg[from] += 1;
        self.adj[to][self.deg[to]] = @intCast(from);
        self.deg[to] += 1;
    }

    fn dfs(self: *const Graph, start: usize, out: []i32) usize {
        var visited = [_]bool{false} ** MAXV;
        var len: usize = 0;
        self.dfsHelper(start, &visited, out, &len);
        return len;
    }

    fn dfsHelper(self: *const Graph, node: usize, visited: *[MAXV]bool, out: []i32, len: *usize) void {
        if (visited[node]) return;
        visited[node] = true;
        out[len.*] = @intCast(node);
        len.* += 1;
        var i: usize = 0;
        while (i < self.deg[node]) : (i += 1) {
            self.dfsHelper(@intCast(self.adj[node][i]), visited, out, len);
        }
    }

    fn bfs(self: *const Graph, start: usize, out: []i32) usize {
        var visited = [_]bool{false} ** MAXV;
        var queue: [MAXV]usize = undefined;
        var head: usize = 0;
        var tail: usize = 0;
        var len: usize = 0;
        queue[tail] = start;
        tail += 1;
        visited[start] = true;
        while (head < tail) {
            const node = queue[head];
            head += 1;
            out[len] = @intCast(node);
            len += 1;
            var i: usize = 0;
            while (i < self.deg[node]) : (i += 1) {
                const nb: usize = @intCast(self.adj[node][i]);
                if (!visited[nb]) {
                    visited[nb] = true;
                    queue[tail] = nb;
                    tail += 1;
                }
            }
        }
        return len;
    }
};

fn eq(a: []const i32, b: []const i32) bool {
    return std.mem.eql(i32, a, b);
}

pub fn main() !void {
    // case 1: 方形图 0-1-3-2-0
    var g1 = Graph{};
    g1.addEdge(0, 1);
    g1.addEdge(0, 2);
    g1.addEdge(1, 3);
    g1.addEdge(2, 3);

    var got: [8]i32 = undefined;
    const want1 = [_]i32{ 0, 1, 3, 2 };
    if (g1.dfs(0, &got) != 4 or !eq(got[0..4], &want1)) return error.TestFailed;
    const want2 = [_]i32{ 0, 1, 2, 3 };
    if (g1.bfs(0, &got) != 4 or !eq(got[0..4], &want2)) return error.TestFailed;

    // case 2: 从另一节点出发
    const want3 = [_]i32{ 2, 0, 1, 3 };
    if (g1.dfs(2, &got) != 4 or !eq(got[0..4], &want3)) return error.TestFailed;
    const want4 = [_]i32{ 2, 0, 3, 1 };
    if (g1.bfs(2, &got) != 4 or !eq(got[0..4], &want4)) return error.TestFailed;

    std.debug.print("PASS\\n", .{});
}
''',
"dart": '''// @@BLOG@@
// LeetCode 133651611. @@T@@ — Dart 版（方案@@N@@）
class Graph {
  final Map<int, List<int>> _adjList = {};

  void addEdge(int from, int to) {
    _adjList.putIfAbsent(from, () => <int>[]);
    _adjList.putIfAbsent(to, () => <int>[]);
    _adjList[from]!.add(to);
    _adjList[to]!.add(from);
  }

  List<int> dfs(int start) {
    final visited = <int>{};
    final result = <int>[];
    void helper(int node) {
      if (visited.contains(node)) return;
      visited.add(node);
      result.add(node);
      for (final neighbor in _adjList[node] ?? <int>[]) {
        helper(neighbor);
      }
    }
    helper(start);
    return result;
  }

  List<int> bfs(int start) {
    final visited = <int>{start};
    final result = <int>[];
    final queue = <int>[start];
    var head = 0;
    while (head < queue.length) {
      final node = queue[head++];
      result.add(node);
      for (final neighbor in _adjList[node] ?? <int>[]) {
        if (!visited.contains(neighbor)) {
          visited.add(neighbor);
          queue.add(neighbor);
        }
      }
    }
    return result;
  }
}

bool eq(List<int> a, List<int> b) {
  if (a.length != b.length) return false;
  for (var i = 0; i < a.length; i++) {
    if (a[i] != b[i]) return false;
  }
  return true;
}

void main() {
  // case 1: 方形图 0-1-3-2-0
  final g1 = Graph();
  g1.addEdge(0, 1);
  g1.addEdge(0, 2);
  g1.addEdge(1, 3);
  g1.addEdge(2, 3);
  if (!eq(g1.dfs(0), [0, 1, 3, 2])) throw StateError('FAILED case1 dfs(0)');
  if (!eq(g1.bfs(0), [0, 1, 2, 3])) throw StateError('FAILED case1 bfs(0)');

  // case 2: 从另一节点出发
  if (!eq(g1.dfs(2), [2, 0, 1, 3])) throw StateError('FAILED case2 dfs(2)');
  if (!eq(g1.bfs(2), [2, 0, 3, 1])) throw StateError('FAILED case2 bfs(2)');

  print('PASS');
}
''',
}

EXTS = {"rust": ".rs", "lua": ".lua", "c": ".c", "cpp": ".cpp", "r": ".R", "zig": ".zig", "dart": ".dart"}

def main():
    for sol in range(1, 9):
        for lang, t in IMPL.items():
            out = t.replace("@@BLOG@@", BLOG).replace("@@T@@", DESC).replace("@@N@@", str(sol))
            emit(lang, REL + "/solution_%d___%d%s" % (sol, sol, EXTS[lang]), out)

if __name__ == "__main__":
    main()
