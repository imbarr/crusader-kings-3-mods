text = ""

with open("output.txt", "w") as out:
    for i in range(0, 244):
        res = """{
			id=repl
			position={ 3.000000 0.000000 0.000000 }
			rotation={ -0.000000 -0.000025 -0.000000 1.000000 }
			scale={ 1.000000 1.000000 1.000000 }
		}
		"""
        text += res.replace("repl", str(i))

    out.write(text)