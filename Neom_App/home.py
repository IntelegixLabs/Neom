import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import cv2
import configparser


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

            @staticmethod
            def dash_cam(self):
                window_user_login1.destroy()
                # second(user_key=user_key, job="BUS ENVIRONMENT")

            @staticmethod
            def data_viewer(self):
                window_user_login1.destroy()
                # second(user_key=user_key, job="EXAM ENVIRONMENT")

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

    display()


if __name__ == '__main__':
    main()
