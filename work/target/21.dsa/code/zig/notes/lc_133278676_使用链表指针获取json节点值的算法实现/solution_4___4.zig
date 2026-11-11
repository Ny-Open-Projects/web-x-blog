// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133278676
// LeetCode 133278676. 使用链表（指针链）获取 JSON 节点值 — Zig 版（方案B：逐键求值，合法路径直接索引）
const std = @import("std"); // 把 @import(「std」) 存入 std

const MAX_CHILDREN = 8; // 把 8 存入 MAX_CHILDREN
const JNode = struct { // 把 struct { 存入 JNode
    is_obj: bool,
    val: i32 = 0,
    keys: [MAX_CHILDREN][]const u8 = undefined,
    children: [MAX_CHILDREN]*JNode = undefined,
    nchildren: usize = 0,

    fn addChild(self: *JNode, key: []const u8, node: *JNode) void { // 定义函数/方法 addChild
        self.keys[self.nchildren] = key; // 把 key; 写入 self.keys[self.nchildren]
        self.children[self.nchildren] = node; // 把 节点; 写入 self.children[self.nchildren]
        self.nchildren += 1; // self.nchildren累加 1
    }

    fn child(self: *const JNode, key: []const u8) *JNode { // 定义函数/方法 child
        var i: usize = 0; // 把 0; 写入 var i: usize
        while (i < self.nchildren) : (i += 1) { // 循环，直到不满足「下标 i 小于 self.nchildren) : (下标 i 累加 1」
            if (std.mem.eql(u8, self.keys[i], key)) return self.children[i];
        }
        unreachable; // 合法路径语义
    }
};

fn getValueEval(data: *JNode, path: []const []const u8) *JNode { // 定义函数/方法 getValueEval
    var cur = data; // 把 data 存入 当前值
    for (path) |key| { // 逐个取出 当前路径 的元素（key）
        cur = cur.child(key); // 把 当前值.子节点(key); 写入 当前值
    }
    return cur; // 返回 当前值
}

pub fn main() !void { // 程序入口：跑内嵌自测用例
    var gpa = std.heap.GeneralPurposeAllocator(.{}){}; // 把 std.堆.GeneralPurposeAllocator(.{}){} 存入 gpa
    const allocator = gpa.allocator(); // 把 gpa.allocator() 存入 allocator

    const data = try allocator.create(JNode); // 把 try allocator.create(JNode) 存入 data
    data.* = .{ .is_obj = true }; // 把 { .is_obj 赋值为 true }; 写入 data.*
    const a = try allocator.create(JNode); // 把 try allocator.create(JNode) 存入 数组
    a.* = .{ .is_obj = true }; // 把 { .is_obj 赋值为 true }; 写入 a.*
    const b = try allocator.create(JNode); // 把 try allocator.create(JNode) 存入 b
    b.* = .{ .is_obj = true }; // 把 { .is_obj 赋值为 true }; 写入 b.*
    const c = try allocator.create(JNode); // 把 try allocator.create(JNode) 存入 字符
    c.* = .{ .is_obj = false, .val = 1 }; // 把 { .is_obj 赋值为 false, .值 赋值为 1 }; 写入 c.*
    b.addChild("c", c); // b.addChild(「字符」, 字符);
    a.addChild("b", b); // 数组.addChild(「b」, b);
    data.addChild("a", a); // data.addChild(「数组」, 数组);
    const d = try allocator.create(JNode); // 把 try allocator.create(JNode) 存入 d
    d.* = .{ .is_obj = true }; // 把 { .is_obj 赋值为 true }; 写入 d.*
    const e = try allocator.create(JNode); // 把 try allocator.create(JNode) 存入 e
    e.* = .{ .is_obj = false, .val = 2 }; // 把 { .is_obj 赋值为 false, .值 赋值为 2 }; 写入 e.*
    d.addChild("e", e); // d.addChild(「e」, e);
    data.addChild("d", d); // data.addChild(「d」, d);

    if (getValueEval(data, &.{ "a", "b", "c" }).val != 1) return error.TestFailed;
    if (getValueEval(data, &.{ "d", "e" }).val != 2) return error.TestFailed;
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
