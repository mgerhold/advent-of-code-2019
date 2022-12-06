def execute_program(program: list[int]) -> None:
    for i in range(0, len(program), 4):
        opcode = program[i]
        if opcode == 99:
            return
        lhs_index = program[i + 1]
        rhs_index = program[i + 2]
        result_index = program[i + 3]
        if opcode == 1:
            program[result_index] = program[lhs_index] + program[rhs_index]
        elif opcode == 2:
            program[result_index] = program[lhs_index] * program[rhs_index]
        else:
            assert False, "unknown opcode"

# part 1
with open("input.txt") as file:
    program = [int(x) for x in file.readline().strip().split(',')]
    program[1] = 12
    program[2] = 2
    execute_program(program)
    print("part 1:", program[0])

# part 2
with open("input.txt") as file:
    initial_memory = [int(x) for x in file.readline().strip().split(',')]
    for noun in range(0, 100):
        for verb in range(0, 100):
            program = initial_memory.copy()
            program[1] = noun
            program[2] = verb
            execute_program(program)
            if program[0] == 19690720:
                print("part 2:", 100 * noun + verb)
