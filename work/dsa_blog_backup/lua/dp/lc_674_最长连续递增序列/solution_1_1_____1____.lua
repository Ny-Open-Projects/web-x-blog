-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130771608
-- LeetCode 674. 最长连续递增序列 — Lua 版（方案1）
local function find_length_of_lcis(nums) -- local function find_length_of_lcis(数组)
	if #nums == 0 then
		return 0
	end -- 若 #数组 等于 0 then return 0 终点
	local best, cur = 1, 1 -- 把 1, 1 写入 local best, cur
	for i = 2, #nums do -- 把 2, #数组 do 写入 for i
		if nums[i] > nums[i - 1] then -- 若 数组[下标 i] 超过 数组[下标 i 减 1] then
			cur = cur + 1 -- 把 当前值 加 1 存入 当前值
			if cur > best then
				best = cur
			end -- 若 当前值 超过 当前最优 then 当前最优 赋值为 当前值 终点
		else -- 否则
			cur = 1 -- 把 1 存入 当前值
		end -- 终点
	end -- 终点
	return best -- 返回 当前最优
end -- 终点
assert(find_length_of_lcis({ 1, 3, 5, 4, 7 }) == 3) -- 断言校验
assert(find_length_of_lcis({ 2, 2, 2, 2, 2 }) == 1) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
