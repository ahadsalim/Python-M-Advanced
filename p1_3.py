def get_info ():
    num= int(input("How many people :"))
    name=list()
    for i in range(num) :
        name.append(input("Enter name and 3 ganre (Horror, Romance, Comedy, History , Adventure , Action): ").split(" "))
    horror=0
    action=0
    comedy=0
    romance=0
    history=0
    adventure=0
    for na in name :
        for j in range(1,4) :
            if na[j].lower() == "horror" :
                horror +=1
            elif na[j].lower() == "romance" :
                romance +=1
            elif na[j].lower() == "comedy" :
                comedy +=1
            elif na[j].lower() == "history" :
                history +=1
            elif na[j].lower() == "adventure" :
                adventure +=1
            elif na[j].lower() == "action" :
                action +=1
    return horror,romance,comedy,history,adventure,action

horror,romance,comedy,history,adventure,action=get_info()
print ("Horror :" + str(horror) + " Romance:" + str(romance) + " Comedy:" + str(comedy) + " History:" + str(history)+ " Adventure=" + str(adventure) + " Action=" + str(action))
