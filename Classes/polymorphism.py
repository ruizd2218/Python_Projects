#declaring parent class
class Alien:
    color = "green"
    eye_color = "red"
    origin = "mars"
    #function that will print their identities to the console when called by the child classes
    def identity(self):
        msg = "This alien is {}, with {} colored eyes, and is from {}".format(self.color, self.eye_color, self.origin)
        return msg
    
#this alien is from mars, so we will only add 2 specific attributes
class MarsAlien(Alien):
    tentacles = 4
    eyes = 6

#this alien is from pluto, so we must change the attributes it possesses to identify it accordingly
class PlutoAlien(Alien):
    color = "red" #all attributes will be changed
    eye_color = "white"
    origin = "pluto"
    legs = 6
    arms = 2

#allows us to print the two aliens to the console
if __name__ == "__main__":
    mars_alien = MarsAlien()
    print(mars_alien.identity())
    

    pluto_alien = PlutoAlien()
    print(pluto_alien.identity())
