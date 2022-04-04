
import csv
all_words={}
section=["esm","famil","keshvar","rang","ashia","ghaza"]

for sections in section:
    all_words[sections]=[]

def normalize(s):
    if not s:
        return ''
    return(s.replace(' ',''))    
def ready_up():
    csvdata=open("esm_famil_data.csv")
    reader=csv.reader(csvdata)
    next(reader)
    for row in reader:
        all_words["esm"].append(normalize(row[0]))
        all_words["famil"].append(normalize(row[1]))
        all_words["keshvar"].append(normalize(row[2]))
        all_words["rang"].append(normalize(row[3]))
        all_words["ashia"].append(normalize(row[4]))
        all_words["ghaza"].append(normalize(row[5]))
ready_up()        
participants=[]
def add_participant(participant,answers):
    
    for sections in section:
       answers[sections]=normalize(answers[sections])
    participants.append({'name':participant,'answers':answers})

add_participant(participant = 'salib', answers = {'esm': 'بردیا', 'famil': 'بابایی', 'keshvar': 'باربادوس', 'rang': 'بنفش', 'ashia': 'بمب', 'ghaza': 'باقالیپلو'})
add_participant(participant = 'kianoush', answers = {'esm': 'بهرام', 'famil': 'بهرامی', 'keshvar': 'برزیل', 'rang': 'بلوطی', 'ashia': 'بیل', 'ghaza': 'به   پلو'})
add_participant(participant = 'sajjad', answers = {'esm': 'بابک', 'famil': 'بهشتی', 'keshvar': 'باهاما', 'rang': 'بژ', 'ashia': '        ', 'ghaza': 'برنج خورشت'})
add_participant(participant = 'farhad', answers = {'esm': 'بهرام', 'famil': 'براتی', 'keshvar': 'بببببب', 'rang': 'بژ', 'ashia': 'بیل', 'ghaza': 'باقلوا'})



def calculate_all():
    scores={}
    for participant in participants:
        this_name=participant['name']
        this_answers=participant['answers']
        scores[this_name]=0
        for sections in section:
            this_answer=normalize(this_answers.get(sections,False))
            if not this_answer or this_answer not in all_words[sections]:
                score=0
            else:
                duplicate=False
                all_answered=True
                for other in participants:
                    if this_name==other['name']:
                        continue
                    other_answer=normalize(other['answers'][sections])
                    if other_answer==this_answer:
                        duplicate=True
                    if not normalize(other_answer):
                        all_answered=False
                if all_answered and duplicate:
                    score=5
                if  not all_answered and duplicate:
                    score=10
                if all_answered and not duplicate:
                    score=10
                if not all_answered and not duplicate:
                    score=15   
            scores[this_name]+=score
    return scores
print(calculate_all())    
                                    