def prompt_user_for_country_name(num_countries):
    countries = []
    for i in range(num_countries):
        country_name = input("Enter name of country: ")
        countries.append(country_name)
    return countries

def get_matches(countries):
    matches = {}
    for idx, country in enumerate(countries):
        for other_country in countries[idx+1:]:
            ans = input(f"Has {country} had a match with {other_country}? (y or n): ")
            if ans == "y":
                result_of_match = input(f"Enter the result {country}-{other_country}: ")
                matches[f"{country}-{other_country}"] = result_of_match
    return matches

def calculate_score(matches):
    score = {} # initialize an empty dict for score
    
    # iterate through each match in matches dictionary
    for match, result in matches.items():
        # split the match string into two country strings
        country1, country2 = match.split("-")
        
        # split the result string into two scores
        score1, score2 = map(int, result.split("-"))
        
        # update score dictionary for each country
        if score1 > score2:
            score[country1] = score.get(country1, 0) + 3
        elif score1 == score2:
            score[country1] = score.get(country1, 0) + 1
            score[country2] = score.get(country2, 0) + 1
        else:
            score[country2] = score.get(country2, 0) + 3
    
    return score

def wins_loses_draws(matches) :
    win = {}
    lose= {}
    draw= {}
    for match, result in matches.items():
        # split the match string into two country strings
        country1, country2 = match.split("-")
        
        # split the result string into two scores
        score1, score2 = map(int, result.split("-"))
        
        # update score dictionary for each country
        if score1 > score2:
            win[country1] = win.get(country1, 0) + 1
            lose[country2]= lose.get(country2, 0) +1
        elif score1 == score2:
            draw[country1] = draw.get(country1, 0) + 1
            draw[country2] = draw.get(country2, 0) + 1
        else:
            win[country2] = win.get(country2, 0) + 1
            lose[country1]= lose.get(country1, 0) +1
    
    return win,lose,draw

def calculate_tafazol(matches,countries):
    put_gol = {} # initialize an empty dict for score
    get_gol = {}
    dif_gol = {}
    # iterate through each match in matches dictionary
    for match, result in matches.items():
        # split the match string into two country strings
        country1, country2 = match.split("-")
        
        # split the result string into two scores
        score1, score2 = map(int, result.split("-"))
        
        # update score dictionary for each country
        put_gol[country1] = put_gol.get(country1, 0) + score1
        put_gol[country2] = put_gol.get(country2, 0) + score2

        get_gol[country1] = get_gol.get(country1, 0) + score2
        get_gol[country2] = get_gol.get(country2, 0) + score1
    
    for coun in countries :
        dif_gol[coun] = put_gol.get(coun, 0) - get_gol.get(coun, 0)
    return dif_gol

num_of_countries = int(input("Enter number of countries: "))
countries = prompt_user_for_country_name(num_of_countries)
matches = get_matches(countries)
scores= calculate_score(matches)
win,lose,draw= wins_loses_draws(matches)
dif=calculate_tafazol(matches,countries)
sorted(countries)
for c in countries :
    print(c,win.get(c,0),lose.get(c,0),draw.get(c,0),dif.get(c,0))
