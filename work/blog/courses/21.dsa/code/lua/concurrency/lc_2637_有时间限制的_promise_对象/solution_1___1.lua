-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145398097
-- LeetCode 2637. 有时间限制的Promise对象 — Lua 版（方案1）
local function promise_with_time_limit(values, resolved, t)
	local out = {} -- 把 {} 写入 local out
	for i = 1, #resolved do -- 把 1, #resolved do 写入 for i
		out[i] = resolved[i] and values[i] or -1 -- 把 resolved[下标 i] and values[下标 i] or 减 1 写入 out[i]
	end -- 终点
	return out -- 返回 out
end -- 终点
local a = promise_with_time_limit({ 5, 0, 9 }, { true, false, true }, 50)
assert(a[1] == 5 and a[2] == -1 and a[3] == 9) -- 断言校验
local b = promise_with_time_limit({ 0 }, { false }, 100) -- 把 promise_with_time_limit({0}, {false}, 100) 写入 local b
assert(b[1] == -1) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
