-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133531071
-- LeetCode 169. 多数元素 — Lua 版（方案1）
local function majority_element(nums) -- local function majority_element(数组)
	local counts = {} -- 把 {} 写入 local counts
	local best, bn = nums[1], 0 -- 把 数组[1], 0 写入 local best, bn
	for _, v in ipairs(nums) do -- 遍历取 值
		counts[v] = (counts[v] or 0) + 1 -- 把 (counts[值] or 0) 加 1 写入 counts[v]
		if counts[v] > bn then
			best, bn = v, counts[v]
		end -- 若 counts[值] 超过 bn then 当前最优, bn 赋值为 值, counts[值] 终点
	end -- 终点
	return best -- 返回 当前最优
end -- 终点
assert(majority_element({ 3, 2, 3 }) == 3) -- 断言校验
assert(majority_element({ 2, 2, 1, 1, 1, 2, 2 }) == 2) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
