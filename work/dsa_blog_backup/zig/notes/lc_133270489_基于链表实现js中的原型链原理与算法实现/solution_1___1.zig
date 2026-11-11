// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133270489
// LeetCode 133270489. 原型链原理 — Zig 版（方案1：instanceOf 沿原型链判定）
const std = @import("std"); // 把 @import(「std」) 存入 std

const Proto = struct { // 把 struct { 存入 Proto
    name: []const u8,
    parent: ?*Proto,
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
    object_proto.* = .{ .name = "Object.prototype", .parent = null };
    const function_proto = try allocator.create(Proto); // 把 try allocator.create(Proto) 存入 function_proto
    function_proto.* = .{ .name = "Function.prototype", .parent = object_proto };
    const array_proto = try allocator.create(Proto); // 把 try allocator.create(Proto) 存入 array_proto
    array_proto.* = .{ .name = "Array.prototype", .parent = object_proto };
    const obj = try allocator.create(Proto); // 把 try allocator.create(Proto) 存入 obj
    obj.* = .{ .name = "obj", .parent = object_proto }; // 把 { .name 赋值为 「obj」, .parent 赋值为 object_proto }; 写入 obj.*
    const func = try allocator.create(Proto); // 把 try allocator.create(Proto) 存入 func
    func.* = .{ .name = "func", .parent = function_proto };
    const arr = try allocator.create(Proto); // 把 try allocator.create(Proto) 存入 数组
    arr.* = .{ .name = "arr", .parent = array_proto }; // 把 { .name 赋值为 「数组」, .parent 赋值为 array_proto }; 写入 arr.*

    if (!instanceOf(obj, object_proto)) return error.TestFailed; // 若 取反 instanceOf(obj, object_proto)，直接返回 error.TestFailed
    if (!instanceOf(func, function_proto)) return error.TestFailed; // 若 取反 instanceOf(func, function_proto)，直接返回 error.TestFailed
    if (!instanceOf(func, object_proto)) return error.TestFailed; // 若 取反 instanceOf(func, object_proto)，直接返回 error.TestFailed
    if (!instanceOf(arr, array_proto)) return error.TestFailed; // 若 取反 instanceOf(数组, array_proto)，直接返回 error.TestFailed
    if (!instanceOf(arr, object_proto)) return error.TestFailed; // 若 取反 instanceOf(数组, object_proto)，直接返回 error.TestFailed
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
