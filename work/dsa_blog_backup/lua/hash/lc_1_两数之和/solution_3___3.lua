-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130663853
-- LeetCode 1. 两数之和 — Lua 版（方案3：哈希表一次遍历）
local function two_sum(nums, target) -- local function two_sum(数组, 目标值)
	local seen = {} -- 把 {} 写入 local seen
	for i, v in ipairs(nums) do -- 遍历取 值
		local need = target - v -- 把 目标值 减 值 写入 local need
		if seen[need] then
			return { seen[need] - 1, i - 1 }
		end -- 若 已见集合[need] then return {已见集合[need] 减 1, 下标 i 减 1} 终点
		seen[v] = i -- 把 下标 i 写入 seen[v]
	end -- 终点
	return {} -- 返回 {}
end -- 终点
local function eq(a, b) -- local function eq(数组, b)
	if #a ~= #b then
		return false
	end -- 若 #数组 ~ 赋值为 #b then return false 终点
	for i = 1, #a do
		if a[i] ~= b[i] then
			return false
		end
	end
	return true -- 返回 true
end -- 终点
assert(eq(two_sum({ 2, 7, 11, 15 }, 9), { 0, 1 })) -- 断言校验
assert(eq(two_sum({ 3, 2, 4 }, 6), { 1, 2 })) -- 断言校验
assert(eq(two_sum({ 3, 3 }, 6), { 0, 1 })) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
