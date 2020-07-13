def arithmetic_arranger(problems, variable=False):

    if len(problems) > 5:
        return "Error: Too many problems."

    line1 = []
    line2 = []
    line3 = []
    line4 = []

    for op in problems:

        equation = op.split(" ")

        try:
            x = int(equation[0])
            y = int(equation[-1])

            maxlen = 0

            for i in equation:
                if len(i) > maxlen:
                    maxlen = len(i)
                else: continue

            num_spaces = maxlen + 2

            if len(equation[0]) > 4 or len(equation[-1]) > 4:
                return "Error: Numbers cannot be more than four digits."

            elif "+" in equation:
                total = x + y
                
                num_string1 = " " * (num_spaces - len(equation[0])) + equation[0]
                num_string2 = "+" + " " * (num_spaces - len(equation[-1]) - 1) + equation[-1]
                num_string3 = "-" * num_spaces
                num_string4 = " " * (num_spaces - len(str(total))) + str(total)
                line1.append(num_string1)
                line2.append(num_string2)
                line3.append(num_string3)
                line4.append(num_string4) 

            elif "-" in equation:
                total = x - y
                num_string1 = " " * (num_spaces - len(equation[0])) + equation[0]
                num_string2 = "-" + " " * (num_spaces - len(equation[-1]) - 1) + equation[-1]
                num_string3 = "-" * num_spaces
                num_string4 = " " * (num_spaces - len(str(total))) + str(total)
                line1.append(num_string1)
                line2.append(num_string2)
                line3.append(num_string3)
                line4.append(num_string4)

            else:
                return "Error: Operator must be '+' or '-'."    



        except ValueError:
            return "Error: Numbers must only contain digits."
    
    final_line1 = "    ".join(line1)
    final_line2 = "    ".join(line2)    
    final_line3 = "    ".join(line3)
    final_line4 = "    ".join(line4)

    if variable == True:
        arranged_problems = "\n".join([final_line1, final_line2, final_line3, final_line4])
    else: arranged_problems = "\n".join([final_line1, final_line2, final_line3])

    return arranged_problems
    

# print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"]))