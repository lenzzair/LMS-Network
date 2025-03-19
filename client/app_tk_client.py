import tkinter as tk

class Lms_network:
    
    __nb_client = 0
    
    def __init__(self):
        self.gui = tk.Tk()
        self.gui.config(bg='skyblue')
        self.gui.title("LMS Network")
        self.gui.geometry("1000x500")
    
    def run_graphique(self):
        self.gui.mainloop()
        
    def start_new_client(self):
        Lms_network.__nb_client += 1
    
        instance_client = tk.Toplevel(self.gui)

        label_def_title = tk.Label(instance_client, 
                               text="Veuillez choisir une adresse IP ou un nom de domaine du serveur cible :", 
                               bg='skyblue', 
                               font=("Arial", 14)).pack(pady=20)
        

       
        self.input_start = tk.Entry(instance_client, font=("Arial", 14), width=50)
        self.input_start.pack(pady=10)


        submit_button = tk.Button(instance_client, text="Valider", command=self.get_input, font=("Arial", 12)).pack(pady=20)
        

    def get_input(self):
        user_input = self.input_start.get()
        print(f"Adresse saisie : {user_input}")  
    
instance1 = Lms_network()
tk.Button(instance1.gui, text="Crée un nouveaux client", command=instance1.start_new_client).pack(pady=20)
instance1.run_graphique()
