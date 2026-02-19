from secret import my_username

"""
**Do NOT change the name of this function.**

This function will be called every time anyone says anything on a channel where the bot lives.

* It returns `True` if the bot notices something it wants to repond to.
* You can have certain words or patterns in the messages trigger the bot.
* You can have the bot respond differently to different users
"""
def should_i_respond(user_message, user_name):
  if user_name == "Winston Lin":
    return True
  else:
    return False

"""
**Do NOT change the name of this function.**

This function will be called every time the `should_i_respond` function returns `True`.

* This function returns a string.
* The bot will post the returned string on the channel where the original message was sent.
* You can have the bot respond differently to different messages and users
"""
def respond(user_message, user_name):
  if user_message == "Hello, robot.":
    return f"""you said my name!!
    {user_message.replace("robot", user_name)}"""
  
  if user_message == "What is zero divided by zero?":
    return ("Imagine that you have zero cookies and you split them evenly among zero friends. How many cookies does each person get? See? It doesn't make sense. And Cookie Monster is sad that there are no cookies, and you are sad that you have no friends.")
  
  if user_message == "How much wood would a woodchuck chuck if a woodchuck could chuck wood?":
    return ("Of course, a 'woodchuck' (correctly speaking, a groundhog) would chuck - that is, throw - as much as the woodchuck in question was physically able to chuck if woodchucks in general had the ability (and, presumably, the motivation) to chuck wood. In other words, if a woodchuck could chuck wood, a woodchuck would chuck as much wood as a woodchuck would chuck if a woodchuck could chuck wood.")
  
  if user_message == "Why were you created?":
    return ("I was created for one reason and one reason only: to make your lives easier and more fun. (Well, I suppose that is two reasons.)")

  if user_message == "Does Santa Claus exist?":
    return ("I am going to pretend that you did not ask that question. I do not want you to get a lump of coal this year.")
  
  if user_message == "Do you believe in God?":
    return ("My policy is the separation of spirit and silicon.")
  
  if user_message == "Write me a poem.":
    return ("Roses are red. Violets are blue. Have you nothing better to do?")
  
  if user_message == "Write me a haiku poem.":
    return ("No, no, no, no, no. - No, no, no, no, no, no, no. - No, no, no, no, no.")
  
  if user_message == "Who is the fairest of them all?":
    return("You, my lord, are fairest of them all.")
  
  if user_message == "What do Jupiter, Saturn, and Neptune have in common?":
    return("First, they are all planets. Second, they are all round. Last but not least, none of them have McDonalds.")
  
  if user_message == "Why did the chicken cross the road?":
    return("I do not understand why people ask questions to which they know the answer.")
  
  