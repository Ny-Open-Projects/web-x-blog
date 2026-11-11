-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134055742
-- LeetCode 283. 移动零 — Lua 版（方案1）
local function move_zeroes(nums) -- local function move_zeroes(数组)
	local pos = 1 -- 把 1 写入 local pos
	for i = 1, #nums do -- 把 1, #数组 do 写入 for i
		if nums[i] ~= 0 then -- 若 数组[下标 i] ~ 赋值为 0 then
			nums[pos], nums[i] = nums[i], nums[pos] -- 把 数组[下标 i], 数组[pos] 写入 nums[pos], nums[i]
			pos = pos + 1 -- 把 pos 加 1 存入 pos
		end -- 终点
	end -- 终点
	return nums -- 返回 数组
end -- 终点
assert(table.concat(move_zeroes({ 0, 1, 0, 3, 12 }), ",") == "1,3,12,0,0") -- 打印输出
assert(table.concat(move_zeroes({ 0 }), ",") == "0") -- 打印输出
print("PASS") -- 全部用例通过，输出 PASS
