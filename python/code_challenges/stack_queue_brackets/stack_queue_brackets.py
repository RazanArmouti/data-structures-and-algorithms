from stack_and_queue.stack import Stack
def ValidateBrackets(str):
    """
    Multi-bracket Validation: help you to represent whether or not the brackets in the string are balanced

    arguments:string
    return: True/False

    """
    openning_bracket=["{","[","("]
    closing_bracket=["}","]",")"]
    stack_bracket=Stack()
    stack_had_brackets = False

    for i in str:
        if i in openning_bracket:
            stack_bracket.push(i)
            stack_had_brackets = True
        elif i in closing_bracket:
            if not stack_bracket.is_empty():
                bracket = stack_bracket.pop()
                if closing_bracket.index(i) != openning_bracket.index(bracket):
                    return False
                else:
                    continue
            else:
             return False
    if stack_had_brackets:
        if stack_bracket.is_empty():
            return True
        else:
            return False
    return False




if __name__=="__main__":
    print(ValidateBrackets("{}")) # True
    print(ValidateBrackets("{}(){}"))  # True
    print(ValidateBrackets("()[[Extra Characters]]"))  # True
    print(ValidateBrackets("(){}[[]]"))  # True
    print(ValidateBrackets("{}{Code}[Fellows](())"))  # True
    print(ValidateBrackets("[({}]"))  # False
    print(ValidateBrackets("(](")) # False
    print(ValidateBrackets("{(})")) # False

