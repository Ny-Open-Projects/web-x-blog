// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145361774
// LeetCode 641. 设计循环双端队列 — Zig 版（方案1）
const std = @import("std"); // 把 @import(「std」) 存入 std
const MyCircularDeque = struct { // 把 struct { 存入 MyCircularDeque
    data: [4096]i32,
    head: usize,
    tail: usize,
    cap: usize,
    size: usize,
    fn new(k: usize) MyCircularDeque { // 定义函数/方法 new
        return .{ .data = undefined, .head = 0, .tail = 0, .cap = k, .size = 0 };
    }
    fn insertFront(self: *MyCircularDeque, v: i32) bool { // 定义函数/方法 insertFront
        if (self.size == self.cap) return false; // 若 self.大小 等于 self.cap，直接返回 false
        self.head = (self.head + self.cap - 1) % self.cap; // 把 (self.头节点 加 self.cap 减 1) 对…取模 self.cap; 写入 头节点
        self.data[self.head] = v; // 把 值; 写入 self.data[self.head]
        self.size += 1; // self.size累加 1
        return true; // 返回 true
    }
    fn insertLast(self: *MyCircularDeque, v: i32) bool { // 定义函数/方法 insertLast
        if (self.size == self.cap) return false; // 若 self.大小 等于 self.cap，直接返回 false
        self.data[self.tail] = v; // 把 值; 写入 self.data[self.tail]
        self.tail = (self.tail + 1) % self.cap; // 把 (self.尾节点 加 1) 对…取模 self.cap; 写入 尾节点
        self.size += 1; // self.size累加 1
        return true; // 返回 true
    }
    fn deleteFront(self: *MyCircularDeque) bool { // 定义函数/方法 deleteFront
        if (self.size == 0) return false; // 若 self.大小 等于 0，直接返回 false
        self.head = (self.head + 1) % self.cap; // 把 (self.头节点 加 1) 对…取模 self.cap; 写入 头节点
        self.size -= 1; // self.size累减 1
        return true; // 返回 true
    }
    fn deleteLast(self: *MyCircularDeque) bool { // 定义函数/方法 deleteLast
        if (self.size == 0) return false; // 若 self.大小 等于 0，直接返回 false
        self.tail = (self.tail + self.cap - 1) % self.cap; // 把 (self.尾节点 加 self.cap 减 1) 对…取模 self.cap; 写入 尾节点
        self.size -= 1; // self.size累减 1
        return true; // 返回 true
    }
    fn getFront(self: *MyCircularDeque) i32 {
        return if (self.size == 0) -1 else self.data[self.head];
    } // 定义函数/方法 getFront
    fn getRear(self: *MyCircularDeque) i32 {
        return if (self.size == 0) -1 else self.data[(self.tail + self.cap - 1) % self.cap];
    } // 定义函数/方法 getRear
    fn isEmpty(self: *MyCircularDeque) bool {
        return self.size == 0;
    } // 定义判定函数 isEmpty
    fn isFull(self: *MyCircularDeque) bool {
        return self.size == self.cap;
    } // 定义判定函数 isFull
};
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var d = MyCircularDeque.new(3); // 把 MyCircularDeque.new(3) 存入 d
    if (!d.insertLast(1)) return error.TestFailed; // 若 取反 d.insertLast(1)，直接返回 error.TestFailed
    if (!d.insertLast(2)) return error.TestFailed; // 若 取反 d.insertLast(2)，直接返回 error.TestFailed
    if (!d.insertFront(3)) return error.TestFailed; // 若 取反 d.insertFront(3)，直接返回 error.TestFailed
    if (d.insertFront(4)) return error.TestFailed; // 若 d.insertFront(4)，直接返回 error.TestFailed
    if (d.getRear() != 2) return error.TestFailed; // 若 d.getRear() 不等于 2，直接返回 error.TestFailed
    if (!d.isFull()) return error.TestFailed; // 若 取反 d.isFull()，直接返回 error.TestFailed
    if (!d.deleteLast()) return error.TestFailed; // 若 取反 d.deleteLast()，直接返回 error.TestFailed
    if (!d.insertFront(4)) return error.TestFailed; // 若 取反 d.insertFront(4)，直接返回 error.TestFailed
    if (d.getFront() != 4) return error.TestFailed; // 若 d.getFront() 不等于 4，直接返回 error.TestFailed
    std.debug.print("PASS\n", .{});
} // 全部用例通过，输出 PASS
