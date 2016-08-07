#! /usr/bin/env python


# coding: UTF-8
# python3.3/python2.7
try:
    from tkinter import *
    import tkinter as tk
    from tkinter.messagebox import askquestion
    from tkinter.messagebox import showinfo
except:
    from Tkinter import *
    import Tkinter as tk
#     from tkMessageBox import askquestion
#     from tkMessageBox import showinfo
import time
import datetime
import random

import model

SIDE = 4
# just used by backward function


matrix_stack = [] 
# just used by forward function


matrix_stack_forward = []

root_bg = 'snow'
start_time = datetime.datetime.now()
check_is_win_flag = True
play_flag = True

class Application():
    def __init__(self, root):
        '''

        Init Form

        '''
        self.root = root
        self.createFrameTop()
        self.createFrameMiddle()
        self.createFrameBottom()
        self.matrix = model.init()
        self.root['bg'] = root_bg
        self.root.bind("<KeyPress> ", self.bind_key)

    def createFrameTop(self):
        '''

        Create LabelFrame Top

        '''
        show_list = ["Score:", "0", "Step:", "0"]

        self.frm_top = tk.LabelFrame(self.root, bg=root_bg, font=('Tempus Sans ITC', 10))
        self.frm_top.grid(row = 0, column = 0, padx = 15, pady = 2,sticky = "wesn")

        self.label_top_list = []
        for (i, operate) in enumerate(show_list):
            label_top = tk.Label(self.frm_top, width = 15, height=2, bg=root_bg, text=show_list[i], font=('Tempus Sans ITC', 15))
            label_top.grid(row = i//4, column = i%4, padx = 5, pady = 2, sticky = "wesn")
            self.label_top_list.append(label_top)

    def createFrameMiddle(self):
        '''

        Create LabelFrame Middle

        '''
        self.frm_middle = tk.LabelFrame(self.root, bg=root_bg, font=('Tempus Sans ITC', 10))
        self.frm_middle.grid(row = 1, column = 0, padx = 15, pady = 2, sticky = "wesn")

        self.createFrameMiddleLeft()
        self.createFrameMiddleRight()

    def createFrameMiddleLeft(self):
        '''

        Create LabelFrame Middle Left

        '''
        self.frm_middle_left = tk.LabelFrame(self.frm_middle, bg='#BBADA0', font=('Tempus Sans ITC', 10))
        self.frm_middle_left.grid(row = 0, column = 0, padx = 5, pady = 2,sticky = "wesn")

        self.btn_middle_list = []
        for i in range(SIDE*SIDE):
            entry_bottom = tk.Button(self.frm_middle_left, bg="#CCC0B4", relief='flat', 
                    width = 4, height=2, borderwidth=1, font=('Dotum', 20, "bold"))
            entry_bottom.grid(row = i//SIDE, column = i%SIDE, padx = 5, pady = 4, sticky = "wesn")
            self.btn_middle_list.append(entry_bottom)

    def createFrameMiddleRight(self):
        '''

        Create LabelFrame Middle Right

        '''
        operate_list = ["Operating Instructions:", 
                        "↑    --    Up", "↓    --    Down", "←    --    Left", "→    --    Right",
                        "s    --    Start/Reset", "b    --    Backward", "f    --    Forward", "q    --    Quit"]

        self.frm_middle_right = tk.LabelFrame(self.frm_middle, bg=root_bg, font=('Tempus Sans ITC', 10))
        self.frm_middle_right.grid(row = 0, column = 1, padx = 5, pady = 2,sticky = "wesn")

        for (i, operate) in enumerate(operate_list):
            label_middle_right = tk.Label(self.frm_middle_right, width=30, height=1, bg=root_bg, text=operate, font=('Tempus Sans ITC', 15))
            label_middle_right.grid(row = i, column = 0, padx = 5, pady = 2, sticky = "w")

    def createFrameBottom(self):
        '''

        Create LabelFrame Bottom

        '''
        show_list = ["Time:", "0", "0"]

        self.frm_bottom = tk.LabelFrame(self.root, bg=root_bg, font=('Tempus Sans ITC', 10))
        self.frm_bottom.grid(row = 2, column = 0, padx = 15, pady = 2, sticky = "wesn")

        self.label_bottom_list = []
        for (i, operate) in enumerate(show_list):
            label_bottom = tk.Label(self.frm_bottom, width = (i+1)*12, height=2, bg=root_bg, text=show_list[i], font=('Tempus Sans ITC', 12))
            label_bottom.grid(row = i//3, column = i%3, padx = 5, pady = 2, sticky = "w")
            self.label_bottom_list.append(label_bottom)
        self.show_time()

    def bind_key(self, event):
        '''

        key event

        '''
        global play_flag

        if play_flag:
            if  event.keysym.lower() not in ["q", "s"]:
                return

        if model.is_over(self.matrix):
            if askquestion("GAME OVER","GAME OVER!\nDo you want to init it?") == 'yes':
                self.reset_game()
                return
            else:
                self.root.destroy()
        else:
            if event.keysym.lower() == "q":
                self.root.destroy()
            elif event.keysym.lower() == "s":
                self.reset_game()
                return
            elif event.keysym == "Left":
                self.matrix = model.move_left(self.matrix)
            elif event.keysym == "Right":
                self.matrix = model.move_right(self.matrix)
            elif event.keysym == "Up":
                self.matrix = model.move_up(self.matrix)
            elif event.keysym == "Down":
                self.matrix = model.move_down(self.matrix)
            elif event.keysym.lower() == "b":
                self.backward()
            elif event.keysym.lower() == "f":
                self.forward()
            
            if event.keysym.lower() in ["q", "left", "right", "up", "down"]:
                try:
                    self.matrix = model.insert(self.matrix)    
                    matrix_stack.append(list([self.matrix, model.g_score]))
                    del matrix_stack_forward[0:]
                except:
                    pass
            try:
                self.label_top_list[1]['text'] = model.g_score
                self.btn_show_matrix(self.matrix)
            except:
                pass
        if check_is_win_flag:
            self.is_win()     

    def btn_show_matrix(self, matrix):
        '''

        show matrix

        '''
        # num : [bg, fg]


        btn_color_dict = {
                            0 : ['#CCC0B4', '#CCC0B4'], 
                            2 : ['#EEE4DA', '#776E65'], 
                            4 : ['#EDE0C8', '#776E65'], 
                            8 : ['#F2B179', '#FFFFFF'],
                            16 : ['#EC8D54', '#FFFFFF'], 
                            32 : ['#F67C5F', '#FFFFFF'], 
                            64 : ['#EA5937', '#FFFFFF'],
                            128 : ['#804000', '#FFFFFF'], 
                            256 : ['#F1D04B', '#FFFFFF'], 
                            512 : ['#E4C02A', '#FFFFFF'],
                            1024 : ['#EE7600', '#FFFFFF'], 
                            2048 : ['#D5A500', '#FFFFFF'],
                            4096 : ['#E4C02A', '#FFFFFF'],
                            8192 : ['#804000', '#FFFFFF'],
                            16384 : ['#EA5937', '#FFFFFF'],
                            32768 : ['#EE7600', '#FFFFFF']
                         }

        for (i,btn_item) in enumerate(self.btn_middle_list):
            btn_item['text'] = matrix[i//4][i%4]

        for btn_item in self.btn_middle_list:
            btn_color_list = btn_color_dict[int(btn_item['text'])]
            btn_item['bg'] = btn_color_list[0]
            btn_item['fg'] = btn_color_list[1]

            if int(btn_item['text']) == 0:
                btn_item['text'] = ''

        step = len(matrix_stack) - 1
        self.label_top_list[3]['text'] = step

    def show_time(self):
        '''

        Displays the current time

        '''
        now = str(time.strftime('%Y-%m-%d %H:%M:%S'))
        self.label_bottom_list[2].config(text=now)
        self.root.after(1024, self.show_time)

    def show_play_time(self):
        '''

        Displays the play time

        '''
        global start_time
        global play_flag
        if play_flag:
            start_time = datetime.datetime.now()
            play_flag = False
        end_time = datetime.datetime.now()
        run_time = (end_time - start_time)
        self.label_bottom_list[1].config(text=str(run_time))
        self.root.after(64, self.show_play_time)

    def backward(self):
        if len(matrix_stack) == 1:
            showinfo('info', 'Cannot back anymore...')
        else:
            matrix_stack_forward.append([self.matrix, model.g_score])
            matrix_stack.pop()
            self.matrix = matrix_stack[-1][0]
            model.g_score = matrix_stack[-1][1]

    def forward(self):
        if len(matrix_stack_forward) == 0:
            showinfo('info', 'Cannot forward anymore...')
        else:
            self.matrix = matrix_stack_forward[-1][0]
            model.g_score = matrix_stack_forward[-1][1]
            matrix_stack_forward.pop()
            matrix_stack.append([self.matrix, model.g_score])

    def is_win(self):
        global check_is_win_flag
        if model.is_win(self.matrix):
            if askquestion("WIN","You win the game!\nDo you want to continue the game?") == 'yes':
                # self.matrix = my_init()


                check_is_win_flag = False
                self.btn_show_matrix(self.matrix)
                return
            else:
                self.root.destroy()

    def reset_game(self):
        '''

        reset game

        '''
        global play_flag
        self.matrix = model.init()
        
        model.g_score = 0
        self.label_top_list[1]['text'] = model.g_score

        del matrix_stack[0:]
        matrix_stack.append([self.matrix, model.g_score])
        self.btn_show_matrix(self.matrix)

        play_flag = True
        self.show_play_time()


if __name__=="__main__":
    '''

    main loop

    '''
    root = tk.Tk()
    root.title("2048")
    # root.iconbitmap('2048.ico')


    Application(root)
    # Set maximize invalid


    root.resizable(False,False)
    root.mainloop()
