-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134707891
-- LeetCode 66. 加一 — Lua 版（方案1）
local function plus_one(digits) -- local function plus_one(digits)
	local d = { table.unpack(digits) } -- 把 {table.unpack(digits)} 写入 local d
	for i = #d, 1, -1 do -- 把 #d, 1, 减 1 do 写入 for i
		if d[i] < 9 then
			d[i] = d[i] + 1
			return d
		end -- 若 d[下标 i] 小于 9 then d[下标 i] 赋值为 d[下标 i] 加 1 return d 终点
		d[i] = 0 -- 把 0 写入 d[i]
	end -- 终点
	return { 1, table.unpack(d) } -- 返回 {1, table.unpack(d)}
end -- 终点
assert(table.concat(plus_one({ 1, 2, 3 }), ",") == "1,2,4") -- 打印输出
assert(table.concat(plus_one({ 4, 3, 2, 1 }), ",") == "4,3,2,2") -- 打印输出
assert(table.concat(plus_one({ 9 }), ",") == "1,0") -- 打印输出
print("PASS") -- 全部用例通过，输出 PASS
