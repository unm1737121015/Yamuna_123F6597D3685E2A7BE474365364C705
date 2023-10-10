#Define the  base class player

class Player:
  def play(self):
      print("The player is playing cricket. ")


# Define the derived class Batman
class Batsman(Player):
 def play(self):
   print("The Batsman is batting.") 
   

# Define the derived class Bowler
class Bowler(Player):
  def play(self):
     print("The Bowler is bowling.")

#Create objects of Batsman and Bowler classesclasses
batsman = Batsman() 
bowler =  Bowler() 

#Call the play()method for each object
batsman.play()
bowler.play()

  