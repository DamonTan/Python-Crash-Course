bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0].title())
print(bicycles[-1].title())
print(bicycles[-2].title())

message = "My first bicycle is a " + bicycles[0] + "."
print(message)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles[0])
motorcycles[0] = 'ducti'
print(motorcycles[0])

motorcycles.append('honda')
print(motorcycles)

too_expensive = motorcycles.remove('honda')
print(motorcycles)

#motorcycles.sort(reverse=True)
print(motorcycles)


#popped_motorcycle = motorcycles.pop(2)
#print(motorcycles)
#print(popped_motorcycle)



