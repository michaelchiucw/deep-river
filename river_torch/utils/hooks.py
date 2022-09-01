from torch import nn


class ForwardOrderTracker:
    def __init__(self, layers_to_track) -> None:
        self.ordered_modules = []
        self.layers_to_track = layers_to_track

    def __call__(self, module, input, output):
        if isinstance(module, self.layers_to_track):
            self.ordered_modules.append(module)


def apply_hooks(module, hook, handles):
    for child in module.children():
        apply_hooks(child, hook, handles)
    handle = module.register_forward_hook(hook)
    handles.append(handle)
