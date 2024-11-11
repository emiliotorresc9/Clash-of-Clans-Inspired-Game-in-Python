
The village will have the following resources:
* Fruits
* Meat
* Stone
* Gold
* Wood

* Each resource can be obtained in various ways, such as hunting, mining, farming, or simply attacking and stealing resources from other villages.

The player can build the following buildings:
* House: Necessary to generate villagers (you can generate up to 3 villagers per house).
  Materials required to build a house: 19 wood, 12 stone, 1 gold.
  Construction requirement: 20 (the total construction attribute of the population must be at least 20).

* Coliseum: Necessary to generate soldiers (you can generate up to 2 soldiers per coliseum).
  Materials required to build a coliseum: 30 wood, 25 stone, 6 gold.
  Construction requirement: 40 (the total construction attribute of the population must be at least 40).

* Stable: Necessary to generate riders (you can generate up to 1 rider per stable).
  Materials required to build a stable: 50 wood, 40 stone, 10 gold.
  Construction requirement: 60 (the total construction attribute of the population must be at least 60).

Village population types:
* Builder: Ideal for construction.
* Warrior: Ideal for attacks.
* Soldier: An improved version of the warrior (requires a coliseum to generate a soldier).
* Rider: An improved version of the soldier (requires a stable to generate a rider).
* Miner: Ideal for mining.
* Villager: Versatile, suitable for most resource-gathering activities but weak in attacks and construction.
* Hunter: An improved version of the villager for hunting.
* Farmer: An improved version of the villager for farming.
* Lumberjack: An improved version of the villager for chopping wood.

The village interface will include an action buffer (activity record) that displays the actions the user adds before executing them.
The interface has 7 action buttons:
* Hunt: Asks how many members you want to send hunting to gather meat.
* Farm: Asks how many members you want to send farming to gather fruits.
* Mine: Asks how many members you want to send mining to gather gold and stone.
* Chop: Asks how many members you want to send chopping to gather wood.
* Flirt: Asks which member you want to reproduce. Restrictions:

Builder:
  - Only one can be generated at a time.
  - Requires 10 fruits, 2 meat, 1 gold.

Warrior:
 - Maximum of 2 can be generated.
 - Requires 3 fruits, 7 meat, 2 gold.

Soldier:
 - Requires a coliseum.
 - The maximum number that can be generated depends on the number of coliseums.
 - Requires 5 fruits, 10 meat, 3 gold.

Rider:
 - Requires a stable.
 - The maximum number that can be generated depends on the number of stables.
 - Requires 10 fruits, 16 meat, 4 gold.

Miner:
 - Only one can be generated at a time.
 - Requires 7 fruits, 5 meat.

Villager:
 - Requires a house to generate.
 - The maximum number of villagers depends on the number of houses.
 - Requires 3 fruits, 1 meat.

Hunter:
 - Only one can be generated at a time.
 - Requires 10 fruits, 1 gold.

Farmer:
 - Only one can be generated at a time.
 - Requires 5 meat, 1 gold.

Lumberjack:
 - Only one can be generated at a time.
 - Requires 5 fruits, 5 meat, 1 gold.

* Build: Asks what you want to build; house, coliseum, or stable. The code will then check if there are enough materials for construction.
  If so, an image of the building will appear in the village, which the user can place in a valid location.
  Once a location is chosen using the arrow keys, pressing Enter will set the building, which can no longer be edited.
  Note that only one type of building can be constructed at a time (click "play" to build another), and no other actions can be performed while constructing.

* Attack: First asks how many village members you want to send for an attack. The program will simulate an opponent, then show your power level and that of the opponent.
  Based on this information, you can decide to proceed with the attack or retreat. Using the implemented algorithm, decisions will be made based on priorities.

For example, if you have 3 villagers, 3 miners, and choose the "mine" option with 3 people, the algorithm will prioritize sending the 3 miners for the task, not the villagers.
Similarly, in an attack, the strongest troops will always be sent first to maximize power. In general, the algorithm can identify priorities when performing tasks in the village.

* The player will always have a text area informing them of events in the village, as well as action buttons on the screen that, when pressed, add actions to the buffer to be executed once the "execute" button is pressed.

* Likewise, the player or village will constantly be on guard against opponents. An algorithm generates random opponents at an indeterminate time who will frequently try to attack.
  In such cases, there are two options: Defend or Surrender. Each option has consequences. If you surrender, you won’t lose troops but will lose resources based on your opponent's strength, and vice versa. If you choose to defend, you won’t lose resources but will lose part of your population proportional to the opponent's level.
