class Check:
    def __init__(self, index, bool):
        self.i = index
        self.bool = bool


person = []
max_val = [0, 0]


def check_exist(num):
    for i in range(len(person)):
        if person[i][0] == num:
            return Check(i, True)
    return Check(0, False)

print("*** Election ***")
count = int(input("Enter a number of voter(s) : "))
votes = list(map(int, input("").split()))
vote_filtered = filter(lambda vote: vote > 0 and vote <= 20, votes)
vote_list = list(vote_filtered)
count = len(vote_list)

if count <= 0:
    print("*** No Candidate Wins ***")
else:
    for j in range(count):
        check = check_exist(vote_list[j])
        if check.bool:
            person[check.i][1] += 1
        else:
            person.append([vote_list[j], 1])

    for j in range(len(person)):
        if max_val[1] < person[j][1]:
            max_val[0] = person[j][0]
            max_val[1] = person[j][1]

    print(max_val[0])