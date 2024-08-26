from difflib import get_close_matches

def get_best_match(user_question:str,questions:dict) ->str | None:
    
    questions : list[str] = [q for q in questions]
    matches : list = get_close_matches(user_question,questions,n=1,cutoff=0.6) # hello --> hell
    
    if matches:
        return matches[0]
    
def chatbot(knowledge:dict):
    
    while True:
        user_input : str = input('You : ')
    
        best_match : str | None = get_best_match(user_input,knowledge)
    
        if answer := knowledge.get(best_match):
            print(f'Chatbot : {answer}')
        else:
            print('Bot: i can not understand...')
        
if __name__ == '__main__':
    brain : dict  = {'hello' : 'hey there!',
                  'how are you':'I am good , thanks',
                  'what is your name':'I am a chatbot',
                  'what time is it ?':'i dont have idea',
                  'what can you do ?':'i can answer the questions',
                  'thank you':'your welcome'}
    
    chatbot(knowledge=brain)
    
