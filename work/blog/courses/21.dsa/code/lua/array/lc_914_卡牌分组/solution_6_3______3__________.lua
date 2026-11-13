-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134934324
-- LeetCode 914. 卡牌分组 — Lua 版（方案6）
local function gcd(a, b) -- local function gcd(数组, b)
	while b ~= 0 do
		a, b = b, a % b
	end -- 把 0 do 数组, b 赋值为 b, 数组 对…取模 b 终点 写入 while b ~
	return a -- 返回 数组
end -- 终点
local function has_groups_size_x(deck) -- local function has_groups_size_x(deck)
	local counts = {} -- 把 {} 写入 local counts
	for _, c in ipairs(deck) do
		counts[c] = (counts[c] or 0) + 1
	end -- 遍历取 字符
	local g = 0 -- 把 0 写入 local g
	for _, v in pairs(counts) do
		g = gcd(g, v)
	end -- 遍历取 值
	return g >= 2 -- 返回 g 不低于 2
end -- 终点
assert(has_groups_size_x({ 1, 2, 3, 4, 4, 3, 2, 1 }) == true) -- 断言校验
assert(has_groups_size_x({ 1, 1, 1, 2, 2, 2, 3, 3 }) == false) -- 断言校验
assert(has_groups_size_x({ 1 }) == false) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
