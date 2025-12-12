# tv_show.py file
# main program
import tv

    

def main():
    #object creation
    tv1=tv.TV()

    #object usage
    if(tv1.show_is_on()):
        print(f"TV is ON, channel {tv1.show_channel()}")
    else:
        print("TV is OFF")

    tv1.turn_on()
    if(tv1.show_is_on()):
        print(f"TV is ON, channel {tv1.show_channel()}")
    else:
        print("TV is OFF")

    tv1.turn_off()
    if(tv1.show_is_on()):
        print(f"TV is ON, channel {tv1.show_channel()}")
    else:
        print("TV is OFF")


if __name__ == "__main__":
   main()