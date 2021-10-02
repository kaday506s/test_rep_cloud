
def _func_line(size):
    return "#"*size


def _func_special(size):
    space_line = "_" * (size - 4)
    return "##" + space_line + "##"


def _func_char_a():
    "########"
    "##____##"
    "########"
    "##____##"
    line_one = _func_line(6)
    space_line = _func_special(7)

    print(line_one)
    print(space_line)
    print(line_one)
    print(space_line)
    return

"""
#######
#_____#
######_
#_____#
#######


########
##_____
#######
_____##
#######

"""
_char_dict = {
    'a': _func_char_a,
}

value = "abs"

for char in value:

    res = _char_dict[char]
    print(res())


