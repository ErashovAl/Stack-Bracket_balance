from stack import Stack

st = Stack()

def brackets(text, pattern = '(){}[]'):
 
    opened, closed = pattern[::2], pattern[1::2]
    if text == '':
        return False

    if text[0] in closed:# or len(text) %2
        return False

    for el in text:
        if el in opened:
            st.push(opened.index(el))
        elif el in closed:
            if st.stack and st.stack[-1] == closed.index(el):
                st.pop()
            else: return False

    return True


if __name__ == '__main__':
    
    sequence = input('Введите последовательность: ')

    if brackets(sequence):
        print('"Сбалансированно"')
    else:
        print('"Несбалансированно"')