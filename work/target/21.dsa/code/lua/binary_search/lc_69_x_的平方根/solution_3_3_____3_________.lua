-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145299731
-- LeetCode 69. x 的平方根 — Lua 版（3 ) 方案3：牛顿迭代）
local function my_sqrt(x) -- local function my_sqrt(x)
	if x < 2 then
		return x
	end -- 若 x 小于 2 then return x 终点
	local r = x -- 把 x 写入 local r
	while r * r > x do -- while 右指针 乘 右指针 超过 x do
		r = (r + x // r) // 2 -- 把 (右指针 加 x 存入 右指针
	end -- 终点
	return r -- 返回 右指针
end -- 终点
local cases = { { 4, 2 }, { 8, 2 }, { 16, 4 }, { 2147395599, 46339 } }
for _, c in ipairs(cases) do -- 遍历取 字符
	assert(my_sqrt(c[1]) == c[2], "x=" .. c[1]) -- 断言校验
end -- 终点
print("PASS") -- 全部用例通过，输出 PASS
