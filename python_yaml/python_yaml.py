import yaml


class PythonYaml:
    def __init__(self):
        self.data = yaml.safe_load(open("./data.yaml"))
        # print(self.data)

    def read_list(self):
        for i in range(len(self.data["height"])):
            print("身高是{}，体重是{}".format(self.data["height"][i], self.data["weight"][i]))


if __name__ == '__main__':
    py1 = PythonYaml()
    py1.read_list()
