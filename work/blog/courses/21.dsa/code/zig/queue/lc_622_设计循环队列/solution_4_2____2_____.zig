// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130471048
// LeetCode 622. 设计循环队列 — Zig 版
const std = @import("std"); // 把 @import(「std」) 存入 std

// 方案4：数组 + front/rear/size 循环队列
const MyCircularQueue = struct { // 把 struct { 存入 MyCircularQueue
    capacity: usize,
    data: []i32,
    front: usize,
    rear: usize,
    size: usize,

    fn init(allocator: std.mem.Allocator, k: usize) !MyCircularQueue { // 定义函数/方法 init
        const data = try allocator.alloc(i32, k); // 把 try allocator.alloc(i32, 下标 k) 存入 data
        @memset(data, 0); // @memset(data, 0);
        return .{ .capacity = k, .data = data, .front = 0, .rear = 0, .size = 0 };
    }

    fn enQueue(self: *MyCircularQueue, value: i32) bool { // 定义函数/方法 enQueue
        if (self.isFull()) return false; // 若 self.isFull()，直接返回 false
        self.data[self.rear] = value; // 把 value; 写入 self.data[self.rear]
        self.rear = (self.rear + 1) % self.capacity; // 把 (self.rear 加 1) 对…取模 self.capacity; 写入 self.rear
        self.size += 1; // self.size累加 1
        return true; // 返回 true
    }

    fn deQueue(self: *MyCircularQueue) bool { // 定义函数/方法 deQueue
        if (self.isEmpty()) return false; // 若 self.isEmpty()，直接返回 false
        self.front = (self.front + 1) % self.capacity; // 把 (self.front 加 1) 对…取模 self.capacity; 写入 self.front
        self.size -= 1; // self.size累减 1
        return true; // 返回 true
    }

    fn getFront(self: *const MyCircularQueue) i32 { // 定义函数/方法 getFront
        if (self.isEmpty()) return -1; // 若 self.isEmpty()，直接返回 减 1
        return self.data[self.front]; // 返回 self.data[self.front]
    }

    fn getRear(self: *const MyCircularQueue) i32 { // 定义函数/方法 getRear
        if (self.isEmpty()) return -1; // 若 self.isEmpty()，直接返回 减 1
        // rear + capacity - 1 避免 usize 下溢（等价 TS 的 (rear - 1 + capacity) % capacity）
        return self.data[(self.rear + self.capacity - 1) % self.capacity];
    }

    fn isEmpty(self: *const MyCircularQueue) bool { // 定义判定函数 isEmpty
        return self.size == 0; // 返回 self.大小 等于 0
    }

    fn isFull(self: *const MyCircularQueue) bool { // 定义判定函数 isFull
        return self.size == self.capacity; // 返回 self.大小 等于 self.capacity
    }
};

fn b2i(b: bool) i32 { // 定义函数/方法 b2i
    return if (b) 1 else 0; // 返回 if (b) 1 else 0
}

pub fn main() !void { // 程序入口：跑内嵌自测用例
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator); // 把 std.堆.ArenaAllocator.init(std.堆.page_allocator) 存入 arena
    defer arena.deinit(); // defer arena.deinit();
    var q = try MyCircularQueue.init(arena.allocator(), 3); // 把 try MyCircularQueue.init(arena.allocator(), 3) 存入 节点

    // 与 TS 事实源内嵌用例一致：[true,true,true,false,3,true,true,true,4]
    // 布尔结果用 1/0 表示
    var got: [9]i32 = undefined; // 把 undefined; 写入 var got: [9]i32
    got[0] = b2i(q.enQueue(1)); // 把 b2i(节点.enQueue(1)); 写入 got[0]
    got[1] = b2i(q.enQueue(2)); // 把 b2i(节点.enQueue(2)); 写入 got[1]
    got[2] = b2i(q.enQueue(3)); // 把 b2i(节点.enQueue(3)); 写入 got[2]
    got[3] = b2i(q.enQueue(4)); // 把 b2i(节点.enQueue(4)); 写入 got[3]
    got[4] = q.getRear(); // 把 节点.getRear(); 写入 got[4]
    got[5] = b2i(q.isFull()); // 把 b2i(节点.isFull()); 写入 got[5]
    got[6] = b2i(q.deQueue()); // 把 b2i(节点.deQueue()); 写入 got[6]
    got[7] = b2i(q.enQueue(4)); // 把 b2i(节点.enQueue(4)); 写入 got[7]
    got[8] = q.getRear(); // 把 节点.getRear(); 写入 got[8]

    const want = [_]i32{ 1, 1, 1, 0, 3, 1, 1, 1, 4 }; // 把 [_]i32{ 1, 1, 1, 0, 3, 1, 1, 1, 4 } 存入 want
    for (got, want, 0..) |g, w, i| { // for (got, want, 0..) 按位或 g, 权重, 下标 i 按位或 {
        if (g != w) { // 若 g 不等于 权重
            std.debug.print("FAIL idx {d} got {d} want {d}\n", .{ i, g, w }); // 打印输出
            return error.TestFailed; // 返回 error.TestFailed
        }
    }
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
