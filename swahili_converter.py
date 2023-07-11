import streamlit as st

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
    
    
def swahili_to_number(string):
    number_mapping = {v: k for k, v in swahili_numbers.items()}
    words = string.lower().split()  # Convert the string to lowercase before splitting
    numerical_number = 0

    if string.lower() in number_mapping:  # Check the lowercase version of the string in the dictionary
        return number_mapping[string.lower()]

    if words[0] in ["kumi", "ishirini", "thelathini", "arobaini", "hamsini", "sitini", "sabini", "themanini", "tisini"]:
        if "na" in words:
            index = words.index("na")
            first_part = " ".join(words[:index])
            second_part = words[index + 1]
            if first_part in number_mapping and second_part in number_mapping:
                numerical_number += number_mapping[first_part] + number_mapping[second_part]
                return numerical_number

   
    return None

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
    st.write("Created by **Melinda Chebet and Oyori Obegi** for Theory of Computation CAT 2 2023")


if __name__ == "__main__":
    main()



