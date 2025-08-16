rLoaded = False
oLoaded = False
main = True
useHistory = True
hLoaded = False
history = []
print("For programs run 'ls -p'")
while main:
    a = input("shell: ")
    if useHistory:
        if hLoaded:
            history.append(a)
    if a == "ls -p":
        print("ls\nhistory\nexit\ninfo\ndice\nguess\nr\no\n")
    elif a == "info":
        print("v: 1.1.0")
        if rLoaded:
            print("r: loaded")
        else:
            print("r: unloaded")
        if oLoaded:
            print("o: loaded")
        else:
            print("o: unloaded")
    elif a == "exit":
        del a
        if rLoaded:
            del random
        if oLoaded:
            del options
        if hLoaded:
            del history
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
            options = ["a","b","c","d"]
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
    elif a == "history" or a == "history --help":
        print("Usage: history [-u,-c,-s,-t,-l,-g]")
        print("-u: unloads history from memory")
        print("-c: clears the history")
        print("-s: shows history")
        print("-t: toggles history")
        print("-l: loads history into memory")
        print("-g: returns history load status")
    elif a == "history -g":
        if hLoaded:
            print("history loaded")
        else:
            print("history unloaded")
    elif a == "history -l":
        if not hLoaded:
            hLoaded = True
            history = []
            print("history loaded")
        else:
            print("history is already loaded")
    elif a == "history -u":
        if hLoaded:
            hLoaded = False
            del history
            print("history unloaded")
        else:
            print("history is not loaded")
    elif a == "history -c":
        if hLoaded:
            if useHistory:
                history = []
                print("history cleared")
            else:
                print("history is disabled")
        else:
            print("history is not loaded")
    elif a == "history -s":
        if useHistory:
            if hLoaded:
                print("\n".join(history))
            else:
                print("history is not loaded")
        else:
            print("history is not enabled")
    elif a == "history -t":
        if useHistory:
            useHistory = False
            print("history disabled")
        else:
            useHistory = True
            print("history enabled")
del main
del useHistory
del oLoaded
del rLoaded
del hLoaded
