-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134120377
-- LeetCode 707. 设计链表 — Lua 版（方案1）
local MyList = {} -- 把 {} 写入 local MyList
MyList.__index = MyList -- 把 MyList 写入 MyList.__index
function MyList.new()
	return setmetatable({ items = {} }, MyList)
end
function MyList:addAtHead(x)
	table.insert(self.items, 1, x)
end -- function MyList:addAtHead(x) table 插入 self.items, 1, x) 终点
function MyList:addAtTail(x)
	self.items[#self.items + 1] = x
end
function MyList:addAtIndex(i, x) -- function MyList:addAtIndex(下标 i, x)
	if i < 0 then
		i = 0
	end -- 若 下标 i 小于 0 then 下标 i 赋值为 0 终点
	if i <= #self.items then
		table.insert(self.items, i + 1, x)
	end
end -- 终点
function MyList:get(i) -- function MyList:get(下标 i)
	if i >= 0 and i < #self.items then
		return self.items[i + 1]
	end
	return -1 -- 返回 减 1
end -- 终点
function MyList:deleteAtIndex(i) -- function MyList:deleteAtIndex(下标 i)
	if i >= 0 and i < #self.items then
		table.remove(self.items, i + 1)
	end
end -- 终点
local l = MyList.new() -- 把 MyList.new() 写入 local l
l:addAtHead(1) -- 左指针:addAtHead(1)
l:addAtTail(3) -- 左指针:addAtTail(3)
l:addAtIndex(1, 2) -- 左指针:addAtIndex(1, 2)
assert(l:get(1) == 2) -- 断言校验
l:deleteAtIndex(1) -- 左指针:deleteAtIndex(1)
assert(l:get(1) == 3) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
