def mysplit(arg: str) -> list:
    if not len(arg.strip()):
        return []
    return arg.split()

print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))