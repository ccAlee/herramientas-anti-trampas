import subprocess
import tkinter
import tkinter.messagebox
import customtkinter
from datetime import date
from datetime import datetime
from PIL import Image


from tkinter import messagebox

import os, time, sys

import time


from discord_webhook import DiscordWebhook, DiscordEmbed

from pymongo import MongoClient


customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

client = MongoClient('URI')
db = client['DB']
collection = db.asd



class login(customtkinter.CTk):
     def __init__(self):
          super().__init__()

          customtkinter.set_appearance_mode("dark")
          customtkinter.set_default_color_theme("green")

          self.title("Frozy | SS-Tool")

          self.geometry("500x350")

          ruta = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))

          self.maxsize(500, 350)

          self.minsize(500, 350)

          self.iconbitmap(ruta+"/logo.ico")

     


          frame = customtkinter.CTkFrame(master=self, fg_color="#1B2223")
          frame.pack(pady=20, padx=60, fill="both", expand=True)

            

          label = customtkinter.CTkLabel(master=frame, text="Frozy • Login System", font=("Roboto", 18))
          label.pack(pady=12, padx=10)



          entry1= customtkinter.CTkEntry(master=frame, placeholder_text="ID")
          entry1.pack(pady=12, padx=10)

          entry2= customtkinter.CTkEntry(master=frame, placeholder_text="Token", show="•")
          entry2.pack(pady=12, padx=10)


          icon = customtkinter.CTkImage(light_image=Image.open(ruta+"/logo_l.png"),
                                            dark_image=Image.open(ruta+"/logo.png"),
                                            size=(30, 30))

            

          button= customtkinter.CTkButton(master=frame, text="Start SS", command=login, image=icon)
          button.pack(pady=12, padx=10)

          label2 = customtkinter.CTkLabel(master=frame, text="Get the token in our discord server.")
          label2.pack(pady=20, padx=10)



class App2(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        global language, disable
        language = 1
        disable= False

        # configure window
        self.title("Frozy | SS-Tool")
        self.geometry(f"{1100}x{580}")

        self.maxsize(1100, 580)
        self.minsize(1100, 580)

        self.iconbitmap("logo.ico")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        ruta = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        icon = customtkinter.CTkImage(light_image=Image.open(ruta+"/logo_l.png"),
                                        dark_image=Image.open(ruta+"/logo_l.png"),
                                        size=(80, 80),
                                        )
        
        icon2 = customtkinter.CTkImage(light_image=Image.open(ruta+"/logo_l.png"),
                                        dark_image=Image.open(ruta+"/logo.png"),
                                        size=(25, 25))

        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(7, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Frozy", font=("Coroto", 26), image=icon)
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event2)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event, image=icon2)
        self.sidebar_button_3.grid(row=5, column=0, padx=20, pady=10)
        self.sidebar_button_4 = customtkinter.CTkButton(self.sidebar_frame, command=self.open_folders)
        self.sidebar_button_4.grid(row=3, column=0, padx=20, pady=10)
        self.sidebar_button_5 = customtkinter.CTkButton(self.sidebar_frame, command=self.virtual_machine)
        self.sidebar_button_5.grid(row=4, column=0, padx=20, pady=10)
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        self.sidebar_button_4.configure(text="Open Folders")

        self.sidebar_button_5.configure(text="Virtual Machine?")

        self.sidebar_button_2.configure(text="Open Regedit")


        self.label_premium = customtkinter.CTkLabel(self.sidebar_frame, text="Soon...\nto Premiun Users")
        self.label_premium.grid(row=6, column=0, padx=20, pady=2)

        # create main entry and button
        self.entry = customtkinter.CTkEntry(self, placeholder_text="CTkEntry")
        self.entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.main_button_1 = customtkinter.CTkButton(master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"))
        self.main_button_1.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

        # create textbox
        self.textbox = customtkinter.CTkTextbox(self, width=250, fg_color="#181F20")
        self.textbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")

        # create tabview
        self.tabview = customtkinter.CTkTabview(self, width=250)
        self.tabview.grid(row=0, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.tabview.add("Discord")
        self.tabview.add("Veredict")
        self.tabview.tab("Discord").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        self.tabview.tab("Veredict").grid_columnconfigure(0, weight=1)



        self.entry_token = customtkinter.CTkEntry(self.tabview.tab("Discord"), placeholder_text="Token")
        self.entry_token.grid(row=1, column=0, padx=20, pady=(20, 10))

       
        self.entry_id_1 = customtkinter.CTkEntry(self.tabview.tab("Discord"), placeholder_text="ID")
        self.entry_id_1.grid(row=0, column=0, padx=20, pady=(10, 10))


        self.string_input_button = customtkinter.CTkButton(self.tabview.tab("Discord"), text="Connect Discord",
                                                           command=self.inputs_disable_buttom)
        self.string_input_button.grid(row=2, column=0, padx=20, pady=(10, 10))


        self.button_veredict_final = customtkinter.CTkButton(self.tabview.tab("Veredict"), text="Start Veredict", command=self.start_veredict)
        self.button_veredict_final.grid(row=3, column=0, padx=20, pady=10)
        self.button_veredict_final.configure(fg_color="#05ab37", hover_color="#057827")

        self.label_veredict= customtkinter.CTkLabel(self.tabview.tab("Veredict"), text="When you send the verdict\n there is no going back\nThe data entered must be correct!")
        self.label_veredict.grid(row=4, column=0, padx=20, pady=0)
        


        # create radiobutton frame
        self.radiobutton_frame = customtkinter.CTkFrame(self)
        self.radiobutton_frame.grid(row=0, column=3, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.radio_var = tkinter.IntVar(value=0)
        self.label_radio_group = customtkinter.CTkLabel(master=self.radiobutton_frame, text="System Language", font=("Coroto", 14))
        self.label_radio_group.grid(row=0, column=2, columnspan=1, padx=10, pady=10, sticky="")
        self.radio_button_1 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, command=self.lang, text="Spanish",variable=self.radio_var, value=0)
        self.radio_button_1.grid(row=1, column=2, pady=10, padx=20, sticky="n")
        self.radio_button_2 = customtkinter.CTkRadioButton(master=self.radiobutton_frame,command=self.lang2, text="English", value=1)
        self.radio_button_2.grid(row=2, column=2, pady=10, padx=20, sticky="n")
        self.radio_button_3 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, text="France", value=2)

        

    

        self.radio_button_3.grid(row=3, column=2, pady=10, padx=20, sticky="n")

        

        # create slider and progressbar frame
        self.slider_progressbar_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.slider_progressbar_frame.grid(row=1, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
        self.slider_progressbar_frame.grid_rowconfigure(4, weight=1)
        self.progressbar_1 = customtkinter.CTkProgressBar(self.slider_progressbar_frame)
        self.progressbar_1.grid(row=1, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
        self.progressbar_2 = customtkinter.CTkProgressBar(self.slider_progressbar_frame)
        self.progressbar_2.grid(row=2, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
        self.slider_1 = customtkinter.CTkSlider(self.slider_progressbar_frame, from_=0, to=1, number_of_steps=4)
        self.slider_1.grid(row=3, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
        self.slider_2 = customtkinter.CTkSlider(self.slider_progressbar_frame, orientation="vertical")
        self.slider_2.grid(row=0, column=1, rowspan=5, padx=(10, 10), pady=(10, 10), sticky="ns")
        self.progressbar_3 = customtkinter.CTkProgressBar(self.slider_progressbar_frame, orientation="vertical")
        self.progressbar_3.grid(row=0, column=2, rowspan=5, padx=(10, 20), pady=(10, 10), sticky="ns")

        # create scrollable frame
        self.scrollable_frame = customtkinter.CTkScrollableFrame(self, label_text="Folders Config")
        self.scrollable_frame.grid(row=1, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.scrollable_frame.grid_columnconfigure(0, weight=1)
        

        # create checkbox and switch frame
        self.checkbox_slider_frame = customtkinter.CTkFrame(self)
        self.checkbox_slider_frame.grid(row=1, column=3, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.checkbox_1 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame)
        self.checkbox_1.grid(row=1, column=0, pady=(0.5, 0), padx=20, sticky="n")
        self.checkbox_2 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame)
        self.checkbox_2.grid(row=2, column=0, pady=(20, 0), padx=20, sticky="n")
        self.checkbox_3 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame)
        self.checkbox_3.grid(row=3, column=0, pady=(20, 0), padx=20, sticky="n")
        self.checkbox_4 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame)
        self.checkbox_4.grid(row=4, column=0, pady=(20, 0), padx=20, sticky="n")

        self.check_label = customtkinter.CTkLabel(self.checkbox_slider_frame, text="Config Logs", font=("Coroto", 16))
        self.check_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.checkbox_1.configure(text="DLL Logs")
        self.checkbox_2.configure(text="RAR Logs")
        self.checkbox_3.configure(text="EXE Logs")
        self.checkbox_4.configure(text="TASK Logs")

        # set default values

        premiun_font=customtkinter.CTkFont(family="", slant="italic")


        

        self.sidebar_button_3.configure(state="disabled", text="Auto Scan", fg_color="#f7cf05", border_color="#ffffff", text_color_disabled="#ffffff", border_width=1, font=premiun_font, anchor="e")
        self.sidebar_button_1.configure(text="Generate Logs")
        self.checkbox_1.select()
        self.radio_button_3.configure(state="disabled")
        self.scaling_optionemenu.set("100%")
        self.slider_1.configure(command=self.progressbar_2.set)
        self.slider_2.configure(command=self.progressbar_3.set)
        self.progressbar_1.configure(mode="indeterminnate")
        self.progressbar_1.start()
        self.textbox.insert("0.0", "ScreenShare Tips\n\n" + "En desarrollo")
        
        

    def inputs_disable_buttom(self):

        # DISABLE BUTTOM SYSTEM WITH LOGIN CODE
        
        global disable
        global webhook

        if disable == True:
            return
        
        try:
            id_input = str(self.entry_id_1.get())

            query = {"id": id_input}
            token = { "token": 1 }
            webhook = { "webhook": "" }

            token_verified = collection.find_one(query, token)
            webhook = collection.find_one(query, webhook)

            webhook = webhook['webhook']

            print(webhook)
                  
            token_input = int(self.entry_token.get())

            if not token_verified['token'] == token_input and not token_verified['id'] == id_input:
                messagebox.showinfo(f"Frozy Error", "The token or ID not is valid!")
                return
            else:
                disable=True

                self.string_input_button.configure(state="disable", fg_color="#13ad3f", text_color_disabled="#ffffff", border_color="#ffffff", text="Ready")

                self.entry_id_1 = customtkinter.CTkEntry(self.tabview.tab("Discord"), placeholder_text="••••••••••••••••••", placeholder_text_color="#FFFFFF")
                self.entry_id_1.grid(row=0, column=0, padx=20, pady=(10, 10))
                self.entry_id_1.configure(state="disable")

                self.entry_token = customtkinter.CTkEntry(self.tabview.tab("Discord"), placeholder_text="••••••••••••••••••", placeholder_text_color="#FFFFFF")
                self.entry_token.grid(row=1, column=0, padx=20, pady=(20, 10))
                self.entry_token.configure(state="disable")
                
                messagebox.showinfo(f"Frozy Success Login", "Now are connect to discord, Good Luck!")
                

        except:
             messagebox.showinfo(f"Frozy Error", "The token or ID not is valid!")
             return

             

    def start_veredict(self):

        global webhook
    
        
        localtime=datetime.now()
        localtime=localtime.strftime("%H:%M:%S")   
        
        if not disable == True:
             messagebox.showerror("Frozy Veredict Error", "You need connect to discord frist!")
             return


        dialog = customtkinter.CTkInputDialog(text="What is the User IGN?", title="Verdict System")
        ign = dialog.get_input()

        if ign == "":
            return

        dialog2 = customtkinter.CTkInputDialog(text="Is Legit? (Y/N)", title="Verdict System")
        legit = dialog2.get_input()

        if legit == 'n' or legit == 'N':
            dialog4 = customtkinter.CTkInputDialog(text="What cheat have the user?", title="Verdict System")
            vere = dialog4.get_input()

        dialog3 = customtkinter.CTkInputDialog(text="What is your IGN?", title="Staff Information")
        staff_ign = dialog3.get_input()

        dialog3 = customtkinter.CTkInputDialog(text="Send verdict? (Y/N)", title="Confirmation")
        confirmation = dialog3.get_input()

        if confirmation == 'y' or confirmation == 'Y':
            if legit == 'y' or legit == 'Y':
                webhook = DiscordWebhook(url=webhook)

                embed = DiscordEmbed(title='Veredict ScreenShare', description=f'**User**: {ign}\n**Verdict**: Legit\n**Staff**: {staff_ign}\n**Checked at**: {localtime}', color='07F00E')

                embed.set_thumbnail(url=f"https://mc-heads.net/avatar/{ign}/100/nohelm.png")

                webhook.add_embed(embed)

                response = webhook.execute()
            else:
                webhook = DiscordWebhook(url=webhook)

                embed = DiscordEmbed(title='Veredict ScreenShare', description=f'**User**: {ign}\n**Verdict**: Cheater\n**Cheats**: {vere}\n**Staff**: {staff_ign}\n**Checked at**: {localtime}', color='F00707')

                embed.set_thumbnail(url=f"https://mc-heads.net/avatar/{ign}/100/nohelm.png")

                webhook.add_embed(embed)

                response = webhook.execute()

        
            

        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)



    def sidebar_button_event2(self):
        
        if language == 1:
            os.system('REG ADD HKCU\Software\Microsoft\Windows\CurrentVersion\Applets\Regedit /v LastKey /t REG_SZ /d "Equipo\HKEY_CURRENT_USER\Software\Microsoft\Windows NT\CurrentVersion\AppCompatFlags\Compatibility Assistant\Store" /f ')
            os.system("START regedit")
        elif language == 0:
            os.system('REG ADD HKCU\Software\Microsoft\Windows\CurrentVersion\Applets\Regedit /v LastKey /t REG_SZ /d "Computer\HKEY_CURRENT_USER\Software\Microsoft\Windows NT\CurrentVersion\AppCompatFlags\Compatibility Assistant\Store" /f ')
            os.system("START regedit")
         

    def lang(self):
         global language
         language=1
         self.radio_button_2.deselect()
    
    def lang2(self):
         global language
         language=0
         self.radio_button_1.deselect()


    def virtual_machine(self):
         
            f = open('vm.bat', 'w')

            with open('vm.bat', 'w') as f:
                f.write("Msinfo32")

            time.sleep(0.5)
            os.system('vm.bat')
            os.system("del vm.bat")

         


    def open_folders(self):
            home = os.path.expanduser( '~' )

                       

            dialog5 = customtkinter.CTkInputDialog(text="The system is 32/64 Bits? (32/64)", title="System Informacion")
            vere = int(dialog5.get_input())

            if vere == 64:
                 usagelogs=home+"//AppData//Local//Microsoft//CLR_v4.0//UsageLogs//"
                 subprocess.run(['explorer', os.path.realpath(usagelogs)])
                 messagebox.showinfo("Next Folder", "Ready to open the next folder?")
                 
            elif vere == 32:
                 usagelogs=home+"//AppData//Local//Microsoft//CLR_v4.0_32//UsageLogs//"
                 subprocess.run(['explorer', os.path.realpath(usagelogs)])
                 messagebox.showinfo("Next Folder", "Ready to open the next folder?")
                 

            index=home+"//Searches//Indexed Locations.search-ms"
            subprocess.run(['explorer', os.path.realpath(index)])
            messagebox.showinfo("Next Folder", "Ready to open the next folder?")

            recycle=home+"//AppData//Local//Microsoft//Windows//History"
            subprocess.run(['explorer', os.path.realpath(recycle)])

            messagebox.showinfo("Next Folder", "Ready to open the next folder?")

            temp=home+"//appdata//local//temp"
            subprocess.run(['explorer', os.path.realpath(temp)])

            messagebox.showinfo("Next Folder", "Ready to open the next folder?")

            minecraft=home+"//appdata//Roaming//.minecraft"
            subprocess.run(['explorer', os.path.realpath(minecraft)])

            messagebox.showinfo("Next Folder", "Ready to open the next folder?")

            recent=home+"//appdata//Roaming//Microsoft//Windows//Recent"
            subprocess.run(['explorer', os.path.realpath(recent)])

            messagebox.showinfo("Next Folder", "Ready to open the next folder?")

            prefetch="C://Windows//prefetch"
            subprocess.run(['explorer', os.path.realpath(prefetch)])

            

            

    def sidebar_button_event(self):

        home = os.path.expanduser( '~' )
        if self.checkbox_1.get() == 1:
            direc=os.getcwd()
            folder=direc+'\\recent_dll.txt'

            f = open('dll.bat', 'w')

            with open('dll.bat', 'w') as f:
                f.write(f"cd {home} \ndir +*.dll+ /s = {folder}".replace("+", '"').replace("=", ">"))

            time.sleep(0.5)
            os.system('dll.bat')
            os.system("del dll.bat")

            with open('recent_dll.txt', 'r+') as f:
                originalContent = f.read()
                f.seek(0, 0)
                f.write(f'\nGenerated by SS-TOOL, Checked at {datetime.now()}\n\nDeveloped by NovatyServices\n\n')
                f.write(originalContent)

            messagebox.showinfo(".dll Logs","The Process are generate, check the folder and open the recent_dll.txt")

        if self.checkbox_2.get() == 1:
                direc=os.getcwd()
                folder=direc+'\\recent_rar.txt'

                f = open('rar.bat', 'w')

                with open('rar.bat', 'w') as f:
                    f.write(f"cd {home} \ndir +*.rar+ /s = {folder}".replace("+", '"').replace("=", ">"))

                time.sleep(0.5)
                os.system('rar.bat')
                os.system("del rar.bat")

                with open('recent_rar.txt', 'r+') as f:
                    originalContent = f.read()
                    f.seek(0, 0)
                    f.write(f'\nGenerated by SS-TOOL, Checked at {datetime.now()}\n\nDeveloped by NovatyServices\n\n')
                    f.write(originalContent)

                messagebox.showinfo(".rar Logs","The Process are generate, check the folder and open the recent_rar.txt")

        if self.checkbox_3.get() == 1:
                    direc=os.getcwd()
                    folder=direc+'\\recent_exe.txt'

                    f = open('exes.bat', 'w')

                    with open('exes.bat', 'w') as f:
                        f.write(f"cd {home} \ndir +*.exe+ /s = {folder}".replace("+", '"').replace("=", ">"))

                    time.sleep(0.5)
                    os.system('exes.bat')
                    os.system("del exes.bat")

                    with open('recent_exe.txt', 'r+') as f:
                        originalContent = f.read()
                        f.seek(0, 0)
                        f.write(f'\nGenerated by SS-TOOL, Checked at {datetime.now()}\n\nDeveloped by NovatyServices\n\n')
                        f.write(originalContent)

                    messagebox.showinfo(".exe Logs","The Process are generate, check the folder and open the recent_exe.txt")
        if self.checkbox_4.get() == 1:
                    direc=os.getcwd()

                    f = open('process.bat', 'w')

                    with open('process.bat', 'w') as f:
                        f.write("tasklist > task.txt"+"\n"+"del process.bat")

                    time.sleep(0.5)
                    os.system('process.bat')

                    with open('task.txt', 'r+') as f:
                        originalContent = f.read()
                        f.seek(0, 0)
                        f.write(f'\nGenerated by SS-TOOL, Checked at {datetime.now()}\n\nDeveloped by NovatyServices\n\n')
                        f.write(originalContent)

                    messagebox.showinfo("Process Logs","The Process are generate, check the folder and open the task.txt")

        if self.checkbox_1.get() == 0 and self.checkbox_2.get() == 0 and self.checkbox_3.get() == 0 and self.checkbox_4.get() == 0:
             messagebox.showinfo("Process Logs","Need minimun one config log select to generate!")
             





if __name__ == "__main__":
    app = App2()
    app.mainloop()