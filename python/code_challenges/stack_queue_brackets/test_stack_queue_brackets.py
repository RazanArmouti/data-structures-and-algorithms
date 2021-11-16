from stack_queue_brackets import ValidateBrackets

def test_ValidateBrackets_1():
    assert ValidateBrackets("{}") == True

def test_ValidateBrackets_2():
    assert ValidateBrackets("{}(){}") == True

def test_ValidateBrackets_3():
    assert ValidateBrackets("()[[Extra Characters]]") == True

def test_ValidateBrackets_4():
    assert ValidateBrackets("(){}[[]]") == True

def test_ValidateBrackets_5():
    assert ValidateBrackets("(](") == False

def test_ValidateBrackets_6():
    assert ValidateBrackets("{(})") == False
