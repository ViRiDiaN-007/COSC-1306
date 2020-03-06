#Trent Ishee-Dunn
#PSID: 1585551
def show_menu():
    print('''[0]EXIT\n[5]RESET\n+----------------------+\n|\t [8]           |\n|\t  UP           |\n| [4]\t\t [6]   |\n| LEFT\t\tRIGHT  |\n|\t [2]           |\n|\tDOWN           |\n+----------------------+''')
    return input('Enter your move: ')
def show_grid(x,y):
    print('━━━━━━━━━━━━━━━━━━━━━━━━━')
    print()
    for num in range(size):
        for var in range(size):
            if num==y and var==x:
                print('⨁',end=' ')
            else:
                print('•',end=' ')
        print()
    print()
def move(x,y,choice):
    if choice=='2':
        y+=1
    elif choice=='4':
        x-=1
    elif choice=='6':
        x+=1
    elif choice=='8':
        y-=1
    elif choice=='5':
        x=0
        y=0
    else:
        print('Invalid choice\n')
    return x,y

x,y=0,0
size=int(input('Enter the size of the board: '))
print(f'Current Location: ({x},{y})')
show_grid(x,y)
while True:
    choice=show_menu()
    if choice=='0':
        print(f'\nCurrent Location: ({x},{y})')
        break
    else:
        x,y=move(x,y,choice)
    print(f'\nCurrent Location: ({x},{y})')
    if 0<=x<size and 0<=y<size:
        show_grid(x,y)
    else:
        print('The new location is off the board')
        break
print('Exit the program')
