/*Matthew Cerniglia
CSC222 UML Challenge - Complete
This program creates a Warrior and a Mage, gives them abilities and items, and has them fight each other.
Initially, the program creates the characters and prints them to the console.
After that, the characters take turns attacking in rounds until one of them has 0 health.
Finally, the program prints the result of the battle, marking any defeated character.
*/

import java.util.ArrayList;

public class Main {

    //Main creates the characters, runs the battle loop until one has 0 health, and prints the result.
    public static void main(String[] args) {

        //Character variables
        Character will;                       //variable to store the Warrior, used as one of the two fighters
        Character matt;                      //variable to store the Mage, used as the other fighter
        Character[] bothCharacters;         //variable to store both characters, used to print them before and after the battle

        //Battle variables
        int round;                          //variable to store the round number, used to label each round of the battle

        //This section creates the characters
        //First naming the characters
        will = new Warrior("Will", 20);
        matt = new Mage("Matt", 15);

        //Next giving Matt's abilities
        matt.learn(new Ability("Fireball", 30));
        matt.learn(new Ability("Ice Blast", 45));

        //Then giving Will's abilities
        will.learn(new Ability("Power Strike", 25));
        will.learn(new Ability("Swing Excalibur", 50));

        //Lastly their items are added to their inventories.
        will.getInventory().add(new Item("Health Potion", 40));
        matt.getInventory().add(new Item("Elixir", 30));

        //This section prints each character before the battle starts.
        System.out.println("=== CHARACTERS ===");
        bothCharacters = new Character[] { will, matt };
        for (Character c : bothCharacters) {
            System.out.println(c);
        }

        //This section runs the battle. The loop keeps going until either character has 0 health.
        //Polymorphism: both variables are type Character and attack() is called the same way (GeeksforGeeks, 2026b).
        //They differ in their attack methods: the Warrior swings a sword and the Mage casts a spell.
        System.out.println("\n---FIGHT---");
        round = 1;
        while (will.getHealth() > 0 && matt.getHealth() > 0) {
            System.out.println("-- Round " + round + " --");

            //will always goes first, and matt only answers if he is still alive after the hit.
            will.attack(matt);
            if (matt.isAlive()) {
                matt.attack(will);
            }

            //Abilities and items are tried once in round 1 to show them off. will has no Sword, so that use fails.
            //Each step is checked first so a defeated character never acts.
            if (round == 1) {
                if (will.isAlive() && matt.isAlive()) {
                    will.useAbility("Power Strike", matt);
                }
                if (will.isAlive() && matt.isAlive()) {
                    matt.useAbility("Fireball", will);
                }
                if (matt.isAlive()) {
                    matt.useItem("Elixir");
                }
                if (will.isAlive()) {
                    will.useItem("Sword");
                }
            }

            if (round == 2) {
                if (will.isAlive() && matt.isAlive()) {
                    will.useAbility("Swing Excalibur", matt);
                }
                if (will.isAlive() && matt.isAlive()) {
                    matt.useAbility("Fireball", will);
                }
                if (matt.isAlive()) {
                    matt.useItem("Elixir");
                }
                if (will.isAlive()) {
                    will.useItem("Health Potion");
                }
            }

            //This prints the health of both characters at the end of the round so the damage can be followed.
            for (Character c : bothCharacters) {
                System.out.println("   " + c);
            }
            round++;
        }

        //This section prints the final result. A character with 0 health is marked as defeated.
        System.out.println("\n=== RESULT ===");
        for (Character c : bothCharacters) {
            System.out.println(c + (c.isAlive() ? "" : "  [DEFEATED]"));
        }
    }
}

//---------------------------------------------
// CHARACTER DOMAIN
//---------------------------------------------

//Interface: any class that implements this has to have an attack() method.
interface Attackable {
    int attack(Character target);
}

//Abstract class: only Warriors and Mages are created, never a plain Character.
abstract class Character implements Attackable {

    //Encapsulation: these fields are private, so other classes have to use the methods below
    private String name;                       //variable to store the character's name, used when printing messages
    private int health;                        //variable to store the current health, used to decide if the character is alive
    private int maxHealth;                     //variable to store the highest health allowed, used to stop healing from going over it
    private Inventory inventory = new Inventory(3);              //Composition: a Character has an Inventory (3 items max)
    private ArrayList<Ability> abilities = new ArrayList<>();    //list of the abilities this character has learned

    //protected: only subclasses (Warrior, Mage) can call this constructor
    protected Character(String name, int maxHealth) {
        this.name = name;
        this.maxHealth = maxHealth;
        this.health = maxHealth;
    }

    //No body here. Warrior and Mage each override it with their own attack() (GeeksforGeeks, 2026a).
    public abstract int attack(Character target);

    //Each subclass returns its own type name for printing.
    public abstract String getType();

    //Adds an ability to the list of abilities this character knows.
    public void learn(Ability ability) {
        abilities.add(ability);
    }

    //Looks for the ability by name and uses it on the target.
    public void useAbility(String abilityName, Character target) {
        for (Ability a : abilities) {
            if (a.getName().equals(abilityName)) {
                System.out.println(name + " uses " + a.getName() + " on " + target.getName());
                target.takeDamage(a.getDamage());
                return;
            }
        }
        //Prints a message if the ability was never learned.
        System.out.println(name + " doesn't know " + abilityName);
    }

    //Finding the item to heal with in the inventory
    public void useItem(String itemName) {
        Item item;                             //variable to store the item found, used to heal and then remove it

        //Finds the item in the inventory. If it is not found, prints a message and returns.
        item = inventory.find(itemName);
        if (item == null) {
            System.out.println(name + " has no " + itemName);
            return;
        }

        //Prints a message, heals by the item's amount, and removes it from the inventory.
        System.out.println(name + " uses " + item.getName());
        heal(item.getHealAmount());
        inventory.remove(item);
    }

    //Lowers health by the amount, but never below 0.
    public void takeDamage(int amount) {
        health = Math.max(0, health - amount);
    }

    //Raises health by the amount, but never above maxHealth.
    public void heal(int amount) {
        health = Math.min(maxHealth, health + amount);
    }

    //A character is alive as long as its health is above 0.
    public boolean isAlive() { return health > 0; }

    public String getName() { return name; }

    public int getHealth() { return health; }

    public Inventory getInventory() { return inventory; }

    //Prints the character's name, type, health, and inventory size/capacity.
    @Override
    public String toString() {
        return name + " the " + getType() + "  HP " + health + "/" + maxHealth
                + "  Items " + inventory.size() + "/" + inventory.getCapacity();
    }
}

//Inheritance: a Warrior is a Character. Its attack damage comes from strength.
class Warrior extends Character {
    private int strength;                      //variable to store the strength, used as the damage of a sword swing

    //Creates a Warrior with 120 max health and the given strength.
    public Warrior(String name, int strength) {
        super(name, 120);
        this.strength = strength;
    }

    //Swings a sword at the target and returns the damage dealt.
    @Override
    public int attack(Character target) {
        System.out.println(getName() + " swings a sword at " + target.getName());
        target.takeDamage(strength);
        return strength;
    }

    @Override
    public String getType() { return "Warrior"; }
}

//Inheritance: a Mage is a Character. Its attack damage comes from intelligence.
class Mage extends Character {
    private int intelligence;                //variable to store the intelligence, used as the damage of a spell

    //Creates a Mage with 100 max health and the given intelligence.
    public Mage(String name, int intelligence) {
        super(name, 100);
        this.intelligence = intelligence;
    }

    //Casts a spell at the target and returns the damage dealt.
    @Override
    public int attack(Character target) {
        System.out.println(getName() + " casts a spell at " + target.getName());
        target.takeDamage(intelligence);
        return intelligence;
    }

    @Override
    public String getType() { return "Mage"; }
}

//---------------------------------------------
// ABILITY DOMAIN
//---------------------------------------------

//An ability is a named attack that a character uses on a target.
class Ability {
    private String name;                       //variable to store the ability name, used to look the ability up
    private int damage;                        //variable to store the damage, used when the ability hits a target

    public Ability(String name, int damage) {
        this.name = name;
        this.damage = damage;
    }

    public String getName() { return name; }

    public int getDamage() { return damage; }
}

//---------------------------------------------
// ITEM DOMAIN
//---------------------------------------------

//An item is a named healing item that is used once and then removed.
class Item {
    private String name;                       //variable to store the item name, used to look the item up
    private int healAmount;                    //variable to store the heal amount, used when the item is used

    public Item(String name, int healAmount) {
        this.name = name;
        this.healAmount = healAmount;
    }

    public String getName() { return name; }

    public int getHealAmount() { return healAmount; }
}

//---------------------------------------------
// INVENTORY DOMAIN
//---------------------------------------------

//Composition: a Character has an Inventory, and an Inventory has Items.
class Inventory {
    private ArrayList<Item> items = new ArrayList<>();    //list of the items currently held
    private int capacity;                      //variable to store the max number of items, used to block adds when full

    public Inventory(int capacity) {
        this.capacity = capacity;
    }

    //Adds the item if there is room. Returns false if the inventory is full.
    public boolean add(Item item) {
        if (items.size() >= capacity) {
            return false;
        }
        items.add(item);
        return true;
    }

    //Returns the item with the matching name, or null if there is none.
    public Item find(String name) {
        for (Item item : items) {
            if (item.getName().equals(name)) {
                return item;
            }
        }
        return null;
    }

    public void remove(Item item) {
        items.remove(item);
    }

    public int size() { return items.size(); }

    public int getCapacity() { return capacity; }
}

/*References
GeeksforGeeks. (2026a, August 29). Overriding in Java. https://www.geeksforgeeks.org/java/overriding-in-java/

GeeksforGeeks. (2026b, June 15). Dynamic method dispatch or runtime polymorphism in Java. https://www.geeksforgeeks.org/java/dynamic-method-dispatch-runtime-polymorphism-java/
*/
