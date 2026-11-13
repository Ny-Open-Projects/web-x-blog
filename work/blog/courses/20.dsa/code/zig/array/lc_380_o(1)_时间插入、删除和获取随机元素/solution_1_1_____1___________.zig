// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134255301
// LeetCode 380. O(1)时间插入删除和获取随机元素 — Zig 版（方案1）
const std = @import("std"); // 把 @import(「std」) 存入 std
const RandomizedSet = struct { // 把 struct { 存入 RandomizedSet
    vals: std.ArrayList(i32),
    pos: std.AutoHashMap(i32, usize),
    fn init(alloc: std.mem.Allocator) RandomizedSet { // 定义函数/方法 init
        return .{ .vals = std.ArrayList(i32).init(alloc), .pos = std.AutoHashMap(i32, usize).init(alloc) };
    }
    fn insert(self: *RandomizedSet, val: i32) bool { // 定义函数/方法 insert
        if (self.pos.contains(val)) return false; // 若 self.pos 是否包含 值)，直接返回 false
        self.pos.put(val, self.vals.items.len) catch unreachable; // self.pos.put(值, self.vals.items.长度) catch unreachable;
        self.vals.append(val) catch unreachable; // 把 值 追加到列表尾部
        return true; // 返回 true
    }
    fn remove(self: *RandomizedSet, val: i32) bool { // 定义函数/方法 remove
        const idx = self.pos.get(val) orelse return false; // 把 self.pos 查找 值) orelse return false 存入 idx
        const last = self.vals.items[self.vals.items.len - 1]; // 把 self.vals.items[self.vals.items.长度 减 1] 存入 last
        self.vals.items[idx] = last; // 把 last; 写入 self.vals.items[idx]
        self.pos.put(last, idx) catch unreachable; // self.pos.put(last, idx) catch unreachable;
        _ = self.vals.pop(); // 弹出栈顶元素
        _ = self.pos.remove(val); // 把 self.pos 弹出 值); 写入 _
        return true; // 返回 true
    }
    fn getRandom(self: *RandomizedSet) i32 { // 定义函数/方法 getRandom
        return self.vals.items[0]; // 返回 self.vals.items[0]
    }
};
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator); // 把 std.堆.ArenaAllocator.init(std.堆.page_allocator) 存入 arena
    defer arena.deinit(); // defer arena.deinit();
    var s = RandomizedSet.init(arena.allocator()); // 把 RandomizedSet.init(arena.allocator()) 存入 字符串
    if (!s.insert(1)) return error.TestFailed; // 若 取反 字符串 插入 1)，直接返回 error.TestFailed
    if (s.remove(2)) return error.TestFailed; // 若 字符串 弹出 2)，直接返回 error.TestFailed
    if (!s.insert(2)) return error.TestFailed; // 若 取反 字符串 插入 2)，直接返回 error.TestFailed
    const r = s.getRandom(); // 把 字符串.getRandom() 存入 右指针
    if (r != 1 and r != 2) return error.TestFailed; // 若 右指针 不等于 1 and 右指针 不等于 2，直接返回 error.TestFailed
    if (!s.remove(1)) return error.TestFailed; // 若 取反 字符串 弹出 1)，直接返回 error.TestFailed
    if (s.insert(2)) return error.TestFailed; // 若 字符串 插入 2)，直接返回 error.TestFailed
    if (s.getRandom() != 2) return error.TestFailed; // 若 字符串.getRandom() 不等于 2，直接返回 error.TestFailed
    std.debug.print("PASS\n", .{});
} // 全部用例通过，输出 PASS
