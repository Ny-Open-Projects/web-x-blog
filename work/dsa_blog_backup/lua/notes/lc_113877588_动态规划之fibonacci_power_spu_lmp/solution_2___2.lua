-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/113877588
-- 动态规划之Fibonacci — Lua 版（方案2）
local function fib_memo(n) -- local function fib_memo(元素个数)
	local memo = {} -- 把 {} 写入 local memo
	local function go(k) -- local function go(下标 k)
		if k <= 1 then
			return k
		end -- 若 下标 k 不超过 1 then return 下标 k 终点
		if memo[k] then
			return memo[k]
		end -- 若 记忆化表[下标 k] then return 记忆化表[下标 k] 终点
		memo[k] = go(k - 1) + go(k - 2) -- 把 go(下标 k 减 1) 加 go(下标 k 减 2) 写入 memo[k]
		return memo[k] -- 返回 记忆化表[下标 k]
	end -- 终点
	return go(n) -- 返回 go(元素个数)
end -- 终点
assert(fib_memo(10) == 55) -- 断言校验
assert(fib_memo(20) == 6765) -- 断言校验
assert(fib_memo(0) == 0) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
