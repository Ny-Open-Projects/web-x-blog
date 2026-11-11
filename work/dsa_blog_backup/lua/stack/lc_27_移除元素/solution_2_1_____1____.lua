-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145114689
-- LeetCode 27. 移除元素 — Lua 版（方案2）
local function remove_element(nums, val) -- local function remove_element(数组, 值)
	local k = 1 -- 把 1 写入 local k
	for i = 1, #nums do -- 把 1, #数组 do 写入 for i
		if nums[i] ~= val then -- 若 数组[下标 i] ~ 赋值为 值 then
			nums[k] = nums[i] -- 把 数组[下标 i] 写入 nums[k]
			k = k + 1 -- 把 下标 k 加 1 存入 下标 k
		end -- 终点
	end -- 终点
	return k - 1 -- 返回 下标 k 减 1
end -- 终点
assert(remove_element({ 3, 2, 2, 3 }, 3) == 2) -- 断言校验
assert(remove_element({ 0, 1, 2, 2, 3, 0, 4, 2 }, 2) == 5) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
