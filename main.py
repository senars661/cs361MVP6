from tkinter import *
from PIL import ImageTk,Image
import json
# window = Tk()
# window.title("Welcome to my Melee Project")
#
# # https://github.com/ETossed/2021MeleeH2H/blob/main/data/World/Full_Year/MPGR_FY.json data from there
f = open('players.json')
data = json.load(f)
val = input("Please enter a player: ")
for player in data:
    if val == player:
        print(data[player])