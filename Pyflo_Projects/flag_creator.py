def main():
    width = int(input("Flag width:\n"))
    height = int(input("Flag height:\n"))
    half_w = width / 2
    half_h = height / 2
    upper_r(half_w,half_h)
    lower_r(width,half_h)
    
def upper_r(hw,hh):
    while hh > 0:
        hh -= 1
        print("#" * int(hw) + "-" * int(hw))
        
def lower_r(w,hh):
    while hh > 0:
        hh -= 1
        print("-" * int(w))
                
main()