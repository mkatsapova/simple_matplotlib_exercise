
import matplotlib.pyplot as plt

data = [33, 25, 20, 12, 10]
plt.figure(num=1, figsize=(6, 6))
plt.axes(aspect=1)
plt.title('Plot`s name', size=14)
plt.pie(data, labels=(f'Group of {data[0]}', f'Group of {data[1]}', f'Group of {data[2]}',
                      f'Group of {data[3]}', f'Group of {data[4]}'))
plt.savefig('figure_with_legend_ex_6.png')
plt.show()
