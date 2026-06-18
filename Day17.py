import os
from quiz_data import question_data

def clear_terminal():
    """Clears the console screen across platform environments."""
    os.system('cls' if os.name == 'nt' else 'clear')

# =====================================================================
# 📦 CUSTOM BLUEPRINT CLASSES (Core OOP Learning Objective)
# =====================================================================

class Question:
    """Models a single question entity with structural text and answer criteria."""
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer

class QuizBrain:
    """Manages the computational game engine logic, tracking, and evaluation loops."""
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_questions(self):
        """Returns True if there are remaining unparsed question objects, otherwise False."""
        return self.question_number < len(self.question_list)

    def next_question(self):
        """Fetches the current active question object and processes user input evaluations."""
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        
        print(f"\n📋 Evaluation Task {self.question_number}:")
        user_answer = input(f"   {current_question.text} (True/False): ").strip().lower()
        
        # Defensive processing normalization map
        normalized_guess = "true" if user_answer in ["t", "true"] else "false"
        self.check_answer(normalized_guess, current_question.answer.lower())

    def check_answer(self, user_guess, correct_answer):
        """Compares user evaluations against correct data profiles and updates engine states."""
        if user_guess == correct_answer:
            self.score += 1
            print("   🟢 ASSESSMENT VALID: Correct analysis.")
        else:
            print("   ❌ ASSESSMENT INVALID: Incorrect analysis.")
            
        print(f"   📈 Current Performance Index: {self.score}/{self.question_number}")
        print("--------------------------------------------------")


# =====================================================================
# 🎮 SYSTEM MASTER RUNTIME CONSOLE
# =====================================================================
def main():
    clear_terminal()
    print("==================================================")
    print("     ENTERPRISE KNOWLEDGE ASSESSMENT ENGINE       ")
    print("==================================================")
    print("System active. Constructing object relational matrices...")
    
    # 💎 OOP INTENT: Initialize an empty list to parse dict items into standalone custom objects
    question_bank = []
    for question in question_data:
        question_text = question["text"]
        question_answer = question["answer"]
        # Instantiating a new Question object blueprint for every iteration
        new_question = Question(question_text, question_answer)
        question_bank.append(new_question)

    # Instantiate the master coordinator engine object
    quiz = QuizBrain(question_bank)

    # Core engine loop running off custom object return method flags
    while quiz.still_has_questions():
        quiz.next_question()

    print("\n==================================================")
    print("             FINAL AUDITED SCORE REPORT           ")
    print("==================================================")
    print("  All verification evaluation sequences complete.")
    print(f"  🎯 Final Verified Score Score: {quiz.score}/{quiz.question_number}")
    print(f"  📊 Final Accuracy Efficiency : {round((quiz.score / quiz.question_number) * 100, 2)}%")
    print("==================================================")

if __name__ == "__main__":
    main()