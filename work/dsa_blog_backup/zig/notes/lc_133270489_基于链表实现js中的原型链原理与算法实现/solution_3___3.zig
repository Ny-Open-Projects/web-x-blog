// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133270489
// LeetCode 133270489. 原型链原理 — Zig 版（方案3：get 查找 + instanceOf 判定）
const std = @import("std"); // 把 @import(「std」) 存入 std

const MAX_PROPS = 8; // 把 8 存入 MAX_PROPS
const Prop = struct { key: []const u8, val: []const u8 }; // 把 struct { key: []const u8, 值: []const u8 } 存入 Prop
const Proto = struct { // 把 struct { 存入 Proto
    name: []const u8,
    props: [MAX_PROPS]Prop = undefined,
    nprops: usize = 0,
    parent: ?*Proto = null,

    fn set(self: *Proto, key: []const u8, val: []const u8) void { // 定义函数/方法 set
        self.props[self.nprops] = .{ .key = key, .val = val }; // 把 { .key 赋值为 key, .值 赋值为 值 }; 写入 self.props[self.nprops]
        self.nprops += 1; // self.nprops累加 1
    }
    fn get(self: *const Proto, key: []const u8) ?[]const u8 { // 定义函数/方法 get
        var cur: ?*const Proto = self; // 把 self; 写入 var cur: ?*const Proto
        while (cur) |node| { // 循环，直到不满足「当前值) 按位或 节点 按位或」
            var i: usize = 0; // 把 0; 写入 var i: usize
            while (i < node.nprops) : (i += 1) { // 循环，直到不满足「下标 i 小于 节点.nprops) : (下标 i 累加 1」
                if (std.mem.eql(u8, node.props[i].key, key)) return node.props[i].val;
            }
            cur = node.parent; // 把 节点.parent; 写入 当前值
        }
        return null; // 返回 null
    }
};

fn instanceOf(obj: *const Proto, prototype: *const Proto) bool { // 定义函数/方法 instanceOf
    var p: ?*const Proto = obj; // 把 obj; 写入 var p: ?*const Proto
    while (p) |cur| { // 循环，直到不满足「节点) 按位或 当前值 按位或」
        if (cur == prototype) return true; // 若 当前值 等于 prototype，直接返回 true
        p = cur.parent; // 把 当前值.parent; 写入 节点
    }
    return false; // 返回 false
}

pub fn main() !void { // 程序入口：跑内嵌自测用例
    var gpa = std.heap.GeneralPurposeAllocator(.{}){}; // 把 std.堆.GeneralPurposeAllocator(.{}){} 存入 gpa
    const allocator = gpa.allocator(); // 把 gpa.allocator() 存入 allocator

    const object_proto = try allocator.create(Proto); // 把 try allocator.create(Proto) 存入 object_proto
    object_proto.* = .{ .name = "Object.prototype" }; // 把 { .name 赋值为 「Object.prototype」 }; 写入 object_proto.*
    _ = object_proto.set("a", "aaa"); // 把 object_proto.set(「数组」, 「数组」); 写入 _
    const function_proto = try allocator.create(Proto); // 把 try allocator.create(Proto) 存入 function_proto
    function_proto.* = .{ .name = "Function.prototype", .parent = object_proto };
    _ = function_proto.set("b", "bbb"); // 把 function_proto.set(「b」, 「b」); 写入 _
    const obj = try allocator.create(Proto); // 把 try allocator.create(Proto) 存入 obj
    obj.* = .{ .name = "obj", .parent = object_proto }; // 把 { .name 赋值为 「obj」, .parent 赋值为 object_proto }; 写入 obj.*
    const func = try allocator.create(Proto); // 把 try allocator.create(Proto) 存入 func
    func.* = .{ .name = "func", .parent = function_proto };

    if (!std.mem.eql(u8, obj.get("a").?, "aaa")) return error.TestFailed;
    if (obj.get("b") != null) return error.TestFailed; // 若 obj 查找 「b」) 不等于 null，直接返回 error.TestFailed
    if (!std.mem.eql(u8, func.get("a").?, "aaa")) return error.TestFailed;
    if (!std.mem.eql(u8, func.get("b").?, "bbb")) return error.TestFailed;
    if (!instanceOf(func, object_proto)) return error.TestFailed; // 若 取反 instanceOf(func, object_proto)，直接返回 error.TestFailed
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
