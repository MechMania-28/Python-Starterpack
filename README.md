# Python-Starterpack
Thank you for coming out to MechMania 28!

This repository contains source code of the Python Starterpack for MechMania 28. You may view or edit any file in this repository.

Make sure you have read [Wiki](https://github.com/MechMania-28/Wiki) for information on the game mechanisms.

## Get Started
Your job is to create a strategy for your bot on where, how and who it should fight. 

To get started, create a class under the strategy package and implement the functions provided by the `strategy` interface. We will also provide an example strategy named `starter_strategy` that will do nothing but being an example.

For each phase in the game, you will be given a `GameState` and your `playerIndex` as input, and you need to submit a decision by returning a value to the corresponding `.._action_decision` methods. After you have done writing down your logic, register your strategy by editing the return values in `StrategyConfig.java`. You could create different strategy implementations and register them for different players.

You'll primarily need to look at the classes within the `game` package to know what are the objects that assembles into in a `GameState` that you will receive from the engine. 

We have provided some useful stuff in the `util` package. `utility` includes some mathematical and random functions. Also, we recommend using `logging.info("your_message")` to debug. It does the same job as `System.out.println` while keeping the output tidy, and prints out more information.

Finally, compile your bot by using `py build.py` and you will find the executable `bot.pyz` under the project root file. Use commands

`py path/to/pyz <player_number>` or the helper scripts `./start-4-python-bots.bat` and `./start-4-python-bots.sh`

to run 4 copies of your bot alongside [Engine](https://github.com/MechMania-28/Engine) to test them out, and use `mm push` (TODO) to submit to the tournament!

Again, make sure you are familiar with the mechanisms of the game and the Strategy class. If you have any questions, do not hesitate to contact us through Discord or in person with any questions!

Good luck!
