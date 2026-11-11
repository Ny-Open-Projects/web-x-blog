-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/93536806
-- 数据结构与算法笔记: 复杂度 — Lua 版（方案11）
local function func_calls(n) -- local function func_calls(元素个数)
	if n <= 1 then
		return 1
	end -- 若 元素个数 不超过 1 then return 1 终点
	return 2 * func_calls(n - 1) -- 返回 2 乘 func_calls(元素个数 减 1)
end -- 终点
assert(func_calls(1) == 1) -- 断言校验
assert(func_calls(2) == 2) -- 断言校验
assert(func_calls(5) == 16) -- 断言校验
assert(func_calls(10) == 512) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
