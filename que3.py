def stored(month):
    count=0
    for letter in month:
        if letter=='r':
            count+=1
    return count
result=stored("marchjranuary")
print(result)
    