-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134893847
-- LeetCode 905. 按奇偶排序数组 — Lua 版（方案2）
local function sort_array_by_parity(nums) -- local function sort_array_by_parity(数组)
	local v = { table.unpack(nums) } -- 把 {table.unpack(数组)} 写入 local v
	local pos = 1 -- 把 1 写入 local pos
	for i = 1, #v do -- 把 1, #值 do 写入 for i
		if v[i] % 2 == 0 then -- 若 值[下标 i] 对…取模 2 等于 0 then
			v[pos], v[i] = v[i], v[pos] -- 把 值[下标 i], 值[pos] 写入 v[pos], v[i]
			pos = pos + 1 -- 把 pos 加 1 存入 pos
		end -- 终点
	end -- 终点
	return v -- 返回 值
end -- 终点
local g1 = sort_array_by_parity({ 3, 1, 2, 4 }) -- 把 sort_array_by_parity({3,1,2,4}) 写入 local g1
assert(#g1 == 4 and g1[1] % 2 == 0 and g1[2] % 2 == 0 and g1[3] % 2 == 1) -- 断言校验
local g2 = sort_array_by_parity({ 1, 2, 3 }) -- 把 sort_array_by_parity({1,2,3}) 写入 local g2
assert(table.concat(g2, ",") == "2,1,3") -- 打印输出
print("PASS") -- 全部用例通过，输出 PASS
