import csv
fopen = 'reviews.csv'
fwrite = 'sitters.csv'
#Person class
class person:

    #constructor that initializes class attributes
    def __init__(self, n, e, r, profile_s):
        self.name = n
        self.email = e
        self.count = 0
        self.rating = []
        self.rating.append(float(r))
        self.rating_score = 0
        self.profile_score = profile_score
        self.search_score = profile_s

    #This prints out the name, email, ratings and search_score
    def print(self):
        print(self.name + " " + " " + self.email)
        print(self.rating)
        print(self.search_score)

    #These functions were created so that sorting could work
    def __lt__(self,other):
        return self.search_score > other.search_score
    def __eq__(self,other):
        if self.search_score == other.search_score:
            return self.name > other.name

#person_dict is going to store the person's name as key and a person object as value
person_dict = {}
next = False
f = open(fopen)
csvf = csv.reader(f)
for row in csvf:
    if next == False:
        next = True
        continue
    #Have not seen this sitter, so it gets created and stored inside person_dict 
    if(row[6] not in person_dict):
        name = row[6].replace(".", "")
        name = name.replace(" ", "")
        temp = set(name)
        profile_score = round(5 * len(temp) / 26, 2)
        p1 = person(name, row[10], row[0], profile_score)
        p1.count += 1
        person_dict[row[6]] = p1
    #Seen this sitter so we append the ratings along with update the scores
    else:
        t = person_dict[row[6]]
        t.count += 1
        t.rating.append(float(row[0]))
        rating_avg = round(float(sum(t.rating))/float(t.count), 2)
        t.rating_score = rating_avg
        if t.count >= 10:
            t.search_score = rating_avg
        else:
            prof_avg = 1-(0.1*t.count)
            t.search_score = round(
                t.profile_score*prof_avg + (1-prof_avg)*rating_avg, 2)
#This is an unsorted array of people objects
unsorted = []
for i in person_dict:
    unsorted.append(person_dict[i])
#Sort the array in descending order using search_score
sorted_list = sorted(unsorted)
#Write to sitters.csv with the headers and person information
header = ['name','email','profile_score','ratings_score','search_score']
with open(fwrite,'w',encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for i in sorted_list:
        temp = []
        temp.append(i.name)
        temp.append(i.email)
        temp.append(i.profile_score)
        temp.append(i.rating_score)
        temp.append(i.search_score)
        writer.writerow(temp)
