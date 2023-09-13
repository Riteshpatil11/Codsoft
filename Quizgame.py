import random

class Question:
    def __init__(self, question, choices, correct_choice):
        self.question = question
        self.choices = choices
        self.correct_choice = correct_choice

class Quiz:
    def __init__(self):
        self.questions = []
        self.score = 0

    def add_question(self, question, choices, correct_choice):
        self.questions.append(Question(question, choices, correct_choice))

    def play(self):
        print("Welcome to the Quiz Game!")
        print("Rules: Answer multiple-choice questions. Enter the letter corresponding to your choice.")
        
        while True:
            self.score = 0
            random.shuffle(self.questions)
            
            for question_obj in self.questions:
                self.display_question(question_obj)
                user_choice = self.get_user_choice(len(question_obj.choices))
                self.check_answer(user_choice, question_obj.correct_choice)
            
            self.display_quiz_results()
            
            play_again = input("Do you want to play again? (yes/no): ")
            if play_again.lower() != "yes":
                break

    def display_question(self, question_obj):
        print("\n" + question_obj.question)
        for i, choice in enumerate(question_obj.choices, start=1):
            print(f"{chr(65 + i - 1)}. {choice}")

    def get_user_choice(self, num_choices):
        while True:
            user_choice = input("Your answer: ").upper()
            if user_choice in [chr(65 + i) for i in range(num_choices)]:
                return user_choice

    def check_answer(self, user_choice, correct_choice):
        if user_choice == correct_choice:
            print("Correct!")
            self.score += 1
        else:
            print(f"Incorrect. The correct answer is {correct_choice}.")

    def display_quiz_results(self):
        print("\nQuiz completed!")
        print(f"Your score: {self.score}/{len(self.questions)}")

def main():
    quiz = Quiz()
    
    # Add your questions here
    quiz.add_question("Which gas do plants primarily use for photosynthesis?", ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"], "B")
    quiz.add_question("What is the largest planet in our solar system?", ["Earth", "Jupiter", "Mars", "Saturn"], "B")
    quiz.add_question("What is the chemical symbol for gold?", ["Au", "Ag", "G", "Go"], "A")
    quiz.add_question("What is the process by which water vapor turns directly into ice?", ["Condensation", "Sublimation", "Evaporation", "Solidification"], "B")
    quiz.add_question("Which famous scientist developed the theory of relativity?", ["Isaac Newton", "Albert Einstein", "Stephen Hawking", "Niels Bohr"], "B")
    quiz.add_question("What is the capital city of Japan?", ["Tokyo", "Kyoto", "Osaka", "Seoul"], "A")
    quiz.add_question("Which planet is known as the 'Red Planet'?", ["Mars", "Jupiter", "Venus", "Mercury"], "A")
    quiz.add_question("What is the chemical symbol for water?", ["Wa", "Wt", "H2O", "Wo"], "C")
    quiz.add_question("Who wrote the play 'Hamlet'?", ["William Shakespeare", "Jane Austen", "Mark Twain", "Charles Dickens"], "A")
    quiz.add_question("What is the process of a liquid becoming a gas?", ["Melting", "Freezing", "Boiling", "Condensation"], "C")

    # Add more questions
    
    quiz.play()

if __name__ == "__main__":
    main()
