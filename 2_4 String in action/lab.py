number_dictionary = {
    '1': [
        "#",
        "#",
        "#",
        "#",
        "#",
    ],
    '2': [
        "###",
        "  #",
        "###",
        "#  ",
        "###",
    ],
    '3': [
        "###",
        "  #",
        "###",
        "  #",
        "###",
    ],
    '4': [
        "# #",
        "# #",
        "###",
        "  #",
        "  #",
    ],
    '5': [
        "###",
        "#  ",
        "###",
        "  #",
        "###",
    ],
    '6': [
        "###",
        "#  ",
        "###",
        "# #",
        "###",
    ],
    '7': [
        "###",
        "  #",
        "  #",
        "  #",
        "  #",
    ],
    '8': [
        "###",
        "# #",
        "###",
        "# #",
        "###",
    ],
    '9': [
        "###",
        "# #",
        "###",
        "  #",
        "###",
    ],
    '0': [
        "###",
        "# #",
        "# #",
        "# #",
        "###",
    ],
}

n_led = input("Enter numbers for LED display.")
led_display = [
    "",
    "",
    "",
    "",
    "",
]

for num in n_led:
    print(f"number adding to led seqeunce: {num}")
    for ind in range(len(led_display)):
        print(f"index adding to led seqeunce: {ind}")
        led_display[ind] += number_dictionary[num][ind] + ' '

for row in led_display: 
    print(row)