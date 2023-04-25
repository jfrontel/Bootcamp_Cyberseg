import sys
cookbook = {
    'Sandwich': {    
        "ingredients" : ['ham', 'bread', 'cheese', 'tomatoes'],
        "meal" : "lunch",
        "prep_time" : 10
    },

    'Cake': {    
        "ingredients" : ['flour', 'sugar', 'eggs'],
        "meal" : "dessert",
        "prep_time" : 60
    },

    'Salad': {    
        "ingredients" : ['avocado', 'arugula', 'tomatoes', 'spinach'],
        "meal" : "lunch",
        "prep_time" : 15
    }
}
def impr_recipe():
    k = cookbook.keys()
    print(k)

def imp_detalles(nomb):
    print(cookbook[nomb])

def clear_recipe(nomb):
    print(f'--- --- --- {cookbook[nomb]} has been deleted')
    del cookbook[nomb]
    
    
def add_recipe():
    name = input("Enter a name:\n")
    cookbook[name] = {"ingredients" : [], "meal" : "", "prep_time" : 0}
    list_ingred = 'a'
    print("Enter ingredients: ")
    while list_ingred != '':
        list_ingred = input()
        if list_ingred != '':
            cookbook[name]['ingredients'].append(list_ingred)
            
    meal_type = input("Enter a mail type:\n")
    cookbook[name]['meal'] = meal_type        
    
    time_preparat = input("Enter a preparation time: ")
    cookbook[name]['prep_time'] = time_preparat  

def ft_error():
    print('''\n[-] Sorry, this option does not exist.\n
List of available option:\n\n1: Add a recipe\n2: Delete a recipe
3: Print a recipe\n4: Print the cookbook\n5: Quit\n\nPlease select an option:''')
    nb_choose = input()
    choose_menu(int(nb_choose))


def choose_menu(nb_choose):
    
    if (nb_choose < 6 and nb_choose > 0):
        
        if nb_choose == 1:
            add_recipe()
            
        elif nb_choose == 2:
            clear_rec = input("Please enter a recipe name to be deleted:\n")
            if clear_rec in cookbook:
                clear_recipe(clear_rec)
            else:
                ft_error()   
            
        elif nb_choose == 3:
            clear_rec = input("Please enter a recipe name to get its details:\n")
            if clear_rec in cookbook:
                imp_detalles(clear_rec)
            else:
                ft_error()   
            
        elif nb_choose == 4:
                print(cookbook)           
                
        elif nb_choose == 5:
            print("Cookbook closed. Goodbye !")

    else:
        ft_error()
    ft_main_menu(nb_choose)

def ft_main_menu(nb_choose):
    if nb_choose == 5:
        exit()
    else:       
        print('''\nWelcome to the Python Cookbook !\nList of available option:\n\n1: Add a recipe\n2: Delete a recipe
3: Print a recipe\n4: Print the cookbook\n5: Quit\n\nPlease select an option:''')
        nb_choose = input()
        choose_menu(int(nb_choose))


nb_choose = 1
ft_main_menu(nb_choose)



