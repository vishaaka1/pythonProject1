import random


dictionary = {'name':['vishaal','akash','surya','ajay'],'place':['thanjavur','chennai','coimbatore','malumbicha patti'],
     'game':['basketball','soccer','tennis','cricket'],'food':['pizza','idli','dosa','burger']}
for _ in range(2):
    name =[]
    for keys,values in dictionary.items():
            name.append(random.choice(list(values)))
            random_name = (random.choice(name))
    story = ('''my name is {}, i\'m living in {}
    me and my friend went to play {} and we ate a {} on our way back'''.format(name[0],name[1],name[2],name[3]))
    print(story)








