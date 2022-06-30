<<<<<<< HEAD
#!/usr/bin/python3
if __name__ == "__main__":
    import add_0 as add_module
    a = 1
    b = 2
    add = add_module.add(a, b)
=======
#!/usr/bin/pytho3

if __name__ == "__main__":
    a = 1
    b = 2

    from add_0 import add
>>>>>>> 6d8299ae2bff1356129e252904a21260dddddb51
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
