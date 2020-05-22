import requests
import json
import random
import html

url=('https://opentdb.com/api.php?amount=1')
endGame=""

print('Welcome to the Trivia Game!')
resp = 1
count=0
mistakes=0

while endGame.lower() != "quit":
    r=requests.get(url)
    if (r.status_code != 200):
            endGame=input('Sorry, there was a problem retrieving the question. Please try again')
    else:
        answer_number=1
        valid_answer=False
        data=json.loads(r.text)
        question=data['results'][0]['question']
        answers=data['results'][0]['incorrect_answers']
        correct_answer=data['results'][0]['correct_answer']
        answers.append(correct_answer)
        random.shuffle(answers)
        print("\n"+html.unescape(question)+"\n")

        for answer in answers:
            print(str(answer_number)+"- "+html.unescape(answer))
            answer_number+=1

        while valid_answer == False:
            user_answer=input("\nType the number of the correct answer: ")
            try:
                user_answer=int(user_answer)
                if user_answer> len(answers) or user_answer<=0:
                    print("Invalid answer.")
                else:
                    valid_answer=True
            except:
                print("Invalid answer. Use only numbers.")
            
        user_answer=answers[int(user_answer)-1]
        
        if user_answer == correct_answer:
            print('\nCongratulations! You answered correctly. The correct answer was: '+correct_answer)
        else:
            print("\nSorry, "+user_answer+ " is Incorrect. The correct answer is: "+correct_answer)
            mistakes+=1
        endGame=input('\nPress enter to play again or type "quit" to quit the game. ')
        count+=1

print('\nTotal incorrect: '+str(mistakes))
print('Total played: '+str(count))
print('Grade: '+ str(int((((count-mistakes)/count)*100)))+'%')
print('Thanks for playing! Hope you enjoyed!')


