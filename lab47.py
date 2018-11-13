file1 = open('.\\data\\PythonIntroduction')
readme_txt1 = file1.read()
print type(readme_txt1), len(readme_txt1), readme_txt1[:60]
file1.close()

with open('.\\data\\PythonIntroduction') as file2:
    readme_txt2 = file2.read().decode('UTF-8')
    print type(readme_txt2), len(readme_txt2), readme_txt2[:60]

file3 = open('.\\data\\clone1', 'w')
file3.write(readme_txt1)
file3.close()
with open('.\\data\\clone2', 'w') as file4:
    file4.write(readme_txt2.encode('UTF-8'))
