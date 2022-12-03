import tkinter
import tkinter.messagebox
import customtkinter
from PIL import Image, ImageTk
import os
import numpy as np
customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"
theme= {
    "red":"#E63946",
    "lg_blue":"#A8DADC",
    "dg_blue":"#1D3557",
    "blue":"#457B9D",
    "white":"#F1FAEE",
    "green":"#5CE639",
    "black":"#000000"
}
PATH = os.path.dirname(os.path.realpath(__file__))
class Card:
    def __init__ (self, num, points, name, img_file):
        self.num = num
        self.name = name
        self.img_file = img_file
        self.points = points
    
    def getPoints(self):
        points = self.points
        return points
    
class Coins:
    def __init__ (self, quantity, value, img_file):
        self.quantity = quantity
        self.value = value
        self.img_file = img_file
    
    def get_quantity(self):
        quantity = self.quantity
        return quantity
    
    def put_in(self):
        quantity = self.quantity
        self.quantity = quantity - 1
    
    def add_quantity(self, add_number):
        quantity = self.quantity
        self.quantity = quantity + add_number

Card0 = Card(1,1,"1_corazon","Corazon_A")
Card1 = Card(2,2,"2_corazon","Corazon_2")
Card2 = Card(3,3,"3_corazon","Corazon_3")
Card3 = Card(4,4,"4_corazon","Corazon_4")
Card4 = Card(5,5,"5_corazon","Corazon_5")
Card5 = Card(6,6,"6_corazon","Corazon_6")
Card6 = Card(7,7,"7_corazon","Corazon_7")
Card7 = Card(8,8,"8_corazon","Corazon_8")
Card8 = Card(9,9,"9_corazon","Corazon_9")
Card9 = Card(10,10,"10_corazon","Corazon_J")
Card10 = Card(11,10,"11_corazon","Corazon_Q")
Card11 = Card(12,10,"12_corazon","Corazon_K")

Card12 = Card(13,1,"1_diamante","Diamante_A")
Card13 = Card(14,2,"2_diamante","Diamante_2")
Card14 = Card(15,3,"3_diamante","Diamante_3")
Card15 = Card(16,4,"4_diamante","Diamante_4")
Card16 = Card(17,5,"5_diamante","Diamante_5")
Card17 = Card(18,6,"6_diamante","Diamante_6")
Card18 = Card(19,7,"7_diamante","Diamante_7")
Card19 = Card(20,8,"8_diamante","Diamante_8")
Card20 = Card(21,9,"9_diamante","Diamante_9")
Card21 = Card(22,10,"10_diamante","Diamante_J")
Card22 = Card(23,10,"11_diamante","Diamante_Q")
Card23 = Card(24,10,"12_diamante","Diamante_K")

Card24 = Card(25,1,"1_trebol","Picas_A")
Card25 = Card(26,2,"2_trebol","Picas_2")
Card26 = Card(27,3,"3_trebol","Picas_3")
Card27 = Card(28,4,"4_trebol","Picas_4")
Card28 = Card(29,5,"5_trebol","Picas_5")
Card29 = Card(30,6,"6_trebol","Picas_6")
Card30 = Card(31,7,"7_trebol","Picas_7")
Card31 = Card(32,8,"8_trebol","Picas_8")
Card32 = Card(33,9,"9_trebol","Picas_9")
Card33 = Card(34,10,"10_trebol","Picas_J")
Card34 = Card(35,10,"11_trebol","Picas_Q")
Card35 = Card(36,10,"12_trebol","Picas_K")

Card36 = Card(37,1,"1_picas","Trebol_A")
Card37 = Card(38,2,"2_picas","Trebol_2")
Card38 = Card(39,3,"3_picas","Trebol_3")
Card39 = Card(40,4,"4_picas","Trebol_4")
Card40 = Card(41,5,"5_picas","Trebol_5")
Card41 = Card(42,6,"6_picas","Trebol_6")
Card42 = Card(43,7,"7_picas","Trebol_7")
Card43 = Card(44,8,"8_picas","Trebol_8")
Card44 = Card(45,9,"9_picas","Trebol_9")
Card45 = Card(46,10,"10_picas","Trebol_J")
Card46 = Card(47,10,"11_picas","Trebol_Q")
Card47 = Card(48,10,"12_picas","Trebol_K")

Coin1= Coins(0,1,"Moneda_Bronce")
Coin10= Coins(0,10,"Moneda_Plata")
Coin100= Coins(0,100,"Moneda_Oro")
Coin1000= Coins(0,1000,"Moneda_Diamante")

Cards_array = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,41,42,43,44,45,46,47,48])
Game_array = Cards_array
np.random.shuffle(Game_array)

class App(customtkinter.CTk):
    
    WIDTH = 1920
    HEIGHT = 1080

    def __init__(self):
        super().__init__()

        self.title("BlackJack_Shadow_isles")
        self.geometry("1920x1080")
        self.resizable(False,False)
        self.attributes('-alpha',0.7)
        # ============ create base frames ============

        # configure grid layout (2x2)misc
        holder_card = Image.open(PATH +"/img/cards/BACK.png").resize((130,200))
        coin_holder = Image.open(PATH +"/img/misc/round_holder.png").resize((100,100))
        self.coin_holder = ImageTk.PhotoImage(coin_holder)
        self.holder_card = ImageTk.PhotoImage(holder_card)
        image_board= Image.open(PATH +"/img/board/board_ixtal.jpg").resize((1920,1030))
        self.board_img= ImageTk.PhotoImage(image_board)
        
        coin_1_img = Image.open(PATH +"/img/cards/"+Coin1.img_file+".png").resize((100,100))
        coin_10_img = Image.open(PATH +"/img/cards/"+Coin10.img_file+".png").resize((100,100))
        coin_100_img = Image.open(PATH +"/img/cards/"+Coin100.img_file+".png").resize((100,100))
        coin_1000_img = Image.open(PATH +"/img/cards/"+Coin1000.img_file+".png").resize((100,100))
        self.coin_1_img = ImageTk.PhotoImage(coin_1_img)
        self.coin_10_img = ImageTk.PhotoImage(coin_10_img)
        self.coin_100_img = ImageTk.PhotoImage(coin_100_img)
        self.coin_1000_img = ImageTk.PhotoImage(coin_1000_img)

        self.frame_back = customtkinter.CTkFrame(master=self, width=1920,height=1030, corner_radius=0, fg_color=theme["lg_blue"])
        self.frame_back.grid(row=1, column=0,columnspan=2, sticky="nw")
        
        self.frame_coins = customtkinter.CTkFrame(master=self, width=380, height= 600)
        self.frame_coins.grid(row=1, column=1, sticky="e")
        self.frame_top = customtkinter.CTkFrame(master=self, width=1920,height=50, corner_radius=0, fg_color=theme["red"])
        self.frame_top.grid(row=0, column=0,columnspan=2, sticky="nw")
        self.label_image_board= tkinter.Label(master=self.frame_back, image=self.board_img,borderwidth=0)
        
        image_holder= Image.open(PATH +"/img/misc/index.png").resize((500,800))
        self.image_holder= ImageTk.PhotoImage(image_holder)        
        self.label_coins_back= tkinter.Label(master=self.frame_coins, image=self.image_holder,borderwidth=0)
        
        self.label_card0_player= tkinter.Label(master=self.frame_back, image=self.holder_card,borderwidth=0)
        self.label_card0_player.place(x=600, y=540) 
        self.label_card1_player= tkinter.Label(master=self.frame_back, image=self.holder_card,borderwidth=0)
        self.label_card1_player.place(x=750, y=540) 
        self.label_card2_player= tkinter.Label(master=self.frame_back, image=self.holder_card,borderwidth=0)
        self.label_card2_player.place(x=900, y=540) 
        self.label_card3_player= tkinter.Label(master=self.frame_back, image=self.holder_card,borderwidth=0)
        self.label_card3_player.place(x=1050, y=540) 
        self.label_card4_player= tkinter.Label(master=self.frame_back, image=self.holder_card,borderwidth=0)
        self.label_card4_player.place(x=1200, y=540)
        
        self.label_card0_dealer= tkinter.Label(master=self.frame_back, image=self.holder_card,borderwidth=0)
        self.label_card0_dealer.place(x=600, y=290) 
        self.label_card1_dealer= tkinter.Label(master=self.frame_back, image=self.holder_card,borderwidth=0)
        self.label_card1_dealer.place(x=750, y=290) 
        self.label_card2_dealer= tkinter.Label(master=self.frame_back, image=self.holder_card,borderwidth=0)
        self.label_card2_dealer.place(x=900, y=290) 
        self.label_card3_dealer= tkinter.Label(master=self.frame_back, image=self.holder_card,borderwidth=0)
        self.label_card3_dealer.place(x=1050, y=290) 
        self.label_card4_dealer= tkinter.Label(master=self.frame_back, image=self.holder_card,borderwidth=0)
        self.label_card4_dealer.place(x=1200, y=290)
        
        self.label_coin1= tkinter.Label(master=self.frame_coins, image=self.coin_1_img,borderwidth=0)
        self.label_coin1.place(x=30, y=30)
        self.label_coin10= tkinter.Label(master=self.frame_coins, image=self.coin_10_img,borderwidth=0)
        self.label_coin10.place(x=30, y=170) 
        self.label_coin100= tkinter.Label(master=self.frame_coins, image=self.coin_100_img,borderwidth=0)
        self.label_coin100.place(x=30, y=310) 
        self.label_coin1000= tkinter.Label(master=self.frame_coins, image=self.coin_1000_img,borderwidth=0)
        self.label_coin1000.place(x=30, y=450)
        
        self.button_add_coin1 = customtkinter.CTkButton(master=self.frame_coins, text="+1", height=100, width=100, corner_radius=0)
        self.button_add_coin1.place(x=160, y=30)
        self.button_rest_coin1 = customtkinter.CTkButton(master=self.frame_coins, text="-1", height=100, width=100, corner_radius=0)
        self.button_rest_coin1.place(x=260, y=30)
        
        self.button_add_coin10 = customtkinter.CTkButton(master=self.frame_coins, text="+1", height=100, width=100, corner_radius=0)
        self.button_add_coin10.place(x=160, y=170)
        self.button_rest_coin10 = customtkinter.CTkButton(master=self.frame_coins, text="-1", height=100, width=100, corner_radius=0)
        self.button_rest_coin10.place(x=260, y=170)
        
        self.button_add_coin100 = customtkinter.CTkButton(master=self.frame_coins, text="+1", height=100, width=100, corner_radius=0)
        self.button_add_coin100.place(x=160, y=310)
        self.button_rest_coin100 = customtkinter.CTkButton(master=self.frame_coins, text="-1", height=100, width=100, corner_radius=0)
        self.button_rest_coin100.place(x=260, y=310)  
        
        self.button_add_coin1000 = customtkinter.CTkButton(master=self.frame_coins, text="+1", height=100, width=100, corner_radius=0)
        self.button_add_coin1000.place(x=160, y=450)
        self.button_rest_coin1000 = customtkinter.CTkButton(master=self.frame_coins, text="-1", height=100, width=100, corner_radius=0)
        self.button_rest_coin1000.place(x=260, y=450)
               
        self.label_coins_back.place(x=0,y=0)
        self.label_image_board.place(x=0, y=0)
        
        self.label_player_points= customtkinter.CTkLabel(master=self.frame_back, text="00",text_font=("Arial",27), width=30)
        self.label_player_points.place(x=345,y=383)
        
        self.label_apuesta= customtkinter.CTkLabel(master=self.frame_back, text="Apuesta: $000000",text_font=("Arial",27), width=30)
        self.label_apuesta.place(x=800,y=850)
        
        self.label_dealer_points= customtkinter.CTkLabel(master=self.frame_back, text="00",text_font=("Arial",27), width=30)
        self.label_dealer_points.place(x=345,y=603)
        
        self.anadir_carta = customtkinter.CTkButton(master=self.frame_back, text="Otra carta?", width=200, height=80, corner_radius=0, text_font=("Arial",20))
        self.termiar_juego = customtkinter.CTkButton(master=self.frame_back, text="Terminar mano", width=200, height=80, corner_radius=0, text_font=("Arial",18))
        self.figar_apuesta = customtkinter.CTkButton(master=self.frame_back, text="Fijar apuesta", width=200, height=80, corner_radius=0, text_font=("Arial",18))
        self.figar_apuesta.place(x=1650, y=810)
        self.anadir_carta.place(x=25, y=550)
        self.termiar_juego.place(x=25, y=400)
    
if __name__ == "__main__":
    app = App()
    app.mainloop()