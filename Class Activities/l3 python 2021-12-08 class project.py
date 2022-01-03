from Stack import Stack
# Question 27- Given a string of arithmetic expressions/
# with brackets, determine if brackets are matching in\
# pairs, means that open bracket matches with close/
# bracket

class Expression:
    def __init__(self, expression):
        self.expression = expression

    def check_brackets(self):
        if self.expression==None or self.expression == "":
            return False
        sta = Stack()
        for ch in self.expression:
            if ch == '(':
                sta.push(ch)
            elif ch ==')':
                if sta.is_empty():
                    return False
                sta.pop()
        return sta.is_empty()

def test():
    expr = "(((a+b)*((c+d)))/(d+(a&c))"
    checker = Expression(expr)
    result = checker.check_brackets()
