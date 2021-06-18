# (control + '/' for comments)

from collections import Counter

mylist = [1,1,1,1,1,1,1,3,3,3,3,3,3,3,2,2,2,2,2,2,4,4,4,5,5]
print(Counter(mylist))

sentence = "How how many times times times does a word word show up up up up up in this this sentence"
print(Counter(sentence.lower().split()))


from collections import defaultdict
d: dict[str,str] = defaultdict(lambda : "null")
d['a'] = 'A'
print(d['a']) #existing key
print(d['b']) #non existing key



from collections import namedtuple
#Dog = NamedTuple('Dog',[ ('age',int), ('breed',str), ('name',str), ])
Dog = namedtuple('Dog',[ 'age', 'breed', 'name' ]) #type: ignore
sammy = Dog(age = 5,breed="Husky",name="Sam")
print(sammy)
print(sammy.age)   #type: ignore
print(sammy.breed) #type: ignore
print(sammy.name)  #type: ignore