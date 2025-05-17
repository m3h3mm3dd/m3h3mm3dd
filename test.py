import os

ip = int(input("How many times do you want to commit? \n"))
autoPush = input("Auto git push when committed? (y/n) \n")

for i in range(ip):
    os.system('git add .')
    os.system(f'git commit -m "Commit {i + 1} of {ip}"')

print(f"Committed {ip} times.")

if autoPush.lower() == "y":
    os.system('git push')
