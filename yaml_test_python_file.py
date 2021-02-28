import yaml

path_to_yaml_file = ('/Users/davnnis2003/PycharmProjects/jimmy-playground/config.yaml')
print(path_to_yaml_file)

with open(r'/Users/davnnis2003/PycharmProjects/jimmy-playground/config.yaml') as file:
    fruits_list = yaml.load(file, Loader=yaml.FullLoader)

    print(fruits_list)
