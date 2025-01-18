def main():
    width = int(input("Flag width:\n"))
    height = int(input("Flag height:\n"))
    for i in width / 2:
        print("#" + "-") * height / 2
        print("-" * width) * height /2
        
main()