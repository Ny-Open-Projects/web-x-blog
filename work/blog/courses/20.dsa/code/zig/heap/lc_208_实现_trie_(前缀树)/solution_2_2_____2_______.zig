// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135533027
// LeetCode 208. 实现 Trie (前缀树) — Zig 版（方案2）
const std = @import("std"); // 把 @import(「std」) 存入 std
const TrieNode = struct { children: [26]?*TrieNode, is_end: bool };
fn tnNew(alloc: std.mem.Allocator) *TrieNode { // 定义函数/方法 tnNew
    const n = alloc.create(TrieNode) catch unreachable; // 把 alloc.create(TrieNode) catch unreachable 存入 元素个数
    n.* = .{ .children = [_]?*TrieNode{null} ** 26, .is_end = false };
    return n; // 返回 元素个数
}
const Trie = struct { // 把 struct { 存入 Trie
    root: *TrieNode,
    fn init(alloc: std.mem.Allocator) Trie {
        return .{ .root = tnNew(alloc) };
    } // 定义函数/方法 init
    fn insert(self: *Trie, word: []const u8, alloc: std.mem.Allocator) void { // 定义函数/方法 insert
        var node = self.root; // 把 self.根节点 存入 节点
        for (word) |ch| { // 逐个取出 单词 的元素（字符）
            const idx = ch - 'a'; // 把 字符 减 '数组' 存入 idx
            if (node.children[idx] == null) node.children[idx] = tnNew(alloc);
            node = node.children[idx].?; // 把 节点.children[idx].?; 写入 节点
        }
        node.is_end = true; // 把 true; 写入 node.is_end
    }
    fn walk(self: *Trie, s: []const u8) ?*TrieNode { // 定义函数/方法 walk
        var node = self.root; // 把 self.根节点 存入 节点
        for (s) |ch| { // 逐个取出 字符串 的元素（字符）
            if (ch < 'a' or ch > 'z') return null; // 若 字符 小于 '数组' or 字符 超过 'z'，直接返回 null
            const idx = ch - 'a'; // 把 字符 减 '数组' 存入 idx
            if (node.children[idx] == null) return null; // 若 节点.children[idx] 等于 null，直接返回 null
            node = node.children[idx].?; // 把 节点.children[idx].?; 写入 节点
        }
        return node; // 返回 节点
    }
    fn search(self: *Trie, word: []const u8) bool { // 定义函数/方法 search
        const n = self.walk(word) orelse return false; // 把 self.walk(单词) orelse return false 存入 元素个数
        return n.is_end; // 返回 元素个数.is_end
    }
    fn startsWith(self: *Trie, prefix: []const u8) bool { // 定义函数/方法 startsWith
        return self.walk(prefix) != null; // 返回 self.walk(prefix) 不等于 null
    }
};
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator); // 把 std.堆.ArenaAllocator.init(std.堆.page_allocator) 存入 arena
    defer arena.deinit(); // defer arena.deinit();
    const alloc = arena.allocator(); // 把 arena.allocator() 存入 alloc
    var t = Trie.init(alloc); // 把 Trie.init(alloc) 存入 另一字符串
    t.insert("apple", alloc); // 另一字符串 插入 「apple」, alloc);
    if (!t.search("apple")) return error.TestFailed; // 若 取反 另一字符串.search(「apple」)，直接返回 error.TestFailed
    if (t.search("app")) return error.TestFailed; // 若 另一字符串.search(「app」)，直接返回 error.TestFailed
    if (!t.startsWith("app")) return error.TestFailed; // 若 取反 另一字符串.startsWith(「app」)，直接返回 error.TestFailed
    if (t.search("appl")) return error.TestFailed; // 若 另一字符串.search(「appl」)，直接返回 error.TestFailed
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
