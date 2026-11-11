-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130497821
-- LeetCode 53. 最大子数组和 — Lua 版（方案2）
local function max_sub_array(nums) -- local function max_sub_array(数组)
	local best, cur = nums[1], nums[1] -- 把 数组[1], 数组[1] 写入 local best, cur
	for i = 2, #nums do -- 把 2, #数组 do 写入 for i
		cur = cur > 0 and cur + nums[i] or nums[i] -- 把 当前值 超过 0 and 当前值 加 数组[下标 i] or 数组[下标 i] 存入 当前值
		if cur > best then
			best = cur
		end -- 若 当前值 超过 当前最优 then 当前最优 赋值为 当前值 终点
	end -- 终点
	return best -- 返回 当前最优
end -- 终点
assert(max_sub_array({ -2, 1, -3, 4, -1, 2, 1, -5, 4 }) == 6) -- 断言校验
assert(max_sub_array({ 1 }) == 1) -- 断言校验
assert(max_sub_array({ 5, 4, -1, 7, 8 }) == 23) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
