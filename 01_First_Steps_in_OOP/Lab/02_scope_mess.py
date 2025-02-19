x = "global"

def outer():
    x = "local"

    def inner():
        x = "nonlocal"
        print("inner:", x)
        print("outer:", x)

    def change_global():
        x = "global: changed!"
        print(x)

    print("outer:", x)
    inner()
    change_global()

print(x)
outer()
