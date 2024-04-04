def main():
    key_materials = {"shards": 0, "fragments": 0, "motes": 0}
    junk = {}

    while True:
        data = input().split()
        for i in range(0, len(data), 2):
            quantity = int(data[i])
            material = data[i + 1].lower()

            if material in key_materials:
                key_materials[material] += quantity
                if key_materials[material] >= 250:
                    if material == "shards":
                        print("Shadowmourne obtained!")
                    elif material == "fragments":
                        print("Valanyr obtained!")
                    elif material == "motes":
                        print("Dragonwrath obtained!")
                    key_materials[material] -= 250
                    remaining_materials(key_materials, junk)
                    return
            else:
                if material in junk:
                    junk[material] += quantity
                else:
                    junk[material] = quantity

def remaining_materials(key_materials, junk):
    for material, quantity in sorted(key_materials.items(), key=lambda x: (-x[1], x[0])):
        print(f"{material}: {quantity}")
    for material, quantity in sorted(junk.items()):
        print(f"{material}: {quantity}")

if __name__ == "__main__":
    main()
