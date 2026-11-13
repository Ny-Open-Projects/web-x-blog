-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107431726
-- LeetCode 107431726. 最大红矩形分析 — Lua 版（方案A：逐行高度 + 暴力区间 / 卡片扩展）
local function get_result(n, m, matrix) -- local function get_result(元素个数, 映射表, 矩阵)
	local ans = 0 -- 把 0 写入 local ans
	local height = {} -- 把 {} 写入 local height
	for i = 1, m + 2 do
		height[i] = 0
	end -- 让 下标 i 从 1 走到 映射表（Lua 1 基）
	for k = 1, n do -- 让 下标 k 从 1 走到 元素个数（Lua 1 基）
		for i = 1, m do -- 让 下标 i 从 1 走到 映射表（Lua 1 基）
			if matrix[k]:sub(i, i) == "." then
				height[i] = height[i] + 1
			else
				height[i] = 0
			end
		end -- 终点
		for a = 1, m do -- 让 数组 从 1 走到 映射表（Lua 1 基）
			local min_h = 50000 -- 把 50000 写入 local min_h
			for c = a, m do -- 把 数组, 映射表 do 写入 for c
				if height[c] < min_h then
					min_h = height[c]
				end -- 若 height[字符] 小于 min_h then min_h 赋值为 height[字符] 终点
			end -- 终点
			local area = (m - a + 1) * min_h -- 把 (映射表 减 数组 加 1) 乘 min_h 写入 local area
			if area > ans then
				ans = area
			end -- 若 area 超过 答案 then 答案 赋值为 area 终点
		end -- 终点
	end -- 终点
	return ans -- 返回 答案
end -- 终点

local function get_result_card(n, m, matrix) -- local function get_result_card(元素个数, 映射表, 矩阵)
	local ans = 0 -- 把 0 写入 local ans
	local height = {} -- 把 {} 写入 local height
	for i = 1, m + 2 do
		height[i] = 0
	end -- 让 下标 i 从 1 走到 映射表（Lua 1 基）
	for k = 1, n do -- 让 下标 k 从 1 走到 元素个数（Lua 1 基）
		for i = 1, m do -- 让 下标 i 从 1 走到 映射表（Lua 1 基）
			if matrix[k]:sub(i, i) == "." then
				height[i] = height[i] + 1
			else
				height[i] = 0
			end
		end -- 终点
		for a = 1, m do -- 让 数组 从 1 走到 映射表（Lua 1 基）
			local cur_h = height[a] -- 把 height[数组] 写入 local cur_h
			local lo = a - 1 -- 把 数组 减 1 写入 local lo
			while lo >= 1 and height[lo] >= cur_h do
				lo = lo - 1
			end
			local hi = a + 1 -- 把 数组 加 1 写入 local hi
			while hi <= m and height[hi] >= cur_h do
				hi = hi + 1
			end
			local area = (hi - lo - 1) * cur_h -- 把 (右边界 减 左边界 减 1) 乘 cur_h 写入 local area
			if area > ans then
				ans = area
			end -- 若 area 超过 答案 then 答案 赋值为 area 终点
		end -- 终点
	end -- 终点
	return ans -- 返回 答案
end -- 终点

local matrix = { ".....", "XXXXX", ".X...", "....." } -- 把 {「.....」, 「.....」, 「.....」, 「.....」} 写入 local matrix
assert(get_result(4, 5, matrix) == 6, "brute") -- 断言校验
assert(get_result_card(4, 5, matrix) == 6, "card") -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
