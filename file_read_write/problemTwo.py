# 2. https://github.com/codebasics/py/blob/master/Basics/Exercise/13_read_write_files/read_write_file_exercise.md

with open("stocks.csv", "r") as f, open("output.csv", "w") as out:
    out.write("Company Name,PE Ratio, PB Ratio\n")
    print(f)
    next(f)
    for line in f:
        # print(line)
        tokens = line.split(",")
        stock = tokens[0]
        print(stock)
        price = float(tokens[1])
        eps = float(tokens[2])
        book = float(tokens[3])
        pe = round(price / eps, 2)
        pb = round(price / book, 2)
        out.write(f"{stock},{pe},{pb}\n")