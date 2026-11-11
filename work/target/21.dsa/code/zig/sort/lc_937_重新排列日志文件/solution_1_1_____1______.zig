// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/139965098
// LeetCode 937. 重新排列日志文件 — Zig 版（方案1）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn contentOf(log: []const u8) []const u8 { // 定义函数/方法 contentOf
    const idx = std.mem.indexOfScalar(u8, log, ' ') orelse return "";
    return log[idx + 1 ..]; // 返回 log[idx 加 1 ..]
}
fn isDigitLog(log: []const u8) bool { // 定义判定函数 isDigitLog
    const c = contentOf(log); // 把 contentOf(log) 存入 字符
    return c.len > 0 and c[0] >= '0' and c[0] <= '9'; // 返回 字符.长度 超过 0 and 字符[0] 不低于 '0' and 字符[0] 不超过 '9'
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator); // 把 std.堆.ArenaAllocator.init(std.堆.page_allocator) 存入 arena
    defer arena.deinit(); // defer arena.deinit();
    const alloc = arena.allocator(); // 把 arena.allocator() 存入 alloc
    const logs = [_][]const u8{ "a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo" };
    var letter = std.ArrayList([]const u8).init(alloc); // 把 std.ArrayList([]const u8).init(alloc) 存入 letter
    var digit = std.ArrayList([]const u8).init(alloc); // 把 std.ArrayList([]const u8).init(alloc) 存入 digit
    for (logs) |log| { // 逐个取出 logs 的元素（log）
        if (isDigitLog(log)) digit.append(log) catch unreachable else letter.append(log) catch unreachable;
    }
    const S = struct { // 把 struct { 存入 S
        fn lt(_: void, a: []const u8, b: []const u8) bool { // 定义函数/方法 lt
            const cr = std.mem.order(u8, contentOf(a), contentOf(b)); // 把 std.mem.order(u8, contentOf(数组), contentOf(b)) 存入 cr
            if (cr != .eq) return cr == .lt; // 若 cr 不等于 .eq，直接返回 cr 等于 .lt
            return std.mem.order(u8, a, b) == .lt; // 返回 std.mem.order(u8, 数组, b) 等于 .lt
        }
    };
    std.sort.pdq([]const u8, letter.items, {}, S.lt); // std.sort.pdq([]const u8, letter.items, {}, S.lt);
    const wants = [_][]const u8{ "g1 act car", "a8 act zoo", "ab1 off key dog", "a1 9 2 3 1", "zo4 4 7" };
    var wi: usize = 0; // 把 0; 写入 var wi: usize
    for (letter.items) |l| { // 逐个取出 letter.items 的元素（左指针）
        if (!std.mem.eql(u8, l, wants[wi])) return error.TestFailed; // 若 取反 std.mem.eql(u8, 左指针, wants[wi])，直接返回 error.TestFailed
        wi += 1; // wi累加 1
    }
    for (digit.items) |d| { // 逐个取出 digit.items 的元素（d）
        if (!std.mem.eql(u8, d, wants[wi])) return error.TestFailed; // 若 取反 std.mem.eql(u8, d, wants[wi])，直接返回 error.TestFailed
        wi += 1; // wi累加 1
    }
    if (wi != 5) return error.TestFailed; // 若 wi 不等于 5，直接返回 error.TestFailed
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
