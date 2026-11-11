-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134378688
-- LeetCode 448. 找到所有数组中消失的数字 — Lua 版（方案1）
local function find_disappeared_numbers(nums) -- local function find_disappeared_numbers(数组)
	local v = { table.unpack(nums) } -- 把 {table.unpack(数组)} 写入 local v
	for i = 1, #v do -- 把 1, #值 do 写入 for i
		local idx = math.abs(v[i]) -- 把 math.取绝对值 值[下标 i]) 写入 local idx
		if v[idx] and v[idx] > 0 then
			v[idx] = -v[idx]
		end -- 若 值[idx] and 值[idx] 超过 0 then 值[idx] 赋值为 减 值[idx] 终点
	end -- 终点
	local out = {} -- 把 {} 写入 local out
	for i = 1, #v do -- 把 1, #值 do 写入 for i
		if v[i] > 0 then
			out[#out + 1] = i
		end -- 若 值[下标 i] 超过 0 then out[#out 加 1] 赋值为 下标 i 终点
	end -- 终点
	return out -- 返回 out
end -- 终点
assert(table.concat(find_disappeared_numbers({ 4, 3, 2, 7, 8, 2, 3, 1 }), ",") == "5,6") -- 打印输出
assert(table.concat(find_disappeared_numbers({ 1, 1 }), ",") == "2") -- 打印输出
print("PASS") -- 全部用例通过，输出 PASS
