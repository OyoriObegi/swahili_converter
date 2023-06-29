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
    

def swahili_to_number(s):
    number_mapping = {v: k for k, v in swahili_numbers.items()}
    words = s.split()
    result = 0
    temp_result = None
    for word in words:
        if word == "na":
            continue
        if word == "sifuri":
            temp_result = 0
        elif word == "mia":
            if temp_result is None:
                temp_result = 100
            else:
                temp_result *= 100
        elif word == "elfu":
            if temp_result is None:
                temp_result = 1000
            else:
                temp_result *= 1000
        elif word in swahili_numbers:
            temp_result = swahili_numbers[word]
        
        if temp_result is not None:
            result += temp_result
            temp_result = None

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



