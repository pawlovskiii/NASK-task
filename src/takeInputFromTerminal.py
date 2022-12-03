def takeInputFromTerminal(stringCPE):
    decision = input(
        "Are you prefer to type your CPE2.3 string? If you do not want to, the sample string CPE2.3 will be placed. \nType yes or no.\n"
    )
    if decision == "yes":
        inputedStringCPE = input("Type your CPE2.3 ")
        return inputedStringCPE
    elif decision == "no":
        return stringCPE
    else:
        raise ValueError("Invalid text of the decision. Please try again. Follow the provided instructions.")
