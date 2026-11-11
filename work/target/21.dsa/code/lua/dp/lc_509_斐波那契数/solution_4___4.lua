-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130510175
-- LeetCode 509. 斐波那契数 — Lua 版（方案4）
local function fib(n)
	if n < 2 then
		return n
	end
	local a, b = 0, 1
	for _ = 2, n do
		a, b = b, a + b
	end
	return b
end
assert(fib(2) == 1)
assert(fib(3) == 2)
assert(fib(4) == 3)
assert(fib(10) == 55)
print("PASS") -- 全部用例通过，输出 PASS
