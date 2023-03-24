import functions


def main():
    user = input("force1/force2: ")
    if user == "force1":
        print(f"F = {functions.force1(mass1=int(input('mass1: ')), mass2=int(input('mass2: ')), radius=int(input('radius: ')))}")
    
    if user == "force2":
        print(f"F = {functions.force2(int(input('mass: ')))}")

if __name__ == "__main__":
    main()
    