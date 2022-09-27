cmds=('python bot.pyz', 'python bot.pyz', 'python bot.pyz', 'python bot.pyz')

# Loop through commands, open terminal, execute command
for i in "${cmds[@]}"
do
    xterm -e "$i && /bin/tcsh" &
done