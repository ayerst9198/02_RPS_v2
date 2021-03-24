def statement_generator(statement, left_side_decoration, top_decoration, bottom_decoration, right_side_decoration):
    left_sides = left_side_decoration * 3

    right_sides = right_side_decoration * 3

    statement = "{} {} {}".format(left_sides, statement, right_sides)

    top_bottom = top_decoration * len(statement)

    bottom_bottom = bottom_decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(bottom_bottom)

    return ""