-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135359346
-- LeetCode 326. 3的幂 — Lua 版（方案1）
local function is_power_of_three(n) -- local function is_power_of_three(元素个数)
	while n ~= 0 and n % 3 == 0 do
		n = math.floor(n / 3)
	end
	return n == 1 -- 返回 元素个数 等于 1
end -- 终点
assert(is_power_of_three(27) == true) -- 断言校验
assert(is_power_of_three(0) == false) -- 断言校验
assert(is_power_of_three(9) == true) -- 断言校验
assert(is_power_of_three(-1) == false) -- 断言校验
assert(is_power_of_three(1) == true) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
