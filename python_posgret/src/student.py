from tkinter import Tk , Canvas , Label, Frame, Entry, Button, E, W
import psycopg2





root = Tk()
root.title("python_posgret")

def guardar_nuevo_usuario(name, password, Email):
   conn= psycopg2.connect("dbname = python_intermedio_db user = postgres password =123456")
   cur = conn.cursor()

   cur.execute("SELECT * FROM usuarios;")
   print(cur.fetchone())

# Canvas 

canvas = Canvas(root, height = 380, width = 400)
canvas.pack()

frame = Frame()
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

label=Label(frame, text= 'Agrega un Usuario')
label.grid(row=0, column=1)

# entreda usuario
label=Label(frame, text= 'Nombre de Usuario')
label.grid(row=1, column=0)

entry_name = Entry(frame)
entry_name.grid(row=1, column=1)

# entrada password
label=Label(frame, text= 'Password')
label.grid(row=2, column=0)

entry_password = Entry(frame)
entry_password.grid(row=2, column=1)

# entrada email
label=Label(frame, text= 'Email')
label.grid(row=3, column=0)

entry_Email = Entry(frame)
entry_Email.grid(row=3, column=1)


button = Button(frame, text="Guardar", command=lambda:guardar_nuevo_usuario(
    entry_name.get(),
    entry_password.get(),
    entry_Email.get()
    ))
button.grid(row=4, column=1, sticky=W+E)


root.mainloop()

