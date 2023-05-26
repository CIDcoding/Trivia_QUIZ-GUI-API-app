from tkinter import *
THEME_COLOR = "#375362"
FONT = ('Arial', 20, 'italic')

# design the UI using Tkinter BUT inside a class
class QuizUI:
    def __init__(self):
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        #score label
        self.score_label = Label(text='Score: 0', bg=THEME_COLOR, fg='white')
        self.score_label.grid(column=1, row=0)

        #canvas
        self.canvas=Canvas(width=300, height=250, highlightthickness=0, bg='white')
        self.canvas_text = self.canvas.create_text(150, 125, text = 'question text here', font=FONT, fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2, padx=20, pady=20)

        # buttons
        check_photo = PhotoImage(file='./images/true.png')
        cross_photo = PhotoImage(file='./images/false.png')
        self.check_button = Button(image=check_photo, highlightthickness=0, borderwidth=0.5)
        self.check_button.grid(column=0, row=2)
        self.cross_button = Button(image=cross_photo, highlightthickness=0, borderwidth=0.5)
        self.cross_button.grid(column=1, row=2)





        self.window.mainloop()

