import tools
import time
import speed

print("""
        .__  .__                       __           .__ 
        |  | |__|____    ____    ____ |  | _______  |__|
        |  | |  \__  \  /    \  / ___\|  |/ /\__  \ |  |
        |  |_|  |/ __ \|   |  \/ /_/  >    <  / __ \|  |
        |____/__(____  /___|  /\___  /|__|_ \(____  /__|
                    \/     \//_____/      \/     \/    

                                    --- Famous brand management system
                                    --- Version 2.2.0
""")

speed.bar()


while True:
  
    tools.menu()
    action_str = input('请选择希望执行的操作: ')
    
    if action_str == '0':
        print(""" 
        ___.                      ___.                 
        \_ |__   ____ ___.__. ____\_ |__   ____ ___.__.
        | __ \_/ __ <   |  |/ __ \| __ \_/ __ <   |  |
        | \_\ \  ___/\___  \  ___/| \_\ \  ___/\___  |
        |___  /\___  > ____|\___  >___  /\___  > ____|
            \/     \/\/         \/    \/     \/\/     
        """)
        time.sleep(1)
        break

    elif action_str in ['1','2','3']:

        if action_str == '1':
            tools.new_card()
        elif action_str == '2':
            tools.show_all()
        elif action_str == '3':
            tools.search_card()

    else:
        print('\n input error \n')