import tkinter
from tkinter import PhotoImage
import ctypes

ctypes.windll.shcore.SetProcessDpiAwareness(1) 


##Configuration génerale
root = tkinter.Tk()
L = 1250
h = 730
donnée_température = ['pas encore de mesure' for i in range(10)]
donnée_humidité = ['pas encore de mesure' for i in range(10)]

root.geometry('{}x{}'.format(L,h))
root.configure(bg='white')
root.title("Plant-project")
root.resizable(False,False)

icon = tkinter.PhotoImage(file=r"Python project\User Interface\Planet Alert\ressource\icon.png")
root.iconphoto(False,icon)

#UI-Componenants :
btn_actualiser = tkinter.PhotoImage(file=r"Python project\User Interface\Planet Alert\ressource\actualiser.png")
act_btn_actualiser = tkinter.PhotoImage(file=r"Python project\User Interface\Planet Alert\ressource\active-actualiser.png")
afficheur = tkinter.PhotoImage(file=r"Python project\User Interface\Planet Alert\ressource\afficheur.png")
dashboard = tkinter.PhotoImage(file=r"Python project\User Interface\Planet Alert\ressource\dashboard.png")
plant_statue = tkinter.PhotoImage(file=r"Python project\User Interface\Planet Alert\ressource\plant.png")
chart_temp = tkinter.PhotoImage(file=r"Python project\User Interface\Planet Alert\ressource\chart.png")
chart_hum = tkinter.PhotoImage(file=r"Python project\User Interface\Planet Alert\ressource\chart.png")
act_chart = tkinter.PhotoImage(file=r"Python project\User Interface\Planet Alert\ressource\act2_chart.png")
history_temp = tkinter.PhotoImage(file=r"Python project\User Interface\Planet Alert\ressource\history.png")
history_hum = tkinter.PhotoImage(file=r"Python project\User Interface\Planet Alert\ressource\history.png")
act_history = tkinter.PhotoImage(file=r"Python project\User Interface\Planet Alert\ressource\act_history.png")
stars = tkinter.PhotoImage(file=r"Python project\User Interface\Planet Alert\ressource\stars.png")
notification = tkinter.PhotoImage(file=r"Python project\User Interface\Planet Alert\ressource\notification.png")
notification_found = tkinter.PhotoImage(file=r"Python project\User Interface\Planet Alert\ressource\notification_found.png")

#root components :
cnv = tkinter.Canvas(root,width=L,height=h,bg="white",highlightthickness=0)

    ##Stars :
for i in range(1,6):
    cnv.create_oval(968+35*(i-1),88,988+35*(i-1),108,outline='',state='hidden',fill='#ffdd55',tag='star{}'.format(i))

cnv.create_image(41,85,image=dashboard,anchor='nw',tag='dashboard')
cnv.create_image(1076,675,image=btn_actualiser,activeimage=act_btn_actualiser,anchor='nw',tag='btn_actualiser')
cnv.create_image(355,82,image=chart_temp,activeimage = act_chart,anchor='nw',tag='chart_temp')
cnv.create_image(355,390,image=chart_hum,activeimage = act_chart,anchor='nw',tag='chart_hum')
cnv.create_image(310,80,image=history_temp,activeimage = act_history,anchor='nw',tag='history_temp')
cnv.create_image(310,388,image=history_hum,activeimage = act_history,anchor='nw',tag='history_hum')
cnv.create_rectangle(904,205,1194,535,outline='',fill='#dde9af',tag='indicator')
cnv.create_image(904,205,image=plant_statue,anchor='nw',tag='plant_statue')
cnv.create_image(965,88,image=stars,anchor='nw',tag='stars')
cnv.create_image(625,675,image=notification,anchor='nw',tag='notification')

##Positioning the components :
cnv.pack()

##Functions :

def evaluating(stars):
    for i in range(5):
        tag = 'star{}'.format(i+1)
        cnv.itemconfig(tag,state='hidden')
    for i in range(stars):
        tag = 'star{}'.format(i+1)
        cnv.itemconfig(tag,state='normal')
    if stars == 5 :
        cnv.itemconfig('indicator',fill='#44aa00')
    elif stars == 4 :
        cnv.itemconfig('indicator',fill='#5aa02c')
    elif stars == 3 :
        cnv.itemconfig('indicator',fill='#8dd35f')
    elif stars == 2 :
        cnv.itemconfig('indicator',fill='#cdde87')
    elif stars == 1 :
        cnv.itemconfig('indicator',fill='#e9ddaf')

def charts():
    pass     ##dans cette fonction on doit avoir le graph realisé en utilisant matplotlib

def alerting(message):
    pass ##cette fonction permet d'envoyer un message

def receiving(message):
    pass ##cette fonction permet de recevoir un message qui vient du proprietaire de la firme

def measuring():
    pass ##les mesures de l'arduino

def mapping():
    pass ##mapping avec la base des données

def historique(L,p_initial):
    for i in range(5,len(L)+5) :
        x = p_initial[0]
        y = p_initial[1]
        cnv.create_oval(x-10-5,y+20*i-5,x-10+5,y+20*i+5,outline='',fill = 'lightgreen')
        cnv.create_text(x,y+20*i,text=L[i-5],anchor = 'w',justify="right",tag='d{}'.format(i+1))

def données_TH(L,p_initial,typ):
    for i in range(len(L)) :
        x = p_initial[0]
        y = p_initial[1]
        cnv.create_oval(x-10-5,y+20*i-5,x-10+5,y+20*i+5,outline='',fill = 'lightgreen')
        cnv.create_text(x,y+20*i,text=L[i],anchor = 'w',justify="right",font = 'Arial',fill = 'white',tag=typ+'{}'.format(i+1))

def updater(L:list,valeur,typ):
    L.insert(0,valeur)
    L.pop()
    for i in range(len(L)):
        name = typ+'{}'.format(i+1)
        cnv.itemconfig(name,text=L[i])

données_TH(donnée_température,(80,160),'t')
données_TH(donnée_humidité,(80,460),'h')

#binding :
cnv.tag_bind('btn_actualiser','<Button-1>',lambda event: updater(donnée_température,'23C° incroyable','t'))

#the mainloop
root.mainloop()