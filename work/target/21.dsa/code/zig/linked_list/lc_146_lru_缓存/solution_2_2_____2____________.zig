// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134537871
// LeetCode 146. LRU缓存 — Zig 版（方案2）
const std = @import("std"); // 把 @import(「std」) 存入 std
const LruSim = struct { // 把 struct { 存入 LruSim
    cap: usize,
    keys: [256]i32,
    vals: [256]i32,
    stamp: [256]i64,
    n: usize,
    clock_: i64,
    fn init(cap: usize) LruSim { // 定义函数/方法 init
        return .{ .cap = cap, .keys = undefined, .vals = undefined, .stamp = undefined, .n = 0, .clock_ = 0 };
    }
    fn find(self: *LruSim, k: i32) ?usize { // 定义函数/方法 find
        for (0..self.n) |i| if (self.keys[i] == k) return i; // 逐个取出 0..self.元素个数 的元素（下标 i）
        return null; // 返回 null
    }
    fn removeIdx(self: *LruSim, idx: usize) void { // 定义函数/方法 removeIdx
        var i = idx; // 把 idx 存入 下标 i
        while (i + 1 < self.n) : (i += 1) { // 循环，直到不满足「下标 i 加 1 小于 self.元素个数) : (下标 i 累加 1」
            self.keys[i] = self.keys[i + 1]; // 把 self.keys[下标 i 加 1]; 写入 self.keys[i]
            self.vals[i] = self.vals[i + 1]; // 把 self.vals[下标 i 加 1]; 写入 self.vals[i]
            self.stamp[i] = self.stamp[i + 1]; // 把 self.stamp[下标 i 加 1]; 写入 self.stamp[i]
        }
        self.n -= 1; // self.n累减 1
    }
    fn get(self: *LruSim, k: i32) i32 { // 定义函数/方法 get
        const i = self.find(k) orelse return -1; // 把 self 查找 下标 k) orelse return 减 1 存入 下标 i
        self.clock_ += 1; // self.clock_累加 1
        self.stamp[i] = self.clock_; // 把 self.clock_; 写入 self.stamp[i]
        return self.vals[i]; // 返回 self.vals[下标 i]
    }
    fn put(self: *LruSim, k: i32, v: i32) void { // 定义函数/方法 put
        if (self.find(k)) |i| { // 若 self 查找 下标 k)) 按位或 下标 i 按位或
            self.vals[i] = v; // 把 值; 写入 self.vals[i]
            self.clock_ += 1; // self.clock_累加 1
            self.stamp[i] = self.clock_; // 把 self.clock_; 写入 self.stamp[i]
            return; // return;
        }
        if (self.n == self.cap) { // 若 self.元素个数 等于 self.cap
            var oldest: usize = 0; // 把 0; 写入 var oldest: usize
            for (1..self.n) |j| { // 逐个取出 1..self.元素个数 的元素（下标 j）
                if (self.stamp[j] < self.stamp[oldest]) oldest = j; // 若 self.stamp[下标 j] 小于 self.stamp[oldest]) oldest 赋值为 下标 j;
            }
            self.removeIdx(oldest); // self.removeIdx(oldest);
        }
        self.clock_ += 1; // self.clock_累加 1
        self.keys[self.n] = k; // 把 下标 k; 写入 self.keys[self.n]
        self.vals[self.n] = v; // 把 值; 写入 self.vals[self.n]
        self.stamp[self.n] = self.clock_; // 把 self.clock_; 写入 self.stamp[self.n]
        self.n += 1; // self.n累加 1
    }
};
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var lru = LruSim.init(2); // 把 LruSim.init(2) 存入 lru
    lru.put(1, 1); // lru.put(1, 1);
    lru.put(2, 2); // lru.put(2, 2);
    if (lru.get(1) != 1) return error.TestFailed; // 若 lru 查找 1) 不等于 1，直接返回 error.TestFailed
    lru.put(3, 3); // lru.put(3, 3);
    if (lru.get(2) != -1) return error.TestFailed; // 若 lru 查找 2) 不等于 减 1，直接返回 error.TestFailed
    lru.put(4, 4); // lru.put(4, 4);
    if (lru.get(1) != -1) return error.TestFailed; // 若 lru 查找 1) 不等于 减 1，直接返回 error.TestFailed
    if (lru.get(3) != 3 or lru.get(4) != 4) return error.TestFailed; // 若 lru 查找 3) 不等于 3 or lru 查找 4) 不等于 4，直接返回 error.TestFailed
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
