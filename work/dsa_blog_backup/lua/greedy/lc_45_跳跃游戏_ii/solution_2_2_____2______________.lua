-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133911745
-- LeetCode 45. 跳跃游戏II — Lua 版（方案2）
local function jump(nums) -- local function jump(数组)
	local position, steps = #nums, 0 -- 把 #数组, 0 写入 local position, steps
	while position > 1 do -- while position 超过 1 do
		for i = 1, position - 1 do -- 让 下标 i 从 1 走到 position（Lua 1 基）
			if i - 1 + nums[i] >= position - 1 then -- 若 下标 i 减 1 加 数组[下标 i] 不低于 position 减 1 then
				position = i -- 把 下标 i 存入 position
				steps = steps + 1 -- 把 steps 加 1 存入 steps
				break -- 跳出循环
			end -- 终点
		end -- 终点
	end -- 终点
	return steps -- 返回 steps
end -- 终点
assert(jump({ 2, 3, 1, 1, 4 }) == 2) -- 断言校验
assert(jump({ 2, 3, 0, 1, 4 }) == 2) -- 断言校验
assert(jump({ 1 }) == 0) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
