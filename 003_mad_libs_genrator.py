story = '''One [adjective] day, [person_name] decided to order a pizza with [number] [adjective2] [food_item](s). 
When the delivery arrived, the [noun] was [verb_ending_with_ing] on top of the pizza box! 
"[exclamation]!" shouted [person_name]. They immediately called the [place] to complain. 
The manager was so [adjective3] that they offered free [dessert] for a [time_period].'''

adjective = input("enter an adjective : ")

person_name = input("enter a person's name : ")

number = input("enter a number : ")

adjective2 = input("enter an adjective : ")

food_item = input("enter a food item : ")

noun = input("enter a noun : ")

verb_ending_with_ing = input("enter a verb ending in 'ing' : ")

exclamation = input("enter a exclamation : ")

place = input("enter a place : ")

adjective3 = input("enter an adjective : ")

dessert = input("enter a name of dessert : ")

time_period = input("enter a time period : ")


new_story = story.replace("[adjective]", adjective)

new_story = new_story.replace("[person_name]", person_name)

new_story = new_story.replace("[number]", number)

new_story = new_story.replace("[adjective2]", adjective2)

new_story = new_story.replace("[food_item]", food_item)

new_story = new_story.replace("[noun]", noun)

new_story = new_story.replace("[verb_ending_with_ing]", verb_ending_with_ing)

new_story = new_story.replace("[exclamation]", exclamation)

new_story = new_story.replace("[place]", place)

new_story = new_story.replace("[adjective3]", adjective3)

new_story = new_story.replace("[dessert]", dessert)

new_story = new_story.replace("[time_period]", time_period)


print (new_story)