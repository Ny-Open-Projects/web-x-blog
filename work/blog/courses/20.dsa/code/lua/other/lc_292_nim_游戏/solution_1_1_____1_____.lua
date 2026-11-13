-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135424151
-- LeetCode 292. Nim游戏 — Lua 版（方案1）
local function can_win_nim(n)
	return n % 4 ~= 0
end -- 把 0 终点 写入 local function can_win_nim(n) return n % 4 ~
assert(can_win_nim(4) == false) -- 断言校验
assert(can_win_nim(1) == true) -- 断言校验
assert(can_win_nim(2) == true) -- 断言校验
assert(can_win_nim(8) == false) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
