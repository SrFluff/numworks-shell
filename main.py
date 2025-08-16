rLoaded = False
oLoaded = False
main = True
print("For programs run 'ls -p'")
while main:
    a = input("shell: ")
    if a == "ls -p":
        print("ls\nexit\ninfo\ndice\nguess\nr\no\n")
    elif a == "info":
        print("v: 1.0.0")
        print("b: 0")
    elif a == "exit":
        del a
        if rLoaded:
            del random
        if oLoaded:
            del options
        main = False
    elif a == "dice":
        if not rLoaded:
            import random
            rLoaded = True
        print(random.randint(1,6))
    elif a == "r" or a == "r --help":
        print("Usage: r [-s,-l,-u]")
        print("-s: random loaded status")
        print("-l: load random")
        print("-u: unload random")
    elif a == "r -u":
        if rLoaded:
            rLoaded = False
            del random
            print("random has been unloaded")
        else:
            print("random is not loaded")
    elif a == "r -s":
        if rLoaded:
            print("random is loaded")
        else:
            print("random is not loaded")
    elif a == "r -l":
        if not rLoaded:
            import random
            rLoaded = True
            print("random loaded into memory")
        else:
            print("random is already loaded")
    elif a == "guess":
        if not rLoaded:
            rLoaded = True
            import random
        if not oLoaded:
            oLoaded = True
        options = ["a","b","c","d"]
        print(options[random.randint(0,3)])
    elif a == "o" or a == "o --help":
        print("Usage: o [-s,-l,u]")
        print("-s: options loaded status")
        print("-l: load options")
        print("-u: unload options")
    elif a == "o -s":
        if oLoaded:
            print("options is loaded")
        else:
            print("options is not loaded")
    elif a == "o -l":
        if not oLoaded:
            oLoaded = True
            print("option loaded into memory")
        else:
            print("option is already loaded")
    elif a == "o -u":
        if oLoaded:
            oLoaded = False
            del options
            print("options has been unloaded")
        else:
            print("options is not loaded")
del main