electrons = int(input())
shell = []

for current_shell in range(1, electrons + 1):
    max_electrons_for_current_shell = 2 * current_shell ** 2
    if electrons > max_electrons_for_current_shell:
        shell.append(max_electrons_for_current_shell)
        electrons -= max_electrons_for_current_shell
    else:
        shell.append(electrons)
        break

print(shell)