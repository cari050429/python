#List Comprehension
def new_contact(x):
    """"This function takes a list and asks the user for info to add a new contact.
    If the contact already existed the functions returns false. Otherwise true."""
    
    name=str(input("Add the info for the new name:"))#get name for the contact
    nickname=input("Add the info for the new nickname:")#get nickname for contact
    try:#if phone number isnt an int it lets the user know
        number= int(input("Add the info for the new number:"))
    except ValueError:
        print("That was not a number, try again")     
              
    xyz=name,nickname,number#tuple of the new contact
    for y in range(len(x)):#goes through the list
        if xyz[0]==x[y][0]:#if the new contact name is already in the list, removes it and changes it
            x.remove(x[y])
            x.append(xyz)
            x.sort()
            print(x)
            return False#returns false because the contact was already there
    x.append(xyz)#if contact isnt there adds it to the list
    x.sort()#sorts alphabetically
    return True

def removes_contact(x):
    """Removes a contact based on the name"""
    name=input("Who's name did you want to remove?:")
    for y in range(len(x)):#for each contact in the least go through until we find the name
        if name==x[y][0]:#remove the contact 
            x.remove(x[y])
            print(x)
            return True
    return False

def find_a_contact(x,name="Beyonce Knowles", nickname="bey"):
    """By using the name or the nickname we find the contact and return it. If 
    we dont find the contact we return none"""
    for n in range(len(x)):#go through the list and see if we can match anything to a contact
        if x[n][0]==name:
            return x[n]
        elif x[n][1]==nickname:
            return x[n]##if we can return the contact
    return None#otherwise return none

def save_contact_list(x):
    """The function writes the list into a csv file. Each row has the contact name, 
    nickname, and phone number"""
    xfile=input("Enter the file name:")###Enter the name of the file
    yfile=open(xfile,'w')#open it as a write 
    for n in x:###for each part of the list
       print(n, file=yfile)#print to the file
    yfile.close()#close file

def read_contact_list():
    """Read the input from the file and return the contact list object"""
    xfile=input("Enter the file name:")
    try:#if file doesn't exist exits program and lets the person know 
        input_file=open(xfile,'r')
    except FileNotFoundError:
        print("A file with that name was not found") 
    x=[]
    for n in input_file: #add the contects into a file
        n.strip().lower()
        x.append(n)
        x.sort()
    return(x)#return the file
    
    
    

contact_list=[("Beyonce Knowles", "bey", "561-1234321"), ("Cardi B",
"Belcalis", "305-4399521"), ("Earl Simmons", "DMX", "305-1010101")]
contact_list.sort()   
x=new_contact(contact_list)
y=removes_contact(contact_list)     
z=find_a_contact(contact_list)
a=save_contact_list(contact_list)   
b = read_contact_list()      
print(b)
            
            
        

