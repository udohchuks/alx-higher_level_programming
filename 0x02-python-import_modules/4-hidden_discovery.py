#!/usr/bin/python3
import importlib.util

if __name__ == "__main__":
    if __name__ == "__main__":
        spec = importlib.util.spec_from_file_location("hidden_4", "hidden_4.pyc")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        # Extract the names that do not start with "__"
        names = sorted(
                name
                for name in dir(module)
                if not name.startswith("__")
                )
        # Print the name
        for name in names:
            print(name)
