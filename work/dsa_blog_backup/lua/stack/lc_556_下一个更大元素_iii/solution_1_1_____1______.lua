-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145397820
-- LeetCode 556. 下一个更大元素 III — Lua 版（方案1）
local function next_greater_element(n) -- local function next_greater_element(元素个数)
	if n < 10 then
		return -1
	end -- 若 元素个数 小于 10 then return 减 1 终点
	local d = {} -- 把 {} 写入 local d
	local x = n -- 把 元素个数 写入 local x
	while x > 0 do
		d[#d + 1] = x % 10
		x = math.floor(x / 10)
	end
	-- d 是逆序的；转正序
	local dd = {} -- 把 {} 写入 local dd
	for i = #d, 1, -1 do
		dd[#dd + 1] = d[i]
	end -- 把 #d, 1, 减 1 do dd[#dd 加 1] 赋值为 d[下标 i] 终点 写入 for i
	local m = #dd -- 把 #dd 写入 local m
	local i = m - 1 -- 把 映射表 减 1 写入 local i
	while i >= 1 and dd[i] >= dd[i + 1] do
		i = i - 1
	end
	if i == 0 then
		return -1
	end -- 若 下标 i 等于 0 then return 减 1 终点
	local j = m -- 把 映射表 写入 local j
	while dd[j] <= dd[i] do
		j = j - 1
	end -- 把 dd[下标 i] do 下标 j 赋值为 下标 j 减 1 终点 写入 while dd[j] <
	dd[i], dd[j] = dd[j], dd[i] -- 把 dd[下标 j], dd[下标 i] 写入 dd[i], dd[j]
	-- 反转 i+1..m
	local lo, hi = i + 1, m -- 把 下标 i 加 1, 映射表 写入 local lo, hi
	while lo < hi do
		dd[lo], dd[hi] = dd[hi], dd[lo]
		lo = lo + 1
		hi = hi - 1
	end
	local res = 0 -- 把 0 写入 local res
	for _, v in ipairs(dd) do
		res = res * 10 + v
	end -- 遍历取 值
	if res > 2147483647 then
		return -1
	end -- 若 结果 超过 2147483647 then return 减 1 终点
	return res -- 返回 结果
end -- 终点
assert(next_greater_element(12) == 21) -- 断言校验
assert(next_greater_element(21) == -1) -- 断言校验
assert(next_greater_element(1) == -1) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
