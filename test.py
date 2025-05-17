import os

ip = int(input("How many times do you want to commit? \n"))
autoPush = input("Auto git push when committed? (y/n) \n")

for i in range(ip):
    os.system('git add .')  # This still works, but even without changes it will not block the commit
    os.system(f'git commit --allow-empty -m "Commit {i + 1} of {ip}"')

print(f"Committed {ip} times.")

if autoPush.lower() == "y":
    os.system('git push')
