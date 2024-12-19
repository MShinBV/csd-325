# Miles Shinsato 11/29/2024 Assignment 7.2

# Defining a function to be called upon
def city_country(city, country, population=None, language=None):

    # Using xxx.title () to Ensure that city, country, and language are properly capitalized
    # Returns a formatted string of the form 'City, Country' - Population: 'Population'.
    # Population is now optional, Language is now optional using if statements
    result = f"{city.title()}, {country.title()}"
    if population:
        result += f" - Population: {population}"
    if language:
         result += f", {language.title()}"
    return result

# Call the function with various inputs and print the results
# Formatted as City, Country, Population, Language
print(city_country("Santiago", "Chile", 5000000, "Spanish"))
print(city_country("Tokyo", "Japan", 9733000, "Japanese"))
print(city_country("Seoul", "South Korea", 9411000, "Korean"))
