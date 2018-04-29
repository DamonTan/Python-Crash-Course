def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing model: " + current_design)
        completed_models.append(current_design)
        
def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for model in completed_models:
        print(model)
        
unprinted_designs = ['iphone', 'robot', 'mirror']
completed_modles = []

print_models(unprinted_designs,completed_modles)
show_completed_models(completed_modles)
