# Nepali Municipalities
[![Downloads](https://static.pepy.tech/personalized-badge/nepal-sub-divisions?period=total&units=international_system&left_color=black&right_color=yellowgreen&left_text=Downloads)](https://pepy.tech/project/nepal-sub-divisions)


This is a simple and small python package contributed by me to get all list of municipalities of Nepal based on given districts of Nepal on latest version now you can autocomplete other info when municipalities name is given.

# Contents
Installation
Use the package manager pip to install nepal-sub-divisions.


To Autocomplete all info based on municipalities name provided
for example if you provide municipalities names then rest of district and province will be autocompleted.

```python
from nepal_municipalities import NepalMunicipality

print(NepalMunicipality.all_data_info('Kathmandu'))
[{'province': 'Province 3', 'country': 'Nepal', 'id': 311, 'district': 'Kathmandu', 'name': 'Kathmandu'}]
```

**If No matching municipalities are supplied The Exception is thrown as below**
``` python
No matching info for provided municipalities try changing spelling or try another name.
```



**To get list of all districts of Nepal**

```python
from nepali_municipalities import NepalMunicipality

print(NepalMunicipality.all_districts()) # this will also give the same result
# ['Bhojpur', 'Dhankuta', 'Ilam', 'Jhapa', ......]

print(NepalMunicipality.all_districts("Koshi")) # search by province name
# ['Morang', 'Sankhuwasabha', 'Udayapur', 'Jhapa', ......]

```

To get list of all municipalities of Nepal based on District provided.

```python
from nepali_municipalities import NepalMunicipality

print(NepalMunicipality.municipalities('Kathmandu'))

# ['Kathmandu', 'Kageshwori Manohara', 'Kirtipur', 'Gokarneshwor', 'Chandragiri', 'Tokha', 'Tarkeshwor', 'Dakchinkali', 'Nagarjun', 'Budhanilkantha', 'Shankharapur']

```


# Contributing
PRs are welcomed. Please, let me know if you have any suggestions or find any bugs.


## License
[MIT](https://choosealicense.com/licenses/mit/)
