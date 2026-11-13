// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133278676
// LeetCode 133278676. 使用链表（指针链）获取 JSON 节点值 — Zig 版（方案A：安全遍历（单用例），缺失返回 null）
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

    fn child(self: *const JNode, key: []const u8) ?*JNode { // 定义函数/方法 child
        var i: usize = 0; // 把 0; 写入 var i: usize
        while (i < self.nchildren) : (i += 1) { // 循环，直到不满足「下标 i 小于 self.nchildren) : (下标 i 累加 1」
            if (std.mem.eql(u8, self.keys[i], key)) return self.children[i];
        }
        return null; // 返回 null
    }
};

fn getValue(data: *JNode, path: []const []const u8) ?*JNode { // 定义函数/方法 getValue
    var node = data; // 把 data 存入 节点
    for (path) |key| { // 逐个取出 当前路径 的元素（key）
        if (!node.is_obj) return null; // 若 取反 节点.is_obj，直接返回 null
        node = node.child(key) orelse return null; // 把 节点.子节点(key) orelse return null; 写入 节点
    }
    return node; // 返回 节点
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

    const r1 = getValue(data, &.{ "a", "b", "c" }) orelse return error.TestFailed;
    if (r1.val != 1) return error.TestFailed; // 若 r1.值 不等于 1，直接返回 error.TestFailed
    if (getValue(data, &.{ "a", "z" }) != null) return error.TestFailed;
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
