// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/138684407
// LeetCode 649. Dota2参议院 — Zig 版（方案1）
const std = @import("std"); // 把 @import(「std」) 存入 std
fn predictPartyVictory(senate: []const u8) []const u8 { // 定义函数/方法 predictPartyVictory
    const n: i32 = @intCast(senate.len); // 把 @intCast(senate.长度); 写入 const n: i32
    var radiant_buf: [8192]i32 = undefined; // 把 undefined; 写入 var radiant_buf: [8192]i32
    var dire_buf: [8192]i32 = undefined; // 把 undefined; 写入 var dire_buf: [8192]i32
    var rn: usize = 0; // 把 0; 写入 var rn: usize
    var dn: usize = 0; // 把 0; 写入 var dn: usize
    var rh: usize = 0; // 把 0; 写入 var rh: usize
    var dh: usize = 0; // 把 0; 写入 var dh: usize
    for (senate, 0..) |c, i| { // for (senate, 0..) 按位或 字符, 下标 i 按位或 {
        if (c == 'R') { // 若 字符 等于 'R'
            radiant_buf[rn] = @intCast(i); // 把 @intCast(下标 i); 写入 radiant_buf[rn]
            rn += 1; // rn累加 1
        } else { // 否则
            dire_buf[dn] = @intCast(i); // 把 @intCast(下标 i); 写入 dire_buf[dn]
            dn += 1; // dn累加 1
        }
    }
    while (rh < rn and dh < dn) { // 循环，直到不满足「rh 小于 rn and dh 小于 dn」
        const r = radiant_buf[rh]; // 把 radiant_buf[rh] 存入 右指针
        rh += 1; // rh累加 1
        const d = dire_buf[dh]; // 把 dire_buf[dh] 存入 d
        dh += 1; // dh累加 1
        if (r < d) { // 若 右指针 小于 d
            radiant_buf[rn] = r + n; // 把 右指针 加 元素个数; 写入 radiant_buf[rn]
            rn += 1; // rn累加 1
        } else { // 否则
            dire_buf[dn] = d + n; // 把 d 加 元素个数; 写入 dire_buf[dn]
            dn += 1; // dn累加 1
        }
    }
    return if (rh >= rn) "Dire" else "Radiant"; // 返回 if (rh 不低于 rn) 「Dire」 else 「Dire」
}
pub fn main() !void { // 程序入口：跑内嵌自测用例
    if (!std.mem.eql(u8, predictPartyVictory("RD"), "Radiant")) return error.TestFailed;
    if (!std.mem.eql(u8, predictPartyVictory("DDR"), "Dire")) return error.TestFailed;
    std.debug.print("PASS\n", .{}); // 全部用例通过，输出 PASS
}
