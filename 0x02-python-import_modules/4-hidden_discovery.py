import dis

if __name__ == "__main__":
    with open("hidden_4.pyc", "rb") as file:
        code = file.read()
        # Disassemble the bytecode
        instructions = dis.get_instructions(code)
        # Extract the names that do not start with "__"
        names = sorted(
                instruction.argval
                for instruction in instructions
                if instruction.opname == "LOAD_CONST" and not instruction.argval.startswith("__")
                )
        # Print the names
        for name in names:
            print(name)
