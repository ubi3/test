import random

print("What Does the Cat Say?")

possible_answer = ["szeretlek te csöves"] * 18
possible_answer.append("hm, homok, beleszarok")
possible_answer.append("hm, hal, felfalom")

print(possible_answer[random.randrange(20)])
