#!/usr/bin/python3
def to_subtract(list_data):
    put_sub = 0
    max_listtt = max(list_data)

    for n in list_data:
        if max_listtt > n:
            put_sub += n

    return (max_listtt - put_sub)


def roman_to_int(roman_stringss):
    if not roman_stringss:
        return 0

    if not isinstance(roman_stringss, str):
        return 0

    rom_no = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    list_keys = list(rom_no.keys())

    nummm = 0
    first_rom = 0
    list_data = [0]

    for ch in roman_stringss:
        for r_num in list_keys:
            if r_num == ch:
                if rom_no.get(ch) <= first_rom:
                    nummm += to_subtract(list_data)
                    list_data = [rom_no.get(ch)]
                else:
                    list_data.append(rom_no.get(ch))

                first_rom = rom_no.get(ch)

    nummm += to_subtract(list_data)

    return (nummm)
