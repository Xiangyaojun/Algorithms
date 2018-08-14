# coding:utf-8

'''
leetcode 224
题目:使用栈实现队列的下列操作：

push(x) -- 将一个元素放入队列的尾部。
pop() -- 从队列首部移除元素。
peek() -- 返回队列首部的元素。
empty() -- 返回队列是否为空。
示例:

MyQueue queue = new MyQueue();

queue.push(1);
queue.push(2);  
queue.peek();  // 返回 1
queue.pop();   // 返回 1
queue.empty(); // 返回 false
说明:

你只能使用标准的栈操作 -- 也就是只有 push to top, peek/pop from top, size, 和 is empty 操作是合法的。
你所使用的语言也许不支持栈。你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准的栈操作即可。
假设所有操作都是有效的 （例如，一个空的队列不会调用 pop 或者 peek 操作）。


'''

class MyQueue:

    def __init__(self):
        self.stack_1 = []
        self.stack_2 = []
        

    def push(self, x):
        while len(self.stack_2)>0:
            temp  = self.stack_2.pop(-1)
            self.stack_1.append(temp) 
        self.stack_1.append(x)

    def pop(self):
        while len(self.stack_1) > 0:
            temp = self.stack_1.pop(-1)
            self.stack_2.append(temp)
        return self.stack_2.pop()

    def peek(self):
        while len(self.stack_1) > 0:
            temp = self.stack_1.pop(-1)
            self.stack_2.append(temp)

        result = self.stack_2[-1]
        while len(self.stack_2) >0:
            temp = self.stack_2.pop(-1)
            self.stack_1.append(temp)
        return result
        

    def empty(self):
        if len(self.stack_1)==0 and len(self.stack_2)==0:
            return True
        else:
            return False
        


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(2)
obj.push(3)
print(obj.pop())
print(obj.pop())
print(obj.pop())

