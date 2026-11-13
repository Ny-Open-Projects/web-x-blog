// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145245934
// LeetCode 155. 最小栈 — Zig 版（方案2）
const std = @import("std"); // 把 @import(「std」) 存入 std
const MinStack = struct { // 把 struct { 存入 MinStack
    vals: [4096]i32,
    mins: [4096]i32,
    n: usize,
    fn init() MinStack { // 定义函数/方法 init
        return .{ .vals = undefined, .mins = undefined, .n = 0 }; // 返回 { .vals 赋值为 undefined, .mins 赋值为 undefined, .元素个数 赋值为 0 }
    }
    fn push(self: *MinStack, v: i32) void { // 定义函数/方法 push
        self.vals[self.n] = v; // 把 值; 写入 self.vals[self.n]
        self.mins[self.n] = if (self.n > 0 and self.mins[self.n - 1] < v) self.mins[self.n - 1] else v;
        self.n += 1; // self.n累加 1
    }
    fn pop(self: *MinStack) void {
        self.n -= 1;
    } // 定义函数/方法 pop
    fn top(self: *MinStack) i32 {
        return self.vals[self.n - 1];
    } // 定义函数/方法 top
    fn getMin(self: *MinStack) i32 {
        return self.mins[self.n - 1];
    } // 定义函数/方法 getMin
};
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var s = MinStack.init(); // 把 MinStack.init() 存入 字符串
    s.push(-2); // 把 减 2 压入栈/数组尾部
    s.push(0); // 把 0 压入栈/数组尾部
    s.push(-3); // 把 减 3 压入栈/数组尾部
    if (s.getMin() != -3) return error.TestFailed; // 若 字符串.getMin() 不等于 减 3，直接返回 error.TestFailed
    s.pop(); // 弹出栈顶元素
    if (s.top() != 0) return error.TestFailed; // 若 字符串.top() 不等于 0，直接返回 error.TestFailed
    if (s.getMin() != -2) return error.TestFailed; // 若 字符串.getMin() 不等于 减 2，直接返回 error.TestFailed
    std.debug.print("PASS\n", .{});
} // 全部用例通过，输出 PASS
