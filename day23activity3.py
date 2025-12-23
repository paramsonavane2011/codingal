cellPhoneCountryCodes = {
    "United States": "+1",
    "India": "+91",
    "United Kingdom": "+44",
    "Australia": "+61",
    "Canada": "+1",
    "Germany": "+49",
}

country = input("Enter a country name: ").lower().strip().capitalize()

if country in cellPhoneCountryCodes:
    print(f"Country code of {country} is {cellPhoneCountryCodes[country]}")
else:
    print("Not found")