note_one = 15.8
note_max_1 = 20
coeff_one = 1

note_two = 14
note_max_2 = 20
coeff_two = 1

note_three = 10.4
note_max_3 = 20
coeff_three = 1

note_four = 13.8
note_max_4 = 20
coeff_four = 1

note_five = 14.8
note_max_5 = 20
coeff_five = 1

note_six = 11.75
note_max_6 = 20
coeff_six = 1

note_seven = 15.12
note_max_7 = 20
coeff_seven = 1

note_eight = 14
note_max_8 = 20
coeff_eight = 1

note_nine = 19.5
note_max_9 = 20
coeff_nine = 1

note_ten = 0
note_max_10 = 0
coeff_ten = 0


average = (
    note_one * coeff_one
    + note_two * coeff_two
    + note_three * coeff_three
    + note_four * coeff_four
    + note_five * coeff_five
    + note_six * coeff_six
    + note_seven * coeff_seven
    + note_eight * coeff_eight
    + note_nine * coeff_nine
    + note_ten * coeff_ten
)

max_number = (
    note_max_1 * coeff_one
    + note_max_2 * coeff_two
    + note_max_3 * coeff_three
    + note_max_4 * coeff_four
    + note_max_5 * coeff_five
    + note_max_6 * coeff_six
    + note_max_7 * coeff_seven
    + note_max_8 * coeff_eight
    + note_max_9 * coeff_nine
    + note_max_10 * coeff_ten
)

average_final = average * 20
average_final = average_final / max_number

print(average_final)


# note_one = 15.3
# note_max_1 = 20
# coeff_one = 1

# note_two = 14.5
# note_max_2 = 20
# coeff_two = 1

# note_three = 10.1
# note_max_3 = 20
# coeff_three = 1

# note_four = 10.1
# note_max_4 = 20
# coeff_four = 1

# note_five = 12.4
# note_max_5 = 20
# coeff_five = 1

# note_six = 13.33
# note_max_6 = 20
# coeff_six = 1

# note_seven = 15.8
# note_max_7 = 20
# coeff_seven = 1

# note_eight = 17
# note_max_8 = 20
# coeff_eight = 1

# note_nine = 14
# note_max_9 = 20
# coeff_nine = 1

# note_ten = 0
# note_max_10 = 0
# coeff_ten = 0
