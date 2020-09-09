# LOGIN GUI USING TKINTER
import tkinter as TK

# Function space

def logIn(user, password):
    print("user: " + user + " , password: " + password)

# Define Tkinter application

root = TK.Tk()
root.title("LOGIN USER GUI")

# Define variables

user = TK.StringVar()
user.set("")

password = TK.StringVar()
password.set("")

prompt1 = "User: "
prompt2 = "Password: "


# Define objects of GUI

label1 = TK.Label(root, text=prompt1, width=len(prompt1), bg='white')
userEntry = TK.Entry(root, textvariable=user,width=len(prompt1))
label2 = TK.Label(root, text=prompt2, width=len(prompt2), bg='white')
passwordEntry = TK.Entry(root, textvariable=password,width=len(prompt2))

# Define buttons

logInButton = TK.Button(root, text="Log in", command=logIn(userEntry.get(), passwordEntry.get()))


#set layout

label1.grid(row=0, column=0, sticky=TK.E)
userEntry.grid(row=0, column=1, sticky=TK.W)
label2.grid(row=1, column=0, sticky=TK.E)
passwordEntry.grid(row=1, column=1, sticky=TK.W)
logInButton.grid(row=2, columnspan=2, sticky=TK.E+TK.W)


TK.mainloop()




