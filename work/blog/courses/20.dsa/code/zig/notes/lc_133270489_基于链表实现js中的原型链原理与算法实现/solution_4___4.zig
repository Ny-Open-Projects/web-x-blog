// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133270489
// LeetCode 133270489. 原型链原理 — Zig 版（方案4：null/undefined 边界：instanceOf 均返回 false）
const std = @import("std"); // 把 @import(「std」) 存入 std

const Obj = struct { // 把 struct { 存入 Obj
    proto: ?*anyopaque = null,
};

const Ctor = struct { // 把 struct { 存入 Ctor
    prototype: ?*anyopaque = null,
};

fn instanceOf(a: ?*const Obj, b: *const Ctor) bool { // 定义函数/方法 instanceOf
    var p: ?*const Obj = a; // 把 数组; 写入 var p: ?*const Obj
    while (p) |cur| { // 循环，直到不满足「节点) 按位或 当前值 按位或」
        if (cur.proto == b.prototype) return true; // 若 当前值.proto 等于 b.prototype，直接返回 true
        // 演示用：__proto__ 无法继续解引用，直接终止
        p = null; // 把 null; 写入 节点
    }
    return false; // 返回 false
}

pub fn main() !void { // 程序入口：跑内嵌自测用例
    const ctor = Ctor{ .prototype = null }; // 把 Ctor{ .prototype 赋值为 null } 存入 ctor
    if (instanceOf(null, &ctor)) return error.TestFailed; // 若 instanceOf(null, 按位与 ctor)，直接返回 error.TestFailed
    if (instanceOf(null, &ctor)) return error.TestFailed; // 若 instanceOf(null, 按位与 ctor)，直接返回 error.TestFailed
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
