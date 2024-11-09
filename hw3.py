import data

#PART 1

#Function takes a list of county demographics as input - list[data.CountyDemographics]
#It returns an int - the total population of that list of counties
#It iterates through each demographic and sums all of their population
def population_total(l : list[data.CountyDemographics]) -> int:

    tot = 0

    for i in l:
        tot += i.population['2014 Population']

    return tot

#PART 2

#Function takes a list of county demographics as input - list[data.CountyDemographics]
#It returns an int - the total population of that list of counties
#It iterates through each county demographic, checking and appending to new list
#if it is the required state
def filter_by_state(l: list[data.CountyDemographics], s: str) -> list[data.CountyDemographics]:

    nl = []

    for i in l:
        if i.state == s:
            nl.append(i)

    return nl

#PART 3
#Function takes a list of county demographics as input - list[data.CountyDemographics]
#and a string as the required key
#It returns a float - approx population amount of that county with that education level
def population_by_education(l: list[data.CountyDemographics], s: str) -> float:

    tot = 0

    for i in l:
        if s in i.education:
            tot += i.education[s] * i.population['2014 Population'] / 100

    return tot

#Function takes a list of county demographics as input - list[data.CountyDemographics]
#and a string as the required key
#It returns float - approx population amount of that county with that ethnicity
def population_by_ethnicity(l: list[data.CountyDemographics], s: str) -> float:

    tot = 0

    for i in l:
        if s in i.ethnicities:
            tot += i.ethnicities[s] * i.population['2014 Population'] / 100

    return tot

#Function takes a list of county demographics as input - list[data.CountyDemographics]
#It returns a float - approx population amount of that county with below poverty income
def population_below_poverty_level(l: list[data.CountyDemographics]) -> float:

    tot = 0

    for i in l:
        tot += i.income['Persons Below Poverty Level'] * i.population['2014 Population'] / 100

    return tot

#PART 4
#Function takes a list of county demographics as input - list[data.CountyDemographics]
#and a string as the required key
#It returns a float - approx population % of total population
#of the list with that education level
def percent_by_education(l: list[data.CountyDemographics], s: str) -> float:
    tot = population_by_education(l, s)
    tot /= population_total(l)

    tot *= 100

    return tot

#Function takes a list of county demographics as input - list[data.CountyDemographics]
#and a string as the required key
#It returns a float - approx population % of total population
#of the list with that ethnicity
def percent_by_ethnicity(l: list[data.CountyDemographics], s: str) -> float:
    tot = population_by_ethnicity(l, s)
    tot /= population_total(l)

    tot *= 100

    return tot

#Function takes a list of county demographics as input - list[data.CountyDemographics]
#It returns a float - approx population % of total population
#of the list with income below poverty
def percent_below_poverty_level(l: list[data.CountyDemographics]) -> float:
    tot = population_below_poverty_level(l)
    tot /= population_total(l)

    tot *= 100

    return tot

#PART 5

#Function takes a list of county demographics as input - list[data.CountyDemographics]
#and a string for key, and a float for threshold % value
#It returns another list of county demographics
#whose specified education % surpass the threshold %
def education_greater_than(l: list[data.CountyDemographics], s: str, thres: float) -> list[data.CountyDemographics]:

    retL = []

    for i in l:
        if s in i.education:
            if i.education[s] > thres:
                retL.append(i)

    return retL

#Function takes a list of county demographics as input - list[data.CountyDemographics]
#and a string for key, and a float for threshold % value
#It returns another list of county demographics
#whose specified education % falls below the threshold %
def education_less_than(l: list[data.CountyDemographics], s: str, thres: float) -> list[data.CountyDemographics]:
    retL = []

    for i in l:
        if s in i.education:
            if i.education[s] < thres:
                retL.append(i)

    return retL

#Function takes a list of county demographics as input - list[data.CountyDemographics]
#and a string for key, and a float for threshold % value
#It returns another list of county demographics
#whose specified ethnicity % surpass the threshold %
def ethnicity_greater_than(l: list[data.CountyDemographics], s: str, thres: float) -> list[data.CountyDemographics]:
    retL = []

    for i in l:
        if s in i.ethnicities:
            if i.ethnicities[s] > thres:
                retL.append(i)

    return retL

#Function takes a list of county demographics as input - list[data.CountyDemographics]
#and a string for key, and a float for threshold % value
#It returns another list of county demographics
#whose specified ethnicity % falls below the threshold %
def ethnicity_less_than(l: list[data.CountyDemographics], s: str, thres: float) -> list[data.CountyDemographics]:
    retL = []

    for i in l:
        if s in i.ethnicities:
            if i.ethnicities[s] < thres:
                retL.append(i)

    return retL

#Function takes a list of county demographics as input - list[data.CountyDemographics]
#and a float for threshold % value
#It returns another list of county demographics
#whose specified poverty income % surpasses the threshold %
def below_poverty_level_greater_than(l: list[data.CountyDemographics], thres: float) -> list[data.CountyDemographics]:

    retL = []

    for i in l:
        if i.income['Persons Below Poverty Level'] > thres:
            retL.append(i)

    return retL

#Function takes a list of county demographics as input - list[data.CountyDemographics]
#and a float for threshold % value
#It returns another list of county demographics
#whose specified poverty income % falls behind the threshold %
def below_poverty_level_less_than(l: list[data.CountyDemographics], thres: float) -> list[data.CountyDemographics]:
    retL = []

    for i in l:
        if i.income['Persons Below Poverty Level'] < thres:
            retL.append(i)

    return retL