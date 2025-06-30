def countdown(a):
    if a == 1 or a == 2:
        return 1
    return countdown(a-1) + countdown(a-2)
print(countdown(5))