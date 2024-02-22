print("\nARR! WHO GOES THERE?! LOOKING FOR SOME TREASAA ARR WE? HERE YOU'LL NEED A MAP MATEY!")

print('''
  ____________________________________________________________________
 / \-----     ---------  -----------     -------------- ------    ----/
 \_/__________________________________________________________________/
 |~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
 |  _   ~~ ~~ __,---'_       "         `. ~~~ _,--.  ~~~~ __,---.  ~~|
 | | \___ ~~ /      ( )   "          "   `-.,' (') \~~ ~ (  / _\ \~~ |
 |  \    \__/_   __(( _)_      (    "   "     (_\_) \___~ `-.___,'  ~|
 |~~ \     (  )_(__)_|( ))  "   ))          "   |    "  \ ~~ ~~~ _ ~~|
 |  ~ \__ (( _( (  ))  ) _)    ((     \/      " |   "    \_____,' | ~|
 |~~ ~   \  ( ))(_)(_)_)|  "    ))    /\   " __,---._  "  "   "  /~~~|
 |    ~~~ |(_ _)| | |   |   "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |
 | ~~     |  |  |   |   _,--- ,--. _  "  (~~  ~~~~  ~~~ ) /___\ \~~ ~|
 |  ~ ~~ /   |      _,----._,'`--'\.`-._  `._~~_~__~_,-'  |H__|  \ ~~|
 |~~    / "     _,-' / `\ ,' / _'  \`.---.._          __        " \~ |
 | ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   " " \~|
 |  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \ \_   " |~|
 | ~ | | -- _    /~/  `-_- _  _,' '  \ \_`-._,-'  / --   \  - \_   / |
 |~~ | \ -      /~~| "     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|
 | ~~\  \_ /   /~~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|
 |~   \      ,'~~|  " (o o)   "         " " |~~~ \_,-' ~ `.     ,'~~ |
 | ~~ ~|__,-'~~~~~\    \"/      "  "   "    /~ ~~   O ~ ~~`-.__/~ ~~~|
 |~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|
 |____~jrei~__~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|
 / \----- ----- ------------  ------- ----- -------  --------  -------/
 \_/__________________________________________________________________/ 
\n\n''')

startingPoint = input("NOW THAT YOU HAVE A MAP, WHERE DO YOU WANNA HEAD TO?(Woods, Pond, House)\t")

lowerCaseStartingPoint = startingPoint.lower()
#####################################################################################################################################################

if lowerCaseStartingPoint == "woods":
    print("\nARR I HATE THE WOODS, THEM MOSQUITOS ARE ANNOYING!")
    print('''
               ,@@@@@@@,
       ,,,.   ,@@@@@@/@@,  .oo8888o.
    ,&%%&%&&%,@@@@@/@@@@@@,8888\88/8o
   ,%&\%&&%&&%,@@@\@@@/@@@88\88888/88'
   %&&%&%&/%&&%@@\@@/ /@@@88888\88888'
   %&&%/ %&%%&&@@\ V /@@' `88\8 `/88'
   `&%\ ` /%&'    |.|        \ '|8'
       |o|        | |         | |
       |.|        | |         | |
jgs \\/ ._\//_/__/  ,\_//__\\/.  \_//__/_
''')
    woodsChoices = input("\nGO ON PICK A DIRECTION MATEY!(Left, Front, Right)\t")
    lowerCaseWoodsChoices = woodsChoices.lower()

    if lowerCaseWoodsChoices == "left":
        print("\nTHOSE BEARS DON'T LOOK TO FRIENDLY MATEY! RUN!!\n\n!!-- GAME OVER --!!\n")

    elif lowerCaseWoodsChoices == "front":
        print("\nARRIGHT MATEY LETS CONTINUE FORTH!")

        

    elif lowerCaseWoodsChoices == "right":
        print("\nNICE WOLF NICEE WOLFF NO NO WAIT!!\n\n!!-- GAME OVER --!!\n")

    else:
        print("\nARR, YOU TURNING BACK NOW?")

#####################################################################################################################################################  
elif lowerCaseStartingPoint == "pond":
    print("\nAYE, A POND MATEY? HOPE YOU CAN SWIM!")
    print('''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~              
        ,---,
  _    _,-'    `--,
 ( `-,'            `\\
  \           ,    o \\
  /   ,       ;       \\
 (_,-' \       `, _  ""//
        `-,___ =='__,-'
              ````
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~              
              ,
             .';
         .-'` .'
       ,`.-'-.`\\
      ; /     '-'
      | \       ,-,
      \  '-.__   )_`'._
       '.     ```      ``'--._
      .-' ,                   `'-.
       '-'`-._           ((   o   )
              `'--....(`- ,__..--'
                       '-'`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~              

                    _ _ _
                ,="`/ / /'=.
               / / / / / / /'.
              /_/_/_/_/_/ / / \     _.='//
           .-' - _ - _ -`"-,/ /\  .'_.='//
          / -_ - _ - _ - _ -\/.'|/_.=`//
         / @    _="`} _- _- _\.=/_. =";
        /     -"_="} - _  - _ -=_-_"=;
        \-.   '=._}          ,._--_=_;
         `-._     ._        /;' \ `"=.;
             `"\`;-.}_ _ _.;\ \/ \'=._\\
               \ =.}\ \ \ \ \'   '._=_.\\
                 \_}`=._\_\.'`       '=.\\
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~              
''')
    pondChoices = input("\nPICK YOUR PATH MATEY, PICK CORRECTLY!(Piranhas, Tiger Sharks, Stonefishes)\t")
    lowerCasePondchoices = pondChoices.lower()

    if lowerCasePondchoices == "piranhas":
        print("\nCOME ON MATEY EVEN I'M NOT THAT BRAVE!\n\n!!-- GAME OVER --!!\n")

    elif lowerCasePondchoices == "tiger sharks":
        print("\nWELL DONE THOSE SHARKS WON'T EAT YOU, THEY PREFER FISH! WHOA THERE'S THE TREASURE RIGHT THERE!\n\n!!-- YOU WIN --!!\n")

    elif lowerCasePondchoices == "stonefishes":
        print("\nDON'T LET THEIR SIZE FOOL YOU MATEY!\n\n!!-- GAME OVER --!!\n")

    else:
        print("\nARR, WHAT'S A LITTLE WATER GONNA HARM YOU??")

#####################################################################################################################################################

elif lowerCaseStartingPoint == "house":
    print("\nHUH? A HOUSE ON AN ISLAND, DOESN'T SOUND LIKE A GOOD IDEA MATEY...")
    print('''
                       _
                     _( )_ 
                    (_)*(_)
                    /\/I\/\   
                   /\/   \/\                         (
                  /\/~~~~~\/\                       (  (
                 /\/~~~~~~~\/\                     ___(___
                /\/         \/\                    [_I_I_]
               /\/  .*   *.  \/\___________________[_I_I_]_______
              /\/ . *  *  * . \/\     _-   _-      [I_I_I]    _- |
             /\/*    *   *    *\/\ _-   _-    _-     _-    _-    |
            /\/   *    *    *   \/\______________________________|
           /\/  *    * | *    *  \/\        _          _        |
          /\/    ' *   |   * '    \/\     _( )_      _( )_      |
         /\/           I           \/\   (_)*(_)    (_)*(_)     |
         \/|                       |\/      I          I        |
           |~~~~~~~~~~~~~~~~~~~~~~~|   _____   ______   _____   |
           |~~~~~~~~~~~~~~~~~~~~~~~|  |     | |      | |     |  |
           |           ()          |  |~~!~~| |  /\  | |~~!~~|  |
           |  _______ ()() _______ |  |_____| |  \/  | |_____|  |
           |  | /|\ |  ()  | /|\ | |  ======= |o     | =======  |
           |  |/ | \|      |/ | \| |______    |      |    ______|
           |  |--+--|      |--+--| |||||||\___|______|___/||||||| ()  ()  ()  ()
  ()  ()  (|  |\ | /|      |\ | /| ||||||||\____________/||||||||()()()()()()()()
 ()()()()()|  |_\|/_|      |_\|/_| |@@@@@@@|\__________/|@@@@@@@|""""""""""""""""
 """"""""""|  =======      ======= |"""""""\|__________|/"""""""
           |()  ()  ()  ()  ()  () |       //__________\\
           ()()()()()()()()()()()()lc     //____________\\
           """""""""""""""""""""""""     //______________\\
''')
    houseChoices = input("\nCHOOSE THE WAY YOU WANNA ENTER!(Front door, Fence door, Window)\t")
    lowerCaseHouseChoices = houseChoices.lower()

    if lowerCaseHouseChoices == "front door":
        print("\nDARRN THE DOOR IS LOCKED! WAIT IT'S OPENING?! AHHH!\n\n!!-- GAME OVER --!!\n")

    elif lowerCaseHouseChoices == "fence door":
        print("\nHAHA LUCKILY THEIR FENCE IS SHORT! KEEP GOING, BUT QUITELY! WHOA THERE'S THE TREASURE RIGHT THERE!\n\n!!-- YOU WIN --!!\n")

    elif lowerCaseHouseChoices == "window":
        print("\nYOU AREN'T A SPY! WAIT, DO I HEAR FOOTSTEPS?? OH NOOO!!\n\n!!-- GAME OVER --!!\n")

    else:
        print("\nOH COME ON IT'S NOT THAT SPOOKY!")

#####################################################################################################################################################

else:
    print("\nARR, PICK ONE OF THEM CHOICES MATEY!")
