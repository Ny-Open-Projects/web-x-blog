-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133493400
-- LeetCode 347. 前K个高频元素 — Lua 版（方案5）
local function top_k_frequent(nums, k) -- local function top_k_frequent(数组, 下标 k)
	local counts = {} -- 把 {} 写入 local counts
	for _, v in ipairs(nums) do
		counts[v] = (counts[v] or 0) + 1
	end -- 遍历取 值
	local items = {} -- 把 {} 写入 local items
	for v, c in pairs(counts) do
		items[#items + 1] = { v, c }
	end -- 遍历取 字符
	table.sort(items, function(a, b) -- 排序
		if a[2] ~= b[2] then
			return a[2] > b[2]
		end -- 若 数组[2] ~ 赋值为 b[2] then return 数组[2] 超过 b[2] 终点
		return a[1] < b[1] -- 返回 数组[1] 小于 b[1]
	end) -- 终点)
	local res = {} -- 把 {} 写入 local res
	for i = 1, k do
		res[i] = items[i][1]
	end -- 让 下标 i 从 1 走到 下标 k（Lua 1 基）
	return res -- 返回 结果
end -- 终点
local got = top_k_frequent({ 1, 1, 1, 2, 2, 3 }, 2) -- 把 top_k_frequent({1, 1, 1, 2, 2, 3}, 2) 写入 local got
table.sort(got) -- 排序
assert(#got == 2 and got[1] == 1 and got[2] == 2) -- 断言校验
local g2 = top_k_frequent({ 1 }, 1) -- 把 top_k_frequent({1}, 1) 写入 local g2
assert(#g2 == 1 and g2[1] == 1) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
