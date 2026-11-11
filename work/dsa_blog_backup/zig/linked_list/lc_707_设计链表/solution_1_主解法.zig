// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134120377
// LeetCode 707. 设计链表 — Zig 版（方案1）
const std = @import("std"); // 把 @import(「std」) 存入 std
const MyList = struct { // 把 struct { 存入 MyList
    items: [4096]i32,
    n: usize,
    fn init() MyList { // 定义函数/方法 init
        return .{ .items = undefined, .n = 0 }; // 返回 { .items 赋值为 undefined, .元素个数 赋值为 0 }
    }
    fn addAtHead(self: *MyList, x: i32) void { // 定义函数/方法 addAtHead
        var i: usize = self.n; // 把 self.元素个数; 写入 var i: usize
        while (i > 0) : (i -= 1) self.items[i] = self.items[i - 1];
        self.items[0] = x; // 把 x; 写入 self.items[0]
        self.n += 1; // self.n累加 1
    }
    fn addAtTail(self: *MyList, x: i32) void { // 定义函数/方法 addAtTail
        self.items[self.n] = x; // 把 x; 写入 self.items[self.n]
        self.n += 1; // self.n累加 1
    }
    fn addAtIndex(self: *MyList, idx: i32, x: i32) void { // 定义函数/方法 addAtIndex
        var idxv = idx; // 把 idx 存入 idxv
        if (idxv < 0) idxv = 0; // 若 idxv 小于 0) idxv 赋值为 0;
        const u: usize = @intCast(idxv); // 把 @intCast(idxv); 写入 const u: usize
        if (u > self.n) return; // 若 节点 u 超过 self.元素个数) return;
        var i: usize = self.n; // 把 self.元素个数; 写入 var i: usize
        while (i > u) : (i -= 1) self.items[i] = self.items[i - 1];
        self.items[u] = x; // 把 x; 写入 self.items[u]
        self.n += 1; // self.n累加 1
    }
    fn get(self: *MyList, idx: i32) i32 { // 定义函数/方法 get
        if (idx < 0 or idx >= @as(i32, @intCast(self.n))) return -1; // 若 idx 小于 0 or idx 不低于 @as(i32, @intCast(self.元素个数))，直接返回 减 1
        return self.items[@intCast(idx)]; // 返回 self.items[@intCast(idx)]
    }
    fn deleteAtIndex(self: *MyList, idx: i32) void { // 定义函数/方法 deleteAtIndex
        if (idx < 0 or idx >= @as(i32, @intCast(self.n))) return; // 若 idx 小于 0 or idx 不低于 @as(i32, @intCast(self.元素个数))) return;
        var i: usize = @intCast(idx); // 把 @intCast(idx); 写入 var i: usize
        while (i + 1 < self.n) : (i += 1) self.items[i] = self.items[i + 1];
        self.n -= 1; // self.n累减 1
    }
};
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var l = MyList.init(); // 把 MyList.init() 存入 左指针
    l.addAtHead(1); // 左指针.addAtHead(1);
    l.addAtTail(3); // 左指针.addAtTail(3);
    l.addAtIndex(1, 2); // 左指针.addAtIndex(1, 2);
    if (l.get(1) != 2) return error.TestFailed; // 若 左指针 查找 1) 不等于 2，直接返回 error.TestFailed
    l.deleteAtIndex(1); // 左指针.deleteAtIndex(1);
    if (l.get(1) != 3) return error.TestFailed; // 若 左指针 查找 1) 不等于 3，直接返回 error.TestFailed
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
