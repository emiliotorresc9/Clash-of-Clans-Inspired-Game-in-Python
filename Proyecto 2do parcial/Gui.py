import tkinter as tk
import time
from PIL import Image, ImageTk
from tkinter import Menu, messagebox
from Heapp import *
from Clases import *
import Cola_de_doble_salida as DEQ
import random 
from tkinter import simpledialog

class Jugar:
    def __init__(self):
        self.aldea = Aldea()
        self.heap = Heap()
        self.buffer = []  
        
    def mostrar_poblacion(self):    #que se haga al mimento de presionar le boton de mostarrt población 
        poblacion = []
        for miembro in self.aldea.poblacion:             
            tipo = getattr(miembro, "tipo")
            if tipo == "Constructor":
                poblacion.append("Constructor")
            elif tipo == "Guerrero":
                poblacion.append("Guerrero")
            elif tipo == "Soldado":
                poblacion.append("Soldado")
            elif tipo == "Jinete":
                poblacion.append("Jinete")
            elif tipo == "Minero":
                poblacion.append("Minero")
            elif tipo == "Aldeano":
                poblacion.append("Aldeano")
            elif tipo == "Cazador":
                poblacion.append("Cazador")
            elif tipo == "Agricultor":
                poblacion.append("Agricultor")
            elif tipo == "Talador":
                poblacion.append("Talador")
        return poblacion
        
    def mostrar_recursos(self):
        recursos = []
        recursos.append("Wood: " + str(self.aldea.madera))
        recursos.append("Stone: " + str(self.aldea.piedra))
        recursos.append("Gold: " + str(self.aldea.oro))
        recursos.append("Fruits: " + str(self.aldea.frutos))
        recursos.append("Meat: " + str(self.aldea.carne))
        return recursos
        
    def accion(self, accion, cuantos):
        miembros = [] 
        nivel = 0
        miembros.append(accion) 
        for i in range(cuantos):            
            miembro = self.aldea.elegir_miembros(accion) 
            miembros.append(miembro) 
            nivel += getattr(miembro, accion, None)
        self.buffer.append(miembros) 
        
    def ejecutar(self):
        list_actions = []
        while self.buffer:
            self.heap.enqueue(len(self.buffer), self.buffer.pop(0))
            
        while not self.heap.is_empty():
            miembros = self.heap.dequeue()[1]
            accion = miembros.pop(0)
            list_actions.append(accion)
            if accion == "atacar":
                mi_nivel = 0
                for miembro in miembros:
                    mi_nivel += getattr(miembro, "atacar", None)
                rival = random.randint(10, mi_nivel)
                messagebox.showinfo("Warning", f"Battle level: Rival->{rival}    You->{mi_nivel}")
                muertes = game.aldea.ataque(miembros, mi_nivel, rival)
                for i in range(len(miembros) - muertes):
                    miembro = miembros.pop(random.randint(0, len(miembros)-1))
                    self.aldea.poblacion.insert_front(miembro)
                final = f"The battle finished, you suffered {muertes} casualties"
                action_message(final)
                        
            elif accion == "construir":
                edificio = miembros.pop(0)
                m = getattr(edificio,"tipo")
                build(m)
                self.aldea.construcciones.insert_front(edificio)
                list_actions.pop()
                text = "The selected members are going to " + accion
                action_message(text)      # imprimir en el textarea     
                for miembro in miembros:
                    self.aldea.poblacion.insert_front(miembro)                
                final = "Assignment "+accion+" completed"
                
                action_message(final)  # imprimir en el textarea
                
            elif accion == "ligar": 
                for persona in miembros:
                    self.aldea.poblacion.insert_front(persona)
                final = "We finished flirting"
                action_message(final)
            
            else:
                text = "The selected members are going to " + accion
                action_message(text)
                ganancias = 0            
                for miembro in miembros:
                    ganancias += getattr(miembro, accion, None)
                    self.aldea.poblacion.insert_front(miembro)
                self.aldea.ganar_recursos(accion, ganancias)
                final = "Assignment "+accion+" completed"
                action_message(final)
        
        list_actions.reverse()
        for gif in list_actions:
            root.after(1000,charge_gif(gif))
            
    def despejar_buffer(self):
        while self.buffer:
            miembros = self.buffer.pop()
            miembros.pop(0)
            for miembro in miembros:
                self.aldea.poblacion.insert_front(miembro) 

root = tk.Tk()
width, height = root.winfo_screenwidth(), root.winfo_screenheight()
root.attributes('-fullscreen', True)

game = Jugar()
current_attack = False

action = {}
action["cultivar"] = 'granjero.gif'
action["cazar"] = 'Cazador.gif'
action["minar"] = 'minero.gif'
action["talar"] = 'Talar.gif'
action["atacar"] = 'swords.gif'
action["construir"] = 'build.gif'
action["ligar"] = 'Mario.gif'

house = tk.PhotoImage(file='House.png')
colisseum = tk.PhotoImage(file='Colisseum.png')
stable = tk.PhotoImage(file='Stable.png')

buildings = {}
buildings['casa'] = house
buildings['coliseo'] = colisseum
buildings['establo'] = stable

loop = None

objetos = []

def build(building):
    global casa_id, name_b, move
    move = True
    name_b = building
    casa_id = main.create_image(400, 10, anchor=tk.NW, image=buildings[building])
    objetos.append((400, 10, casa_id,building)) 

def right(event):
    if objetos:
        main.move(objetos[-1][2], 10, 0)

def left(event):
    if objetos:
        main.move(objetos[-1][2], -10, 0)

def up(event):
    if objetos:
        main.move(objetos[-1][2], 0, -10)

def down(event):
    if objetos:
        main.move(objetos[-1][2], 0, 10)

def place(event):
    global move
    coords = main.coords(casa_id)
    a = objetos[-1][3]
    objetos[-1] = (coords[0], coords[1], casa_id,a) 
    if move:
        charge_gif('construir',name_b)
        move = False
    else:
        pass

# animaciones normales
def animation(lista,frames,current_frame=0,):
    global loop
    main.create_image(0, 0, anchor=tk.NW, image=village)
    image = lista[current_frame]
    main.create_image(500, 200, anchor=tk.NW, image=image)
    current_frame = (current_frame + 1) % frames 

    loop = root.after(50, lambda: animation(lista,frames,current_frame))

def stop_animation():
    global loop
    if loop is not None:
        root.after_cancel(loop)
        loop = None
    main.create_image(0, 0, anchor=tk.NW, image=village)
    for coord in objetos:
        main.create_image(coord[0], coord[1], anchor=tk.NW, image=buildings[coord[3]])

def start_animation(lista,frames):
    global loop
    animation(lista,frames,current_frame=0)
    root.after(4000, stop_animation)

# animaciones build
loop_build = None

def list_frames(frames, info, new_size):
    l = []
    for i in range(frames):
        info.seek(i)
        r_i = info.resize(new_size, Image.LANCZOS)
        obj = ImageTk.PhotoImage(r_i)
        l.append(obj)
    return l

def charge_gif(name,building = None):
    file = action[name]
    info = Image.open(file)
    frames = info.n_frames
    photoimage_objects = list_frames(frames, info, (400, 400))
    start_animation(photoimage_objects,frames)

num_attack = 0

def check_attack():
    if num_attack>0:
        attack = random.randint(0,7)
        if attack==0:
            action_message("",True)
            play()
        else:
            if game.buffer:
                game.ejecutar()
            else:
                action_message("No actions in buffer")
    else:
        pass

def play():
    global surrender,defense,rival
    messagebox.showinfo("Warning", "You are bieng under attack") 
    game.despejar_buffer()
    rival = random.randint(10,100)
    messagebox.showinfo("Warning", "Everyone returned to the village because of the invasion") 
    text = "Rival battle level: "+str(rival)+"\nYour battle level: "+str(game.aldea.get_nivel_batalla())
    messagebox.showinfo("Warning", text)

    surrender = tk.Button(root,text="SURRENDER",font=("Calibri", 12),cursor="hand2",bg="blue",fg="white",command=surrend)
    surrender.place(x=500, y=height - 400, relwidth=.1, relheight=.05)

    defense = tk.Button(root,text="DEFEND",font=("Calibri", 12),cursor="hand2",bg="blue",fg="white",command=defend)
    defense.place(x=900, y=height - 400, relwidth=.1, relheight=.05)

def surrend():
    surrender.destroy()
    defense.destroy()
    game.aldea.perder_recursos(rival)
    messagebox.showinfo("Warning","The other village plundered you")

def defend():
    surrender.destroy()
    defense.destroy()
    game.aldea.batalla(rival)
    messagebox.showinfo("Warning","The battle finished, you may suffered some casualties")

# Play Button
def on_button_click():
    global num_attack
    num_attack += 1
    button_build.config(state=tk.NORMAL)
    button_hunt.config(state=tk.NORMAL)
    button_farm.config(state=tk.NORMAL)
    button_mine.config(state=tk.NORMAL)
    button_chop.config(state=tk.NORMAL)
    button_attack.config(state=tk.NORMAL)
    button_flirt.config(state=tk.NORMAL)
    output_message = "   Game has started!"
    text_output.config(state=tk.NORMAL)
    text_output.insert(tk.END, output_message + "\n")
    text_output.config(state=tk.DISABLED)
    check_attack()

# x, -
def on_exit_button_click():
    root.destroy()

def minimizar():
    root.iconify()

# write text_output
def action_message(message,clean=False):
    if clean:
        text_output.config(state=tk.NORMAL)
        text_output.delete(1.0, tk.END)
        text_output.config(state=tk.DISABLED)
    else:
        text_output.config(state=tk.NORMAL)
        text_output.insert(tk.END, message + "\n")
        text_output.config(state=tk.DISABLED)

def ask_quantity(action):
    quantity = simpledialog.askinteger("Input", f"How many people do you want {action}?", minvalue=1)
    if quantity is not None and quantity<=game.aldea.poblacion.size():
        action_message(f"   {quantity} person{'s' if quantity > 1 else ''} {action}ing...") 
    return quantity

def on_hunt():
    quantity = ask_quantity("hunt")
    
    if quantity <= game.aldea.poblacion.size():
        button_build.config(state=tk.DISABLED)
        game.accion("cazar", quantity)
    else:
        messagebox.showinfo("Warning", "Not enough members")

def on_farm():
    quantity = ask_quantity("farm")
    if quantity <= game.aldea.poblacion.size():
        button_build.config(state=tk.DISABLED)
        game.accion("cultivar", quantity)
    else:
        messagebox.showinfo("Warning", "Not enough members")

def on_mine():
    quantity = ask_quantity("mine")
    if quantity <= game.aldea.poblacion.size():
        button_build.config(state=tk.DISABLED)
        game.accion("minar", quantity)
    else:
        messagebox.showinfo("Warning", "Not enough members")

def on_chop():
    quantity = ask_quantity("chop")
    if quantity <= game.aldea.poblacion.size():
        button_build.config(state=tk.DISABLED)
        game.accion("talar", quantity)
    else:
        messagebox.showinfo("Warning", "Not enough members")

def on_attack():
    quantity = ask_quantity("attack")
    if quantity <= game.aldea.poblacion.size():
        button_build.config(state=tk.DISABLED)
        game.accion("atacar", quantity)
    else:
        messagebox.showinfo("Warning", "Not enough members")

def on_build():
    pass

def on_flirt():
    pass

# New functions for the population and resources buttons
def show_population():
    action_message("   Showing population... 👥")
    population = game.mostrar_poblacion()
    for member in population:
        action_message("      "+member)
    

def show_resources():
    action_message("   Showing resources... 💰")
    recursos = game.mostrar_recursos()
    for recurso in recursos:
        action_message("      "+recurso)

# Load the village image
v = Image.open('aldea.jpg')
v = v.resize((width, height), Image.LANCZOS)
village = ImageTk.PhotoImage(v)

#main canvas
main = tk.Canvas(root, width=width, height=height)
main.place(x=0, y=0)
main.create_image(0, 0, anchor=tk.NW, image=village)

main.bind("<Right>", right)
main.bind("<Left>", left)
main.bind("<Up>", up)
main.bind("<Down>", down)
main.bind("<Return>", place)

main.focus_set()

# MENU: build for constructing 
def casa():
    data = game.aldea.construir(game.aldea.poblacion.size(), 1)
    if data == False:
        messagebox.showinfo("Warning", "Not enough members")
    elif data == None:
        messagebox.showinfo("Warning", "Not enough resources to build it")
    else:
        button_build.config(state=tk.DISABLED)
        button_hunt.config(state=tk.DISABLED)
        button_farm.config(state=tk.DISABLED)
        button_mine.config(state=tk.DISABLED)
        button_chop.config(state=tk.DISABLED)
        button_attack.config(state=tk.DISABLED)
        button_flirt.config(state=tk.DISABLED)
        action_message("   Building a house... 🏠")
        game.buffer.append(data)

def coliseo():
    data = game.aldea.construir(game.aldea.poblacion.size(), 2)
    if data == False:
        messagebox.showinfo("Warning", "Not enough members")
    elif data == None:
        messagebox.showinfo("Warning", "Not enough resources to build it")
    else:
        button_build.config(state=tk.DISABLED)
        button_hunt.config(state=tk.DISABLED)
        button_farm.config(state=tk.DISABLED)
        button_mine.config(state=tk.DISABLED)
        button_chop.config(state=tk.DISABLED)
        button_attack.config(state=tk.DISABLED)
        button_flirt.config(state=tk.DISABLED)
        action_message("   Building a coliseum... 🏟")
        game.buffer.append(data)

def establo():
    data = game.aldea.construir(game.aldea.poblacion.size(), 3)
    if data == False:
        messagebox.showinfo("Warning", "Not enough members")
    elif data == None:
        messagebox.showinfo("Warning", "Not enough resources to build it")
    else:
        button_build.config(state=tk.DISABLED)
        button_hunt.config(state=tk.DISABLED)
        button_farm.config(state=tk.DISABLED)
        button_mine.config(state=tk.DISABLED)
        button_chop.config(state=tk.DISABLED)
        button_attack.config(state=tk.DISABLED)
        button_flirt.config(state=tk.DISABLED)
        action_message("   Building a stable... 🐎")
        game.buffer.append(data)

def cuantos_ligan(ligue, maxx):
    quantity = simpledialog.askinteger("Input", f"How many {ligue} (maximum {maxx})?", minvalue=1)
    if quantity is not None:
        if quantity > maxx:
            messagebox.showinfo("Warning", "Maximum exceeded")
            return False
        return quantity

# Menu options for flirting
def ligar_constructor(): 
    miembros = game.aldea.ligar(game.aldea.construcciones, 1, 1)
    if miembros == "Coliseo":
        messagebox.showinfo("Warning", "Need a Colosseum")
    elif miembros == "Establo":
        messagebox.showinfo("Warning", "Need a stable")
    elif miembros == "recursos":
        messagebox.showinfo("Warning", "Need more resources")
    else:
        miembros.insert(0, "ligar")
        game.buffer.append(miembros)
        button_build.config(state=tk.DISABLED)
        action_message("   Flirting with the builder... ❤")
    
def ligar_guerrero():
    cuantos = cuantos_ligan("guerrero", 2)
    miembros = game.aldea.ligar(game.aldea.construcciones, 2, cuantos)
    if miembros == "Coliseo":
        messagebox.showinfo("Warning", "Need a Colosseum")
    elif miembros == "Establo":
        messagebox.showinfo("Warning", "Need a stable")
    elif miembros == "recursos":
        messagebox.showinfo("Warning", "Need more resources")
    else:
        miembros.insert(0, "ligar")
        game.buffer.append(miembros)
        button_build.config(state=tk.DISABLED)
        action_message("   Flirting with the warrior... ❤")
        
def ligar_soldado():
    si = False
    coliseos = 0
    for edificio in game.aldea.construcciones:
        if getattr(edificio, "tipo") == "coliseo":
            si = True
            coliseos += 1
    if si == True:
        cuantos = cuantos_ligan("soladado", 2*coliseos) 
        miembros = game.aldea.ligar(game.aldea.construcciones, 3, cuantos)
        if miembros == "Coliseo":
            messagebox.showinfo("Warning", "Need a Colosseum")
        elif miembros == "Establo":
            messagebox.showinfo("Warning", "Need a stable")
        elif miembros == "recursos":
            messagebox.showinfo("Warning", "Need more resources")
        else:
            miembros.insert(0, "ligar")
            game.buffer.append(miembros)
            button_build.config(state=tk.DISABLED)
            action_message("   Flirting with the soldier... ❤")
    else:
        messagebox.showinfo("Warning", "Need a Colosseum")

def ligar_jinete():
    si = False
    establos = 0
    for edificio in game.aldea.construcciones:
        if getattr(edificio, "tipo") == "establo":
            si = True
            establos += 1
    if si == True:
        cuantos = cuantos_ligan("jinete", establos)
        miembros = game.aldea.ligar(game.aldea.construcciones, 4, cuantos)
        if miembros == "Coliseo":
            messagebox.showinfo("Warning", "Need a Colosseum")
        elif miembros == "Establo":
            messagebox.showinfo("Warning", "Need a stable")
        elif miembros == "recursos":
            messagebox.showinfo("Warning", "Need more resources")
        else:
            miembros.insert(0, "ligar")
            game.buffer.append(miembros)
            button_build.config(state=tk.DISABLED)
            action_message("   Flirting with the knight... ❤")
    else:
        messagebox.showinfo("Warning", "Need a stable")

def ligar_minero(): 
    miembros = game.aldea.ligar(game.aldea.construcciones, 5, 1)
    if miembros == "Coliseo":
        messagebox.showinfo("Warning", "Need a Colosseum")
    elif miembros == "Establo":
        messagebox.showinfo("Warning", "Need a stable")
    elif miembros == "recursos":
        messagebox.showinfo("Warning", "Need more resources")
    else:
        miembros.insert(0, "ligar")
        game.buffer.append(miembros)
        button_build.config(state=tk.DISABLED)
        action_message("   Flirting with the miner... ❤")

def ligar_aldeano():
    si = False
    casas = 0
    for edificio in game.aldea.construcciones:
        if getattr(edificio, "tipo") == "casa":
            si = True
            casas += 1
    if si == True:
        cuantos = cuantos_ligan("aldeano", casas*3)
        miembros = game.aldea.ligar(game.aldea.construcciones, 6, cuantos)
        if miembros == "Coliseo":
            messagebox.showinfo("Warning", "Need a Colosseum")
        elif miembros == "Establo":
            messagebox.showinfo("Warning", "Need a stable")
        elif miembros == "recursos":
            messagebox.showinfo("Warning", "Need more resources")
        else:
            miembros.insert(0, "ligar")
            game.buffer.append(miembros)
            button_build.config(state=tk.DISABLED)
            action_message("   Flirting with the villager... ❤")
    else:
        messagebox.showinfo("Warning", "Necesitas una Casa")

def ligar_cazador(): 
    miembros = game.aldea.ligar(game.aldea.construcciones, 7, 1)
    if miembros == "Coliseo":
        messagebox.showinfo("Warning", "Necesitas un Coliseo")
    elif miembros == "Establo":
        messagebox.showinfo("Warning", "Necesitas un Establo")
    elif miembros == "recursos":
        messagebox.showinfo("Warning", "Necesitas mas recursos")
    else:
        miembros.insert(0, "ligar")
        game.buffer.append(miembros)
        button_build.config(state=tk.DISABLED)
        action_message("   Flirting with the hunter... ❤")

def ligar_agricultor(): 
    miembros = game.aldea.ligar(game.aldea.construcciones, 8, 1)
    if miembros == "Coliseo":
        messagebox.showinfo("Warning", "Necesitas un Coliseo")
    elif miembros == "Establo":
        messagebox.showinfo("Warning", "Necesitas un Establo")
    elif miembros == "recursos":
        messagebox.showinfo("Warning", "Necesitas mas recursos")
    else:
        miembros.insert(0, "ligar")
        game.buffer.append(miembros)
        button_build.config(state=tk.DISABLED)
        action_message("   Flirting with the farmer... ❤")

def ligar_talador(): 
    miembros = game.aldea.ligar(game.aldea.construcciones, 9, 1)
    if miembros == "Coliseo":
        messagebox.showinfo("Warning", "Necesitas un Coliseo")
    elif miembros == "Establo":
        messagebox.showinfo("Warning", "Necesitas un Establo")
    elif miembros == "recursos":
        messagebox.showinfo("Warning", "Necesitas mas recursos")
    else:
        miembros.insert(0, "ligar")
        game.buffer.append(miembros)
        button_build.config(state=tk.DISABLED)
        action_message("   Flirting with the lumberjack... ❤")

# Creating the build and flirt options menus
build_options = tk.Menu(root, tearoff=0)
build_options.add_command(label="House", command=casa)
build_options.add_command(label="Colosseum", command=coliseo)
build_options.add_command(label="Stable", command=establo)

flirt_options = tk.Menu(root, tearoff=0)
flirt_options.add_command(label="Builder", command=ligar_constructor)
flirt_options.add_command(label="Warrior", command=ligar_guerrero)
flirt_options.add_command(label="Soldier", command=ligar_soldado)
flirt_options.add_command(label="Knight", command=ligar_jinete)
flirt_options.add_command(label="Miner", command=ligar_minero)
flirt_options.add_command(label="Villager", command=ligar_aldeano)
flirt_options.add_command(label="Hunter", command=ligar_cazador)
flirt_options.add_command(label="Farmer", command=ligar_agricultor)
flirt_options.add_command(label="Lumberjack", command=ligar_talador)

def build_menu(event):
    if button_build['state'] == tk.NORMAL:
        build_options.post(event.x_root, event.y_root)

def flirt_menu(event):
    if button_flirt['state'] == tk.NORMAL:
        flirt_options.post(event.x_root, event.y_root)

# Creating the buttons
button_START = tk.Button(root, text="▶", command=on_button_click, bg="black", fg="white", font=("Georgia", 18), width=5, height=1, cursor="hand2")
button_START.place(x=width - 110, y=height - 95)

button_hunt = tk.Button(root, text="HUNT", command=on_hunt, bg="lightgreen", fg="black", font=("Calibri", 12), cursor="hand2")
button_hunt.place(x=width - 1500, y=height - 90, relwidth=.1, relheight=.05)

button_farm = tk.Button(root, text="FARM", command=on_farm, bg="lightgreen", fg="black", font=("Calibri", 12), cursor="hand2")
button_farm.place(x=width - 1300, y=height - 90, relwidth=.1, relheight=.05)

button_mine = tk.Button(root, text="MINE", command=on_mine, bg="lightgreen", fg="black", font=("Calibri", 12), cursor="hand2")
button_mine.place(x=width - 1100, y=height - 90, relwidth=.1, relheight=.05)

button_chop = tk.Button(root, text="CHOP", command=on_chop, bg="lightgreen", fg="black", font=("Calibri", 12), cursor="hand2")
button_chop.place(x=width - 900, y=height - 90, relwidth=.1, relheight=.05)

button_attack = tk.Button(root, text="ATTACK", command=on_attack, bg="lightgreen", fg="black", font=("Calibri", 12), cursor="hand2")
button_attack.place(x=width - 300, y=height - 90, relwidth=.1, relheight=.05)

button_build = tk.Button(root, text="BUILD", command=on_build, bg="lightgreen", fg="black", font=("Calibri", 12), cursor="hand2")
button_build.place(x=width - 500, y=height - 90, relwidth=.1, relheight=.05)
button_build.bind("<Button-1>", build_menu)

button_flirt = tk.Button(root, text="FLIRT", command=on_flirt, bg="lightgreen", fg="black", font=("Calibri", 12), cursor="hand2")
button_flirt.place(x=width - 700, y=height - 90, relwidth=.1, relheight=.05)
button_flirt.bind("<Button-1>", flirt_menu)

button_EXIT = tk.Button(root, text="x", command=on_exit_button_click, bg="red", fg="white", font=("Arial", 11), cursor="hand2")
button_EXIT.place(x=width - 60, y=0, relwidth=.04, relheight=.03)

button_MIN = tk.Button(root, text="-", command=minimizar, bg="blue", fg="white", font=("Arial", 11), cursor="hand2")
button_MIN.place(x=width - 123, y=0, relwidth=.04, relheight=.03)

people = Image.open('People.png')
population = ImageTk.PhotoImage(people)
button_population = tk.Button(root,image = population, command=show_population, bg="red", fg="white", cursor="hand2")
button_population.place(x=width-1500, y=height-200,relwidth=.06,relheight=.09)

resource = Image.open('Cofre.png')
chest = ImageTk.PhotoImage(resource)
button_resources = tk.Button(root, image=chest, command=show_resources, bg="red", fg="white", font=("Calibri", 14), cursor="hand2")
button_resources.place(x=width - 1390, y=height-200, relwidth=.06, relheight=.09)

# Activity record
label_header = tk.Label(root, text="ACTIVITY RECORD", bg="lightblue", fg="black", font=("Georgia", 14), width=20, height=2)
label_header.place(x=14, y=height - 840)

# Create a frame to hold the text widget and scrollbar
frame = tk.Frame(root)
frame.place(x=15, y=height - 780)

# Create the scrollbar
scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Create the text output area
text_output = tk.Text(frame, height=25, width=20, bg="lightblue", font=("Georgia", 12), yscrollcommand=scrollbar.set)  # Link scrollbar to text
text_output.pack(side=tk.LEFT)

# Configure the scrollbar
scrollbar.config(command=text_output.yview)  # Link the scrollbar to the text widget
    
root.mainloop()