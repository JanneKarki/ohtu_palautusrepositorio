from urllib import request
from project import Project
import tomli


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        deserialized_toml = tomli.loads(content)

        name = deserialized_toml["tool"]["poetry"]["name"]

        description = deserialized_toml["tool"]["poetry"]["description"]
        if not description:
            description = "-"

        dependencies_list = []
        dependencies = deserialized_toml["tool"]["poetry"]["dependencies"]
        for i in dependencies.keys():
            dependencies_list.append(i)

        dev_list = []
        dev_dependencies = deserialized_toml["tool"]["poetry"]["dev-dependencies"]
        for i in dev_dependencies.keys():
            dev_list.append(i)

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, description, dependencies_list, dev_list)
