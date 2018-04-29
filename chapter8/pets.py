def describle_pets(pet_name,animal_type='dog'):
    """show infomation of pets"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name + ".")
    
describle_pets('jack')
describle_pets(animal_type='monkey',pet_name='ross')

describle_pets(pet_name='harry')
describle_pets()
