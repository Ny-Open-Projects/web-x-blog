-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134073792
-- 数据结构与算法之排序: 快速排序 — Lua 版（方案1）
local function quick_sort(nums) -- local function quick_sort(数组)
	if #nums <= 1 then
		return nums
	end -- 若 #数组 不超过 1 then return 数组 终点
	local pivot = nums[#nums // 2 + 1] -- 把 数组[#数组 写入 local pivot
	local lt, eq, gt = {}, {}, {} -- 把 {}, {}, {} 写入 local lt, eq, gt
	for _, x in ipairs(nums) do -- 遍历取 x
		if x < pivot then
			lt[#lt + 1] = x -- 若 x 小于 pivot then lt[#lt 加 1] 赋值为 x
		elseif x == pivot then
			eq[#eq + 1] = x -- 把 赋值为 pivot then eq[#eq 加 1] 赋值为 x 写入 elseif x
		else
			gt[#gt + 1] = x
		end -- 否则
	end -- 终点
	local out = {} -- 把 {} 写入 local out
	for _, v in ipairs(quick_sort(lt)) do
		out[#out + 1] = v
	end -- 遍历取 值
	for _, v in ipairs(eq) do
		out[#out + 1] = v
	end -- 遍历取 值
	for _, v in ipairs(quick_sort(gt)) do
		out[#out + 1] = v
	end -- 遍历取 值
	return out -- 返回 out
end -- 终点
assert(table.concat(quick_sort({ 5, 4, 3, 2, 1 }), ",") == "1,2,3,4,5") -- 打印输出
assert(table.concat(quick_sort({ 3, 1, 4, 1, 5 }), ",") == "1,1,3,4,5") -- 打印输出
print("PASS") -- 全部用例通过，输出 PASS
