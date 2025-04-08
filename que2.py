def checks(month):
    for letter in month:
        if letter=='r':
            exists=True
            break
        else:
            exists=False
            
    return exists
            
result=checks("arch")
print(result)
    



