def main():
    print("\n" + "=" * 50)
    print("🎮 WELCOME TO THE QUIZ CHALLENGE!".center(50))
    print("📌 Note: You'll get two chances for each question.".center(50))
    print("=" * 50)

    print("🚀 LET'S START THE QUIZ! 🚀".center(50))

    while True:
        questions = load_questions()
        score = play_quiz(questions)
        show_result(score)
        
        if not play_again():
            break

def load_questions():
    # Store all quiz questions and answers
    questions = {
        "What is the capital of India?": "Delhi",
        "Which planet is known as the Red Planet?": "Mars",
        "Which keyword is used to define a function in Python?": "def",
        "Which function is used to display output in Python?": "print",
        "How many days are in a leap year?": "366",
        "What is the largest ocean on Earth?": "Pacific",
        "Which keyword is used to stop a loop?": "break"
    }

    return questions


def play_quiz(questions):
    score = 0
    total_questions = len(questions)

    # Display each question and track progress through the quiz
    for number, (question, answer) in enumerate(questions.items(), start=1):

        print("\n" + "-" * 50)
        print(f"Question {number}/{total_questions}")
        print(f"❓ {question}")

        user_answer = input("Your Answer: ").strip()

        if user_answer.lower() == answer.lower():
            print("✔ CORRECT!")
            score += 1
        else:
            print("❌ WRONG! You have one more chance")

            # Allow one additional attempt before revealing the answer
            user_answer = input("Try Again: ").strip()

            if user_answer.lower() == answer.lower():
                print("✔ CORRECT!")
                score += 1
            else:
                print("❌ WRONG AGAIN!")
                print(f"✔ Correct Answer: {answer.title()}")

    print("\n" + "-" * 50)
    print("*** QUIZ COMPLETED ***".center(50))
    print("-" * 50)

    # Calculate and display the final quiz performance
    percentage = (score / total_questions) * 100
    
    print("\n" + "-" * 50)
    print(" ~~~ QUIZ RESULTS ~~~ ")
    
    print(f"📊 Your Score: {score}/{total_questions}")
    print(f"📈 Percentage: {percentage:.0f}%")
    
    return score


def show_result(score):
    # Display the player's performance after the quiz
    if score == 7:
        print("🏆 EXCELLENT! You have a strong knowledge base 🥇")
    elif score >= 5:
        print("🌟 GREAT JOB! You performed very well 🥈")
    elif score >= 3:
        print("👍 GOOD! Keep practicing to improve 🥉")
    else:
        print("📚 Keep learning and try again!")
    
    
def play_again():
    # Ask the user if they want to play again
    while True:
        print("-" * 50)
        choice = input("Play again? (Y/N): ").strip().lower()

        if choice == "n":
            print("\n" + "=" * 50)
            print("🎉 THANKS FOR PLAYING 🎉".center(50))
            print("👋 See you next time!".center(50))
            print("=" * 50)
            return False

        elif choice == "y":
            return True

        else:
            print("Please enter Y or N.")

if __name__ == "__main__":
    main()