def ValidateBrackets(str):
    """
    Multi-bracket Validation: help you to represent whether or not the brackets in the string are balanced

    arguments:string
    return: True/False

    """
    openning_bracket=["{","[","("]
    closing_bracket=["}","]",")"]
    stack_bracket=[]

    for i in str:
        if i in openning_bracket:
            stack_bracket.append(i)
        elif i in closing_bracket:
            idx=closing_bracket.index(i)
            if stack_bracket and (openning_bracket[idx] == stack_bracket[len(stack_bracket)-1]) :
               stack_bracket.pop()
    if not stack_bracket :
        return True
    else:
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

