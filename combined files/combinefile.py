import fileinput
import glob


file_list = glob.glob("*.txt")
file = open("result.txt", "w", encoding='utf-8')
input_lines = fileinput.input(file_list, encoding='utf-8')
file.writelines(str(line)+"\n" for line in input_lines)

# f = open("result.txt", "w+")
# f.write("output")
