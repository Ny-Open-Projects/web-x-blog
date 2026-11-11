-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130506068
-- LeetCode 70. 爬楼梯 — Lua 版（方案1）
local function climb_stairs(n)
	if n <= 2 then
		return n
	end
	local a, b = 1, 2
	for _ = 3, n do
		a, b = b, a + b
	end
	return b
end
assert(climb_stairs(2) == 2)
assert(climb_stairs(3) == 3)
assert(climb_stairs(10) == 89)
print("PASS") -- 全部用例通过，输出 PASS
