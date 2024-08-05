from itertools import combinations

Kevin = {"Halsey", "Taylor Swift", "Mitski", "Joji", "Shawn Mendes", "Sabrina Carpenter" , "Nicky Minaj", "Conan Gray",
         "One Direction", "Justin Bieber"}

Stuart = {"Kendrick Lamar", "Steve Lacy", "Tyler the Creator", "Joji", "TheWeeknd", "Coldplay", "Kanye West",
          "Travis Scott", "Frank Ocean", "Brent Faiyaz"}

Bob = {"Conan Gray", "Joji", "Dove Cameron", "Mitski", "Arctic Monkeys", "Steve Lacy", "Kendrick Lamar",
       "Isabel LaRosa", "Shawn Mendes", "Coldplay"}

Edith = {"Metallica", "Billie Eilish", "TheWeeknd", "Mitski", "NF", "Conan Gray", "Kendrick Lamar", "Nicky Minaj",
         "Kanye West", "Coldplay"}

dj = [list(Kevin), list(Stuart), list(Bob), list(Edith)]
djstr = ["Kevin", "Stuart", "Bob", "Edith"]

temp_lst = []
temp_set = set()
dj_pair = []

def method1():
    global temp_lst, temp_set, dj_pair
    for djname in range(0, len(dj)):
        for djname2 in range(djname+1, len(dj)):
            temp_lst = dj[djname] + dj[djname2]
            temp_set = set(dj[djname] + dj[djname2])
            
            common_artists = len(temp_lst) - len(temp_set)
            percent1 = round(common_artists*100/len(dj[djname]), 2)
            percent2 = round(common_artists*100/len(dj[djname2]), 2)
            if percent1>=30 and percent2>=30:
                dj_pair += [str(percent1)+ "\t" + str(percent2) + "\t" + str(djstr[djname]) + " & " + str(djstr[djname2])]


    print(*reversed(sorted(dj_pair)), sep="\n")
    #'*' is called unpacking operator, used to unpack all the elements of a iterable datatype


def method2():
    global dj
    dj = [Kevin, Stuart, Bob, Edith]
    djcombi = list(combinations(dj, 2))
    #'djcombi' is the list of all the possible pair combinations of sets(Kevin, Stuart, Bob, Edith) in tuples
    #[(set of Kevin, set of Stuart), (set of Kevin, set of Bob)........]

    djcombi_str = list(combinations(djstr, 2))

    percent = list(map(lambda n: round(len(n[0] & n[1])*100/len(n[0]), 5),djcombi))
    #FOLLOWING REQUIRED IF LENGTH OF ALL LISTS ARE DIFF
    '''percent2 = list(map(lambda n: round(len(n[0] & n[1])*100/len(n[1]), 5),djcombi))'''
    #'percent1' and 'percent2' are the lists of all percentages of 1st and 2nd term respectively
    #Eg: (set of Kevin, set of Stuart)
    #percentage of 1st value in tuple(Kevin)  = n[0] & n[1]*100/len(n[0])
    #percentage of 2nd value in tuple(Stuart) = n[0] & n[1]*100/len(n[1])

    per = list(zip(percent, djcombi_str))
    #List of (percent1, percent2, (djname1, djname2)) of all combinations along with djname i.e djname1 and djname2

    per = list(filter(lambda tup: tup[0]>=30, per))
    #Filtering the list having percentage of each individual in a pair>=30

    per = list(reversed(sorted(per)))
    print(*per, sep="\n")

method1()
method2()
