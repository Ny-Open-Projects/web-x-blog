-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135124945
-- LeetCode 202. 快乐数 — Lua 版（方案1）
local function bit_square_sum(n) -- local function bit_square_sum(元素个数)
	local s = 0 -- 把 0 写入 local s
	while n > 0 do -- while 元素个数 超过 0 do
		local d = n % 10 -- 把 元素个数 对…取模 10 写入 local d
		s = s + d * d -- 把 字符串 加 d 乘 d 存入 字符串
		n = math.floor(n / 10) -- 把 math.floor(元素个数 除以 10) 存入 元素个数
	end -- 终点
	return s -- 返回 字符串
end -- 终点
local function is_happy(n) -- local function is_happy(元素个数)
	local seen = {} -- 把 {} 写入 local seen
	while n ~= 1 and not seen[n] do -- 把 1 and not 已见集合[元素个数] do 写入 while n ~
		seen[n] = true -- 把 true 写入 seen[n]
		n = bit_square_sum(n) -- 把 bit_square_sum(元素个数) 存入 元素个数
	end -- 终点
	return n == 1 -- 返回 元素个数 等于 1
end -- 终点
assert(bit_square_sum(1) == 1) -- 断言校验
assert(bit_square_sum(19) == 82) -- 断言校验
assert(bit_square_sum(82) == 68) -- 断言校验
assert(is_happy(19) == true) -- 断言校验
assert(is_happy(1) == true) -- 断言校验
assert(is_happy(2) == false) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
