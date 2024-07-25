import json

class QuizApp:
    def __init__(self):
        self.questions = []
        self.load_questions()
        self.score = 0

    def load_questions(self):
        # Define some questions and answers
        self.questions = [
            {
                "question": "What is the capital of France?",
                "options": ["A) London", "B) Paris", "C) Berlin", "D) Madrid"],
                "answer": "B"
            },
            {
                "question": "What is the largest planet in our Solar System?",
                "options": ["A) Earth", "B) Mars", "C) Jupiter", "D) Saturn"],
                "answer": "C"
            },
            {
                "question": "What is the boiling point of water?",
                "options": ["A) 90°C", "B) 100°C", "C) 110°C", "D) 120°C"],
                "answer": "B"
            }
        ]

    def start_quiz(self):
        print("Welcome to the Quiz App!")
        for i, q in enumerate(self.questions):
            print(f"\nQuestion {i+1}: {q['question']}")
            for option in q['options']:
                print(option)
            answer = input("Your answer: ").strip().upper()
            if answer == q['answer']:
                print("Correct!")
                self.score += 1
            else:
                print(f"Wrong! The correct answer is {q['answer']}")

        self.show_results()

    def show_results(self):
        print(f"\nYour final score is {self.score} out of {len(self.questions)}")
        if self.score == len(self.questions):
            print("Excellent! You got all the answers right!")
        elif self.score >= len(self.questions) // 2:
            print("Good job! You got more than half correct.")
        else:
            print("Better luck next time.")

if __name__ == "__main__":
    quiz = QuizApp()
    quiz.start_quiz()
