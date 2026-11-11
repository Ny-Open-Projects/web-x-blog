// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145114011
// LeetCode 232. 用栈实现队列 — Zig 版（方案1）
const std = @import("std"); // 把 @import(「std」) 存入 std
const MyQueue = struct { // 把 struct { 存入 MyQueue
    in_: [4096]i32,
    in_n: usize,
    out_: [4096]i32,
    out_n: usize,
    fn init() MyQueue {
        return .{ .in_ = undefined, .in_n = 0, .out_ = undefined, .out_n = 0 };
    } // 定义函数/方法 init
    fn in2out(self: *MyQueue) void { // 定义函数/方法 in2out
        while (self.in_n > 0) { // 循环，直到不满足「self.in_n 超过 0」
            self.in_n -= 1; // self.in_n累减 1
            self.out_[self.out_n] = self.in_[self.in_n]; // 把 self.in_[self.in_n]; 写入 self.out_[self.out_n]
            self.out_n += 1; // self.out_n累加 1
        }
    }
    fn push(self: *MyQueue, x: i32) void { // 定义函数/方法 push
        self.in_[self.in_n] = x; // 把 x; 写入 self.in_[self.in_n]
        self.in_n += 1; // self.in_n累加 1
    }
    fn pop(self: *MyQueue) i32 { // 定义函数/方法 pop
        if (self.out_n == 0) self.in2out(); // 若 self.out_n 等于 0) self.in2out();
        self.out_n -= 1; // self.out_n累减 1
        return self.out_[self.out_n]; // 返回 self.out_[self.out_n]
    }
    fn peek(self: *MyQueue) i32 { // 定义函数/方法 peek
        if (self.out_n == 0) self.in2out(); // 若 self.out_n 等于 0) self.in2out();
        return self.out_[self.out_n - 1]; // 返回 self.out_[self.out_n 减 1]
    }
    fn empty(self: *MyQueue) bool {
        return self.in_n == 0 and self.out_n == 0;
    } // 定义函数/方法 empty
};
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var q = MyQueue.init(); // 把 MyQueue.init() 存入 节点
    q.push(1); // 把 1 压入栈/数组尾部
    q.push(2); // 把 2 压入栈/数组尾部
    if (q.peek() != 1) return error.TestFailed; // 若 节点.peek() 不等于 1，直接返回 error.TestFailed
    if (q.pop() != 1) return error.TestFailed; // 若 节点 弹出 ) 不等于 1，直接返回 error.TestFailed
    if (q.empty()) return error.TestFailed; // 若 节点 是否为空，直接返回 error.TestFailed
    std.debug.print("PASS\n", .{});
} // 全部用例通过，输出 PASS
