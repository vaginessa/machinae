import yaml
from collections import OrderedDict


class MachinaeLoader(yaml.SafeLoader):
    def construct_mapping(self, node):
        self.flatten_mapping(node)
        return OrderedDict(self.construct_pairs(node))


MachinaeLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
    MachinaeLoader.construct_mapping)


class MachinaeDumper(yaml.Dumper):
    def represent_dict(self, data):
        return self.represent_mapping('tag:yaml.org,2002:map', data, False)

    def represent_list(self, data):
        return self.represent_sequence('tag:yaml.org,2002:seq', data, False)


MachinaeDumper.add_representer(
    OrderedDict,
    MachinaeDumper.represent_dict)

MachinaeDumper.add_representer(
    list,
    MachinaeDumper.represent_list)


def safe_load(*args, **kwargs):
    kwargs["Loader"] = MachinaeLoader
    return yaml.load(*args, **kwargs)


def dump(*args, **kwargs):
    kwargs["Dumper"] = MachinaeDumper
    return yaml.dump(*args, **kwargs)
