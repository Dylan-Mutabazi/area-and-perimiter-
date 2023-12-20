game.splash("Lets calculate the area of a trapezoid!")
let base_1 = game.askForNumber("whats the first base in cm")
let base_2 = game.askForNumber("whats the second base in cm")
let height = game.askForNumber("whats the height in cm")
let area = (base_1 + base_2) / 2 * height
game.splash(" the area of the trapezoid of height" + height + " cm width bases 1 of " + base_1 + " cm and base 2 " + base_2 + " cm is " + area + " cm^2! ")
