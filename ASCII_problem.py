def enter_name():
    name = input("Enter a name: ")
    name = name.upper()
    return name


def as_key(name):
    after = "|"
    length = len(name)
    top_line = "+-" * length
    bottom_line = "+-" * length
    for each in name:
       if each == " ":
           each  = "'"
       dash = "|"
       after = after + each + dash
    return length, top_line, bottom_line, dash, after
        
        
def main():
    name = enter_name()
    length, top_line, bottom_line, dash, after = as_key(name)
    print(top_line,"\n", after,"\n", bottom_line)
   








main()
