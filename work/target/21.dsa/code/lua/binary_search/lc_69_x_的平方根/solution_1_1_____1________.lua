-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145299731
-- LeetCode 69. x 的平方根 — Lua 版（1 ) 方案1：二分（精确区间判断））
local function my_sqrt(x) -- local function my_sqrt(x)
	if x < 2 then
		return x
	end -- 若 x 小于 2 then return x 终点
	local lo, hi = 1, x // 2 -- 把 1, x 写入 local lo, hi
	while lo <= hi do -- 把 右边界 do 写入 while lo <
		local m = lo + (hi - lo) // 2 -- 把 左边界 加 (右边界 减 左边界) 写入 local m
		if m * m <= x and x < (m + 1) * (m + 1) then
			return m
		elseif m * m > x then
			hi = m - 1
		else
			lo = m + 1
		end
	end -- 终点
	return lo -- 返回 左边界
end -- 终点
local cases = { { 4, 2 }, { 8, 2 }, { 16, 4 }, { 2147395599, 46339 } }
for _, c in ipairs(cases) do -- 遍历取 字符
	assert(my_sqrt(c[1]) == c[2], "x=" .. c[1]) -- 断言校验
end -- 终点
print("PASS") -- 全部用例通过，输出 PASS
