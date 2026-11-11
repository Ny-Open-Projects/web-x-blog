-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145299731
-- LeetCode 69. x 的平方根 — Lua 版（4 ) 方案4：二分（返回 hi））
local function my_sqrt(x) -- local function my_sqrt(x)
	local lo, hi = 1, x -- 把 1, x 写入 local lo, hi
	while lo <= hi do -- 把 右边界 do 写入 while lo <
		local m = lo + (hi - lo) // 2 -- 把 左边界 加 (右边界 减 左边界) 写入 local m
		if m * m == x then
			return m -- 若 映射表 乘 映射表 等于 x then return 映射表
		elseif m * m < x then
			lo = m + 1
		else
			hi = m - 1
		end
	end -- 终点
	return hi -- 返回 右边界
end -- 终点
local cases = { { 4, 2 }, { 8, 2 }, { 16, 4 }, { 2147395599, 46339 } }
for _, c in ipairs(cases) do -- 遍历取 字符
	assert(my_sqrt(c[1]) == c[2], "x=" .. c[1]) -- 断言校验
end -- 终点
print("PASS") -- 全部用例通过，输出 PASS
