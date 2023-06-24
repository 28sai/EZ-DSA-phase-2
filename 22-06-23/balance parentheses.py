def paraCheck(seq): 
    while True: 
        if '()' in seq or "[]" in seq or "{}" in seq:  
            return True
        
        else:
            pass
    return False
  
seq =input()
print(paraCheck(seq))  