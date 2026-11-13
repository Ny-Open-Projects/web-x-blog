// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134097112
// 实现LRU缓存算法功能 — Zig 版（方案3）
const std = @import("std"); // 把 @import(「std」) 存入 std
const NoteLru = struct { // 把 struct { 存入 NoteLru
    cap: usize,
    keys: [256]i32,
    vals: [256]i32,
    n: usize,
    fn init(cap: usize) NoteLru { // 定义函数/方法 init
        return .{ .cap = cap, .keys = undefined, .vals = undefined, .n = 0 };
    }
    fn find(self: *NoteLru, k: i32) ?usize { // 定义函数/方法 find
        for (0..self.n) |i| if (self.keys[i] == k) return i; // 逐个取出 0..self.元素个数 的元素（下标 i）
        return null; // 返回 null
    }
    fn removeIdx(self: *NoteLru, idx: usize) void { // 定义函数/方法 removeIdx
        var i = idx; // 把 idx 存入 下标 i
        while (i + 1 < self.n) : (i += 1) { // 循环，直到不满足「下标 i 加 1 小于 self.元素个数) : (下标 i 累加 1」
            self.keys[i] = self.keys[i + 1]; // 把 self.keys[下标 i 加 1]; 写入 self.keys[i]
            self.vals[i] = self.vals[i + 1]; // 把 self.vals[下标 i 加 1]; 写入 self.vals[i]
        }
        self.n -= 1; // self.n累减 1
    }
    fn get(self: *NoteLru, k: i32) i32 { // 定义函数/方法 get
        const i = self.find(k) orelse return -1; // 把 self 查找 下标 k) orelse return 减 1 存入 下标 i
        const v = self.vals[i]; // 把 self.vals[下标 i] 存入 值
        const kv = self.keys[i]; // 把 self.keys[下标 i] 存入 kv
        self.removeIdx(i); // self.removeIdx(下标 i);
        self.keys[self.n] = kv; // 把 kv; 写入 self.keys[self.n]
        self.vals[self.n] = v; // 把 值; 写入 self.vals[self.n]
        self.n += 1; // self.n累加 1
        return v; // 返回 值
    }
    fn put(self: *NoteLru, k: i32, v: i32) void { // 定义函数/方法 put
        if (self.find(k)) |i| self.removeIdx(i) else if (self.n == self.cap) self.removeIdx(0);
        self.keys[self.n] = k; // 把 下标 k; 写入 self.keys[self.n]
        self.vals[self.n] = v; // 把 值; 写入 self.vals[self.n]
        self.n += 1; // self.n累加 1
    }
};
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var c = NoteLru.init(2); // 把 NoteLru.init(2) 存入 字符
    c.put(1, 1); // 字符.put(1, 1);
    c.put(2, 2); // 字符.put(2, 2);
    if (c.get(1) != 1) return error.TestFailed; // 若 字符 查找 1) 不等于 1，直接返回 error.TestFailed
    c.put(3, 3); // 字符.put(3, 3);
    if (c.get(2) != -1) return error.TestFailed; // 若 字符 查找 2) 不等于 减 1，直接返回 error.TestFailed
    c.put(4, 4); // 字符.put(4, 4);
    if (c.get(1) != -1) return error.TestFailed; // 若 字符 查找 1) 不等于 减 1，直接返回 error.TestFailed
    if (c.get(3) != 3 or c.get(4) != 4) return error.TestFailed; // 若 字符 查找 3) 不等于 3 or 字符 查找 4) 不等于 4，直接返回 error.TestFailed
    std.debug.print("PASS\n", .{});
} // 全部用例通过，输出 PASS
