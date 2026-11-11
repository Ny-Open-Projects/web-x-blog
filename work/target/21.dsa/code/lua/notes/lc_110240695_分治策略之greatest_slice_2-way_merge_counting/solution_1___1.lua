-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/110240695
-- LeetCode 110240695. 分治策略之 greatest slice — Lua 版（方案A：暴力枚举所有子段）
local function max_sub_array_bf(arr) -- local function max_sub_array_bf(数组)
	local best = -math.huge -- 把 减 math.huge 写入 local best
	for i = 1, #arr do -- 把 1, #数组 do 写入 for i
		local s = 0 -- 把 0 写入 local s
		for j = i, #arr do -- 把 下标 i, #数组 do 写入 for j
			s = s + arr[j] -- 把 字符串 加 数组[下标 j] 存入 字符串
			if s > best then
				best = s
			end -- 若 字符串 超过 当前最优 then 当前最优 赋值为 字符串 终点
		end -- 终点
	end -- 终点
	return best -- 返回 当前最优
end -- 终点

local cases = { -- 把 { 写入 local cases
	{ { -2, 1, -3, 4, -1, 2, 1, -5, 4 }, 6 },
	{ { 1 }, 1 },
	{ { -1, -2, -3 }, -1 },
	{ { 5, 4, -1, 7, 8 }, 23 },
}
for idx, c in ipairs(cases) do -- 遍历取 字符
	assert(max_sub_array_bf(c[1]) == c[2], "case " .. idx .. " failed") -- 断言校验
end -- 终点
print("PASS") -- 全部用例通过，输出 PASS
