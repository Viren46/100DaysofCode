##Hurdles with Variable Heights Challenge
#Open the URL and paste the code to test it out
#http://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json


def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def start():
    if wall_in_front() and not is_facing_north():
        turn_left()
        while wall_on_right():
            if wall_in_front():
                turn_left()
            else:
                move()
        turn_right()
        move()
        turn_right()
        move()
    else:
        move()
        
while not at_goal():
    start()