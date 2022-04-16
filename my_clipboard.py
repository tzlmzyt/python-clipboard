import sys
import clipboard
import json


print("")
print("--------------------------- 1 ------------------------")
print(sys)
print("")
print(sys.argv)
print("")
print(clipboard)
print("")
print(json)
print("") 
print("") 
print("") 
print("--------------------------- 2 ------------------------")

print("") 
print(sys.argv[1:])

print("") 
print(len(sys.argv))

print("") 
print("") 
print("") 
print("--------------------------- 3 ------------------------")



def save_json(filepath, data):
    with open(filepath, "w"):
        # as f
        f = open(filepath, "w")
        
        print("* f:", end=" ")
        print(f)
        print("")
        
        print("""* open(filepath, "w"):""", end=" ")
        print(open(filepath, "w"))
        print("")
                
        # json.dump(data, open(filepath, "w"))
        json.dump(data, f)
        print("* json.dump:", end=" ")
        print(json.dump)
        
        print("* json.dump(data, f):", end=" ")
        print("")


save_json("data.json", {'key':'hhh'})
save_json("data.json", {'key2':'hhhh'})


def load_json(filepath):
    with open(filepath, "r"):
        f2 = open(filepath, "r")
        print("* f2:", end=" ")
        print(f2)

        print("""* open(filepath, "r"):""", end=" ")
        print(open(filepath, "r"))
        print("")        
        
        
        data = json.load(f2)
        print("""* json.load(open(filepath, "r")):""" , end = " ")
        print(json.load(open(filepath, "r")))
        
        print("* data:", end = "")
        print(data)
        return data
        

#load_json("data.json")


print("") 
print("") 



if len(sys.argv) > 1:    
    command = sys.argv[1]
    print("The command has got： " + command +"\n")
    if command == "-save":
        print("I have already saved your text.")
    elif command == "-load":
        print("I have already loaded your text.")
    elif command == '-list':
        print("I have already listed your text.")
    elif command == "-help":
        print("")
        print("my_clipboard.py -save 1234")
        print("I will save your text: 1234")
        print("")
        
        
    else:
        print('Aw, It looks like a unkown command.')
else:
    print("Tring to use this command: -save, -load, -list, -help.")


print("") 
print("") 
print("") 


