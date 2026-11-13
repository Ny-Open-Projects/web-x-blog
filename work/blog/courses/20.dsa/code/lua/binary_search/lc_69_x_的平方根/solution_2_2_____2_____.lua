-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145299731
-- LeetCode 69. x 的平方根 — Lua 版（2 ) 方案2：二分（保留 ans））
local function my_sqrt(x) -- local function my_sqrt(x)
	local lo, hi, ans = 0, x, 0 -- 把 0, x, 0 写入 local lo, hi, ans
	while lo <= hi do -- 把 右边界 do 写入 while lo <
		local m = lo + (hi - lo) // 2 -- 把 左边界 加 (右边界 减 左边界) 写入 local m
		if m * m <= x then
			ans = m
			lo = m + 1
		else
			hi = m - 1
		end
	end -- 终点
	return ans -- 返回 答案
end -- 终点
local cases = { { 4, 2 }, { 8, 2 }, { 16, 4 }, { 2147395599, 46339 } }
for _, c in ipairs(cases) do -- 遍历取 字符
	assert(my_sqrt(c[1]) == c[2], "x=" .. c[1]) -- 断言校验
end -- 终点
print("PASS") -- 全部用例通过，输出 PASS
