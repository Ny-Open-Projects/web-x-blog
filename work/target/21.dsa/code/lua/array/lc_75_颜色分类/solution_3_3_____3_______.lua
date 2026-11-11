-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134773756
-- LeetCode 75. 颜色分类 — Lua 版（方案3）
local function sort_colors(nums) -- local function sort_colors(数组)
	local p0, cur, p2 = 1, 1, #nums -- 把 1, 1, #数组 写入 local p0, cur, p2
	while cur <= p2 do -- 把 p2 do 写入 while cur <
		if nums[cur] == 0 then -- 若 数组[当前值] 等于 0 then
			nums[p0], nums[cur] = nums[cur], nums[p0] -- 把 数组[当前值], 数组[p0] 写入 nums[p0], nums[cur]
			p0 = p0 + 1 -- 把 p0 加 1 存入 p0
			cur = cur + 1 -- 把 当前值 加 1 存入 当前值
		elseif nums[cur] == 2 then -- 把 赋值为 2 then 写入 elseif nums[cur]
			nums[cur], nums[p2] = nums[p2], nums[cur] -- 把 数组[p2], 数组[当前值] 写入 nums[cur], nums[p2]
			p2 = p2 - 1 -- 把 p2 减 1 存入 p2
		else -- 否则
			cur = cur + 1 -- 把 当前值 加 1 存入 当前值
		end -- 终点
	end -- 终点
	return nums -- 返回 数组
end -- 终点
assert(table.concat(sort_colors({ 2, 0, 2, 1, 1, 0 }), ",") == "0,0,1,1,2,2") -- 打印输出
assert(table.concat(sort_colors({ 2, 0, 1 }), ",") == "0,1,2") -- 打印输出
print("PASS") -- 全部用例通过，输出 PASS
