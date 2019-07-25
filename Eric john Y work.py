
record = True
index = []
my_empty = []
while record:

    my_list =["0.create","1.Read","2.update","3.delete","4.exit"]
    print(my_list)

    num = (input("enter number: ")).lower()

    if num == "0":
        songs = (input("enter song: ")).lower()
        my_empty.append(songs)
        print("Done:")
    elif num == "1":
        print(my_empty)
    elif num == "2":
        index = int (input("index: "))
        update = input("enter new song: ") .lower()
        my_empty [index] = update
        print("recorded")
    elif num == "3":
        songremove = input("enter song to delete: ")
        my_empty.remove(songremove)
        print("deleted")
    elif num == "4":
        record = False
    else:
        record = True
        
