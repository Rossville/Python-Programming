questions = {
    1 : "Which planet is known as the \"Red Planet\"?",
    2 : 'What is the capital city of Australia?',
    3 : 'Who painted the Mona Lisa?',
    4 : 'What is the largest ocean on Earth?',
    5 : 'What is the currency of Japan?',
    6 : 'Who was the first person to step on the Moon?',
    7 : 'Which country is famous for the ancient ruins of Machu Picchu?',
    8 : 'What is the chemical symbol for gold?',
    9 : 'Who wrote the play "Romeo and Juliet"?',
    10 : 'Which gas do plants primarily use for photosynthesis?'
}

options = {
    1 : ["Jupiter","Mars","Saturn","Venus"],
    2 : ["Sydney","Canberra","Melbourne","Brisbane"],
    3 : ["Vincent van Gogh","Leonardo da Vinci","Pablo Picasso","Michelangelo"],
    4 : ["Atlantic Ocean","Indian Ocean","Pacific Ocean","Arctic Ocean"],
    5 : ["Yen","Dollar","Rupee","Won"],
    6 : ["Neil Armstrong","Buzz Aldrin","Yuri Gagarin","John Glenn"],
    7 : ["Mexico","Peru","Brazil","Egypt"],
    8 : ["Au","Ag","Pb","Mg"],
    9 : ["William Shakespeare","Jane Austen","Charles Dickens","Ernest Hemingway"],
    10 : ["Oxygen","Nitrogen","Carbon Dioxide","Hydrogen"]
}

correct_answer = {
    1 : "Jupiter",
    2 : "Canberra",
    3 : "Leonardo da Vinci",
    4 : "Pacific Ocean",
    5 : "Yen",
    6 : "Neil Armstrong",
    7 : "Peru",
    8 : "Au",
    9 : "William Shakespeare",
    10 : "Carbon Dioxide"
}

exit_the_game = False
score = 0

while(not exit_the_game):
    for i in range(1,11):
        print(i,".",questions[i])
        print(f"1.{options[i][0]}\t2.{options[i][1]}")
        print(f"3.{options[i][2]}\t4.{options[i][3]}")
        print("Enter 0 to exit the quiz")
        user_input = int(input())
        if user_input == 0:
            exit_the_game = True
            break
        else:
            if(options[i][user_input-1] == correct_answer[i]):
                print(" ---- Correct ----")
                score+=1
            else:
                print(" ---- Incorrect ----")
            if i == 10:
                exit_the_game = True
    

print("Score : ",score)
if score >= 8:
    print("You are great at General Knowleadge!")
elif(score >=5 and score < 8):
    print("You scored average!")
else:
    print("You need to focus on your General Knowleadge")