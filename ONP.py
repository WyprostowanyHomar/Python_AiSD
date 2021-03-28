from data_struct import Stack
def IfCorrectParenthesese(napis):
    stack = Stack()
    parent = ['(',')','[',']','{','}','<','>']
    beg = ['(', '[','{','<']
    end = [')',']','}','>']
    for c in napis:
        if c in parent:
            if c in beg:
                stack.push(c)
            else:
                for i in range(len(beg)):
                    if c == end[i]:
                        if stack.top() == beg[i]:
                            stack.pop()
                        else:
                            return False
    if stack.is_empty():
        return True
    return False


def ParenthesesePosition(napis):
    stack = Stack()
    result = []
    for k in range(len(napis)):
        c = napis[k]
        if c == '(':
            stack.push(k)
        if c == ')':
            result.append([stack.top(), k])
            stack.pop()
    for pair in result:
        print(pair)
    return result


def ParenthesesePosition1(napis):
    stack = Stack()
    parent = ['(', ')', '[', ']', '{', '}', '<', '>']
    beg = ['(', '[', '{', '<']
    end = [')', ']', '}', '>']
    result = []
    for k in range(len(napis)):
        c = napis[k]
        if c in parent:
            if c in beg:
                stack.push((c,k))
            for i in range(len(beg)):
                if c == end[i]:
                    if stack.top()[0] == beg[i]:
                        result.append([stack.top()[1],k])
                        stack.pop()
                    else:
                        pass
    return result


def ConvertToONP(napis):
    stack = Stack()
    result = ''
    prev_is_num = False
    temp_num = ''
    for k in range(len(napis)):
        znak = napis[k]
        if prev_is_num and znak not in '0123456789':
            result += '[' + temp_num + ']'
            temp_num = ''
            prev_is_num = False

        if znak == '(':
            stack.push(znak)
        elif znak == ')':
            head = stack.top()
            while head != '(':
                result += head
                stack.pop()
                head = stack.top()
            stack.pop()
        elif znak in ['-', '+']:
            while (True):
                head = stack.top()
                if head in ['^', '*', '/', '+', '-']:
                    result += head
                    stack.pop()
                else:
                    break
            stack.push(znak)
        elif znak in ['*', '/']:
            while (True):
                head = stack.top()
                if head in ['^', '*', '/']:
                    result += head
                    stack.pop()
                else:
                    break
            stack.push(znak)
        elif znak == '^':
            while(True):
                head = stack.top()
                if head == '^':
                    result += head
                    stack.pop()
                else:
                    break
            stack.push(znak)
        elif znak ==' ':
            pass
        else:
            prev_is_num = True
            temp_num += znak
            #result += znak
    if temp_num !='':
        result+='[' + temp_num + ']'
    while not stack.is_empty():
        result += stack.top()
        stack.pop()
    return result

def ConvertToONP_priorities(napis, priority_dic = {'+':3,'-':3,'*':2,'/':2,'^':1}):
    stack = Stack()
    result = ''
    prev_is_num = False
    temp_num = ''
    for k in range(len(napis)):
        znak = napis[k]
        #jeżeli obecny znak nie jest cyfrą,a poprzedni był to nalezy zapisać całą liczbę
        if prev_is_num and znak not in '0123456789':
            result += '[' + temp_num + ']'
            temp_num = ''
            prev_is_num = False

        if znak == '(':
            stack.push(znak)
        elif znak == ')':
            head = stack.top()
            while head != '(':
                result += head
                stack.pop()
                head = stack.top()
            stack.pop()
        # jeżeli operator nie jest w słowniku, to zostanie potraktowany jak cyfra
        elif znak in priority_dic.keys():
            priority = priority_dic[znak]
            while (True):
                head = stack.top()
                if head in priority_dic.keys() and priority_dic[head] >= priority:
                    result += head
                    stack.pop()
                else:
                    break
            stack.push(znak)
        elif znak ==' ':
            pass
        else:
            prev_is_num = True
            temp_num += znak
    if temp_num !='':
        result+='[' + temp_num + ']'
    while not stack.is_empty():
        result += stack.top()
        stack.pop()
    return result

def ConvertToONP_cyfry(napis):
    stack = Stack()
    result = ''
    for k in range(len(napis)):
        znak = napis[k]
        if znak == '(':
            stack.push(znak)
        elif znak == ')':
            head = stack.top()
            while head != '(':
                result += head
                stack.pop()
                head = stack.top()
            stack.pop()
        elif znak in ['-', '+']:
            while (True):
                head = stack.top()
                if head in ['^', '*', '/', '+', '-']:
                    result += head
                    stack.pop()
                else:
                    break
            stack.push(znak)
        elif znak in ['*', '/']:
            while (True):
                head = stack.top()
                if head in ['^', '*', '/']:
                    result += head
                    stack.pop()
                else:
                    break
            stack.push(znak)
        elif znak == '^':
            while (True):
                head = stack.top()
                if head == '^':
                    result += head
                    stack.pop()
                else:
                    break
            stack.push(znak)
        elif znak == ' ':
            pass
        else:
            result += znak

    while not stack.is_empty():
        result += stack.top()
        stack.pop()
    return result
