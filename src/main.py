import tkinter
import tkinter.messagebox
import customtkinter
from PIL import Image, ImageTk
import os
import numpy as np
customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"
theme= {
    "lg_blue":"#65f7e0",
    "dr_blue":"#0A5B6D",
    "blue":"#00A99D",
    "lg_gold":"#D9BE81",
    "dr_gold":"#7A6930",
    "gold":"#C6A040",
    "black":"#000000",
    "white":"#FFFFFF"
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
global idex_card   
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
hand_wins =0
hand_loses = 0 
index_card = 0
player_points = 0
dealer_points = 0
last_draw_card = 0
bet = 0
money = 10000
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
        holder_card = Image.open(PATH +"/img/cards/BACK.png").resize((160,250))
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
        self.frame_top = customtkinter.CTkFrame(master=self, width=1920,height=50, corner_radius=0, fg_color=theme["blue"])
        self.frame_top.grid(row=0, column=0,columnspan=2, sticky="nw")
        self.label_image_board= tkinter.Label(master=self.frame_back, image=self.board_img,borderwidth=0)
        
        image_holder= Image.open(PATH +"/img/cards/Moneda_Rectangulo.png").resize((500,800))
        self.image_holder= ImageTk.PhotoImage(image_holder)        
        self.label_coins_back= tkinter.Label(master=self.frame_coins, image=self.image_holder,borderwidth=0)
        
        self.label_card0_player= tkinter.Label(master=self.frame_back, image=self.holder_card,borderwidth=0)
        self.label_card0_player.place(x=500, y=530) 
        self.label_card1_player= tkinter.Label(master=self.frame_back, image=self.holder_card,borderwidth=0)
        self.label_card1_player.place(x=700, y=530) 
        self.label_card2_player= tkinter.Label(master=self.frame_back, image=self.holder_card,borderwidth=0)
        self.label_card2_player.place(x=900, y=530) 
        self.label_card3_player= tkinter.Label(master=self.frame_back, image=self.holder_card,borderwidth=0)
        self.label_card3_player.place(x=1100, y=530) 
        self.label_card4_player= tkinter.Label(master=self.frame_back, image=self.holder_card,borderwidth=0)
        self.label_card4_player.place(x=1300, y=530)
        
        self.label_card0_dealer= tkinter.Label(master=self.frame_back, image=self.holder_card,borderwidth=0)
        self.label_card0_dealer.place(x=500, y=250) 
        self.label_card1_dealer= tkinter.Label(master=self.frame_back, image=self.holder_card,borderwidth=0)
        self.label_card1_dealer.place(x=700, y=250) 
        self.label_card2_dealer= tkinter.Label(master=self.frame_back, image=self.holder_card,borderwidth=0)
        self.label_card2_dealer.place(x=900, y=250) 
        self.label_card3_dealer= tkinter.Label(master=self.frame_back, image=self.holder_card,borderwidth=0)
        self.label_card3_dealer.place(x=1100, y=250) 
        self.label_card4_dealer= tkinter.Label(master=self.frame_back, image=self.holder_card,borderwidth=0)
        self.label_card4_dealer.place(x=1300, y=250)
        
        self.label_coin1= tkinter.Label(master=self.frame_coins, image=self.coin_1_img,borderwidth=0)
        self.label_coin1.place(x=30, y=30)
        self.label_coin10= tkinter.Label(master=self.frame_coins, image=self.coin_10_img,borderwidth=0)
        self.label_coin10.place(x=30, y=170) 
        self.label_coin100= tkinter.Label(master=self.frame_coins, image=self.coin_100_img,borderwidth=0)
        self.label_coin100.place(x=30, y=310) 
        self.label_coin1000= tkinter.Label(master=self.frame_coins, image=self.coin_1000_img,borderwidth=0)
        self.label_coin1000.place(x=30, y=450)
        
        self.button_add_coin1 = customtkinter.CTkButton(master=self.frame_coins, text="+1", height=100, width=100, corner_radius=0,background=theme["dr_gold"], fg_color=theme["dr_gold"], text_color=theme["black"], hover_color=theme["lg_gold"], command= lambda:add_bet(1))
        self.button_add_coin1.place(x=160, y=30)
        self.button_rest_coin1 = customtkinter.CTkButton(master=self.frame_coins, text="-1", height=100, width=100, corner_radius=0,background=theme["dr_blue"], fg_color= theme["dr_blue"], text_color=theme["white"], hover_color=theme["blue"], command= lambda:res_bet(1))
        self.button_rest_coin1.place(x=260, y=30)
        
        self.button_add_coin10 = customtkinter.CTkButton(master=self.frame_coins, text="+10", height=100, width=100, corner_radius=0,background=theme["dr_gold"], fg_color=theme["dr_gold"], text_color=theme["black"], hover_color=theme["lg_gold"], command= lambda:add_bet(10))
        self.button_add_coin10.place(x=160, y=170)
        self.button_rest_coin10 = customtkinter.CTkButton(master=self.frame_coins, text="-10", height=100, width=100, corner_radius=0,background=theme["dr_blue"], fg_color= theme["dr_blue"], text_color=theme["white"], hover_color=theme["blue"], command= lambda:res_bet(10))
        self.button_rest_coin10.place(x=260, y=170)
        
        self.button_add_coin100 = customtkinter.CTkButton(master=self.frame_coins, text="+100", height=100, width=100, corner_radius=0,background=theme["dr_gold"], fg_color=theme["dr_gold"], text_color=theme["black"], hover_color=theme["lg_gold"], command= lambda:add_bet(100))
        self.button_add_coin100.place(x=160, y=310)
        self.button_rest_coin100 = customtkinter.CTkButton(master=self.frame_coins, text="-100", height=100, width=100, corner_radius=0, background=theme["dr_blue"], fg_color= theme["dr_blue"], text_color=theme["white"], hover_color=theme["blue"], command= lambda:res_bet(100))
        self.button_rest_coin100.place(x=260, y=310)  
        
        self.button_add_coin1000 = customtkinter.CTkButton(master=self.frame_coins, text="+1000", height=100, width=100, corner_radius=0,background=theme["dr_gold"], fg_color=theme["dr_gold"], text_color=theme["black"], hover_color=theme["lg_gold"], command= lambda:add_bet(1000))
        self.button_add_coin1000.place(x=160, y=450)
        self.button_rest_coin1000 = customtkinter.CTkButton(master=self.frame_coins, text="-1000", height=100, width=100, corner_radius=0, background=theme["dr_blue"], fg_color= theme["dr_blue"], text_color=theme["white"], hover_color=theme["blue"], command= lambda:res_bet(1000))
        self.button_rest_coin1000.place(x=260, y=450)
               
        self.label_coins_back.place(x=0,y=0)
        self.label_image_board.place(x=0, y=0)
        
        self.label_player_points= customtkinter.CTkLabel(master=self.frame_back, text="00",text_font=("Arial",27), width=30)
        self.label_player_points.place(x=345,y=603)
        
        self.label_apuesta= customtkinter.CTkLabel(master=self.frame_back, text="Apuesta: $",text_font=("Arial",27), width=30)
        self.label_apuesta.place(x=800,y=850)
        
        self.label_dealer_points= customtkinter.CTkLabel(master=self.frame_back, text="00",text_font=("Arial",27), width=30)
        self.label_dealer_points.place(x=345,y=383)
        
        self.anadir_carta = customtkinter.CTkButton(master=self.frame_back, text="Otra carta?", width=200, height=80, corner_radius=0, text_font=("Arial",20), background=theme["dr_gold"], fg_color=theme["dr_gold"], text_color=theme["black"], hover_color=theme["lg_gold"], command=lambda:draw_card(self), state="disabled")
        
        self.end_game = customtkinter.CTkButton(master=self.frame_back, text="Terminar mano", width=200, height=80, corner_radius=0, text_font=("Arial",18), background=theme["dr_blue"], fg_color= theme["dr_blue"], text_color=theme["white"], hover_color=theme["blue"], state="disabled", command = lambda:end_game())
        
        self.new_hand = customtkinter.CTkButton(master=self.frame_back, text="Nueva mano", width=200, height=80, corner_radius=0, text_font=("Arial",18), background=theme["dr_blue"], fg_color= theme["dr_blue"], text_color=theme["white"], hover_color=theme["blue"], state="disabled", command = lambda:new_game())
        self.new_hand.place(x=1650, y=950)
        
        self.figar_apuesta = customtkinter.CTkButton(master=self.frame_back, text="Fijar apuesta", width=200, height=80, corner_radius=0, text_font=("Arial",18), background=theme["dr_gold"], fg_color=theme["dr_gold"], text_color=theme["black"], hover_color=theme["lg_gold"],command =lambda:set_bet())
        
        self.label_money= customtkinter.CTkLabel(master=self.frame_back, text="$10000",text_font=("Arial",27), width=200, height=80, corner_radius =0, fg_color= theme["dr_gold"], text_color= theme["black"])
        self.label_money.place(x=1650,y=150)
        
        self.label_wins= customtkinter.CTkLabel(master=self.frame_back, text="Wins: 0",text_font=("Arial",27), width=200, height=80, corner_radius =0, fg_color= theme["dr_gold"], text_color= theme["black"])
        
        self.label_loses= customtkinter.CTkLabel(master=self.frame_back, text="Loses: 0",text_font=("Arial",27), width=200, height=80, corner_radius =0, fg_color= theme["dr_gold"], text_color= theme["black"])
        
        image_close = Image.open(PATH+"/img/misc/Close.png").resize((50,50))
        self.image_Close = ImageTk.PhotoImage(image_close)
        
        self.close_button =  customtkinter.CTkButton(image= self.image_Close, border_width=0, master=self.frame_top, text="", width=50, height=50, corner_radius=0, compound="left", fg_color=theme["blue"], bg_color=theme["dr_blue"], hover_color=theme["blue"], command=lambda:on_closing(self))
        self.close_button.place(x=0, y=0)
        self.label_wins.place(x=25, y=25)
        self.label_loses.place(x=225, y=25)
        
        self.figar_apuesta.place(x=1650, y=810)
        self.anadir_carta.place(x=25, y=550)
        self.end_game.place(x=25, y=400)
        
        def play(self):
            global index_card
            global player_points
            global dealer_points
            global last_draw_card
            if(last_draw_card > 48):
                last_draw_card = 0
                np.random.shuffle(Game_array)
            index_card = 1
            dealer_card1 = Game_array[last_draw_card]
            last_draw_card += 1
            dealer_card2 = Game_array[last_draw_card]
            last_draw_card += 1
            player_card1 = Game_array[last_draw_card]
            last_draw_card += 1
            player_card2 = Game_array[last_draw_card]
            # ========================= IF for image cards & Points  card 0 ============================================
            if (player_card1 == 1):
                card0_player = Image.open(PATH +"/img/cards/"+Card0.img_file+".png").resize((160,250))
                self.card0_player = ImageTk.PhotoImage(card0_player)
                self.label_card0_player= tkinter.Label(master=self.frame_back, image=self.card0_player,borderwidth=0)
                self.label_card0_player.place(x=500, y=530)
                player_points += Card0.points
            if (player_card1 == 2):
                card0_player = Image.open(PATH +"/img/cards/"+Card1.img_file+".png").resize((160,250))
                self.card0_player = ImageTk.PhotoImage(card0_player)
                self.label_card0_player= tkinter.Label(master=self.frame_back, image=self.card0_player,borderwidth=0)
                self.label_card0_player.place(x=500, y=530)
                player_points += Card1.points
            if (player_card1 == 3):
                card0_player = Image.open(PATH +"/img/cards/"+Card2.img_file+".png").resize((160,250))
                self.card0_player = ImageTk.PhotoImage(card0_player)
                self.label_card0_player= tkinter.Label(master=self.frame_back, image=self.card0_player,borderwidth=0)
                self.label_card0_player.place(x=500, y=530)
                player_points += Card2.points
            if (player_card1 == 4):
                card0_player = Image.open(PATH +"/img/cards/"+Card3.img_file+".png").resize((160,250))
                self.card0_player = ImageTk.PhotoImage(card0_player)
                self.label_card0_player= tkinter.Label(master=self.frame_back, image=self.card0_player,borderwidth=0)
                self.label_card0_player.place(x=500, y=530)
                player_points += Card3.points
            if (player_card1 == 5):
                card0_player = Image.open(PATH +"/img/cards/"+Card4.img_file+".png").resize((160,250))
                self.card0_player = ImageTk.PhotoImage(card0_player)
                self.label_card0_player= tkinter.Label(master=self.frame_back, image=self.card0_player,borderwidth=0)
                self.label_card0_player.place(x=500, y=530)
                player_points += Card4.points
            if (player_card1 == 6):
                card0_player = Image.open(PATH +"/img/cards/"+Card5.img_file+".png").resize((160,250))
                self.card0_player = ImageTk.PhotoImage(card0_player)
                self.label_card0_player= tkinter.Label(master=self.frame_back, image=self.card0_player,borderwidth=0)
                self.label_card0_player.place(x=500, y=530)
                player_points += Card5.points
            if (player_card1 == 7):
                card0_player = Image.open(PATH +"/img/cards/"+Card6.img_file+".png").resize((160,250))
                self.card0_player = ImageTk.PhotoImage(card0_player)
                self.label_card0_player= tkinter.Label(master=self.frame_back, image=self.card0_player,borderwidth=0)
                self.label_card0_player.place(x=500, y=530)
                player_points += Card6.points
            if (player_card1 == 8):
                card0_player = Image.open(PATH +"/img/cards/"+Card7.img_file+".png").resize((160,250))
                self.card0_player = ImageTk.PhotoImage(card0_player)
                self.label_card0_player= tkinter.Label(master=self.frame_back, image=self.card0_player,borderwidth=0)
                self.label_card0_player.place(x=500, y=530)
                player_points += Card7.points
            if (player_card1 == 9):
                card0_player = Image.open(PATH +"/img/cards/"+Card8.img_file+".png").resize((160,250))
                self.card0_player = ImageTk.PhotoImage(card0_player)
                self.label_card0_player= tkinter.Label(master=self.frame_back, image=self.card0_player,borderwidth=0)
                self.label_card0_player.place(x=500, y=530)
                player_points += Card8.points
            if (player_card1 == 10):
                card0_player = Image.open(PATH +"/img/cards/"+Card9.img_file+".png").resize((160,250))
                self.card0_player = ImageTk.PhotoImage(card0_player)
                self.label_card0_player= tkinter.Label(master=self.frame_back, image=self.card0_player,borderwidth=0)
                self.label_card0_player.place(x=500, y=530)
                player_points += Card9.points
            if (player_card1 == 11):
                card0_player = Image.open(PATH +"/img/cards/"+Card10.img_file+".png").resize((160,250))
                self.card0_player = ImageTk.PhotoImage(card0_player)
                self.label_card0_player= tkinter.Label(master=self.frame_back, image=self.card0_player,borderwidth=0)
                self.label_card0_player.place(x=500, y=530)
                player_points += Card10.points
            if (player_card1 == 12):
                card0_player = Image.open(PATH +"/img/cards/"+Card11.img_file+".png").resize((160,250))
                self.card0_player = ImageTk.PhotoImage(card0_player)
                self.label_card0_player= tkinter.Label(master=self.frame_back, image=self.card0_player,borderwidth=0)
                self.label_card0_player.place(x=500, y=530)
                player_points += Card11.points
            if (player_card1 == 13):
                card0_player = Image.open(PATH +"/img/cards/"+Card12.img_file+".png").resize((160,250))
                self.card0_player = ImageTk.PhotoImage(card0_player)
                self.label_card0_player= tkinter.Label(master=self.frame_back, image=self.card0_player,borderwidth=0)
                self.label_card0_player.place(x=500, y=530)
                player_points += Card12.points
            if (player_card1 == 14):
                card0_player = Image.open(PATH +"/img/cards/"+Card13.img_file+".png").resize((160,250))
                self.card0_player = ImageTk.PhotoImage(card0_player)
                self.label_card0_player= tkinter.Label(master=self.frame_back, image=self.card0_player,borderwidth=0)
                self.label_card0_player.place(x=500, y=530)
                player_points += Card13.points
            if (player_card1 == 15):
                card0_player = Image.open(PATH +"/img/cards/"+Card14.img_file+".png").resize((160,250))
                self.card0_player = ImageTk.PhotoImage(card0_player)
                self.label_card0_player= tkinter.Label(master=self.frame_back, image=self.card0_player,borderwidth=0)
                self.label_card0_player.place(x=500, y=530)
                player_points += Card14.points
            if (player_card1 == 16):
                card0_player = Image.open(PATH +"/img/cards/"+Card15.img_file+".png").resize((160,250))
                self.card0_player = ImageTk.PhotoImage(card0_player)
                self.label_card0_player= tkinter.Label(master=self.frame_back, image=self.card0_player,borderwidth=0)
                self.label_card0_player.place(x=500, y=530)
                player_points += Card15.points
            if (player_card1 == 17):
                card0_player = Image.open(PATH +"/img/cards/"+Card16.img_file+".png").resize((160,250))
                self.card0_player = ImageTk.PhotoImage(card0_player)
                self.label_card0_player= tkinter.Label(master=self.frame_back, image=self.card0_player,borderwidth=0)
                self.label_card0_player.place(x=500, y=530)
                player_points += Card16.points
            if (player_card1 == 18):
                card0_player = Image.open(PATH +"/img/cards/"+Card17.img_file+".png").resize((160,250))
                self.card0_player = ImageTk.PhotoImage(card0_player)
                self.label_card0_player= tkinter.Label(master=self.frame_back, image=self.card0_player,borderwidth=0)
                self.label_card0_player.place(x=500, y=530)
                player_points += Card17.points
            if (player_card1 == 19):
                card0_player = Image.open(PATH +"/img/cards/"+Card18.img_file+".png").resize((160,250))
                self.card0_player = ImageTk.PhotoImage(card0_player)
                self.label_card0_player= tkinter.Label(master=self.frame_back, image=self.card0_player,borderwidth=0)
                self.label_card0_player.place(x=500, y=530)
                player_points += Card18.points
            if (player_card1 == 20):
                card0_player = Image.open(PATH +"/img/cards/"+Card19.img_file+".png").resize((160,250))
                self.card0_player = ImageTk.PhotoImage(card0_player)
                self.label_card0_player= tkinter.Label(master=self.frame_back, image=self.card0_player,borderwidth=0)
                self.label_card0_player.place(x=500, y=530)
                player_points += Card19.points
            if (player_card1 == 21):
                card0_player = Image.open(PATH +"/img/cards/"+Card20.img_file+".png").resize((160,250))
                self.card0_player = ImageTk.PhotoImage(card0_player)
                self.label_card0_player= tkinter.Label(master=self.frame_back, image=self.card0_player,borderwidth=0)
                self.label_card0_player.place(x=500, y=530)
                player_points += Card20.points
            if (player_card1 == 22):
                card0_player = Image.open(PATH +"/img/cards/"+Card21.img_file+".png").resize((160,250))
                self.card0_player = ImageTk.PhotoImage(card0_player)
                self.label_card0_player= tkinter.Label(master=self.frame_back, image=self.card0_player,borderwidth=0)
                self.label_card0_player.place(x=500, y=530)
                player_points += Card21.points
            if (player_card1 == 23):
                card0_player = Image.open(PATH +"/img/cards/"+Card22.img_file+".png").resize((160,250))
                self.card0_player = ImageTk.PhotoImage(card0_player)
                self.label_card0_player= tkinter.Label(master=self.frame_back, image=self.card0_player,borderwidth=0)
                self.label_card0_player.place(x=500, y=530)
                player_points += Card22.points
            if (player_card1 == 24):
                card0_player = Image.open(PATH +"/img/cards/"+Card23.img_file+".png").resize((160,250))
                self.card0_player = ImageTk.PhotoImage(card0_player)
                self.label_card0_player= tkinter.Label(master=self.frame_back, image=self.card0_player,borderwidth=0)
                self.label_card0_player.place(x=500, y=530)
                player_points += Card23.points
            if (player_card1 == 25):
                card0_player = Image.open(PATH +"/img/cards/"+Card24.img_file+".png").resize((160,250))
                self.card0_player = ImageTk.PhotoImage(card0_player)
                self.label_card0_player= tkinter.Label(master=self.frame_back, image=self.card0_player,borderwidth=0)
                self.label_card0_player.place(x=500, y=530)
                player_points += Card24.points
            if (player_card1 == 26):
                card0_player = Image.open(PATH +"/img/cards/"+Card25.img_file+".png").resize((160,250))
                self.card0_player = ImageTk.PhotoImage(card0_player)
                self.label_card0_player= tkinter.Label(master=self.frame_back, image=self.card0_player,borderwidth=0)
                self.label_card0_player.place(x=500, y=530)
                player_points += Card25.points
            if (player_card1 == 27):
                card0_player = Image.open(PATH +"/img/cards/"+Card26.img_file+".png").resize((160,250))
                self.card0_player = ImageTk.PhotoImage(card0_player)
                self.label_card0_player= tkinter.Label(master=self.frame_back, image=self.card0_player,borderwidth=0)
                self.label_card0_player.place(x=500, y=530)
                player_points += Card26.points
            if (player_card1 == 28):
                card0_player = Image.open(PATH +"/img/cards/"+Card27.img_file+".png").resize((160,250))
                self.card0_player = ImageTk.PhotoImage(card0_player)
                self.label_card0_player= tkinter.Label(master=self.frame_back, image=self.card0_player,borderwidth=0)
                self.label_card0_player.place(x=500, y=530)
                player_points += Card27.points
            if (player_card1 == 29):
                card0_player = Image.open(PATH +"/img/cards/"+Card28.img_file+".png").resize((160,250))
                self.card0_player = ImageTk.PhotoImage(card0_player)
                self.label_card0_player= tkinter.Label(master=self.frame_back, image=self.card0_player,borderwidth=0)
                self.label_card0_player.place(x=500, y=530)
                player_points += Card28.points
            if (player_card1 == 30):
                card0_player = Image.open(PATH +"/img/cards/"+Card29.img_file+".png").resize((160,250))
                self.card0_player = ImageTk.PhotoImage(card0_player)
                self.label_card0_player= tkinter.Label(master=self.frame_back, image=self.card0_player,borderwidth=0)
                self.label_card0_player.place(x=500, y=530)
                player_points += Card29.points
            if (player_card1 == 31):
                card0_player = Image.open(PATH +"/img/cards/"+Card30.img_file+".png").resize((160,250))
                self.card0_player = ImageTk.PhotoImage(card0_player)
                self.label_card0_player= tkinter.Label(master=self.frame_back, image=self.card0_player,borderwidth=0)
                self.label_card0_player.place(x=500, y=530)
                player_points += Card30.points
            if (player_card1 == 32):
                card0_player = Image.open(PATH +"/img/cards/"+Card31.img_file+".png").resize((160,250))
                self.card0_player = ImageTk.PhotoImage(card0_player)
                self.label_card0_player= tkinter.Label(master=self.frame_back, image=self.card0_player,borderwidth=0)
                self.label_card0_player.place(x=500, y=530)
                player_points += Card31.points
            if (player_card1 == 33):
                card0_player = Image.open(PATH +"/img/cards/"+Card32.img_file+".png").resize((160,250))
                self.card0_player = ImageTk.PhotoImage(card0_player)
                self.label_card0_player= tkinter.Label(master=self.frame_back, image=self.card0_player,borderwidth=0)
                self.label_card0_player.place(x=500, y=530)
                player_points += Card32.points
            if (player_card1 == 34):
                card0_player = Image.open(PATH +"/img/cards/"+Card33.img_file+".png").resize((160,250))
                self.card0_player = ImageTk.PhotoImage(card0_player)
                self.label_card0_player= tkinter.Label(master=self.frame_back, image=self.card0_player,borderwidth=0)
                self.label_card0_player.place(x=500, y=530)
                player_points += Card33.points
            if (player_card1 == 35):
                card0_player = Image.open(PATH +"/img/cards/"+Card34.img_file+".png").resize((160,250))
                self.card0_player = ImageTk.PhotoImage(card0_player)
                self.label_card0_player= tkinter.Label(master=self.frame_back, image=self.card0_player,borderwidth=0)
                self.label_card0_player.place(x=500, y=530)
                player_points += Card34.points
            if (player_card1 == 36):
                card0_player = Image.open(PATH +"/img/cards/"+Card35.img_file+".png").resize((160,250))
                self.card0_player = ImageTk.PhotoImage(card0_player)
                self.label_card0_player= tkinter.Label(master=self.frame_back, image=self.card0_player,borderwidth=0)
                self.label_card0_player.place(x=500, y=530)
                player_points += Card35.points
            if (player_card1 == 37):
                card0_player = Image.open(PATH +"/img/cards/"+Card36.img_file+".png").resize((160,250))
                self.card0_player = ImageTk.PhotoImage(card0_player)
                self.label_card0_player= tkinter.Label(master=self.frame_back, image=self.card0_player,borderwidth=0)
                self.label_card0_player.place(x=500, y=530)
                player_points += Card36.points
            if (player_card1 == 38):
                card0_player = Image.open(PATH +"/img/cards/"+Card37.img_file+".png").resize((160,250))
                self.card0_player = ImageTk.PhotoImage(card0_player)
                self.label_card0_player= tkinter.Label(master=self.frame_back, image=self.card0_player,borderwidth=0)
                self.label_card0_player.place(x=500, y=530)
                player_points += Card37.points
            if (player_card1 == 39):
                card0_player = Image.open(PATH +"/img/cards/"+Card38.img_file+".png").resize((160,250))
                self.card0_player = ImageTk.PhotoImage(card0_player)
                self.label_card0_player= tkinter.Label(master=self.frame_back, image=self.card0_player,borderwidth=0)
                self.label_card0_player.place(x=500, y=530)
                player_points += Card38.points
            if (player_card1 == 40):
                card0_player = Image.open(PATH +"/img/cards/"+Card39.img_file+".png").resize((160,250))
                self.card0_player = ImageTk.PhotoImage(card0_player)
                self.label_card0_player= tkinter.Label(master=self.frame_back, image=self.card0_player,borderwidth=0)
                self.label_card0_player.place(x=500, y=530)
                player_points += Card39.points
            if (player_card1 == 41):
                card0_player = Image.open(PATH +"/img/cards/"+Card40.img_file+".png").resize((160,250))
                self.card0_player = ImageTk.PhotoImage(card0_player)
                self.label_card0_player= tkinter.Label(master=self.frame_back, image=self.card0_player,borderwidth=0)
                self.label_card0_player.place(x=500, y=530)
                player_points += Card40.points
            if (player_card1 == 42):
                card0_player = Image.open(PATH +"/img/cards/"+Card41.img_file+".png").resize((160,250))
                self.card0_player = ImageTk.PhotoImage(card0_player)
                self.label_card0_player= tkinter.Label(master=self.frame_back, image=self.card0_player,borderwidth=0)
                self.label_card0_player.place(x=500, y=530)
                player_points += Card41.points
            if (player_card1 == 43):
                card0_player = Image.open(PATH +"/img/cards/"+Card42.img_file+".png").resize((160,250))
                self.card0_player = ImageTk.PhotoImage(card0_player)
                self.label_card0_player= tkinter.Label(master=self.frame_back, image=self.card0_player,borderwidth=0)
                self.label_card0_player.place(x=500, y=530)
                player_points += Card42.points
            if (player_card1 == 44):
                card0_player = Image.open(PATH +"/img/cards/"+Card43.img_file+".png").resize((160,250))
                self.card0_player = ImageTk.PhotoImage(card0_player)
                self.label_card0_player= tkinter.Label(master=self.frame_back, image=self.card0_player,borderwidth=0)
                self.label_card0_player.place(x=500, y=530)
                player_points += Card43.points
            if (player_card1 == 45):
                card0_player = Image.open(PATH +"/img/cards/"+Card44.img_file+".png").resize((160,250))
                self.card0_player = ImageTk.PhotoImage(card0_player)
                self.label_card0_player= tkinter.Label(master=self.frame_back, image=self.card0_player,borderwidth=0)
                self.label_card0_player.place(x=500, y=530)
                player_points += Card44.points
            if (player_card1 == 46):
                card0_player = Image.open(PATH +"/img/cards/"+Card45.img_file+".png").resize((160,250))
                self.card0_player = ImageTk.PhotoImage(card0_player)
                self.label_card0_player= tkinter.Label(master=self.frame_back, image=self.card0_player,borderwidth=0)
                self.label_card0_player.place(x=500, y=530)
                player_points += Card45.points
            if (player_card1 == 47):
                card0_player = Image.open(PATH +"/img/cards/"+Card46.img_file+".png").resize((160,250))
                self.card0_player = ImageTk.PhotoImage(card0_player)
                self.label_card0_player= tkinter.Label(master=self.frame_back, image=self.card0_player,borderwidth=0)
                self.label_card0_player.place(x=500, y=530)
                player_points += Card46.points
            if (player_card1 == 48):
                card0_player = Image.open(PATH +"/img/cards/"+Card47.img_file+".png").resize((160,250))
                self.card0_player = ImageTk.PhotoImage(card0_player)
                self.label_card0_player= tkinter.Label(master=self.frame_back, image=self.card0_player,borderwidth=0)
                self.label_card0_player.place(x=500, y=530)
                player_points += Card47.points
                
            #========== End card 1 player
            
            if (player_card2 == 1):
                card1_player = Image.open(PATH +"/img/cards/"+Card0.img_file+".png").resize((160,250))
                self.card1_player = ImageTk.PhotoImage(card1_player)
                self.label_card1_player= tkinter.Label(master=self.frame_back, image=self.card1_player,borderwidth=0)
                self.label_card1_player.place(x=700, y=530)
                player_points += Card0.points
            if (player_card2 == 2):
                card1_player = Image.open(PATH +"/img/cards/"+Card1.img_file+".png").resize((160,250))
                self.card1_player = ImageTk.PhotoImage(card1_player)
                self.label_card1_player= tkinter.Label(master=self.frame_back, image=self.card1_player,borderwidth=0)
                self.label_card1_player.place(x=700, y=530)
                player_points += Card1.points
            if (player_card2 == 3):
                card1_player = Image.open(PATH +"/img/cards/"+Card2.img_file+".png").resize((160,250))
                self.card1_player = ImageTk.PhotoImage(card1_player)
                self.label_card1_player= tkinter.Label(master=self.frame_back, image=self.card1_player,borderwidth=0)
                self.label_card1_player.place(x=700, y=530)
                player_points += Card2.points
            if (player_card2 == 4):
                card1_player = Image.open(PATH +"/img/cards/"+Card3.img_file+".png").resize((160,250))
                self.card1_player = ImageTk.PhotoImage(card1_player)
                self.label_card1_player= tkinter.Label(master=self.frame_back, image=self.card1_player,borderwidth=0)
                self.label_card1_player.place(x=700, y=530)
                player_points += Card3.points
            if (player_card2 == 5):
                card1_player = Image.open(PATH +"/img/cards/"+Card4.img_file+".png").resize((160,250))
                self.card1_player = ImageTk.PhotoImage(card1_player)
                self.label_card1_player= tkinter.Label(master=self.frame_back, image=self.card1_player,borderwidth=0)
                self.label_card1_player.place(x=700, y=530)
                player_points += Card4.points
            if (player_card2 == 6):
                card1_player = Image.open(PATH +"/img/cards/"+Card5.img_file+".png").resize((160,250))
                self.card1_player = ImageTk.PhotoImage(card1_player)
                self.label_card1_player= tkinter.Label(master=self.frame_back, image=self.card1_player,borderwidth=0)
                self.label_card1_player.place(x=700, y=530)
                player_points += Card5.points
            if (player_card2 == 7):
                card1_player = Image.open(PATH +"/img/cards/"+Card6.img_file+".png").resize((160,250))
                self.card1_player = ImageTk.PhotoImage(card1_player)
                self.label_card1_player= tkinter.Label(master=self.frame_back, image=self.card1_player,borderwidth=0)
                self.label_card1_player.place(x=700, y=530)
                player_points += Card6.points
            if (player_card2 == 8):
                card1_player = Image.open(PATH +"/img/cards/"+Card7.img_file+".png").resize((160,250))
                self.card1_player = ImageTk.PhotoImage(card1_player)
                self.label_card1_player= tkinter.Label(master=self.frame_back, image=self.card1_player,borderwidth=0)
                self.label_card1_player.place(x=700, y=530)
                player_points += Card7.points
            if (player_card2 == 9):
                card1_player = Image.open(PATH +"/img/cards/"+Card8.img_file+".png").resize((160,250))
                self.card1_player = ImageTk.PhotoImage(card1_player)
                self.label_card1_player= tkinter.Label(master=self.frame_back, image=self.card1_player,borderwidth=0)
                self.label_card1_player.place(x=700, y=530)
                player_points += Card8.points
            if (player_card2 == 10):
                card1_player = Image.open(PATH +"/img/cards/"+Card9.img_file+".png").resize((160,250))
                self.card1_player = ImageTk.PhotoImage(card1_player)
                self.label_card1_player= tkinter.Label(master=self.frame_back, image=self.card1_player,borderwidth=0)
                self.label_card1_player.place(x=700, y=530)
                player_points += Card9.points
            if (player_card2 == 11):
                card1_player = Image.open(PATH +"/img/cards/"+Card10.img_file+".png").resize((160,250))
                self.card1_player = ImageTk.PhotoImage(card1_player)
                self.label_card1_player= tkinter.Label(master=self.frame_back, image=self.card1_player,borderwidth=0)
                self.label_card1_player.place(x=700, y=530)
                player_points += Card10.points
            if (player_card2 == 12):
                card1_player = Image.open(PATH +"/img/cards/"+Card11.img_file+".png").resize((160,250))
                self.card1_player = ImageTk.PhotoImage(card1_player)
                self.label_card1_player= tkinter.Label(master=self.frame_back, image=self.card1_player,borderwidth=0)
                self.label_card1_player.place(x=700, y=530)
                player_points += Card11.points
            if (player_card2 == 13):
                card1_player = Image.open(PATH +"/img/cards/"+Card12.img_file+".png").resize((160,250))
                self.card1_player = ImageTk.PhotoImage(card1_player)
                self.label_card1_player= tkinter.Label(master=self.frame_back, image=self.card1_player,borderwidth=0)
                self.label_card1_player.place(x=700, y=530)
                player_points += Card12.points
            if (player_card2 == 14):
                card1_player = Image.open(PATH +"/img/cards/"+Card13.img_file+".png").resize((160,250))
                self.card1_player = ImageTk.PhotoImage(card1_player)
                self.label_card1_player= tkinter.Label(master=self.frame_back, image=self.card1_player,borderwidth=0)
                self.label_card1_player.place(x=700, y=530)
                player_points += Card13.points
            if (player_card2 == 15):
                card1_player = Image.open(PATH +"/img/cards/"+Card14.img_file+".png").resize((160,250))
                self.card1_player = ImageTk.PhotoImage(card1_player)
                self.label_card1_player= tkinter.Label(master=self.frame_back, image=self.card1_player,borderwidth=0)
                self.label_card1_player.place(x=700, y=530)
                player_points += Card14.points
            if (player_card2 == 16):
                card1_player = Image.open(PATH +"/img/cards/"+Card15.img_file+".png").resize((160,250))
                self.card1_player = ImageTk.PhotoImage(card1_player)
                self.label_card1_player= tkinter.Label(master=self.frame_back, image=self.card1_player,borderwidth=0)
                self.label_card1_player.place(x=700, y=530)
                player_points += Card15.points
            if (player_card2 == 17):
                card1_player = Image.open(PATH +"/img/cards/"+Card16.img_file+".png").resize((160,250))
                self.card1_player = ImageTk.PhotoImage(card1_player)
                self.label_card1_player= tkinter.Label(master=self.frame_back, image=self.card1_player,borderwidth=0)
                self.label_card1_player.place(x=700, y=530)
                player_points += Card16.points
            if (player_card2 == 18):
                card1_player = Image.open(PATH +"/img/cards/"+Card17.img_file+".png").resize((160,250))
                self.card1_player = ImageTk.PhotoImage(card1_player)
                self.label_card1_player= tkinter.Label(master=self.frame_back, image=self.card1_player,borderwidth=0)
                self.label_card1_player.place(x=700, y=530)
                player_points += Card17.points
            if (player_card2 == 19):
                card1_player = Image.open(PATH +"/img/cards/"+Card18.img_file+".png").resize((160,250))
                self.card1_player = ImageTk.PhotoImage(card1_player)
                self.label_card1_player= tkinter.Label(master=self.frame_back, image=self.card1_player,borderwidth=0)
                self.label_card1_player.place(x=700, y=530)
                player_points += Card18.points
            if (player_card2 == 20):
                card1_player = Image.open(PATH +"/img/cards/"+Card19.img_file+".png").resize((160,250))
                self.card1_player = ImageTk.PhotoImage(card1_player)
                self.label_card1_player= tkinter.Label(master=self.frame_back, image=self.card1_player,borderwidth=0)
                self.label_card1_player.place(x=700, y=530)
                player_points += Card19.points
            if (player_card2 == 21):
                card1_player = Image.open(PATH +"/img/cards/"+Card20.img_file+".png").resize((160,250))
                self.card1_player = ImageTk.PhotoImage(card1_player)
                self.label_card1_player= tkinter.Label(master=self.frame_back, image=self.card1_player,borderwidth=0)
                self.label_card1_player.place(x=700, y=530)
                player_points += Card20.points
            if (player_card2 == 22):
                card1_player = Image.open(PATH +"/img/cards/"+Card21.img_file+".png").resize((160,250))
                self.card1_player = ImageTk.PhotoImage(card1_player)
                self.label_card1_player= tkinter.Label(master=self.frame_back, image=self.card1_player,borderwidth=0)
                self.label_card1_player.place(x=700, y=530)
                player_points += Card21.points
            if (player_card2 == 23):
                card1_player = Image.open(PATH +"/img/cards/"+Card22.img_file+".png").resize((160,250))
                self.card1_player = ImageTk.PhotoImage(card1_player)
                self.label_card1_player= tkinter.Label(master=self.frame_back, image=self.card1_player,borderwidth=0)
                self.label_card1_player.place(x=700, y=530)
                player_points += Card22.points
            if (player_card2 == 24):
                card1_player = Image.open(PATH +"/img/cards/"+Card23.img_file+".png").resize((160,250))
                self.card1_player = ImageTk.PhotoImage(card1_player)
                self.label_card1_player= tkinter.Label(master=self.frame_back, image=self.card1_player,borderwidth=0)
                self.label_card1_player.place(x=700, y=530)
                player_points += Card23.points
            if (player_card2 == 25):
                card1_player = Image.open(PATH +"/img/cards/"+Card24.img_file+".png").resize((160,250))
                self.card1_player = ImageTk.PhotoImage(card1_player)
                self.label_card1_player= tkinter.Label(master=self.frame_back, image=self.card1_player,borderwidth=0)
                self.label_card1_player.place(x=700, y=530)
                player_points += Card24.points
            if (player_card2 == 26):
                card1_player = Image.open(PATH +"/img/cards/"+Card25.img_file+".png").resize((160,250))
                self.card1_player = ImageTk.PhotoImage(card1_player)
                self.label_card1_player= tkinter.Label(master=self.frame_back, image=self.card1_player,borderwidth=0)
                self.label_card1_player.place(x=700, y=530)
                player_points += Card25.points
            if (player_card2 == 27):
                card1_player = Image.open(PATH +"/img/cards/"+Card26.img_file+".png").resize((160,250))
                self.card1_player = ImageTk.PhotoImage(card1_player)
                self.label_card1_player= tkinter.Label(master=self.frame_back, image=self.card1_player,borderwidth=0)
                self.label_card1_player.place(x=700, y=530)
                player_points += Card26.points
            if (player_card2 == 28):
                card1_player = Image.open(PATH +"/img/cards/"+Card27.img_file+".png").resize((160,250))
                self.card1_player = ImageTk.PhotoImage(card1_player)
                self.label_card1_player= tkinter.Label(master=self.frame_back, image=self.card1_player,borderwidth=0)
                self.label_card1_player.place(x=700, y=530)
                player_points += Card27.points
            if (player_card2 == 29):
                card1_player = Image.open(PATH +"/img/cards/"+Card28.img_file+".png").resize((160,250))
                self.card1_player = ImageTk.PhotoImage(card1_player)
                self.label_card1_player= tkinter.Label(master=self.frame_back, image=self.card1_player,borderwidth=0)
                self.label_card1_player.place(x=700, y=530)
                player_points += Card28.points
            if (player_card2 == 30):
                card1_player = Image.open(PATH +"/img/cards/"+Card29.img_file+".png").resize((160,250))
                self.card1_player = ImageTk.PhotoImage(card1_player)
                self.label_card1_player= tkinter.Label(master=self.frame_back, image=self.card1_player,borderwidth=0)
                self.label_card1_player.place(x=700, y=530)
                player_points += Card29.points
            if (player_card2 == 31):
                card1_player = Image.open(PATH +"/img/cards/"+Card30.img_file+".png").resize((160,250))
                self.card1_player = ImageTk.PhotoImage(card1_player)
                self.label_card1_player= tkinter.Label(master=self.frame_back, image=self.card1_player,borderwidth=0)
                self.label_card1_player.place(x=700, y=530)
                player_points += Card30.points
            if (player_card2 == 32):
                card1_player = Image.open(PATH +"/img/cards/"+Card31.img_file+".png").resize((160,250))
                self.card1_player = ImageTk.PhotoImage(card1_player)
                self.label_card1_player= tkinter.Label(master=self.frame_back, image=self.card1_player,borderwidth=0)
                self.label_card1_player.place(x=700, y=530)
                player_points += Card31.points
            if (player_card2 == 33):
                card1_player = Image.open(PATH +"/img/cards/"+Card32.img_file+".png").resize((160,250))
                self.card1_player = ImageTk.PhotoImage(card1_player)
                self.label_card1_player= tkinter.Label(master=self.frame_back, image=self.card1_player,borderwidth=0)
                self.label_card1_player.place(x=700, y=530)
                player_points += Card32.points
            if (player_card2 == 34):
                card1_player = Image.open(PATH +"/img/cards/"+Card33.img_file+".png").resize((160,250))
                self.card1_player = ImageTk.PhotoImage(card1_player)
                self.label_card1_player= tkinter.Label(master=self.frame_back, image=self.card1_player,borderwidth=0)
                self.label_card1_player.place(x=700, y=530)
                player_points += Card33.points
            if (player_card2 == 35):
                card1_player = Image.open(PATH +"/img/cards/"+Card34.img_file+".png").resize((160,250))
                self.card1_player = ImageTk.PhotoImage(card1_player)
                self.label_card1_player= tkinter.Label(master=self.frame_back, image=self.card1_player,borderwidth=0)
                self.label_card1_player.place(x=700, y=530)
                player_points += Card34.points
            if (player_card2 == 36):
                card1_player = Image.open(PATH +"/img/cards/"+Card35.img_file+".png").resize((160,250))
                self.card1_player = ImageTk.PhotoImage(card1_player)
                self.label_card1_player= tkinter.Label(master=self.frame_back, image=self.card1_player,borderwidth=0)
                self.label_card1_player.place(x=700, y=530)
                player_points += Card35.points
            if (player_card2 == 37):
                card1_player = Image.open(PATH +"/img/cards/"+Card36.img_file+".png").resize((160,250))
                self.card1_player = ImageTk.PhotoImage(card1_player)
                self.label_card1_player= tkinter.Label(master=self.frame_back, image=self.card1_player,borderwidth=0)
                self.label_card1_player.place(x=700, y=530)
                player_points += Card36.points
            if (player_card2 == 38):
                card1_player = Image.open(PATH +"/img/cards/"+Card37.img_file+".png").resize((160,250))
                self.card1_player = ImageTk.PhotoImage(card1_player)
                self.label_card1_player= tkinter.Label(master=self.frame_back, image=self.card1_player,borderwidth=0)
                self.label_card1_player.place(x=700, y=530)
                player_points += Card37.points
            if (player_card2 == 39):
                card1_player = Image.open(PATH +"/img/cards/"+Card38.img_file+".png").resize((160,250))
                self.card1_player = ImageTk.PhotoImage(card1_player)
                self.label_card1_player= tkinter.Label(master=self.frame_back, image=self.card1_player,borderwidth=0)
                self.label_card1_player.place(x=700, y=530)
                player_points += Card38.points
            if (player_card2 == 40):
                card1_player = Image.open(PATH +"/img/cards/"+Card39.img_file+".png").resize((160,250))
                self.card1_player = ImageTk.PhotoImage(card1_player)
                self.label_card1_player= tkinter.Label(master=self.frame_back, image=self.card1_player,borderwidth=0)
                self.label_card1_player.place(x=700, y=530)
                player_points += Card39.points
            if (player_card2 == 41):
                card1_player = Image.open(PATH +"/img/cards/"+Card40.img_file+".png").resize((160,250))
                self.card1_player = ImageTk.PhotoImage(card1_player)
                self.label_card1_player= tkinter.Label(master=self.frame_back, image=self.card1_player,borderwidth=0)
                self.label_card1_player.place(x=700, y=530)
                player_points += Card40.points
            if (player_card2 == 42):
                card1_player = Image.open(PATH +"/img/cards/"+Card41.img_file+".png").resize((160,250))
                self.card1_player = ImageTk.PhotoImage(card1_player)
                self.label_card1_player= tkinter.Label(master=self.frame_back, image=self.card1_player,borderwidth=0)
                self.label_card1_player.place(x=700, y=530)
                player_points += Card41.points
            if (player_card2 == 43):
                card1_player = Image.open(PATH +"/img/cards/"+Card42.img_file+".png").resize((160,250))
                self.card1_player = ImageTk.PhotoImage(card1_player)
                self.label_card1_player= tkinter.Label(master=self.frame_back, image=self.card1_player,borderwidth=0)
                self.label_card1_player.place(x=700, y=530)
                player_points += Card42.points
            if (player_card2 == 44):
                card1_player = Image.open(PATH +"/img/cards/"+Card43.img_file+".png").resize((160,250))
                self.card1_player = ImageTk.PhotoImage(card1_player)
                self.label_card1_player= tkinter.Label(master=self.frame_back, image=self.card1_player,borderwidth=0)
                self.label_card1_player.place(x=700, y=530)
                player_points += Card43.points
            if (player_card2 == 45):
                card1_player = Image.open(PATH +"/img/cards/"+Card44.img_file+".png").resize((160,250))
                self.card1_player = ImageTk.PhotoImage(card1_player)
                self.label_card1_player= tkinter.Label(master=self.frame_back, image=self.card1_player,borderwidth=0)
                self.label_card1_player.place(x=700, y=530)
                player_points += Card44.points
            if (player_card2 == 46):
                card1_player = Image.open(PATH +"/img/cards/"+Card45.img_file+".png").resize((160,250))
                self.card1_player = ImageTk.PhotoImage(card1_player)
                self.label_card1_player= tkinter.Label(master=self.frame_back, image=self.card1_player,borderwidth=0)
                self.label_card1_player.place(x=700, y=530)
                player_points += Card45.points
            if (player_card2 == 47):
                card1_player = Image.open(PATH +"/img/cards/"+Card46.img_file+".png").resize((160,250))
                self.card1_player = ImageTk.PhotoImage(card1_player)
                self.label_card1_player= tkinter.Label(master=self.frame_back, image=self.card1_player,borderwidth=0)
                self.label_card1_player.place(x=700, y=530)
                player_points += Card46.points
            if (player_card2 == 48):
                card1_player = Image.open(PATH +"/img/cards/"+Card47.img_file+".png").resize((160,250))
                self.card1_player = ImageTk.PhotoImage(card1_player)
                self.label_card1_player= tkinter.Label(master=self.frame_back, image=self.card1_player,borderwidth=0)
                self.label_card1_player.place(x=700, y=530)
                player_points += Card47.points
            # =========== end player card 2 
            
            if (dealer_card1 == 1):
                card0_dealer = Image.open(PATH +"/img/cards/"+Card0.img_file+".png").resize((160,250))
                self.card0_dealer = ImageTk.PhotoImage(card0_dealer)
                self.label_card0_dealer= tkinter.Label(master=self.frame_back, image=self.card0_dealer,borderwidth=0)
                self.label_card0_dealer.place(x=500, y=250) 
                dealer_points += Card0.points
            if (dealer_card1 == 2):
                card0_dealer = Image.open(PATH +"/img/cards/"+Card1.img_file+".png").resize((160,250))
                self.card0_dealer = ImageTk.PhotoImage(card0_dealer)
                self.label_card0_dealer= tkinter.Label(master=self.frame_back, image=self.card0_dealer,borderwidth=0)
                self.label_card0_dealer.place(x=500, y=250)
                dealer_points += Card1.points
            if (dealer_card1 == 3):
                card0_dealer = Image.open(PATH +"/img/cards/"+Card2.img_file+".png").resize((160,250))
                self.card0_dealer = ImageTk.PhotoImage(card0_dealer)
                self.label_card0_dealer= tkinter.Label(master=self.frame_back, image=self.card0_dealer,borderwidth=0)
                self.label_card0_dealer.place(x=500, y=250) 
                dealer_points += Card2.points
            if (dealer_card1 == 4):
                card0_dealer = Image.open(PATH +"/img/cards/"+Card3.img_file+".png").resize((160,250))
                self.card0_dealer = ImageTk.PhotoImage(card0_dealer)
                self.label_card0_dealer= tkinter.Label(master=self.frame_back, image=self.card0_dealer,borderwidth=0)
                self.label_card0_dealer.place(x=500, y=250) 
                dealer_points += Card3.points
            if (dealer_card1 == 5):
                card0_dealer = Image.open(PATH +"/img/cards/"+Card4.img_file+".png").resize((160,250))
                self.card0_dealer = ImageTk.PhotoImage(card0_dealer)
                self.label_card0_dealer= tkinter.Label(master=self.frame_back, image=self.card0_dealer,borderwidth=0)
                self.label_card0_dealer.place(x=500, y=250) 
                dealer_points += Card4.points
            if (dealer_card1 == 6):
                card0_dealer = Image.open(PATH +"/img/cards/"+Card5.img_file+".png").resize((160,250))
                self.card0_dealer = ImageTk.PhotoImage(card0_dealer)
                self.label_card0_dealer= tkinter.Label(master=self.frame_back, image=self.card0_dealer,borderwidth=0)
                self.label_card0_dealer.place(x=500, y=250)
                dealer_points += Card5.points
            if (dealer_card1 == 7):
                card0_dealer = Image.open(PATH +"/img/cards/"+Card6.img_file+".png").resize((160,250))
                self.card0_dealer = ImageTk.PhotoImage(card0_dealer)
                self.label_card0_dealer= tkinter.Label(master=self.frame_back, image=self.card0_dealer,borderwidth=0)
                self.label_card0_dealer.place(x=500, y=250) 
                dealer_points += Card6.points
            if (dealer_card1 == 8):
                card0_dealer = Image.open(PATH +"/img/cards/"+Card7.img_file+".png").resize((160,250))
                self.card0_dealer = ImageTk.PhotoImage(card0_dealer)
                self.label_card0_dealer= tkinter.Label(master=self.frame_back, image=self.card0_dealer,borderwidth=0)
                self.label_card0_dealer.place(x=500, y=250) 
                dealer_points += Card7.points
            if (dealer_card1 == 9):
                card0_dealer = Image.open(PATH +"/img/cards/"+Card8.img_file+".png").resize((160,250))
                self.card0_dealer = ImageTk.PhotoImage(card0_dealer)
                self.label_card0_dealer= tkinter.Label(master=self.frame_back, image=self.card0_dealer,borderwidth=0)
                self.label_card0_dealer.place(x=500, y=250)
                dealer_points += Card8.points
            if (dealer_card1 == 10):
                card0_dealer = Image.open(PATH +"/img/cards/"+Card9.img_file+".png").resize((160,250))
                self.card0_dealer = ImageTk.PhotoImage(card0_dealer)
                self.label_card0_dealer= tkinter.Label(master=self.frame_back, image=self.card0_dealer,borderwidth=0)
                self.label_card0_dealer.place(x=500, y=250)
                dealer_points += Card9.points
            if (dealer_card1 == 11):
                card0_dealer = Image.open(PATH +"/img/cards/"+Card10.img_file+".png").resize((160,250))
                self.card0_dealer = ImageTk.PhotoImage(card0_dealer)
                self.label_card0_dealer= tkinter.Label(master=self.frame_back, image=self.card0_dealer,borderwidth=0)
                self.label_card0_dealer.place(x=500, y=250) 
                dealer_points += Card10.points
            if (dealer_card1 == 12):
                card0_dealer = Image.open(PATH +"/img/cards/"+Card11.img_file+".png").resize((160,250))
                self.card0_dealer = ImageTk.PhotoImage(card0_dealer)
                self.label_card0_dealer= tkinter.Label(master=self.frame_back, image=self.card0_dealer,borderwidth=0)
                self.label_card0_dealer.place(x=500, y=250) 
                dealer_points += Card11.points
            if (dealer_card1 == 13):
                card0_dealer = Image.open(PATH +"/img/cards/"+Card12.img_file+".png").resize((160,250))
                self.card0_dealer = ImageTk.PhotoImage(card0_dealer)
                self.label_card0_dealer= tkinter.Label(master=self.frame_back, image=self.card0_dealer,borderwidth=0)
                self.label_card0_dealer.place(x=500, y=250) 
                dealer_points += Card12.points
            if (dealer_card1 == 14):
                card0_dealer = Image.open(PATH +"/img/cards/"+Card13.img_file+".png").resize((160,250))
                self.card0_dealer = ImageTk.PhotoImage(card0_dealer)
                self.label_card0_dealer= tkinter.Label(master=self.frame_back, image=self.card0_dealer,borderwidth=0)
                self.label_card0_dealer.place(x=500, y=250) 
                dealer_points += Card13.points
            if (dealer_card1 == 15):
                card0_dealer = Image.open(PATH +"/img/cards/"+Card14.img_file+".png").resize((160,250))
                self.card0_dealer = ImageTk.PhotoImage(card0_dealer)
                self.label_card0_dealer= tkinter.Label(master=self.frame_back, image=self.card0_dealer,borderwidth=0)
                self.label_card0_dealer.place(x=500, y=250)
                dealer_points += Card14.points
            if (dealer_card1 == 16):
                card0_dealer = Image.open(PATH +"/img/cards/"+Card15.img_file+".png").resize((160,250))
                self.card0_dealer = ImageTk.PhotoImage(card0_dealer)
                self.label_card0_dealer= tkinter.Label(master=self.frame_back, image=self.card0_dealer,borderwidth=0)
                self.label_card0_dealer.place(x=500, y=250) 
                dealer_points += Card15.points
            if (dealer_card1 == 17):
                card0_dealer = Image.open(PATH +"/img/cards/"+Card16.img_file+".png").resize((160,250))
                self.card0_dealer = ImageTk.PhotoImage(card0_dealer)
                self.label_card0_dealer= tkinter.Label(master=self.frame_back, image=self.card0_dealer,borderwidth=0)
                self.label_card0_dealer.place(x=500, y=250) 
                dealer_points += Card16.points
            if (dealer_card1 == 18):
                card0_dealer = Image.open(PATH +"/img/cards/"+Card17.img_file+".png").resize((160,250))
                self.card0_dealer = ImageTk.PhotoImage(card0_dealer)
                self.label_card0_dealer= tkinter.Label(master=self.frame_back, image=self.card0_dealer,borderwidth=0)
                self.label_card0_dealer.place(x=500, y=250) 
                dealer_points += Card17.points
            if (dealer_card1 == 19):
                card0_dealer = Image.open(PATH +"/img/cards/"+Card18.img_file+".png").resize((160,250))
                self.card0_dealer = ImageTk.PhotoImage(card0_dealer)
                self.label_card0_dealer= tkinter.Label(master=self.frame_back, image=self.card0_dealer,borderwidth=0)
                self.label_card0_dealer.place(x=500, y=250) 
                dealer_points += Card18.points
            if (dealer_card1 == 20):
                card0_dealer = Image.open(PATH +"/img/cards/"+Card19.img_file+".png").resize((160,250))
                self.card0_dealer = ImageTk.PhotoImage(card0_dealer)
                self.label_card0_dealer= tkinter.Label(master=self.frame_back, image=self.card0_dealer,borderwidth=0)
                self.label_card0_dealer.place(x=500, y=250)
                dealer_points += Card19.points
            if (dealer_card1 == 21):
                card0_dealer = Image.open(PATH +"/img/cards/"+Card20.img_file+".png").resize((160,250))
                self.card0_dealer = ImageTk.PhotoImage(card0_dealer)
                self.label_card0_dealer= tkinter.Label(master=self.frame_back, image=self.card0_dealer,borderwidth=0)
                self.label_card0_dealer.place(x=500, y=250)
                dealer_points += Card20.points
            if (dealer_card1 == 22):
                card0_dealer = Image.open(PATH +"/img/cards/"+Card21.img_file+".png").resize((160,250))
                self.card0_dealer = ImageTk.PhotoImage(card0_dealer)
                self.label_card0_dealer= tkinter.Label(master=self.frame_back, image=self.card0_dealer,borderwidth=0)
                self.label_card0_dealer.place(x=500, y=250)
                dealer_points += Card21.points
            if (dealer_card1 == 23):
                card0_dealer = Image.open(PATH +"/img/cards/"+Card22.img_file+".png").resize((160,250))
                self.card0_dealer = ImageTk.PhotoImage(card0_dealer)
                self.label_card0_dealer= tkinter.Label(master=self.frame_back, image=self.card0_dealer,borderwidth=0)
                self.label_card0_dealer.place(x=500, y=250)
                dealer_points += Card22.points
            if (dealer_card1 == 24):
                card0_dealer = Image.open(PATH +"/img/cards/"+Card23.img_file+".png").resize((160,250))
                self.card0_dealer = ImageTk.PhotoImage(card0_dealer)
                self.label_card0_dealer= tkinter.Label(master=self.frame_back, image=self.card0_dealer,borderwidth=0)
                self.label_card0_dealer.place(x=500, y=250)
                dealer_points += Card23.points
            if (dealer_card1 == 25):
                card0_dealer = Image.open(PATH +"/img/cards/"+Card24.img_file+".png").resize((160,250))
                self.card0_dealer = ImageTk.PhotoImage(card0_dealer)
                self.label_card0_dealer= tkinter.Label(master=self.frame_back, image=self.card0_dealer,borderwidth=0)
                self.label_card0_dealer.place(x=500, y=250)
                dealer_points += Card24.points
            if (dealer_card1 == 26):
                card0_dealer = Image.open(PATH +"/img/cards/"+Card25.img_file+".png").resize((160,250))
                self.card0_dealer = ImageTk.PhotoImage(card0_dealer)
                self.label_card0_dealer= tkinter.Label(master=self.frame_back, image=self.card0_dealer,borderwidth=0)
                self.label_card0_dealer.place(x=500, y=250)
                dealer_points += Card25.points
            if (dealer_card1 == 27):
                card0_dealer = Image.open(PATH +"/img/cards/"+Card26.img_file+".png").resize((160,250))
                self.card0_dealer = ImageTk.PhotoImage(card0_dealer)
                self.label_card0_dealer= tkinter.Label(master=self.frame_back, image=self.card0_dealer,borderwidth=0)
                self.label_card0_dealer.place(x=500, y=250)
                dealer_points += Card26.points
            if (dealer_card1 == 28):
                card0_dealer = Image.open(PATH +"/img/cards/"+Card27.img_file+".png").resize((160,250))
                self.card0_dealer = ImageTk.PhotoImage(card0_dealer)
                self.label_card0_dealer= tkinter.Label(master=self.frame_back, image=self.card0_dealer,borderwidth=0)
                self.label_card0_dealer.place(x=500, y=250)
                dealer_points += Card27.points
            if (dealer_card1 == 29):
                card0_dealer = Image.open(PATH +"/img/cards/"+Card28.img_file+".png").resize((160,250))
                self.card0_dealer = ImageTk.PhotoImage(card0_dealer)
                self.label_card0_dealer= tkinter.Label(master=self.frame_back, image=self.card0_dealer,borderwidth=0)
                self.label_card0_dealer.place(x=500, y=250)
                dealer_points += Card28.points
            if (dealer_card1 == 30):
                card0_dealer = Image.open(PATH +"/img/cards/"+Card29.img_file+".png").resize((160,250))
                self.card0_dealer = ImageTk.PhotoImage(card0_dealer)
                self.label_card0_dealer= tkinter.Label(master=self.frame_back, image=self.card0_dealer,borderwidth=0)
                self.label_card0_dealer.place(x=500, y=250)
                dealer_points += Card29.points
            if (dealer_card1 == 31):
                card0_dealer = Image.open(PATH +"/img/cards/"+Card30.img_file+".png").resize((160,250))
                self.card0_dealer = ImageTk.PhotoImage(card0_dealer)
                self.label_card0_dealer= tkinter.Label(master=self.frame_back, image=self.card0_dealer,borderwidth=0)
                self.label_card0_dealer.place(x=500, y=250)
                dealer_points += Card30.points
            if (dealer_card1 == 32):
                card0_dealer = Image.open(PATH +"/img/cards/"+Card31.img_file+".png").resize((160,250))
                self.card0_dealer = ImageTk.PhotoImage(card0_dealer)
                self.label_card0_dealer= tkinter.Label(master=self.frame_back, image=self.card0_dealer,borderwidth=0)
                self.label_card0_dealer.place(x=500, y=250)
                dealer_points += Card31.points
            if (dealer_card1 == 33):
                card0_dealer = Image.open(PATH +"/img/cards/"+Card32.img_file+".png").resize((160,250))
                self.card0_dealer = ImageTk.PhotoImage(card0_dealer)
                self.label_card0_dealer= tkinter.Label(master=self.frame_back, image=self.card0_dealer,borderwidth=0)
                self.label_card0_dealer.place(x=500, y=250)
                dealer_points += Card32.points
            if (dealer_card1 == 34):
                card0_dealer = Image.open(PATH +"/img/cards/"+Card33.img_file+".png").resize((160,250))
                self.card0_dealer = ImageTk.PhotoImage(card0_dealer)
                self.label_card0_dealer= tkinter.Label(master=self.frame_back, image=self.card0_dealer,borderwidth=0)
                self.label_card0_dealer.place(x=500, y=250)
                dealer_points += Card33.points
            if (dealer_card1 == 35):
                card0_dealer = Image.open(PATH +"/img/cards/"+Card34.img_file+".png").resize((160,250))
                self.card0_dealer = ImageTk.PhotoImage(card0_dealer)
                self.label_card0_dealer= tkinter.Label(master=self.frame_back, image=self.card0_dealer,borderwidth=0)
                self.label_card0_dealer.place(x=500, y=250)
                dealer_points += Card34.points
            if (dealer_card1 == 36):
                card0_dealer = Image.open(PATH +"/img/cards/"+Card35.img_file+".png").resize((160,250))
                self.card0_dealer = ImageTk.PhotoImage(card0_dealer)
                self.label_card0_dealer= tkinter.Label(master=self.frame_back, image=self.card0_dealer,borderwidth=0)
                self.label_card0_dealer.place(x=500, y=250)
                dealer_points += Card35.points
            if (dealer_card1 == 37):
                card0_dealer = Image.open(PATH +"/img/cards/"+Card36.img_file+".png").resize((160,250))
                self.card0_dealer = ImageTk.PhotoImage(card0_dealer)
                self.label_card0_dealer= tkinter.Label(master=self.frame_back, image=self.card0_dealer,borderwidth=0)
                self.label_card0_dealer.place(x=500, y=250)
                dealer_points += Card36.points
            if (dealer_card1 == 38):
                card0_dealer = Image.open(PATH +"/img/cards/"+Card37.img_file+".png").resize((160,250))
                self.card0_dealer = ImageTk.PhotoImage(card0_dealer)
                self.label_card0_dealer= tkinter.Label(master=self.frame_back, image=self.card0_dealer,borderwidth=0)
                self.label_card0_dealer.place(x=500, y=250)
                dealer_points += Card37.points
            if (dealer_card1 == 39):
                card0_dealer = Image.open(PATH +"/img/cards/"+Card38.img_file+".png").resize((160,250))
                self.card0_dealer = ImageTk.PhotoImage(card0_dealer)
                self.label_card0_dealer= tkinter.Label(master=self.frame_back, image=self.card0_dealer,borderwidth=0)
                self.label_card0_dealer.place(x=500, y=250)
                dealer_points += Card38.points
            if (dealer_card1 == 40):
                card0_dealer = Image.open(PATH +"/img/cards/"+Card39.img_file+".png").resize((160,250))
                self.card0_dealer = ImageTk.PhotoImage(card0_dealer)
                self.label_card0_dealer= tkinter.Label(master=self.frame_back, image=self.card0_dealer,borderwidth=0)
                self.label_card0_dealer.place(x=500, y=250)
                dealer_points += Card39.points
            if (dealer_card1 == 41):
                card0_dealer = Image.open(PATH +"/img/cards/"+Card40.img_file+".png").resize((160,250))
                self.card0_dealer = ImageTk.PhotoImage(card0_dealer)
                self.label_card0_dealer= tkinter.Label(master=self.frame_back, image=self.card0_dealer,borderwidth=0)
                self.label_card0_dealer.place(x=500, y=250)
                dealer_points += Card40.points
            if (dealer_card1 == 42):
                card0_dealer = Image.open(PATH +"/img/cards/"+Card41.img_file+".png").resize((160,250))
                self.card0_dealer = ImageTk.PhotoImage(card0_dealer)
                self.label_card0_dealer= tkinter.Label(master=self.frame_back, image=self.card0_dealer,borderwidth=0)
                self.label_card0_dealer.place(x=500, y=250)
                dealer_points += Card41.points
            if (dealer_card1 == 43):
                card0_dealer = Image.open(PATH +"/img/cards/"+Card42.img_file+".png").resize((160,250))
                self.card0_dealer = ImageTk.PhotoImage(card0_dealer)
                self.label_card0_dealer= tkinter.Label(master=self.frame_back, image=self.card0_dealer,borderwidth=0)
                self.label_card0_dealer.place(x=500, y=250)
                dealer_points += Card42.points
            if (dealer_card1 == 44):
                card0_dealer = Image.open(PATH +"/img/cards/"+Card43.img_file+".png").resize((160,250))
                self.card0_dealer = ImageTk.PhotoImage(card0_dealer)
                self.label_card0_dealer= tkinter.Label(master=self.frame_back, image=self.card0_dealer,borderwidth=0)
                self.label_card0_dealer.place(x=500, y=250)
                dealer_points += Card43.points
            if (dealer_card1 == 45):
                card0_dealer = Image.open(PATH +"/img/cards/"+Card44.img_file+".png").resize((160,250))
                self.card0_dealer = ImageTk.PhotoImage(card0_dealer)
                self.label_card0_dealer= tkinter.Label(master=self.frame_back, image=self.card0_dealer,borderwidth=0)
                self.label_card0_dealer.place(x=500, y=250)
                dealer_points += Card44.points
            if (dealer_card1 == 46):
                card0_dealer = Image.open(PATH +"/img/cards/"+Card45.img_file+".png").resize((160,250))
                self.card0_dealer = ImageTk.PhotoImage(card0_dealer)
                self.label_card0_dealer= tkinter.Label(master=self.frame_back, image=self.card0_dealer,borderwidth=0)
                self.label_card0_dealer.place(x=500, y=250)
                dealer_points += Card45.points
            if (dealer_card1 == 47):
                card0_dealer = Image.open(PATH +"/img/cards/"+Card46.img_file+".png").resize((160,250))
                self.card0_dealer = ImageTk.PhotoImage(card0_dealer)
                self.label_card0_dealer= tkinter.Label(master=self.frame_back, image=self.card0_dealer,borderwidth=0)
                self.label_card0_dealer.place(x=500, y=250)
                dealer_points += Card46.points
            if (dealer_card1 == 48):
                card0_dealer = Image.open(PATH +"/img/cards/"+Card47.img_file+".png").resize((160,250))
                self.card0_dealer = ImageTk.PhotoImage(card0_dealer)
                self.label_card0_dealer= tkinter.Label(master=self.frame_back, image=self.card0_dealer,borderwidth=0)
                self.label_card0_dealer.place(x=500, y=250)
                dealer_points += Card47.points
            # ================ end card 1 dealer
            
            if (dealer_card1 == 1):
                card1_dealer = Image.open(PATH +"/img/cards/"+Card0.img_file+".png").resize((160,250))
                self.card1_dealer = ImageTk.PhotoImage(card1_dealer)
                self.label_card1_dealer= tkinter.Label(master=self.frame_back, image=self.card1_dealer, borderwidth=0)
                self.label_card1_dealer.place(x=700, y=250)
                dealer_points += Card0.points
            if (dealer_card1 == 2):
                card1_dealer = Image.open(PATH +"/img/cards/"+Card1.img_file+".png").resize((160,250))
                self.card1_dealer = ImageTk.PhotoImage(card1_dealer)
                self.label_card1_dealer= tkinter.Label(master=self.frame_back, image=self.card1_dealer, borderwidth=0)
                self.label_card1_dealer.place(x=700, y=250)
                dealer_points += Card1.points
            if (dealer_card1 == 3):
                card1_dealer = Image.open(PATH +"/img/cards/"+Card2.img_file+".png").resize((160,250))
                self.card1_dealer = ImageTk.PhotoImage(card1_dealer)
                self.label_card1_dealer= tkinter.Label(master=self.frame_back, image=self.card1_dealer, borderwidth=0)
                self.label_card1_dealer.place(x=700, y=250)
                dealer_points += Card2.points
            if (dealer_card1 == 4):
                card1_dealer = Image.open(PATH +"/img/cards/"+Card3.img_file+".png").resize((160,250))
                self.card1_dealer = ImageTk.PhotoImage(card1_dealer)
                self.label_card1_dealer= tkinter.Label(master=self.frame_back, image=self.card1_dealer, borderwidth=0)
                self.label_card1_dealer.place(x=700, y=250)
                dealer_points += Card3.points
            if (dealer_card1 == 5):
                card1_dealer = Image.open(PATH +"/img/cards/"+Card4.img_file+".png").resize((160,250))
                self.card1_dealer = ImageTk.PhotoImage(card1_dealer)
                self.label_card1_dealer= tkinter.Label(master=self.frame_back, image=self.card1_dealer, borderwidth=0)
                self.label_card1_dealer.place(x=700, y=250)
                dealer_points += Card4.points
            if (dealer_card1 == 6):
                card1_dealer = Image.open(PATH +"/img/cards/"+Card5.img_file+".png").resize((160,250))
                self.card1_dealer = ImageTk.PhotoImage(card1_dealer)
                self.label_card1_dealer= tkinter.Label(master=self.frame_back, image=self.card1_dealer, borderwidth=0)
                self.label_card1_dealer.place(x=700, y=250)
                dealer_points += Card5.points
            if (dealer_card1 == 7):
                card1_dealer = Image.open(PATH +"/img/cards/"+Card6.img_file+".png").resize((160,250))
                self.card1_dealer = ImageTk.PhotoImage(card1_dealer)
                self.label_card1_dealer= tkinter.Label(master=self.frame_back, image=self.card1_dealer, borderwidth=0)
                self.label_card1_dealer.place(x=700, y=250)
                dealer_points += Card6.points
            if (dealer_card1 == 8):
                card1_dealer = Image.open(PATH +"/img/cards/"+Card7.img_file+".png").resize((160,250))
                self.card1_dealer = ImageTk.PhotoImage(card1_dealer)
                self.label_card1_dealer= tkinter.Label(master=self.frame_back, image=self.card1_dealer, borderwidth=0)
                self.label_card1_dealer.place(x=700, y=250)
                dealer_points += Card7.points
            if (dealer_card1 == 9):
                card1_dealer = Image.open(PATH +"/img/cards/"+Card8.img_file+".png").resize((160,250))
                self.card1_dealer = ImageTk.PhotoImage(card1_dealer)
                self.label_card1_dealer= tkinter.Label(master=self.frame_back, image=self.card1_dealer, borderwidth=0)
                self.label_card1_dealer.place(x=700, y=250)
                dealer_points += Card8.points
            if (dealer_card1 == 10):
                card1_dealer = Image.open(PATH +"/img/cards/"+Card9.img_file+".png").resize((160,250))
                self.card1_dealer = ImageTk.PhotoImage(card1_dealer)
                self.label_card1_dealer= tkinter.Label(master=self.frame_back, image=self.card1_dealer, borderwidth=0)
                self.label_card1_dealer.place(x=700, y=250)
                dealer_points += Card9.points
            if (dealer_card1 == 11):
                card1_dealer = Image.open(PATH +"/img/cards/"+Card10.img_file+".png").resize((160,250))
                self.card1_dealer = ImageTk.PhotoImage(card1_dealer)
                self.label_card1_dealer= tkinter.Label(master=self.frame_back, image=self.card1_dealer, borderwidth=0)
                self.label_card1_dealer.place(x=700, y=250)
                dealer_points += Card10.points
            if (dealer_card1 == 12):
                card1_dealer = Image.open(PATH +"/img/cards/"+Card11.img_file+".png").resize((160,250))
                self.card1_dealer = ImageTk.PhotoImage(card1_dealer)
                self.label_card1_dealer= tkinter.Label(master=self.frame_back, image=self.card1_dealer, borderwidth=0)
                self.label_card1_dealer.place(x=700, y=250)
                dealer_points += Card11.points
            if (dealer_card1 == 13):
                card1_dealer = Image.open(PATH +"/img/cards/"+Card12.img_file+".png").resize((160,250))
                self.card1_dealer = ImageTk.PhotoImage(card1_dealer)
                self.label_card1_dealer= tkinter.Label(master=self.frame_back, image=self.card1_dealer, borderwidth=0)
                self.label_card1_dealer.place(x=700, y=250)
                dealer_points += Card12.points
            if (dealer_card1 == 14):
                card1_dealer = Image.open(PATH +"/img/cards/"+Card13.img_file+".png").resize((160,250))
                self.card1_dealer = ImageTk.PhotoImage(card1_dealer)
                self.label_card1_dealer= tkinter.Label(master=self.frame_back, image=self.card1_dealer, borderwidth=0)
                self.label_card1_dealer.place(x=700, y=250)
                dealer_points += Card13.points
            if (dealer_card1 == 15):
                card1_dealer = Image.open(PATH +"/img/cards/"+Card14.img_file+".png").resize((160,250))
                self.card1_dealer = ImageTk.PhotoImage(card1_dealer)
                self.label_card1_dealer= tkinter.Label(master=self.frame_back, image=self.card1_dealer, borderwidth=0)
                self.label_card1_dealer.place(x=700, y=250)
                dealer_points += Card14.points
            if (dealer_card1 == 16):
                card1_dealer = Image.open(PATH +"/img/cards/"+Card15.img_file+".png").resize((160,250))
                self.card1_dealer = ImageTk.PhotoImage(card1_dealer)
                self.label_card1_dealer= tkinter.Label(master=self.frame_back, image=self.card1_dealer, borderwidth=0)
                self.label_card1_dealer.place(x=700, y=250)
                dealer_points += Card15.points
            if (dealer_card1 == 17):
                card1_dealer = Image.open(PATH +"/img/cards/"+Card16.img_file+".png").resize((160,250))
                self.card1_dealer = ImageTk.PhotoImage(card1_dealer)
                self.label_card1_dealer= tkinter.Label(master=self.frame_back, image=self.card1_dealer, borderwidth=0)
                self.label_card1_dealer.place(x=700, y=250)
                dealer_points += Card16.points
            if (dealer_card1 == 18):
                card1_dealer = Image.open(PATH +"/img/cards/"+Card17.img_file+".png").resize((160,250))
                self.card1_dealer = ImageTk.PhotoImage(card1_dealer)
                self.label_card1_dealer= tkinter.Label(master=self.frame_back, image=self.card1_dealer, borderwidth=0)
                self.label_card1_dealer.place(x=700, y=250)
                dealer_points += Card17.points
            if (dealer_card1 == 19):
                card1_dealer = Image.open(PATH +"/img/cards/"+Card18.img_file+".png").resize((160,250))
                self.card1_dealer = ImageTk.PhotoImage(card1_dealer)
                self.label_card1_dealer= tkinter.Label(master=self.frame_back, image=self.card1_dealer, borderwidth=0)
                self.label_card1_dealer.place(x=700, y=250)
                dealer_points += Card18.points
            if (dealer_card1 == 20):
                card1_dealer = Image.open(PATH +"/img/cards/"+Card19.img_file+".png").resize((160,250))
                self.card1_dealer = ImageTk.PhotoImage(card1_dealer)
                self.label_card1_dealer= tkinter.Label(master=self.frame_back, image=self.card1_dealer, borderwidth=0)
                self.label_card1_dealer.place(x=700, y=250)
                dealer_points += Card19.points                
            if (dealer_card1 == 21):
                card1_dealer = Image.open(PATH +"/img/cards/"+Card20.img_file+".png").resize((160,250))
                self.card1_dealer = ImageTk.PhotoImage(card1_dealer)
                self.label_card1_dealer= tkinter.Label(master=self.frame_back, image=self.card1_dealer, borderwidth=0)
                self.label_card1_dealer.place(x=700, y=250)
                dealer_points += Card20.points
            if (dealer_card1 == 22):
                card1_dealer = Image.open(PATH +"/img/cards/"+Card21.img_file+".png").resize((160,250))
                self.card1_dealer = ImageTk.PhotoImage(card1_dealer)
                self.label_card1_dealer= tkinter.Label(master=self.frame_back, image=self.card1_dealer, borderwidth=0)
                self.label_card1_dealer.place(x=700, y=250)
                dealer_points += Card21.points
            if (dealer_card1 == 23):
                card1_dealer = Image.open(PATH +"/img/cards/"+Card22.img_file+".png").resize((160,250))
                self.card1_dealer = ImageTk.PhotoImage(card1_dealer)
                self.label_card1_dealer= tkinter.Label(master=self.frame_back, image=self.card1_dealer, borderwidth=0)
                self.label_card1_dealer.place(x=700, y=250)
                dealer_points += Card22.points
            if (dealer_card1 == 24):
                card1_dealer = Image.open(PATH +"/img/cards/"+Card23.img_file+".png").resize((160,250))
                self.card1_dealer = ImageTk.PhotoImage(card1_dealer)
                self.label_card1_dealer= tkinter.Label(master=self.frame_back, image=self.card1_dealer, borderwidth=0)
                self.label_card1_dealer.place(x=700, y=250)
                dealer_points += Card23.points
            if (dealer_card1 == 25):
                card1_dealer = Image.open(PATH +"/img/cards/"+Card24.img_file+".png").resize((160,250))
                self.card1_dealer = ImageTk.PhotoImage(card1_dealer)
                self.label_card1_dealer= tkinter.Label(master=self.frame_back, image=self.card1_dealer, borderwidth=0)
                self.label_card1_dealer.place(x=700, y=250)
                dealer_points += Card24.points
            if (dealer_card1 == 26):
                card1_dealer = Image.open(PATH +"/img/cards/"+Card25.img_file+".png").resize((160,250))
                self.card1_dealer = ImageTk.PhotoImage(card1_dealer)
                self.label_card1_dealer= tkinter.Label(master=self.frame_back, image=self.card1_dealer, borderwidth=0)
                self.label_card1_dealer.place(x=700, y=250)
                dealer_points += Card25.points
            if (dealer_card1 == 27):
                card1_dealer = Image.open(PATH +"/img/cards/"+Card26.img_file+".png").resize((160,250))
                self.card1_dealer = ImageTk.PhotoImage(card1_dealer)
                self.label_card1_dealer= tkinter.Label(master=self.frame_back, image=self.card1_dealer, borderwidth=0)
                self.label_card1_dealer.place(x=700, y=250)
                dealer_points += Card26.points
            if (dealer_card1 == 28):
                card1_dealer = Image.open(PATH +"/img/cards/"+Card27.img_file+".png").resize((160,250))
                self.card1_dealer = ImageTk.PhotoImage(card1_dealer)
                self.label_card1_dealer= tkinter.Label(master=self.frame_back, image=self.card1_dealer, borderwidth=0)
                self.label_card1_dealer.place(x=700, y=250)
                dealer_points += Card27.points
            if (dealer_card1 == 29):
                card1_dealer = Image.open(PATH +"/img/cards/"+Card28.img_file+".png").resize((160,250))
                self.card1_dealer = ImageTk.PhotoImage(card1_dealer)
                self.label_card1_dealer= tkinter.Label(master=self.frame_back, image=self.card1_dealer, borderwidth=0)
                self.label_card1_dealer.place(x=700, y=250)
                dealer_points += Card28.points
            if (dealer_card1 == 30):
                card1_dealer = Image.open(PATH +"/img/cards/"+Card29.img_file+".png").resize((160,250))
                self.card1_dealer = ImageTk.PhotoImage(card1_dealer)
                self.label_card1_dealer= tkinter.Label(master=self.frame_back, image=self.card1_dealer, borderwidth=0)
                self.label_card1_dealer.place(x=700, y=250)
                dealer_points += Card29.points
            if (dealer_card1 == 31):
                card1_dealer = Image.open(PATH +"/img/cards/"+Card30.img_file+".png").resize((160,250))
                self.card1_dealer = ImageTk.PhotoImage(card1_dealer)
                self.label_card1_dealer= tkinter.Label(master=self.frame_back, image=self.card1_dealer, borderwidth=0)
                self.label_card1_dealer.place(x=700, y=250)
                dealer_points += Card30.points
            if (dealer_card1 == 32):
                card1_dealer = Image.open(PATH +"/img/cards/"+Card31.img_file+".png").resize((160,250))
                self.card1_dealer = ImageTk.PhotoImage(card1_dealer)
                self.label_card1_dealer= tkinter.Label(master=self.frame_back, image=self.card1_dealer, borderwidth=0)
                self.label_card1_dealer.place(x=700, y=250)
                dealer_points += Card31.points
            if (dealer_card1 == 33):
                card1_dealer = Image.open(PATH +"/img/cards/"+Card32.img_file+".png").resize((160,250))
                self.card1_dealer = ImageTk.PhotoImage(card1_dealer)
                self.label_card1_dealer= tkinter.Label(master=self.frame_back, image=self.card1_dealer, borderwidth=0)
                self.label_card1_dealer.place(x=700, y=250)
                dealer_points += Card32.points
            if (dealer_card1 == 34):
                card1_dealer = Image.open(PATH +"/img/cards/"+Card33.img_file+".png").resize((160,250))
                self.card1_dealer = ImageTk.PhotoImage(card1_dealer)
                self.label_card1_dealer= tkinter.Label(master=self.frame_back, image=self.card1_dealer, borderwidth=0)
                self.label_card1_dealer.place(x=700, y=250)
                dealer_points += Card33.points
            if (dealer_card1 == 35):
                card1_dealer = Image.open(PATH +"/img/cards/"+Card34.img_file+".png").resize((160,250))
                self.card1_dealer = ImageTk.PhotoImage(card1_dealer)
                self.label_card1_dealer= tkinter.Label(master=self.frame_back, image=self.card1_dealer, borderwidth=0)
                self.label_card1_dealer.place(x=700, y=250)
                dealer_points += Card34.points
            if (dealer_card1 == 36):
                card1_dealer = Image.open(PATH +"/img/cards/"+Card35.img_file+".png").resize((160,250))
                self.card1_dealer = ImageTk.PhotoImage(card1_dealer)
                self.label_card1_dealer= tkinter.Label(master=self.frame_back, image=self.card1_dealer, borderwidth=0)
                self.label_card1_dealer.place(x=700, y=250)
                dealer_points += Card35.points
            if (dealer_card1 == 37):
                card1_dealer = Image.open(PATH +"/img/cards/"+Card36.img_file+".png").resize((160,250))
                self.card1_dealer = ImageTk.PhotoImage(card1_dealer)
                self.label_card1_dealer= tkinter.Label(master=self.frame_back, image=self.card1_dealer, borderwidth=0)
                self.label_card1_dealer.place(x=700, y=250)
                dealer_points += Card36.points
            if (dealer_card1 == 38):
                card1_dealer = Image.open(PATH +"/img/cards/"+Card37.img_file+".png").resize((160,250))
                self.card1_dealer = ImageTk.PhotoImage(card1_dealer)
                self.label_card1_dealer= tkinter.Label(master=self.frame_back, image=self.card1_dealer, borderwidth=0)
                self.label_card1_dealer.place(x=700, y=250)
                dealer_points += Card37.points
            if (dealer_card1 == 39):
                card1_dealer = Image.open(PATH +"/img/cards/"+Card38.img_file+".png").resize((160,250))
                self.card1_dealer = ImageTk.PhotoImage(card1_dealer)
                self.label_card1_dealer= tkinter.Label(master=self.frame_back, image=self.card1_dealer, borderwidth=0)
                self.label_card1_dealer.place(x=700, y=250)
                dealer_points += Card38.points
            if (dealer_card1 == 40):
                card1_dealer = Image.open(PATH +"/img/cards/"+Card39.img_file+".png").resize((160,250))
                self.card1_dealer = ImageTk.PhotoImage(card1_dealer)
                self.label_card1_dealer= tkinter.Label(master=self.frame_back, image=self.card1_dealer, borderwidth=0)
                self.label_card1_dealer.place(x=700, y=250)
                dealer_points += Card39.points
            if (dealer_card1 == 41):
                card1_dealer = Image.open(PATH +"/img/cards/"+Card40.img_file+".png").resize((160,250))
                self.card1_dealer = ImageTk.PhotoImage(card1_dealer)
                self.label_card1_dealer= tkinter.Label(master=self.frame_back, image=self.card1_dealer, borderwidth=0)
                self.label_card1_dealer.place(x=700, y=250)
                dealer_points += Card40.points
            if (dealer_card1 == 42):
                card1_dealer = Image.open(PATH +"/img/cards/"+Card41.img_file+".png").resize((160,250))
                self.card1_dealer = ImageTk.PhotoImage(card1_dealer)
                self.label_card1_dealer= tkinter.Label(master=self.frame_back, image=self.card1_dealer, borderwidth=0)
                self.label_card1_dealer.place(x=700, y=250)
                dealer_points += Card41.points
            if (dealer_card1 == 43):
                card1_dealer = Image.open(PATH +"/img/cards/"+Card42.img_file+".png").resize((160,250))
                self.card1_dealer = ImageTk.PhotoImage(card1_dealer)
                self.label_card1_dealer= tkinter.Label(master=self.frame_back, image=self.card1_dealer, borderwidth=0)
                self.label_card1_dealer.place(x=700, y=250)
                dealer_points += Card42.points
            if (dealer_card1 == 44):
                card1_dealer = Image.open(PATH +"/img/cards/"+Card43.img_file+".png").resize((160,250))
                self.card1_dealer = ImageTk.PhotoImage(card1_dealer)
                self.label_card1_dealer= tkinter.Label(master=self.frame_back, image=self.card1_dealer, borderwidth=0)
                self.label_card1_dealer.place(x=700, y=250)
                dealer_points += Card43.points
            if (dealer_card1 == 45):
                card1_dealer = Image.open(PATH +"/img/cards/"+Card44.img_file+".png").resize((160,250))
                self.card1_dealer = ImageTk.PhotoImage(card1_dealer)
                self.label_card1_dealer= tkinter.Label(master=self.frame_back, image=self.card1_dealer, borderwidth=0)
                self.label_card1_dealer.place(x=700, y=250)
                dealer_points += Card44.points
            if (dealer_card1 == 46):
                card1_dealer = Image.open(PATH +"/img/cards/"+Card45.img_file+".png").resize((160,250))
                self.card1_dealer = ImageTk.PhotoImage(card1_dealer)
                self.label_card1_dealer= tkinter.Label(master=self.frame_back, image=self.card1_dealer, borderwidth=0)
                self.label_card1_dealer.place(x=700, y=250)
                dealer_points += Card45.points
            if (dealer_card1 == 47):
                card1_dealer = Image.open(PATH +"/img/cards/"+Card46.img_file+".png").resize((160,250))
                self.card1_dealer = ImageTk.PhotoImage(card1_dealer)
                self.label_card1_dealer= tkinter.Label(master=self.frame_back, image=self.card1_dealer, borderwidth=0)
                self.label_card1_dealer.place(x=700, y=250)
                dealer_points += Card46.points
            if (dealer_card1 == 48):
                card1_dealer = Image.open(PATH +"/img/cards/"+Card47.img_file+".png").resize((160,250))
                self.card1_dealer = ImageTk.PhotoImage(card1_dealer)
                self.label_card1_dealer= tkinter.Label(master=self.frame_back, image=self.card1_dealer, borderwidth=0)
                self.label_card1_dealer.place(x=700, y=250)
                dealer_points += Card47.points
            self.label_card0_dealer= tkinter.Label(master=self.frame_back, image=self.holder_card,borderwidth=0)
            self.label_card0_dealer.place(x=500, y=250)
            self.label_player_points.configure(text=str(player_points))
            self.label_dealer_points.configure(text="??")   
        play(self)
        
        def draw_card(self):
            global index_card
            global player_points
            global dealer_points
            global last_draw_card
            if(last_draw_card > 48):
                last_draw_card = 0
                np.random.shuffle(Game_array)
            index_card += 1 
            if(index_card == 2):                
                if(dealer_points<16):
                    last_draw_card +=1
                    dealer_card2 = Game_array [last_draw_card]
                    if(dealer_card2 == 1):
                        card2_dealer = Image.open(PATH +"/img/cards/"+Card0.img_file+".png").resize((160,250))
                        self.card2_dealer = ImageTk.PhotoImage(card2_dealer)
                        self.label_card2_dealer= tkinter.Label(master=self.frame_back, image=self.card2_dealer, borderwidth=0)
                        self.label_card2_dealer.place(x=900, y=250)
                        dealer_points += Card0.points
                    if(dealer_card2 == 2):
                        card2_dealer = Image.open(PATH +"/img/cards/"+Card1.img_file+".png").resize((160,250))
                        self.card2_dealer = ImageTk.PhotoImage(card2_dealer)
                        self.label_card2_dealer= tkinter.Label(master=self.frame_back, image=self.card2_dealer, borderwidth=0)
                        self.label_card2_dealer.place(x=900, y=250)
                        dealer_points += Card1.points
                    if(dealer_card2 == 3):
                        card2_dealer = Image.open(PATH +"/img/cards/"+Card2.img_file+".png").resize((160,250))
                        self.card2_dealer = ImageTk.PhotoImage(card2_dealer)
                        self.label_card2_dealer= tkinter.Label(master=self.frame_back, image=self.card2_dealer, borderwidth=0)
                        self.label_card2_dealer.place(x=900, y=250)
                        dealer_points += Card2.points
                    if(dealer_card2 == 4):
                        card2_dealer = Image.open(PATH +"/img/cards/"+Card3.img_file+".png").resize((160,250))
                        self.card2_dealer = ImageTk.PhotoImage(card2_dealer)
                        self.label_card2_dealer= tkinter.Label(master=self.frame_back, image=self.card2_dealer, borderwidth=0)
                        self.label_card2_dealer.place(x=900, y=250)
                        dealer_points += Card3.points
                    if(dealer_card2 == 5):
                        card2_dealer = Image.open(PATH +"/img/cards/"+Card4.img_file+".png").resize((160,250))
                        self.card2_dealer = ImageTk.PhotoImage(card2_dealer)
                        self.label_card2_dealer= tkinter.Label(master=self.frame_back, image=self.card2_dealer, borderwidth=0)
                        self.label_card2_dealer.place(x=900, y=250)
                        dealer_points += Card4.points
                    if(dealer_card2 == 6):
                        card2_dealer = Image.open(PATH +"/img/cards/"+Card5.img_file+".png").resize((160,250))
                        self.card2_dealer = ImageTk.PhotoImage(card2_dealer)
                        self.label_card2_dealer= tkinter.Label(master=self.frame_back, image=self.card2_dealer, borderwidth=0)
                        self.label_card2_dealer.place(x=900, y=250)
                        dealer_points += Card5.points
                    if(dealer_card2 == 7):
                        card2_dealer = Image.open(PATH +"/img/cards/"+Card6.img_file+".png").resize((160,250))
                        self.card2_dealer = ImageTk.PhotoImage(card2_dealer)
                        self.label_card2_dealer= tkinter.Label(master=self.frame_back, image=self.card2_dealer, borderwidth=0)
                        self.label_card2_dealer.place(x=900, y=250)
                        dealer_points += Card6.points
                    if(dealer_card2 == 8):
                        card2_dealer = Image.open(PATH +"/img/cards/"+Card7.img_file+".png").resize((160,250))
                        self.card2_dealer = ImageTk.PhotoImage(card2_dealer)
                        self.label_card2_dealer= tkinter.Label(master=self.frame_back, image=self.card2_dealer, borderwidth=0)
                        self.label_card2_dealer.place(x=900, y=250)
                        dealer_points += Card7.points
                    if(dealer_card2 == 9):
                        card2_dealer = Image.open(PATH +"/img/cards/"+Card8.img_file+".png").resize((160,250))
                        self.card2_dealer = ImageTk.PhotoImage(card2_dealer)
                        self.label_card2_dealer= tkinter.Label(master=self.frame_back, image=self.card2_dealer, borderwidth=0)
                        self.label_card2_dealer.place(x=900, y=250)
                        dealer_points += Card8.points
                    if(dealer_card2 == 10):
                        card2_dealer = Image.open(PATH +"/img/cards/"+Card9.img_file+".png").resize((160,250))
                        self.card2_dealer = ImageTk.PhotoImage(card2_dealer)
                        self.label_card2_dealer= tkinter.Label(master=self.frame_back, image=self.card2_dealer, borderwidth=0)
                        self.label_card2_dealer.place(x=900, y=250)
                        dealer_points += Card9.points
                    if(dealer_card2 == 11):
                        card2_dealer = Image.open(PATH +"/img/cards/"+Card10.img_file+".png").resize((160,250))
                        self.card2_dealer = ImageTk.PhotoImage(card2_dealer)
                        self.label_card2_dealer= tkinter.Label(master=self.frame_back, image=self.card2_dealer, borderwidth=0)
                        self.label_card2_dealer.place(x=900, y=250)
                        dealer_points += Card10.points
                    if(dealer_card2 == 12):
                        card2_dealer = Image.open(PATH +"/img/cards/"+Card11.img_file+".png").resize((160,250))
                        self.card2_dealer = ImageTk.PhotoImage(card2_dealer)
                        self.label_card2_dealer= tkinter.Label(master=self.frame_back, image=self.card2_dealer, borderwidth=0)
                        self.label_card2_dealer.place(x=900, y=250)
                        dealer_points += Card11.points
                    if(dealer_card2 == 13):
                        card2_dealer = Image.open(PATH +"/img/cards/"+Card12.img_file+".png").resize((160,250))
                        self.card2_dealer = ImageTk.PhotoImage(card2_dealer)
                        self.label_card2_dealer= tkinter.Label(master=self.frame_back, image=self.card2_dealer, borderwidth=0)
                        self.label_card2_dealer.place(x=900, y=250)
                        dealer_points += Card12.points
                    if(dealer_card2 == 14):
                        card2_dealer = Image.open(PATH +"/img/cards/"+Card13.img_file+".png").resize((160,250))
                        self.card2_dealer = ImageTk.PhotoImage(card2_dealer)
                        self.label_card2_dealer= tkinter.Label(master=self.frame_back, image=self.card2_dealer, borderwidth=0)
                        self.label_card2_dealer.place(x=900, y=250)
                        dealer_points += Card13.points
                    if(dealer_card2 == 15):
                        card2_dealer = Image.open(PATH +"/img/cards/"+Card14.img_file+".png").resize((160,250))
                        self.card2_dealer = ImageTk.PhotoImage(card2_dealer)
                        self.label_card2_dealer= tkinter.Label(master=self.frame_back, image=self.card2_dealer, borderwidth=0)
                        self.label_card2_dealer.place(x=900, y=250)
                        dealer_points += Card14.points
                    if(dealer_card2 == 16):
                        card2_dealer = Image.open(PATH +"/img/cards/"+Card15.img_file+".png").resize((160,250))
                        self.card2_dealer = ImageTk.PhotoImage(card2_dealer)
                        self.label_card2_dealer= tkinter.Label(master=self.frame_back, image=self.card2_dealer, borderwidth=0)
                        self.label_card2_dealer.place(x=900, y=250)
                        dealer_points += Card15.points
                    if(dealer_card2 == 17):
                        card2_dealer = Image.open(PATH +"/img/cards/"+Card16.img_file+".png").resize((160,250))
                        self.card2_dealer = ImageTk.PhotoImage(card2_dealer)
                        self.label_card2_dealer= tkinter.Label(master=self.frame_back, image=self.card2_dealer, borderwidth=0)
                        self.label_card2_dealer.place(x=900, y=250)
                        dealer_points += Card16.points
                    if(dealer_card2 == 18):
                        card2_dealer = Image.open(PATH +"/img/cards/"+Card17.img_file+".png").resize((160,250))
                        self.card2_dealer = ImageTk.PhotoImage(card2_dealer)
                        self.label_card2_dealer= tkinter.Label(master=self.frame_back, image=self.card2_dealer, borderwidth=0)
                        self.label_card2_dealer.place(x=900, y=250)
                        dealer_points += Card17.points
                    if(dealer_card2 == 19):
                        card2_dealer = Image.open(PATH +"/img/cards/"+Card18.img_file+".png").resize((160,250))
                        self.card2_dealer = ImageTk.PhotoImage(card2_dealer)
                        self.label_card2_dealer= tkinter.Label(master=self.frame_back, image=self.card2_dealer, borderwidth=0)
                        self.label_card2_dealer.place(x=900, y=250)
                        dealer_points += Card18.points
                    if(dealer_card2 == 20):
                        card2_dealer = Image.open(PATH +"/img/cards/"+Card19.img_file+".png").resize((160,250))
                        self.card2_dealer = ImageTk.PhotoImage(card2_dealer)
                        self.label_card2_dealer= tkinter.Label(master=self.frame_back, image=self.card2_dealer, borderwidth=0)
                        self.label_card2_dealer.place(x=900, y=250)
                        dealer_points += Card19.points
                    if(dealer_card2 == 21):
                        card2_dealer = Image.open(PATH +"/img/cards/"+Card20.img_file+".png").resize((160,250))
                        self.card2_dealer = ImageTk.PhotoImage(card2_dealer)
                        self.label_card2_dealer= tkinter.Label(master=self.frame_back, image=self.card2_dealer, borderwidth=0)
                        self.label_card2_dealer.place(x=900, y=250)
                        dealer_points += Card20.points
                    if(dealer_card2 == 22):
                        card2_dealer = Image.open(PATH +"/img/cards/"+Card21.img_file+".png").resize((160,250))
                        self.card2_dealer = ImageTk.PhotoImage(card2_dealer)
                        self.label_card2_dealer= tkinter.Label(master=self.frame_back, image=self.card2_dealer, borderwidth=0)
                        self.label_card2_dealer.place(x=900, y=250)
                        dealer_points += Card21.points
                    if(dealer_card2 == 23):
                        card2_dealer = Image.open(PATH +"/img/cards/"+Card22.img_file+".png").resize((160,250))
                        self.card2_dealer = ImageTk.PhotoImage(card2_dealer)
                        self.label_card2_dealer= tkinter.Label(master=self.frame_back, image=self.card2_dealer, borderwidth=0)
                        self.label_card2_dealer.place(x=900, y=250)
                        dealer_points += Card22.points
                    if(dealer_card2 == 24):
                        card2_dealer = Image.open(PATH +"/img/cards/"+Card23.img_file+".png").resize((160,250))
                        self.card2_dealer = ImageTk.PhotoImage(card2_dealer)
                        self.label_card2_dealer= tkinter.Label(master=self.frame_back, image=self.card2_dealer, borderwidth=0)
                        self.label_card2_dealer.place(x=900, y=250)
                        dealer_points += Card23.points
                    if(dealer_card2 == 25):
                        card2_dealer = Image.open(PATH +"/img/cards/"+Card24.img_file+".png").resize((160,250))
                        self.card2_dealer = ImageTk.PhotoImage(card2_dealer)
                        self.label_card2_dealer= tkinter.Label(master=self.frame_back, image=self.card2_dealer, borderwidth=0)
                        self.label_card2_dealer.place(x=900, y=250)
                        dealer_points += Card24.points
                    if(dealer_card2 == 26):
                        card2_dealer = Image.open(PATH +"/img/cards/"+Card25.img_file+".png").resize((160,250))
                        self.card2_dealer = ImageTk.PhotoImage(card2_dealer)
                        self.label_card2_dealer= tkinter.Label(master=self.frame_back, image=self.card2_dealer, borderwidth=0)
                        self.label_card2_dealer.place(x=900, y=250)
                        dealer_points += Card25.points
                    if(dealer_card2 == 27):
                        card2_dealer = Image.open(PATH +"/img/cards/"+Card26.img_file+".png").resize((160,250))
                        self.card2_dealer = ImageTk.PhotoImage(card2_dealer)
                        self.label_card2_dealer= tkinter.Label(master=self.frame_back, image=self.card2_dealer, borderwidth=0)
                        self.label_card2_dealer.place(x=900, y=250)
                        dealer_points += Card26.points
                    if(dealer_card2 == 28):
                        card2_dealer = Image.open(PATH +"/img/cards/"+Card27.img_file+".png").resize((160,250))
                        self.card2_dealer = ImageTk.PhotoImage(card2_dealer)
                        self.label_card2_dealer= tkinter.Label(master=self.frame_back, image=self.card2_dealer, borderwidth=0)
                        self.label_card2_dealer.place(x=900, y=250)
                        dealer_points += Card27.points
                    if(dealer_card2 == 29):
                        card2_dealer = Image.open(PATH +"/img/cards/"+Card28.img_file+".png").resize((160,250))
                        self.card2_dealer = ImageTk.PhotoImage(card2_dealer)
                        self.label_card2_dealer= tkinter.Label(master=self.frame_back, image=self.card2_dealer, borderwidth=0)
                        self.label_card2_dealer.place(x=900, y=250)
                        dealer_points += Card28.points
                    if(dealer_card2 == 30):
                        card2_dealer = Image.open(PATH +"/img/cards/"+Card29.img_file+".png").resize((160,250))
                        self.card2_dealer = ImageTk.PhotoImage(card2_dealer)
                        self.label_card2_dealer= tkinter.Label(master=self.frame_back, image=self.card2_dealer, borderwidth=0)
                        self.label_card2_dealer.place(x=900, y=250)
                        dealer_points += Card29.points
                    if(dealer_card2 == 31):
                        card2_dealer = Image.open(PATH +"/img/cards/"+Card30.img_file+".png").resize((160,250))
                        self.card2_dealer = ImageTk.PhotoImage(card2_dealer)
                        self.label_card2_dealer= tkinter.Label(master=self.frame_back, image=self.card2_dealer, borderwidth=0)
                        self.label_card2_dealer.place(x=900, y=250)
                        dealer_points += Card30.points
                    if(dealer_card2 == 32):
                        card2_dealer = Image.open(PATH +"/img/cards/"+Card31.img_file+".png").resize((160,250))
                        self.card2_dealer = ImageTk.PhotoImage(card2_dealer)
                        self.label_card2_dealer= tkinter.Label(master=self.frame_back, image=self.card2_dealer, borderwidth=0)
                        self.label_card2_dealer.place(x=900, y=250)
                        dealer_points += Card31.points
                    if(dealer_card2 == 33):
                        card2_dealer = Image.open(PATH +"/img/cards/"+Card32.img_file+".png").resize((160,250))
                        self.card2_dealer = ImageTk.PhotoImage(card2_dealer)
                        self.label_card2_dealer= tkinter.Label(master=self.frame_back, image=self.card2_dealer, borderwidth=0)
                        self.label_card2_dealer.place(x=900, y=250)
                        dealer_points += Card32.points
                    if(dealer_card2 == 34):
                        card2_dealer = Image.open(PATH +"/img/cards/"+Card33.img_file+".png").resize((160,250))
                        self.card2_dealer = ImageTk.PhotoImage(card2_dealer)
                        self.label_card2_dealer= tkinter.Label(master=self.frame_back, image=self.card2_dealer, borderwidth=0)
                        self.label_card2_dealer.place(x=900, y=250)
                        dealer_points += Card33.points
                    if(dealer_card2 == 35):
                        card2_dealer = Image.open(PATH +"/img/cards/"+Card34.img_file+".png").resize((160,250))
                        self.card2_dealer = ImageTk.PhotoImage(card2_dealer)
                        self.label_card2_dealer= tkinter.Label(master=self.frame_back, image=self.card2_dealer, borderwidth=0)
                        self.label_card2_dealer.place(x=900, y=250)
                        dealer_points += Card34.points
                    if(dealer_card2 == 36):
                        card2_dealer = Image.open(PATH +"/img/cards/"+Card35.img_file+".png").resize((160,250))
                        self.card2_dealer = ImageTk.PhotoImage(card2_dealer)
                        self.label_card2_dealer= tkinter.Label(master=self.frame_back, image=self.card2_dealer, borderwidth=0)
                        self.label_card2_dealer.place(x=900, y=250)
                        dealer_points += Card35.points
                    if(dealer_card2 == 37):
                        card2_dealer = Image.open(PATH +"/img/cards/"+Card36.img_file+".png").resize((160,250))
                        self.card2_dealer = ImageTk.PhotoImage(card2_dealer)
                        self.label_card2_dealer= tkinter.Label(master=self.frame_back, image=self.card2_dealer, borderwidth=0)
                        self.label_card2_dealer.place(x=900, y=250)
                        dealer_points += Card36.points
                    if(dealer_card2 == 38):
                        card2_dealer = Image.open(PATH +"/img/cards/"+Card37.img_file+".png").resize((160,250))
                        self.card2_dealer = ImageTk.PhotoImage(card2_dealer)
                        self.label_card2_dealer= tkinter.Label(master=self.frame_back, image=self.card2_dealer, borderwidth=0)
                        self.label_card2_dealer.place(x=900, y=250)
                        dealer_points += Card37.points
                    if(dealer_card2 == 39):
                        card2_dealer = Image.open(PATH +"/img/cards/"+Card38.img_file+".png").resize((160,250))
                        self.card2_dealer = ImageTk.PhotoImage(card2_dealer)
                        self.label_card2_dealer= tkinter.Label(master=self.frame_back, image=self.card2_dealer, borderwidth=0)
                        self.label_card2_dealer.place(x=900, y=250)
                        dealer_points += Card38.points
                    if(dealer_card2 == 40):
                        card2_dealer = Image.open(PATH +"/img/cards/"+Card39.img_file+".png").resize((160,250))
                        self.card2_dealer = ImageTk.PhotoImage(card2_dealer)
                        self.label_card2_dealer= tkinter.Label(master=self.frame_back, image=self.card2_dealer, borderwidth=0)
                        self.label_card2_dealer.place(x=900, y=250)
                        dealer_points += Card39.points
                    if(dealer_card2 == 41):
                        card2_dealer = Image.open(PATH +"/img/cards/"+Card40.img_file+".png").resize((160,250))
                        self.card2_dealer = ImageTk.PhotoImage(card2_dealer)
                        self.label_card2_dealer= tkinter.Label(master=self.frame_back, image=self.card2_dealer, borderwidth=0)
                        self.label_card2_dealer.place(x=900, y=250)
                        dealer_points += Card40.points
                    if(dealer_card2 == 42):
                        card2_dealer = Image.open(PATH +"/img/cards/"+Card41.img_file+".png").resize((160,250))
                        self.card2_dealer = ImageTk.PhotoImage(card2_dealer)
                        self.label_card2_dealer= tkinter.Label(master=self.frame_back, image=self.card2_dealer, borderwidth=0)
                        self.label_card2_dealer.place(x=900, y=250)
                        dealer_points += Card41.points
                    if(dealer_card2 == 43):
                        card2_dealer = Image.open(PATH +"/img/cards/"+Card42.img_file+".png").resize((160,250))
                        self.card2_dealer = ImageTk.PhotoImage(card2_dealer)
                        self.label_card2_dealer= tkinter.Label(master=self.frame_back, image=self.card2_dealer, borderwidth=0)
                        self.label_card2_dealer.place(x=900, y=250)
                        dealer_points += Card42.points
                    if(dealer_card2 == 44):
                        card2_dealer = Image.open(PATH +"/img/cards/"+Card43.img_file+".png").resize((160,250))
                        self.card2_dealer = ImageTk.PhotoImage(card2_dealer)
                        self.label_card2_dealer= tkinter.Label(master=self.frame_back, image=self.card2_dealer, borderwidth=0)
                        self.label_card2_dealer.place(x=900, y=250)
                        dealer_points += Card43.points
                    if(dealer_card2 == 45):
                        card2_dealer = Image.open(PATH +"/img/cards/"+Card44.img_file+".png").resize((160,250))
                        self.card2_dealer = ImageTk.PhotoImage(card2_dealer)
                        self.label_card2_dealer= tkinter.Label(master=self.frame_back, image=self.card2_dealer, borderwidth=0)
                        self.label_card2_dealer.place(x=900, y=250)
                        dealer_points += Card44.points
                    if(dealer_card2 == 46):
                        card2_dealer = Image.open(PATH +"/img/cards/"+Card45.img_file+".png").resize((160,250))
                        self.card2_dealer = ImageTk.PhotoImage(card2_dealer)
                        self.label_card2_dealer= tkinter.Label(master=self.frame_back, image=self.card2_dealer, borderwidth=0)
                        self.label_card2_dealer.place(x=900, y=250)
                        dealer_points += Card45.points
                    if(dealer_card2 == 47):
                        card2_dealer = Image.open(PATH +"/img/cards/"+Card46.img_file+".png").resize((160,250))
                        self.card2_dealer = ImageTk.PhotoImage(card2_dealer)
                        self.label_card2_dealer= tkinter.Label(master=self.frame_back, image=self.card2_dealer, borderwidth=0)
                        self.label_card2_dealer.place(x=900, y=250)
                        dealer_points += Card46.points
                    if(dealer_card2 == 48):
                        card2_dealer = Image.open(PATH +"/img/cards/"+Card47.img_file+".png").resize((160,250))
                        self.card2_dealer = ImageTk.PhotoImage(card2_dealer)
                        self.label_card2_dealer= tkinter.Label(master=self.frame_back, image=self.card2_dealer, borderwidth=0)
                        self.label_card2_dealer.place(x=900, y=250)
                        dealer_points += Card47.points
                        #======== end dealer card 3
                last_draw_card +=1
                player_card2 = Game_array[last_draw_card]
                if(player_card2 == 1):
                        card2_player = Image.open(PATH +"/img/cards/"+Card0.img_file+".png").resize((160,250))
                        self.card2_player = ImageTk.PhotoImage(card2_player)
                        self.label_card2_player= tkinter.Label(master=self.frame_back, image=self.card2_player, borderwidth=0)
                        self.label_card2_player.place(x=900, y=530)
                        player_points += Card0.points
                if(player_card2 == 2):
                        card2_player = Image.open(PATH +"/img/cards/"+Card1.img_file+".png").resize((160,250))
                        self.card2_player = ImageTk.PhotoImage(card2_player)
                        self.label_card2_player= tkinter.Label(master=self.frame_back, image=self.card2_player, borderwidth=0)
                        self.label_card2_player.place(x=900, y=530)
                        player_points += Card1.points
                if(player_card2 == 3):
                        card2_player = Image.open(PATH +"/img/cards/"+Card2.img_file+".png").resize((160,250))
                        self.card2_player = ImageTk.PhotoImage(card2_player)
                        self.label_card2_player= tkinter.Label(master=self.frame_back, image=self.card2_player, borderwidth=0)
                        self.label_card2_player.place(x=900, y=530)
                        player_points += Card2.points
                if(player_card2 == 4):
                        card2_player = Image.open(PATH +"/img/cards/"+Card3.img_file+".png").resize((160,250))
                        self.card2_player = ImageTk.PhotoImage(card2_player)
                        self.label_card2_player= tkinter.Label(master=self.frame_back, image=self.card2_player, borderwidth=0)
                        self.label_card2_player.place(x=900, y=530)
                        player_points += Card3.points
                if(player_card2 == 5):
                        card2_player = Image.open(PATH +"/img/cards/"+Card4.img_file+".png").resize((160,250))
                        self.card2_player = ImageTk.PhotoImage(card2_player)
                        self.label_card2_player= tkinter.Label(master=self.frame_back, image=self.card2_player, borderwidth=0)
                        self.label_card2_player.place(x=900, y=530)
                        player_points += Card4.points
                if(player_card2 == 6):
                        card2_player = Image.open(PATH +"/img/cards/"+Card5.img_file+".png").resize((160,250))
                        self.card2_player = ImageTk.PhotoImage(card2_player)
                        self.label_card2_player= tkinter.Label(master=self.frame_back, image=self.card2_player, borderwidth=0)
                        self.label_card2_player.place(x=900, y=530)
                        player_points += Card5.points
                if(player_card2 == 7):
                        card2_player = Image.open(PATH +"/img/cards/"+Card6.img_file+".png").resize((160,250))
                        self.card2_player = ImageTk.PhotoImage(card2_player)
                        self.label_card2_player= tkinter.Label(master=self.frame_back, image=self.card2_player, borderwidth=0)
                        self.label_card2_player.place(x=900, y=530)
                        player_points += Card6.points
                if(player_card2 == 8):
                        card2_player = Image.open(PATH +"/img/cards/"+Card7.img_file+".png").resize((160,250))
                        self.card2_player = ImageTk.PhotoImage(card2_player)
                        self.label_card2_player= tkinter.Label(master=self.frame_back, image=self.card2_player, borderwidth=0)
                        self.label_card2_player.place(x=900, y=530)
                        player_points += Card7.points
                if(player_card2 == 9):
                        card2_player = Image.open(PATH +"/img/cards/"+Card8.img_file+".png").resize((160,250))
                        self.card2_player = ImageTk.PhotoImage(card2_player)
                        self.label_card2_player= tkinter.Label(master=self.frame_back, image=self.card2_player, borderwidth=0)
                        self.label_card2_player.place(x=900, y=530)
                        player_points += Card8.points
                if(player_card2 == 10):
                        card2_player = Image.open(PATH +"/img/cards/"+Card9.img_file+".png").resize((160,250))
                        self.card2_player = ImageTk.PhotoImage(card2_player)
                        self.label_card2_player= tkinter.Label(master=self.frame_back, image=self.card2_player, borderwidth=0)
                        self.label_card2_player.place(x=900, y=530)
                        player_points += Card9.points
                if(player_card2 == 11):
                        card2_player = Image.open(PATH +"/img/cards/"+Card10.img_file+".png").resize((160,250))
                        self.card2_player = ImageTk.PhotoImage(card2_player)
                        self.label_card2_player= tkinter.Label(master=self.frame_back, image=self.card2_player, borderwidth=0)
                        self.label_card2_player.place(x=900, y=530)
                        player_points += Card10.points
                if(player_card2 == 12):
                        card2_player = Image.open(PATH +"/img/cards/"+Card11.img_file+".png").resize((160,250))
                        self.card2_player = ImageTk.PhotoImage(card2_player)
                        self.label_card2_player= tkinter.Label(master=self.frame_back, image=self.card2_player, borderwidth=0)
                        self.label_card2_player.place(x=900, y=530)
                        player_points += Card11.points
                if(player_card2 == 13):
                        card2_player = Image.open(PATH +"/img/cards/"+Card12.img_file+".png").resize((160,250))
                        self.card2_player = ImageTk.PhotoImage(card2_player)
                        self.label_card2_player= tkinter.Label(master=self.frame_back, image=self.card2_player, borderwidth=0)
                        self.label_card2_player.place(x=900, y=530)
                        player_points += Card12.points
                if(player_card2 == 14):
                        card2_player = Image.open(PATH +"/img/cards/"+Card13.img_file+".png").resize((160,250))
                        self.card2_player = ImageTk.PhotoImage(card2_player)
                        self.label_card2_player= tkinter.Label(master=self.frame_back, image=self.card2_player, borderwidth=0)
                        self.label_card2_player.place(x=900, y=530)
                        player_points += Card13.points
                if(player_card2 == 15):
                        card2_player = Image.open(PATH +"/img/cards/"+Card14.img_file+".png").resize((160,250))
                        self.card2_player = ImageTk.PhotoImage(card2_player)
                        self.label_card2_player= tkinter.Label(master=self.frame_back, image=self.card2_player, borderwidth=0)
                        self.label_card2_player.place(x=900, y=530)
                        player_points += Card14.points
                if(player_card2 == 16):
                        card2_player = Image.open(PATH +"/img/cards/"+Card15.img_file+".png").resize((160,250))
                        self.card2_player = ImageTk.PhotoImage(card2_player)
                        self.label_card2_player= tkinter.Label(master=self.frame_back, image=self.card2_player, borderwidth=0)
                        self.label_card2_player.place(x=900, y=530)
                        player_points += Card15.points
                if(player_card2 == 17):
                        card2_player = Image.open(PATH +"/img/cards/"+Card16.img_file+".png").resize((160,250))
                        self.card2_player = ImageTk.PhotoImage(card2_player)
                        self.label_card2_player= tkinter.Label(master=self.frame_back, image=self.card2_player, borderwidth=0)
                        self.label_card2_player.place(x=900, y=530)
                        player_points += Card16.points
                if(player_card2 == 18):
                        card2_player = Image.open(PATH +"/img/cards/"+Card17.img_file+".png").resize((160,250))
                        self.card2_player = ImageTk.PhotoImage(card2_player)
                        self.label_card2_player= tkinter.Label(master=self.frame_back, image=self.card2_player, borderwidth=0)
                        self.label_card2_player.place(x=900, y=530)
                        player_points += Card17.points
                if(player_card2 == 19):
                        card2_player = Image.open(PATH +"/img/cards/"+Card18.img_file+".png").resize((160,250))
                        self.card2_player = ImageTk.PhotoImage(card2_player)
                        self.label_card2_player= tkinter.Label(master=self.frame_back, image=self.card2_player, borderwidth=0)
                        self.label_card2_player.place(x=900, y=530)
                        player_points += Card18.points
                if(player_card2 == 20):
                        card2_player = Image.open(PATH +"/img/cards/"+Card19.img_file+".png").resize((160,250))
                        self.card2_player = ImageTk.PhotoImage(card2_player)
                        self.label_card2_player= tkinter.Label(master=self.frame_back, image=self.card2_player, borderwidth=0)
                        self.label_card2_player.place(x=900, y=530)
                        player_points += Card19.points
                if(player_card2 == 21):
                        card2_player = Image.open(PATH +"/img/cards/"+Card20.img_file+".png").resize((160,250))
                        self.card2_player = ImageTk.PhotoImage(card2_player)
                        self.label_card2_player= tkinter.Label(master=self.frame_back, image=self.card2_player, borderwidth=0)
                        self.label_card2_player.place(x=900, y=530)
                        player_points += Card20.points
                if(player_card2 == 22):
                        card2_player = Image.open(PATH +"/img/cards/"+Card21.img_file+".png").resize((160,250))
                        self.card2_player = ImageTk.PhotoImage(card2_player)
                        self.label_card2_player= tkinter.Label(master=self.frame_back, image=self.card2_player, borderwidth=0)
                        self.label_card2_player.place(x=900, y=530)
                        player_points += Card21.points
                if(player_card2 == 23):
                        card2_player = Image.open(PATH +"/img/cards/"+Card22.img_file+".png").resize((160,250))
                        self.card2_player = ImageTk.PhotoImage(card2_player)
                        self.label_card2_player= tkinter.Label(master=self.frame_back, image=self.card2_player, borderwidth=0)
                        self.label_card2_player.place(x=900, y=530)
                        player_points += Card22.points
                if(player_card2 == 24):
                        card2_player = Image.open(PATH +"/img/cards/"+Card23.img_file+".png").resize((160,250))
                        self.card2_player = ImageTk.PhotoImage(card2_player)
                        self.label_card2_player= tkinter.Label(master=self.frame_back, image=self.card2_player, borderwidth=0)
                        self.label_card2_player.place(x=900, y=530)
                        player_points += Card23.points
                if(player_card2 == 25):
                        card2_player = Image.open(PATH +"/img/cards/"+Card24.img_file+".png").resize((160,250))
                        self.card2_player = ImageTk.PhotoImage(card2_player)
                        self.label_card2_player= tkinter.Label(master=self.frame_back, image=self.card2_player, borderwidth=0)
                        self.label_card2_player.place(x=900, y=530)
                        player_points += Card24.points
                if(player_card2 == 26):
                        card2_player = Image.open(PATH +"/img/cards/"+Card25.img_file+".png").resize((160,250))
                        self.card2_player = ImageTk.PhotoImage(card2_player)
                        self.label_card2_player= tkinter.Label(master=self.frame_back, image=self.card2_player, borderwidth=0)
                        self.label_card2_player.place(x=900, y=530)
                        player_points += Card25.points
                if(player_card2 == 27):
                        card2_player = Image.open(PATH +"/img/cards/"+Card26.img_file+".png").resize((160,250))
                        self.card2_player = ImageTk.PhotoImage(card2_player)
                        self.label_card2_player= tkinter.Label(master=self.frame_back, image=self.card2_player, borderwidth=0)
                        self.label_card2_player.place(x=900, y=530)
                        player_points += Card26.points
                if(player_card2 == 28):
                        card2_player = Image.open(PATH +"/img/cards/"+Card27.img_file+".png").resize((160,250))
                        self.card2_player = ImageTk.PhotoImage(card2_player)
                        self.label_card2_player= tkinter.Label(master=self.frame_back, image=self.card2_player, borderwidth=0)
                        self.label_card2_player.place(x=900, y=530)
                        player_points += Card27.points
                if(player_card2 == 29):
                        card2_player = Image.open(PATH +"/img/cards/"+Card28.img_file+".png").resize((160,250))
                        self.card2_player = ImageTk.PhotoImage(card2_player)
                        self.label_card2_player= tkinter.Label(master=self.frame_back, image=self.card2_player, borderwidth=0)
                        self.label_card2_player.place(x=900, y=530)
                        player_points += Card28.points
                if(player_card2 == 30):
                        card2_player = Image.open(PATH +"/img/cards/"+Card29.img_file+".png").resize((160,250))
                        self.card2_player = ImageTk.PhotoImage(card2_player)
                        self.label_card2_player= tkinter.Label(master=self.frame_back, image=self.card2_player, borderwidth=0)
                        self.label_card2_player.place(x=900, y=530)
                        player_points += Card29.points
                if(player_card2 == 31):
                        card2_player = Image.open(PATH +"/img/cards/"+Card30.img_file+".png").resize((160,250))
                        self.card2_player = ImageTk.PhotoImage(card2_player)
                        self.label_card2_player= tkinter.Label(master=self.frame_back, image=self.card2_player, borderwidth=0)
                        self.label_card2_player.place(x=900, y=530)
                        player_points += Card30.points
                if(player_card2 == 32):
                        card2_player = Image.open(PATH +"/img/cards/"+Card31.img_file+".png").resize((160,250))
                        self.card2_player = ImageTk.PhotoImage(card2_player)
                        self.label_card2_player= tkinter.Label(master=self.frame_back, image=self.card2_player, borderwidth=0)
                        self.label_card2_player.place(x=900, y=530)
                        player_points += Card31.points
                if(player_card2 == 33):
                        card2_player = Image.open(PATH +"/img/cards/"+Card32.img_file+".png").resize((160,250))
                        self.card2_player = ImageTk.PhotoImage(card2_player)
                        self.label_card2_player= tkinter.Label(master=self.frame_back, image=self.card2_player, borderwidth=0)
                        self.label_card2_player.place(x=900, y=530)
                        player_points += Card32.points
                if(player_card2 == 34):
                        card2_player = Image.open(PATH +"/img/cards/"+Card33.img_file+".png").resize((160,250))
                        self.card2_player = ImageTk.PhotoImage(card2_player)
                        self.label_card2_player= tkinter.Label(master=self.frame_back, image=self.card2_player, borderwidth=0)
                        self.label_card2_player.place(x=900, y=530)
                        player_points += Card33.points
                if(player_card2 == 35):
                        card2_player = Image.open(PATH +"/img/cards/"+Card34.img_file+".png").resize((160,250))
                        self.card2_player = ImageTk.PhotoImage(card2_player)
                        self.label_card2_player= tkinter.Label(master=self.frame_back, image=self.card2_player, borderwidth=0)
                        self.label_card2_player.place(x=900, y=530)
                        player_points += Card34.points
                if(player_card2 == 36):
                        card2_player = Image.open(PATH +"/img/cards/"+Card35.img_file+".png").resize((160,250))
                        self.card2_player = ImageTk.PhotoImage(card2_player)
                        self.label_card2_player= tkinter.Label(master=self.frame_back, image=self.card2_player, borderwidth=0)
                        self.label_card2_player.place(x=900, y=530)
                        player_points += Card35.points
                if(player_card2 == 37):
                        card2_player = Image.open(PATH +"/img/cards/"+Card36.img_file+".png").resize((160,250))
                        self.card2_player = ImageTk.PhotoImage(card2_player)
                        self.label_card2_player= tkinter.Label(master=self.frame_back, image=self.card2_player, borderwidth=0)
                        self.label_card2_player.place(x=900, y=530)
                        player_points += Card36.points
                if(player_card2 == 38):
                        card2_player = Image.open(PATH +"/img/cards/"+Card37.img_file+".png").resize((160,250))
                        self.card2_player = ImageTk.PhotoImage(card2_player)
                        self.label_card2_player= tkinter.Label(master=self.frame_back, image=self.card2_player, borderwidth=0)
                        self.label_card2_player.place(x=900, y=530)
                        player_points += Card37.points
                if(player_card2 == 39):
                        card2_player = Image.open(PATH +"/img/cards/"+Card38.img_file+".png").resize((160,250))
                        self.card2_player = ImageTk.PhotoImage(card2_player)
                        self.label_card2_player= tkinter.Label(master=self.frame_back, image=self.card2_player, borderwidth=0)
                        self.label_card2_player.place(x=900, y=530)
                        player_points += Card38.points
                if(player_card2 == 40):
                        card2_player = Image.open(PATH +"/img/cards/"+Card39.img_file+".png").resize((160,250))
                        self.card2_player = ImageTk.PhotoImage(card2_player)
                        self.label_card2_player= tkinter.Label(master=self.frame_back, image=self.card2_player, borderwidth=0)
                        self.label_card2_player.place(x=900, y=530)
                        player_points += Card39.points
                if(player_card2 == 41):
                        card2_player = Image.open(PATH +"/img/cards/"+Card40.img_file+".png").resize((160,250))
                        self.card2_player = ImageTk.PhotoImage(card2_player)
                        self.label_card2_player= tkinter.Label(master=self.frame_back, image=self.card2_player, borderwidth=0)
                        self.label_card2_player.place(x=900, y=530)
                        player_points += Card40.points
                if(player_card2 == 42):
                        card2_player = Image.open(PATH +"/img/cards/"+Card41.img_file+".png").resize((160,250))
                        self.card2_player = ImageTk.PhotoImage(card2_player)
                        self.label_card2_player= tkinter.Label(master=self.frame_back, image=self.card2_player, borderwidth=0)
                        self.label_card2_player.place(x=900, y=530)
                        player_points += Card41.points
                if(player_card2 == 43):
                        card2_player = Image.open(PATH +"/img/cards/"+Card42.img_file+".png").resize((160,250))
                        self.card2_player = ImageTk.PhotoImage(card2_player)
                        self.label_card2_player= tkinter.Label(master=self.frame_back, image=self.card2_player, borderwidth=0)
                        self.label_card2_player.place(x=900, y=530)
                        player_points += Card42.points
                if(player_card2 == 44):
                        card2_player = Image.open(PATH +"/img/cards/"+Card43.img_file+".png").resize((160,250))
                        self.card2_player = ImageTk.PhotoImage(card2_player)
                        self.label_card2_player= tkinter.Label(master=self.frame_back, image=self.card2_player, borderwidth=0)
                        self.label_card2_player.place(x=900, y=530)
                        player_points += Card43.points
                if(player_card2 == 45):
                        card2_player = Image.open(PATH +"/img/cards/"+Card44.img_file+".png").resize((160,250))
                        self.card2_player = ImageTk.PhotoImage(card2_player)
                        self.label_card2_player= tkinter.Label(master=self.frame_back, image=self.card2_player, borderwidth=0)
                        self.label_card2_player.place(x=900, y=530)
                        player_points += Card44.points
                if(player_card2 == 46):
                        card2_player = Image.open(PATH +"/img/cards/"+Card45.img_file+".png").resize((160,250))
                        self.card2_player = ImageTk.PhotoImage(card2_player)
                        self.label_card2_player= tkinter.Label(master=self.frame_back, image=self.card2_player, borderwidth=0)
                        self.label_card2_player.place(x=900, y=530)
                        player_points += Card45.points
                if(player_card2 == 47):
                        card2_player = Image.open(PATH +"/img/cards/"+Card46.img_file+".png").resize((160,250))
                        self.card2_player = ImageTk.PhotoImage(card2_player)
                        self.label_card2_player= tkinter.Label(master=self.frame_back, image=self.card2_player, borderwidth=0)
                        self.label_card2_player.place(x=900, y=530)
                        player_points += Card46.points
                if(player_card2 == 48):
                        card2_player = Image.open(PATH +"/img/cards/"+Card47.img_file+".png").resize((160,250))
                        self.card2_player = ImageTk.PhotoImage(card2_player)
                        self.label_card2_player= tkinter.Label(master=self.frame_back, image=self.card2_player, borderwidth=0)
                        self.label_card2_player.place(x=900, y=530)
                        player_points += Card47.points
            if(index_card == 3):                
                if(dealer_points<16):
                    last_draw_card +=1
                    dealer_card3 = Game_array [last_draw_card]
                    if(dealer_card3 == 1):
                        card3_dealer = Image.open(PATH +"/img/cards/"+Card0.img_file+".png").resize((160,250))
                        self.card3_dealer = ImageTk.PhotoImage(card3_dealer)
                        self.label_card3_dealer= tkinter.Label(master=self.frame_back, image=self.card3_dealer, borderwidth=0)
                        self.label_card3_dealer.place(x=1100, y=250)
                        dealer_points += Card0.points
                    if(dealer_card3 == 2):
                        card3_dealer = Image.open(PATH +"/img/cards/"+Card1.img_file+".png").resize((160,250))
                        self.card3_dealer = ImageTk.PhotoImage(card3_dealer)
                        self.label_card3_dealer= tkinter.Label(master=self.frame_back, image=self.card3_dealer, borderwidth=0)
                        self.label_card3_dealer.place(x=1100, y=250)
                        dealer_points += Card1.points
                    if(dealer_card3 == 3):
                        card3_dealer = Image.open(PATH +"/img/cards/"+Card2.img_file+".png").resize((160,250))
                        self.card3_dealer = ImageTk.PhotoImage(card3_dealer)
                        self.label_card3_dealer= tkinter.Label(master=self.frame_back, image=self.card3_dealer, borderwidth=0)
                        self.label_card3_dealer.place(x=1100, y=250)
                        dealer_points += Card2.points
                    if(dealer_card3 == 4):
                        card3_dealer = Image.open(PATH +"/img/cards/"+Card3.img_file+".png").resize((160,250))
                        self.card3_dealer = ImageTk.PhotoImage(card3_dealer)
                        self.label_card3_dealer= tkinter.Label(master=self.frame_back, image=self.card3_dealer, borderwidth=0)
                        self.label_card3_dealer.place(x=1100, y=250)
                        dealer_points += Card3.points
                    if(dealer_card3 == 5):
                        card3_dealer = Image.open(PATH +"/img/cards/"+Card4.img_file+".png").resize((160,250))
                        self.card3_dealer = ImageTk.PhotoImage(card3_dealer)
                        self.label_card3_dealer= tkinter.Label(master=self.frame_back, image=self.card3_dealer, borderwidth=0)
                        self.label_card3_dealer.place(x=1100, y=250)
                        dealer_points += Card4.points
                    if(dealer_card3 == 6):
                        card3_dealer = Image.open(PATH +"/img/cards/"+Card5.img_file+".png").resize((160,250))
                        self.card3_dealer = ImageTk.PhotoImage(card3_dealer)
                        self.label_card3_dealer= tkinter.Label(master=self.frame_back, image=self.card3_dealer, borderwidth=0)
                        self.label_card3_dealer.place(x=1100, y=250)
                        dealer_points += Card5.points
                    if(dealer_card3 == 7):
                        card3_dealer = Image.open(PATH +"/img/cards/"+Card6.img_file+".png").resize((160,250))
                        self.card3_dealer = ImageTk.PhotoImage(card3_dealer)
                        self.label_card3_dealer= tkinter.Label(master=self.frame_back, image=self.card3_dealer, borderwidth=0)
                        self.label_card3_dealer.place(x=1100, y=250)
                        dealer_points += Card6.points
                    if(dealer_card3 == 8):
                        card3_dealer = Image.open(PATH +"/img/cards/"+Card7.img_file+".png").resize((160,250))
                        self.card3_dealer = ImageTk.PhotoImage(card3_dealer)
                        self.label_card3_dealer= tkinter.Label(master=self.frame_back, image=self.card3_dealer, borderwidth=0)
                        self.label_card3_dealer.place(x=1100, y=250)
                        dealer_points += Card7.points
                    if(dealer_card3 == 9):
                        card3_dealer = Image.open(PATH +"/img/cards/"+Card8.img_file+".png").resize((160,250))
                        self.card3_dealer = ImageTk.PhotoImage(card3_dealer)
                        self.label_card3_dealer= tkinter.Label(master=self.frame_back, image=self.card3_dealer, borderwidth=0)
                        self.label_card3_dealer.place(x=1100, y=250)
                        dealer_points += Card8.points
                    if(dealer_card3 == 10):
                        card3_dealer = Image.open(PATH +"/img/cards/"+Card9.img_file+".png").resize((160,250))
                        self.card3_dealer = ImageTk.PhotoImage(card3_dealer)
                        self.label_card3_dealer= tkinter.Label(master=self.frame_back, image=self.card3_dealer, borderwidth=0)
                        self.label_card3_dealer.place(x=1100, y=250)
                        dealer_points += Card9.points
                    if(dealer_card3 == 11):
                        card3_dealer = Image.open(PATH +"/img/cards/"+Card10.img_file+".png").resize((160,250))
                        self.card3_dealer = ImageTk.PhotoImage(card3_dealer)
                        self.label_card3_dealer= tkinter.Label(master=self.frame_back, image=self.card3_dealer, borderwidth=0)
                        self.label_card3_dealer.place(x=1100, y=250)
                        dealer_points += Card10.points
                    if(dealer_card3 == 12):
                        card3_dealer = Image.open(PATH +"/img/cards/"+Card11.img_file+".png").resize((160,250))
                        self.card3_dealer = ImageTk.PhotoImage(card3_dealer)
                        self.label_card3_dealer= tkinter.Label(master=self.frame_back, image=self.card3_dealer, borderwidth=0)
                        self.label_card3_dealer.place(x=1100, y=250)
                        dealer_points += Card11.points
                    if(dealer_card3 == 13):
                        card3_dealer = Image.open(PATH +"/img/cards/"+Card12.img_file+".png").resize((160,250))
                        self.card3_dealer = ImageTk.PhotoImage(card3_dealer)
                        self.label_card3_dealer= tkinter.Label(master=self.frame_back, image=self.card3_dealer, borderwidth=0)
                        self.label_card3_dealer.place(x=1100, y=250)
                        dealer_points += Card12.points
                    if(dealer_card3 == 14):
                        card3_dealer = Image.open(PATH +"/img/cards/"+Card13.img_file+".png").resize((160,250))
                        self.card3_dealer = ImageTk.PhotoImage(card3_dealer)
                        self.label_card3_dealer= tkinter.Label(master=self.frame_back, image=self.card3_dealer, borderwidth=0)
                        self.label_card3_dealer.place(x=1100, y=250)
                        dealer_points += Card13.points
                    if(dealer_card3 == 15):
                        card3_dealer = Image.open(PATH +"/img/cards/"+Card14.img_file+".png").resize((160,250))
                        self.card3_dealer = ImageTk.PhotoImage(card3_dealer)
                        self.label_card3_dealer= tkinter.Label(master=self.frame_back, image=self.card3_dealer, borderwidth=0)
                        self.label_card3_dealer.place(x=1100, y=250)
                        dealer_points += Card14.points
                    if(dealer_card3 == 16):
                        card3_dealer = Image.open(PATH +"/img/cards/"+Card15.img_file+".png").resize((160,250))
                        self.card3_dealer = ImageTk.PhotoImage(card3_dealer)
                        self.label_card3_dealer= tkinter.Label(master=self.frame_back, image=self.card3_dealer, borderwidth=0)
                        self.label_card3_dealer.place(x=1100, y=250)
                        dealer_points += Card15.points
                    if(dealer_card3 == 17):
                        card3_dealer = Image.open(PATH +"/img/cards/"+Card16.img_file+".png").resize((160,250))
                        self.card3_dealer = ImageTk.PhotoImage(card3_dealer)
                        self.label_card3_dealer= tkinter.Label(master=self.frame_back, image=self.card3_dealer, borderwidth=0)
                        self.label_card3_dealer.place(x=1100, y=250)
                        dealer_points += Card16.points
                    if(dealer_card3 == 18):
                        card3_dealer = Image.open(PATH +"/img/cards/"+Card17.img_file+".png").resize((160,250))
                        self.card3_dealer = ImageTk.PhotoImage(card3_dealer)
                        self.label_card3_dealer= tkinter.Label(master=self.frame_back, image=self.card3_dealer, borderwidth=0)
                        self.label_card3_dealer.place(x=1100, y=250)
                        dealer_points += Card17.points
                    if(dealer_card3 == 19):
                        card3_dealer = Image.open(PATH +"/img/cards/"+Card18.img_file+".png").resize((160,250))
                        self.card3_dealer = ImageTk.PhotoImage(card3_dealer)
                        self.label_card3_dealer= tkinter.Label(master=self.frame_back, image=self.card3_dealer, borderwidth=0)
                        self.label_card3_dealer.place(x=1100, y=250)
                        dealer_points += Card18.points
                    if(dealer_card3 == 20):
                        card3_dealer = Image.open(PATH +"/img/cards/"+Card19.img_file+".png").resize((160,250))
                        self.card3_dealer = ImageTk.PhotoImage(card3_dealer)
                        self.label_card3_dealer= tkinter.Label(master=self.frame_back, image=self.card3_dealer, borderwidth=0)
                        self.label_card3_dealer.place(x=1100, y=250)
                        dealer_points += Card19.points
                    if(dealer_card3 == 21):
                        card3_dealer = Image.open(PATH +"/img/cards/"+Card20.img_file+".png").resize((160,250))
                        self.card3_dealer = ImageTk.PhotoImage(card3_dealer)
                        self.label_card3_dealer= tkinter.Label(master=self.frame_back, image=self.card3_dealer, borderwidth=0)
                        self.label_card3_dealer.place(x=1100, y=250)
                        dealer_points += Card20.points
                    if(dealer_card3 == 22):
                        card2_dealer = Image.open(PATH +"/img/cards/"+Card21.img_file+".png").resize((160,250))
                        self.card2_dealer = ImageTk.PhotoImage(card3_dealer)
                        self.label_card3_dealer= tkinter.Label(master=self.frame_back, image=self.card2_dealer, borderwidth=0)
                        self.label_card3_dealer.place(x=1100, y=250)
                        dealer_points += Card21.points
                    if(dealer_card3 == 23):
                        card3_dealer = Image.open(PATH +"/img/cards/"+Card22.img_file+".png").resize((160,250))
                        self.card3_dealer = ImageTk.PhotoImage(card3_dealer)
                        self.label_card3_dealer= tkinter.Label(master=self.frame_back, image=self.card3_dealer, borderwidth=0)
                        self.label_card3_dealer.place(x=1100, y=250)
                        dealer_points += Card22.points
                    if(dealer_card3 == 24):
                        card3_dealer = Image.open(PATH +"/img/cards/"+Card23.img_file+".png").resize((160,250))
                        self.card3_dealer = ImageTk.PhotoImage(card3_dealer)
                        self.label_card3_dealer= tkinter.Label(master=self.frame_back, image=self.card3_dealer, borderwidth=0)
                        self.label_card3_dealer.place(x=1100, y=250)
                        dealer_points += Card23.points
                    if(dealer_card3 == 25):
                        card3_dealer = Image.open(PATH +"/img/cards/"+Card24.img_file+".png").resize((160,250))
                        self.card3_dealer = ImageTk.PhotoImage(card3_dealer)
                        self.label_card3_dealer= tkinter.Label(master=self.frame_back, image=self.card3_dealer, borderwidth=0)
                        self.label_card3_dealer.place(x=1100, y=250)
                        dealer_points += Card24.points
                    if(dealer_card3 == 26):
                        card3_dealer = Image.open(PATH +"/img/cards/"+Card25.img_file+".png").resize((160,250))
                        self.card3_dealer = ImageTk.PhotoImage(card3_dealer)
                        self.label_card3_dealer= tkinter.Label(master=self.frame_back, image=self.card3_dealer, borderwidth=0)
                        self.label_card3_dealer.place(x=1100, y=250)
                        dealer_points += Card25.points
                    if(dealer_card3 == 27):
                        card3_dealer = Image.open(PATH +"/img/cards/"+Card26.img_file+".png").resize((160,250))
                        self.card3_dealer = ImageTk.PhotoImage(card3_dealer)
                        self.label_card3_dealer= tkinter.Label(master=self.frame_back, image=self.card3_dealer, borderwidth=0)
                        self.label_card3_dealer.place(x=1100, y=250)
                        dealer_points += Card26.points
                    if(dealer_card3 == 28):
                        card3_dealer = Image.open(PATH +"/img/cards/"+Card27.img_file+".png").resize((160,250))
                        self.card3_dealer = ImageTk.PhotoImage(card3_dealer)
                        self.label_card3_dealer= tkinter.Label(master=self.frame_back, image=self.card3_dealer, borderwidth=0)
                        self.label_card3_dealer.place(x=1100, y=250)
                        dealer_points += Card27.points
                    if(dealer_card3 == 29):
                        card2_dealer = Image.open(PATH +"/img/cards/"+Card28.img_file+".png").resize((160,250))
                        self.card2_dealer = ImageTk.PhotoImage(card3_dealer)
                        self.label_card3_dealer= tkinter.Label(master=self.frame_back, image=self.card2_dealer, borderwidth=0)
                        self.label_card3_dealer.place(x=1100, y=250)
                        dealer_points += Card28.points
                    if(dealer_card3 == 30):
                        card3_dealer = Image.open(PATH +"/img/cards/"+Card29.img_file+".png").resize((160,250))
                        self.card3_dealer = ImageTk.PhotoImage(card3_dealer)
                        self.label_card3_dealer= tkinter.Label(master=self.frame_back, image=self.card3_dealer, borderwidth=0)
                        self.label_card3_dealer.place(x=1100, y=250)
                        dealer_points += Card29.points
                    if(dealer_card3 == 31):
                        card3_dealer = Image.open(PATH +"/img/cards/"+Card30.img_file+".png").resize((160,250))
                        self.card3_dealer = ImageTk.PhotoImage(card3_dealer)
                        self.label_card3_dealer= tkinter.Label(master=self.frame_back, image=self.card3_dealer, borderwidth=0)
                        self.label_card3_dealer.place(x=1100, y=250)
                        dealer_points += Card30.points
                    if(dealer_card3 == 32):
                        card3_dealer = Image.open(PATH +"/img/cards/"+Card31.img_file+".png").resize((160,250))
                        self.card3_dealer = ImageTk.PhotoImage(card3_dealer)
                        self.label_card3_dealer= tkinter.Label(master=self.frame_back, image=self.card3_dealer, borderwidth=0)
                        self.label_card3_dealer.place(x=1100, y=250)
                        dealer_points += Card31.points
                    if(dealer_card3 == 33):
                        card3_dealer = Image.open(PATH +"/img/cards/"+Card32.img_file+".png").resize((160,250))
                        self.card3_dealer = ImageTk.PhotoImage(card3_dealer)
                        self.label_card3_dealer= tkinter.Label(master=self.frame_back, image=self.card3_dealer, borderwidth=0)
                        self.label_card3_dealer.place(x=1100, y=250)
                        dealer_points += Card32.points
                    if(dealer_card3 == 34):
                        card3_dealer = Image.open(PATH +"/img/cards/"+Card33.img_file+".png").resize((160,250))
                        self.card3_dealer = ImageTk.PhotoImage(card3_dealer)
                        self.label_card3_dealer= tkinter.Label(master=self.frame_back, image=self.card3_dealer, borderwidth=0)
                        self.label_card3_dealer.place(x=1100, y=250)
                        dealer_points += Card33.points
                    if(dealer_card3 == 35):
                        card3_dealer = Image.open(PATH +"/img/cards/"+Card34.img_file+".png").resize((160,250))
                        self.card3_dealer = ImageTk.PhotoImage(card3_dealer)
                        self.label_card3_dealer= tkinter.Label(master=self.frame_back, image=self.card3_dealer, borderwidth=0)
                        self.label_card3_dealer.place(x=1100, y=250)
                        dealer_points += Card34.points
                    if(dealer_card3 == 36):
                        card3_dealer = Image.open(PATH +"/img/cards/"+Card35.img_file+".png").resize((160,250))
                        self.card3_dealer = ImageTk.PhotoImage(card3_dealer)
                        self.label_card3_dealer= tkinter.Label(master=self.frame_back, image=self.card3_dealer, borderwidth=0)
                        self.label_card3_dealer.place(x=1100, y=250)
                        dealer_points += Card35.points
                    if(dealer_card3 == 37):
                        card3_dealer = Image.open(PATH +"/img/cards/"+Card36.img_file+".png").resize((160,250))
                        self.card3_dealer = ImageTk.PhotoImage(card3_dealer)
                        self.label_card3_dealer= tkinter.Label(master=self.frame_back, image=self.card3_dealer, borderwidth=0)
                        self.label_card3_dealer.place(x=1100, y=250)
                        dealer_points += Card36.points
                    if(dealer_card3 == 38):
                        card3_dealer = Image.open(PATH +"/img/cards/"+Card37.img_file+".png").resize((160,250))
                        self.card3_dealer = ImageTk.PhotoImage(card3_dealer)
                        self.label_card3_dealer= tkinter.Label(master=self.frame_back, image=self.card3_dealer, borderwidth=0)
                        self.label_card3_dealer.place(x=1100, y=250)
                        dealer_points += Card37.points
                    if(dealer_card3 == 39):
                        card3_dealer = Image.open(PATH +"/img/cards/"+Card38.img_file+".png").resize((160,250))
                        self.card3_dealer = ImageTk.PhotoImage(card3_dealer)
                        self.label_card3_dealer= tkinter.Label(master=self.frame_back, image=self.card3_dealer, borderwidth=0)
                        self.label_card3_dealer.place(x=1100, y=250)
                        dealer_points += Card38.points
                    if(dealer_card3 == 40):
                        card2_dealer = Image.open(PATH +"/img/cards/"+Card39.img_file+".png").resize((160,250))
                        self.card2_dealer = ImageTk.PhotoImage(card3_dealer)
                        self.label_card3_dealer= tkinter.Label(master=self.frame_back, image=self.card2_dealer, borderwidth=0)
                        self.label_card3_dealer.place(x=1100, y=250)
                        dealer_points += Card39.points
                    if(dealer_card3 == 41):
                        card3_dealer = Image.open(PATH +"/img/cards/"+Card40.img_file+".png").resize((160,250))
                        self.card3_dealer = ImageTk.PhotoImage(card3_dealer)
                        self.label_card3_dealer= tkinter.Label(master=self.frame_back, image=self.card3_dealer, borderwidth=0)
                        self.label_card3_dealer.place(x=1100, y=250)
                        dealer_points += Card40.points
                    if(dealer_card3 == 42):
                        card3_dealer = Image.open(PATH +"/img/cards/"+Card41.img_file+".png").resize((160,250))
                        self.card3_dealer = ImageTk.PhotoImage(card2_dealer)
                        self.label_card3_dealer= tkinter.Label(master=self.frame_back, image=self.card3_dealer, borderwidth=0)
                        self.label_card3_dealer.place(x=1100, y=250)
                        dealer_points += Card41.points
                    if(dealer_card3 == 43):
                        card3_dealer = Image.open(PATH +"/img/cards/"+Card42.img_file+".png").resize((160,250))
                        self.card3_dealer = ImageTk.PhotoImage(card3_dealer)
                        self.label_card3_dealer= tkinter.Label(master=self.frame_back, image=self.card3_dealer, borderwidth=0)
                        self.label_card3_dealer.place(x=1100, y=250)
                        dealer_points += Card42.points
                    if(dealer_card3 == 44):
                        card3_dealer = Image.open(PATH +"/img/cards/"+Card43.img_file+".png").resize((160,250))
                        self.card3_dealer = ImageTk.PhotoImage(card3_dealer)
                        self.label_card3_dealer= tkinter.Label(master=self.frame_back, image=self.card3_dealer, borderwidth=0)
                        self.label_card3_dealer.place(x=1100, y=250)
                        dealer_points += Card43.points
                    if(dealer_card3 == 45):
                        card3_dealer = Image.open(PATH +"/img/cards/"+Card44.img_file+".png").resize((160,250))
                        self.card3_dealer = ImageTk.PhotoImage(card3_dealer)
                        self.label_card3_dealer= tkinter.Label(master=self.frame_back, image=self.card2_dealer, borderwidth=0)
                        self.label_card3_dealer.place(x=1100, y=250)
                        dealer_points += Card44.points
                    if(dealer_card3 == 46):
                        card3_dealer = Image.open(PATH +"/img/cards/"+Card45.img_file+".png").resize((160,250))
                        self.card3_dealer = ImageTk.PhotoImage(card3_dealer)
                        self.label_card3_dealer= tkinter.Label(master=self.frame_back, image=self.card3_dealer, borderwidth=0)
                        self.label_card3_dealer.place(x=1100, y=250)
                        dealer_points += Card45.points
                    if(dealer_card3 == 47):
                        card3_dealer = Image.open(PATH +"/img/cards/"+Card46.img_file+".png").resize((160,250))
                        self.card3_dealer = ImageTk.PhotoImage(card3_dealer)
                        self.label_card3_dealer= tkinter.Label(master=self.frame_back, image=self.card3_dealer, borderwidth=0)
                        self.label_card3_dealer.place(x=1100, y=250)
                        dealer_points += Card46.points
                    if(dealer_card3 == 48):
                        card3_dealer = Image.open(PATH +"/img/cards/"+Card47.img_file+".png").resize((160,250))
                        self.card3_dealer = ImageTk.PhotoImage(card3_dealer)
                        self.label_card3_dealer= tkinter.Label(master=self.frame_back, image=self.card3_dealer, borderwidth=0)
                        self.label_card3_dealer.place(x=1100, y=250)
                        dealer_points += Card47.points
                        #======== end dealer card 3
                last_draw_card +=1
                player_card3 = Game_array[last_draw_card]
                if(player_card3 == 1):
                        card3_player = Image.open(PATH +"/img/cards/"+Card0.img_file+".png").resize((160,250))
                        self.card3_player = ImageTk.PhotoImage(card3_player)
                        self.label_card3_player= tkinter.Label(master=self.frame_back, image=self.card3_player, borderwidth=0)
                        self.label_card3_player.place(x=1100, y=530)
                        player_points += Card0.points
                if(player_card3 == 2):
                        card3_player = Image.open(PATH +"/img/cards/"+Card1.img_file+".png").resize((160,250))
                        self.card3_player = ImageTk.PhotoImage(card3_player)
                        self.label_card3_player= tkinter.Label(master=self.frame_back, image=self.card3_player, borderwidth=0)
                        self.label_card3_player.place(x=1100, y=530)
                        player_points += Card1.points
                if(player_card3 == 3):
                        card3_player = Image.open(PATH +"/img/cards/"+Card2.img_file+".png").resize((160,250))
                        self.card3_player = ImageTk.PhotoImage(card3_player)
                        self.label_card3_player= tkinter.Label(master=self.frame_back, image=self.card3_player, borderwidth=0)
                        self.label_card3_player.place(x=1100, y=530)
                        player_points += Card2.points
                if(player_card3 == 4):
                        card3_player = Image.open(PATH +"/img/cards/"+Card3.img_file+".png").resize((160,250))
                        self.card3_player = ImageTk.PhotoImage(card3_player)
                        self.label_card3_player= tkinter.Label(master=self.frame_back, image=self.card3_player, borderwidth=0)
                        self.label_card3_player.place(x=1100, y=530)
                        player_points += Card3.points
                if(player_card3 == 5):
                        card3_player = Image.open(PATH +"/img/cards/"+Card4.img_file+".png").resize((160,250))
                        self.card3_player = ImageTk.PhotoImage(card3_player)
                        self.label_card3_player= tkinter.Label(master=self.frame_back, image=self.card3_player, borderwidth=0)
                        self.label_card3_player.place(x=1100, y=530)
                        player_points += Card4.points
                if(player_card3 == 6):
                        card3_player = Image.open(PATH +"/img/cards/"+Card5.img_file+".png").resize((160,250))
                        self.card3_player = ImageTk.PhotoImage(card3_player)
                        self.label_card3_player= tkinter.Label(master=self.frame_back, image=self.card3_player, borderwidth=0)
                        self.label_card3_player.place(x=1100, y=530)
                        player_points += Card5.points
                if(player_card3 == 7):
                        card3_player = Image.open(PATH +"/img/cards/"+Card6.img_file+".png").resize((160,250))
                        self.card3_player = ImageTk.PhotoImage(card3_player)
                        self.label_card3_player= tkinter.Label(master=self.frame_back, image=self.card3_player, borderwidth=0)
                        self.label_card3_player.place(x=1100, y=530)
                        player_points += Card6.points
                if(player_card3 == 8):
                        card3_player = Image.open(PATH +"/img/cards/"+Card7.img_file+".png").resize((160,250))
                        self.card3_player = ImageTk.PhotoImage(card3_player)
                        self.label_card3_player= tkinter.Label(master=self.frame_back, image=self.card3_player, borderwidth=0)
                        self.label_card3_player.place(x=1100, y=530)
                        player_points += Card7.points
                if(player_card3 == 9):
                        card3_player = Image.open(PATH +"/img/cards/"+Card8.img_file+".png").resize((160,250))
                        self.card3_player = ImageTk.PhotoImage(card3_player)
                        self.label_card3_player= tkinter.Label(master=self.frame_back, image=self.card3_player, borderwidth=0)
                        self.label_card3_player.place(x=1100, y=530)
                        player_points += Card8.points
                if(player_card3 == 10):
                        card3_player = Image.open(PATH +"/img/cards/"+Card9.img_file+".png").resize((160,250))
                        self.card3_player = ImageTk.PhotoImage(card3_player)
                        self.label_card3_player= tkinter.Label(master=self.frame_back, image=self.card3_player, borderwidth=0)
                        self.label_card3_player.place(x=1100, y=530)
                        player_points += Card9.points
                if(player_card3 == 11):
                        card3_player = Image.open(PATH +"/img/cards/"+Card10.img_file+".png").resize((160,250))
                        self.card3_player = ImageTk.PhotoImage(card2_player)
                        self.label_card3_player= tkinter.Label(master=self.frame_back, image=self.card3_player, borderwidth=0)
                        self.label_card3_player.place(x=1100, y=530)
                        player_points += Card10.points
                if(player_card3 == 12):
                        card3_player = Image.open(PATH +"/img/cards/"+Card11.img_file+".png").resize((160,250))
                        self.card3_player = ImageTk.PhotoImage(card3_player)
                        self.label_card3_player= tkinter.Label(master=self.frame_back, image=self.card3_player, borderwidth=0)
                        self.label_card3_player.place(x=1100, y=530)
                        player_points += Card11.points
                if(player_card3 == 13):
                        card3_player = Image.open(PATH +"/img/cards/"+Card12.img_file+".png").resize((160,250))
                        self.card3_player = ImageTk.PhotoImage(card3_player)
                        self.label_card3_player= tkinter.Label(master=self.frame_back, image=self.card3_player, borderwidth=0)
                        self.label_card3_player.place(x=1100, y=530)
                        player_points += Card12.points
                if(player_card3 == 14):
                        card3_player = Image.open(PATH +"/img/cards/"+Card13.img_file+".png").resize((160,250))
                        self.card3_player = ImageTk.PhotoImage(card3_player)
                        self.label_card3_player= tkinter.Label(master=self.frame_back, image=self.card3_player, borderwidth=0)
                        self.label_card3_player.place(x=1100, y=530)
                        player_points += Card13.points
                if(player_card3 == 15):
                        card3_player = Image.open(PATH +"/img/cards/"+Card14.img_file+".png").resize((160,250))
                        self.card3_player = ImageTk.PhotoImage(card3_player)
                        self.label_card3_player= tkinter.Label(master=self.frame_back, image=self.card3_player, borderwidth=0)
                        self.label_card3_player.place(x=1100, y=530)
                        player_points += Card14.points
                if(player_card3 == 16):
                        card3_player = Image.open(PATH +"/img/cards/"+Card15.img_file+".png").resize((160,250))
                        self.card3_player = ImageTk.PhotoImage(card3_player)
                        self.label_card3_player= tkinter.Label(master=self.frame_back, image=self.card3_player, borderwidth=0)
                        self.label_card3_player.place(x=1100, y=530)
                        player_points += Card15.points
                if(player_card3 == 17):
                        card3_player = Image.open(PATH +"/img/cards/"+Card16.img_file+".png").resize((160,250))
                        self.card3_player = ImageTk.PhotoImage(card3_player)
                        self.label_card3_player= tkinter.Label(master=self.frame_back, image=self.card3_player, borderwidth=0)
                        self.label_card3_player.place(x=1100, y=530)
                        player_points += Card16.points
                if(player_card3 == 18):
                        card3_player = Image.open(PATH +"/img/cards/"+Card17.img_file+".png").resize((160,250))
                        self.card3_player = ImageTk.PhotoImage(card3_player)
                        self.label_card3_player= tkinter.Label(master=self.frame_back, image=self.card3_player, borderwidth=0)
                        self.label_card3_player.place(x=1100, y=530)
                        player_points += Card17.points
                if(player_card3 == 19):
                        card3_player = Image.open(PATH +"/img/cards/"+Card18.img_file+".png").resize((160,250))
                        self.card3_player = ImageTk.PhotoImage(card3_player)
                        self.label_card3_player= tkinter.Label(master=self.frame_back, image=self.card3_player, borderwidth=0)
                        self.label_card3_player.place(x=1100, y=530)
                        player_points += Card18.points
                if(player_card3 == 20):
                        card3_player = Image.open(PATH +"/img/cards/"+Card19.img_file+".png").resize((160,250))
                        self.card3_player = ImageTk.PhotoImage(card3_player)
                        self.label_card3_player= tkinter.Label(master=self.frame_back, image=self.card3_player, borderwidth=0)
                        self.label_card3_player.place(x=1100, y=530)
                        player_points += Card19.points
                if(player_card3 == 21):
                        card3_player = Image.open(PATH +"/img/cards/"+Card20.img_file+".png").resize((160,250))
                        self.card3_player = ImageTk.PhotoImage(card3_player)
                        self.label_card3_player= tkinter.Label(master=self.frame_back, image=self.card3_player, borderwidth=0)
                        self.label_card3_player.place(x=1100, y=530)
                        player_points += Card20.points
                if(player_card3 == 22):
                        card3_player = Image.open(PATH +"/img/cards/"+Card21.img_file+".png").resize((160,250))
                        self.card3_player = ImageTk.PhotoImage(card3_player)
                        self.label_card3_player= tkinter.Label(master=self.frame_back, image=self.card3_player, borderwidth=0)
                        self.label_card3_player.place(x=1100, y=530)
                        player_points += Card21.points
                if(player_card3 == 23):
                        card3_player = Image.open(PATH +"/img/cards/"+Card22.img_file+".png").resize((160,250))
                        self.card3_player = ImageTk.PhotoImage(card3_player)
                        self.label_card3_player= tkinter.Label(master=self.frame_back, image=self.card3_player, borderwidth=0)
                        self.label_card3_player.place(x=1100, y=530)
                        player_points += Card22.points
                if(player_card3 == 24):
                        card3_player = Image.open(PATH +"/img/cards/"+Card23.img_file+".png").resize((160,250))
                        self.card3_player = ImageTk.PhotoImage(card3_player)
                        self.label_card3_player= tkinter.Label(master=self.frame_back, image=self.card3_player, borderwidth=0)
                        self.label_card3_player.place(x=1100, y=530)
                        player_points += Card23.points
                if(player_card3 == 25):
                        card3_player = Image.open(PATH +"/img/cards/"+Card24.img_file+".png").resize((160,250))
                        self.card3_player = ImageTk.PhotoImage(card3_player)
                        self.label_card3_player= tkinter.Label(master=self.frame_back, image=self.card3_player, borderwidth=0)
                        self.label_card3_player.place(x=1100, y=530)
                        player_points += Card24.points
                if(player_card3 == 26):
                        card3_player = Image.open(PATH +"/img/cards/"+Card25.img_file+".png").resize((160,250))
                        self.card3_player = ImageTk.PhotoImage(card3_player)
                        self.label_card3_player= tkinter.Label(master=self.frame_back, image=self.card3_player, borderwidth=0)
                        self.label_card3_player.place(x=1100, y=530)
                        player_points += Card25.points
                if(player_card3 == 27):
                        card3_player = Image.open(PATH +"/img/cards/"+Card26.img_file+".png").resize((160,250))
                        self.card3_player = ImageTk.PhotoImage(card3_player)
                        self.label_card3_player= tkinter.Label(master=self.frame_back, image=self.card3_player, borderwidth=0)
                        self.label_card3_player.place(x=1100, y=530)
                        player_points += Card26.points
                if(player_card3 == 28):
                        card3_player = Image.open(PATH +"/img/cards/"+Card27.img_file+".png").resize((160,250))
                        self.card3_player = ImageTk.PhotoImage(card3_player)
                        self.label_card3_player= tkinter.Label(master=self.frame_back, image=self.card3_player, borderwidth=0)
                        self.label_card3_player.place(x=1100, y=530)
                        player_points += Card27.points
                if(player_card3 == 29):
                        card3_player = Image.open(PATH +"/img/cards/"+Card28.img_file+".png").resize((160,250))
                        self.card3_player = ImageTk.PhotoImage(card3_player)
                        self.label_card3_player= tkinter.Label(master=self.frame_back, image=self.card3_player, borderwidth=0)
                        self.label_card3_player.place(x=1100, y=530)
                        player_points += Card28.points
                if(player_card3 == 30):
                        card3_player = Image.open(PATH +"/img/cards/"+Card29.img_file+".png").resize((160,250))
                        self.card3_player = ImageTk.PhotoImage(card3_player)
                        self.label_card3_player= tkinter.Label(master=self.frame_back, image=self.card3_player, borderwidth=0)
                        self.label_card3_player.place(x=1100, y=530)
                        player_points += Card29.points
                if(player_card3 == 31):
                        card2_player = Image.open(PATH +"/img/cards/"+Card30.img_file+".png").resize((160,250))
                        self.card2_player = ImageTk.PhotoImage(card3_player)
                        self.label_card3_player= tkinter.Label(master=self.frame_back, image=self.card2_player, borderwidth=0)
                        self.label_card3_player.place(x=1100, y=530)
                        player_points += Card30.points
                if(player_card3 == 32):
                        card3_player = Image.open(PATH +"/img/cards/"+Card31.img_file+".png").resize((160,250))
                        self.card3_player = ImageTk.PhotoImage(card3_player)
                        self.label_card3_player= tkinter.Label(master=self.frame_back, image=self.card3_player, borderwidth=0)
                        self.label_card3_player.place(x=1100, y=530)
                        player_points += Card31.points
                if(player_card3 == 33):
                        card3_player = Image.open(PATH +"/img/cards/"+Card32.img_file+".png").resize((160,250))
                        self.card3_player = ImageTk.PhotoImage(card3_player)
                        self.label_card3_player= tkinter.Label(master=self.frame_back, image=self.card3_player, borderwidth=0)
                        self.label_card3_player.place(x=1100, y=530)
                        player_points += Card32.points
                if(player_card3 == 34):
                        card3_player = Image.open(PATH +"/img/cards/"+Card33.img_file+".png").resize((160,250))
                        self.card3_player = ImageTk.PhotoImage(card3_player)
                        self.label_card3_player= tkinter.Label(master=self.frame_back, image=self.card3_player, borderwidth=0)
                        self.label_card3_player.place(x=1100, y=530)
                        player_points += Card33.points
                if(player_card3 == 35):
                        card3_player = Image.open(PATH +"/img/cards/"+Card34.img_file+".png").resize((160,250))
                        self.card3_player = ImageTk.PhotoImage(card3_player)
                        self.label_card3_player= tkinter.Label(master=self.frame_back, image=self.card3_player, borderwidth=0)
                        self.label_card3_player.place(x=1100, y=530)
                        player_points += Card34.points
                if(player_card3 == 36):
                        card3_player = Image.open(PATH +"/img/cards/"+Card35.img_file+".png").resize((160,250))
                        self.card3_player = ImageTk.PhotoImage(card3_player)
                        self.label_card3_player= tkinter.Label(master=self.frame_back, image=self.card3_player, borderwidth=0)
                        self.label_card3_player.place(x=1100, y=530)
                        player_points += Card35.points
                if(player_card3 == 37):
                        card3_player = Image.open(PATH +"/img/cards/"+Card36.img_file+".png").resize((160,250))
                        self.card3_player = ImageTk.PhotoImage(card3_player)
                        self.label_card3_player= tkinter.Label(master=self.frame_back, image=self.card3_player, borderwidth=0)
                        self.label_card3_player.place(x=1100, y=530)
                        player_points += Card36.points
                if(player_card3 == 38):
                        card3_player = Image.open(PATH +"/img/cards/"+Card37.img_file+".png").resize((160,250))
                        self.card3_player = ImageTk.PhotoImage(card3_player)
                        self.label_card3_player= tkinter.Label(master=self.frame_back, image=self.card2_player, borderwidth=0)
                        self.label_card3_player.place(x=1100, y=530)
                        player_points += Card37.points
                if(player_card3 == 39):
                        card3_player = Image.open(PATH +"/img/cards/"+Card38.img_file+".png").resize((160,250))
                        self.card3_player = ImageTk.PhotoImage(card3_player)
                        self.label_card3_player= tkinter.Label(master=self.frame_back, image=self.card3_player, borderwidth=0)
                        self.label_card3_player.place(x=1100, y=530)
                        player_points += Card38.points
                if(player_card3 == 40):
                        card3_player = Image.open(PATH +"/img/cards/"+Card39.img_file+".png").resize((160,250))
                        self.card3_player = ImageTk.PhotoImage(card3_player)
                        self.label_card3_player= tkinter.Label(master=self.frame_back, image=self.card3_player, borderwidth=0)
                        self.label_card3_player.place(x=1100, y=530)
                        player_points += Card39.points
                if(player_card3 == 41):
                        card3_player = Image.open(PATH +"/img/cards/"+Card40.img_file+".png").resize((160,250))
                        self.card3_player = ImageTk.PhotoImage(card3_player)
                        self.label_card3_player= tkinter.Label(master=self.frame_back, image=self.card3_player, borderwidth=0)
                        self.label_card3_player.place(x=1100, y=530)
                        player_points += Card40.points
                if(player_card3 == 42):
                        card3_player = Image.open(PATH +"/img/cards/"+Card41.img_file+".png").resize((160,250))
                        self.card3_player = ImageTk.PhotoImage(card3_player)
                        self.label_card3_player= tkinter.Label(master=self.frame_back, image=self.card3_player, borderwidth=0)
                        self.label_card3_player.place(x=1100, y=530)
                        player_points += Card41.points
                if(player_card3 == 43):
                        card3_player = Image.open(PATH +"/img/cards/"+Card42.img_file+".png").resize((160,250))
                        self.card3_player = ImageTk.PhotoImage(card3_player)
                        self.label_card3_player= tkinter.Label(master=self.frame_back, image=self.card3_player, borderwidth=0)
                        self.label_card3_player.place(x=1100, y=530)
                        player_points += Card42.points
                if(player_card3 == 44):
                        card3_player = Image.open(PATH +"/img/cards/"+Card43.img_file+".png").resize((160,250))
                        self.card3_player = ImageTk.PhotoImage(card3_player)
                        self.label_card3_player= tkinter.Label(master=self.frame_back, image=self.card3_player, borderwidth=0)
                        self.label_card3_player.place(x=1100, y=530)
                        player_points += Card43.points
                if(player_card3 == 45):
                        card3_player = Image.open(PATH +"/img/cards/"+Card44.img_file+".png").resize((160,250))
                        self.card3_player = ImageTk.PhotoImage(card3_player)
                        self.label_card3_player= tkinter.Label(master=self.frame_back, image=self.card3_player, borderwidth=0)
                        self.label_card3_player.place(x=1100, y=530)
                        player_points += Card44.points
                if(player_card3 == 46):
                        card2_player = Image.open(PATH +"/img/cards/"+Card45.img_file+".png").resize((160,250))
                        self.card2_player = ImageTk.PhotoImage(card3_player)
                        self.label_card3_player= tkinter.Label(master=self.frame_back, image=self.card2_player, borderwidth=0)
                        self.label_card3_player.place(x=1100, y=530)
                        player_points += Card45.points
                if(player_card3 == 47):
                        card3_player = Image.open(PATH +"/img/cards/"+Card46.img_file+".png").resize((160,250))
                        self.card3_player = ImageTk.PhotoImage(card3_player)
                        self.label_card3_player= tkinter.Label(master=self.frame_back, image=self.card3_player, borderwidth=0)
                        self.label_card3_player.place(x=1100, y=530)
                        player_points += Card46.points
                if(player_card3 == 48):
                        card3_player = Image.open(PATH +"/img/cards/"+Card47.img_file+".png").resize((160,250))
                        self.card3_player = ImageTk.PhotoImage(card3_player)
                        self.label_card3_player= tkinter.Label(master=self.frame_back, image=self.card3_player, borderwidth=0)
                        self.label_card3_player.place(x=1100, y=530)
                        player_points += Card47.points
            if(index_card == 4):                
                if(dealer_points<16):
                    last_draw_card +=1
                    dealer_card4 = Game_array [last_draw_card]
                    if(dealer_card4 == 1):
                        card4_dealer = Image.open(PATH +"/img/cards/"+Card0.img_file+".png").resize((160,250))
                        self.card4_dealer = ImageTk.PhotoImage(card4_dealer)
                        self.label_card4_dealer= tkinter.Label(master=self.frame_back, image=self.card4_dealer, borderwidth=0)
                        self.label_card4_dealer.place(x=1300, y=250)
                        dealer_points += Card0.points
                    if(dealer_card4 == 2):
                        card4_dealer = Image.open(PATH +"/img/cards/"+Card1.img_file+".png").resize((160,250))
                        self.card4_dealer = ImageTk.PhotoImage(card4_dealer)
                        self.label_card4_dealer= tkinter.Label(master=self.frame_back, image=self.card4_dealer, borderwidth=0)
                        self.label_card4_dealer.place(x=1300, y=250)
                        dealer_points += Card1.points
                    if(dealer_card4 == 3):
                        card4_dealer = Image.open(PATH +"/img/cards/"+Card2.img_file+".png").resize((160,250))
                        self.card4_dealer = ImageTk.PhotoImage(card4_dealer)
                        self.label_card4_dealer= tkinter.Label(master=self.frame_back, image=self.card4_dealer, borderwidth=0)
                        self.label_card4_dealer.place(x=1300, y=250)
                        dealer_points += Card2.points
                    if(dealer_card4 == 4):
                        card4_dealer = Image.open(PATH +"/img/cards/"+Card3.img_file+".png").resize((160,250))
                        self.card4_dealer = ImageTk.PhotoImage(card4_dealer)
                        self.label_card4_dealer= tkinter.Label(master=self.frame_back, image=self.card4_dealer, borderwidth=0)
                        self.label_card4_dealer.place(x=1300, y=250)
                        dealer_points += Card3.points
                    if(dealer_card4 == 5):
                        card4_dealer = Image.open(PATH +"/img/cards/"+Card4.img_file+".png").resize((160,250))
                        self.card4_dealer = ImageTk.PhotoImage(card4_dealer)
                        self.label_card4_dealer= tkinter.Label(master=self.frame_back, image=self.card4_dealer, borderwidth=0)
                        self.label_card4_dealer.place(x=1300, y=250)
                        dealer_points += Card4.points
                    if(dealer_card4 == 6):
                        card4_dealer = Image.open(PATH +"/img/cards/"+Card5.img_file+".png").resize((160,250))
                        self.card4_dealer = ImageTk.PhotoImage(card4_dealer)
                        self.label_card4_dealer= tkinter.Label(master=self.frame_back, image=self.card4_dealer, borderwidth=0)
                        self.label_card4_dealer.place(x=1300, y=250)
                        dealer_points += Card5.points
                    if(dealer_card4 == 7):
                        card4_dealer = Image.open(PATH +"/img/cards/"+Card6.img_file+".png").resize((160,250))
                        self.card4_dealer = ImageTk.PhotoImage(card4_dealer)
                        self.label_card4_dealer= tkinter.Label(master=self.frame_back, image=self.card4_dealer, borderwidth=0)
                        self.label_card4_dealer.place(x=1300, y=250)
                        dealer_points += Card6.points
                    if(dealer_card4 == 8):
                        card4_dealer = Image.open(PATH +"/img/cards/"+Card7.img_file+".png").resize((160,250))
                        self.card4_dealer = ImageTk.PhotoImage(card4_dealer)
                        self.label_card4_dealer= tkinter.Label(master=self.frame_back, image=self.card4_dealer, borderwidth=0)
                        self.label_card4_dealer.place(x=1300, y=250)
                        dealer_points += Card7.points
                    if(dealer_card4 == 9):
                        card4_dealer = Image.open(PATH +"/img/cards/"+Card8.img_file+".png").resize((160,250))
                        self.card4_dealer = ImageTk.PhotoImage(card4_dealer)
                        self.label_card4_dealer= tkinter.Label(master=self.frame_back, image=self.card4_dealer, borderwidth=0)
                        self.label_card4_dealer.place(x=1300, y=250)
                        dealer_points += Card8.points
                    if(dealer_card4 == 10):
                        card4_dealer = Image.open(PATH +"/img/cards/"+Card9.img_file+".png").resize((160,250))
                        self.card4_dealer = ImageTk.PhotoImage(card4_dealer)
                        self.label_card4_dealer= tkinter.Label(master=self.frame_back, image=self.card4_dealer, borderwidth=0)
                        self.label_card4_dealer.place(x=1300, y=250)
                        dealer_points += Card9.points
                    if(dealer_card4 == 11):
                        card4_dealer = Image.open(PATH +"/img/cards/"+Card10.img_file+".png").resize((160,250))
                        self.card4_dealer = ImageTk.PhotoImage(card4_dealer)
                        self.label_card4_dealer= tkinter.Label(master=self.frame_back, image=self.card4_dealer, borderwidth=0)
                        self.label_card4_dealer.place(x=1300, y=250)
                        dealer_points += Card10.points
                    if(dealer_card4 == 12):
                        card4_dealer = Image.open(PATH +"/img/cards/"+Card11.img_file+".png").resize((160,250))
                        self.card4_dealer = ImageTk.PhotoImage(card4_dealer)
                        self.label_card4_dealer= tkinter.Label(master=self.frame_back, image=self.card4_dealer, borderwidth=0)
                        self.label_card4_dealer.place(x=1300, y=250)
                        dealer_points += Card11.points
                    if(dealer_card4 == 13):
                        card4_dealer = Image.open(PATH +"/img/cards/"+Card12.img_file+".png").resize((160,250))
                        self.card4_dealer = ImageTk.PhotoImage(card4_dealer)
                        self.label_card4_dealer= tkinter.Label(master=self.frame_back, image=self.card4_dealer, borderwidth=0)
                        self.label_card4_dealer.place(x=1300, y=250)
                        dealer_points += Card12.points
                    if(dealer_card4 == 14):
                        card4_dealer = Image.open(PATH +"/img/cards/"+Card13.img_file+".png").resize((160,250))
                        self.card4_dealer = ImageTk.PhotoImage(card4_dealer)
                        self.label_card4_dealer= tkinter.Label(master=self.frame_back, image=self.card4_dealer, borderwidth=0)
                        self.label_card4_dealer.place(x=1300, y=250)
                        dealer_points += Card13.points
                    if(dealer_card4 == 15):
                        card4_dealer = Image.open(PATH +"/img/cards/"+Card14.img_file+".png").resize((160,250))
                        self.card4_dealer = ImageTk.PhotoImage(card4_dealer)
                        self.label_card4_dealer= tkinter.Label(master=self.frame_back, image=self.card4_dealer, borderwidth=0)
                        self.label_card4_dealer.place(x=1300, y=250)
                        dealer_points += Card14.points
                    if(dealer_card4 == 16):
                        card4_dealer = Image.open(PATH +"/img/cards/"+Card15.img_file+".png").resize((160,250))
                        self.card4_dealer = ImageTk.PhotoImage(card4_dealer)
                        self.label_card4_dealer= tkinter.Label(master=self.frame_back, image=self.card4_dealer, borderwidth=0)
                        self.label_card4_dealer.place(x=1300, y=250)
                        dealer_points += Card15.points
                    if(dealer_card4 == 17):
                        card4_dealer = Image.open(PATH +"/img/cards/"+Card16.img_file+".png").resize((160,250))
                        self.card4_dealer = ImageTk.PhotoImage(card4_dealer)
                        self.label_card4_dealer= tkinter.Label(master=self.frame_back, image=self.card4_dealer, borderwidth=0)
                        self.label_card4_dealer.place(x=1300, y=250)
                        dealer_points += Card16.points
                    if(dealer_card4 == 18):
                        card4_dealer = Image.open(PATH +"/img/cards/"+Card17.img_file+".png").resize((160,250))
                        self.card4_dealer = ImageTk.PhotoImage(card4_dealer)
                        self.label_card4_dealer= tkinter.Label(master=self.frame_back, image=self.card4_dealer, borderwidth=0)
                        self.label_card4_dealer.place(x=1300, y=250)
                        dealer_points += Card17.points
                    if(dealer_card4 == 19):
                        card4_dealer = Image.open(PATH +"/img/cards/"+Card18.img_file+".png").resize((160,250))
                        self.card4_dealer = ImageTk.PhotoImage(card4_dealer)
                        self.label_card4_dealer= tkinter.Label(master=self.frame_back, image=self.card4_dealer, borderwidth=0)
                        self.label_card4_dealer.place(x=1300, y=250)
                        dealer_points += Card18.points
                    if(dealer_card4 == 20):
                        card4_dealer = Image.open(PATH +"/img/cards/"+Card19.img_file+".png").resize((160,250))
                        self.card4_dealer = ImageTk.PhotoImage(card4_dealer)
                        self.label_card4_dealer= tkinter.Label(master=self.frame_back, image=self.card4_dealer, borderwidth=0)
                        self.label_card4_dealer.place(x=1300, y=250)
                        dealer_points += Card19.points
                    if(dealer_card4 == 21):
                        card4_dealer = Image.open(PATH +"/img/cards/"+Card20.img_file+".png").resize((160,250))
                        self.card4_dealer = ImageTk.PhotoImage(card4_dealer)
                        self.label_card4_dealer= tkinter.Label(master=self.frame_back, image=self.card4_dealer, borderwidth=0)
                        self.label_card4_dealer.place(x=1300, y=250)
                        dealer_points += Card20.points
                    if(dealer_card4 == 22):
                        card4_dealer = Image.open(PATH +"/img/cards/"+Card21.img_file+".png").resize((160,250))
                        self.card4_dealer = ImageTk.PhotoImage(card4_dealer)
                        self.label_card4_dealer= tkinter.Label(master=self.frame_back, image=self.card4_dealer, borderwidth=0)
                        self.label_card4_dealer.place(x=1300, y=250)
                        dealer_points += Card21.points
                    if(dealer_card4 == 23):
                        card4_dealer = Image.open(PATH +"/img/cards/"+Card22.img_file+".png").resize((160,250))
                        self.card4_dealer = ImageTk.PhotoImage(card4_dealer)
                        self.label_card4_dealer= tkinter.Label(master=self.frame_back, image=self.card4_dealer, borderwidth=0)
                        self.label_card4_dealer.place(x=1300, y=250)
                        dealer_points += Card22.points
                    if(dealer_card4 == 24):
                        card4_dealer = Image.open(PATH +"/img/cards/"+Card23.img_file+".png").resize((160,250))
                        self.card4_dealer = ImageTk.PhotoImage(card4_dealer)
                        self.label_card4_dealer= tkinter.Label(master=self.frame_back, image=self.card4_dealer, borderwidth=0)
                        self.label_card4_dealer.place(x=1300, y=250)
                        dealer_points += Card23.points
                    if(dealer_card4 == 25):
                        card4_dealer = Image.open(PATH +"/img/cards/"+Card24.img_file+".png").resize((160,250))
                        self.card4_dealer = ImageTk.PhotoImage(card4_dealer)
                        self.label_card4_dealer= tkinter.Label(master=self.frame_back, image=self.card4_dealer, borderwidth=0)
                        self.label_card4_dealer.place(x=1300, y=250)
                        dealer_points += Card24.points
                    if(dealer_card4 == 26):
                        card4_dealer = Image.open(PATH +"/img/cards/"+Card25.img_file+".png").resize((160,250))
                        self.card4_dealer = ImageTk.PhotoImage(card4_dealer)
                        self.label_card4_dealer= tkinter.Label(master=self.frame_back, image=self.card4_dealer, borderwidth=0)
                        self.label_card4_dealer.place(x=1300, y=250)
                        dealer_points += Card25.points
                    if(dealer_card4 == 27):
                        card4_dealer = Image.open(PATH +"/img/cards/"+Card26.img_file+".png").resize((160,250))
                        self.card4_dealer = ImageTk.PhotoImage(card4_dealer)
                        self.label_card4_dealer= tkinter.Label(master=self.frame_back, image=self.card4_dealer, borderwidth=0)
                        self.label_card4_dealer.place(x=1300, y=250)
                        dealer_points += Card26.points
                    if(dealer_card4 == 28):
                        card3_dealer = Image.open(PATH +"/img/cards/"+Card27.img_file+".png").resize((160,250))
                        self.card3_dealer = ImageTk.PhotoImage(card3_dealer)
                        self.label_card4_dealer= tkinter.Label(master=self.frame_back, image=self.card3_dealer, borderwidth=0)
                        self.label_card4_dealer.place(x=1300, y=250)
                        dealer_points += Card27.points
                    if(dealer_card4 == 29):
                        card4_dealer = Image.open(PATH +"/img/cards/"+Card28.img_file+".png").resize((160,250))
                        self.card4_dealer = ImageTk.PhotoImage(card4_dealer)
                        self.label_card4_dealer= tkinter.Label(master=self.frame_back, image=self.card4_dealer, borderwidth=0)
                        self.label_card4_dealer.place(x=1300, y=250)
                        dealer_points += Card28.points
                    if(dealer_card4 == 30):
                        card3_dealer = Image.open(PATH +"/img/cards/"+Card29.img_file+".png").resize((160,250))
                        self.card3_dealer = ImageTk.PhotoImage(card3_dealer)
                        self.label_card4_dealer= tkinter.Label(master=self.frame_back, image=self.card3_dealer, borderwidth=0)
                        self.label_card4_dealer.place(x=1300, y=250)
                        dealer_points += Card29.points
                    if(dealer_card4 == 31):
                        card4_dealer = Image.open(PATH +"/img/cards/"+Card30.img_file+".png").resize((160,250))
                        self.card4_dealer = ImageTk.PhotoImage(card3_dealer)
                        self.label_card4_dealer= tkinter.Label(master=self.frame_back, image=self.card4_dealer, borderwidth=0)
                        self.label_card4_dealer.place(x=1300, y=250)
                        dealer_points += Card30.points
                    if(dealer_card4 == 32):
                        card4_dealer = Image.open(PATH +"/img/cards/"+Card31.img_file+".png").resize((160,250))
                        self.card4_dealer = ImageTk.PhotoImage(card4_dealer)
                        self.label_card4_dealer= tkinter.Label(master=self.frame_back, image=self.card4_dealer, borderwidth=0)
                        self.label_card4_dealer.place(x=1300, y=250)
                        dealer_points += Card31.points
                    if(dealer_card4 == 33):
                        card4_dealer = Image.open(PATH +"/img/cards/"+Card32.img_file+".png").resize((160,250))
                        self.card4_dealer = ImageTk.PhotoImage(card4_dealer)
                        self.label_card4_dealer= tkinter.Label(master=self.frame_back, image=self.card4_dealer, borderwidth=0)
                        self.label_card4_dealer.place(x=1300, y=250)
                        dealer_points += Card32.points
                    if(dealer_card4 == 34):
                        card4_dealer = Image.open(PATH +"/img/cards/"+Card33.img_file+".png").resize((160,250))
                        self.card4_dealer = ImageTk.PhotoImage(card4_dealer)
                        self.label_card4_dealer= tkinter.Label(master=self.frame_back, image=self.card4_dealer, borderwidth=0)
                        self.label_card4_dealer.place(x=1300, y=250)
                        dealer_points += Card33.points
                    if(dealer_card4 == 35):
                        card4_dealer = Image.open(PATH +"/img/cards/"+Card34.img_file+".png").resize((160,250))
                        self.card4_dealer = ImageTk.PhotoImage(card4_dealer)
                        self.label_card4_dealer= tkinter.Label(master=self.frame_back, image=self.card4_dealer, borderwidth=0)
                        self.label_card4_dealer.place(x=1300, y=250)
                        dealer_points += Card34.points
                    if(dealer_card4 == 36):
                        card4_dealer = Image.open(PATH +"/img/cards/"+Card35.img_file+".png").resize((160,250))
                        self.card4_dealer = ImageTk.PhotoImage(card3_dealer)
                        self.label_card4_dealer= tkinter.Label(master=self.frame_back, image=self.card4_dealer, borderwidth=0)
                        self.label_card4_dealer.place(x=1300, y=250)
                        dealer_points += Card35.points
                    if(dealer_card4 == 37):
                        card4_dealer = Image.open(PATH +"/img/cards/"+Card36.img_file+".png").resize((160,250))
                        self.card4_dealer = ImageTk.PhotoImage(card4_dealer)
                        self.label_card4_dealer= tkinter.Label(master=self.frame_back, image=self.card4_dealer, borderwidth=0)
                        self.label_card4_dealer.place(x=1300, y=250)
                        dealer_points += Card36.points
                    if(dealer_card4 == 38):
                        card4_dealer = Image.open(PATH +"/img/cards/"+Card37.img_file+".png").resize((160,250))
                        self.card4_dealer = ImageTk.PhotoImage(card4_dealer)
                        self.label_card4_dealer= tkinter.Label(master=self.frame_back, image=self.card4_dealer, borderwidth=0)
                        self.label_card4_dealer.place(x=1300, y=250)
                        dealer_points += Card37.points
                    if(dealer_card4 == 39):
                        card4_dealer = Image.open(PATH +"/img/cards/"+Card38.img_file+".png").resize((160,250))
                        self.card4_dealer = ImageTk.PhotoImage(card4_dealer)
                        self.label_card4_dealer= tkinter.Label(master=self.frame_back, image=self.card4_dealer, borderwidth=0)
                        self.label_card4_dealer.place(x=1300, y=250)
                        dealer_points += Card38.points
                    if(dealer_card4 == 40):
                        card4_dealer = Image.open(PATH +"/img/cards/"+Card39.img_file+".png").resize((160,250))
                        self.card4_dealer = ImageTk.PhotoImage(card4_dealer)
                        self.label_card4_dealer= tkinter.Label(master=self.frame_back, image=self.card4_dealer, borderwidth=0)
                        self.label_card4_dealer.place(x=1300, y=250)
                        dealer_points += Card39.points
                    if(dealer_card4 == 41):
                        card4_dealer = Image.open(PATH +"/img/cards/"+Card40.img_file+".png").resize((160,250))
                        self.card4_dealer = ImageTk.PhotoImage(card4_dealer)
                        self.label_card4_dealer= tkinter.Label(master=self.frame_back, image=self.card4_dealer, borderwidth=0)
                        self.label_card4_dealer.place(x=1300, y=250)
                        dealer_points += Card40.points
                    if(dealer_card4 == 42):
                        card4_dealer = Image.open(PATH +"/img/cards/"+Card41.img_file+".png").resize((160,250))
                        self.card4_dealer = ImageTk.PhotoImage(card2_dealer)
                        self.label_card4_dealer= tkinter.Label(master=self.frame_back, image=self.card4_dealer, borderwidth=0)
                        self.label_card4_dealer.place(x=1300, y=250)
                        dealer_points += Card41.points
                    if(dealer_card4 == 43):
                        card4_dealer = Image.open(PATH +"/img/cards/"+Card42.img_file+".png").resize((160,250))
                        self.card4_dealer = ImageTk.PhotoImage(card3_dealer)
                        self.label_card3_dealer= tkinter.Label(master=self.frame_back, image=self.card4_dealer, borderwidth=0)
                        self.label_card3_dealer.place(x=1300, y=250)
                        dealer_points += Card42.points
                    if(dealer_card4 == 44):
                        card4_dealer = Image.open(PATH +"/img/cards/"+Card43.img_file+".png").resize((160,250))
                        self.card4_dealer = ImageTk.PhotoImage(card4_dealer)
                        self.label_card4_dealer= tkinter.Label(master=self.frame_back, image=self.card4_dealer, borderwidth=0)
                        self.label_card4_dealer.place(x=1300, y=250)
                        dealer_points += Card43.points
                    if(dealer_card4 == 45):
                        card4_dealer = Image.open(PATH +"/img/cards/"+Card44.img_file+".png").resize((160,250))
                        self.card4_dealer = ImageTk.PhotoImage(card4_dealer)
                        self.label_card4_dealer= tkinter.Label(master=self.frame_back, image=self.card4_dealer, borderwidth=0)
                        self.label_card4_dealer.place(x=1300, y=250)
                        dealer_points += Card44.points
                    if(dealer_card4 == 46):
                        card4_dealer = Image.open(PATH +"/img/cards/"+Card45.img_file+".png").resize((160,250))
                        self.card4_dealer = ImageTk.PhotoImage(card4_dealer)
                        self.label_card4_dealer= tkinter.Label(master=self.frame_back, image=self.card4_dealer, borderwidth=0)
                        self.label_card4_dealer.place(x=1300, y=250)
                        dealer_points += Card45.points
                    if(dealer_card4 == 47):
                        card4_dealer = Image.open(PATH +"/img/cards/"+Card46.img_file+".png").resize((160,250))
                        self.card4_dealer = ImageTk.PhotoImage(card4_dealer)
                        self.label_card4_dealer= tkinter.Label(master=self.frame_back, image=self.card4_dealer, borderwidth=0)
                        self.label_card4_dealer.place(x=1300, y=250)
                        dealer_points += Card46.points
                    if(dealer_card4 == 48):
                        card4_dealer = Image.open(PATH +"/img/cards/"+Card47.img_file+".png").resize((160,250))
                        self.card4_dealer = ImageTk.PhotoImage(card4_dealer)
                        self.label_card4_dealer= tkinter.Label(master=self.frame_back, image=self.card4_dealer, borderwidth=0)
                        self.label_card4_dealer.place(x=1300, y=250)
                        dealer_points += Card47.points
                        #======== end dealer card 3
                last_draw_card +=1
                player_card4 = Game_array[last_draw_card]
                if(player_card4 == 1):
                        card4_player = Image.open(PATH +"/img/cards/"+Card0.img_file+".png").resize((160,250))
                        self.card4_player = ImageTk.PhotoImage(card4_player)
                        self.label_card3_player= tkinter.Label(master=self.frame_back, image=self.card4_player, borderwidth=0)
                        self.label_card3_player.place(x=1300, y=530)
                        player_points += Card0.points
                if(player_card4 == 2):
                        card4_player = Image.open(PATH +"/img/cards/"+Card1.img_file+".png").resize((160,250))
                        self.card4_player = ImageTk.PhotoImage(card4_player)
                        self.label_card3_player= tkinter.Label(master=self.frame_back, image=self.card4_player, borderwidth=0)
                        self.label_card3_player.place(x=1300, y=530)
                        player_points += Card1.points
                if(player_card4 == 3):
                        card4_player = Image.open(PATH +"/img/cards/"+Card2.img_file+".png").resize((160,250))
                        self.card4_player = ImageTk.PhotoImage(card4_player)
                        self.label_card3_player= tkinter.Label(master=self.frame_back, image=self.card4_player, borderwidth=0)
                        self.label_card3_player.place(x=1300, y=530)
                        player_points += Card2.points
                if(player_card4 == 4):
                        card4_player = Image.open(PATH +"/img/cards/"+Card3.img_file+".png").resize((160,250))
                        self.card4_player = ImageTk.PhotoImage(card4_player)
                        self.label_card3_player= tkinter.Label(master=self.frame_back, image=self.card4_player, borderwidth=0)
                        self.label_card3_player.place(x=1300, y=530)
                        player_points += Card3.points
                if(player_card4 == 5):
                        card4_player = Image.open(PATH +"/img/cards/"+Card4.img_file+".png").resize((160,250))
                        self.card4_player = ImageTk.PhotoImage(card4_player)
                        self.label_card3_player= tkinter.Label(master=self.frame_back, image=self.card4_player, borderwidth=0)
                        self.label_card3_player.place(x=1300, y=530)
                        player_points += Card4.points
                if(player_card4 == 6):
                        card4_player = Image.open(PATH +"/img/cards/"+Card5.img_file+".png").resize((160,250))
                        self.card4_player = ImageTk.PhotoImage(card4_player)
                        self.label_card3_player= tkinter.Label(master=self.frame_back, image=self.card4_player, borderwidth=0)
                        self.label_card3_player.place(x=1300, y=530)
                        player_points += Card5.points
                if(player_card4 == 7):
                        card4_player = Image.open(PATH +"/img/cards/"+Card6.img_file+".png").resize((160,250))
                        self.card4_player = ImageTk.PhotoImage(card4_player)
                        self.label_card3_player= tkinter.Label(master=self.frame_back, image=self.card4_player, borderwidth=0)
                        self.label_card3_player.place(x=1300, y=530)
                        player_points += Card6.points
                if(player_card4 == 8):
                        card4_player = Image.open(PATH +"/img/cards/"+Card7.img_file+".png").resize((160,250))
                        self.card4_player = ImageTk.PhotoImage(card4_player)
                        self.label_card3_player= tkinter.Label(master=self.frame_back, image=self.card4_player, borderwidth=0)
                        self.label_card3_player.place(x=1300, y=530)
                        player_points += Card7.points
                if(player_card4 == 9):
                        card4_player = Image.open(PATH +"/img/cards/"+Card8.img_file+".png").resize((160,250))
                        self.card4_player = ImageTk.PhotoImage(card4_player)
                        self.label_card3_player= tkinter.Label(master=self.frame_back, image=self.card4_player, borderwidth=0)
                        self.label_card3_player.place(x=1300, y=530)
                        player_points += Card8.points
                if(player_card4 == 10):
                        card4_player = Image.open(PATH +"/img/cards/"+Card9.img_file+".png").resize((160,250))
                        self.card4_player = ImageTk.PhotoImage(card4_player)
                        self.label_card3_player= tkinter.Label(master=self.frame_back, image=self.card4_player, borderwidth=0)
                        self.label_card3_player.place(x=1300, y=530)
                        player_points += Card9.points
                if(player_card4 == 11):
                        card4_player = Image.open(PATH +"/img/cards/"+Card10.img_file+".png").resize((160,250))
                        self.card4_player = ImageTk.PhotoImage(card4_player)
                        self.label_card3_player= tkinter.Label(master=self.frame_back, image=self.card4_player, borderwidth=0)
                        self.label_card3_player.place(x=1300, y=530)
                        player_points += Card10.points
                if(player_card4 == 12):
                        card4_player = Image.open(PATH +"/img/cards/"+Card11.img_file+".png").resize((160,250))
                        self.card4_player = ImageTk.PhotoImage(card4_player)
                        self.label_card3_player= tkinter.Label(master=self.frame_back, image=self.card4_player, borderwidth=0)
                        self.label_card3_player.place(x=1300, y=530)
                        player_points += Card11.points
                if(player_card4 == 13):
                        card4_player = Image.open(PATH +"/img/cards/"+Card12.img_file+".png").resize((160,250))
                        self.card4_player = ImageTk.PhotoImage(card4_player)
                        self.label_card3_player= tkinter.Label(master=self.frame_back, image=self.card4_player, borderwidth=0)
                        self.label_card3_player.place(x=1300, y=530)
                        player_points += Card12.points
                if(player_card4 == 14):
                        card4_player = Image.open(PATH +"/img/cards/"+Card13.img_file+".png").resize((160,250))
                        self.card4_player = ImageTk.PhotoImage(card4_player)
                        self.label_card3_player= tkinter.Label(master=self.frame_back, image=self.card4_player, borderwidth=0)
                        self.label_card3_player.place(x=1300, y=530)
                        player_points += Card13.points
                if(player_card4 == 15):
                        card4_player = Image.open(PATH +"/img/cards/"+Card14.img_file+".png").resize((160,250))
                        self.card4_player = ImageTk.PhotoImage(card4_player)
                        self.label_card3_player= tkinter.Label(master=self.frame_back, image=self.card4_player, borderwidth=0)
                        self.label_card3_player.place(x=1300, y=530)
                        player_points += Card14.points
                if(player_card4 == 16):
                        card4_player = Image.open(PATH +"/img/cards/"+Card15.img_file+".png").resize((160,250))
                        self.card4_player = ImageTk.PhotoImage(card4_player)
                        self.label_card3_player= tkinter.Label(master=self.frame_back, image=self.card4_player, borderwidth=0)
                        self.label_card3_player.place(x=1300, y=530)
                        player_points += Card15.points
                if(player_card4 == 17):
                        card4_player = Image.open(PATH +"/img/cards/"+Card16.img_file+".png").resize((160,250))
                        self.card4_player = ImageTk.PhotoImage(card4_player)
                        self.label_card3_player= tkinter.Label(master=self.frame_back, image=self.card4_player, borderwidth=0)
                        self.label_card3_player.place(x=1300, y=530)
                        player_points += Card16.points
                if(player_card4 == 18):
                        card4_player = Image.open(PATH +"/img/cards/"+Card17.img_file+".png").resize((160,250))
                        self.card4_player = ImageTk.PhotoImage(card4_player)
                        self.label_card3_player= tkinter.Label(master=self.frame_back, image=self.card4_player, borderwidth=0)
                        self.label_card3_player.place(x=1300, y=530)
                        player_points += Card17.points
                if(player_card4 == 19):
                        card4_player = Image.open(PATH +"/img/cards/"+Card18.img_file+".png").resize((160,250))
                        self.card4_player = ImageTk.PhotoImage(card4_player)
                        self.label_card3_player= tkinter.Label(master=self.frame_back, image=self.card4_player, borderwidth=0)
                        self.label_card3_player.place(x=1300, y=530)
                        player_points += Card18.points
                if(player_card4 == 20):
                        card4_player = Image.open(PATH +"/img/cards/"+Card19.img_file+".png").resize((160,250))
                        self.card4_player = ImageTk.PhotoImage(card4_player)
                        self.label_card3_player= tkinter.Label(master=self.frame_back, image=self.card4_player, borderwidth=0)
                        self.label_card3_player.place(x=1300, y=530)
                        player_points += Card19.points
                if(player_card4 == 21):
                        card4_player = Image.open(PATH +"/img/cards/"+Card20.img_file+".png").resize((160,250))
                        self.card4_player = ImageTk.PhotoImage(card4_player)
                        self.label_card3_player= tkinter.Label(master=self.frame_back, image=self.card4_player, borderwidth=0)
                        self.label_card3_player.place(x=1300, y=530)
                        player_points += Card20.points
                if(player_card4 == 22):
                        card4_player = Image.open(PATH +"/img/cards/"+Card21.img_file+".png").resize((160,250))
                        self.card4_player = ImageTk.PhotoImage(card4_player)
                        self.label_card3_player= tkinter.Label(master=self.frame_back, image=self.card4_player, borderwidth=0)
                        self.label_card3_player.place(x=1300, y=530)
                        player_points += Card21.points
                if(player_card4 == 23):
                        card4_player = Image.open(PATH +"/img/cards/"+Card22.img_file+".png").resize((160,250))
                        self.card4_player = ImageTk.PhotoImage(card4_player)
                        self.label_card3_player= tkinter.Label(master=self.frame_back, image=self.card4_player, borderwidth=0)
                        self.label_card3_player.place(x=1300, y=530)
                        player_points += Card22.points
                if(player_card4 == 24):
                        card4_player = Image.open(PATH +"/img/cards/"+Card23.img_file+".png").resize((160,250))
                        self.card4_player = ImageTk.PhotoImage(card4_player)
                        self.label_card3_player= tkinter.Label(master=self.frame_back, image=self.card4_player, borderwidth=0)
                        self.label_card3_player.place(x=1300, y=530)
                        player_points += Card23.points
                if(player_card4 == 25):
                        card4_player = Image.open(PATH +"/img/cards/"+Card24.img_file+".png").resize((160,250))
                        self.card4_player = ImageTk.PhotoImage(card4_player)
                        self.label_card3_player= tkinter.Label(master=self.frame_back, image=self.card4_player, borderwidth=0)
                        self.label_card3_player.place(x=1300, y=530)
                        player_points += Card24.points
                if(player_card4 == 26):
                        card4_player = Image.open(PATH +"/img/cards/"+Card25.img_file+".png").resize((160,250))
                        self.card4_player = ImageTk.PhotoImage(card4_player)
                        self.label_card3_player= tkinter.Label(master=self.frame_back, image=self.card4_player, borderwidth=0)
                        self.label_card3_player.place(x=1300, y=530)
                        player_points += Card25.points
                if(player_card4 == 27):
                        card4_player = Image.open(PATH +"/img/cards/"+Card26.img_file+".png").resize((160,250))
                        self.card4_player = ImageTk.PhotoImage(card4_player)
                        self.label_card3_player= tkinter.Label(master=self.frame_back, image=self.card4_player, borderwidth=0)
                        self.label_card3_player.place(x=1300, y=530)
                        player_points += Card26.points
                if(player_card4 == 28):
                        card4_player = Image.open(PATH +"/img/cards/"+Card27.img_file+".png").resize((160,250))
                        self.card4_player = ImageTk.PhotoImage(card4_player)
                        self.label_card3_player= tkinter.Label(master=self.frame_back, image=self.card4_player, borderwidth=0)
                        self.label_card3_player.place(x=1300, y=530)
                        player_points += Card27.points
                if(player_card4 == 29):
                        card4_player = Image.open(PATH +"/img/cards/"+Card28.img_file+".png").resize((160,250))
                        self.card4_player = ImageTk.PhotoImage(card4_player)
                        self.label_card3_player= tkinter.Label(master=self.frame_back, image=self.card4_player, borderwidth=0)
                        self.label_card3_player.place(x=1300, y=530)
                        player_points += Card28.points
                if(player_card4 == 30):
                        card4_player = Image.open(PATH +"/img/cards/"+Card29.img_file+".png").resize((160,250))
                        self.card4_player = ImageTk.PhotoImage(card4_player)
                        self.label_card3_player= tkinter.Label(master=self.frame_back, image=self.card4_player, borderwidth=0)
                        self.label_card3_player.place(x=1300, y=530)
                        player_points += Card29.points
                if(player_card4 == 31):
                        card4_player = Image.open(PATH +"/img/cards/"+Card30.img_file+".png").resize((160,250))
                        self.card4_player = ImageTk.PhotoImage(card4_player)
                        self.label_card3_player= tkinter.Label(master=self.frame_back, image=self.card4_player, borderwidth=0)
                        self.label_card3_player.place(x=1300, y=530)
                        player_points += Card30.points
                if(player_card4 == 32):
                        card4_player = Image.open(PATH +"/img/cards/"+Card31.img_file+".png").resize((160,250))
                        self.card4_player = ImageTk.PhotoImage(card4_player)
                        self.label_card3_player= tkinter.Label(master=self.frame_back, image=self.card4_player, borderwidth=0)
                        self.label_card3_player.place(x=1300, y=530)
                        player_points += Card31.points
                if(player_card4 == 33):
                        card4_player = Image.open(PATH +"/img/cards/"+Card32.img_file+".png").resize((160,250))
                        self.card4_player = ImageTk.PhotoImage(card4_player)
                        self.label_card3_player= tkinter.Label(master=self.frame_back, image=self.card4_player, borderwidth=0)
                        self.label_card3_player.place(x=1300, y=530)
                        player_points += Card32.points
                if(player_card4 == 34):
                        card4_player = Image.open(PATH +"/img/cards/"+Card33.img_file+".png").resize((160,250))
                        self.card4_player = ImageTk.PhotoImage(card4_player)
                        self.label_card3_player= tkinter.Label(master=self.frame_back, image=self.card4_player, borderwidth=0)
                        self.label_card3_player.place(x=1300, y=530)
                        player_points += Card33.points
                if(player_card4 == 35):
                        card4_player = Image.open(PATH +"/img/cards/"+Card34.img_file+".png").resize((160,250))
                        self.card4_player = ImageTk.PhotoImage(card4_player)
                        self.label_card3_player= tkinter.Label(master=self.frame_back, image=self.card4_player, borderwidth=0)
                        self.label_card3_player.place(x=1300, y=530)
                        player_points += Card34.points
                if(player_card4 == 36):
                        card4_player = Image.open(PATH +"/img/cards/"+Card35.img_file+".png").resize((160,250))
                        self.card4_player = ImageTk.PhotoImage(card4_player)
                        self.label_card3_player= tkinter.Label(master=self.frame_back, image=self.card4_player, borderwidth=0)
                        self.label_card3_player.place(x=1300, y=530)
                        player_points += Card35.points
                if(player_card4 == 37):
                        card4_player = Image.open(PATH +"/img/cards/"+Card36.img_file+".png").resize((160,250))
                        self.card4_player = ImageTk.PhotoImage(card4_player)
                        self.label_card3_player= tkinter.Label(master=self.frame_back, image=self.card4_player, borderwidth=0)
                        self.label_card3_player.place(x=1300, y=530)
                        player_points += Card36.points
                if(player_card4 == 38):
                        card4_player = Image.open(PATH +"/img/cards/"+Card37.img_file+".png").resize((160,250))
                        self.card4_player = ImageTk.PhotoImage(card4_player)
                        self.label_card3_player= tkinter.Label(master=self.frame_back, image=self.card4_player, borderwidth=0)
                        self.label_card3_player.place(x=1300, y=530)
                        player_points += Card37.points
                if(player_card4 == 39):
                        card4_player = Image.open(PATH +"/img/cards/"+Card38.img_file+".png").resize((160,250))
                        self.card4_player = ImageTk.PhotoImage(card4_player)
                        self.label_card3_player= tkinter.Label(master=self.frame_back, image=self.card4_player, borderwidth=0)
                        self.label_card3_player.place(x=1300, y=530)
                        player_points += Card38.points
                if(player_card4 == 40):
                        card4_player = Image.open(PATH +"/img/cards/"+Card39.img_file+".png").resize((160,250))
                        self.card4_player = ImageTk.PhotoImage(card4_player)
                        self.label_card3_player= tkinter.Label(master=self.frame_back, image=self.card4_player, borderwidth=0)
                        self.label_card3_player.place(x=1300, y=530)
                        player_points += Card39.points
                if(player_card4 == 41):
                        card4_player = Image.open(PATH +"/img/cards/"+Card40.img_file+".png").resize((160,250))
                        self.card4_player = ImageTk.PhotoImage(card3_player)
                        self.label_card3_player= tkinter.Label(master=self.frame_back, image=self.card4_player, borderwidth=0)
                        self.label_card3_player.place(x=1300, y=530)
                        player_points += Card40.points
                if(player_card4 == 42):
                        card3_player = Image.open(PATH +"/img/cards/"+Card41.img_file+".png").resize((160,250))
                        self.card3_player = ImageTk.PhotoImage(card3_player)
                        self.label_card3_player= tkinter.Label(master=self.frame_back, image=self.card3_player, borderwidth=0)
                        self.label_card3_player.place(x=1300, y=530)
                        player_points += Card41.points
                if(player_card4 == 43):
                        card4_player = Image.open(PATH +"/img/cards/"+Card42.img_file+".png").resize((160,250))
                        self.card4_player = ImageTk.PhotoImage(card3_player)
                        self.label_card3_player= tkinter.Label(master=self.frame_back, image=self.card4_player, borderwidth=0)
                        self.label_card3_player.place(x=1300, y=530)
                        player_points += Card42.points
                if(player_card4 == 44):
                        card4_player = Image.open(PATH +"/img/cards/"+Card43.img_file+".png").resize((160,250))
                        self.card4_player = ImageTk.PhotoImage(card4_player)
                        self.label_card3_player= tkinter.Label(master=self.frame_back, image=self.card4_player, borderwidth=0)
                        self.label_card3_player.place(x=1300, y=530)
                        player_points += Card43.points
                if(player_card4 == 45):
                        card4_player = Image.open(PATH +"/img/cards/"+Card44.img_file+".png").resize((160,250))
                        self.card4_player = ImageTk.PhotoImage(card4_player)
                        self.label_card3_player= tkinter.Label(master=self.frame_back, image=self.card4_player, borderwidth=0)
                        self.label_card3_player.place(x=1300, y=530)
                        player_points += Card44.points
                if(player_card4 == 46):
                        card4_player = Image.open(PATH +"/img/cards/"+Card45.img_file+".png").resize((160,250))
                        self.card4_player = ImageTk.PhotoImage(card4_player)
                        self.label_card3_player= tkinter.Label(master=self.frame_back, image=self.card4_player, borderwidth=0)
                        self.label_card3_player.place(x=1300, y=530)
                        player_points += Card45.points
                if(player_card4 == 47):
                        card4_player = Image.open(PATH +"/img/cards/"+Card46.img_file+".png").resize((160,250))
                        self.card4_player = ImageTk.PhotoImage(card4_player)
                        self.label_card3_player= tkinter.Label(master=self.frame_back, image=self.card4_player, borderwidth=0)
                        self.label_card3_player.place(x=1300, y=530)
                        player_points += Card46.points
                if(player_card4 == 48):
                        card4_player = Image.open(PATH +"/img/cards/"+Card47.img_file+".png").resize((160,250))
                        self.card4_player = ImageTk.PhotoImage(card4_player)
                        self.label_card3_player= tkinter.Label(master=self.frame_back, image=self.card4_player, borderwidth=0)
                        self.label_card3_player.place(x=1300, y=530)
                        player_points += Card47.points
                         
            self.label_player_points.configure(text=str(player_points))
            self.label_dealer_points.configure(text="??")
            self.figar_apuesta.configure(state="enabled")
            self.button_add_coin1.configure(state="enabled")
            self.button_add_coin10.configure(state="enabled")
            self.button_add_coin100.configure(state="enabled")
            self.button_add_coin1000.configure(state="enabled")
            self.button_rest_coin1.configure(state="enabled")
            self.button_rest_coin10.configure(state="enabled")
            self.button_rest_coin100.configure(state="enabled")
            self.button_rest_coin1000.configure(state="disenabledabled")
            self.end_game.configure(state="disabled")
            self.anadir_carta.configure(state="disabled")
            self.figar_apuesta.configure(state="enabled")
        
        def set_bet():
            if(bet > 0):
                self.figar_apuesta.configure(state="disabled")
                self.button_add_coin1.configure(state="disabled")
                self.button_add_coin10.configure(state="disabled")
                self.button_add_coin100.configure(state="disabled")
                self.button_add_coin1000.configure(state="disabled")
                self.button_rest_coin1.configure(state="disabled")
                self.button_rest_coin10.configure(state="disabled")
                self.button_rest_coin100.configure(state="disabled")
                self.button_rest_coin1000.configure(state="disabled")
                self.end_game.configure(state="enabled")
                self.anadir_carta.configure(state="enabled")
        def new_game():
            global player_points
            global dealer_points
            player_points = 0
            dealer_points = 0
            self.label_card0_player= tkinter.Label(master=self.frame_back, image=self.holder_card,borderwidth=0)
            self.label_card0_player.place(x=500, y=530) 
            self.label_card1_player= tkinter.Label(master=self.frame_back, image=self.holder_card,borderwidth=0)
            self.label_card1_player.place(x=700, y=530) 
            self.label_card2_player= tkinter.Label(master=self.frame_back, image=self.holder_card,borderwidth=0)
            self.label_card2_player.place(x=900, y=530) 
            self.label_card3_player= tkinter.Label(master=self.frame_back, image=self.holder_card,borderwidth=0)
            self.label_card3_player.place(x=1100, y=530) 
            self.label_card4_player= tkinter.Label(master=self.frame_back, image=self.holder_card,borderwidth=0)
            self.label_card4_player.place(x=1300, y=530)
            self.label_card0_dealer= tkinter.Label(master=self.frame_back, image=self.holder_card,borderwidth=0)
            self.label_card0_dealer.place(x=500, y=250) 
            self.label_card1_dealer= tkinter.Label(master=self.frame_back, image=self.holder_card,borderwidth=0)
            self.label_card1_dealer.place(x=700, y=250) 
            self.label_card2_dealer= tkinter.Label(master=self.frame_back, image=self.holder_card,borderwidth=0)
            self.label_card2_dealer.place(x=900, y=250) 
            self.label_card3_dealer= tkinter.Label(master=self.frame_back, image=self.holder_card,borderwidth=0)
            self.label_card3_dealer.place(x=1100, y=250) 
            self.label_card4_dealer= tkinter.Label(master=self.frame_back, image=self.holder_card,borderwidth=0)
            self.label_card4_dealer.place(x=1300, y=250)
            self.end_game.configure(state="disabled")
            self.anadir_carta.configure(state="disabled")
            self.figar_apuesta.configure(state="enabled")
            self.button_add_coin1.configure(state="enabled")
            self.button_add_coin10.configure(state="enabled")
            self.button_add_coin100.configure(state="enabled")
            self.button_add_coin1000.configure(state="enabled")
            self.button_rest_coin1.configure(state="enabled")
            self.button_rest_coin10.configure(state="enabled")
            self.button_rest_coin100.configure(state="enabled")
            self.button_rest_coin1000.configure(state="enabled")
            play(self)
            self.new_hand.configure(state="disabled")
             
        def end_game():
            global player_points
            global dealer_points
            global hand_wins
            global bet
            global money
            global hand_loses
            self.label_dealer_points.configure(text=str(dealer_points))
            if(player_points > 21):
                Win = False
                hand_loses += 1
            elif(dealer_points > 21):
                Win = True              
            elif(player_points > dealer_points):
                Win = True
            elif(player_points == dealer_points):
                Win = False
                money += bet
            else:
                Win = False
                hand_loses += 1
            if(Win):
                hand_wins += 1
                money += 2*bet
            bet = 0
            self.label_wins.configure(text="Wins:"+str(hand_wins)) 
            self.label_loses.configure(text="Loses: "+str(hand_loses))
            self.label_apuesta.configure(text="Apuesta: $"+str(bet))
            self.label_money.configure(text="$"+str(money))
            self.new_hand.configure(state="enabled")
                   
        def add_bet(value):
            global bet
            global money
            bet += value
            money -= value
            self.label_apuesta.configure(text="Apuesta: $"+str(bet))
            self.label_money.configure(text="$"+str(money))
        
        def res_bet(value):
            global bet
            global money
            bet -= value
            money += value
            self.label_apuesta.configure(text="Apuesta: $"+str(bet))
            self.label_money.configure(text="$"+str(money))
        
        def on_closing(self, event=0):
            self.destroy()
        
            
                
                
                            
if __name__ == "__main__":
    app = App()
    app.mainloop()