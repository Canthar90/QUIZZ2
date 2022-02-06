from tkinter import *
from quiz_brain import QuizBrain
import time

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.true_jpg = PhotoImage(file="images/true.png")
        self.false_jpg = PhotoImage(file="images/false.png")
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="Some Question Text", width=280, fill=THEME_COLOR,
                                                     font=("Arial", 20, "italic" ))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.true_button = Button(image=self.true_jpg, command=self.true_pressed)
        self.true_button.grid(column=0, row=2)

        self.false_button = Button(image=self.false_jpg, command=self.false_pressed)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()



        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():

            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="The Quiz are over now there si no more questions")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")


    def true_pressed(self):
        is_right = self.quiz.check_answer(user_answer="True")
        self.give_feedback(is_right)
        # time.sleep(1)
        # self.get_next_question()

    def false_pressed(self):
        is_right = self.quiz.check_answer(user_answer="False")
        self.give_feedback(is_right)
        # time.sleep(1)
        # self.get_next_question()

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)
