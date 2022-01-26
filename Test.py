from tkinter import *
from tkinter import messagebox as mb
import json


class GUI_and_features:
    def __init__(self):
        self.question_number = 0
        self.show_title()
        self.show_question()
        self.chosen_opt = IntVar()
        self.options = self.radio_buttons()
        self.show_option()
        self.buttons()
        self.questions_size = len(question)
        self.correct = 0

    def disp_res(self):

        wrong_count = self.questions_size - self.correct
        correct = f"Correct: {self.correct}"
        wrong = f"Wrong: {wrong_count}"

        score = int(self.correct / self.questions_size * 100)
        result = f"Score: {score}%"

        mb.showinfo("Result", f"{result}\n{correct}\n{wrong}")

    def check_ans(self, question_number):

        if self.chosen_opt.get() == answer[question_number]:
            return True

    def next_btn(self):

        if self.check_ans(self.question_number):
            self.correct += 1

        self.question_number += 1

        if self.question_number == self.questions_size:
            self.disp_res()
            root.destroy()
        else:
            self.show_question()
            self.show_option()

    def buttons(self):

        next_button = Button(
            root,
            text="Next",
            command=self.next_btn,
            width=10,
            bg="#F2780C",
            fg="white",
            font=("ariel", 16, "bold")
        )

        next_button.place(x=350, y=380)

        quit_button = Button(
            root,
            text="Quit",
            command=root.destroy,
            width=5,
            bg="black",
            fg="white",
            font=("ariel", 16, " bold")
        )

        quit_button.place(x=700, y=50)

    def show_option(self):
        val = 0
        self.chosen_opt.set(0)

        for option in options[self.question_number]:
            self.options[val]['text'] = option
            val += 1

    def show_question(self):

        question_number = Label(
            root,
            text=question[self.question_number],
            width=60,
            font=('ariel', 16, 'bold'),
            anchor='w',
            wraplength=700,
            justify='center'
        )

        question_number.place(x=70, y=100)

    def show_title(self):

        title = Label(
            root,
            text="PyQuiz",
            width=50,
            bg="yellow",
            fg="black",
            font=("ariel", 20, "bold")
        )

        title.place(x=0, y=2)

    def radio_buttons(self):

        q_list = []

        y_pos = 150

        while len(q_list) < 4:
            radio_btn = Radiobutton(
                root,
                text=" ",
                variable=self.chosen_opt,
                value=len(q_list) + 1,
                font=("ariel", 14)
            )
            q_list.append(radio_btn)

            radio_btn.place(x=100, y=y_pos)

            y_pos += 40

        return q_list


root = Tk()
root.geometry("800x450")

root.title("PyQuiz")

with open('data.json') as f:
    data = json.load(f)

question = (data['question'])
options = (data['options'])
answer = (data['answer'])

quiz = GUI_and_features()

root.mainloop()