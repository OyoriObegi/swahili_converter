# Swahili Number Converter
The Swahili Number Converter is a Python application that allows you to convert numerical numbers to their Swahili word representations and vice versa. The application is designed as a learning exercise for understanding Regular Expressions in Theory of Computing, a Computer Science Undergraduate Course.

# How it Works
The application currently supports numerical numbers between 0 and 100, inclusive. It utilizes a set of predefined mappings in the swahili_numbers dictionary to convert numerical numbers to their corresponding Swahili words. For example, it can accurately convert numbers like 5, 20, 45, 60, and 100 to their respective Swahili word representations.

For numbers less than 100, the application breaks them down into tens and ones, and then combines the Swahili word representations for these parts. For example, the number 45 is split into 40 (arobaini) and 5 (tano), and the application combines them as "arobaini na tano."

The swahili_to_number function allows you to convert Swahili words back to numerical numbers. It can handle certain Swahili words like "kumi" (10), "ishirini" (20), etc., and it can recognize the word "na" (and) as a separator between numbers in Swahili.

# Future Extensions
1. *Handling Larger Numbers:* To support numbers beyond 100, you can expand the swahili_numbers dictionary to include mappings for thousands, millions, and so on.

2. *Decimal and Fraction Support:* Modify the functions to handle decimal numbers and fractions in both numerical and Swahili word representations.

3. *Enhance Swahili Parsing:* Improve the Swahili-to-number conversion logic to handle more complex structures and patterns in the Swahili language.

4. *Error Handling:* Implement better error handling for invalid inputs or cases where the input does not match any known patterns.

5. *Negative Number Support:* Add support for negative numbers in both directions.

# Getting Started
1. Install the required dependencies by running: pip install streamlit.

2. Run the application using the command: streamlit run swahili_number_converter.py.

3. The application will launch in your default web browser, allowing you to interact with it.

# Contributing
We welcome contributions to improve and extend the functionality of the Swahili Number Converter. If you have any ideas or improvements, feel free to open an issue or submit a pull request.

# Credits
The Swahili Number Converter application was created for the Theory of Computation Class, 2023.


Test the app here: [https://swahiliconverter.streamlit.app/#swahili-number-converter]
