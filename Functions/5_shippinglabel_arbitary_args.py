def shipping(*args,**kwargs):
    for arg in args:
        print(arg,end=" ")
    print()
    for i in kwargs.values():
        print(i,end=" ")
    print()
    print(f"{kwargs.get("colony")}")
    print(f"{kwargs.get("city")}")
    

shipping("Mr.","Shivam","Tyagi",
         House_no="592",
        colony = "Indira Colony",
        city = "Muzaffarnagar")