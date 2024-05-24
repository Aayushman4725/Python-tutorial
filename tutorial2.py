#Create a list of names and print the second item.
name_list=['Ram','Rita','Shankar','Devi']
print(name_list[1])

#Create a list of sports and then replace the second item with another sport.
sport_list=['Basketball','Soccer','Table Tennis','Hockey']
sport_list[1]='Baseball'
print(sport_list[1])

#Create a list containing num ber and delete the fifth number from the array.
num_list=[1,23,45,25,12,20]
print(num_list)
del num_list[4]
print(num_list)

#Create two list of numbers and merge them.
num_list2=[2,22,14,16,42,68]
print(num_list+num_list2)

#Create a list of numbers and find the length, minimum and maximum.
num_list3=num_list+num_list2
print(len(num_list3))
print(max(num_list3))
print(min(num_list3))

#Create a dictionary with the key being names and values being ages and then delete the sencond key/value pair.
name={'aryan':20,'sabish':15,'sayush':18}
print(name)
del name['sabish']
print(name)

#Create a dictionary of students and scores and printn out a student's score
marks={'atish':90,'sabin':'99','kushal':80}
print(marks['kushal'])

#Create a dictionary of names and ages and the print out all the keys an values.
name2={'Gita':20,'Sita':18,'Hari':19}
print(name2)

#Create a tuple of your favourite movies.
movies=('Infinity War','Toy Story','Kung fu panda','Harry Potter')
print(movies)

#Create a tuple and print all the items from the first to third index.
print(movies[0:3])


