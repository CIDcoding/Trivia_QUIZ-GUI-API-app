from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
FONT = ('Arial', 20, 'italic')

# design the UI using Tkinter BUT inside a class
class QuizUI:
    def __init__(self, quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        #score label
        self.score_label = Label(text='Score: 0', bg=THEME_COLOR, fg='white')
        self.score_label.grid(column=1, row=0)

        #canvas
        self.canvas=Canvas(width=300, height=250, highlightthickness=0, bg='white')
        self.canvas_text = self.canvas.create_text(150, 125, text='', font=FONT, fill=THEME_COLOR, width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, padx=20, pady=20)

        # buttons
        check_photo = PhotoImage(file='./images/true.png')
        cross_photo = PhotoImage(file='./images/false.png')
        self.check_button = Button(image=check_photo, highlightthickness=0, borderwidth=0.5, command=self.check_pressed)
        self.check_button.grid(column=0, row=2)
        self.cross_button = Button(image=cross_photo, highlightthickness=0, borderwidth=0.5, command = self.cross_pressed)
        self.cross_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg='white')
            self.score_label.config(text=f'Score: {self.quiz.score}/{self.quiz.question_number}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_text, text=q_text)
        else:
            self.canvas.config(bg='white')
            self.canvas.itemconfig(self.canvas_text, text='You have reached the end of the quiz!')
            self.check_button.config(state='disabled')
            self.cross_button.config(state='disabled')


    def check_pressed(self):
        is_right = self.quiz.check_answer('True')
        self.give_player_feedback(is_right)


    def cross_pressed(self):
        is_right = self.quiz.check_answer('True')
        self.give_player_feedback(is_right)

    def give_player_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)
