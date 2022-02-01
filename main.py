# simple mad libs style program
import time


print("Welcome to my Mad-Libs style text game.")
print("First, you will set your nouns, adjectives, adverbs and verbs.")

adjective_1 = input("Choose an adjective ")
noun_1 = input("Choose a noun ")
verb_1 = input("Choose a past-tense verb ")
adverb_1 = input("Choose an adverb ")
noun_2 = input("Choose a noun ")
noun_3 = input("Choose a noun ")
adjective_2 = input("Choose an adjective ")
verb_2 = input("Choose a verb ")
adverb_2 = input("Choose an adverb ")
verb_3 = input("Choose a past-tense verb ")
adjective_3 = input("Choose an adjective ")
adjective_4 = input("Choose an adjective ")

time.sleep(2)
print("Calculating....")
time.sleep(1)
print("...")
time.sleep(1)
print("..")
time.sleep(1)
print(".")
time.sleep(2)

print("Today I went to the zoo. I saw a " + adjective_1)

print(noun_1 + " jumping up and down in its tree.")

print("He " + verb_1 + " " + adverb_1)

print("through the large tunnel that led to its " + adjective_2)

print(noun_2 + ". I got some peanuts and passed")

print("them through the cage to a gigantic gray" + noun_3)

print("towering above my head. Feeding that animal made")

print("me hungry. I went to get a " + adjective_3 + " scoop")

print("of ice cream. It filled my stomach. Afterwards I had to")

print(verb_2 + " " + adverb_2 + " to catch our bus.")

print("When I got home I " + verb_3 + " my")

print("mom for a " + adjective_4 + " day at the zoo.")