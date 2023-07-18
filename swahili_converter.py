import streamlit as st
import re

swahili_numbers = {
    0: 'sufuri',
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
    100: 'mia moja'
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

def swahili_to_number(string):
    number_mapping = {v: k for k, v in swahili_numbers.items()}
    words = string.lower().split()  # Convert the string to lowercase before splitting
    numerical_number = 0

    if string.lower() in number_mapping:  # Check the lowercase version of the string in the dictionary
        return number_mapping[string.lower()]

    # Regular expression pattern to match numbers like 'kumi', 'ishirini', etc.
    number_pattern = r'\b(?:kumi|ishirini|thelathini|arobaini|hamsini|sitini|sabini|themanini|tisini)\b'
    # Regular expression pattern to match the separator 'na'
    separator_pattern = r'\bna\b'

    # Join the words together to form the input string
    input_string = ' '.join(words)

    # Use regular expressions to detect and extract the numerical values and separator
    matches = re.findall(number_pattern, input_string)
    separator_matches = re.findall(separator_pattern, input_string)

    # Calculate the numerical number by summing up the extracted numerical values
    numerical_number = sum(number_mapping[match] for match in matches)

    # Check if 'na' is present, and adjust the numerical number accordingly
    if len(separator_matches) == 1 and matches:
        index = input_string.index('na')
        prefix = input_string[:index].strip()
        suffix = input_string[index + 2:].strip()
        if prefix in number_mapping and suffix in number_mapping:
            numerical_number += number_mapping[suffix]

    return numerical_number

def main():
    st.title("Swahili Number Converter")
    st.write("The Swahili Number Converter app allows you to convert numerical numbers to Swahili words and vice versa. Enter a number or a Swahili word and select the corresponding input type.")

    input_type = st.selectbox("Input Type:", ("Number", "Swahili Word"))
    user_input = st.text_input("Enter your Input:")

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
    st.write("Created by **Melinda Chebet and Oyori Obegi** for Theory of Computation CAT 2 2023")

if __name__ == "__main__":
    main()
