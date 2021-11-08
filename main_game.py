#imports all the sub files
from played_before.played_before_v3 import played_before
from questions.questions_v2 import questions
from score_counter.score_counter_v2 import score_counter
from round_counter.round_counter_v2 import round_counter
from Welcome.welcome_v2 import welcome
from yesno.yesno_v1 import yesno
from user_questions.user_questions_v1 import user_questions
from continue_playing.continue_playing_v1 import continue_playing

#opens the questions storage file and reads from it
with open('question_storage.py', 'r') as q:
    def read_line(q):
        line_start = q.tell()
        q.readline()
        line_end = q.tell() - 2
        q.seek(line_start)
        output = q.read(line_end)
        q.read(2)
        return output


    def main():
        #variabales for the functions
        r=0
        score = 0
        askquestion = [        "question",                 "question"]
        answer1 = [         "wrong answer",             "wrong answer"]
        answer2 = [         "right answer",             "right answer"]
        answer3 = [         "wrong answer",             "wrong answer"]
        answer4 = [         "wrong answer",             "wrong answer"]
        correct_answer = [  "right answer",             "right answer"]
        yes = ["yes", "y"]
        no = ["no", "n"]
        length = len(askquestion)


        #loads questions from storage

        output1 = 1
        while len(output1) > 0 :
            output1 = read_line(q)
            askquestion.append(output1)
            output2 = read_line(q)
            answer1.append(output2)
            output3 = read_line(q)
            answer2.append(output3)
            output4 = read_line(q)
            answer3.append(output4)
            output5 = read_line(q)
            answer4.append(output5)
            output6 = read_line(q)
            correct_answer.append(output6)


        #functions
        welcome()
        played_before()



        while True:
            while True :
                length = len(askquestion)
                r = round_counter(r)
                win = questions(r, askquestion, answer1, answer2, answer3, answer4, correct_answer, length)
                score = score_counter(win, score)
                breakey = continue_playing(False)
                if breakey == True:
                    break

            user_questions(yes,no)
            breakey = continue_playing(True)
            if breakey == True:
                break
            else:
                output1 = read_line(q)
                askquestion.append(output1)
                output2 = read_line(q)
                answer1.append(output2)
                output3 = read_line(q)
                answer2.append(output3)
                output4 = read_line(q)
                answer3.append(output4)
                output5 = read_line(q)
                answer4.append(output5)
                output6 = read_line(q)
                correct_answer.append(output6)


    main()
