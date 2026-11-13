// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145198996
// LeetCode 225. 用队列实现栈 — Zig 版（方案2）
const std = @import("std"); // 把 @import(「std」) 存入 std
const MyStack = struct { // 把 struct { 存入 MyStack
    q: [4096]i32,
    head: usize,
    fn init() MyStack {
        return .{ .q = undefined, .head = 0 };
    } // 定义函数/方法 init
    fn push(self: *MyStack, x: i32) void { // 定义函数/方法 push
        var i: usize = self.head; // 把 self.头节点; 写入 var i: usize
        while (i > 0) : (i -= 1) self.q[i] = self.q[i - 1];
        self.q[0] = x; // 把 x; 写入 self.q[0]
        self.head += 1; // self.head累加 1
    }
    fn pop(self: *MyStack) i32 { // 定义函数/方法 pop
        const v = self.q[0]; // 把 self.节点[0] 存入 值
        var i: usize = 0; // 把 0; 写入 var i: usize
        while (i + 1 < self.head) : (i += 1) self.q[i] = self.q[i + 1];
        self.head -= 1; // self.head累减 1
        return v; // 返回 值
    }
    fn top(self: *MyStack) i32 {
        return self.q[0];
    } // 定义函数/方法 top
    fn empty(self: *MyStack) bool {
        return self.head == 0;
    } // 定义函数/方法 empty
};
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var s = MyStack.init(); // 把 MyStack.init() 存入 字符串
    s.push(1); // 把 1 压入栈/数组尾部
    s.push(2); // 把 2 压入栈/数组尾部
    if (s.top() != 2) return error.TestFailed; // 若 字符串.top() 不等于 2，直接返回 error.TestFailed
    if (s.pop() != 2) return error.TestFailed; // 若 字符串 弹出 ) 不等于 2，直接返回 error.TestFailed
    if (s.empty()) return error.TestFailed; // 若 字符串 是否为空，直接返回 error.TestFailed
    std.debug.print("PASS\n", .{});
} // 全部用例通过，输出 PASS
