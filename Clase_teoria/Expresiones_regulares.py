import re
texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Amet et amet."
# patron = "[a-z] {3}"
# print(re.search(patron,texto))
# print(texto[22:26])

# print(re.match(patron,texto))
# print(re.findall(patron,texto))
# print(re.search(patron,texto).group())

patron = "ipsum(.*)sit"
print(re.search(patron,texto), " \n")
print(re.search(patron,texto).group())
print(re.search(patron,texto).group(0))                  #igual que un group sin nada
print(re.search(patron,texto).group(1))

print(re.sub(patron,"###",texto))