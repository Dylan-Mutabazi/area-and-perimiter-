game.splash("Lets calculate the area of a trapezoid!")
base_1 = game.ask_for_number("whats the first base in cm")
base_2 = game.ask_for_number("whats the second base in cm")
height = game.ask_for_number("whats the height in cm")
area = (base_1 + base_2) / (2 * height)
game.splash(" the area of the trapezoid of height" + ("" + str(height)) + " cm width bases of " + ("" + str(base_1)) + " cm and " + ("" + str(base_2)) + " cm is " + ("" + str(area)) + " cm^2! ")