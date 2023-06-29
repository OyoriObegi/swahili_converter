import streamlit as st

swahili_numbers = {
    0: 'sifuri',
    1: 'moja',
    2: 'mbili',
    3: 'tatu',
    4: 'nne',
    5: 'tano',
    6: 'sita',
    7: 'saba',
    8: 'nane',
    9: 'tisa',
    10: 'kumi',
    20: 'ishirini',
    30: 'thelathini',
    40: 'arobaini',
    50: 'hamsini',
    60: 'sitini',
    70: 'sabini',
    80: 'themanini',
    90: 'tisini',
}
def number_to_swahili(n):
    if n in swahili_numbers:
        return swahili_numbers[n]
    
    if n < 100:
        tens, ones = divmod(n, 10)
        if ones == 0:
            return f'{swahili_numbers[tens * 10]}'
        else:
            return f'{swahili_numbers[tens * 10]} na {swahili_numbers[ones]}'
    
    if n < 1000:
        hundreds, remainder = divmod(n, 100)
        if remainder == 0:
            return f'mia {number_to_swahili(hundreds)}'
        else:
            return f'mia {number_to_swahili(hundreds)} na {number_to_swahili(remainder)}'
    
    if n < 10000:
        thousands, remainder = divmod(n, 1000)
        if remainder == 0:
            return f'elfu {number_to_swahili(thousands)}'
        else:
            return f'elfu {number_to_swahili(thousands)} {number_to_swahili(remainder)}'

import re

def swahili_to_number(s):
    swahili_numbers = {
        "moja": 1,
        "mbili": 2,
        "tatu": 3,
        "nne": 4,
        "tano": 5,
        "sita": 6,
        "saba": 7,
        "nane": 8,
        "tisa": 9,
        "kumi": 10,
        "ishirini": 20,
        "thelathini": 30,
        "arobaini": 40,
        "hamsini": 50,
        "sitini": 60,
        "sabini": 70,
        "themanini": 80,
        "tisini": 90,
        "mia": 100,
        "elfu moja": 1000,
        "elfu kumi": 10000
    }

    words = s.split()
    result = 0
    temp_result = None
    for i, word in enumerate(words):
        if word in swahili_numbers:
            number = swahili_numbers[word]
            if temp_result is None:
                temp_result = number
            else:
                temp_result += number
        elif word.startswith("kumi") and i < len(words) - 1 and words[i + 1] != "na":
            tens_word = word.replace("kumi", "")
            tens = swahili_numbers[tens_word]
            temp_result = tens
        elif word.startswith("mia") and i < len(words) - 1:
            next_word = words[i + 1]
            if next_word == "na":
                temp_result = 0
            else:
                hundreds = swahili_numbers[word]
                if next_word in swahili_numbers:
                    ones = swahili_numbers[next_word]
                    temp_result = hundreds + ones
                elif next_word.startswith("kumi") and i < len(words) - 2 and words[i + 2] != "na":
                    tens_word = next_word.replace("kumi", "")
                    tens = swahili_numbers[tens_word]
                    temp_result = hundreds + tens
        elif word.startswith("elfu") and i < len(words) - 1:
            next_word = words[i + 1]
            if next_word == "na":
                temp_result = 0
            else:
                thousands = swahili_numbers[word]
                if next_word in swahili_numbers:
                    ones = swahili_numbers[next_word]
                    temp_result = thousands + ones
                elif next_word.startswith("kumi") and i < len(words) - 2 and words[i + 2] != "na":
                    tens_word = next_word.replace("kumi", "")
                    tens = swahili_numbers[tens_word]
                    temp_result = thousands + tens
                elif next_word == "elfu" and i < len(words) - 2 and words[i + 2] != "na":
                    next_next_word = words[i + 2]
                    if next_next_word in swahili_numbers:
                        ones = swahili_numbers[next_next_word]
                        temp_result = thousands * 1000 + ones
                    elif next_next_word.startswith("kumi") and i < len(words) - 3 and words[i + 3] != "na":
                        tens_word = next_next_word.replace("kumi", "")
                        tens = swahili_numbers[tens_word]
                        temp_result = thousands * 1000 + tens

        if temp_result is not None and temp_result >= 1000:
            result += temp_result
            temp_result = None

    if temp_result is not None:
        result += temp_result

    return result



def main():
    st.title("Swahili Number Converter")
    st.write("The Swahili Number Converter app allows you to convert numerical numbers to Swahili words and vice versa. Enter a number or a Swahili word and select the corresponding input type.")

    input_type = st.selectbox("Input Type:", ("Number", "Swahili Word"))
    user_input = st.text_input("Enter your input:")

    if input_type == "Number":
        try:
            number = int(user_input)
            result = number_to_swahili(number)
            st.write(f"Swahili: {result}")
        except ValueError:
            st.write("Invalid input. Please enter a valid number.")
    else:
        result = swahili_to_number(user_input)
        st.write(f"Number: {result}")

    st.write("\n")  # Add vertical space
    st.write("Created by Melinda Chebet and Oyori Obegi for Theory of Computation CAT 2 2023")


if __name__ == "__main__":
    main()



