// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145634738
// LeetCode 1797. 设计一个验证系统 — Zig 版（方案1）
const std = @import("std"); // 把 @import(「std」) 存入 std
const AuthManager = struct { // 把 struct { 存入 AuthManager
    ttl: i64,
    ids: [64][32]u8,
    id_lens: [64]usize,
    exps: [64]i64,
    n: usize,
    fn init(ttl: i64) AuthManager { // 定义函数/方法 init
        return .{ .ttl = ttl, .ids = undefined, .id_lens = undefined, .exps = undefined, .n = 0 };
    }
    fn find(self: *AuthManager, id: []const u8) ?usize { // 定义函数/方法 find
        for (0..self.n) |i| { // 逐个取出 0..self.元素个数 的元素（下标 i）
            if (std.mem.eql(u8, self.ids[i][0..self.id_lens[i]], id)) return i;
        }
        return null; // 返回 null
    }
    fn generate(self: *AuthManager, id: []const u8, t: i64) void { // 定义函数/方法 generate
        const i = self.find(id) orelse blk: { // 把 self 查找 id) orelse blk: { 存入 下标 i
            const idx = self.n; // 把 self.元素个数 存入 idx
            self.n += 1; // self.n累加 1
            @memcpy(self.ids[idx][0..id.len], id); // @memcpy(self.ids[idx][0..id.长度], id);
            self.id_lens[idx] = id.len; // 把 id.长度; 写入 self.id_lens[idx]
            break :blk idx; // break :blk idx;
        };
        self.exps[i] = t + self.ttl; // 把 另一字符串 加 self.ttl; 写入 self.exps[i]
    }
    fn countValidTokens(self: *AuthManager, t: i64) usize { // 定义函数/方法 countValidTokens
        var cnt: usize = 0; // 把 0; 写入 var cnt: usize
        for (0..self.n) |i| { // 逐个取出 0..self.元素个数 的元素（下标 i）
            if (self.exps[i] > t) cnt += 1; // 若 self.exps[下标 i] 超过 另一字符串) 计数 累加 1;
        }
        return cnt; // 返回 计数
    }
    fn renew(self: *AuthManager, id: []const u8, t: i64) usize { // 定义函数/方法 renew
        if (self.find(id)) |i| { // 若 self 查找 id)) 按位或 下标 i 按位或
            if (self.exps[i] > t) self.exps[i] = t + self.ttl;
        }
        return self.countValidTokens(t); // 返回 self.countValidTokens(另一字符串)
    }
};
pub fn main() !void { // 程序入口：跑内嵌自测用例
    var auth = AuthManager.init(5); // 把 AuthManager.init(5) 存入 auth
    auth.generate("aaa", 1); // auth.generate(「aaa」, 1);
    if (auth.countValidTokens(3) != 1) return error.TestFailed; // 若 auth.countValidTokens(3) 不等于 1，直接返回 error.TestFailed
    if (auth.renew("aaa", 4) != 1) return error.TestFailed; // 若 auth.renew(「aaa」, 4) 不等于 1，直接返回 error.TestFailed
    if (auth.countValidTokens(6) != 1) return error.TestFailed; // 若 auth.countValidTokens(6) 不等于 1，直接返回 error.TestFailed
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
