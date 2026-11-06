from beam import read_config

config = read_config("config.json")
E = config["E"]
I = config["I"]
spans = config["spans"]
point_loads = config["point_loads"]
uniform_loads = config["uniform_loads"]

print(E, I)
print(spans)