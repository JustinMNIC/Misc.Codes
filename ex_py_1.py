#Please read this, ty :

"""
soo.. I tried to built other programs and I always had issues with the GUI - like, my brain is not working or something when it comes to UI. 
I have ideas for cool and actually useful programs, and I can write the back-end stuff ( easier or harder, depends on the chase). My weakness is the UI. So...
Me beeing me, I decided to take a few steps back and do some little projects that are easier. 
This is one of those projects. 
"""

import customtkinter as ctk

class Program(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("'The most complex program ever built by any human'")
        self.geometry("500x500")

        self.grid_rowconfigure(tuple(i for i in range(6)), weight=1)
        self.grid_columnconfigure(tuple(i for i in range(9)), weight=1)

        var_text = ctk.StringVar(self, value="Welcome!", name="var_text")
        var_text.trace_add("write", self.update_label)
        self.awesome_text = ctk.CTkLabel(self, text=var_text.get())
        self.awesome_text.grid(row=0, rowspan=1, column=0, columnspan=5, sticky="news")

        self.input_box = ctk.CTkEntry(self, textvariable=var_text)
        self.input_box.grid(row=2, column=0, sticky="news")
        
        self.change_color = ctk.CTkOptionMenu(self, values=["white", "black", "green", "yellow", "blue"], command= self.change_col)
        self.change_color.grid(row = 0, column = 8)
        
        self.reverse_text = ctk.CTkButton(self, text = "Reverse the text", command= self.reverse)
        self.reverse_text.grid(row = 3, column = 1)
    
    def reverse(self, *args):
        reversed_text = self.awesome_text.cget("text")[::-1]
        self.input_box.delete(0, ctk.END)
        self.input_box.insert(0, reversed_text)

    def change_col(self, *args):
        self.awesome_text.configure(text_color= self.change_color.get())
    def update_label(self, *args):
        self.awesome_text.configure(text=self.input_box.get())

if __name__ == "__main__":
    program_instance = Program()
    program_instance.mainloop()
