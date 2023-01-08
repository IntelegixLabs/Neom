import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox, Frame, filedialog, Label, DISABLED
from PIL import Image, ImageTk
import cv2
import configparser
import json
import os


class CreateToolTip(object):

    def __init__(self, widget, text='widget info'):
        self.waittime = 500
        self.wraplength = 180
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.leave)
        self.widget.bind("<ButtonPress>", self.leave)
        self.id = None
        self.tw = None

    def enter(self, event=None):
        self.schedule()

    def leave(self, event=None):
        self.unschedule()
        self.hidetip()

    def schedule(self):
        self.unschedule()
        self.id = self.widget.after(self.waittime, self.showtip)

    def unschedule(self):
        id = self.id
        self.id = None
        if id:
            self.widget.after_cancel(id)

    def showtip(self, event=None):
        x = y = 0
        x, y, cx, cy = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 20
        self.tw = tk.Toplevel(self.widget)
        self.tw.wm_overrideredirect(True)
        self.tw.wm_geometry("+%d+%d" % (x, y))
        label = tk.Label(self.tw, text=self.text, justify='left',
                         background="#ffffff", relief='solid', borderwidth=1,
                         wraplength=self.wraplength)
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tw
        self.tw = None
        if tw:
            tw.destroy()


version = '1.0.1'


def main():
    def loading():
        rootx = tk.Tk()
        rootx.iconbitmap(default='Data/Images/icons/favicon.ico')
        rootx.image = tk.PhotoImage(file='Data/Images/Background/load.gif')
        labelx = tk.Label(rootx, image=rootx.image, bg='white')
        rootx.overrideredirect(True)
        rootx.geometry("+600+100")
        rootx.wm_attributes("-topmost", True)
        rootx.wm_attributes("-disabled", True)
        rootx.wm_attributes("-transparentcolor", "white")
        labelx.pack()
        labelx.after(500, lambda: labelx.destroy())
        rootx.after(500, lambda: rootx.destroy())  # Destroy the widget after 0.5 seconds
        labelx.mainloop()

    for i in range(0, 1):
        loading()

    def display():

        class Store_DATA_IN_INI:

            def __init__(self, win):

                load = cv2.imread('Data/Images/Background/background.jpg', 1)
                cv2imagex1 = cv2.cvtColor(load, cv2.COLOR_BGR2RGBA)
                load = Image.fromarray(cv2imagex1)
                regx = tk.Tk()
                load = load.resize((int(regx.winfo_screenwidth()), int(regx.winfo_screenheight())), Image.LANCZOS)

                render = ImageTk.PhotoImage(load)
                img = tk.Label(image=render)
                img.image = render
                img.place(x=-1, y=0)

                load = cv2.imread('Data/Images/Background/logo.png', 1)
                cv2imagex1 = cv2.cvtColor(load, cv2.COLOR_BGR2RGBA)
                load = Image.fromarray(cv2imagex1)
                load = load.resize((int(250), int(160)), Image.LANCZOS)
                render = ImageTk.PhotoImage(load)
                img = tk.Label(image=render)
                img.image = render
                img.place(x=1665, y=0)

                self.b0 = tk.Button(win,
                                    bg='#f7421e',
                                    fg='#b7f731',
                                    relief='flat',
                                    width=20, command=self.quit)
                self.b0.place(x=0, y=0, width=150, height=150)

                self.b0b = tk.Button(win,
                                     bg='#33ff00',
                                     fg='#b7f731',
                                     relief='flat',
                                     width=100, command=self.settings)
                self.b0b.place(x=1770, y=950, width=150, height=150)

                self.b1 = ttk.Button(win, text='Pot Holes Detection', width=20, command=self.pot_holes)
                self.b1.place(x=90, y=470, width=300, height=100)

                self.b2 = ttk.Button(win, text='Uploaded Data Viewer', width=20, command=self.data_viewer)
                self.b2.place(x=300, y=780, width=300, height=100)

                self.b3 = ttk.Button(win, text='Live Dash Cam', width=20, command=self.dash_cam)
                self.b3.place(x=1400, y=220, width=300, height=100)

                self.b4 = ttk.Button(win, text='Label Picture', width=20, command=self.label_picture)
                self.b4.place(x=1480, y=530, width=300, height=100)

                regx.destroy()

            def settings(self):

                class TOKENS:

                    def __init__(self, tokens):

                        config = configparser.ConfigParser()
                        config.read('Data/Keys/config.ini')
                        config_token = config.items('TOKEN')
                        TOKEN = str(config_token[0][1])
                        UP_URL = str(config_token[1][1])

                        self.lbl = tk.Label(tokens, text="TOKEN", font=("Helvetica", 30, 'bold'), bg='white')
                        self.lbl.place(x=60, y=70)

                        self.txtfld1 = ttk.Combobox(tokens, font=("Helvetica", 30, 'bold'))
                        self.txtfld1.place(x=220, y=70, width=550)
                        self.txtfld1.set(TOKEN)

                        self.lb2 = tk.Label(tokens, text="USER", font=("Helvetica", 30, 'bold'), bg='white')
                        self.lb2.place(x=60, y=170)

                        self.txtfld2 = ttk.Combobox(tokens, font=("Helvetica", 30, 'bold'))
                        self.txtfld2.place(x=220, y=170, width=550)
                        self.txtfld2.set(UP_URL)

                        self.btn = ttk.Button(tokens, text="UPDATE", width=20, command=self.token_validate)
                        self.btn.place(x=500, y=250, width=270, height=50)

                    def token_validate(self):
                        if (str(self.txtfld1.get()) != "") and (str(self.txtfld2.get()) != ""):

                            config = configparser.ConfigParser()
                            config.write('Data/Keys/config.ini')

                            file = open('Data/Keys/config.ini', "w+")

                            config.add_section('TOKEN')
                            config.set('TOKEN', 'TOKEN', str(self.txtfld1.get()))
                            config.set('TOKEN', 'UP_URL', str(self.txtfld2.get()))

                            config.write(file)
                            file.close()

                            tk.messagebox.showinfo("Success", "Updated Successfully")

                            tokens_user_login.destroy()

                        else:
                            tk.messagebox.showerror("Error", "EMPTY VALUES")

                    @staticmethod
                    def quit():
                        tokens_user_login.destroy()

                tokens_user_login = tk.Tk()
                tokens_user_login.config(background='white')
                tokens_user_login.attributes('-alpha', 0.9)

                TOKENS(tokens_user_login)
                tokens_user_login.iconbitmap(default='DATA/Images/icons/favicon.ico')
                tokens_user_login.title('Neom  Car Dashboard Settings ' + version)
                tokens_user_login.geometry("850x350")
                tokens_user_login.mainloop()

            @staticmethod
            def quit():
                window_user_login1.destroy()
                exit(0)

            @staticmethod
            def pot_holes(self):
                window_user_login1.destroy()
                # second(user_key=user_key, job="HOSTEL ENVIRONMENT")

            def data_viewer(self):
                window_user_login1.destroy()
                data_viewer()

            @staticmethod
            def dash_cam(self):
                window_user_login1.destroy()
                # second(user_key=user_key, job="BUS ENVIRONMENT")

            @staticmethod
            def label_picture(self):
                window_user_login1.destroy()
                # second(user_key=user_key, job="EXAM ENVIRONMENT")

            @staticmethod
            def start(self):
                window_user_login1.destroy()
                # second(user_key=user_key, job="START ENVIRONMENT")

        window_user_login1 = tk.Tk()
        window_user_login1.config(background='#EFEFEF')
        window_user_login1.attributes('-fullscreen', True)

        Store_DATA_IN_INI(window_user_login1)
        window_user_login1.iconbitmap(default='DATA/Images/icons/favicon.ico')
        window_user_login1.title('Neom')
        window_user_login1.mainloop()

    def data_viewer():

        class View_Image:

            def __init__(self, win):

                self.label_class = {0: 'POTHOLES', 1: 'GRAFFITI', 2: 'FADED SIGNAGE', 3: 'GARBAGE',
                                    4: 'CONSTRUCTION ROAD', 5: 'BROKEN SIGNAGE', 6: 'BAD STREETLIGHT',
                                    7: 'BAD BILLBOARD', 8: 'SAND ON ROAD', 9: 'CLUTTER SIDEWALK',
                                    10: 'UNKEPT FACADE'}

                self.image_class = {'POTHOLES': 0, 'GRAFFITI': 1, 'FADED SIGNAGE': 2, 'GARBAGE': 3,
                                    'CONSTRUCTION ROAD': 4, 'BROKEN SIGNAGE': 5, 'BAD STREETLIGHT': 6,
                                    'BAD BILLBOARD': 7, 'SAND ON ROAD': 8, 'CLUTTER SIDEWALK': 9,
                                    'UNKEPT FACADE': 10}

                load = cv2.imread('Data/Images/Background/background_2.jpg', 1)
                cv2imagex1 = cv2.cvtColor(load, cv2.COLOR_BGR2RGBA)
                load = Image.fromarray(cv2imagex1)
                load = load.resize((int(1920), int(1080)), Image.LANCZOS)
                render = ImageTk.PhotoImage(load)
                img = tk.Label(image=render)
                img.image = render
                img.place(x=0, y=0)
                # LABEL AND TEXT BOX TO ENTER DETAILS OF ALL ELEMENTS OF A STATION
                self.lb_title = Label(win, text="Capability",
                                      font=("Ariel", 30, 'underline'), bg='#F7F7F9')
                self.lb_title.place(x=550, y=110)

                self.lb1 = Label(win, text="User Id", font=("Helvetica", 20), bg='#F7F7F9')
                self.lb1.place(x=60, y=350)

                self.txtfld1 = ttk.Combobox(win, font=("Helvetica", 20), )
                self.txtfld1.place(x=300, y=350)
                self.txtfld1.configure(state=DISABLED)

                self.lb2 = Label(win, text="Image Class", fg='black', font=("Helvetica", 20), bg='#F7F7F9')
                self.lb2.place(x=650, y=350)

                self.txtfld2 = ttk.Combobox(win, font=("Helvetica", 20),
                                            values=['POTHOLES', 'GRAFFITI', 'FADED SIGNAGE', 'GARBAGE',
                                                    'CONSTRUCTION ROAD', 'BROKEN SIGNAGE', 'BAD STREETLIGHT',
                                                    'BAD BILLBOARD', 'SAND ON ROAD', 'CLUTTER SIDEWALK',
                                                    'UNKEPT FACADE'])
                self.txtfld2.place(x=890, y=350)
                self.txtfld2.set("")

                self.lb3 = Label(win, text="W Coordinate", fg='black', font=("Helvetica", 20), bg='#F7F7F9')
                self.lb3.place(x=60, y=425)

                self.txtfld3 = ttk.Combobox(win, font=("Helvetica", 20))
                self.txtfld3.place(x=300, y=425)
                self.txtfld3.set("")

                self.lb4 = Label(win, text="X Coordinate", fg='black', font=("Helvetica", 20), bg='#F7F7F9')
                self.lb4.place(x=650, y=425)
                self.txtfld4 = ttk.Combobox(win, font=("Helvetica", 20))
                self.txtfld4.place(x=890, y=425)
                self.txtfld4.set("")

                self.lb5 = Label(win, text="Y Coordinate", fg='black', font=("Helvetica", 20), bg='#F7F7F9')
                self.lb5.place(x=60, y=500)

                self.txtfld5 = ttk.Combobox(win, font=("Helvetica", 20))
                self.txtfld5.place(x=300, y=500)
                self.txtfld5.set("")

                self.lb6 = Label(win, text="Z Coordinate", fg='black', font=("Helvetica", 20), bg='#F7F7F9')
                self.lb6.place(x=650, y=500)

                self.txtfld6 = ttk.Combobox(win, font=("Helvetica", 20))
                self.txtfld6.place(x=890, y=500)
                self.txtfld6.set("")

                self.lb7 = Label(win, text="Latitude", fg='black', font=("Helvetica", 20), bg='#F7F7F9')
                self.lb7.place(x=60, y=575)

                self.txtfld7 = ttk.Combobox(win, font=("Helvetica", 20))
                self.txtfld7.place(x=300, y=575)
                self.txtfld7.set("")

                self.lb8 = Label(win, text="Longitude", fg='black', font=("Helvetica", 20), bg='#F7F7F9')
                self.lb8.place(x=650, y=575)

                self.txtfld8 = ttk.Combobox(win, font=("Helvetica", 20))
                self.txtfld8.place(x=890, y=575)
                self.txtfld8.set("")

                self.btn_submit = ttk.Button(win, text="SUBMIT")
                self.btn_submit.place(x=600, y=660, width=250, height=60)

                # listx = []
                #
                # iter = 0
                #
                # path = 'Data/Saved_Images'
                #
                # print(path)
                #
                # for dirname, _, filenames in os.walk(path):
                #     for filename in filenames:
                #         print(path + '/' + filename)
                #         listx.append(str(path + '/' + filename))
                #
                # load = cv2.imread('Data/Images/Background/logo.png', 1)
                # cv2imagex1 = cv2.cvtColor(load, cv2.COLOR_BGR2RGBA)
                # load = Image.fromarray(cv2imagex1)
                # load = load.resize((int(70), int(70)), Image.ANTIALIAS)
                # render = ImageTk.PhotoImage(load)
                # img = tk.Label(image=render)
                # img.image = render
                # img.place(x=0, y=700)
                #
                # img1 = tk.Label(image=render)
                # img1.image = render
                #
                # img1.place(x=1296, y=700)

                # print(listx)
                #
                # listx = sorted(listx, reverse=True)
                #
                # print(listx)
                #
                # def image_viewer(iter, key=0):
                #
                #     print("ft", iter)
                #
                #     if iter > len(listx) - 1:
                #         iter = len(listx) - 1
                #
                #     if iter <= -1:
                #         iter = 0
                #
                #     print(iter)
                #
                #     load = cv2.imread(listx[iter], 1)
                #     cv2imagex1 = cv2.cvtColor(load, cv2.COLOR_BGR2RGBA)
                #     load = Image.fromarray(cv2imagex1)
                #     regx = tk.Tk()
                #     load = load.resize(
                #         (int(regx.winfo_screenwidth()) - 140, int(regx.winfo_screenheight()) - 70),
                #         Image.ANTIALIAS)
                #
                #     render = ImageTk.PhotoImage(load)
                #     img = tk.Label(image=render)
                #     img.image = render
                #     img.place(x=70, y=70)
                #
                #     regx.destroy()
                #
                #     if key == 2:
                #
                #         try:
                #             self.forward_right.destroy()
                #             self.forward_right = ttk.Button(win, text=">", style='my.TButton', width=20,
                #                                             command=lambda: image_viewer(iter + 1, key=2))
                #             self.forward_right.place(x=1296, y=70, width=74, height=632)
                #         except:
                #             pass
                #
                #         try:
                #             self.back_left.destroy()
                #
                #             self.back_left = ttk.Button(win, text="<", style='my.TButton', width=20,
                #                                         command=lambda: image_viewer(iter - 1, key=1))
                #             self.back_left.place(x=0, y=70, width=74, height=632)
                #         except:
                #             pass
                #
                #     if key == 1:
                #         try:
                #             self.back_left.destroy()
                #
                #             self.back_left = ttk.Button(win, text="<", style='my.TButton', width=20,
                #                                         command=lambda: image_viewer(iter - 1, key=1))
                #             self.back_left.place(x=0, y=70, width=74, height=632)
                #         except:
                #             pass
                #
                #         try:
                #             self.forward_right.destroy()
                #             self.forward_right = ttk.Button(win, text=">", style='my.TButton', width=20,
                #                                             command=lambda: image_viewer(iter + 1, key=2))
                #             self.forward_right.place(x=1296, y=70, width=74, height=632)
                #         except:
                #             pass
                #
                #     return iter
                #
                # image_viewer(iter)
                #

                #
                # s = ttk.Style()
                # s.configure('my.TButton', font=('Aerial', 25, 'bold'))
                #
                # self.back_left = ttk.Button(win, text="<", style='my.TButton', width=20,
                #                             command=lambda: image_viewer(iter - 1, key=1))
                # self.back_left.place(x=0, y=70, width=74, height=632)
                #
                # self.forward_right = ttk.Button(win, text=">", style='my.TButton', width=20,
                #                                 command=lambda: image_viewer(iter + 1, key=2))
                # self.forward_right.place(x=1296, y=70, width=74, height=632)
                #
                # self.h0 = ttk.Button(win, style='my.TButton', width=20)
                # self.h0.place(x=70, y=-1, width=1226, height=72)

                self.temp_values = []

                with open('Data/Data/sample.json', 'r') as openfile:
                    # Reading from json file
                    json_object = json.load(openfile)
                    for each in json_object["data"]:
                        self.temp_values.append([each["userid"], each["image_url"], each["w_cord"], each["x_cord"],
                                                 each["y_cord"], each["z_cord"], each["latitude"], each["longitude"],
                                                 each["class_of_image"], each["auto"], each["uploaded"]])

                self.frame = Frame(win)
                self.frame.place(x=20, y=755)

                self.tree = ttk.Treeview(self.frame, columns=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12), height=14,
                                         show="headings")
                self.tree.pack(side='left')

                self.val = ["serial No", "User Id", "Image Url", "W Coordinate", "X Coordinate", "Y Coordinate",
                            "Z Coordinate", "Latitude", "Longitude", "Class Of Image", "Auto", "Uploaded"]

                for i in range(1, len(self.val) + 1):
                    self.tree.heading(i, text=self.val[i - 1])

                for i in range(1, len(self.val) + 1):
                    self.tree.column(i, width=156, anchor='center')

                self.scroll1 = ttk.Scrollbar(self.frame, orient="vertical", command=self.tree.yview)
                self.scroll1.pack(side='right', fill='y')

                for i in range(len(self.temp_values)):
                    if str(self.temp_values[i][10]) == "Yes":
                        self.tree.insert('', 'end', values=(str(i),
                                                            str(self.temp_values[i][0]), str(self.temp_values[i][1]),
                                                            str(self.temp_values[i][2])
                                                            , str(self.temp_values[i][3]), str(self.temp_values[i][4]),
                                                            str(self.temp_values[i][5]),
                                                            str(self.temp_values[i][6]), str(self.temp_values[i][7]),
                                                            str(self.label_class[self.temp_values[i][8]]),
                                                            str(self.temp_values[i][9]), str(self.temp_values[i][10])),
                                         tags=('odd',))
                    else:
                        self.tree.insert('', 'end', values=(str(i),
                                                            str(self.temp_values[i][0]), str(self.temp_values[i][1]),
                                                            str(self.temp_values[i][2])
                                                            , str(self.temp_values[i][3]), str(self.temp_values[i][4]),
                                                            str(self.temp_values[i][5]),
                                                            str(self.temp_values[i][6]), str(self.temp_values[i][7]),
                                                            str(self.label_class[self.temp_values[i][8]]),
                                                            str(self.temp_values[i][9]), str(self.temp_values[i][10])),
                                         tags=('even',))

                self.tree.tag_configure('odd', background='#CCFF99')
                self.tree.tag_configure('even', background='#FFFF99')

                self.b0 = tk.Button(win,
                                    bg='#33ff00',
                                    fg='#b7f731',
                                    relief='flat',
                                    width=20, command=self.back)
                self.b0.place(x=0, y=0, width=150, height=150)

                self.b0r = tk.Button(win,
                                     bg='#f7421e',
                                     fg='#b7f731',
                                     relief='flat',
                                     width=20, command=self.quit)
                self.b0r.place(x=1296, y=0, width=150, height=150)

            @staticmethod
            def quit():
                window_user_login3.destroy()
                exit(0)

            @staticmethod
            def back():
                window_user_login3.destroy()
                display()

        window_user_login3 = tk.Tk()
        window_user_login3.config(background='#EFEFEF')
        window_user_login3.attributes('-fullscreen', True)

        View_Image(window_user_login3)
        window_user_login3.iconbitmap(default='DATA/Images/icons/favicon.ico')
        window_user_login3.title('Neom')
        window_user_login3.mainloop()

    display()


if __name__ == '__main__':
    main()
