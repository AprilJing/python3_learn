my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 * 2.54 # centimeters
my_weight = 180 * 0.454 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print("Let's talk about %s." % my_name)
print("He's %r cm tall" % my_height)
print("He's %r kg heavy." % my_weight)
print("Actually that's not too heavy")
print("He's got %s eyes and %s hair." % (my_eyes, my_hair))
print("His teeth are usually %s depending on the ccoffee." % my_teeth)

# this line is tricky, try to get it exactly right
print("If I add %d, %r, and %f I get %r." % (my_age, my_height, my_weight,
                                             my_age + my_height + my_weight))
print(round(1.7333))