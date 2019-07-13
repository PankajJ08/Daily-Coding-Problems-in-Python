"""Given a number in Roman numeral format, convert it to decimal."""
import importlib
importlib.import_module("graph")
def roman_number(num, roman):
    """Function that take number into Roman format and convert into decimal format."""
    ans = 0
    for i in range(len(num)):
        if i == 0:
            ans += roman[num[i]]
        else:
            if roman[num[i]] <= roman[num[i - 1]]:
                ans += roman[num[i]]
            else:
                ans += roman[num[i]] - 2* roman[num[i - 1]]

    return ans


if __name__ == "__main__":
    roman = {
        'M': 1000,
        'D': 500,
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        'I': 1
    }

    n = "XIII"
    print(roman_number(n, roman))
