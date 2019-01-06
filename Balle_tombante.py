from tkinter import *
from random import randrange

pos_X=250
pos_Y=250
score_joueur1 = 0
score_joueur2 = 0
dx = 1
dy = 2
temps = 0
points_pour_victoire = 0
delete_victoire = False
stop = True
delete_rejouer = False
delete_vitesse = False

def play():
    global jeu, rejouer, delete_victoire, score_joueur1, score_joueur2, vitesse,delete_vitesse
    def Update():
        global menu_principale, score_joueur1, score_joueur2, delete_rejouer, rejouer, vitesse, delete_vitesse
        if canvas.coords(balle)[2]>=500:
            score_joueur1 = score_joueur1 + 1
            victoire_joueur()
            Rejouer()
        if canvas.coords(balle)[0]<=0:
            score_joueur2 = score_joueur2 + 1
            victoire_joueur()
            Rejouer()
        deplacement()
        jeu.after(temps,Update)
        if delete_rejouer == True:
            delete_rejouer = False
            rejouer.destroy()
        if delete_vitesse == True:
            delete_vitesse = False
            vitesse.destroy()


    def deplacement():
        global dx, dy
        if canvas.coords(balle)[3]>=500:
            dy=-1*dy
        if canvas.coords(balle)[1]<=0:
            dy=-1*dy
        if canvas.coords(balle)[3]>=canvas.coords(raquette_joueur1)[1] and canvas.coords(balle)[2]>=canvas.coords(raquette_joueur1)[0] and canvas.coords(balle)[0]<=canvas.coords(raquette_joueur1)[2] and canvas.coords(balle)[3]<=canvas.coords(raquette_joueur1)[3]:
            dx=-1*dx
        if canvas.coords(balle)[3]>=canvas.coords(raquette_joueur2)[1] and canvas.coords(balle)[2]>=canvas.coords(raquette_joueur2)[0] and canvas.coords(balle)[0]<=canvas.coords(raquette_joueur2)[2] and canvas.coords(balle)[3]<=canvas.coords(raquette_joueur2)[3]:
            dx=-1*dx
        canvas.move(balle, dx, dy)

    def KeyBoard(event):
        Key = event.keysym
        if Key == 'Up':
            canvas.move(raquette_joueur1,0,-15)
        if Key == 'Down':
            canvas.move(raquette_joueur1,0,15)
        if Key == 'r':
            canvas.move(raquette_joueur2,0,-15)
        if Key == 'f':
            canvas.move(raquette_joueur2,0,15)
    
    def victoire_joueur():
        global points_pour_victoire, score_joueur1, score_joueur2, stop, fenetre,jeu
        if points_pour_victoire == score_joueur1:
            jeu.destroy()
            fenetre = Tk()
            fenetre.geometry("300x250")
            label = Label(fenetre, text="Le joueur 1 gagne la partie !")
            label.pack(padx = 10, pady = 10)
            button_quitter_jeu = Button(fenetre, text = "  Quitter  ", command = fenetre.destroy)
            button_quitter_jeu.pack(padx = 10, pady = 10)
            fenetre.mainloop()
            score_joueur1 = 0
        if points_pour_victoire == score_joueur2:
            jeu.destroy()
            score_joueur2 = 0
            fenetre = Tk()
            fenetre.geometry("300x250")
            label = Label(fenetre, text="Le joueur 2 gagne la partie !")
            label.pack(padx = 10, pady = 10)
            button_quitter_jeu = Button(fenetre, text = "  Quitter  ", command = fenetre.destroy)
            button_quitter_jeu.pack(padx = 10, pady = 10)
            fenetre.mainloop()
    
    jeu = Tk()
    jeu.title("Game")
    canvas = Canvas(jeu, width = 500, height = 500, bd = 0, bg = "white")
    canvas.pack(padx = 10, pady = 10)

    Bouton_Quitter = Button(jeu, text = "Quitter", command = jeu.destroy)
    Bouton_Quitter.pack()

    Bouton_score_joueur1 = Button(jeu, text = "Score: " + str(score_joueur1))
    Bouton_score_joueur1.pack()

    Bouton_score_joueur2 = Button(jeu, text = "Score: " + str(score_joueur2))
    Bouton_score_joueur2.pack()

    balle = canvas.create_oval(pos_X, pos_Y ,pos_X+20, pos_Y+20, fill = 'red')
    raquette_joueur1 = canvas.create_rectangle(10, 240, 20, 320,fill = 'black')
    raquette_joueur2 = canvas.create_rectangle(480, 240, 490, 320,fill = 'black')

    canvas.focus_set()
    canvas.bind('<Key>',KeyBoard)

    Update()

    jeu.mainloop()

def Nombre_de_Victoires():
    global menu_principale, victoire
    menu_principale.destroy()
    victoire = Tk()
    victoire.title("Choix du nombre de points à obtenir pour une victoire !")
    victoire.geometry("500x250")

    button_points1 = Button(victoire, text = "  1  ", command = Victoire1)
    button_points1.pack(padx = 10, pady = 10)

    button_points1 = Button(victoire, text = "  2  ", command = Victoire2)
    button_points1.pack(padx = 10, pady = 10)

    button_points1 = Button(victoire, text = "  3  ", command = Victoire3)
    button_points1.pack(padx = 10, pady = 10)

    victoire.mainloop()

def Choix_de_la_vitesse():
    global vitesse,victoire
    victoire.destroy()
    vitesse = Tk()
    vitesse.title("Choix de la vitesse de la balle !")
    vitesse.geometry("500x250")

    button_vitesse_bas = Button(vitesse, text = "  Vitesse basse  ", command = Vitesse1)
    button_vitesse_bas.pack(padx = 10, pady = 10)

    button_vitesse_normal = Button(vitesse, text = "  Vitesse normale  ", command = Vitesse2)
    button_vitesse_normal.pack(padx = 10, pady = 10)

    button_vitesse_rapide = Button(vitesse, text = "  Vitesse rapide  ", command = Vitesse3)
    button_vitesse_rapide.pack(padx = 10, pady = 10)

    vitesse.mainloop()

def Victoire1():
    global points_pour_victoire, victoire, delete_victoire
    points_pour_victoire = 1
    delete_victoire = True
    Choix_de_la_vitesse()

def Victoire2():
    global points_pour_victoire, victoire, delete_victoire
    points_pour_victoire = 2
    delete_victoire = True
    Choix_de_la_vitesse()

def Victoire3():
    global points_pour_victoire, victoire, delete_victoire
    points_pour_victoire = 3
    delete_victoire = True
    Choix_de_la_vitesse()

def Vitesse1():
    global temps, delete_vitesse
    temps = 15
    delete_vitesse = True
    play()

def Vitesse2():
    global temps, delete_vitesse
    temps = 10
    delete_vitesse = True
    play()

def Vitesse3():
    global temps, delete_vitesse
    temps = 7
    delete_vitesse = True
    play()

def Rejouer():
    global rejouer, jeu, delete_rejouer
    delete_rejouer = True
    jeu.destroy()
    rejouer = Tk()
    rejouer.title("Rejouer")
    rejouer.geometry("300x250")

    button_rejouer = Button(rejouer, text ="   Rejouer   ", command = play)
    button_rejouer.pack(padx = 10, pady = 10)
        
    button_quitter_rejouer = Button(rejouer, text ="   Partir    ", command = rejouer.destroy)
    button_quitter_rejouer.pack(padx = 10, pady = 10)
        
    rejouer.mainloop()


while stop:
    menu_principale = Tk()
    fenetre = 0
    jeu = 0
    victoire = 0
    rejouer = 0
    vitesse = 0
    menu_principale.title("Pong")
    menu_principale.geometry("300x250")
        
    button_jouer = Button(menu_principale, text ="   Jouer   ", command = Nombre_de_Victoires)
    button_jouer.pack(padx = 10, pady = 10)
        
    button_quitter = Button(menu_principale, text ="   Partir   ", command = quit)
    button_quitter.pack(padx = 10, pady = 10)
        
    menu_principale.mainloop()
