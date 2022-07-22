import os

for file in os.listdir("titles"):
    with open("titles/" + file, "w") as f:
        f.write("")