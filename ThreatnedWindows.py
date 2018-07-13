import pyscreenshot as ImageGrab

if __name__ == '__main__':

    # grab fullscreen
    im = ImageGrab.grab()

    # save image file
    im.save('Desktop.png')

    # show image in a window
    im.show()
   import pyscreenshot as ImageGrab

if __name__ == '__main__':
    # part of the screen
    im = ImageGrab.grab(bbox=(10, 10, 510, 510))  # X1,Y1,X2,Y2
    im.show()
    import pyscreenshot as ImageGrab

if __name__ == '__main__':
    # part of the screen
    im = ImageGrab.grab(bbox=(10, 10, 510, 510))  # X1,Y1,X2,Y2
    im.show()
    import pyscreenshot as ImageGrab

if __name__ == '__main__':
    # part of the screen
    im = ImageGrab.grab(bbox=(10, 10, 510, 510))  # X1,Y1,X2,Y2
    im.show()
    import pyscreenshot as ImageGrab

if __name__ == '__main__':
    # part of the screen
    im = ImageGrab.grab(bbox=(10, 10, 510, 510))  # X1,Y1,X2,Y2
    im.show()
    import pyscreenshot as ImageGrab

if __name__ == '__main__':
    # part of the screen
    im = ImageGrab.grab(bbox=(10, 10, 510, 510))  # X1,Y1,X2,Y2
    im.show()
    try:
    a = int(input())
except:
    raise Exception('you corrputed windows idiot')
    try:
    a = int(input())
except:
    raise Exception('you corrputed windows idiot')
    try:
    a = int(input())
except:
    raise Exception('you corrputed windows idiot')
    try:
    a = int(input())
except:
    raise Exception('you corrputed windows idiot')
    import time

print("Is it dark outside?\n==================")

#month_number : sunset_hour
dark = {

    1: 16,
    2: 17,
    3: 18,
    4: 19,
    5: 19,
    6: 20,
    7: 20,
    8: 19,
    9: 18,
    10: 17,
    11: 16,
    12: 16

    }

#month_number : sunrise_hour
light = {

    1: 8,
    2: 7,
    3: 6,
    4: 5,
    5: 4,
    6: 4,
    7: 4,
    8: 5,
    9: 6,
    10: 6,
    11: 7,
    12: 8

    }

#get the structure containing the current time
time_now = time.localtime()

#use the 'light' and 'dark' dictionaries
#it's dark if the hour is later than or equal to the sunset time
#or earlier than the sunrise time.
if time_now.tm_hour >=dark[time_now.tm_mon] or time_now.tm_hour < light[time_now.tm_mon]:
    print("Go Inside Idiot,Sorry If I'm Insulting You.")
else:
    print("Goodbye")
