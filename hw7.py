from collections import deque

class Stack:
    def __init__(self):
        self.stack = deque() # используем колоду или двусторонняя очередь

    def pop(self):
        """Метод удаляющий верхний элимент. Стек изменяется. Метод возвращает верхний элимент стека"""
        if len(self.stack) == 0:
            return None
        element = self.stack[-1]
        self.stack.pop()
        return element


    def push(self, item):
        """Метод добавляющий элимент на верншину стека. Метод ничего не возвращает"""
        self.stack.append(item)

    def isEmpty(self):
        """Метод проверки стека на пустоту. Должен возращать True или False"""
        if len(self.stack) == 0:
            return True
        elif len(self.stack) > 0:
            return False

    def peek(self):
        """Метод возращает верхний элимент стека, но не удаляет его. Стек не меняется"""
        if len(self.stack) == 0:
            return None
        element = self.stack[-1]
        return element

def balanced(str):
    stack = Stack()
    balance = True
    index = 0
    while index < len(str) and balance:
        symbol = str[index]
        if symbol in "([{":
            stack.push(symbol)
        else:
            if stack.isEmpty():
                balance = False
            else:
                top = stack.pop()
                if not matches(top, symbol):
                    balance = False
        index += 1
    if balance and stack.isEmpty():
        return "сбалансировано"
    else:
        return "несбалансировано"

def matches(open, close):
    opens = "([{"
    closers = ")]}"
    return opens.index(open) == closers.index(close)

#сбалансированные
string_1 = '(((([{}]))))'
string_2 = '[([])((([[[]]])))]{()}'
string_3 = '{{[()]}}'

#несбалансированные
string_4 = '}{}'
string_5 = '{{[(])]}}'
string_6 = '[[{())}]'

print(balanced(string_1))