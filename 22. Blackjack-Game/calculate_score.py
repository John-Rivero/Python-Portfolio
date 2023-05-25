#Takes a List of cards as input and returns the score. 
def calculate_score(score):
    
    if (score[0] == 11 and score [1] == 10) or (score[0] == 10 and score[1] == 11):
        return 0
    
    else:
        if sum(score) > 21:
            if score[0] == 11:
                score[0] == 1
                
            elif score[1] == 11:
                score[1] == 1
       
        total = score[0] + score[1]
        return total